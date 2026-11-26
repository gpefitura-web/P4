"""Exploratory (D126): one example series per positive-control model, persisting and losing the cycle, with the rolling indicators of the
pipeline (window 50 % of L), for Figure 1 of the manuscript. Same simulator as positive_control_full.py; seed sequence 20261201.
Output: results_calibration/example_series.csv.   Usage: python -I example_series.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, PIPE)
import numpy as np, pandas as pd
import positive_control_full as pc
import surrogates as sg

seeds = np.random.SeedSequence(20261201).spawn(6); k = 0; rows = []
for model in ("super", "sub", "mult"):
    for lost in (False, True):
        rng = np.random.default_rng(seeds[k]); k += 1
        x = pc.simulate(model, lost, rng); w = int(round(0.5 * pc.L))
        ac = sg.rolling_stat(x[None, :], w, "ac1")[0]; var = sg.rolling_stat(x[None, :], w, "var")[0]
        for t in range(pc.L):
            j = t - (w - 1)
            rows.append(dict(model=model, lost=lost, year=t + 1, S=x[t], window_end=bool(j >= 0), ac1=ac[j] if j >= 0 else np.nan, var=var[j] if j >= 0 else np.nan))
pd.DataFrame(rows).to_csv(os.path.join(PIPE, "results_calibration", "example_series.csv"), index=False)
print(len(rows), "rows")
