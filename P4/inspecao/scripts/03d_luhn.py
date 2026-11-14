"""Stage 3.4 - Luhn+2022 Table 2/3 (HD 166620) and the D45 recipe."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import numpy as np
from scipy import stats

from common import check, read_vizier, write_out

A10 = "audit/A10_luhn.md"
D45 = "DECISOES_D41_D54.md D45"
lu = read_vizier("J_ApJ_936_L23_table2.tsv")
lu["y"] = lu.Year.astype(float)
lu["s"] = lu.SHK.astype(float)
lu["yr"] = np.floor(lu.y).astype(int)
out = []

check("3.4-01", "Luhn Table 2 rows", 1885, len(lu), A10 + " header")
inst = lu.Inst.value_counts().to_dict()
check("3.4-02", "Inst=MW rows", 1654, inst.get("MW", 0), A10 + " §1.1")
check("3.4-03", "Inst=HIRES rows", 112, inst.get("HIRES", 0), A10 + " §1.1")
check("3.4-04", "Inst=new_MW rows (table)", 119, inst.get("new_MW", 0), A10 + " A10-F1")
check("3.4-05", "Inst=new_MW rows vs Luhn §2.2 text (158)", 158, inst.get("new_MW", 0),
      A10 + " A10-F1 (known contradiction, grade X)")
# 107 / 1547 / 9 / 103. Luhn's table carries no HKP-1/HKP-2 label, and in Baum's
# Table 1 the two photometers overlap in time for this star, so the 107/1547 split
# cannot be derived from Luhn's table by a date cut. What can be checked here:
# MW total = 107 + 1547, HIRES split at 2004.0 = 9 / 103, and the per-instrument
# labels in Baum Table 1 (check 3.3-48).
t1 = read_vizier("J_AJ_163_183_table1.tsv")
b = t1[t1.HD == "166620"].copy()
b["t"] = b.Time.astype(float)
last_hkp1 = b[b.Inst == "HKP-1"].t.max()
first_hkp2 = b[b.Inst == "HKP-2"].t.min()
mw = lu[lu.Inst == "MW"]
hi = lu[lu.Inst == "HIRES"]
check("3.4-06", "Luhn MW rows = 107 + 1547", 107 + 1547, len(mw), A10 + " §1.1")
check("3.4-06b", "Luhn HIRES rows before / from 2004.0", "9/103",
      f"{int((hi.y < 2004).sum())}/{int((hi.y >= 2004).sum())}", A10 + " §1.1")
check("3.4-06c", "HKP-1/HKP-2 split of Luhn's MW rows by a date cut at Baum's last HKP-1 "
      f"epoch ({last_hkp1:.3f}); Baum's first HKP-2 epoch is {first_hkp2:.3f} (overlap), "
      "so 107/1547 is not derivable from Luhn's table alone", "107/1547",
      f"{int((mw.y <= last_hkp1 + 1e-3).sum())}/{int((mw.y > last_hkp1 + 1e-3).sum())}",
      A10 + " §1.1", info=True)
bm = b[b.Inst.isin(["HKP-1", "HKP-2"])]
check("3.4-06d", "Baum HKP-1+HKP-2 rows for HD 166620 = Luhn MW rows", len(mw), len(bm),
      A10 + " §1.1 (Luhn retains B22 data before 1995 June 4)")
check("3.4-06e", "max |S_Luhn - S_Baum| over the MW rows matched in time order", 0,
      round(float(np.abs(np.sort(mw.s.values) - np.sort(bm.Svalue.astype(float).values)).max()), 5),
      A10 + " §2.2 quote ('No offset of S_HK applied')", tol=5e-5)
out.append(f"# Baum HD166620: last HKP-1 {last_hkp1:.4f}, first HKP-2 {first_hkp2:.4f}")
rng = lu.groupby("Inst").y.agg(["min", "max"])
check("3.4-07", "MW range", "1966.593-1995.423",
      f"{rng.loc['MW','min']:.3f}-{rng.loc['MW','max']:.3f}", A10 + " §1.1")
check("3.4-08", "new_MW range", "1995.447-2002.486",
      f"{rng.loc['new_MW','min']:.3f}-{rng.loc['new_MW','max']:.3f}", A10 + " §1.1")
check("3.4-09", "HIRES range", "1997.418-2020.185",
      f"{rng.loc['HIRES','min']:.3f}-{rng.loc['HIRES','max']:.3f}", A10 + " §1.1")
y = np.sort(lu.y.values)
d = np.diff(y)
i = int(d.argmax())
check("3.4-10", "largest gap in S_HK (yr)", 2.82, round(float(d.max()), 2), A10 + " §1.2",
      tol=0.005)
check("3.4-11", "largest gap interval", "2005.64-2008.46", f"{y[i]:.2f}-{y[i+1]:.2f}",
      A10 + " §1.2")

# annual means in the critical window (A10 §1.2 table)
exp_tab = {1990: (0.1747, 57), 1991: (0.1815, 63), 1992: (0.1821, 132), 1993: (0.1924, 84),
           1994: (0.1993, 100), 1995: (0.2126, 23), 1996: (0.1966, 22), 1997: (0.1850, 32),
           1998: (0.1838, 16), 1999: (0.1812, 12), 2000: (0.1735, 12), 2001: (0.1784, 15),
           2002: (0.1815, 5), 2004: (0.1713, 3), 2005: (0.1707, 6), 2008: (0.1708, 10),
           2009: (0.1706, 36), 2010: (0.1693, 22)}
ann = lu.groupby("yr").s.agg(["mean", "count"])
bad = [(k, v, (round(float(ann.loc[k, "mean"]), 4), int(ann.loc[k, "count"])))
       for k, v in exp_tab.items()
       if k not in ann.index or abs(ann.loc[k, "mean"] - v[0]) > 5.1e-5
       or int(ann.loc[k, "count"]) != v[1]]
check("3.4-12", "rows of the A10 §1.2 annual-mean table (18) not reproduced", 0, len(bad),
      A10 + " §1.2")
if bad:
    out.append(f"# annual table mismatches: {bad}")
yrs = [k for k in range(1995, 2003) if k in ann.index]
check("3.4-13", "annual S_HK means available 1995-2002", 8, len(yrs),
      "DECISOES_D41_D54.md D46")
n9502 = int(ann.loc[1995:2002, "count"].sum())
check("3.4-14", "raw S_HK observations with 1995.0 <= t < 2002.0", 132,
      int(((lu.y >= 1995) & (lu.y < 2002)).sum()), "paper_state_v6.md §5")
v = {"calendar years 1995-2002 inclusive (the 8 annual means of D46)": n9502,
     "same, excluding HIRES": int(((lu.yr >= 1995) & (lu.yr <= 2002) & (lu.Inst != "HIRES")).sum()),
     "new_MW only": int(inst.get("new_MW", 0))}
check("3.4-15", "the '132' of paper_state_v6 §5 under other readings of '1995-2002'", "",
      str(v), "paper_state_v6.md §5 (window labelled 1995-2002, same label as the 8 annual means)",
      info=True)

# Luhn Table 3 (APT)
l3 = read_vizier("J_ApJ_936_L23_table3.tsv")
l3["yr"] = np.floor(l3.Year.astype(float)).astype(int)
check("3.4-16", "Luhn Table 3 rows", 1278, len(l3), A10 + " §1.1")
check("3.4-17", "APT calendar years with data", 17, l3.yr.nunique(), A10 + " §1.1")
check("3.4-18", "APT calendar years 2005-2015 with data", 0,
      int(l3.yr.between(2005, 2015).sum()), A10 + " §1.1")
check("3.4-19", "APT calendar years 1993-2004 with data", 12,
      int(l3[l3.yr.between(1993, 2004)].yr.nunique()), "DECISOES_D41_D54.md D46")
npy = l3[l3.yr.between(1993, 2004)].groupby("yr").size()
check("3.4-20", "APT nights per year 1993-2004 (min-max)", "47-119",
      f"{npy.min()}-{npy.max()}", A10 + " §1.2")

l3["m"] = l3.mag.astype(float)
sm = l3.groupby("yr").m.mean()
pre, post = sm[sm.index <= 2003], sm[sm.index >= 2004]
check("3.4-20b", "APT seasonal means (calendar years): range before 2004 (mmag)", 2.8,
      round(1000 * float(pre.max() - pre.min()), 1), A10 + " §1.3", tol=0.05)
check("3.4-20c", "APT seasonal means: std over 2004 + 2016-2020 (mmag, ddof=1 | ddof=0)", 0.22,
      f"{1000*post.std(ddof=1):.2f} | {1000*post.std(ddof=0):.2f}",
      A10 + " §1.3 (A10 recomputation; Luhn's text says 0.35)", info=True)
post2 = sm[sm.index >= 2016]
check("3.4-20d", "same, 2016-2020 only (ddof=1) | range before 2005 (mmag)", "",
      f"{1000*post2.std(ddof=1):.2f} | {1000*float(sm[sm.index<=2004].max()-sm[sm.index<=2004].min()):.1f}",
      "variant", info=True)

# ---- three states --------------------------------------------------------
states = {"min1": (1971.0, 1975.0, 0.012, 0.1810, 0.0035, 44, 0.0027),
          "min2": (1987.0, 1991.0, 0.012, 0.1724, 0.0058, 315, 0.0054),
          "grand": (2004.0, 9999.0, 0.003, 0.1705, 0.0020, 103, 0.0019)}
res = {}
k = 21
for name, (a, bnd, noise, emean, eraw, en, ecorr) in states.items():
    g = lu[(lu.y >= a) & (lu.y < bnd)]
    m, s1, s0 = g.s.mean(), g.s.std(ddof=1), g.s.std(ddof=0)
    nz = noise * m
    c1 = float(np.sqrt(s1**2 - nz**2))
    c0 = float(np.sqrt(s0**2 - nz**2))
    # seasonal variant: sigma inside each calendar-year season, then the same quadrature
    ss = g.groupby("yr").s.agg(["count", "mean", "std"])
    ss = ss[ss["count"] > 1]
    res[name] = dict(n=len(g), m=m, s1=s1, c1=c1, ss=ss, nz=nz)
    check(f"3.4-{k}", f"{name}: N in interval", en, len(g), A10 + " §1.3"); k += 1
    check(f"3.4-{k}", f"{name}: <S_HK> (4 dec)", f"{emean:.4f}", f"{m:.4f}",
          A10 + " §1.3"); k += 1
    check(f"3.4-{k}", f"{name}: raw std of the whole interval (ddof=1, 4 dec)",
          f"{eraw:.4f}", f"{s1:.4f}", A10 + " §1.4"); k += 1
    check(f"3.4-{k}", f"{name}: noise = {noise*100:.1f}% of <S_HK> (4 dec)", "",
          f"{nz:.4f}", A10 + " §1.4", info=True); k += 1
    check(f"3.4-{k}", f"{name}: corrected sigma_S, interval-wide std minus noise in "
          "quadrature (ddof=1, 4 dec)", f"{ecorr:.4f}", f"{c1:.4f}", D45); k += 1
    check(f"3.4-{k}", f"{name}: same, 5 decimals, ddof=1 | ddof=0", "",
          f"{c1:.5f} | {c0:.5f}", "variant", info=True); k += 1
    sq = np.sqrt(np.clip(ss["std"]**2 - (noise * ss["mean"])**2, 0, None))
    check(f"3.4-{k}", f"{name}: D45 step (1) read literally - sigma inside each calendar-year "
          "season, noise removed in quadrature per season; mean | median over seasons "
          f"(n seasons={len(ss)})", f"{ecorr:.4f}",
          f"{sq.mean():.4f} | {sq.median():.4f}", D45 + " step (1), literal reading",
          info=True); k += 1
    out.append(f"# {name} seasonal table\n{ss.round(5).to_string()}")

# ---- F-test --------------------------------------------------------------


def ftest(sa, na, sb, nb):
    f = sa**2 / sb**2
    p1 = float(stats.f.sf(f, na - 1, nb - 1))
    return f, p1, 2 * p1


EXP_P = 8.78e-6
a, g = res["min1"], res["grand"]
f, p1, p2 = ftest(a["s1"], a["n"], g["s1"], g["n"])
check("3.4-50", "F-test min1 vs grand on RAW interval variances, two-sided p",
      EXP_P, p2, A10 + " §1.4 item 4 (Luhn §3.1)", tol=0.05e-6)
check("3.4-51", "same, one-sided p", "", p1, "variant", info=True)
f, p1, p2 = ftest(a["c1"], a["n"], g["c1"], g["n"])
check("3.4-52", "F-test min1 vs grand on noise-CORRECTED sigma_S (D45 steps 2 then 3), "
      "two-sided p", EXP_P, p2, D45 + " / paper_state_v6.md §2", tol=0.05e-6)
check("3.4-53", "same, one-sided p", "", p1, "variant", info=True)
f, p1, p2 = ftest(0.0027, 44, 0.0019, 103)
check("3.4-54", "F-test using the published rounded values 0.0027 (N=44) vs 0.0019 (N=103), "
      "two-sided p", EXP_P, p2, D45, tol=0.05e-6)
b2 = res["min2"]
f, p1, p2 = ftest(b2["c1"], b2["n"], g["c1"], g["n"])
check("3.4-55", "F-test min2 vs grand on corrected sigma_S, two-sided p", "", p2,
      "not in the documents", info=True)
# seasonal-sample F-test: seasons as the sampling unit
sa, sg = a["ss"]["std"], g["ss"]["std"]
check("3.4-56", "seasons with >1 obs: min1 | min2 | grand", "",
      f"{len(a['ss'])} | {len(b2['ss'])} | {len(g['ss'])}", "variant", info=True)
hir = lu[(lu.Inst == "HIRES") & (lu.y >= 2004)].groupby("yr").s.agg(["count", "mean", "std"])
hir = hir[hir["count"] > 1]
rel = 100 * hir["std"] / hir["mean"]
check("3.4-57", "Keck seasons (calendar years, >1 obs) with sigma_S/<S> below 1.2 %, out of N",
      "6/9", f"{int((rel < 1.2).sum())}/{len(hir)}",
      A10 + " §1.4 item 2 (Luhn quote: 'less than this in six of the nine seasons')")
check("3.4-57b", "same, below 0.3 % (the reading suggested by the order of A10 §1.4 item 2)",
      "6/9", f"{int((rel < 0.3).sum())}/{len(hir)}", A10 + " §1.4 item 2", info=True)
check("3.4-57c", "two lowest Keck seasonal sigma_S/<S> (%)", "approach 0.3",
      ", ".join(f"{x:.3f}" for x in sorted(rel)[:2]), A10 + " §1.4 item 2", info=True)
out.append("# Keck seasonal relative sigma (%)\n" + rel.round(3).to_string())
y14 = lu[lu.yr == 2014]
check("3.4-58", "2014: N obs | S", "1 | 0.1776",
      f"{len(y14)} | {y14.s.iloc[0]:.4f}" if len(y14) else "0", A10 + " A10-F7")

# ---- numeric fingerprint of the new_MW rows (A13-F2) -------------------------
def ndec(x):
    return len(x.strip().rstrip("0").split(".")[-1]) if "." in x else 0


for inst_name in ("MW", "HIRES", "new_MW"):
    g = lu[lu.Inst == inst_name]
    dm = max(ndec(x) for x in g.SHK)
    fr = (g.JD.astype(float) % 1).round(2).nunique()
    check(f"3.4-60 {inst_name}", f"{inst_name}: rows | max decimals in S_HK | distinct JD fractional parts",
          "", f"{len(g)} | {dm} | {fr}", "data/J_ApJ_936_L23_table2.tsv (A13-F2)", info=True)
nm = lu[lu.Inst == "new_MW"]
check("3.4-61", "new_MW rows with S_HK given to more than 4 decimals", "119/119",
      f"{int(sum(ndec(x) > 4 for x in nm.SHK))}/{len(nm)}", "A13-F2; Luhn arXiv:2207.00612 §2.2 '119 (scraped) observations'")
check("3.4-62", "MW and HIRES rows with S_HK given to more than 4 decimals", 0,
      int(sum(ndec(x) > 4 for x in lu[lu.Inst != "new_MW"].SHK)), "data/J_ApJ_936_L23_table2.tsv")
dup = nm[nm.duplicated("JD", keep=False)]
check("3.4-63", "new_MW rows sharing an epoch with another row (same JD, different S_HK)", "",
      len(dup), "A13-F2", info=True)

write_out("03d_luhn.txt", "\n".join(out) + "\n")
