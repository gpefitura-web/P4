"""Writes manuscrito/tab_segments.tex from pipeline_v2/results (generated table; no hand-typed numbers)."""
import os
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, "results")
OUT = os.path.join(os.path.dirname(HERE), "manuscrito", "tab_segments.tex")
seg = pd.read_csv(os.path.join(R, "segments.csv"), dtype={"HD": str})
res = pd.read_csv(os.path.join(R, "star_results.csv"), dtype={"HD": str})
ran = seg[seg.rodou == "sim"].copy()
lab = {"Flat_limpa": "Flat", "CYCLE_Excellent": "Cycle", "Var": "Var", "Long": "Long"}
order = {"Flat_limpa": 0, "CYCLE_Excellent": 1, "Var": 2, "Long": 3}
ran["o"] = ran.grupo.map(order).fillna(4); ran["hn"] = ran.HD.str.extract(r"(\d+)").astype(float).fillna(0)
ran = ran.sort_values(["o", "hn"])
m = res[(res.series == "S") & (res.frac == 0.5)]
rows = []
for _, r in ran.iterrows():
    d = m[(m.HD == r.HD) & (m.seg_year0 == r.seg_year0)]
    ar = d[d["stat"] == "ac1"].set_index("config"); vr = d[d["stat"] == "var"]
    conc = lambda x: int(((x.tau > 0) & (x.p_upper < 0.05)).sum())
    def tp(c):
        return f"{ar.loc[c, 'tau']:+.2f}".replace("-", "$-$") + f" & {ar.loc[c, 'p_upper']:.3f}"
    hd = r.HD.replace("(Sun)", "Sun$^{b}$")
    dag = "" if str(r.banda_Rphot).startswith("DENTRO") else "$^{a}$"
    y0 = int(r.seg_year0)
    rows.append(f"{hd} & {lab.get(r.grupo, r.grupo)} & {y0}--{y0 + int(r.L) - 1} & {int(r.L)} & {int(r.n_filled)} & {r.bv:.2f}{dag} & {tp('none')} & {tp('s1')} & {conc(d[d['stat'] == 'ac1'])}/{conc(d[d['stat'] == 'var'])} \\\\")
hdr = ("\\begin{tabular}{llrrrrrrrrr}\n\\hline\nHD & Group & Years & $L$ & Interp. & $B\\!-\\!V$ & $\\tau$ & $p$ & $\\tau$ & $p$ & Conc. \\\\\n"
       " & & & & & & \\multicolumn{2}{c}{original series} & \\multicolumn{2}{c}{$\\sigma = 1$ yr} & AR/Var \\\\\n\\hline\n")
open(OUT, "w", encoding="utf-8").write(hdr + "\n".join(rows) + "\n\\hline\n\\end{tabular}\n")
print(len(rows), "rows ->", OUT)
