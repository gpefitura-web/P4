"""D108: primary pair (Var u Long > Flat_limpa, AR(1), sigma = 1, one-sided Mann-Whitney) and Holm (D109: per metric x configuration block of 5 pairs; the 30-test family of the first run is kept as p_holm_30) over the
30 other tests of REPORT.md s.6 (5 pairs x [AC1 in 4 configs + var_norm in 2 configs]). Reads results/star_metrics.csv only.
Family of 30 fixed here before computing. Usage: python -I group_primary.py"""
import os, sys
import numpy as np, pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, "results")
met = pd.read_csv(os.path.join(R, "star_metrics.csv"), dtype={"HD": str})
best = met.sort_values("L", ascending=False).drop_duplicates(["HD", "config"])
best = best[best.HD != "(Sun)"]


def mw(a, b):
    U, p = stats.mannwhitneyu(a, b, alternative="greater")
    return float(U), float(p)


d = best[best.config == "s1"]
a = d[d.grupo.isin(["Var", "Long"])].ac1.values; b = d[d.grupo == "Flat_limpa"].ac1.values
U, p = mw(a, b)
prim = dict(teste="Var u Long > Flat_limpa, AC1, s1", n1=len(a), n2=len(b), U=U, p=p, med1=float(np.median(a)), med2=float(np.median(b)))

rows = []
for cfg in ("none", "s1", "s3", "s5"):
    dd = best[best.config == cfg]
    for metric in (("ac1", "var_norm") if cfg in ("none", "s1") else ("ac1",)):
        for g1, g2 in (("Var", "Flat_limpa"), ("Long", "Flat_limpa"), ("CYCLE_Excellent", "Flat_limpa"),
                       ("Var", "CYCLE_Excellent"), ("Long", "CYCLE_Excellent")):
            x = dd[dd.grupo == g1][metric].values; y = dd[dd.grupo == g2][metric].values
            U_, p_ = mw(x, y)
            rows.append(dict(config=cfg, metric=metric, g1=g1, g2=g2, n1=len(x), n2=len(y), U=U_, p=p_))
t = pd.DataFrame(rows)
t["p_holm_30"] = multipletests(t.p.values, method="holm")[1]          # superseded family (D109), kept for the record
t["p_holm"] = t.groupby(["metric", "config"]).p.transform(lambda x: pd.Series(multipletests(x.values, method="holm")[1], index=x.index))   # D109: family = the 5 pairs of one metric x configuration
t.to_csv(os.path.join(R, "group_holm.csv"), index=False)
pd.DataFrame([prim]).to_csv(os.path.join(R, "group_primary.csv"), index=False)
print(prim); print(len(t), "tests; Holm (block) p < 0.05:", int((t.p_holm < 0.05).sum()), "; raw p < 0.05:", int((t.p < 0.05).sum()))
print(t.sort_values("p").head(6).to_string(index=False))
