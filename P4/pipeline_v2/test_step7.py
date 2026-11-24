"""Step 7 check: reproduces checks 3.7-12..3.7-14 (log R'HK and R_phot/R_HK with the catalogue B-V of B95)."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rhk
ok = True
for hd, bv, S, elog, eratio in (("10700", 0.72, 0.171, -4.959, 0.486), ("32147", 1.06, 0.286, -4.948, 0.054),
                                 ("201091", 1.18, 0.658, -4.764, 0.006)):
    rp, rh = rhk.rhk_prime(S, bv)
    lg, ratio = math.log10(rp), rhk.rphot(bv) / rh
    g = abs(lg - elog) <= 0.0006 and abs(ratio - eratio) <= 0.0006; ok &= g
    print(f"HD {hd}: log R'HK {lg:.3f} (exp {elog}); Rphot/RHK {ratio:.3f} (exp {eratio}); band {rhk.band(bv)} -> {'PASS' if g else 'FAIL'}")
print("ALL OK" if ok else "SOME FAIL")
