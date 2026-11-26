"""Exploratory (D126): real-data check of the surrogate test on sunspot group numbers (Vaquero+2016, v1.12), around the Dalton Minimum.
Declared before running the indicators (only the coverage table was looked at, to choose the segments):
 - daily value = mean of GROUPS over the stations of that day (STATION > 0, GROUPS >= 0); annual value = mean of the daily values;
 - a year is usable if it has >= 50 days with data; gaps of 1-2 unusable years are filled linearly and flagged, gaps >= 3 split (rule D98);
 - the resulting long segment 1795-2010 is cut into six non-overlapping 36-yr blocks: 1795-1830 (contains the Dalton Minimum, the
   amplitude of the annual maxima falls from ~4.8 in 1788 to ~3.1 in 1801 and ~2.4 in 1816) and five later blocks as a reference;
 - the pipeline test as in run_all.py (four detrending configurations, window 50 %, ARMA surrogates by AIC with the gap mask, 1000
   surrogates, seed 20261130), on the annual mean and on its square root (variance-stabilising for counts).
One real event only: this is an illustration of the sign and size of the indicators, not a statistical test of CSD.
Output: results_explore/dalton_control.{csv,txt}.   Usage: python -I dalton_control.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE); sys.path.insert(0, PIPE)
import numpy as np, pandas as pd
import annual, detrend as dt, indicators as ind, surrogates as sg

NS, SEED = 1000, 20261130
d = pd.read_csv(os.path.join(os.path.dirname(PIPE), "data", "Vaquero2016_GNobservations_JV_V1-12.csv"), comment="%")
g = d[(d.GROUPS >= 0) & (d.STATION > 0)]
day = g.groupby(["YEAR", "MONTH", "DAY"]).GROUPS.mean().reset_index()
ann = day.groupby("YEAR").GROUPS.agg(["mean", "size"]).reset_index().rename(columns={"YEAR": "year", "mean": "S", "size": "n"})
ann = ann[(ann.year >= 1700) & (ann.n >= 50)]
segs = [s for s in annual.segments(ann[["year", "S", "n"]]) if len(s["years"]) >= 36]
out = ["Usable segments (>= 50 days/yr, gap rule D98, length >= 36 yr):"]
for s in segs: out.append(f"  {s['years'][0]}-{s['years'][-1]}: L={len(s['years'])}, filled years={s['filled'].sum()}")
long = max(segs, key=lambda s: len(s["years"])); y0 = long["years"][0]
rows = []
BLOCKS = [(1795 + 36 * i, 1795 + 36 * i + 35) for i in range(6)]
rng_seq = np.random.SeedSequence(SEED).spawn(len(BLOCKS) * 2 * 4)
k = 0
for (a, b) in BLOCKS:
    m = (long["years"] >= a) & (long["years"] <= b)
    if m.sum() < 36 or a < y0: out.append(f"block {a}-{b} not available"); continue
    S, fl = long["S"][m], long["filled"][m]
    for tname, x in (("raw", S), ("sqrt", np.sqrt(S))):
        for gi, sigma in enumerate(dt.CONFIGS):
            res = dt.residual(x, sigma); rng = np.random.default_rng(rng_seq[k]); k += 1
            model = sg.fit_arma(res); Ss = sg.apply_mask(sg.simulate(model, len(x), NS, rng), fl); w = ind.window_size(len(x), 0.5)
            for stat in ("ac1", "var"):
                tau = float(sg.tau_rows(sg.rolling_stat(res[None, :], w, stat))[0]); ts = sg.tau_rows(sg.rolling_stat(Ss, w, stat))
                rows.append(dict(block=f"{a}-{b}", transform=tname, config=dt.label(sigma), stat=stat, tau=tau,
                                 p_lower=(np.sum(ts <= tau) + 1) / (NS + 1), p_upper=(np.sum(ts >= tau) + 1) / (NS + 1), arma=str(model["order"]), filled=int(fl.sum())))
df = pd.DataFrame(rows); df.to_csv(os.path.join(PIPE, "results_explore", "dalton_control.csv"), index=False)
out += ["", "Annual maxima of the long segment by Schwabe cycle (year of max: value), for the amplitude record:"]
yrs, S = long["years"], long["S"]
mx = [(int(yrs[i]), round(float(S[i]), 2)) for i in range(1, len(S) - 1) if S[i] >= S[i - 1] and S[i] >= S[i + 1] and S[i] > 2.0]
out.append("  " + ", ".join(f"{a}: {b}" for a, b in mx))
out += ["", "block | transform | stat | tau (4 configs: none, s1, s3, s5) | p_lower (4 configs) | p_upper (4 configs)"]
for (blk, tr, st), q in df.groupby(["block", "transform", "stat"], sort=False):
    out.append(f"{blk} | {tr} | {st} | " + " ".join(f"{v:+.2f}" for v in q.tau) + " | " + " ".join(f"{v:.3f}" for v in q.p_lower) + " | " + " ".join(f"{v:.3f}" for v in q.p_upper))
txt = "\n".join(out); print(txt); open(os.path.join(PIPE, "results_explore", "dalton_control.txt"), "w").write(txt + "\n")
