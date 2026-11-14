"""Stages 3.6 and 3.7 - Isaacson+2024 tables and the Noyes+1984 validity file."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import math

from common import check, read_csv, read_vizier, write_out

A11 = "audit/A11_raridade.md"
A12 = "audit/A12_noyes.md"
out = []

# ---- 3.6 Isaacson+2024 ---------------------------------------------------
i2 = read_vizier("J_ApJS_274_35_table2.tsv")
i3 = read_vizier("J_ApJS_274_35_table3.tsv")
i4 = read_vizier("J_ApJS_274_35_table4.tsv")
for c in ("Smed", "SSD", "Nobs"):
    i2[c] = i2[c].astype(float)
check("3.6-01", "Isaacson Table 2 rows", 710, len(i2), A11 + " check 2")
check("3.6-02", "Isaacson Table 2 distinct names", 710, i2.Name.nunique(), A11 + " check 2")
check("3.6-03", "Isaacson Table 4 rows", 138, len(i4), A11 + " check 1")
check("3.6-04", "Isaacson Table 4 distinct names", 138, i4.Name.nunique(), A11 + " check 1")
check("3.6-05", "Isaacson Table 3 rows", 52380, len(i3), A11 + " check 3")
check("3.6-06", "Table 3 rows vs text of the paper (52 372)", 52372, len(i3),
      A11 + " §b.1 (known delta of 8)")
check("3.6-07", "stars with Nobs >= 45", 290, int((i2.Nobs >= 45).sum()), A11 + " check 4")
n3 = i3.groupby("Name").size()
m = i2.set_index("Name").Nobs
dn = [(k, int(m[k]), int(n3.get(k, 0))) for k in m.index if int(m[k]) != int(n3.get(k, 0))]
check("3.6-08", "stars where Table 2 Nobs != Table 3 row count", "", len(dn),
      "not checked in the audits", info=True)
out.append(f"# Table2 Nobs vs Table3 count mismatches (first 15 of {len(dn)}): {dn[:15]}")
check("3.6-09", "Table 4 names absent from Table 2", 0,
      len(set(i4.Name) - set(i2.Name)), "implicit")
check("3.6-10", "Table 4 stars with Table 2 Nobs < 45", "",
      int((i2[i2.Name.isin(i4.Name)].Nobs < 45).sum()),
      A11 + " §b.1 (cycle search restricted to >= 45 obs)", info=True)

tau = i2[i2.Name == "HD 10700"].iloc[0]
check("3.6-11", "HD 10700 SSD | Smed | Nobs", "0.00121 | 0.1674 | 944",
      f"{tau.SSD:.5f} | {tau.Smed:.4f} | {int(tau.Nobs)}", A11 + " §b.3")
check("3.6-12", "HD 10700 SSD/Smed (%)", 0.723, round(100 * tau.SSD / tau.Smed, 3),
      A11 + " §b.2 note", tol=0.0005)
well = i2[i2.Nobs >= 45]
check("3.6-13", "Nobs >= 45 and SSD < 0.00121 (tabulated tau Cet)", 48,
      int((well.SSD < tau.SSD).sum()), A11 + " A11b-F1")
check("3.6-14", "Nobs >= 45 and SSD < 0.00125 (text value)", 52,
      int((well.SSD < 0.00125).sum()), A11 + " A11b-F1")
check("3.6-15", "Nobs >= 45 and SSD <= 0.00121", "", int((well.SSD <= tau.SSD).sum()),
      "variant (ties)", info=True)
rel_tau = tau.SSD / tau.Smed
check("3.6-16", "Nobs >= 45 and SSD/Smed < tau Cet's (relative criterion)", "",
      int(((well.SSD / well.Smed) < rel_tau).sum()),
      "variant: 'menos dispersas' read as relative scatter", info=True)
check("3.6-17", "Nobs > 45 (strict) and SSD < 0.00121", "",
      int(((i2.Nobs > 45) & (i2.SSD < tau.SSD)).sum()), "variant", info=True)

c = read_csv("isaacson2024_least_active_50.csv")
check("3.6-18", "rows in isaacson2024_least_active_50.csv", 48, len(c),
      "paper_state_v6.md §10")
sel = set(well[well.SSD < tau.SSD].Name)
check("3.6-19", "CSV names == reproduced filter (symmetric difference)", 0,
      len(sel ^ set(c.Name)), "isaacson2024_least_active_50.csv 'fonte' column")
j = c.merge(i2, on="Name", suffixes=("_csv", "_t2"))
bad = int(((j.SSD_csv.astype(float) - j.SSD_t2).abs() > 1e-9).sum() +
          ((j.Smed_csv.astype(float) - j.Smed_t2).abs() > 1e-9).sum() +
          ((j.Nobs_csv.astype(float) - j.Nobs_t2).abs() > 1e-9).sum())
check("3.6-20", "CSV cells (SSD, Smed, Nobs) differing from Table 2", 0, bad,
      "isaacson2024_least_active_50.csv vs data/J_ApJS_274_35_table2.tsv")
dr = (j.disp_rel_pct.astype(float) - 100 * j.SSD_t2 / j.Smed_t2).abs().max()
check("3.6-21", "max |disp_rel_pct - 100*SSD/Smed| in CSV", 0, round(float(dr), 3),
      "isaacson2024_least_active_50.csv", tol=0.0006)
check("3.6-22", "'fonte' column documents the filter criterion (contains 'SSD' or '45')",
      "yes", "yes" if c.fonte.str.contains("SSD|45").any() else "no",
      A11 + " A11b-F1 ('criterio documentado na propria coluna fonte')")
out.append("# distinct 'fonte' values: " + " || ".join(sorted(set(c.fonte))))
check("3.6-23", "CSV stars with relative scatter above tau Cet's 0.723 %", "",
      int((c.disp_rel_pct.astype(float) > 100 * rel_tau).sum()),
      "consequence of an absolute-SSD criterion", info=True)
h = i2[i2.Name == "HD 55575"].iloc[0]
check("3.6-24", "HD 55575 SSD/Smed (%)", 0.448, round(100 * h.SSD / h.Smed, 3),
      A11 + " check 7", tol=0.0005)
check("3.6-25", "least-scattered star with Nobs >= 45 by SSD/Smed", "HD 55575",
      well.assign(r=well.SSD / well.Smed).sort_values("r").Name.iloc[0],
      A11 + " §b.2 ('a menos ativa com >= 45 obs')")
check("3.6-26", "least-scattered star with Nobs >= 45 by absolute SSD", "HD 55575",
      well.sort_values("SSD").Name.iloc[0], A11 + " §b.2")

# A11 §b.3 table
exp = {"HD 10700": ("0.1674", "0.00121", "0.72", 944, None),
       "HD 23249": ("0.1361", "0.00117", "0.86", 75, None),
       "HD 190360": ("0.1460", "0.00139", "0.95", 280, None),
       "HD 166620": ("0.1706", "0.00190", "1.11", 149, None),
       "HD 115617": ("0.1698", "0.00191", "1.12", 609, None),
       "HD 182572": ("0.1673", "0.00250", "1.49", 80, None),
       "HD 3651": ("0.1665", "0.00665", "3.99", 157, None),
       "HD 10476": ("0.1926", "0.00798", "4.14", 180, "9.11"),
       "HD 4915": ("0.1887", "0.01108", "5.87", 98, "4.86"),
       "HD 32147": ("0.2598", "0.02310", "8.89", 625, None)}
p4 = i4.set_index("Name").Per
bad = []
for name, (smed, ssd, relp, n, per) in exp.items():
    r = i2[i2.Name == name]
    if r.empty:
        bad.append((name, "absent"))
        continue
    r = r.iloc[0]
    got = (f"{r.Smed:.4f}", f"{r.SSD:.5f}", f"{100*r.SSD/r.Smed:.2f}", int(r.Nobs),
           p4.get(name))
    if got[:4] != (smed, ssd, relp, n):
        bad.append((name, got))
    if per is not None and (got[4] is None or abs(float(got[4]) - float(per)) > 1e-9):
        bad.append((name, "period", got[4]))
    if per is None and got[4] is not None and name != "HD 32147":
        bad.append((name, "unexpected cycle", got[4]))
check("3.6-27", "rows of the A11 §b.3 table (10 present stars) not reproduced", 0,
      len(bad), A11 + " §b.3")
if bad:
    out.append(f"# A11 b.3 mismatches: {bad}")
check("3.6-28", "HD 43587 / HD 160346 present in Table 2", "absent/absent",
      "/".join("present" if (i2.Name == x).any() else "absent"
               for x in ("HD 43587", "HD 160346")), A11 + " §b.3")
check("3.6-29", "HD 32147 in Table 4 (A11 §b.3 prints a dash)", "",
      f"Per={p4.get('HD 32147')}" if "HD 32147" in p4.index else "absent",
      A11 + " §b.3", info=True)
check("3.6-30", "HD 23249 SSD < tau Cet SSD ('menos disperso que tau Cet? sim')", "yes",
      "yes" if float(i2[i2.Name == "HD 23249"].SSD.iloc[0]) < tau.SSD else "no",
      A11 + " §b.3")
check("3.6-31", "HD 23249 SSD/Smed < tau Cet SSD/Smed (relative)", "",
      "yes" if 0.00117 / 0.1361 < rel_tau else "no", "variant", info=True)

# ---- 3.7 Noyes validity --------------------------------------------------
n = read_csv("noyes1984_validade_cor.csv")
b = read_csv("baliunas_table2_full.csv")
check("3.7-01", "rows in noyes1984_validade_cor.csv", 112, len(n), A12 + " §3.1")
mm = n.merge(b, on="HD", suffixes=("_n", "_b"))
check("3.7-02", "rows whose HD/bv/primary_class/FAP differ from the frozen catalogue", 0,
      int(len(n) - len(mm) + (mm.bv_n.astype(float) != mm.bv_b.astype(float)).sum()
          + (mm.primary_class_n != mm.primary_class_b).sum() + (mm.FAP_n != mm.FAP_b).sum()),
      "noyes1984_validade_cor.csv vs baliunas_table2_full.csv")
check("3.7-02b", "rows whose B-V string differs from the catalogue only in formatting "
      "(e.g. '0.7' vs '0.70')", "", int((mm.bv_n != mm.bv_b).sum()),
      "noyes1984_validade_cor.csv vs baliunas_table2_full.csv", info=True)


def band(bv):
    """Bands as labelled in the CSV (boundaries inclusive where the CSV labels imply)."""
    if bv < 0.44:
        return "FORA"
    if bv <= 0.82:
        return "DENTRO"
    if bv <= 1.0:
        return "EXTRAPOLADO (0.82-1.0"
    if bv <= 1.2:
        return "EXTRAPOLADO + C_cf incerto"
    return "EXTRAPOLADO + pior"


bvf = b.bv.astype(float)
cnt = bvf.map(band).value_counts().to_dict()
for i, (k, v) in enumerate([("DENTRO", 82), ("EXTRAPOLADO (0.82-1.0", 17),
                            ("EXTRAPOLADO + C_cf incerto", 6), ("EXTRAPOLADO + pior", 2),
                            ("FORA", 5)]):
    check(f"3.7-{3+i:02d}", f"recomputed from catalogue B-V: band '{k}'", v, cnt.get(k, 0),
          "DECISOES_D41_D54.md D53")
lab = n.faixa_Rphot_Noyes84
wrong = [(h, bv, f) for h, bv, f in zip(n.HD, n.bv, lab) if not f.startswith(band(float(bv)))]
check("3.7-08", "CSV rows whose label disagrees with the recomputed band", 0, len(wrong),
      "noyes1984_validade_cor.csv")
check("3.7-09", "stars with B-V exactly 0.44 | 0.82 | 1.00 | 1.20 (boundary cases)", "",
      " | ".join(",".join(b.HD[(bvf - x).abs() < 1e-9]) or "-" for x in (0.44, 0.82, 1.0, 1.2)),
      "DECISOES_D41_D54.md D53 (source range is the open interval 0.44 < B-V < 0.82)",
      info=True)
strict_in = int(((bvf > 0.44) & (bvf < 0.82)).sum())
check("3.7-10", "stars strictly inside 0.44 < B-V < 0.82 (open interval, as printed in D52/D53)",
      82, strict_in, "DECISOES_D41_D54.md D53")
check("3.7-11", "stars with B-V > 1.0 (D53 text: '6 acima de 1.0' and '2 acima de 1.2')",
      "", f">1.0: {int((bvf > 1.0).sum())}; >1.2: {int((bvf > 1.2).sum())}",
      "DECISOES_D41_D54.md D53", info=True)

# D52 formulas, shown step by step for three stars (B-V and S from the catalogue)


def noyes(bv, s):
    logc = 1.13 * bv**3 - 3.91 * bv**2 + 2.84 * bv - 0.47
    x = 0.63 - bv
    dlog = 0.135 * x - 0.814 * x**2 + 6.03 * x**3 if x > 0 else 0.0
    ccf = 10 ** (logc + dlog)
    rhk = 1.340e-4 * ccf * s
    logrphot = -4.898 + 1.918 * bv**2 - 2.893 * bv**3
    rphot = 10 ** logrphot
    rp = rhk - rphot
    alt = 10 ** (-4.02 - 1.40 * bv)  # Duncan alternative form (grade B, A12-F6)
    return dict(logC=logc, dlogC=dlog, Ccf=ccf, RHK=rhk, logRphot=logrphot, Rphot=rphot,
                Rp=rp, logRp=math.log10(rp) if rp > 0 else float("nan"),
                frac_phot=rphot / rhk,
                logRp_alt=math.log10(rhk - alt) if rhk > alt else float("nan"))


out.append("\n# D52 recipe applied (B-V and <S> from baliunas_table2_full.csv)")
k = 12
for hd in ("10700", "32147", "201091", "166620", "(Sun)"):
    r = b[b.HD == hd].iloc[0]
    bv, s = float(r.bv), float(r.S)
    q = noyes(bv, s)
    out.append(f"HD {hd}: B-V={bv} S={s} band={band(bv)}\n"
               f"  log C_cf = 1.13*{bv}^3 - 3.91*{bv}^2 + 2.84*{bv} - 0.47 = {q['logC']:.4f}\n"
               f"  delta log C = {q['dlogC']:.4f}  ->  C_cf = {q['Ccf']:.4f}\n"
               f"  R_HK = 1.340e-4 * {q['Ccf']:.4f} * {s} = {q['RHK']:.4e}\n"
               f"  log R_phot = -4.898 + 1.918*{bv}^2 - 2.893*{bv}^3 = {q['logRphot']:.4f}"
               f"  ->  R_phot = {q['Rphot']:.4e}\n"
               f"  R'_HK = {q['Rp']:.4e}  ->  log R'_HK = {q['logRp']:.3f}\n"
               f"  R_phot / R_HK = {q['frac_phot']:.3f};  log R'_HK with Duncan form = "
               f"{q['logRp_alt']:.3f}")
    check(f"3.7-{k}", f"HD {hd}: log R'_HK from D52 with catalogue B-V={bv}, <S>={s} "
          f"(band {band(bv)}); R_phot/R_HK; log R'_HK with Duncan R_phot", "",
          f"{q['logRp']:.3f}; {q['frac_phot']:.3f}; {q['logRp_alt']:.3f}",
          "DECISOES_D41_D54.md D52 (no expected value in the documents: D39 forbade conversion)",
          info=True)
    k += 1
# external comparison available inside the package: CLS V logRhk and Luhn's value
for hd, name in (("10700", "HD 10700"), ("32147", "HD 32147"), ("166620", "HD 166620")):
    r = b[b.HD == hd].iloc[0]
    q = noyes(float(r.bv), float(r.S))
    t = i2[i2.Name == name].iloc[0]
    q2 = noyes(float(t["B-V"]), float(t.Smed))
    check(f"3.7-{k}", f"{name}: CLS V Table 2 logRhk vs D52 applied to CLS V's own B-V="
          f"{t['B-V']} and Smed={t.Smed:.4f} | vs D52 with catalogue B-V={r.bv}, <S>={r.S}",
          t.logRhk, f"{q2['logRp']:.3f} | {q['logRp']:.3f}",
          "data/J_ApJS_274_35_table2.tsv (logRhk column)", info=True)
    k += 1
# monotonicity claim of D40/A12-F5: dR'/dS = 1.340e-4*C_cf > 0 for fixed B-V
check(f"3.7-{k}", "D40: R'_HK is affine in S at fixed B-V with positive slope "
      "(min of 1.340e-4*C'_cf over the 112 catalogue B-V values > 0)", "yes",
      "yes" if min(noyes(x, 0.2)["Ccf"] for x in bvf) > 0 else "no",
      "P4_RESEARCH_NOTEBOOK.md D40; audit/A12_noyes.md A12-F5")
k += 1
neg = [h for h, x, s in zip(b.HD, bvf, b.S.astype(float)) if noyes(x, s)["Rp"] <= 0]
check(f"3.7-{k}", "catalogue stars for which D52 gives R'_HK <= 0 with <S> of Table 2", "",
      ",".join(neg) or "none", "not in the documents", info=True)
write_out("03f_isaacson_noyes.txt", "\n".join(out) + "\n")
