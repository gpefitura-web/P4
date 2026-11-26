"""Size and power of the surrogate test when a deterministic cycle is present (D121; answers the reviewers' point that the ARMA surrogate
may absorb a cycle). Series of L = 30 years, three interpolated points as in test_step5.py, window 50 %, rolling lag-1 autocorrelation of
the original series, upper-tail p. Noise: AR(1) with unit innovations, coefficient constant at 0.5 (null) or rising linearly from 0.3 to 0.7
(trend). Cycle: A sin(2 pi t / P + phase), P = 11 years, A = 1.5 (standard deviation of the cycle about the same as that of the noise),
random phase. These values are an illustration, not derived from any star. Fixed seed 7070, 200 series per cell, 1000 surrogates each.
Output: results/power_cycle.txt.   Usage: python -I power_cycle.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import surrogates as sg

HERE = os.path.dirname(os.path.abspath(__file__))
L, NREP, NS, P, A = 30, 200, 1000, 11.0, 1.5
filled = np.zeros(L, bool); filled[[9, 10, 20]] = True
rng = np.random.default_rng(7070)


def series(path, cycle):
    x = np.zeros(L); x[0] = rng.normal() / np.sqrt(1 - path[0] ** 2)
    for t in range(1, L):
        x[t] = path[t] * x[t - 1] + rng.normal()
    if cycle:
        x = x + A * np.sin(2 * np.pi * np.arange(L) / P + rng.uniform(0, 2 * np.pi))
    return sg.apply_mask(x[None, :], filled)[0]


rows = []
for name, path, cycle in (("null, no cycle", np.full(L, 0.5), False), ("trend, no cycle", np.linspace(0.3, 0.7, L), False),
                          ("null, with cycle", np.full(L, 0.5), True), ("trend, with cycle", np.linspace(0.3, 0.7, L), True)):
    rej = 0
    for _ in range(NREP):
        o = sg.surrogate_test(series(path, cycle), filled, 0.5, "ac1", NS, rng)
        rej += o["p_upper"] < 0.05
    rows.append(f"{name} | {rej / NREP:.3f}")
out = [f"Rejection rate of the surrogate test (p_upper < 0.05); L = {L}, {NREP} series per cell, {NS} surrogates, cycle P = {P:g} yr, A = {A:g}",
       "cell | rejection rate"] + rows
open(os.path.join(HERE, "results", "power_cycle.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
