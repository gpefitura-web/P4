"""Phase 1/2 - Egeland+2017 Table 4 (calibrated solar S-index series), machine readable.

Source: https://content.cld.iop.org/journals/0004-637X/835/1/25/revision1/apjaa4e49t4_mrt.txt
Stored unchanged as data/Egeland2017_table4_apjaa4e49t4_mrt.txt. Reads it with a fixed-width
parser taken from the file's own byte-by-byte description. Run with python -I.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import datetime
import hashlib

import numpy as np

from common import DATA, check, write_out

A3 = "audit/A3_egeland.md"
path = os.path.join(DATA, "Egeland2017_table4_apjaa4e49t4_mrt.txt")
raw = open(path, "rb").read()
rows = []
for ln in raw.decode("utf-8").splitlines():
    p = ln.split()
    if len(p) >= 4 and p[0].replace(".", "", 1).isdigit() and "/" in p[3]:
        rows.append((float(p[0]) + 2400000.0, float(p[1]), float(p[2]), p[3]))
jd = np.array([r[0] for r in rows])
org = np.array([r[1] for r in rows])
cal = np.array([r[2] for r in rows])
inst = np.array([r[3] for r in rows])


def year(j):
    d = datetime.datetime(2000, 1, 1, 12) + datetime.timedelta(days=float(j) - 2451545.0)
    y0 = datetime.datetime(d.year, 1, 1)
    y1 = datetime.datetime(d.year + 1, 1, 1)
    return d.year + (d - y0) / (y1 - y0)


yr = np.array([year(j) for j in jd])
out = []
check("3.12-01", "Table 4 rows parsed", "", len(rows), "data/Egeland2017_table4_apjaa4e49t4_mrt.txt",
      info=True)
check("3.12-02", "sha256 of the stored file (first 16 hex)", "", hashlib.sha256(raw).hexdigest()[:16],
      "bib/MANIFEST.json", info=True)
check("3.12-03", "first and last epoch (decimal year)", "",
      f"{yr.min():.3f} - {yr.max():.3f}", "Table 4 (JD - 2400000 in column 1)", info=True)
check("3.12-04", "series starts in 1966 and ends in 2016 (not 2021)", "1966/2016",
      f"{int(yr.min())}/{int(yr.max())}", A3 + " F5 and §8 ('beyond the 1966-2021 window')")
ins = {}
for k in sorted(set(inst)):
    m = inst == k
    ins[k] = (int(m.sum()), yr[m].min(), yr[m].max())
check("3.12-05", "instruments in Table 4 (as a set)", ", ".join(sorted(
    ["MWO/HKP-1", "NSO/SP", "MWO/HKP-2", "SSS/CCD-1", "SSS/CCD-2"])),
      ", ".join(sorted(ins)), A3 + " F5")
for k, (n, a, b) in ins.items():
    check(f"3.12-06 {k}", f"{k}: rows | first - last year", "", f"{n} | {a:.2f} - {b:.2f}",
          "Table 4", info=True)
out += [f"{k}: N={n} {a:.3f}-{b:.3f}" for k, (n, a, b) in ins.items()]
check("3.12-07", "A3 F5 says the series spans 'cycles 15-24'; Egeland §4.6 says the composite "
      "of Table 4 covers cycles 20-24 and cycles 15-19 are only in the monthly KKL composite "
      "(Figure 4, bottom)", "15-24", "20-24 (1966-2016)",
      A3 + " F5 vs Egeland+2017 §4.6 (p. 9)")
dif = np.abs(org - cal)
check("3.12-08", "rows where calibrated S differs from original S", "", int((dif > 1e-9).sum()),
      "Table 4", info=True)
ann = {}
for y, c in zip(np.floor(yr).astype(int), cal):
    ann.setdefault(y, []).append(c)
n_per = np.array([len(v) for v in ann.values()])
check("3.12-09", "calendar years with data | median observations per year | min | max", "",
      f"{len(ann)} | {float(np.median(n_per)):.0f} | {n_per.min()} | {n_per.max()}", "Table 4",
      info=True)
g = np.diff(np.sort(jd)) / 365.25
check("3.12-10", "largest internal gap (yr)", "", f"{g.max():.2f}", "Table 4", info=True)
check("3.12-11", "mean calibrated S, all rows | median", "", f"{cal.mean():.4f} | {np.median(cal):.4f}",
      "Table 4 (not a cycle mean: sampling is uneven)", info=True)
am = np.array([np.mean(v) for v in ann.values()])
check("3.12-12", "mean of annual means of calibrated S (D08 convention: annual mean over all years)",
      "0.1694 (cycles 15-24, Egeland Table 2)", f"{am.mean():.4f}",
      "P4_RESEARCH_NOTEBOOK.md D16; different window (1966-2016)", info=True)
# pipeline expectation (p4_pipeline.ipynb cell 10: 1965 < year < 2022, N ~ 20440 daily points)
check("3.12-13", "rows vs the ~20 440 daily points the pipeline assumes for 1966-2021 "
      "(synthetic generator, cell 10)", 20440, len(rows), "p4_pipeline.ipynb cell 10")
write_out("08_egeland_t4.txt", "\n".join(out) + "\n")
