"""Support for RECOMENDACOES_PENDENTES.md. Read-only; synthetic parts use no stellar values. Run with `python -I`.
(1) Binarity rule: seven non-standard Flat/Flat? minus the 12 stars of B95 Appendix B -> five clean Flat?
(2) Single-instrument-era segment lengths after D98 (gaps 1-2 years filled, split at >= 3 years) for the 10 stars.
(3) Detrending bandwidth (Q3): AR(1) noise + 10-year sinusoid, Gaussian smoothing sigma 1, 2, 3, 5 years."""
import os
import sys
from collections import defaultdict

import numpy as np
from scipy.ndimage import gaussian_filter1d
from scipy.stats import kendalltau

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, check, write_out

# ---- (1) binarity rule -------------------------------------------------------------------------
SEVEN = {"10700", "23249", "43587", "158614", "178428", "182572", "190360"}   # 03h_crossmatch_groups.txt
APPB = {"3443", "39587", "76572", "81809", "88355", "114378", "124570", "137107", "141004", "156026", "158614", "178428"}
five = sorted(SEVEN - APPB, key=int)
check("3.19-01", "Flat/Flat? non-standard (D13 alone) minus the 12 stars of B95 Appendix B (audit/A1_baliunas.md §2.5)",
      "10700,23249,43587,182572,190360", ",".join(five), "03h_crossmatch_groups.txt; audit/A1_baliunas.md §2.5")

# ---- (2) single-era segments ---------------------------------------------------------------------
era = defaultdict(lambda: defaultdict(set))
for ln in open(os.path.join(ROOT, "data", "J_AJ_163_183_table1.tsv"), encoding="utf-8"):
    if ln.startswith("#") or ";" not in ln:
        continue
    p = [x.strip() for x in ln.rstrip("\n").split(";")]
    if p[0].isdigit() and p[4] != "sigma":
        era[p[0]]["MW" if p[3].startswith("HKP") else "Keck"].add(int(float(p[2])))
STARS = ["10700", "23249", "182572", "190360", "10476", "152391", "166620", "26965", "4628", "101501"]


def segments(ys):
    s = sorted(ys)
    segs, start = [], s[0]
    for a, b in zip(s, s[1:]):
        if b - a - 1 >= 3:
            segs.append(a - start + 1)
            start = b
    segs.append(s[-1] - start + 1)
    return segs


lines = ["(2) segments (years) by instrument era after D98: HD | Mount Wilson (HKP-1/2) | Keck (HIRES-1/2)"]
n_mw24 = n_keck24 = 0
for h in STARS:
    mw = segments(era[h]["MW"]) if era[h]["MW"] else []
    kk = segments(era[h]["Keck"]) if era[h]["Keck"] else []
    n_mw24 += any(x >= 24 for x in mw)
    n_keck24 += any(x >= 24 for x in kk)
    lines.append(f"{h} | {mw} | {kk}")
check("3.19-02", "of the 10 stars: with a single-era (Mount Wilson) segment >= 24 years | with a Keck-era segment >= 24 years", "",
      f"{n_mw24}/10 | {n_keck24}/10", "saidas/17_recommendation_support.txt", info=True)

# ---- (3) detrending bandwidth --------------------------------------------------------------------
def ac1(x):
    m = x.mean()
    return np.sum((x[:-1] - m) * (x[1:] - m)) / np.sum((x - m) ** 2)


def ar1_noise(n, c, rng):
    x = np.zeros(n)
    x[0] = rng.normal() / np.sqrt(1 - c * c)
    for t in range(1, n):
        x[t] = c * x[t - 1] + rng.normal()
    return x


lines += ["", "(3) DETRENDING: x = 3*SD(noise)*sin(2 pi t/10) + AR(1) noise (c = 0.5); residual = x - Gaussian smooth(x, sigma).",
          "500 simulations; reference = AR(1) of the true noise. L = 30 and 54 years; rolling window 50 %",
          "L | sigma (yr) | mean residual AC1 | reference AC1 | rolling tau mean (null) | tau SD"]
def harm(x, period):
    t = np.arange(len(x))
    A = np.column_stack([np.ones(len(x)), t, np.sin(2 * np.pi * t / period), np.cos(2 * np.pi * t / period)])
    beta, *_ = np.linalg.lstsq(A, x, rcond=None)
    return x - A @ beta


