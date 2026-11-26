"""Rewrites the marked macro block of manuscrito/main.tex from pipeline_v2/results (REG-MAC: no number typed in the text).
Usage: python -I make_macros.py"""
import os, re, json
import sys
import numpy as np, pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p4io, run_all   # run_all is import-safe (main() is guarded); it supplies the design constants NSURR and BASE_SEED

HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, "results")
OUT = os.path.join(os.path.dirname(HERE), "manuscrito", "main.tex")   # macros live in a marked block of main.tex
res = pd.read_csv(os.path.join(R, "star_results.csv"), dtype={"HD": str})
seg = pd.read_csv(os.path.join(R, "segments.csv"), dtype={"HD": str})
h1 = json.load(open(os.path.join(R, "h1.json")))
prim = pd.read_csv(os.path.join(R, "group_primary.csv")).iloc[0]
hol = pd.read_csv(os.path.join(R, "group_holm.csv"))
auto = open(os.path.join(R, "autotest_step5.txt")).read()
M = {}
STATN = {"ac1": "AR", "var": "Var"}


def put(name, val, fmt="{}"):
    t = fmt.format(val)
    M[name] = ("\\textminus{}" + t[1:]) if t.startswith("-") else t


ran = seg[seg.rodou == "sim"]
put("NSegments", len(ran)); put("NStarsRun", int((ran.HD != "(Sun)").sum()))
put("NNotRun", int((seg.rodou == "nao").drop_duplicates().sum() and (seg[seg.rodou == "nao"].HD.nunique())))
put("NLow", int((ran.precisao == "baixa").sum())); put("NSunYears", int(ran[ran.HD == "(Sun)"].L.iloc[0]))
put("NSurr", run_all.NSURR); put("SeedBase", run_all.BASE_SEED)
put("NConfigs", res.config.nunique()); put("NFracs", res.frac.nunique())
put("LMin", int(ran.L.min())); put("LMax", int(ran[ran.HD != "(Sun)"].L.max()))
# H1
for k, tag in (("min1", "MinOne"), ("min2", "MinTwo"), ("grand", "Grand")):
    s = h1["states"][k]
    put(f"HOneN{tag}", s["n"]); put(f"HOneMean{tag}", s["mean"], "{:.4f}")
    put(f"HOneRaw{tag}", s["sigma_raw"], "{:.4f}"); put(f"HOneSigA{tag}", s["sigma_A"], "{:.4f}"); put(f"HOneSigB{tag}", s["sigma_B"], "{:.4f}")
f = h1["F_min1_vs_grand"]
def sci(x):
    m, e = f"{x:.0e}".split("e"); return f"{m}\\times10^{{{int(e)}}}"
put("HOnePRaw", "$" + sci(f["raw"]["p_two"]) + "$"); put("HOnePCorrA", "$" + sci(f["corrected_A"]["p_two"]) + "$")
put("HOnePCorrB", "$" + sci(f["corrected_B"]["p_two"]) + "$")
put("HOneFRaw", f["raw"]["F"], "{:.2f}"); put("HOneFCorrA", f["corrected_A"]["F"], "{:.2f}")
# concordance and counts at 50 %
m5 = res[(res.series == "S") & (res.frac == 0.5)]
sig = m5.assign(c=(m5.tau > 0) & (m5.p_upper < 0.05))
put("NCellsHalf", len(m5.groupby(["HD", "seg_year0", "stat", "config"])))
put("NSigHalf", int(sig.c.sum()))
for stat in ("ac1", "var"):
    conc = sig[sig["stat"] == stat].groupby(["HD", "seg_year0"]).c.sum()
    put(f"MaxConc{STATN[stat]}", int(conc.max())); put(f"NConcThree{STATN[stat]}", int((conc >= 3).sum()))
    pos = m5[(m5["stat"] == stat) & (m5.config == "s1")]
    put(f"NTauPos{STATN[stat]}SOne", int((pos.tau > 0).sum()))
