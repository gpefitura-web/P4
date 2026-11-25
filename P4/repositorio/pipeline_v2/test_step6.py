"""Step 6 check against P4_SOURCE_VALUES V22, V24, V25 (checks 3.4-25, -32, -39, -50, -52; B: 3.4-27, -34, -41)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import state_comparison as sc
r = sc.run_h1(); ok = True
def chk(name, got, exp, tol):
    global ok
    g = abs(got - exp) <= tol; ok &= g
    print(f"{name}: {got:.6g} vs {exp:.6g} -> {'PASS' if g else 'FAIL'}")
for k, a, b in (("min1", .0027, .0028), ("min2", .0054, .0048), ("grand", .0019, .0015)):
    chk(f"sigma_A {k}", r["states"][k]["sigma_A"], a, 5e-5); chk(f"sigma_B {k}", r["states"][k]["sigma_B"], b, 5e-5)
for k, n in (("min1", 44), ("min2", 315), ("grand", 103)):
    ok &= r["states"][k]["n"] == n; print("N", k, r["states"][k]["n"], n)
f = r["F_min1_vs_grand"]
chk("F raw p two-sided (V25 8.78e-6)", f["raw"]["p_two"], 8.78e-6, 0.05e-6)
chk("F corrected(A) p two-sided (V25 8.7e-3)", f["corrected_A"]["p_two"], 8.68e-3, 0.05e-3)
print("ALL OK" if ok else "SOME FAIL")
