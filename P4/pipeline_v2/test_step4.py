"""Step 4 check: reproduce inspecao/saidas/17_recommendation_support.txt (3): mean residual AC1 and rolling-tau
mean/SD for none, sigma 1, 3, 5 at L = 30 and 54 (same seeds, same generator, 500 simulations)."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indicators as ind, detrend as dt

REF = {(30, None): (0.73, -0.03, 0.34), (30, 1): (0.02, 0.00, 0.49), (30, 3): (0.66, -0.00, 0.36), (30, 5): (0.71, 0.02, 0.35),
       (54, None): (0.73, -0.01, 0.36), (54, 1): (0.05, -0.02, 0.49), (54, 3): (0.69, 0.04, 0.42), (54, 5): (0.73, 0.05, 0.38)}

def ar1_noise(n, c, rng):
    x = np.zeros(n); x[0] = rng.normal() / np.sqrt(1 - c * c)
    for t in range(1, n): x[t] = c * x[t - 1] + rng.normal()
    return x

ok = True
for (L, sig), (a_ref, t_ref, sd_ref) in REF.items():
    rng = np.random.default_rng(1700 + L)
    t = np.arange(L); res, taus = [], []
    for _ in range(500):
        noise = ar1_noise(L, 0.5, rng)
        x = 3 * noise.std() * np.sin(2 * np.pi * t / 10) + noise
        r = dt.residual(x, sig)
        res.append(ind.ac1(r)); taus.append(ind.kendall_tau(ind.rolling(r, 0.5)))
    a, tm, sd = np.mean(res), np.nanmean(taus), np.nanstd(taus)
    good = abs(a - a_ref) <= 0.01 and abs(tm - t_ref) <= 0.01 and abs(sd - sd_ref) <= 0.01
    ok &= good
    print(f"L={L} sigma={dt.label(sig)}: AC1 {a:+.2f} (ref {a_ref:+.2f}) tau {tm:+.2f} ({t_ref:+.2f}) SD {sd:.2f} ({sd_ref:.2f}) {'PASS' if good else 'FAIL'}")
print("ALL OK" if ok else "SOME FAIL")