allc = res[res.series == "S"]
sa = allc.assign(c=(allc.tau > 0) & (allc.p_upper < 0.05)).groupby(["HD", "seg_year0", "stat"]).c.sum()
put("MaxConcSweep", int(sa.max()))
f2 = h1["F_min2_vs_grand"]
assert f2["raw"]["p_two"] < 1e-3 and f2["corrected_A"]["p_two"] < 1e-3
put("HOnePTwoBound", "$<10^{-3}$")
# source counts read from the frozen catalog and the input files (check_manuscript_constants.py and test_step1.py also confront them)
cat = p4io.load_catalog(only_included=False)
put("NCatalog", len(cat)); put("NBaumStars", p4io.load_baum(drop_sigma=False).HD.nunique()); put("NVTwoStars", p4io.load_v2001().HD.nunique())
put("NExclCalib", int(cat.motivo.str.startswith("D13").sum())); put("NExclBinary", int(cat.motivo.str.startswith("R11").sum()))
flat = cat[cat.classe_B95.str.startswith("Flat")]
put("NFlatClass", len(flat)); put("NFlatCalib", int(flat.motivo.str.startswith("D13").sum()))
put("NFlatBin", int(((flat.apendiceB_binaria == "sim") & ~flat.motivo.str.startswith("D13")).sum()))
clean = cat[cat.grupo_P4 == "Flat_limpa"]
put("NFlatClean", len(clean)); put("NFlatSeries", int((clean.status_amostra == "incluida").sum()))
assert len(flat) == int(flat.motivo.str.startswith("D13").sum()) + int(((flat.apendiceB_binaria == "sim") & ~flat.motivo.str.startswith("D13")).sum()) + len(clean)
# the two significant cells at a window of 50 % (the text names them by star and by configuration)
sg = sig[sig.c].assign(o=lambda d: d.config.map({"none": 0, "s1": 1})).sort_values("o")
assert len(sg) == 2 and list(sg.config) == ["none", "s1"] and all(sg["stat"] == "ac1"), "text wording of the two flagged cells is out of date"
for (_, r), tag in zip(sg.iterrows(), ("One", "Two")):
    put(f"Sig{tag}HD", r.HD); put(f"Sig{tag}Tau", r.tau, "{:+.2f}"); put(f"Sig{tag}P", r.p_upper, "{:.3f}")
put("NChance", int(round(0.05 * len(m5.groupby(["HD", "seg_year0", "stat", "config"])))))
put("NOtherSeg", len(ran) - int((ran.HD == "166620").sum()))
put("NSweepCells", res.config.nunique() * res.frac.nunique())
hdh = ran[ran.HD == "166620"].iloc[0]; put("HDHEnd", int(hdh.seg_year0 + hdh.L - 1))
w5 = res[(res.frac == 0.5) & (res.series == "S")].drop_duplicates(["HD", "seg_year0"])
put("WinMin", int(w5.w.min())); put("WinMax", int(w5.w.max()))
rl = res[res.series == "RHK"].drop_duplicates(["HD", "seg_year0"]).merge(seg[["HD", "seg_year0", "L"]], on=["HD", "seg_year0"], suffixes=("_r", ""))
put("RHKLMin", int(rl.L.min())); put("RHKLMax", int(rl.L.max()))
# HD 166620 (H2) and the Sun
for hd, tag in (("166620", "HDH"), ("(Sun)", "Sun")):
    d = m5[(m5.HD == hd) & (m5["stat"] == "ac1")].set_index("config")
    for cfg, ct in (("none", "None"), ("s1", "SOne")):
        put(f"{tag}Tau{ct}", d.loc[cfg, "tau"], "{:.2f}"); put(f"{tag}P{ct}", d.loc[cfg, "p_upper"], "{:.2f}")
put("HDHL", int(seg[seg.HD == "166620"].L.iloc[0]))
dv = m5[(m5.HD == "166620") & (m5["stat"] == "var")].set_index("config")
put("HDHVarTauSOne", dv.loc["s1", "tau"], "{:.2f}"); put("HDHVarPSOne", dv.loc["s1", "p_upper"], "{:.2f}")
put("HDHVarTauNone", dv.loc["none", "tau"], "{:.2f}"); put("HDHVarPNone", dv.loc["none", "p_upper"], "{:.2f}")
seg_ok = seg[seg.rodou == "sim"].set_index("HD")
put("WinHD", int(round(0.5 * seg_ok.loc["166620", "L"]))); put("WinSun", int(round(0.5 * seg_ok.loc["(Sun)", "L"])))
put("NFigTests", int(len(m5[(m5["stat"] == "ac1") & m5.config.isin(["none", "s1"])])))
met = pd.read_csv(os.path.join(R, "star_metrics.csv"), dtype={"HD": str})
best = met.sort_values("L", ascending=False).drop_duplicates(["HD", "config"])
best = best[best.HD != "(Sun)"]
put("MedACNone", best[best.config == "none"].ac1.median(), "{:.2f}"); put("MedACSOne", best[best.config == "s1"].ac1.median(), "{:.2f}")
put("NACNoneHigh", int((best[best.config == "none"].ac1 > 0.5).sum())); put("NStarsMetric", int((best.config == "none").sum()))
# R'HK identity
pv = res.pivot_table(index=["HD", "seg_year0", "config", "frac", "stat"], columns="series", values="tau")
put("RHKMaxDiff", float(np.abs(pv.RHK - pv.S).max()), "{:.0f}"); put("RHKNCompare", len(pv))
# group tests
put("PrimN", int(prim.n1)); put("PrimNFlat", int(prim.n2)); put("PrimP", prim.p, "{:.2f}"); put("PrimU", prim.U, "{:.0f}")
put("PrimMedVL", prim.med1, "{:.2f}"); put("PrimMedFlat", prim.med2, "{:.2f}")
put("NHolmTests", len(hol)); put("NHolmSig", int((hol.p_holm < 0.05).sum())); put("NRawSig", int((hol.p < 0.05).sum()))
for cfg, tag in (("s1", "SOne"), ("none", "None")):
    r = hol[(hol.config == cfg) & (hol.metric == "var_norm") & (hol.g1 == "CYCLE_Excellent") & (hol.g2 == "Flat_limpa")].iloc[0]
    put(f"CycFlatP{tag}", r.p, "{:.4f}"); put(f"CycFlatHolm{tag}", r.p_holm, "{:.4f}")
