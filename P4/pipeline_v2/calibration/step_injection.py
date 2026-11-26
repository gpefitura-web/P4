"""Exploratory (D126): effect of an instrumental step (e.g. HKP-1 -> HKP-2 in 1977, 11 yr into a 1966-start segment) on the rolling indicators
and on the surrogate test. AR(1) series (coefficient 0.5, unit innovations) of L = 30 yr, no trend. After year 11 a step in level of
d x sd (sd = 1.155, the marginal sd) and/or a multiplicative change g of the noise sd is applied. Rolling indicators, window 50 %, raw series
(config 'none'), Kendall tau; 500 surrogates, 500 series per case; seed sequence 20261129.
Output: results_calibration/step_injection.{csv,txt}.   Usage: python -I step_injection.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE); sys.path.insert(0, PIPE)
QUICK = "--quick" in sys.argv; RESDIR = os.path.join(PIPE, "results_calibration_quick" if QUICK else "results_calibration"); os.makedirs(RESDIR, exist_ok=True)
import numpy as np, pandas as pd
from multiprocessing import Pool
import surrogates as sg

L, K, NS, NREP, SD = 30, 11, (150 if QUICK else 500), (60 if QUICK else 500), 1 / np.sqrt(1 - 0.25)
CASES = [("none", 0.0, 1.0), ("level 0.5sd", 0.5, 1.0), ("level 1sd", 1.0, 1.0), ("level 2sd", 2.0, 1.0),
         ("noise x0.5", 0.0, 0.5), ("noise x1.5", 0.0, 1.5), ("level 1sd + noise x0.5", 1.0, 0.5)]

def job(a):
    name, d, g, rep, seed = a; rng = np.random.default_rng(seed)
    x = np.zeros(L); x[0] = rng.normal() / np.sqrt(0.75)
    for t in range(1, L): x[t] = 0.5 * x[t - 1] + rng.normal()
    x[K:] = x[K:] * g + d * SD
    mod = sg.fit_arma(x); row = dict(case=name, rep=rep); f = np.zeros(L, bool)
    for stat in ("ac1", "var"):
        o = sg.surrogate_test(x, f, 0.5, stat, NS, rng, model=mod)
        row.update({f"tau_{stat}": o["tau"], f"pup_{stat}": o["p_upper"], f"plow_{stat}": o["p_D22"]})
    return row

if __name__ == "__main__":
    tasks = [(n, d, g, r) for n, d, g in CASES for r in range(NREP)]
    seeds = np.random.SeedSequence(20261129).spawn(len(tasks)); tasks = [t + (s,) for t, s in zip(tasks, seeds)]
    with Pool(4) as p: rows = p.map(job, tasks, chunksize=8)
    df = pd.DataFrame(rows); df.to_csv(os.path.join(RESDIR, "step_injection.csv"), index=False)
    out = ["Step injected at year 11 of 30 (AR(1) 0.5, no trend); 500 series/case, 500 surrogates, window 50 %",
           "case | stat | median tau | reject upper | reject lower"]
    for n, _, _ in CASES:
        g = df[df.case == n]
        for stat in ("ac1", "var"):
            out.append(f"{n} | {stat} | {g[f'tau_{stat}'].median():+.2f} | {(g[f'pup_{stat}'] < .05).mean():.3f} | {(g[f'plow_{stat}'] < .05).mean():.3f}")
    txt = "\n".join(out); print(txt); open(os.path.join(RESDIR, "step_injection.txt"), "w").write(txt + "\n")
