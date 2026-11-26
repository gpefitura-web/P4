"""Positive control on a dynamical model of cycle loss (D122). A noisy supercritical Hopf oscillator (Stuart-Landau form),
dz = (mu(t) + i w) z dt - |z|^2 z dt + s dW (complex white noise), w = 2 pi / 11 per year, s = 0.15, Euler-Maruyama with 20 steps per year.
The "S index" is the annual mean of Re z plus a constant. Two cases of 30 years: the cycle persists (mu = 0.3 throughout) and the cycle is
lost (mu falls linearly from +0.3 to -0.3, crossing the bifurcation in the middle of the record). The whole surrogate test of the
pipeline (original series, window 50 %, 1000 surrogates) is applied to the rolling lag-1 autocorrelation and the variance; the rejection
rates of the upper-tail p (the direction assumed in the manuscript) and of the lower-tail p are reported, with the median Kendall tau.
200 series per case, seed 9090. Illustration of the sign of the indicators in one model, not a calibration to any star.
Output: results/positive_control.txt.   Usage: python -I positive_control.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import surrogates as sg

HERE = os.path.dirname(os.path.abspath(__file__))
L, NREP, NS, SPY, W, S0 = 30, 200, 1000, 20, 2 * np.pi / 11.0, 0.15
rng = np.random.default_rng(9090)
filled = np.zeros(L, bool)


def simulate(mu_path):
    n = L * SPY; dt = 1.0 / SPY
    mu = np.interp(np.arange(n) * dt, np.arange(L) + 0.5, mu_path)
    z = 0.5 * np.exp(1j * rng.uniform(0, 2 * np.pi)); out = np.empty(n)
    for _ in range(40 * SPY):                                  # burn-in at the starting mu
        z += ((mu[0] + 1j * W) * z - abs(z) ** 2 * z) * dt + S0 * np.sqrt(dt) * (rng.normal() + 1j * rng.normal()) / np.sqrt(2)
    for i in range(n):
        z += ((mu[i] + 1j * W) * z - abs(z) ** 2 * z) * dt + S0 * np.sqrt(dt) * (rng.normal() + 1j * rng.normal()) / np.sqrt(2)
        out[i] = z.real
    return out.reshape(L, SPY).mean(axis=1) + 1.0


rows = []
for name, mu_path in (("cycle persists", np.full(L, 0.3)), ("cycle lost", np.linspace(0.3, -0.3, L))):
    res = {"ac1": [], "var": []}
    for _ in range(NREP):
        x = simulate(mu_path)
        for stat in ("ac1", "var"):
            res[stat].append(sg.surrogate_test(x, filled, 0.5, stat, NS, rng))
    for stat in ("ac1", "var"):
        up = np.mean([r["p_upper"] < 0.05 for r in res[stat]]); lo = np.mean([r["p_D22"] < 0.05 for r in res[stat]])
        rows.append(f"{name} | {stat} | {np.median([r['tau'] for r in res[stat]]):+.2f} | {up:.3f} | {lo:.3f}")
out = [f"Positive control: noisy supercritical Hopf oscillator, L = {L} yr, period 11 yr, noise {S0:g}; {NREP} series per case, {NS} surrogates; window 50 %",
       "case | indicator | median tau | rejection upper tail | rejection lower tail"] + rows
open(os.path.join(HERE, "results", "positive_control.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
