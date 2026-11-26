"""Does the ARMA order chosen by AIC depend on the scale of the series? An affine change (S -> a*S + b, as in the conversion to R'HK)
should not change the maximum-likelihood fit or the AIC ranking. Before D121 the fit was done on the raw scale and the order did change
(33 of 92 cases at standardization; see D120 in the notebook). The fit is now done on the standardized series, so the order must be
the same after any affine change. For each analyzed Mount Wilson segment of a star (the Sun is left out so that the script does not need
Table 4 of Egeland) and each of the four detrending configurations, the residual is fitted as it is and after the change x -> 1000 x + 5.
Output: results/scale_sensitivity.txt.
Usage: python -I scale_sensitivity.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import p4io, annual, detrend as dt, surrogates as sg, run_all

HERE = os.path.dirname(os.path.abspath(__file__))
n = same = 0
rows = []
for _, r in p4io.load_catalog().iterrows():
    if r.serie_fonte == "Egeland2017_T4" or r.indicador_elegivel_D100 != "sim":
        continue
    ann = annual.annual_means(p4io.load_star(r.HD, r), "MW")
    for seg in annual.segments(ann):
        if len(seg["years"]) < run_all.MIN_SEG:
            continue
        for sigma in dt.CONFIGS:
            res = dt.residual(seg["S"], sigma)
            o_raw = sg.fit_arma(res)["order"]; o_aff = sg.fit_arma(1000.0 * res + 5.0)["order"]
            n += 1; same += o_raw == o_aff
            rows.append(f"{r.HD} | {seg['year0']} | {dt.label(sigma)} | {o_raw} | {o_aff}")
out = ["ARMA order chosen by AIC on the residual as it is and after the affine change x -> 1000 x + 5; star segments, four configurations",
       "cases | identical order | different order", f"{n} | {same} | {n - same}", "", "HD | segment start | config | order as is | order after the change"] + rows
with open(os.path.join(HERE, "results", "scale_sensitivity.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
print("\n".join(out[:3]))
