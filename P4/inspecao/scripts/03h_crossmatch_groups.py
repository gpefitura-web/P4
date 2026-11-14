"""Stages 3.8 and 3.9 - cross-matches and the P4 candidate groups."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import re

import numpy as np

from common import check, isnum, read_csv, read_vizier, write_out

A9 = "audit/A9_baum.md"
A6 = "audit/A6_saar.md"
A12 = "audit/A12_noyes.md"
out = []
b = read_csv("baliunas_table2_full.csv")
b["bvf"] = b.bv.astype(float)
t2 = read_vizier("J_163_183_table2.tsv")
t2["ClassTP"] = t2.ClassTP.str.strip()
t2["ClassB95"] = t2.ClassB95.str.strip()
c59 = read_csv("baum2022_59stars.csv")
cp = read_csv("baum2022_cycle_periods.csv")

# ---- 3.8 Baum x A1 -------------------------------------------------------
inA1 = t2[t2.HD.isin(b.HD)]
check("3.8-01", "Baum stars present in the A1 catalogue by HD", 27, len(inA1), A9 + " §2")
check("3.8-02", "Baum stars with ClassB95 filled", 26,
      int((t2.ClassB95 != "").sum()), A9 + " §2")
diff = sorted(set(inA1.HD) - set(t2.HD[t2.ClassB95 != ""]))
check("3.8-03", "in A1 by HD but ClassB95 blank", "185144", ",".join(diff), A9 + " A9-F2")
check("3.8-04", "ClassB95 filled but HD not in A1", "",
      ",".join(sorted(set(t2.HD[t2.ClassB95 != ""]) - set(b.HD))) or "none",
      "implicit", info=True)
r = b[b.HD == "185144"].iloc[0]
check("3.8-05", "HD 185144 in A1 (class|P_cyc|FAP|grade)", "CYCLE|||A",
      f"{r.primary_class}|{r.P_cyc}|{r.FAP}|{r.grade}", A9 + " A9-F2")
check("3.8-06", "baum2022_59stars.csv em_baliunas_A1 == True", 27,
      int((c59.em_baliunas_A1 == "True").sum()), A9 + " §2")
def norm(x):
    """Compare cells as numbers when numeric ('2.6' == '2.60'), else as strings."""
    return f"{float(x):.6g}" if isnum(x) else x


j = c59[c59.em_baliunas_A1 == "True"].merge(b, on="HD")
bad = sum(int((j[a].map(norm) != j[c].map(norm)).sum())
          for a, c in [("class_A1", "primary_class"), ("FAP_A1", "FAP"), ("P_cyc_A1", "P_cyc"),
                       ("dP_A1", "dP"), ("bv_A1", "bv")])
check("3.8-07", "A1 columns copied into baum2022_59stars.csv that differ in value from the "
      "catalogue", 0, bad, "baum2022_59stars.csv vs baliunas_table2_full.csv")


def b95_kind(s):
    """Type of a Baum 'ClassB95' cell: cycle / flat / flat? / long / var."""
    s = s.lower()
    if re.search(r"\d", s) or s in ("poor", "fair", "good", "excl"):
        return "cycle"
    return s


def tp_kind(s):
    return "cycle" if re.match(r"^\d", s) else s.lower()


both = t2[t2.ClassB95 != ""].copy()
both["k95"] = both.ClassB95.map(b95_kind)
both["ktp"] = both.ClassTP.map(tp_kind)
out.append("# ClassB95 -> ClassTP for the 26 common stars\n"
           + both[["HD", "ClassB95", "ClassTP", "k95", "ktp"]].to_string())
strict = both[both.k95.str.rstrip("?") != both.ktp.str.rstrip("?")]
loose = both[both.k95 != both.ktp]
NAMED = ("100180 101501 10780 115617 126053 143761 182572 188512 190406 217014 22072 37394 "
         "3795 9562").split()  # the list A9 §2 labels 'treze'
check("3.8-08", "of the 26, stars changing class TYPE (cycle/flat/long/var; 'flat?' and "
      "'flat' one type)", 13, len(strict), A9 + " §2 ('treze' by change of type)")
check("3.8-09", "HD numbers actually listed in A9 §2 under the label 'treze'", 13,
      len(NAMED), A9 + " §2")
check("3.8-10", "listed in A9 §2 but with no change of type in Table 2", "none",
      ",".join(sorted(set(NAMED) - set(strict.HD))) or "none", A9 + " §2")
check("3.8-11", "of the 26, stars whose class changes when 'flat?' -> 'flat' also counts "
      "(the rule A9 §2 applies to HD 10700)", 14, len(loose),
      A9 + " §2 ('Total 14', checksum 6); DECISOES_D41_D54.md D43")
check("3.8-11b", "'flat?' -> 'flat' stars among the 26", "10700",
      ",".join(sorted(set(loose.HD) - set(strict.HD))), A9 + " §2 (names only HD 10700)")
check("3.8-11c", "stars with cycle -> cycle but a different period (not a change of type)",
      "", ",".join(f"{h}:{a}->{c}" for h, a, c in zip(both.HD, both.ClassB95, both.ClassTP)
                   if b95_kind(a) == "cycle" and tp_kind(c) == "cycle"),
      "data/J_163_183_table2.tsv", info=True)
out.append("# strict type changes: " + ",".join(sorted(strict.HD)))
# Baum's transcription of B95 vs the A1 catalogue
bj = both.merge(b, on="HD", how="left")
mis = []
for _, x in bj.iterrows():
    a1 = x.primary_class
    k = {"CYCLE": "cycle", "Flat": "flat", "Flat?": "flat?", "Long": "long", "Var": "var"}.get(a1)
    if k != x.k95:
        mis.append((x.HD, x.ClassB95, a1))
tent = [(x.HD, x.ClassB95, x.P_cyc, x.FAP) for _, x in bj.iterrows()
        if x.k95 == "cycle" and x.P_cyc == ""]
check("3.8-12", "of the 26, stars where Baum's ClassB95 type differs from A1 primary_class",
      0, len(mis), "implicit (Baum transcribes B95)")
if mis:
    out.append(f"# Baum B95 transcription vs A1: {mis}")
check("3.8-12b", "stars for which Baum's ClassB95 carries a B95 period/grade while the A1 "
      "catalogue has P_cyc blank (HD:ClassB95:P_cyc_A1:FAP_A1)", "",
      "; ".join(f"{h}:{c}:'{p}':'{f}'" for h, c, p, f in tent) or "none",
      "data/J_163_183_table2.tsv vs baliunas_table2_full.csv", info=True)

# ---- 14 periods ----------------------------------------------------------
check("3.8-13", "rows in baum2022_cycle_periods.csv", 14, len(cp),
      "DECISOES_D41_D54.md D42")
meth = cp.metodo_baum.str.contains("olho")
check("3.8-14", "periods 'by periodogram' / 'by eye'", "10/4",
      f"{int((~meth).sum())}/{int(meth.sum())}", "DECISOES_D41_D54.md D42")
num = t2[t2.ClassTP.str.match(r"^\d")]
pt = {h: float(re.match(r"[\d.]+", c).group()) for h, c in zip(num.HD, num.ClassTP)}
q = {h: "?" in c for h, c in zip(num.HD, num.ClassTP)}
bad = [(h, p, pt.get(h)) for h, p in zip(cp.HD, cp.P_baum_yr.astype(float))
       if pt.get(h) != p]
check("3.8-15", "CSV periods differing from Table 2 ClassTP", 0,
      len(bad) + len(set(pt) ^ set(cp.HD)), "baum2022_cycle_periods.csv vs data/J_163_183_table2.tsv")
badm = [h for h, m in zip(cp.HD, meth) if q.get(h) != bool(m)]
check("3.8-16", "CSV 'metodo_baum' inconsistent with the '?' mark in Table 2", 0, len(badm),
      "baum2022_cycle_periods.csv vs data/J_163_183_table2.tsv")
check("3.8-17", "distinct stars marked '?' in Table 2 (A9-F1 lists 'HD 101501, 166620, "
      "190406, 4628, mais HD 4628')", 4, int(sum(q.values())), A9 + " A9-F1")
# delta / sigma table of A9-F3
expF3 = {"26965": -2.0, "219834B": -3.0, "166620": 4.0, "10476": 7.0, "152391": -9.0,
         "4628": 20.0}
bb = b.set_index("HD")
rows = []
for h in cp.HD:
    if h in bb.index and isnum(bb.loc[h, "P_cyc"]):
        d = pt[h] - float(bb.loc[h, "P_cyc"])
        rows.append((h, bb.loc[h, "P_cyc"], bb.loc[h, "dP"], bb.loc[h, "FAP"], pt[h],
                     round(d, 2), round(d / float(bb.loc[h, "dP"]), 2)))
out.append("# Baum vs Baliunas periods: HD, P_B95, dP, FAP, P_Baum, delta, delta/sigma\n"
           + "\n".join(map(str, rows)))
check("3.8-18", "stars with a numeric period in both Baum and A1", 7, len(rows),
      A9 + " A9-F3")
got = {r[0]: r[6] for r in rows}
badF3 = [(h, v, got.get(h)) for h, v in expF3.items() if abs(got.get(h, 1e9) - v) > 0.5]
check("3.8-19", "rows of the A9-F3 table whose delta/sigma is not reproduced (tol 0.5)", 0,
      len(badF3), A9 + " A9-F3")
check("3.8-20", "HD 4628 delta/sigma: recomputed | CSV | A9-F3 text", "20.4 | 20.4 | +20",
      f"{got['4628']:.1f} | {float(cp[cp.HD=='4628'].delta_sigma.iloc[0]):.1f} | +20",
      A9 + " A9-F3", info=True)
check("3.8-21", "all overlapping periods diverge by >= 2 sigma (|delta/sigma| min, "
      "HD 190406 excluded as a change of primary)", ">=2",
      round(min(abs(v) for h, v in got.items() if h != "190406"), 2), A9 + " A9-F3",
      info=True)
check("3.8-22", "FAP Excellent among the 7 overlapping", 6,
      sum(1 for r in rows if r[3] == "Excellent"), A9 + " A9-F3")
check("3.8-23", "HD 190406 delta_sigma stored in the CSV (A9-F3 prints 'troca de primario')",
      "", cp[cp.HD == "190406"].delta_sigma.iloc[0], "baum2022_cycle_periods.csv", info=True)
badd = [(h, ds, got.get(h)) for h, ds in zip(cp.HD, cp.delta_sigma)
        if ds != "" and abs(float(ds) - got.get(h, 1e9)) > 0.05]
check("3.8-24", "CSV delta_sigma differing from recomputation", 0, len(badd),
      "baum2022_cycle_periods.csv")
check("3.8-25", "CSV rows with class_baliunas filled but star absent from A1", 0,
      int(((cp.class_baliunas != "") & ~cp.HD.isin(b.HD)).sum()), "baum2022_cycle_periods.csv")
nn = t2.set_index("HD")
badn = [h for h in cp.HD if int(cp[cp.HD == h].N_obs.iloc[0]) != int(nn.loc[h, "Nobs"])
        or int(cp[cp.HD == h].baseline_yr.iloc[0]) != int(nn.loc[h, "Base"])]
check("3.8-26", "CSV N_obs/baseline differing from Table 2", 0, len(badn),
      "baum2022_cycle_periods.csv")

# ---- Saar cross-match ----------------------------------------------------
s = read_csv("audit/saar_baliunas_crossmatch.csv")
check("3.8-30", "rows in saar_baliunas_crossmatch.csv", 70, len(s), A6 + " §2")
t5only = s[s.saar_notes.str.contains("Table 5 only")]
t1rows = s[~s.saar_notes.str.contains("Table 5 only")]
check("3.8-31", "Saar Table 1 entries / Table 5-only rows", "61/9",
      f"{len(t1rows)}/{len(t5only)}", A6 + " §2")
check("3.8-32", "Saar Table 1 entries flagged in_bal_catalogue", 59,
      int((t1rows.in_bal_catalogue == "True").sum()), A6 + " §2")
check("3.8-33", "Saar Table 1 entries actually present in the catalogue by HD", 59,
      int(t1rows.HD.isin(b.HD).sum()), A6 + " §2")
check("3.8-34", "Table 1 entries not in the catalogue", "98230B,Sun",
      ",".join(sorted(t1rows.HD[~t1rows.HD.isin(b.HD)])), A6 + " §2")
check("3.8-35", "Table 5-only rows: present in catalogue by HD | in_bal_catalogue filled | "
      "bal_class filled", "", f"{int(t5only.HD.isin(b.HD).sum())} | "
      f"{int((t5only.in_bal_catalogue != '').sum())} | {int((t5only.bal_class != '').sum())}",
      "audit/saar_baliunas_crossmatch.csv (not stated in A6)", info=True)


def pnum(x):
    return float(x) if isnum(x) else None


pairs = t1rows[t1rows.saar_Pcyc.map(isnum) & t1rows.bal_Pcyc.map(isnum)]
check("3.8-36", "pairs with a plain numeric primary period in both papers (CSV; Sun row has "
      "no Baliunas values in the CSV)", 30, len(pairs), A6 + " §2")
sunrow = s[s.HD == "Sun"].iloc[0]
check("3.8-37", "Sun row in CSV: bal_class|bal_Pcyc|in_bal_catalogue", "",
      f"{sunrow.bal_class}|{sunrow.bal_Pcyc}|{sunrow.in_bal_catalogue}",
      A6 + " §2.1 lists the Sun among the 24 identical pairs", info=True)
ident = pairs[pairs.saar_Pcyc.astype(float) == pairs.bal_Pcyc.astype(float)]
check("3.8-38", "numeric pairs identical in value (CSV)", "", len(ident),
      A6 + " §2.1 ('24 of 30 identical', list of 22 HD + Sun + HD 100180)", info=True)
named24 = ("1835 18256 20630 76151 78366 114710 152391 156026 10476 16160 26965 32147 103095 "
           "115404 160346 166620 190406 201091 219834B 155885 194012 206860").split()
check("3.8-39", "HD numbers named in A6 §2.1 as identical (excluding Sun and HD 100180)", "",
      len(named24), A6 + " §2.1", info=True)
check("3.8-40", "named-identical stars that are NOT identical in the CSV", 0,
      len(set(named24) - set(ident.HD)), A6 + " §2.1")
check("3.8-41", "identical pairs in the CSV not named in A6 §2.1", "",
      ",".join(sorted(set(ident.HD) - set(named24))) or "none", A6 + " §2.1", info=True)
dv = pairs[pairs.saar_Pcyc.astype(float) != pairs.bal_Pcyc.astype(float)]
check("3.8-42", "numeric pairs differing (CSV)", "100180,149661,165341A,201092,3651,4628,81809",
      ",".join(sorted(dv.HD)), A6 + " §2.2 (6 rows: 165341A, 201092, 149661, 3651, 4628, 100180)",
      info=True)
out.append("# differing pairs\n" + dv[["HD", "saar_Pcyc", "bal_Pcyc", "bal_dP", "diff_pct"]].to_string())
jb = t1rows.merge(b, on="HD")
badb = sum(int((jb[a].map(norm) != jb[c].map(norm)).sum())
           for a, c in [("bal_class", "primary_class"), ("bal_FAP", "FAP"), ("bal_Pcyc", "P_cyc"),
                        ("bal_dP", "dP"), ("bal_S", "S"), ("bal_sec", "secondary")])
check("3.8-43", "Baliunas columns in the cross-match that differ from the catalogue", 0, badb,
      "audit/saar_baliunas_crossmatch.csv vs baliunas_table2_full.csv")
cls = jb.primary_class.value_counts().to_dict()
check("3.8-44", "Baliunas classes of Saar's 59 matched stars CYCLE/Long/Var/Flat?/Flat",
      "42/9/7/1/0", "/".join(str(cls.get(k, 0)) for k in ("CYCLE", "Long", "Var", "Flat?", "Flat")),
      A6 + " §2.5")
STD17 = ("9562 13421 29645 45067 76572 89744 107213 124570 136202 142373 143761 159332 "
         "187013 187691 207978 212754 216385").split()  # A6 §3
flagged = set(s.HD[s.bal_T1_sigmaS_pct != ""])
check("3.8-45", "of the 17 Baliunas standard stars (A6 §3), flagged in the cross-match "
      "(bal_T1_sigmaS_pct filled)", 17, len(flagged & set(STD17)),
      A6 + " §6 decision 6 ('the flag has been added')")
check("3.8-46", "standard stars absent from the cross-match file", "",
      ",".join(sorted(set(STD17) - set(s.HD), key=int)) or "none", A6 + " §3", info=True)
check("3.8-47", "standard stars in the A1 catalogue", 17, int(b.HD.isin(STD17).sum()),
      A6 + " §3")
fl = b[b.primary_class == "Flat"]
check("3.8-48", "Flat stars that are standards", 7, int(fl.HD.isin(STD17).sum()),
      A6 + " A6-F7")
check("3.8-49", "Flat? stars that are standards", 1,
      int(b[b.primary_class == "Flat?"].HD.isin(STD17).sum()), A6 + " A6-F7")
T5 = "9562 10700 45067 89744 107213 124570 143761 178428 207978 212754".split()
check("3.8-50", "Saar Table 5 F stars that are standards", 8, len(set(T5) & set(STD17)),
      A6 + " A6-F7")
t5c = b[b.HD.isin(T5)].primary_class.value_counts().to_dict()
check("3.8-51", "Baliunas classes of Saar's 10 F stars Flat/Long/Flat?", "5/4/1",
      f"{t5c.get('Flat',0)}/{t5c.get('Long',0)}/{t5c.get('Flat?',0)}", A6 + " A6-F4")

# ---- 3.9 groups ----------------------------------------------------------
APPB = "3443 39587 76572 81809 88355 114378 124570 137107 141004 156026 158614 178428".split()
flat_all = b[b.primary_class.isin(["Flat", "Flat?"])]
nonstd = flat_all[~flat_all.HD.isin(STD17)]
check("3.9-01", "Flat+Flat? stars that are not standards (D13 alone)", 5, len(nonstd),
      "P4_RESEARCH_NOTEBOOK.md D13; " + A9 + " §2.1 ('5 estrelas, pos-D13')")
out.append("# Flat/Flat? non-standard: " + ",".join(nonstd.HD))
clean = nonstd[~nonstd.HD.isin(APPB)]
EXP5 = sorted(["43587", "10700", "190360", "182572", "23249"])
check("3.9-02", "Flat+Flat? non-standard AND not in Baliunas Appendix B binary list "
      "(A1 §2.5) - inferred rule, the defining document is missing", ",".join(EXP5),
      ",".join(sorted(clean.HD)), A9 + " §2.1 (list); rule not stated in any file present")
check("3.9-03", "the two non-standard Flat stars left out of the 'five'", "",
      ",".join(sorted(set(nonstd.HD) - set(EXP5))), "A1 §2.5 lists both in Appendix B",
      info=True)
five = b[b.HD.isin(EXP5)]
check("3.9-04", "of the five, in Baum", 4, int(five.HD.isin(t2.HD).sum()), A9 + " §2.1")
check("3.9-05", "of the five, absent from Baum", "43587",
      ",".join(sorted(set(EXP5) - set(t2.HD))), A9 + " §2.1")
check("3.9-06", "spectral types of the five containing IV or Vp (as OCR'd: 'Iv', 'IV', 'Vp')",
      3, int(five.sptype.str.contains(r"I[Vv]|Vp").sum()),
      "P4_RESEARCH_NOTEBOOK.md Q7 ('Tres das cinco elegiveis sao IV/Vp')")
out.append("# five clean Flat\n" + five[["HD", "bv", "sptype", "S", "primary_class"]].to_string())
ce = b[(b.primary_class == "CYCLE") & (b.FAP == "Excellent")]
EXP13 = ["4628", "10476", "16160", "26965", "32147", "81809", "103095", "152391", "160346",
         "166620", "201091", "219834B", "(Sun)"]
check("3.9-07", "CYCLE + FAP Excellent rows", 13, len(ce), A9 + " §2.1")
check("3.9-08", "CYCLE+Excellent set equals the A9 §2.1 list", 0,
      len(set(ce.HD) ^ set(EXP13)), A9 + " §2.1")
check("3.9-09", "of the 13, in Baum", 6, int(ce.HD.isin(t2.HD).sum()), A9 + " §2.1")
check("3.9-10", "of the 13, absent from Baum (the Sun row included)", 7,
      int((~ce.HD.isin(t2.HD)).sum()), A9 + " A9-F5 ('os sete ausentes')")
absent = ce[~ce.HD.isin(t2.HD)]
check("3.9-11", "B-V of the absent controls (Sun excluded)", "0.96-1.18 or binary",
      "; ".join(f"{h}={v}" for h, v in zip(absent.HD, absent.bv) if h != "(Sun)"),
      "paper_state_v6.md §3.1", info=True)
# P_cyc and B-V printed in A9 §2.1
expP = {"4628": ("8.37", "0.08", "0.88"), "10476": ("9.6", "0.1", "0.84"),
        "16160": ("13.2", "0.2", "0.98"), "26965": ("10.1", "0.1", "0.82"),
        "32147": ("11.1", "0.2", "1.06"), "81809": ("8.17", "0.08", "0.64"),
        "103095": ("7.3", "0.08", "0.75"), "152391": ("10.9", "0.2", "0.76"),
        "160346": ("7.0", "0.08", "0.96"), "166620": ("15.8", "0.3", "0.87"),
        "201091": ("7.3", "0.1", "1.18"), "219834B": ("10.0", "0.2", "0.91"),
        "(Sun)": ("10.0", "0.1", "0.66")}
badp = [h for h, (p, dp, bv) in expP.items()
        if not (float(bb.loc[h, "P_cyc"]) == float(p) and float(bb.loc[h, "dP"]) == float(dp)
                and float(bb.loc[h, "bv"]) == float(bv))]
check("3.9-12", "rows of the A9 §2.1 control table whose P, dP or B-V differ from the catalogue",
      0, len(badp), A9 + " §2.1")
tp = t2.set_index("HD").ClassTP
expTP = {"4628": "10.0?", "10476": "10.3", "26965": "9.9", "152391": "9.1", "166620": "17.0?",
         "219834B": "9.4", "10700": "flat", "190360": "flat", "182572": "var", "23249": "flat"}
check("3.9-13", "Baum classes printed in A9 §2.1 that differ from Table 2", 0,
      sum(1 for h, v in expTP.items() if tp.get(h) != v), A9 + " §2.1")

# A12-F1: validity band by group
ins = lambda d, lo=0.44, hi=0.82, closed=True: int(((d.bvf >= lo) & (d.bvf <= hi)).sum()) \
    if closed else int(((d.bvf > lo) & (d.bvf < hi)).sum())
check("3.9-14", "five clean Flat inside 0.44-0.82 (closed interval)", 4, ins(five),
      A12 + " A12-F1")
check("3.9-15", "13 CYCLE+Excellent inside 0.44-0.82 (closed interval, Sun included)", 5,
      ins(ce), A12 + " A12-F1")
check("3.9-16", "13 CYCLE+Excellent inside the OPEN interval 0.44 < B-V < 0.82 "
      "(HD 26965 sits at 0.82)", 5, ins(ce, closed=False), A12 + " A12-F1; D53")
check("3.9-17", "CYCLE+Excellent with B-V > 1.0", "201091,32147",
      ",".join(sorted(ce.HD[ce.bvf > 1.0])), A12 + " A12-F1")
ce_ns = ce[ce.HD != "(Sun)"]
check("3.9-18", "12 stellar CYCLE+Excellent (Sun row excluded): inside / outside (closed)",
      "", f"{ins(ce_ns)}/{len(ce_ns) - ins(ce_ns)}", "variant", info=True)
ce_b = ce[ce.HD.isin(t2.HD)]
five_b = five[five.HD.isin(t2.HD)]
check("3.9-19", "restricted to stars in Baum: Flat inside/total | CYCLE+Excellent inside/total",
      "", f"{ins(five_b)}/{len(five_b)} | {ins(ce_b)}/{len(ce_b)}",
      "variant relevant to Q1 option (ii) x Q8", info=True)
# Same count with the B-V published in CLS V Table 2 for the stars that are there
i2 = read_vizier("J_ApJS_274_35_table2.tsv").set_index("Name")
rows = []
for h in list(five.HD) + list(ce_ns.HD):
    name = "HD " + h
    bv_cls = float(i2.loc[name, "B-V"]) if name in i2.index else None
    rows.append((h, float(bb.loc[h, "bv"]), bv_cls))
out.append("# B-V: A1 catalogue vs CLS V Table 2 (None = star not in CLS V)\n"
           + "\n".join(f"{h}: A1={a} CLSV={c}" for h, a, c in rows))
have = [(h, a, c) for h, a, c in rows if c is not None]
dbv = [round(a - c, 3) for h, a, c in have]
check("3.9-20", "P4 candidate stars also in CLS V Table 2", "", len(have), "variant", info=True)
check("3.9-21", "B-V(A1 catalogue) - B-V(CLS V): min | median | max over those stars", "",
      f"{min(dbv)} | {float(np.median(dbv))} | {max(dbv)}",
      "baliunas_table2_full.csv vs data/J_ApJS_274_35_table2.tsv", info=True)
flip = [f"{h}: {a}->{c}" for h, a, c in have
        if (0.44 <= a <= 0.82) != (0.44 <= c <= 0.82) or (a > 1.0) != (c > 1.0)]
check("3.9-22", "candidate stars whose Noyes band changes if CLS V's B-V is used", "",
      "; ".join(flip) or "none", A12 + " A12-F1 (band assignment used A1 B-V only)", info=True)
ce_cls = [(h, a, c) for h, a, c in have if h in set(ce_ns.HD)]
check("3.9-23", "CYCLE+Excellent stars in CLS V: inside 0.44-0.82 with A1 B-V | with CLS V B-V "
      "| N", "", f"{sum(0.44 <= a <= 0.82 for h, a, c in ce_cls)} | "
      f"{sum(0.44 <= c <= 0.82 for h, a, c in ce_cls)} | {len(ce_cls)}", "variant", info=True)
# all catalogue stars in CLS V
allr = [(h, float(v), float(i2.loc["HD " + h, "B-V"])) for h, v in zip(b.HD, b.bv)
        if "HD " + h in i2.index and isnum(i2.loc["HD " + h, "B-V"])]
dd = np.array([a - c for h, a, c in allr])
check("3.9-24", "all A1 catalogue stars found in CLS V: N | median(A1 - CLSV) | "
      "N with |diff| > 0.03", "", f"{len(allr)} | {np.median(dd):.3f} | {int((abs(dd) > 0.03).sum())}",
      "baliunas_table2_full.csv vs data/J_ApJS_274_35_table2.tsv", info=True)
out.append("# all A1 x CLS V B-V pairs\n" + "\n".join(f"{h}: {a} vs {c} ({a-c:+.3f})"
                                                       for h, a, c in allr))

# medians of B-V (paper_state_v5 §4 and A12 §3.1)
V5 = "paper_state_v5.md §4"


def med(d):
    return round(float(d.bvf.median()), 3)


g = lambda k: b[b.primary_class == k]
check("3.9-30", "median B-V, CYCLE + FAP Excellent (13, Sun included)", 0.88, med(ce), V5)
check("3.9-31", "median B-V, CYCLE + FAP Excellent (12, Sun excluded)", "", med(ce_ns),
      "variant", info=True)
check("3.9-32", "median B-V, Flat + Flat? (15 stars, the label printed in v5 §4)", 0.73,
      med(flat_all), V5)
check("3.9-33", "median B-V, five clean Flat (label used by A12 §3.1 for 0.73)", 0.73,
      med(five), A12 + " §3.1")
check("3.9-34", "median B-V, Var (29)", 0.61, med(g("Var")), V5)
check("3.9-35", "median B-V, Long (16)", 0.49, med(g("Long")), V5)
check("3.9-36", "median B-V, Long (16) vs A12 §3.1", 0.525, med(g("Long")), A12 + " §3.1")
check("3.9-37", "median B-V, Flat (11)", 0.56, med(g("Flat")), A12 + " §3.1")
check("3.9-38", "median B-V, Flat? (4)", 0.665, med(g("Flat?")), A12 + " §3.1")
check("3.9-39", "median B-V, CYCLE (52)", 0.725, med(g("CYCLE")), A12 + " §3.1")
check("3.9-40", "median B-V, 7 non-standard Flat+Flat? (D13 only)", "", med(nonstd),
      "variant", info=True)
check("3.9-41", "median B-V, Long non-standard", "",
      f"{med(g('Long')[~g('Long').HD.isin(STD17)])} (n={int((~g('Long').HD.isin(STD17)).sum())})",
      "variant", info=True)
check("3.9-42", "median B-V, CYCLE with a graded FAP (46)", "",
      med(b[(b.primary_class == 'CYCLE') & (b.FAP != '')]), "variant", info=True)
# D39 examples
for i, (h, v) in enumerate([("23249", 0.92), ("160346", 0.96), ("32147", 1.06)]):
    check(f"3.9-{43+i}", f"B-V of HD {h} in the catalogue", v, float(bb.loc[h, "bv"]),
          "P4_RESEARCH_NOTEBOOK.md D39")
write_out("03h_crossmatch_groups.txt", "\n".join(out) + "\n")
