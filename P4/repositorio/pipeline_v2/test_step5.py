"""Step 5 mandatory self-test: on synthetic null AR(1) series (no trend), the rejection rate at 5 % must lie in
[3 %, 7 %]. Fixed seeds, 600 series, 1000 surrogates each; L = 30 with three interpolated points (mask), window 50 %,
statistic = rolling lag-1 autocorrelation, Kendall tau, original series (no detrending)."""
import os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import surrogates as sg

def ar1(n, c, rng):
    x = np.zeros(n); x[0] = rng.normal() / np.sqrt(1 - c * c)
    for t in range(1, n): x[t] = c * x[t - 1] + rng.normal()
    return x

NREP, NS, L = 600, 1000, 30
filled = np.zeros(L, bool); filled[[9, 10, 20]] = True
rng = np.random.default_rng(5050)
t0 = time.time(); rej_up = rej_lo = 0; orders = {}
for k in range(NREP):
    x = ar1(L, 0.5, rng)
    x = sg.apply_mask(x[None, :], filled)[0]                  # data pass through the same interpolation
    out = sg.surrogate_test(x, filled, 0.5, "ac1", NS, rng)
    rej_up += out["p_upper"] < 0.05; rej_lo += out["p_D22"] < 0.05
    orders[out["order"]] = orders.get(out["order"], 0) + 1
up, lo = rej_up / NREP, rej_lo / NREP
print(f"engine {out['engine']}; orders chosen {orders}; time {time.time()-t0:.0f}s")
print(f"rejection p_upper<0.05: {up:.3f}; p_D22<0.05: {lo:.3f}; required in [0.03, 0.07]")
print("ALL OK" if 0.03 <= up <= 0.07 and 0.03 <= lo <= 0.07 else "SOME FAIL")
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results"), exist_ok=True)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "autotest_step5.txt"), "w") as fh:
    fh.write(f"Step 5 self-test (test_step5.py), seed 5050: {NREP} null AR(1) series (c=0.5, L={L}, 3 interpolated points), {NS} ARMA surrogates each.\n"
             f"engine {out['engine']}; AIC orders chosen: {sorted(orders.items(), key=lambda kv: -kv[1])}\n"
             f"rejection p_upper<0.05: {up:.3f} ; p_D22<0.05: {lo:.3f} ; required in [0.03, 0.07] -> {'PASS' if 0.03 <= up <= 0.07 and 0.03 <= lo <= 0.07 else 'FAIL'}\n")
