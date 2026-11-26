"""Exploratory (D126): design power curve of the surrogate test for TRUE critical slowing down (AR(1) coefficient rising 0.3 -> 0.7),
against the AR(1) null (0.5 constant), as a function of record length L (years, annual means), observation-noise ratio r (white noise
sd = r x sd of the AR(1) process) and the presence of an 11-yr cycle (amplitude 1.5 in units of the innovation sd). Window 50 %, 500
surrogates, 200 series per cell, config 'none', ARMA by AIC; seed sequence 20261128. Score for AUC = -upper-tail p.
Output: results_calibration/power_design.{csv,txt}.   Usage: python -I power_design.py"""
import os, sys, warnings, itertools
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE); sys.path.insert(0, PIPE)
QUICK = "--quick" in sys.argv; RESDIR = os.path.join(PIPE, "results_calibration_quick" if QUICK else "results_calibration"); os.makedirs(RESDIR, exist_ok=True)
import numpy as np, pandas as pd
from multiprocessing import Pool
import surrogates as sg

NS, NREP, A = (150 if QUICK else 500), (30 if QUICK else 200), 1.5

def make(L, trend, r, cyc, rng):
    path = np.linspace(0.3, 0.7, L) if trend else np.full(L, 0.5)
    x = np.zeros(L); x[0] = rng.normal() / np.sqrt(1 - path[0] ** 2)
    for t in range(1, L): x[t] = path[t] * x[t - 1] + rng.normal()
    sd = 1 / np.sqrt(1 - 0.5 ** 2)
    x = x + rng.normal(0, r * sd, L)
    if cyc: x = x + A * np.sin(2 * np.pi * np.arange(L) / 11.0 + rng.uniform(0, 2 * np.pi))
    return x

def job(a):
    L, r, cyc, trend, rep, seed = a; rng = np.random.default_rng(seed)
    x = make(L, trend, r, cyc, rng); mod = sg.fit_arma(x); row = dict(L=L, r=r, cyc=cyc, trend=trend, rep=rep)
    filled = np.zeros(L, bool)
    for stat in ("ac1", "var"):
        o = sg.surrogate_test(x, filled, 0.5, stat, NS, rng, model=mod); row[f"pup_{stat}"] = o["p_upper"]
    return row

def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    return (pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()

if __name__ == "__main__":
    grid = list(itertools.product((30, 50, 100, 200), (0.0, 0.5, 1.0), (False, True), (False, True)))
    tasks = [(L, r, c, t, k) for L, r, c, t in grid for k in range(NREP)]
    seeds = np.random.SeedSequence(20261128).spawn(len(tasks)); tasks = [t + (s,) for t, s in zip(tasks, seeds)]
    with Pool(4) as p: rows = p.map(job, tasks, chunksize=8)
    df = pd.DataFrame(rows); df.to_csv(os.path.join(RESDIR, "power_design.csv"), index=False)
    out = ["Power for true CSD (AR(1) 0.3 -> 0.7) vs null; 200 series/cell, 500 surrogates; reject = p_upper < 0.05",
           "L | obs noise ratio | cycle | stat | size (null) | power (trend) | AUC"]
    for L, r, c in itertools.product((30, 50, 100, 200), (0.0, 0.5, 1.0), (False, True)):
        g = df[(df.L == L) & (df.r == r) & (df.cyc == c)]
        for stat in ("ac1", "var"):
            n0 = g[~g.trend][f"pup_{stat}"]; n1 = g[g.trend][f"pup_{stat}"]
            out.append(f"{L} | {r:g} | {'yes' if c else 'no'} | {stat} | {(n0 < .05).mean():.3f} | {(n1 < .05).mean():.3f} | {auc(-n1, -n0):.3f}")
    txt = "\n".join(out); print(txt); open(os.path.join(RESDIR, "power_design.txt"), "w").write(txt + "\n")
