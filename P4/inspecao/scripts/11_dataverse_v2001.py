"""Compare HK_Project_v2001_NSO (Dataverse H85QPF) with Baum+2022 Table 1 (VizieR J/AJ/163/183).
Read-only: data/ is read, nothing is written there. Run with `python -I`."""
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, check, write_out

D = os.path.join(ROOT, "data", "HK_Project_v2001_NSO")
BAUM = os.path.join(ROOT, "data", "J_AJ_163_183_table1.tsv")

def jd_to_year(jd):
    return 2000.0 + (jd - 2451544.5) / 365.25

# --- v2001 files ---------------------------------------------------------
v = {}
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".mgd"):
        continue
    hd = fn[2:-4].lstrip("0")
    rows = []
    for ln in open(os.path.join(D, fn), encoding="latin-1"):
        f = ln.split()
        if len(f) < 10:
            continue
        s, jdrel, inst = float(f[1]), float(f[2]), f[7]
        rows.append((2444000.0 + jdrel, s, inst))
    v[hd] = rows

# --- Baum ----------------------------------------------------------------
b = defaultdict(list)
for ln in open(BAUM, encoding="utf-8"):
    if ln.startswith("#") or ";" not in ln:
        continue
    p = [x.strip() for x in ln.rstrip("\n").split(";")]
    if len(p) < 5 or not p[0].isdigit():
        continue
    b[p[0]].append((float(p[2]), float(p[1]), p[3], p[4]))

check("3.15-01", "stars (files) in HK_Project_v2001_NSO", 35, len(v), "bib/DOWNLOAD_LOG.md; README.pdf", )
check("3.15-02", "HD 166620 present in HK_Project_v2001_NSO", "no", "yes" if "166620" in v else "no",
      "Dataverse file list 2026-11-24")
common = sorted((h for h in v if h in b), key=int)
check("3.15-03", "v2001 stars also in Baum+2022 (59 stars)", "", len(common), "data/J_AJ_163_183_table1.tsv", info=True)
out = ["HD | v2001 N | v2001 last yr | Baum HKP N | Baum last HKP-2 yr | v2001 rows after Baum last HKP yr | "
       "Baum HKP rows matched in v2001 (dt<0.002 yr, |dS|<=0.00051) | median dS of matches"]
tot_b = tot_m = 0
ext = {}
for h in common:
    vr = v[h]
    br = [r for r in b[h] if r[2].startswith("HKP")]
    last_b = max((r[0] for r in br), default=float("nan"))
    ext[h] = sum(1 for jd, s, i in vr if jd_to_year(jd) > last_b + 0.002)
    vy = sorted((jd_to_year(jd), s) for jd, s, i in vr)
    import bisect
    ys = [y for y, _ in vy]
    m = 0
    ds = []
    for t, s, _, _ in br:
        k = bisect.bisect_left(ys, t - 0.002)
        best = None
        while k < len(ys) and ys[k] <= t + 0.002:
            d = abs(vy[k][1] - s)
            best = d if best is None or d < best else best
            k += 1
        if best is not None and best <= 0.00051:
            m += 1
            ds.append(best)
    tot_b += len(br)
    tot_m += m
    ds.sort()
    out.append(f"{h} | {len(vr)} | {max(ys):.2f} | {len(br)} | {last_b:.2f} | {ext[h]} | {m}/{len(br)} | "
               f"{(ds[len(ds)//2] if ds else float('nan')):.5f}")
check("3.15-04", "Baum HKP rows of the common stars reproduced in v2001 (time within 0.002 yr, S within 5e-4)",
      "", f"{tot_m}/{tot_b}", "data/HK_Project_v2001_NSO vs data/J_AJ_163_183_table1.tsv", info=True)
check("3.15-05", "common stars with v2001 rows later than Baum's last HKP epoch (by > 0 rows)", "",
      f"{sum(1 for h in common if ext[h] > 0)}/{len(common)}", "same", info=True)
write_out("11_dataverse_v2001.txt", "\n".join(out) + "\n")

# --- the 29 stars that Baum does not have: what the catalogue says about them ---------------------
import csv
cat = {r["HD"]: r for r in csv.DictReader(open(os.path.join(ROOT, "baliunas_table2_full.csv"), encoding="utf-8"))}
out2 = ["HD | catalogue class | P_cyc | FAP | B-V | v2001 N | first yr | last yr | baseline yr | seasons (calendar years) | largest gap yr"]
for h in sorted((x for x in v if x not in b), key=lambda x: int(x.rstrip("ab") or 0) if x.rstrip("ab").isdigit() else 0):
    ys = sorted(jd_to_year(jd) for jd, s, i in v[h])
    seas = len({int(y) for y in ys})
    gap = max((y2 - y1 for y1, y2 in zip(ys, ys[1:])), default=0)
    c = cat.get(h) or cat.get(h.upper()) or {}
    out2.append(f"{h} | {c.get('primary_class','?')} | {c.get('P_cyc','')} | {c.get('FAP','')} | {c.get('bv','')} | "
                f"{len(ys)} | {ys[0]:.2f} | {ys[-1]:.2f} | {ys[-1]-ys[0]:.1f} | {seas} | {gap:.2f}")
write_out("11_dataverse_v2001_not_in_baum.txt", "\n".join(out2) + "\n")
absent = ["16160", "32147", "160346", "201091", "81809", "103095"]
check("3.15-06", "the six Baum-absent controls (I-12) present in v2001: 160346, 201091, 81809, 103095 yes; 16160, 32147 no",
      "4/6", f"{sum(1 for h in absent if h in v)}/6", "audit/ERRATA_2026-11-14.md E-I12; data/HK_Project_v2001_NSO", info=True)

# annual (calendar-year) structure of the v2001 stars that Baum does not have
out3 = ["HD | distinct calendar years | longest consecutive run | missing-year gaps"]
for h in ["160346", "201091", "81809", "103095", "13421", "124570", "158614", "216385"]:
    ys = sorted({int(jd_to_year(jd)) for jd, s, i in v[h]})
    best = cur = 1
    gaps = []
    for a, bb in zip(ys, ys[1:]):
        if bb == a + 1:
            cur += 1
        else:
            gaps.append(bb - a - 1)
            cur = 1
        best = max(best, cur)
    out3.append(f"{h} | {len(ys)} | {best} | {gaps}")
write_out("11_dataverse_v2001_runs.txt", "\n".join(out3) + "\n")
