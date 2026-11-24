"""Synthetic test of lag-1 autocorrelation estimators on annual series with the REAL gap patterns of the P4 stars.
No stellar S values are used (only which calendar years have data), so D04/D11 are not touched. Stationary AR(1),
no cycle, no noise, no detrending: a controlled test of the gap handling, not of the stars.
Methods: oracle (no gaps), naive (ignore gaps), pairs (only consecutive-year pairs), lin_short (linear interpolation of
gaps <= 2 years, longer gaps left empty), lin_all (linear interpolation of every gap). Fixed seeds. Run with `python -I`."""
import csv
import os
import sys
from collections import defaultdict

import numpy as np
from scipy.stats import kendalltau

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, check, write_out

# ---- real year-presence masks ----------------------------------------------------------------
yrs = defaultdict(set)
for ln in open(os.path.join(ROOT, "data", "J_AJ_163_183_table1.tsv"), encoding="utf-8"):
    if ln.startswith("#") or ";" not in ln:
        continue
    p = [x.strip() for x in ln.rstrip("\n").split(";")]
    if p[0].isdigit() and p[4] != "sigma":
        yrs[p[0]].add(int(float(p[2])))
STARS = ["10700", "23249", "182572", "190360", "10476", "152391", "166620", "26965", "4628", "101501"]
MASK = {}
for h in STARS:
    s = sorted(yrs[h])
    MASK[h] = np.array([y in yrs[h] for y in range(s[0], s[-1] + 1)])


def ac1_pairs(x):
    """lag-1 autocorrelation using only pairs of consecutive entries that are both finite."""
    a, b = x[:-1], x[1:]
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 5:
        return np.nan
    m = np.nanmean(x)
    den = np.nansum((x[np.isfinite(x)] - m) ** 2)
    return np.sum((a[ok] - m) * (b[ok] - m)) / den * (np.isfinite(x).sum() / ok.sum())


def interp(x, maxgap):
    y = x.copy()
    idx = np.where(np.isfinite(x))[0]
    for i0, i1 in zip(idx[:-1], idx[1:]):
        g = i1 - i0 - 1
        if 0 < g <= maxgap:
            y[i0 + 1:i1] = np.interp(np.arange(i0 + 1, i1), [i0, i1], [x[i0], x[i1]])
    return y


def estimate(x, method):
    if method == "oracle":
        return ac1_pairs(x)
    if method == "naive":
        v = x[np.isfinite(x)]
        return ac1_pairs(v)
    if method == "pairs":
        return ac1_pairs(x)
    if method == "lin_short":
        return ac1_pairs(interp(x, 2))
    if method == "lin_all":
        return ac1_pairs(interp(x, 10 ** 6))
    raise ValueError(method)


METHODS = ["naive", "pairs", "lin_short", "lin_all"]


def sim_ar1(c_path, rng):
    n = len(c_path)
    x = np.zeros(n)
    x[0] = rng.normal() / np.sqrt(1 - c_path[0] ** 2)
    for t in range(1, n):
        x[t] = c_path[t] * x[t - 1] + rng.normal()
    return x


def rolling(x, method, win_frac=0.5):
    n = len(x)
    w = int(round(n * win_frac))
    out = []
    for s in range(0, n - w + 1):
        seg = x[s:s + w]
        out.append(estimate(seg, method))
    return np.array(out)


# ---- 1. bias of the whole-series estimate, per star and c ----------------------------------
NS = 400
lines = ["BIAS of whole-series lag-1 estimate (mean estimate - true c), 400 simulations per cell",
         "star | n_years | missing | c | oracle | " + " | ".join(METHODS)]
