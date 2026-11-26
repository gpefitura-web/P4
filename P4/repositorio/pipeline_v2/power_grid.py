"""Power of the whole surrogate test over cycle period and amplitude (D122; extends power_cycle.py, which uses one period and one amplitude).
Series of L = 30 years with three interpolated points, window 50 %, rolling lag-1 autocorrelation of the original series, upper-tail p at 5 %.
Noise AR(1), unit innovations, coefficient constant at 0.5 (null) or rising from 0.3 to 0.7 (trend); cycle A sin(2 pi t / P + phase), random phase.
Grid: P in 8, 11, 16 years and A in 0.75, 1.5, 3.0 (A = 0 is the no-cycle case). 150 series per cell, 500 surrogates, seed 7171.
Output: results/power_grid.txt.   Usage: python -I power_grid.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import surrogates as sg

HERE = os.path.dirname(os.path.abspath(__file__))
L, NREP, NS = 30, 150, 500
filled = np.zeros(L, bool); filled[[9, 10, 20]] = True
rng = np.random.default_rng(7171)


def series(path, P, A):
    x = np.zeros(L); x[0] = rng.normal() / np.sqrt(1 - path[0] ** 2)
    for t in range(1, L):
        x[t] = path[t] * x[t - 1] + rng.normal()
    if A > 0:
        x = x + A * np.sin(2 * np.pi * np.arange(L) / P + rng.uniform(0, 2 * np.pi))
    return sg.apply_mask(x[None, :], filled)[0]


rows = []
for P, A in [(11, 0.0)] + [(P, A) for P in (8, 11, 16) for A in (0.75, 1.5, 3.0)]:
    rate = {}
    for name, path in (("null", np.full(L, 0.5)), ("trend", np.linspace(0.3, 0.7, L))):
        rej = sum(sg.surrogate_test(series(path, P, A), filled, 0.5, "ac1", NS, rng)["p_upper"] < 0.05 for _ in range(NREP))
        rate[name] = rej / NREP
    rows.append(f"{P} | {A:g} | {rate['null']:.3f} | {rate['trend']:.3f}")
out = [f"Rejection rate of the surrogate test (p_upper < 0.05); L = {L}, {NREP} series per cell, {NS} surrogates",
       "period (yr) | cycle amplitude | null | trend"] + rows
open(os.path.join(HERE, "results", "power_grid.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
