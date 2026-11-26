"""Exploratory (D125): two-sided power and AUC of the surrogate test, larger samples than the v1 positive control.
Cases (L = 30 yr, window 50 %, 1000 surrogates, seed 20261126):
  hopf_persist / hopf_lost : noisy supercritical Hopf oscillator as in positive_control.py, grid of period P and dynamical noise s0
  ar1_null / ar1_trend     : AR(1) without cycle, constant 0.5 or rising 0.3 -> 0.7 (true critical slowing down, no cycle)
Per series: tau and p_D22 (lower tail) and p_upper for ac1 and var, one ARMA fit shared by both indicators.
AUC: probability that a 'lost' series has a smaller lower-tail p (resp. larger tau) than a 'persist' series (ties = 1/2).
Usage: python -I power_bilateral.py   Output: results_explore/power_bilateral.{csv,txt}"""
import os, sys, warnings, itertools
warnings.filterwarnings("ignore")
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE)
sys.path.insert(0, PIPE)
import numpy as np, pandas as pd
from multiprocessing import Pool
import surrogates as sg

L, SPY, NS = 30, 20, 1000
FILLED = np.zeros(L, bool)

def hopf(mu_path, P, s0, rng):
    w = 2 * np.pi / P; n = L * SPY; dt = 1.0 / SPY
    mu = np.interp(np.arange(n) * dt, np.arange(L) + 0.5, mu_path)
    z = 0.5 * np.exp(1j * rng.uniform(0, 2 * np.pi)); out = np.empty(n); k = s0 * np.sqrt(dt / 2)
    for _ in range(40 * SPY):
        z += ((mu[0] + 1j * w) * z - abs(z) ** 2 * z) * dt + k * (rng.normal() + 1j * rng.normal())
    for i in range(n):
        z += ((mu[i] + 1j * w) * z - abs(z) ** 2 * z) * dt + k * (rng.normal() + 1j * rng.normal())
        out[i] = z.real
    return out.reshape(L, SPY).mean(axis=1) + 1.0

def ar1(path, rng):
    x = np.zeros(L); x[0] = rng.normal() / np.sqrt(1 - path[0] ** 2)
    for t in range(1, L): x[t] = path[t] * x[t - 1] + rng.normal()
    return x

def job(a):
    case, P, s0, rep, seed = a
    rng = np.random.default_rng(seed)
    if case == "hopf_persist": x = hopf(np.full(L, 0.3), P, s0, rng)
    elif case == "hopf_lost": x = hopf(np.linspace(0.3, -0.3, L), P, s0, rng)
    elif case == "ar1_null": x = ar1(np.full(L, 0.5), rng)
    else: x = ar1(np.linspace(0.3, 0.7, L), rng)
    mod = sg.fit_arma(x); row = dict(case=case, P=P, s0=s0, rep=rep)
    for stat in ("ac1", "var"):
        o = sg.surrogate_test(x, FILLED, 0.5, stat, NS, rng, model=mod)
        row.update({f"tau_{stat}": o["tau"], f"plow_{stat}": o["p_D22"], f"pup_{stat}": o["p_upper"]})
    return row

def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    gt = (pos[:, None] > neg[None, :]).mean(); eq = (pos[:, None] == neg[None, :]).mean()
    return gt + 0.5 * eq

if __name__ == "__main__":
    ss = np.random.SeedSequence(20261126); tasks = []
    grid = list(itertools.product((8.0, 11.0, 15.0), (0.10, 0.15, 0.30)))
    for P, s0 in grid:
        n = 1000 if (P, s0) == (11.0, 0.15) else 300
        for case in ("hopf_persist", "hopf_lost"):
            tasks += [(case, P, s0, r) for r in range(n)]
    tasks += [(c, 0.0, 0.0, r) for c in ("ar1_null", "ar1_trend") for r in range(1000)]
    seeds = ss.spawn(len(tasks)); tasks = [t + (s,) for t, s in zip(tasks, seeds)]
    with Pool(4) as p: rows = p.map(job, tasks, chunksize=8)
    df = pd.DataFrame(rows); df.to_csv(os.path.join(PIPE, "results_explore", "power_bilateral.csv"), index=False)
    out = ["Two-sided rejection (p < 0.05) and AUC; L=30, window 50 %, 1000 surrogates. n per cell in column n.",
           "case | P | s0 | n | stat | median tau | reject upper | reject lower"]
    for (case, P, s0), g in df.groupby(["case", "P", "s0"]):
        for stat in ("ac1", "var"):
            out.append(f"{case} | {P:g} | {s0:g} | {len(g)} | {stat} | {g[f'tau_{stat}'].median():+.2f} | {(g[f'pup_{stat}'] < .05).mean():.3f} | {(g[f'plow_{stat}'] < .05).mean():.3f}")
    out += ["", "AUC lost vs persist (score = -lower-tail p, and score = -tau)", "P | s0 | stat | AUC(p_low) | AUC(-tau)"]
    for P, s0 in grid:
        a = df[(df.case == "hopf_lost") & (df.P == P) & (df.s0 == s0)]; b = df[(df.case == "hopf_persist") & (df.P == P) & (df.s0 == s0)]
        for stat in ("ac1", "var"):
            out.append(f"{P:g} | {s0:g} | {stat} | {auc(-a[f'plow_{stat}'], -b[f'plow_{stat}']):.3f} | {auc(-a[f'tau_{stat}'], -b[f'tau_{stat}']):.3f}")
    a = df[df.case == "ar1_trend"]; b = df[df.case == "ar1_null"]
    out += ["", "AUC ar1_trend vs ar1_null (score = -upper-tail p)"]
    for stat in ("ac1", "var"): out.append(f"{stat} | {auc(-a[f'pup_{stat}'], -b[f'pup_{stat}']):.3f}")
    txt = "\n".join(out); print(txt); open(os.path.join(PIPE, "results_explore", "power_bilateral.txt"), "w").write(txt + "\n")