bias_tab = defaultdict(list)
for h in STARS:
    m = MASK[h]
    for c in (0.3, 0.5, 0.7):
        rng = np.random.default_rng(1000 + int(h) % 1000 + int(c * 10))
        est = {k: [] for k in ["oracle"] + METHODS}
        for _ in range(NS):
            full = sim_ar1(np.full(len(m), c), rng)
            obs = np.where(m, full, np.nan)
            est["oracle"].append(estimate(full, "oracle"))
            for k in METHODS:
                est[k].append(estimate(obs, k))
        row = {k: float(np.nanmean(v) - c) for k, v in est.items()}
        for k in row:
            bias_tab[(k, c)].append(row[k])
        lines.append(f"{h} | {len(m)} | {int((~m).sum())} | {c} | " + " | ".join(f"{row[k]:+.3f}" for k in ["oracle"] + METHODS))
lines.append("")
lines.append("MEDIAN OVER THE 10 STARS of the bias:")
for c in (0.3, 0.5, 0.7):
    lines.append(f"c={c}: " + " | ".join(f"{k} {np.median(bias_tab[(k, c)]):+.3f}" for k in ["oracle"] + METHODS))

# ---- 2. rolling window, Kendall tau, null and trend --------------------------------------------
lines += ["", "ROLLING WINDOW (50 % of the series length) Kendall tau of the lag-1 estimate, 150 simulations per cell",
          "null: c constant 0.5; trend: c rises linearly 0.3 -> 0.7. share = fraction of simulations with tau >= 0.3 (descriptive threshold)",
          "star | setting | " + " | ".join(f"{k} mean tau (share>=0.3)" for k in ["oracle"] + METHODS)]
NR = 150
summ = defaultdict(list)
for h in STARS:
    m = MASK[h]
    n = len(m)
    for setting, path in (("null", np.full(n, 0.5)), ("trend", np.linspace(0.3, 0.7, n))):
        rng = np.random.default_rng(5000 + int(h) % 1000 + (0 if setting == "null" else 7))
        taus = {k: [] for k in ["oracle"] + METHODS}
        for _ in range(NR):
            full = sim_ar1(path, rng)
            obs = np.where(m, full, np.nan)
            for k in ["oracle"] + METHODS:
                r = rolling(full if k == "oracle" else obs, k)
                ok = np.isfinite(r)
                taus[k].append(kendalltau(np.arange(len(r))[ok], r[ok])[0] if ok.sum() > 4 else np.nan)
        cells = []
        for k in ["oracle"] + METHODS:
            t = np.array(taus[k])
            cells.append(f"{np.nanmean(t):+.2f} ({np.nanmean(t >= 0.3):.2f})")
            summ[(k, setting)].append((np.nanmean(t), float(np.nanmean(t >= 0.3))))
        lines.append(f"{h} | {setting} | " + " | ".join(cells))
lines.append("")
lines.append("MEDIAN OVER THE 10 STARS (mean tau, share >= 0.3):")
for setting in ("null", "trend"):
    lines.append(f"{setting}: " + " | ".join(
        f"{k} {np.median([a for a, b in summ[(k, setting)]]):+.2f} ({np.median([b for a, b in summ[(k, setting)]]):.2f})"
        for k in ["oracle"] + METHODS))
write_out("15_gap_interpolation_test.txt", "\n".join(lines) + "\n")

check("3.17-01", "synthetic test run on the real gap masks of the 10 stars (no stellar values used)", "10", str(len(STARS)),
      "data/J_AJ_163_183_table1.tsv (year presence only)", info=True)
for c in (0.3, 0.5, 0.7):
    check(f"3.17-02-c{c}", f"median bias of the whole-series lag-1 estimate, c = {c}: oracle | naive | pairs | lin_short | lin_all", "",
          " | ".join(f"{np.median(bias_tab[(k, c)]):+.3f}" for k in ["oracle"] + METHODS), "saidas/15_gap_interpolation_test.txt", info=True)
for setting in ("null", "trend"):
    check(f"3.17-03-{setting}", f"median over stars of mean Kendall tau of the rolling lag-1 estimate ({setting}): oracle | naive | pairs | lin_short | lin_all",
          "", " | ".join(f"{np.median([a for a, b in summ[(k, setting)]]):+.2f}" for k in ["oracle"] + METHODS),
          "saidas/15_gap_interpolation_test.txt", info=True)
