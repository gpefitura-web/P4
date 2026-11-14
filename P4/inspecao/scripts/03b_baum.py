"""Stages 3.2, 3.3 and 3.5 - Baum+2022 Table 1 / Table 2 and derived files."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import numpy as np

from common import check, pd, read_csv, read_vizier, write_out

A9 = "audit/A9_baum.md"
t1 = read_vizier("J_AJ_163_183_table1.tsv")
t2 = read_vizier("J_163_183_table2.tsv")
t1["S"] = t1.Svalue.astype(float)
t1["t"] = t1.Time.astype(float)
out = []

# ---- 3.2 Table 1 ---------------------------------------------------------
check("3.2-01", "Table 1 rows", 62135, len(t1), A9 + " §1.1")
check("3.2-02", "Table 1 distinct stars", 59, t1.HD.nunique(), A9 + " §1.1")
check("3.2-03", "Table 2 rows", 59, len(t2), A9 + " §0")
check("3.2-04", "t_min (2 decimals)", "1966.18", f"{t1.t.min():.2f}", A9 + " §1.1")
check("3.2-05", "t_max (2 decimals)", "2020.19", f"{t1.t.max():.2f}", A9 + " §1.1")
inst = t1.Inst.value_counts().to_dict()
for i, (k, v) in enumerate([("HKP-1", 2207), ("HKP-2", 50223),
                            ("HIRES-1", 1772), ("HIRES-2", 7933)]):
    check(f"3.2-{6+i:02d}", f"observations with Inst={k}", v, inst.get(k, 0),
          A9 + " §1.2")
nst = t1.groupby("Inst").HD.nunique().to_dict()
for i, (k, v) in enumerate([("HKP-1", 22), ("HKP-2", 59), ("HIRES-1", 49),
                            ("HIRES-2", 59)]):
    check(f"3.2-{10+i:02d}", f"stars with Inst={k}", v, nst.get(k, 0), A9 + " §1.2")
rng = t1.groupby("Inst").t.agg(["min", "max"])
exp_rng = {"HKP-1": "1966.18-1977.57", "HKP-2": "1977.25-2001.77",
           "HIRES-1": "1996.53-2003.54", "HIRES-2": "2004.63-2020.18"}
for i, k in enumerate(exp_rng):
    got = f"{rng.loc[k, 'min']:.2f}-{rng.loc[k, 'max']:.2f}"
    check(f"3.2-{14+i:02d}", f"time range of Inst={k}", exp_rng[k], got, A9 + " §1.2")
fl = t1.Flag.value_counts().to_dict()
for i, (k, v) in enumerate([("none", 58880), ("1day", 2782), ("sigma", 444),
                            ("1day/sigma", 29)]):
    check(f"3.2-{18+i:02d}", f"observations with Flag={k}", v, fl.get(k, 0),
          A9 + " §1.2")
sig = t1.Flag.str.contains("sigma")
check("3.2-22", "clean series (no 'sigma' flag)", 61662, int((~sig).sum()), A9 + " §1.2")

n1 = t1.groupby("HD").size()
t2n = t2.set_index("HD").Nobs.astype(int)
mism = [(h, int(t2n[h]), int(n1.get(h, -1))) for h in t2n.index if t2n[h] != n1.get(h, -1)]
check("3.2-23", "stars where Table 2 Nobs != Table 1 row count", 0, len(mism),
      A9 + " §3 check 1")
check("3.2-24", "sum of Table 2 Nobs", 62135, int(t2n.sum()), A9 + " §3 check 1")
base = t1.groupby("HD").t.agg(lambda x: x.max() - x.min())
cad = t2.set_index("HD").Cadence.astype(float)
dcad = (cad - n1 / base).abs().max()
check("3.2-25", "max |Cadence - Nobs/baseline|", 0.005, round(float(dcad), 3),
      A9 + " §3 check 2", tol=0.0005)
ct = t2.ClassTP.str.strip()
check("3.2-26", "ClassTP flat", 24, int((ct == "flat").sum()), A9 + " §1.4")
check("3.2-27", "ClassTP var", 17, int((ct == "var").sum()), A9 + " §1.4")
check("3.2-28", "ClassTP long", 4, int((ct == "long").sum()), A9 + " §1.4")
num = ct[ct.str.match(r"^\d")]
check("3.2-29", "ClassTP numeric period", 14, len(num), A9 + " §1.4")
check("3.2-30", "ClassTP numeric period with '?'", 4, int(num.str.contains(r"\?").sum()),
      "DECISOES_D41_D54.md D42")
check("3.2-31", "stars marked '?' (sorted)", "101501,166620,190406,4628",
      ",".join(sorted(t2.HD[ct.str.match(r"^\d.*\?")])), A9 + " A9-F1")
check("3.2-32", "ClassB95 filled", 26, int((t2.ClassB95.str.strip() != "").sum()),
      A9 + " §1.1")

# ---- 3.3 N per star ------------------------------------------------------
check("3.3-01", "median N observations per star", 698, float(n1.median()),
      A9 + " §1.3")
check("3.3-02", "min / max N observations", "43/4676", f"{n1.min()}/{n1.max()}",
      A9 + " §1.3")
check("3.3-03", "stars with N obs > 100", 56, int((n1 > 100).sum()), A9 + " §1.3")
low = sorted((h, int(n)) for h, n in n1.items() if n <= 100)
check("3.3-04", "stars with N obs <= 100", "145958A=84,145958B=76,178911B=43",
      ",".join(f"{h}={n}" for h, n in low), A9 + " §1.3")
t1["yr"] = np.floor(t1.t).astype(int)
ns_all = t1.groupby("HD").yr.nunique()
ns_clean = t1[~sig].groupby("HD").yr.nunique()
check("3.3-05", "median annual seasons (distinct calendar years, all points)", 27,
      float(ns_all.median()), A9 + " §1.3")
check("3.3-06", "min / max annual seasons", "9/54", f"{ns_all.min()}/{ns_all.max()}",
      A9 + " §1.3")
check("3.3-07", "stars with > 100 annual seasons", 0, int((ns_all > 100).sum()),
      A9 + " §1.3")
check("3.3-08", "median annual seasons, sigma-flagged points removed", "",
      float(ns_clean.median()), "variant, not in the documents", info=True)


def maxgap(x):
    return float(np.diff(np.sort(x.values)).max())


gap = t1.groupby("HD").t.apply(maxgap)
gap_clean = t1[~sig].groupby("HD").t.apply(maxgap)
check("3.3-09", "median largest internal gap (yr)", 7.17, round(float(gap.median()), 2),
      A9 + " §1.3", tol=0.005)
check("3.3-10", "stars with largest gap > 5 yr", 42, int((gap > 5).sum()), A9 + " §1.3")
check("3.3-11", "median largest gap, sigma-flagged removed", "",
      round(float(gap_clean.median()), 2), "variant, not in the documents", info=True)
b = np.floor(base + 0.5)
check("3.3-12", "baseline min/median/max (yr, rounded)", "24/41/54",
      f"{round(base.min())}/{round(base.median())}/{round(base.max())}", A9 + " §1.3")
check("3.3-13", "stars with Cadence > 10 obs/yr", 39, int((cad > 10).sum()),
      A9 + " A9-F9")

# compare against baum2022_59stars.csv, column by column
c = read_csv("baum2022_59stars.csv").set_index("HD")
check("3.3-14", "baum2022_59stars.csv shape", "59x33", f"{len(c)}x{c.shape[1] + 1}",
      "paper_state_v6.md §10")
per_inst = t1.groupby(["HD", "Inst"]).size().unstack(fill_value=0)
cmp_cols = {
    "N_obs_total": n1, "N_obs_limpo": t1[~sig].groupby("HD").size(),
    "N_sigma_clipped": t1[sig].groupby("HD").size().reindex(n1.index, fill_value=0),
    "N_estacoes_anuais": ns_all, "N_HKP1": per_inst["HKP-1"],
    "N_HKP2": per_inst["HKP-2"], "N_HIRES1": per_inst["HIRES-1"],
    "N_HIRES2": per_inst["HIRES-2"],
}
k = 15
for col, ser in cmp_cols.items():
    diff = [(h, c.loc[h, col], int(ser[h])) for h in c.index
            if int(float(c.loc[h, col])) != int(ser[h])]
    check(f"3.3-{k}", f"baum2022_59stars.csv rows differing from Table 1 in {col}",
          0, len(diff), "baum2022_59stars.csv vs data/J_AJ_163_183_table1.tsv")
    if diff:
        out.append(f"# diff {col}: {diff}")
    k += 1
for col, ser, tol in [("t_min", t1.groupby("HD").t.min(), 0.0006),
                      ("t_max", t1.groupby("HD").t.max(), 0.0006),
                      ("maior_lacuna_yr", gap, 0.0006),
                      ("baseline_yr_exato", base, 0.0006)]:
    diff = [(h, c.loc[h, col], round(float(ser[h]), 3)) for h in c.index
            if abs(float(c.loc[h, col]) - float(ser[h])) > tol]
    check(f"3.3-{k}", f"baum2022_59stars.csv rows differing from Table 1 in {col}",
          0, len(diff), "baum2022_59stars.csv vs data/J_AJ_163_183_table1.tsv")
    if diff:
        out.append(f"# diff {col}: {diff}")
    k += 1
for col, t2col in [("Smed_baum", "Svalue"), ("Teff", "Teff"), ("logg", "logg"),
                   ("FeH", "Fe/H"), ("Mass", "Mass"), ("Age", "Age"),
                   ("baseline_yr_T2", "Base"), ("cadence_obs_per_yr", "Cadence")]:
    s2 = t2.set_index("HD")[t2col].astype(float)
    diff = [(h, c.loc[h, col], s2[h]) for h in c.index
            if abs(float(c.loc[h, col]) - s2[h]) > 1e-9]
    check(f"3.3-{k}", f"baum2022_59stars.csv rows differing from Table 2 in {col}",
          0, len(diff), "baum2022_59stars.csv vs data/J_163_183_table2.tsv")
    if diff:
        out.append(f"# diff {col}: {diff}")
    k += 1
for col, t2col in [("class_Baum", "ClassTP"), ("class_B95_por_Baum", "ClassB95")]:
    s2 = t2.set_index("HD")[t2col].str.strip()
    diff = [(h, c.loc[h, col], s2[h]) for h in c.index if c.loc[h, col] != s2[h]]
    check(f"3.3-{k}", f"baum2022_59stars.csv rows differing from Table 2 in {col}",
          0, len(diff), "baum2022_59stars.csv vs data/J_163_183_table2.tsv")
    if diff:
        out.append(f"# diff {col}: {diff}")
    k += 1
check(f"3.3-{k}", "rows of baum2022_59stars.csv graded other than A", 0,
      int((c.grau != "A").sum()), "paper_state_v6.md §10")

# Key stars quoted in the documents
for cid, hd, exp, src in [("3.3-40", "101501", "2239/49", "DECISOES_D41_D54.md D49"),
                          ("3.3-41", "166620", "1766/54", A9 + " §1.6"),
                          ("3.3-42", "10700", "2526/52", A9 + " §2.1"),
                          ("3.3-43", "190360", "1659/53", A9 + " §2.1"),
                          ("3.3-44", "182572", "2161/52", A9 + " §2.1"),
                          ("3.3-45", "23249", "1337/52", A9 + " §2.1")]:
    r = t2[t2.HD == hd].iloc[0]
    check(cid, f"HD {hd} Nobs/Base (Table 2)", exp, f"{int(r.Nobs)}/{int(r.Base)}", src)
h = t1[t1.HD == "166620"].sort_values("t")
g = np.diff(h.t.values)
i = int(g.argmax())
check("3.3-46", "HD 166620 largest gap in Baum Table 1 (yr)", 6.91, round(float(g.max()), 2),
      "audit/A10_luhn.md §1.2", tol=0.005)
check("3.3-47", "HD 166620 largest gap interval", "1997.73-2004.64",
      f"{h.t.values[i]:.2f}-{h.t.values[i+1]:.2f}", "audit/A10_luhn.md §1.2")
hi = h.Inst.value_counts().to_dict()
check("3.3-48", "HD 166620 per instrument (HKP-1/HKP-2/HIRES-1/HIRES-2) in Baum T1",
      "107/1547/9/103",
      f"{hi.get('HKP-1',0)}/{hi.get('HKP-2',0)}/{hi.get('HIRES-1',0)}/{hi.get('HIRES-2',0)}",
      A9 + " §3 check 7")

# Coverage facts for the two objects named in the registered recommendation (counts only;
# no variability statistic is computed here)
for cid, hd in (("3.3-50", "101501"), ("3.3-51", "166620")):
    g = t1[t1.HD == hd].sort_values("t")
    pi = g.Inst.value_counts().to_dict()
    mwlast = g[g.Inst.isin(["HKP-1", "HKP-2"])].t.max()
    hir = g[g.Inst.isin(["HIRES-1", "HIRES-2"])]
    dg = np.diff(g.t.values)
    j = int(dg.argmax())
    check(cid, f"HD {hd}: N per instrument HKP-1/HKP-2/HIRES-1/HIRES-2 | last MW epoch | "
          "HIRES epochs (first-last) | largest gap (from-to)", "",
          f"{pi.get('HKP-1',0)}/{pi.get('HKP-2',0)}/{pi.get('HIRES-1',0)}/{pi.get('HIRES-2',0)} | "
          f"{mwlast:.2f} | {hir.t.min():.2f}-{hir.t.max():.2f} | "
          f"{dg.max():.2f} yr ({g.t.values[j]:.2f}-{g.t.values[j+1]:.2f})",
          "data/J_AJ_163_183_table1.tsv", info=True)
g = t1[t1.HD == "101501"]
check("3.3-52", "HD 101501: fraction of the 2239 observations taken at Mount Wilson (%)", "",
      round(100 * g.Inst.isin(["HKP-1", "HKP-2"]).mean(), 2),
      "DECISOES_D41_D54.md D49 ('2 239 observacoes, baseline de 49 anos')", info=True)
check("3.3-53", "HD 101501: calendar years with data in 1980-1990 | N obs in 1980-1990", "",
      f"{g[g.yr.between(1980, 1990)].yr.nunique()} | {int(g.yr.between(1980, 1990).sum())}",
      "DECISOES_D41_D54.md D49 ('estado plano ~1980-1990')", info=True)
check("3.3-54", "HD 101501 in the instrument-step file (needs >= 10 HIRES-2 points)", "absent",
      "present" if "101501" in set(read_csv("audit/a9_instrument_step.csv").HD) else "absent",
      A9 + " §1.7")
FLAT4 = ["10700", "190360", "182572", "23249"]          # A9 §2.1
CYC6 = ["4628", "10476", "26965", "152391", "166620", "219834B"]  # A9 §2.1
for cid, lab, grp in (("3.3-55", "4 clean Flat in Baum", FLAT4),
                      ("3.3-56", "6 CYCLE+Excellent in Baum", CYC6)):
    check(cid, f"{lab}: median N obs | median annual seasons | median N HIRES-2 | "
          "median largest gap (yr)", "",
          f"{float(n1[grp].median())} | {float(ns_all[grp].median())} | "
          f"{float(per_inst.loc[grp, 'HIRES-2'].median())} | {float(gap[grp].median()):.2f}",
          A9 + " A9-F5 (N x group in the Baum subset)", info=True)

# ---- 3.5 instrument step -------------------------------------------------
s = read_csv("audit/a9_instrument_step.csv").set_index("HD")
check("3.5-01", "rows in a9_instrument_step.csv", 51, len(s), A9 + " §1.7")
rel_csv = s.delta_rel_pct.astype(float)
check("3.5-02", "sample std of delta_rel_pct in CSV (ddof=1)", 4.47,
      round(float(rel_csv.std(ddof=1)), 2), A9 + " §1.7", tol=0.005)
check("3.5-03", "population std of delta_rel_pct in CSV (ddof=0)", "",
      round(float(rel_csv.std(ddof=0)), 2), "variant", info=True)
check("3.5-04", "median delta_rel_pct in CSV", 0.00, round(float(rel_csv.median()), 2),
      A9 + " §1.7", tol=0.005)
check("3.5-05", "mean delta_rel_pct in CSV", -0.61, round(float(rel_csv.mean()), 2),
      A9 + " §1.7", tol=0.005)
check("3.5-06", "|delta| > 1.2 % in CSV", 25, int((rel_csv.abs() > 1.2).sum()),
      A9 + " §1.7")
check("3.5-07", "|delta| > 5 % in CSV", 10, int((rel_csv.abs() > 5).sum()), A9 + " §1.7")
check("3.5-08", "HD 166620 delta_rel_pct in CSV", -8.78,
      round(float(rel_csv["166620"]), 2), A9 + " §1.7", tol=0.005)
check("3.5-09", "HD 4628 delta_rel_pct in CSV", -16.3, round(float(rel_csv["4628"]), 1),
      A9 + " §1.7", tol=0.05)
check("3.5-10", "largest |delta| star in CSV", "4628", rel_csv.abs().idxmax(),
      A9 + " §1.7")


def step(df, minpts=10):
    """Median(HIRES-2) - median(HKP-2) per star, stars with >= minpts in both."""
    rows = {}
    for hd, g in df.groupby("HD"):
        a = g[g.Inst == "HKP-2"].S
        z = g[g.Inst == "HIRES-2"].S
        if len(a) >= minpts and len(z) >= minpts:
            rows[hd] = (a.median(), z.median(), 100 * (z.median() - a.median()) / a.median(),
                        len(a), len(z))
    return pd.DataFrame.from_dict(rows, orient="index",
                                  columns=["mA", "mZ", "rel", "nA", "nZ"])


variants = {"flag none only": t1[t1.Flag == "none"],
            "sigma-flagged removed": t1[~sig],
            "all rows": t1}
best = None
for name, df in variants.items():
    r = step(df)
    same_n = (set(r.index) == set(s.index) and
              all(int(s.loc[h, "N_HKP2"]) == r.loc[h, "nA"] and
                  int(s.loc[h, "N_HIRES2"]) == r.loc[h, "nZ"] for h in r.index))
    out.append(f"# step variant '{name}': {len(r)} stars, std(ddof=1)={r.rel.std(ddof=1):.3f}, "
               f">1.2%={int((r.rel.abs() > 1.2).sum())}, >5%={int((r.rel.abs() > 5).sum())}, "
               f"N columns identical to CSV={same_n}")
    if same_n and best is None:
        best = (name, r)
if best is None:
    check("3.5-11", "variant of Table 1 filtering that reproduces N_HKP2/N_HIRES2 of the CSV",
          "one of: flag none / no sigma / all", "none", A9 + " §1.7 (rule not stated)")
    name, r = "sigma-flagged removed", step(t1[~sig])
else:
    name, r = best
    check("3.5-11", "variant of Table 1 filtering that reproduces N_HKP2/N_HIRES2 of the CSV",
          "", name, A9 + " §1.7 (filter rule not stated in the audit)", info=True)
check("3.5-12", f"recomputed: stars with >=10 pts in HKP-2 and HIRES-2 ({name})", 51,
      len(r), A9 + " §1.7")
common = [h for h in r.index if h in s.index]
dmax = max(abs(r.loc[h, "rel"] - float(s.loc[h, "delta_rel_pct"])) for h in common)
check("3.5-13", "recomputed vs CSV: max |diff| of delta_rel_pct (pct points)", 0,
      round(float(dmax), 6), "audit/a9_instrument_step.csv", tol=1e-6)
check("3.5-14", "recomputed std of relative step (ddof=1)", 4.47,
      round(float(r.rel.std(ddof=1)), 2), A9 + " §1.7", tol=0.005)
check("3.5-15", "recomputed |delta| > 1.2 %", 25, int((r.rel.abs() > 1.2).sum()),
      A9 + " §1.7")
check("3.5-16", "recomputed |delta| > 5 %", 10, int((r.rel.abs() > 5).sum()), A9 + " §1.7")
check("3.5-17", "recomputed HD 166620", -8.78, round(float(r.loc["166620", "rel"]), 2),
      A9 + " §1.7", tol=0.005)
check("3.5-18", "recomputed HD 4628", -16.3, round(float(r.loc["4628", "rel"]), 1),
      A9 + " §1.7", tol=0.05)
zero = r[r.rel.abs() < 1e-9]
check("3.5-19", "stars with step exactly 0 (medians identical to 4 decimals)", "",
      ",".join(sorted(zero.index)), "not stated in the documents", info=True)
small = r[r.rel.abs() < 0.2]
check("3.5-19b", "stars with |step| < 0.2 % (HKP-2 and HIRES-2 medians coincide to ~3e-4 in S)",
      "", f"{len(small)}: " + ",".join(sorted(small.index)),
      A9 + " §1.5 (Baum: 'Fourteen stars ... were shifted' to align medians; not named)",
      info=True)
rest = r[r.rel.abs() >= 0.2]
check("3.5-19c", "std of the relative step (ddof=1, pct) over the remaining stars | N", "",
      f"{rest.rel.std(ddof=1):.2f} | {len(rest)}", "variant, not in the documents", info=True)
named = ["22072", "23249", "217014", "3795", "10145", "65583"]
check("3.5-20", "step of stars Baum names as median-shifted (HD 22072, 23249, 217014 "
      "HKP-1->HKP-2; 3795, 10145, 65583 MW->HIRES-1), pct",
      "", "; ".join(f"{h}={r.loc[h, 'rel']:+.2f}" if h in r.index else f"{h}=n/a"
                    for h in named), A9 + " §1.5", info=True)
excl = sorted(set(t2.HD) - set(r.index))
check("3.5-21", "stars excluded from the step statistic (<10 pts in one instrument)", 8,
      len(excl), A9 + " §1.7 (59 - 51)")
out.append("# excluded from step: " + ",".join(excl))
out.append("# top |step|:\n" + r.reindex(r.rel.abs().sort_values(ascending=False).index)
           .head(12).to_string())
# The step statistic is dominated by a few large values: robust spread for context
mad = float((r.rel - r.rel.median()).abs().median()) * 1.4826
check("3.5-22", "robust spread of relative step (1.4826*MAD, pct)", "", round(mad, 2),
      "variant, not in the documents", info=True)
write_out("03b_baum.txt", "\n".join(out) + "\n")
