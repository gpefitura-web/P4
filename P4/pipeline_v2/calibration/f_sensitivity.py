"""Exploratory (D125): sensitivity of sigma_S (method A) and state ratios of HD 166620 to the instrumental noise fraction f
of the Mount Wilson states (min1, min2). The Keck fraction of the grand minimum is kept at its published value and also varied."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import state_comparison as sc

d = sc.load_luhn()
out = ["f_MW | sigma_A min1 | sigma_A min2 | sigma_A grand (f_Keck=0.003) | min1/grand | min2/grand | p_one min1 | p_one min2"]
st = {k: sc.state_stats(d, k) for k in sc.STATES}
print("raw:", {k: (round(v['sigma_raw'], 4), round(v['mean'], 4), v['n']) for k, v in st.items()})
def sig(name, f):
    g = d[(d.y >= sc.STATES[name][0]) & (d.y < sc.STATES[name][1])]
    v = g.s.var(ddof=1) - (f * g.s.mean()) ** 2
    return (np.sqrt(v) if v > 0 else np.nan), len(g)
sg, ng = sig("grand", 0.003)
for f in [0.008, 0.010, 0.012, 0.014, 0.016, 0.017, 0.018, 0.019, 0.0193]:
    s1, n1 = sig("min1", f); s2, n2 = sig("min2", f)
    p1 = sc.ftest(s1, n1, sg, ng)["p_one"] if s1 == s1 else np.nan
    p2 = sc.ftest(s2, n2, sg, ng)["p_one"]
    out.append(f"{f:.4f} | {s1:.4f} | {s2:.4f} | {sg:.4f} | {s1/sg:.2f} | {s2/sg:.2f} | {p1:.3g} | {p2:.3g}")
out.append("")
out.append("Keck fraction varied (f_MW = 0.012 and 0.017):")
for fk in [0.001, 0.003, 0.006, 0.010]:
    sgk, _ = sig("grand", fk)
    for f in (0.012, 0.017):
        s1, _ = sig("min1", f); s2, _ = sig("min2", f)
        out.append(f"f_Keck={fk:.3f} f_MW={f:.3f} grand={sgk:.4f} min1/grand={s1/sgk:.2f} min2/grand={s2/sgk:.2f}")
# f at which min1 sigma_A equals the grand-minimum sigma_A
g = d[(d.y >= 1971) & (d.y < 1975)]
fx = np.sqrt((g.s.var(ddof=1) - sg ** 2)) / g.s.mean()
out.append(f"f_MW at which sigma_A(min1) = sigma_A(grand): {fx:.4f}")
txt = "\n".join(out); print(txt)
open(os.path.join(os.path.dirname(HERE), "results_calibration", "f_sensitivity.txt"), "w").write(txt + "\n")