rows3 = {}
for L in (30, 54):
    for sig in (None, 1, 2, 3, 5, "harm10", "harm12"):
        rng = np.random.default_rng(1700 + L)
        t = np.arange(L)
        res, ref, taus = [], [], []
        for _ in range(500):
            noise = ar1_noise(L, 0.5, rng)
            x = 3 * noise.std() * np.sin(2 * np.pi * t / 10) + noise
            if sig is None:
                r = x
            elif sig == "harm10":
                r = harm(x, 10.0)          # fitted cycle with the true period
            elif sig == "harm12":
                r = harm(x, 12.0)          # fitted cycle with a period 20 % too long
            else:
                r = x - gaussian_filter1d(x, sig, mode="nearest")
            res.append(ac1(r))
            ref.append(ac1(noise))
            w = L // 2
            roll = np.array([ac1(r[s:s + w]) for s in range(L - w + 1)])
            taus.append(kendalltau(np.arange(len(roll)), roll)[0])
        rows3[(L, sig)] = (np.mean(res), np.mean(ref), np.nanmean(taus), np.nanstd(taus))
        lines.append(f"{L} | {'none' if sig is None else sig} | {np.mean(res):+.2f} | {np.mean(ref):+.2f} | {np.nanmean(taus):+.2f} | {np.nanstd(taus):.2f}")
write_out("17_recommendation_support.txt", "\n".join(lines) + "\n")
check("3.19-03", "residual lag-1 AC at L = 54: none | sigma 1 | 2 | 3 | 5 years | fitted cycle P=10 (true) | fitted cycle P=12 (20 % off); reference 0.44", "",
      " | ".join(f"{rows3[(54, s)][0]:+.2f}" for s in (None, 1, 2, 3, 5, "harm10", "harm12")), "saidas/17_recommendation_support.txt", info=True)
check("3.19-04", "rolling tau mean under the null at L = 54: none | sigma 1 | 2 | 3 | 5 | harm10 | harm12", "",
      " | ".join(f"{rows3[(54, s)][2]:+.2f}" for s in (None, 1, 2, 3, 5, "harm10", "harm12")), "saidas/17_recommendation_support.txt", info=True)

# ---- (3b) power of tau by detrending: trend c 0.3 -> 0.7 versus null c 0.5, L = 54 ----------------------
def auc(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return float(np.mean([(x > b).mean() + 0.5 * (x == b).mean() for x in a]))


L = 54
w = L // 2
t = np.arange(L)
lines2 = ["", "(3b) POWER at L = 54: AUC(trend > null) of the rolling tau, by detrending (500 simulations each)"]
auc_by = {}
for sig in (None, 1, 2, 3, 5, "harm10", "harm12"):
    out = {}
    for name, path in (("null", np.full(L, 0.5)), ("trend", np.linspace(0.3, 0.7, L))):
        rng = np.random.default_rng(1800 + (0 if name == "null" else 1))
        taus = []
        for _ in range(500):
            noise = np.zeros(L)
            noise[0] = rng.normal() / np.sqrt(1 - path[0] ** 2)
            for k in range(1, L):
                noise[k] = path[k] * noise[k - 1] + rng.normal()
            x = 3 * noise.std() * np.sin(2 * np.pi * t / 10) + noise
            if sig is None:
                r = x
            elif sig == "harm10":
                r = harm(x, 10.0)
            elif sig == "harm12":
                r = harm(x, 12.0)
            else:
                r = x - gaussian_filter1d(x, sig, mode="nearest")
            roll = np.array([ac1(r[s:s + w]) for s in range(L - w + 1)])
            taus.append(kendalltau(np.arange(len(roll)), roll)[0])
        out[name] = np.array(taus)
    auc_by[sig] = auc(out["trend"], out["null"])
    lines2.append(f"{'none' if sig is None else sig} | AUC {auc_by[sig]:.2f}")
with open(os.path.join(ROOT, "inspecao", "saidas", "17_recommendation_support.txt"), "a", encoding="utf-8") as fh:
    fh.write("\n".join(lines2) + "\n")
check("3.19-05", "AUC(trend > null) at L = 54 by detrending: none | sigma 1 | 2 | 3 | 5 | harm10 | harm12", "",
      " | ".join(f"{auc_by[s]:.2f}" for s in (None, 1, 2, 3, 5, "harm10", "harm12")), "saidas/17_recommendation_support.txt", info=True)
