"""Writes manuscrito/cal_table_simulations.tex (summary of all simulations) and manuscrito/cal_table_stars.tex (extended stellar table: source,
spectral type from Baum+2022, evolutionary flag and log g, observations per year) from the code constants and results (REG-MAC).
Spectral types are taken only from the Baum+2022 table (grade A); the digitised Baliunas types are not used. Usage: python -I make_tables_calibration.py"""
import os, sys, re
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "calibration"))
import p4io, annual
import positive_control_full as pcf, power_bilateral as pb, power_design as pdz, step_injection as si
ROOT = os.path.dirname(HERE); MAN = os.path.join(ROOT, "manuscrito")
def seed(script):
    return re.search(r"SeedSequence\((\d+)\)", open(os.path.join(HERE, "calibration", script), encoding="utf-8").read()).group(1)
def tex(x): return str(x).replace("_", "\\_")

# ---- simulation summary ----
bi = pd.read_csv(os.path.join(HERE, "results_calibration", "power_bilateral.csv"))
nbi_c = int((bi[(bi.case == "hopf_lost") & (bi.P == 11.0) & (bi.s0 == 0.15)]).shape[0]); nbi_o = int(bi[(bi.case == "hopf_lost") & ~((bi.P == 11.0) & (bi.s0 == 0.15))].groupby(["P", "s0"]).size().iloc[0])
rows = [
 ("Positive control", "Hopf oscillator, three variants (super-, subcritical, multiplicative noise); cycle persists or is lost",
  f"$L={pcf.L}$ yr, period 11 yr, dynamical noise {pcf.S0:g}, observation noise {pcf.OBS:g}", f"{pcf.NREP}", f"{pcf.NS}", seed("positive_control_full.py")),
 ("Two-sided power grid", "supercritical Hopf, cycle persists or is lost",
  f"periods 8, 11, 15 yr; dynamical noise 0.10, 0.15, 0.30", f"{nbi_c} (centre), {nbi_o} (others)", f"{pb.NS}", seed("power_bilateral.py")),
 ("Size and true CSD", "AR(1), constant 0.5 or rising 0.3 to 0.7, no cycle", f"$L={pb.L}$ yr", f"{int((bi.case == 'ar1_null').sum())}", f"{pb.NS}", seed("power_bilateral.py")),
 ("Design power curve", "AR(1) 0.3 to 0.7 against 0.5, with or without an 11-yr cycle, observation-noise ratio 0, 0.5, 1",
  "$L = 30, 50, 100, 200$ yr", f"{pdz.NREP}", f"{pdz.NS}", seed("power_design.py")),
 ("Instrumental step", "AR(1) 0.5, step in level or noise after year %d" % si.K, f"$L={si.L}$ yr; level 0.5, 1, 2 sd; noise $\\times$0.5, $\\times$1.5", f"{si.NREP}", f"{si.NS}", seed("step_injection.py")),
]
body = ("\\begin{tabular}{p{1.8cm}p{3.3cm}p{3.5cm}p{1.5cm}rr}\n\\hline\nExperiment & Model & Parameters & Series & Surr. & Seed \\\\\n\\hline\n"
        + "\n".join(f"{a} & {b} & {c} & {d} & {e} & {f} \\\\" for a, b, c, d, e, f in rows) + "\n\\hline\n\\end{tabular}\n")
open(os.path.join(MAN, "cal_table_simulations.tex"), "w", encoding="utf-8").write(body)

# ---- extended stellar table ----
seg = pd.read_csv(os.path.join(HERE, "results", "segments.csv"), dtype={"HD": str}); ran = seg[seg.rodou == "sim"].copy()
cat = p4io.load_catalog(only_included=False).set_index("HD")
baum = pd.read_csv(os.path.join(ROOT, "baum2022_59stars.csv"), dtype={"HD": str}).set_index("HD")
lab = {"Flat_limpa": "Flat", "CYCLE_Excellent": "Cycle", "Var": "Var", "Long": "Long"}; order = {"Flat_limpa": 0, "CYCLE_Excellent": 1, "Var": 2, "Long": 3}
ran["o"] = ran.grupo.map(order).fillna(4); ran.loc[ran.HD == "(Sun)", "o"] = 4; ran["hn"] = ran.HD.str.extract(r"(\d+)").astype(float).fillna(0); ran = ran.sort_values(["o", "hn"])
SRC = {"Baum": "Baum", "v2001": "HK v2001", "Egeland2017_T4": "Egeland"}
out = []
for _, r in ran.iterrows():
    sun = r.HD == "(Sun)"
    obs = p4io.load_star(r.HD, cat.loc[r.HD].copy().rename(None) if False else pd.Series(cat.loc[r.HD].to_dict()))
    ann = annual.annual_means(obs, None if sun else "MW")
    y0, y1 = int(r.seg_year0), int(r.seg_year0 + r.L - 1); a = ann[(ann.year >= y0) & (ann.year <= y1)]
    spt = baum.loc[r.HD, "SpType"] if r.HD in baum.index else "--"
    lg = baum.loc[r.HD, "logg"] if r.HD in baum.index else None
    flag = "sub." if cat.loc[r.HD, "subgigante_catalogo"] == "sim" else "MS"
    hd = r.HD.replace("(Sun)", "Sun")
    out.append(f"{hd} & {lab.get(r.grupo, r.grupo)} & {SRC.get(r.fonte, r.fonte)} & {spt} & {flag} & {'--' if lg is None or pd.isna(lg) else f'{lg:.2f}'} & {y0}--{y1} & {int(r.L)} & {int(r.n_filled)} & {int(a.n.median())} & {int(a.n.min())} \\\\")
hdr = ("\\begin{tabular}{lllllrrrrrr}\n\\hline\nHD & Group & Source & Spec. type & Flag & $\\log g$ & Years & $L$ & Interp. & $n$ med. & $n$ min. \\\\\n\\hline\n")
open(os.path.join(MAN, "cal_table_stars.tex"), "w", encoding="utf-8").write(hdr + "\n".join(out) + "\n\\hline\n\\end{tabular}\n")
print(len(rows), "simulation rows,", len(out), "star rows")
