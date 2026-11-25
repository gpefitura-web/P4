"""Step 3 check: SD of the lag-1 estimate in a window of w points on AR(1) noise ~ sqrt((1-c^2)/w)
(inspecao/saidas/16_min_segment.txt s.1: w=12 -> 0.249 vs 0.250; w=24 -> 0.184 vs 0.177 at c=0.5)."""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indicators as ind

def sim(n, c, rng):
    x = np.zeros(n); x[0] = rng.normal() / np.sqrt(1 - c * c)
    for t in range(1, n): x[t] = c * x[t - 1] + rng.normal()
    return x

rng = np.random.default_rng(3)
ok = True
for w, ref in ((12, 0.249), (24, 0.184)):
    e = np.array([ind.ac1(sim(w, 0.5, rng)) for _ in range(4000)])
    th = np.sqrt((1 - 0.25) / w)
    good = abs(e.std() - th) < 0.02 and abs(e.std() - ref) < 0.02
    ok &= good
    print(f"w={w}: SD {e.std():.3f}, formula {th:.3f}, inspecao {ref} -> {'PASS' if good else 'FAIL'}")
r = ind.rolling(sim(24, 0.5, rng), 0.5)
print("L=24, 50 %: windows", len(r), "(expected 13)"); ok &= len(r) == 13
print("tau of increasing seq:", ind.kendall_tau(np.arange(10.)))
print("ALL OK" if ok else "SOME FAIL")
