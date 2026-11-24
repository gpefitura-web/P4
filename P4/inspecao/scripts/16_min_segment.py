"""Minimum segment length for rolling-window lag-1 autocorrelation on annual series (D98 splits stars at gaps >= 3 years).
Synthetic AR(1), no stellar values. (1) precision of the lag-1 estimate vs window length, against the Held & Kleinen
error formula; (2) discrimination (AUC) between 'null' and 'trend' for the rolling-window Kendall tau as a function of
the segment length (window = 50 % of the segment, D20); (3) real segment lengths after D98. Fixed seeds. `python -I`."""
import os
import sys
from collections import defaultdict

import numpy as np
from scipy.stats import kendalltau

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, check, write_out


def ac1(x):
    m = x.mean()
    return np.sum((x[:-1] - m) * (x[1:] - m)) / np.sum((x - m) ** 2)


def sim(path, rng):
    n = len(path)
    x = np.zeros(n)
    x[0] = rng.normal() / np.sqrt(1 - path[0] ** 2)
    for t in range(1, n):
        x[t] = path[t] * x[t - 1] + rng.normal()
    return x


lines = ["1. PRECISION of the lag-1 estimate vs window length w (annual points), 4000 simulations",
         "w | c | SD of estimate | Held&Kleinen sqrt((1-c^2)/w) | bias (mean - c)"]
rng = np.random.default_rng(16)
sd_tab = {}
for c in (0.5, 0.7):
    for w in (6, 8, 10, 12, 15, 18, 20, 24, 30, 40):
        e = np.array([ac1(sim(np.full(w, c), rng)) for _ in range(4000)])
        sd_tab[(w, c)] = (e.std(), np.sqrt((1 - c * c) / w), e.mean() - c)
        lines.append(f"{w} | {c} | {e.std():.3f} | {np.sqrt((1 - c * c) / w):.3f} | {e.mean() - c:+.3f}")


def auc(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return float(np.mean([(x > b).mean() + 0.5 * (x == b).mean() for x in a]))


lines += ["", "2. DISCRIMINATION null (c = 0.5) vs trend (c 0.3 -> 0.7) by Kendall tau of the rolling lag-1 estimate,",
          "window = 50 % of the segment length L (min 5 points), 600 simulations per cell",
          "L | window | n windows | tau null mean | tau null SD | tau trend mean | AUC(trend > null) | share trend tau >= 0.5 | share null tau >= 0.5"]
auc_tab = {}
for L in (10, 12, 15, 18, 20, 24, 30, 40, 50):
    w = max(5, int(round(L * 0.5)))
    nw = L - w + 1
    tn, tt = [], []
    rngn = np.random.default_rng(1600 + L)
    for _ in range(600):
        for path, store in ((np.full(L, 0.5), tn), (np.linspace(0.3, 0.7, L), tt)):
            x = sim(path, rngn)
            r = np.array([ac1(x[s:s + w]) for s in range(nw)])
            store.append(kendalltau(np.arange(nw), r)[0] if nw > 2 else np.nan)
    tn, tt = np.array(tn), np.array(tt)
    a = auc(tt[np.isfinite(tt)], tn[np.isfinite(tn)])
    auc_tab[L] = a
    lines.append(f"{L} | {w} | {nw} | {np.nanmean(tn):+.2f} | {np.nanstd(tn):.2f} | {np.nanmean(tt):+.2f} | {a:.2f} | "
                 f"{np.nanmean(tt >= 0.5):.2f} | {np.nanmean(tn >= 0.5):.2f}")

# ---- 3. real segments after D98 --------------------------------------------------------------------
yrs = defaultdict(set)
for ln in open(os.path.join(ROOT, "data", "J_AJ_163_183_table1.tsv"), encoding="utf-8"):
    if ln.startswith("#") or ";" not in ln:
        continue
    p = [x.strip() for x in ln.rstrip("\n").split(";")]
    if p[0].isdigit() and p[4] != "sigma":
        yrs[p[0]].add(int(float(p[2])))
STARS = ["10700", "23249", "182572", "190360", "10476", "152391", "166620", "26965", "4628", "101501"]
lines += ["", "3. REAL SEGMENTS after D98 (gaps of 1-2 years filled; split at gaps >= 3 years), length in years including filled ones",
          "HD | segments (years) "]
seglen = {}
for h in STARS:
    s = sorted(yrs[h])
    segs, start = [], s[0]
    for a, b in zip(s, s[1:]):
        if b - a - 1 >= 3:
            segs.append(a - start + 1)
            start = b
    segs.append(s[-1] - start + 1)
    seglen[h] = segs
    lines.append(f"{h} | {segs}")
write_out("16_min_segment.txt", "\n".join(lines) + "\n")

for thr in (12, 20, 24, 30):
    n_ok = sum(1 for h in STARS for L in seglen[h] if L >= thr)
    stars_ok = sum(1 for h in STARS if max(seglen[h]) >= thr)
    check(f"3.18-0{(12, 20, 24, 30).index(thr) + 1}", f"segments of the 10 stars with length >= {thr} years | stars with at least one such segment", "",
          f"{n_ok} | {stars_ok}/10", "saidas/16_min_segment.txt", info=True)
check("3.18-05", "AUC(trend > null) of the rolling Kendall tau at L = 20 | 30 | 50", "",
      f"{auc_tab[20]:.2f} | {auc_tab[30]:.2f} | {auc_tab[50]:.2f}", "saidas/16_min_segment.txt", info=True)
check("3.18-06", "SD of the lag-1 estimate at w = 10 | 12 | 24 (c = 0.5)", "",
      f"{sd_tab[(10, 0.5)][0]:.3f} | {sd_tab[(12, 0.5)][0]:.3f} | {sd_tab[(24, 0.5)][0]:.3f}", "saidas/16_min_segment.txt", info=True)
