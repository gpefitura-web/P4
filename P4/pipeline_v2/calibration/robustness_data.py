"""Exploratory (D125): data-treatment robustness of the stellar indicator results, without touching run_all.py.
Variants of the annual series of every eligible star segment, same pipeline and same seed structure as run_all.py (series S only):
  base       : as in run_all.py (check: tau and p must reproduce results/star_results.csv)
  hkp2       : observations before 1977.0 dropped (HKP-2 era only), segments >= 24 yr kept
  no6667     : years 1966 and 1967 set missing (gap rule D98 then re-applied)
  min5       : years with fewer than 5 observations set missing
Output: results_calibration/robustness_data.csv and .txt.   Usage: python -I robustness_data.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE)
QUICK = "--quick" in sys.argv; RESDIR = os.path.join(PIPE, "results_calibration_quick" if QUICK else "results_calibration"); os.makedirs(RESDIR, exist_ok=True)
sys.path.insert(0, PIPE)
import numpy as np, pandas as pd
from multiprocessing import Pool
import p4io, annual, indicators as ind, detrend as dt, surrogates as sg

BASE_SEED, NSURR, MIN_SEG = 20261124, (200 if QUICK else 1000), 24
VARIANTS = ("base", "hkp2", "no6667", "min5")

def ann_variant(obs, sun, v):
    o = obs
    if v == "hkp2": o = obs[obs.t >= 1977.0]
    a = annual.annual_means(o, None if sun else "MW")
    if v == "no6667": a = a[~a.year.isin([1966, 1967])]
    if v == "min5": a = a[a.n >= 5]
    return a

def work(args):
    ci, r = args
    sun = r["serie_fonte"] == "Egeland2017_T4"
    if not sun and r["indicador_elegivel_D100"] != "sim": return []
    obs = p4io.load_star(r["HD"], pd.Series(r)); rows = []
    for v in VARIANTS:
        ann = ann_variant(obs, sun, v)
        if len(ann) < 3: continue
        for si, seg in enumerate(annual.segments(ann)):
            L = len(seg["years"])
            if L < MIN_SEG: continue
            # base: reuse the same seed index as run_all (segment index si, series S ki=0)
            for gi, sigma in enumerate(dt.CONFIGS):
                res = dt.residual(seg["S"], sigma)
                rng = np.random.default_rng([BASE_SEED, ci, si, 0, gi])
                model = sg.fit_arma(res)
                Ss = sg.apply_mask(sg.simulate(model, L, NSURR, rng), seg["filled"])
                for frac in ind.FRACS:
                    w = ind.window_size(L, frac)
                    for stat in ("ac1", "var"):
                        tau = float(sg.tau_rows(sg.rolling_stat(res[None, :], w, stat))[0])
                        ts = sg.tau_rows(sg.rolling_stat(Ss, w, stat))
                        rows.append(dict(variant=v, HD=r["HD"], seg_year0=seg["year0"], L=L, config=dt.label(sigma), frac=frac, stat=stat,
                                         tau=tau, p_D22=(np.sum(ts <= tau) + 1) / (NSURR + 1), p_upper=(np.sum(ts >= tau) + 1) / (NSURR + 1)))
    return rows

if __name__ == "__main__":
    cat = p4io.load_catalog()
    with Pool(4) as p: res = p.map(work, [(ci, r.to_dict()) for ci, r in cat.iterrows()])
    df = pd.DataFrame([x for rr in res for x in rr]); df.to_csv(os.path.join(RESDIR, "robustness_data.csv"), index=False)
    ref = pd.read_csv(os.path.join(PIPE, "results", "star_results.csv")); ref = ref[ref.series == "S"]
    out = []
    b = df[df.variant == "base"].merge(ref, on=["HD", "seg_year0", "config", "frac", "stat"], suffixes=("", "_ref"))
    out.append(f"check base vs star_results.csv: cells {len(b)}, max |dtau| {np.abs(b.tau - b.tau_ref).max():.2e}, max |dp_upper| {np.abs(b.p_upper - b.p_upper_ref).max():.3f}")
    out.append("variant | segments | cells | tau median ac1 | tau median var | p_upper<0.05 | p_lower<0.05 | median |dtau| vs base | sign flips vs base")
    base = df[df.variant == "base"].set_index(["HD", "seg_year0", "config", "frac", "stat"])
    for v in VARIANTS:
        g = df[df.variant == v]; nseg = g.groupby(["HD", "seg_year0"]).ngroups
        j = g.set_index(["HD", "seg_year0", "config", "frac", "stat"]).join(base[["tau"]], rsuffix="_b", how="inner")
        d = (j.tau - j.tau_b).abs().median() if v != "base" else 0.0
        fl = int((np.sign(j.tau) != np.sign(j.tau_b)).sum()) if v != "base" else 0
        out.append(f"{v} | {nseg} | {len(g)} | {g[g.stat=='ac1'].tau.median():+.3f} | {g[g.stat=='var'].tau.median():+.3f} | {(g.p_upper<.05).sum()} | {(g.p_D22<.05).sum()} | {d:.3f} | {fl}/{len(j)}")
    # exclude the three segments with > 2 interpolated years
    ex = df[(df.variant == "base") & ~df.HD.isin(["182572", "190360", "217014"])]
    out.append(f"base without 182572/190360/217014 | {ex.groupby(['HD','seg_year0']).ngroups} | {len(ex)} | {ex[ex.stat=='ac1'].tau.median():+.3f} | {ex[ex.stat=='var'].tau.median():+.3f} | {(ex.p_upper<.05).sum()} | {(ex.p_D22<.05).sum()} | - | -")
    txt = "\n".join(out); print(txt); open(os.path.join(RESDIR, "robustness_data.txt"), "w").write(txt + "\n")