# autotest
a = re.search(r"p_upper<0.05: ([0-9.]+) ; p_D22<0.05: ([0-9.]+)", auto)
put("AutoUp", 100 * float(a.group(1)), "{:.1f}"); put("AutoLo", 100 * float(a.group(2)), "{:.1f}")
# ---- additions after the independent reviews --------------------------------------------------------------
import math, re as _re
rm = pd.read_csv(os.path.join(R, "star_results.csv"), dtype={"HD": str})
pv2 = rm[rm.frac == 0.5].pivot_table(index=["HD", "seg_year0", "config", "stat"], columns="series", values="p_upper")
put("RHKMaxPDiff", float(np.abs(pv2.RHK - pv2.S).max()), "{:.2f}")
mr = rm[(rm.series == "RHK") & (rm.frac == 0.5)]
put("NSigHalfRHK", int(((mr.tau > 0) & (mr.p_upper < 0.05)).sum()))
put("NHolmSigThirty", int((hol.p_holm_30 < 0.05).sum()))
for cfg, tag in (("s1", "SOne"), ("none", "None")):
    r = hol[(hol.config == cfg) & (hol.metric == "var_norm") & (hol.g1 == "CYCLE_Excellent") & (hol.g2 == "Flat_limpa")].iloc[0]
    put(f"CycFlatHolmThirty{tag}", r.p_holm_30, "{:.2f}")
put("MinPCycleFlat", 1 / math.comb(12, 4), "{:.4f}"); put("MinPFourFour", 1 / math.comb(8, 4), "{:.3f}")
for P, n in ((10, "Ten"), (12, "Twelve"), (16, "Sixteen")):
    put(f"Per{n}", P)
    put(f"ResAmp{n}", 100 * (1 - math.exp(-0.5 * (2 * math.pi * 1.0 / P) ** 2)), "{:.0f}")
ng = ran[ran.HD != "(Sun)"].grupo.value_counts()
for g, n in (("Flat_limpa", "Flat"), ("CYCLE_Excellent", "Cycle"), ("Var", "Var"), ("Long", "Long")):
    put(f"NGroup{n}", int(ng.get(g, 0)))
txt16 = open(os.path.join(R, "power_simulation.txt")).read()
pl = [int(x) for x in _re.findall(r"^(\d+) \| \d+ \| \d+ \| [+-]", txt16, _re.M)]
put("PowLMin", min(pl)); put("PowLMax", max(pl))
for Lx, n in ((24, "TwentyFour"), (30, "Thirty"), (40, "Forty")):
    mm = _re.search(rf"^{Lx} \| \d+ \| \d+ \| [^|]+\| [^|]+\| [^|]+\| ([0-9.]+) \|", txt16, _re.M)
    put(f"AUC{n}", float(mm.group(1)), "{:.2f}")
# ---- additions after the second round of independent reviews (D120) -------------------------------------------------
put("NChanceEff", int(round(len(m5.groupby(["HD", "seg_year0", "stat", "config"])) * float(a.group(1)))))   # expected count at the measured size
hs = h1["states"]
put("HOneMeanPct", 100 * (hs["min2"]["mean"] - hs["grand"]["mean"]) / hs["min2"]["mean"], "{:.1f}")
put("HOneRatioRaw", hs["min2"]["sigma_raw"] / hs["grand"]["sigma_raw"], "{:.1f}"); put("HOneRatioA", hs["min2"]["sigma_A"] / hs["grand"]["sigma_A"], "{:.1f}")
ar = res.drop_duplicates(["HD", "seg_year0", "config", "series"]).pivot_table(index=["HD", "seg_year0", "config"], columns="series", values="arma", aggfunc="first")
put("NArmaCmp", len(ar)); put("NArmaDiff", int((ar.S != ar.RHK).sum()))
sc_txt = open(os.path.join(R, "scale_sensitivity.txt")).read()
cs = _re.search(r"^(\d+) \| (\d+) \| (\d+)$", sc_txt, _re.M)
put("NScaleCases", int(cs.group(1))); put("NScaleSame", int(cs.group(2))); put("NScaleDiff", int(cs.group(3)))
block = "\n".join(f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in M.items())
src = open(OUT, encoding="utf-8").read()
beg, end = "%%% BEGIN GENERATED MACROS", "%%% END GENERATED MACROS"
i = src.index(beg); i = src.index("\n", i) + 1; j = src.index(end)
open(OUT, "w", encoding="utf-8").write(src[:i] + block + "\n" + src[j:])
print(len(M), "macros written into the marked block of", OUT)
