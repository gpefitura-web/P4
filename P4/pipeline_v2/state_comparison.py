"""Step 6 - H1: state comparison of HD 166620 (Luhn+2022 Table 2): sigma_S per state, conta A (principal) and B,
F-test with raw and noise-corrected variances. Uses the raw (not annual) series (D92, D95)."""
import os
import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
LUHN = os.path.join(os.path.dirname(HERE), "data", "J_ApJ_936_L23_table2.tsv")

# state: (t_from, t_to, instrumental noise fraction of <S>)   Luhn 3.1 p.4 / D45
STATES = {"min1": (1971.0, 1975.0, 0.012), "min2": (1987.0, 1991.0, 0.012), "grand": (2004.0, 9999.0, 0.003)}


def load_luhn():
    rows = []
    with open(LUHN, encoding="utf-8") as fh:
        lines = [ln.rstrip("\n") for ln in fh if ln.strip() and not ln.startswith("#")]
    hdr = [c.strip() for c in lines[0].split(";")]
    for ln in lines[3:]:
        rows.append([c.strip() for c in ln.split(";")])
    d = pd.DataFrame(rows, columns=hdr)
    d["y"] = d.Year.astype(float); d["s"] = d.SHK.astype(float); d["yr"] = np.floor(d.y).astype(int)
    return d


def state_stats(d, name):
    a, b, noise = STATES[name]
    g = d[(d.y >= a) & (d.y < b)]
    m, s1 = g.s.mean(), g.s.std(ddof=1)
    nz = noise * m
    A = float(np.sqrt(s1 ** 2 - nz ** 2))                      # conta A: interval-wide sigma minus noise in quadrature
    ss = g.groupby("yr").s.agg(["count", "mean", "std"]); ss = ss[ss["count"] > 1]
    Bv = float(np.sqrt(np.clip(ss["std"] ** 2 - (noise * ss["mean"]) ** 2, 0, None)).mean())   # conta B: per season, mean
    return dict(n=len(g), mean=float(m), sigma_raw=float(s1), noise=float(nz), sigma_A=A, sigma_B=Bv, n_seasons=len(ss))


def ftest(sa, na, sb, nb):
    f = sa ** 2 / sb ** 2
    p1 = float(stats.f.sf(f, na - 1, nb - 1))
    return dict(F=float(f), p_one=p1, p_two=min(1.0, 2 * p1))


def run_h1():
    d = load_luhn()
    # new_MW rows (1995-2002, grade C) fall outside all three state windows, so they are never used here
    st = {k: state_stats(d, k) for k in STATES}
    out = {"states": st}
    for a, b in (("min1", "grand"), ("min2", "grand")):
        out[f"F_{a}_vs_{b}"] = {
            "raw": ftest(st[a]["sigma_raw"], st[a]["n"], st[b]["sigma_raw"], st[b]["n"]),
            "corrected_A": ftest(st[a]["sigma_A"], st[a]["n"], st[b]["sigma_A"], st[b]["n"]),
            "corrected_B": ftest(st[a]["sigma_B"], st[a]["n"], st[b]["sigma_B"], st[b]["n"])}
    return out
