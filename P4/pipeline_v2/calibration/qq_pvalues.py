"""Exploratory (D126): distribution of the 192 stellar p-values of the official run (series S, window 50 %: 24 segments x 4 configurations x
2 indicators) against the uniform law. No new surrogates. The 4 configurations of one segment are strongly dependent, so KS p-values are
indicative only; the per-configuration subsets (48 cells) are also given. Output: results_calibration/qq_pvalues.{csv,txt}.
Usage: python -I qq_pvalues.py"""
import os
import numpy as np, pandas as pd
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__)); PIPE = os.path.dirname(HERE)
d = pd.read_csv(os.path.join(PIPE, "results", "star_results.csv"), dtype={"HD": str})
d = d[(d.series == "S") & (d.frac == 0.5)]
N = 1001
out = [f"cells {len(d)} (segments {d.groupby(['HD', 'seg_year0']).ngroups})", "tail | subset | cells | frac p<0.05 | frac p<0.01 | KS D | KS p (indicative)"]
rows = []
for tail, col in (("upper", "p_upper"), ("lower", "p_D22")):
    for sub, g in [("all", d)] + [(f"{c}", d[d.config == c]) for c in ("none", "s1", "s3", "s5")] + [(f"{s}", d[d.stat == s]) for s in ("ac1", "var")]:
        p = g[col].values; ks = stats.kstest(p, "uniform")
        out.append(f"{tail} | {sub} | {len(p)} | {(p < .05).mean():.3f} | {(p < .01).mean():.3f} | {ks.statistic:.3f} | {ks.pvalue:.3f}")
    p = np.sort(d[col].values); q = (np.arange(1, len(p) + 1) - 0.5) / len(p)
    rows += [dict(tail=tail, rank=i + 1, p_obs=a, p_unif=b) for i, (a, b) in enumerate(zip(p, q))]
pd.DataFrame(rows).to_csv(os.path.join(PIPE, "results_calibration", "qq_pvalues.csv"), index=False)
txt = "\n".join(out); print(txt); open(os.path.join(PIPE, "results_calibration", "qq_pvalues.txt"), "w").write(txt + "\n")
