"""Writes manuscrito/calibration_macros.tex from pipeline_v2/results_calibration (and results/), REG-MAC: no number typed in the text.
Macro names are letters only (digits spelled out). Usage: python -I make_macros_calibration.py"""
import os, sys, math
import numpy as np, pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "calibration"))
import state_comparison as sc
import positive_control_full as pcf, power_bilateral as pb, power_design as pd_, step_injection as si
R = os.path.join(HERE, "results_calibration"); RES = os.path.join(HERE, "results")
OUT = os.path.join(os.path.dirname(HERE), "manuscrito", "calibration_macros.tex")
W = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
M = {}
def nm(*parts):
    return "".join(W[int(c)] if c.isdigit() else c for p in parts for c in str(p) if c.isalnum())
def put(name, val, fmt="{}"):
    t = fmt.format(val); M[name] = ("\\textminus{}" + t[1:]) if t.startswith("-") else t
def pct(x): return 100 * float(x)
ST = {"ac1": "Ac", "var": "Var"}

# ---- positive controls (positive_control_full.csv) ----
pc = pd.read_csv(os.path.join(R, "positive_control_full.csv"))
put("PCFNRep", pcf.NREP); put("PCNSurr", pcf.NS); put("PCL", pcf.L); put("PCNoiseDyn", pcf.S0, "{:.2f}"); put("PCNoiseObs", pcf.OBS, "{:.2f}")
put("PCFPeriod", 11); put("PCStepsPerYear", pcf.SPY)
MN = {"super": "Super", "sub": "Sub", "mult": "Mult"}
def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    return (pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()
for m, T in MN.items():
    put(f"PCMu{T}Start", pcf.MU[m][0], "{:+.1f}"); put(f"PCMu{T}End", pcf.MU[m][1], "{:+.1f}")
    for s, S in ST.items():
        a = pc[(pc.model == m) & pc.lost]; b = pc[(pc.model == m) & ~pc.lost]
        put(f"PC{T}{S}TauLost", a[f"tau_{s}"].median(), "{:+.2f}")
        put(f"PC{T}{S}LowLost", pct((a[f"plow_{s}"] < .05).mean()), "{:.1f}"); put(f"PC{T}{S}UpLost", pct((a[f"pup_{s}"] < .05).mean()), "{:.1f}")
        put(f"PC{T}{S}LowPersist", pct((b[f"plow_{s}"] < .05).mean()), "{:.1f}"); put(f"PC{T}{S}UpPersist", pct((b[f"pup_{s}"] < .05).mean()), "{:.1f}")
        put(f"PC{T}{S}AUC", auc(-a[f"plow_{s}"], -b[f"plow_{s}"]), "{:.2f}")
    a = pc[(pc.model == m) & pc.lost]
    put(f"PC{T}SDFirst", a.amp_first5.median(), "{:.2f}"); put(f"PC{T}SDLast", a.amp_last5.median(), "{:.2f}")

put("PCPersistMax", pct(max((g[f"{t}_{st}"] < .05).mean() for m in MN for st in ST for t in ("plow", "pup") for g in [pc[(pc.model == m) & ~pc.lost]])), "{:.1f}")

# ---- bilateral power grid (power_bilateral.csv) ----
bi = pd.read_csv(os.path.join(R, "power_bilateral.csv"))
c = bi[(bi.P == 11.0) & (bi.s0 == 0.15)]
put("PBNCentral", len(c[c.case == "hopf_lost"])); put("PBNOther", int(bi[(bi.case == "hopf_lost") & ~((bi.P == 11.0) & (bi.s0 == 0.15))].groupby(["P", "s0"]).size().iloc[0]))
for case, tag in (("ar1_null", "Null"), ("ar1_trend", "Trend")):
    g = bi[bi.case == case]
    for s, S in ST.items():
        put(f"PB{tag}{S}Up", pct((g[f"pup_{s}"] < .05).mean()), "{:.1f}"); put(f"PB{tag}{S}Low", pct((g[f"plow_{s}"] < .05).mean()), "{:.1f}")
        put(f"PB{tag}{S}Tau", g[f"tau_{s}"].median(), "{:+.2f}")
put("PBNNull", len(bi[bi.case == "ar1_null"]))
for s, S in ST.items():
    put(f"PBTrend{S}AUC", auc(-bi[bi.case == "ar1_trend"][f"pup_{s}"], -bi[bi.case == "ar1_null"][f"pup_{s}"]), "{:.2f}")
    aucs = []
    for (P, s0), g in bi[bi.case.isin(["hopf_lost", "hopf_persist"])].groupby(["P", "s0"]):
        aucs.append(auc(-g[g.case == "hopf_lost"][f"plow_{s}"], -g[g.case == "hopf_persist"][f"plow_{s}"]))
    put(f"PBGrid{S}AUCMin", min(aucs), "{:.2f}"); put(f"PBGrid{S}AUCMax", max(aucs), "{:.2f}")
    put(f"PBGrid{S}LowMax", pct(max((g[f"plow_{s}"] < .05).mean() for (_, _, cs), g in bi.groupby(["P", "s0", "case"]) if cs == "hopf_lost")), "{:.1f}")
    put(f"PBGrid{S}LowMin", pct(min((g[f"plow_{s}"] < .05).mean() for (_, _, cs), g in bi.groupby(["P", "s0", "case"]) if cs == "hopf_lost")), "{:.1f}")
    put(f"PBPersist{S}UpMax", pct(max((g[f"pup_{s}"] < .05).mean() for (_, _, cs), g in bi.groupby(["P", "s0", "case"]) if cs == "hopf_persist")), "{:.1f}")
put("PBPeriodMin", int(bi[bi.P > 0].P.min())); put("PBPeriodMax", int(bi[bi.P > 0].P.max()))
put("PBNoiseMin", bi[bi.s0 > 0].s0.min(), "{:.2f}"); put("PBNoiseMax", bi[bi.s0 > 0].s0.max(), "{:.2f}")

# ---- design power curve (power_design.csv) ----
de = pd.read_csv(os.path.join(R, "power_design.csv"))
put("PDNRep", pd_.NREP); put("PDNSurr", pd_.NS); put("PDCycleAmp", pd_.A, "{:.1f}")
NZ = {0.0: "Zero", 0.5: "Half", 1.0: "One"}
for (L, r, cyc), g in de.groupby(["L", "r", "cyc"]):
    for s, S in ST.items():
        n0 = g[~g.trend][f"pup_{s}"]; n1 = g[g.trend][f"pup_{s}"]; tag = nm("PD", L, NZ[r], "Cyc" if cyc else "NoCyc", S)
        put(tag + "Size", pct((n0 < .05).mean()), "{:.1f}"); put(tag + "Power", pct((n1 < .05).mean()), "{:.1f}"); put(tag + "AUC", auc(-n1, -n0), "{:.2f}")

# ---- step injection (step_injection.csv) ----
st = pd.read_csv(os.path.join(R, "step_injection.csv"))
put("SINRep", len(st[st.case == "none"])); put("SINSurr", si.NS); put("SIStepYear", si.K); put("SIL", si.L)
CN = {"none": "None", "level 0.5sd": "LevelHalf", "level 1sd": "LevelOne", "level 2sd": "LevelTwo", "noise x0.5": "NoiseHalf", "noise x1.5": "NoiseUp", "level 1sd + noise x0.5": "LevelOneNoiseHalf"}
for case, T in CN.items():
    g = st[st.case == case]
    for s, S in ST.items():
        put(f"SI{T}{S}Tau", g[f"tau_{s}"].median(), "{:+.2f}"); put(f"SI{T}{S}Up", pct((g[f"pup_{s}"] < .05).mean()), "{:.1f}"); put(f"SI{T}{S}Low", pct((g[f"plow_{s}"] < .05).mean()), "{:.1f}")

# ---- QQ of the 192 stellar p values (results/star_results.csv) ----
sr = pd.read_csv(os.path.join(RES, "star_results.csv"), dtype={"HD": str}); sr = sr[(sr.series == "S") & (sr.frac == 0.5)]
put("QQNCells", len(sr))
for col, T in (("p_upper", "Up"), ("p_D22", "Low")):
    p = sr[col].values; ks = stats.kstest(p, "uniform")
    put(f"QQ{T}Frac", pct((p < .05).mean()), "{:.1f}"); put(f"QQ{T}KSD", ks.statistic, "{:.2f}")
    for s, S in ST.items(): put(f"QQ{T}{S}Frac", pct((sr[sr["stat"] == s][col] < .05).mean()), "{:.1f}")

# ---- sensitivity of sigma_S of HD 166620 to the noise fraction f (Luhn+2022 raw series) ----
d = sc.load_luhn()
def sig(name, f):
    a, b, _ = sc.STATES[name]; g = d[(d.y >= a) & (d.y < b)]; v = g.s.var(ddof=1) - (f * g.s.mean()) ** 2
    return (math.sqrt(v) if v > 0 else float("nan")), len(g)
sg_, _ = sig("grand", sc.STATES["grand"][2])
for f, T in ((0.012, "Pub"), (0.017, "High"), (0.019, "Top")):
    s1, _ = sig("min1", f); s2, _ = sig("min2", f)
    put(f"FS{T}F", 100 * f, "{:.1f}"); put(f"FS{T}SigOne", s1, "{:.4f}"); put(f"FS{T}SigTwo", s2, "{:.4f}")
    put(f"FS{T}RatioOne", s1 / sg_, "{:.2f}"); put(f"FS{T}RatioTwo", s2 / sg_, "{:.2f}")
put("FSGrandSig", sg_, "{:.4f}")
g1 = d[(d.y >= 1971) & (d.y < 1975)]
put("FSCrossF", 100 * math.sqrt(g1.s.var(ddof=1) - sg_ ** 2) / g1.s.mean(), "{:.2f}")
ratio2 = [sig("min2", f)[0] / sg_ for f in np.arange(0.008, 0.0191, 0.001)]
put("FSRatioTwoMin", min(ratio2), "{:.1f}"); put("FSRatioTwoMax", max(ratio2), "{:.1f}")
put("FSNOne", sig("min1", 0.012)[1])

# ---- data robustness (robustness_data.csv) ----
rb = pd.read_csv(os.path.join(R, "robustness_data.csv"), dtype={"HD": str})
VN = {"base": "Base", "hkp2": "HKPTwo", "no6667": "NoStart", "min5": "MinFive"}
for v, T in VN.items():
    g = rb[rb.variant == v]
    put(f"RB{T}NSeg", g.groupby(["HD", "seg_year0"]).ngroups); put(f"RB{T}NCells", len(g))
    put(f"RB{T}Up", pct((g.p_upper < .05).mean()), "{:.1f}"); put(f"RB{T}Low", pct((g.p_D22 < .05).mean()), "{:.1f}")
b = rb[rb.variant == "base"].groupby(["HD", "config", "frac", "stat"], as_index=False).tau.median().rename(columns={"tau": "tau_b"})
h = rb[rb.variant == "hkp2"].groupby(["HD", "config", "frac", "stat"], as_index=False).tau.median()
m = h.merge(b, on=["HD", "config", "frac", "stat"])
put("RBHKPTwoFlips", int((np.sign(m.tau) != np.sign(m.tau_b)).sum())); put("RBHKPTwoMatched", len(m))
put("RBHKPTwoFlipPct", pct((np.sign(m.tau) != np.sign(m.tau_b)).mean()), "{:.0f}")
for s, S in ST.items():
    mm = m[m["stat"] == s]; put(f"RBHKPTwo{S}Corr", np.corrcoef(mm.tau, mm.tau_b)[0, 1], "{:.2f}")
mm5 = rb[rb.variant == "min5"].merge(rb[rb.variant == "base"], on=["HD", "seg_year0", "config", "frac", "stat"], suffixes=("", "_b"))
put("RBMinFiveFlips", int((np.sign(mm5.tau) != np.sign(mm5.tau_b)).sum())); put("RBMinFiveMatched", len(mm5))
ex = rb[(rb.variant == "base") & ~rb.HD.isin(["182572", "190360", "217014"])]
put("RBNoInterpNSeg", ex.groupby(["HD", "seg_year0"]).ngroups); put("RBNoInterpUp", pct((ex.p_upper < .05).mean()), "{:.1f}")

# ---- Dalton Minimum, sunspot group numbers (dalton_control.csv and the Vaquero+2016 file) ----
dc = pd.read_csv(os.path.join(R, "dalton_control.csv"))
blk = dc[(dc.block == "1795-1830") & (dc["transform"] == "raw")]
put("DALNBlocks", dc.block.nunique())
for s, S in ST.items():
    q = blk[blk["stat"] == s]
    put(f"DAL{S}TauMin", q.tau.min(), "{:+.2f}"); put(f"DAL{S}TauMax", q.tau.max(), "{:+.2f}")
    put(f"DAL{S}PLowMin", q.p_lower.min(), "{:.2f}"); put(f"DAL{S}PLowMax", q.p_lower.max(), "{:.2f}")
    put(f"DAL{S}PUpMin", q.p_upper.min(), "{:.3f}"); put(f"DAL{S}PUpMax", q.p_upper.max(), "{:.2f}")
v = pd.read_csv(os.path.join(os.path.dirname(HERE), "data", "Vaquero2016_GNobservations_JV_V1-12.csv"), comment="%")
v = v[(v.GROUPS >= 0) & (v.STATION > 0)]
an = v.groupby(["YEAR", "MONTH", "DAY"]).GROUPS.mean().reset_index().groupby("YEAR").GROUPS.agg(["mean", "size"])
for yr, tag in ((1801, "OneEightZeroOne"), (1816, "OneEightOneSix"), (1830, "OneEightThreeZero")): put(f"DALMax{tag}", an.loc[yr, "mean"], "{:.1f}")
put("DALDaysMin", 50); put("DALBlockLen", 36)
put("DALNObs", len(v)); put("DALNObservers", v.STATION.nunique())

body = "% Generated by pipeline_v2/make_macros_calibration.py from results_calibration/ (REG-MAC). Do not edit by hand.\n" + "\n".join(f"\\newcommand{{\\{k}}}{{{v}}}" for k, v in sorted(M.items())) + "\n"
open(OUT, "w", encoding="utf-8").write(body)
print(len(M), "macros ->", OUT)
