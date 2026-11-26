"""Exploratory (D126): fully specified positive controls for the surrogate test, three dynamical models of cycle loss.
Common: complex amplitude z, Re z observed, 20 Euler-Maruyama steps per year, L = 30 yr annual means, period 11 yr (w = 2 pi / 11),
dynamical noise s0 = 0.15 (complex white, per-component sd s0 sqrt(dt/2)), observation noise sd 0.05 added to each annual mean, +1.0 offset,
40 yr burn-in at the initial parameter. The control parameter mu is linear in time between the two values below (annual nodes).
  super : dz = (mu + iw) z - |z|^2 z,               persist mu = 0.3,  lost mu: +0.3 -> -0.3 (bifurcation at t = 15 yr, mid record)
  sub   : dz = (mu + iw) z + |z|^2 z - |z|^4 z,     persist mu = -0.1, lost mu: -0.1 -> -0.5 (fold of the limit cycle at mu = -0.25, t = 11.25 yr)
  mult  : as super but noise sd multiplied by (1 + |z|)
Surrogate test of the pipeline (ARMA by AIC on the series as it is, config 'none', window 50 %, 1000 surrogates); 1000 series per case,
seed sequence 20261127. Output: results_explore/positive_control_full.{csv,txt}.   Usage: python -I positive_control_full.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE); sys.path.insert(0, PIPE)
import numpy as np, pandas as pd
from multiprocessing import Pool
import surrogates as sg

L, SPY, NS, W, S0, OBS, NREP = 30, 20, 1000, 2 * np.pi / 11.0, 0.15, 0.05, 1000
MU = {"super": (0.3, -0.3), "sub": (-0.1, -0.5), "mult": (0.3, -0.3)}
FILLED = np.zeros(L, bool)

def simulate(model, lost, rng):
    m0, m1 = MU[model]; path = np.linspace(m0, m1, L) if lost else np.full(L, m0)
    n = L * SPY; dt = 1.0 / SPY; mu = np.interp(np.arange(n) * dt, np.arange(L) + 0.5, path)
    cub = 1.0 if model == "sub" else -1.0
    def step(z, m):
        g = (m + 1j * W) * z + cub * abs(z) ** 2 * z - (abs(z) ** 4 * z if model == "sub" else 0)
        k = S0 * np.sqrt(dt / 2) * ((1 + abs(z)) if model == "mult" else 1.0)
        return z + g * dt + k * (rng.normal() + 1j * rng.normal())
    z = (1.0 if model == "sub" else 0.5) * np.exp(1j * rng.uniform(0, 2 * np.pi)); out = np.empty(n)
    for _ in range(40 * SPY): z = step(z, mu[0])
    for i in range(n): z = step(z, mu[i]); out[i] = z.real
    return out.reshape(L, SPY).mean(axis=1) + 1.0 + rng.normal(0, OBS, L)

def job(a):
    model, lost, rep, seed = a; rng = np.random.default_rng(seed)
    x = simulate(model, lost, rng); mod = sg.fit_arma(x); row = dict(model=model, lost=lost, rep=rep, amp_first5=float(np.std(x[:5])), amp_last5=float(np.std(x[-5:])))
    for stat in ("ac1", "var"):
        o = sg.surrogate_test(x, FILLED, 0.5, stat, NS, rng, model=mod)
        row.update({f"tau_{stat}": o["tau"], f"plow_{stat}": o["p_D22"], f"pup_{stat}": o["p_upper"]})
    return row

def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    return (pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()

if __name__ == "__main__":
    cases = [(m, l) for m in MU for l in (False, True)]
    tasks = [(m, l, r) for m, l in cases for r in range(NREP)]
    seeds = np.random.SeedSequence(20261127).spawn(len(tasks)); tasks = [t + (s,) for t, s in zip(tasks, seeds)]
    with Pool(4) as p: rows = p.map(job, tasks, chunksize=8)
    df = pd.DataFrame(rows); df.to_csv(os.path.join(PIPE, "results_explore", "positive_control_full.csv"), index=False)
    out = [f"Positive controls, L={L}, obs noise {OBS}, dynamical noise {S0}, {NREP} series/case, {NS} surrogates, window 50 %",
           "model | case | stat | median tau | reject upper | reject lower | sd first5 / last5 (median)"]
    for (m, l), g in df.groupby(["model", "lost"]):
        for stat in ("ac1", "var"):
            out.append(f"{m} | {'lost' if l else 'persist'} | {stat} | {g[f'tau_{stat}'].median():+.2f} | {(g[f'pup_{stat}'] < .05).mean():.3f} | {(g[f'plow_{stat}'] < .05).mean():.3f} | {g.amp_first5.median():.3f} / {g.amp_last5.median():.3f}")
    out += ["", "AUC lost vs persist (score = -lower-tail p / -tau)", "model | stat | AUC(p_low) | AUC(-tau)"]
    for m in MU:
        a = df[(df.model == m) & df.lost]; b = df[(df.model == m) & ~df.lost]
        for stat in ("ac1", "var"):
            out.append(f"{m} | {stat} | {auc(-a[f'plow_{stat}'], -b[f'plow_{stat}']):.3f} | {auc(-a[f'tau_{stat}'], -b[f'tau_{stat}']):.3f}")
    txt = "\n".join(out); print(txt); open(os.path.join(PIPE, "results_explore", "positive_control_full.txt"), "w").write(txt + "\n")
