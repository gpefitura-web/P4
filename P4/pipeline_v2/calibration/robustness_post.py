"""Exploratory (D125): post-processing of results_explore/robustness_data.csv (no surrogates re-run).
Compares the HKP-2-only variant with the base run star by star (HD level, since segments start in 1977 and the keys differ):
median tau per (HD, config, frac, stat) and fraction of raw cells with p_upper < 0.05 / p_lower < 0.05 per variant.
Output: results_explore/robustness_post.txt.   Usage: python -I robustness_post.py"""
import os
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(os.path.dirname(HERE), "results_explore")
df = pd.read_csv(os.path.join(R, "robustness_data.csv"), dtype={"HD": str})
out = ["Fraction of raw cells with p < 0.05 by variant (nominal 0.05 if the test is valid and cells independent)", "variant | cells | upper | lower"]
for v, g in df.groupby("variant"):
    out.append(f"{v} | {len(g)} | {(g.p_upper < .05).mean():.3f} | {(g.p_D22 < .05).mean():.3f}")
b = df[df.variant == "base"].groupby(["HD", "config", "frac", "stat"], as_index=False).tau.median().rename(columns={"tau": "tau_b"})
h = df[df.variant == "hkp2"].groupby(["HD", "config", "frac", "stat"], as_index=False).tau.median()
m = h.merge(b, on=["HD", "config", "frac", "stat"])
out += ["", f"HKP-2 only vs base, HD level: {m.HD.nunique()} stars, {len(m)} matched cells",
        f"median tau base {m.tau_b.median():+.3f}, hkp2 {m.tau.median():+.3f}; median |dtau| {(m.tau - m.tau_b).abs().median():.3f}; sign flips {(np.sign(m.tau) != np.sign(m.tau_b)).sum()}/{len(m)}"]
for stat, g in m.groupby("stat"):
    out.append(f"{stat}: median tau base {g.tau_b.median():+.3f}, hkp2 {g.tau.median():+.3f}, corr {np.corrcoef(g.tau, g.tau_b)[0, 1]:.2f}")
g = df[df.variant == "hkp2"]
out += ["", "HKP-2 flagged cells by star (p_upper<0.05): " + ", ".join(f"{k}:{v}" for k, v in g[g.p_upper < .05].groupby("HD").size().items())]
txt = "\n".join(out); print(txt); open(os.path.join(R, "robustness_post.txt"), "w").write(txt + "\n")
