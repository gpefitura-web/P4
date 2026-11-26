"""Does the ARMA order chosen by AIC depend on the scale of the series? An affine change (S -> a*S + b, as in the conversion to R'HK)
should not change the maximum-likelihood fit or the AIC ranking. For each analyzed Mount Wilson segment of a star (the Sun is left out
so that the script does not need Table 4 of Egeland) and each of the four detrending configurations, the residual is fitted as it is and
after standardization (mean 0, SD 1). Output: results/scale_sensitivity.txt.
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
            o_raw = sg.fit_arma(res)["order"]; o_std = sg.fit_arma((res - res.mean()) / res.std())["order"]
            n += 1; same += o_raw == o_std
            rows.append(f"{r.HD} | {seg['year0']} | {dt.label(sigma)} | {o_raw} | {o_std}")
out = [f"ARMA order chosen by AIC on the residual as it is and after standardization (mean 0, SD 1); star segments, four configurations",
       f"cases | identical order | different order", f"{n} | {same} | {n - same}", "", "HD | segment start | config | order as is | order standardized"] + rows
with open(os.path.join(HERE, "results", "scale_sensitivity.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
print("\n".join(out[:3]))
