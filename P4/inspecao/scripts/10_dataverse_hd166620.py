"""Stage 3.14 - NSO/Dataverse HK Project v1995 file for HD 166620 vs Luhn+2022 Table 2 (MW rows)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import numpy as np

from common import DATA, check, read_vizier, write_out

SRC = "data/HK_Project_v1995_NSO_166620.mgd (doi:10.7910/DVN/ZRJ6NT, file 166620.mgd)"
rows = []
with open(os.path.join(DATA, "HK_Project_v1995_NSO_166620.mgd"), encoding="utf-8") as fh:
    for ln in fh:
        f = ln.split()
        rows.append((float(f[2]), float(f[1])))  # (JD - 2444000, calibrated S)
nso = np.array(rows)
jd = nso[:, 0] + 2444000.0
year_nso = 2000.0 + (jd - 2451544.5) / 365.25
lu = read_vizier("J_ApJ_936_L23_table2.tsv")
mw = lu[lu.Inst == "MW"].copy()
mw["s"] = mw.SHK.astype(float)
mw["y"] = mw.Year.astype(float)
mw = mw.sort_values("y").reset_index(drop=True)
nso_s = nso[np.argsort(nso[:, 0], kind="stable")][:, 1]

check("3.14-01", "rows in the NSO file for HD 166620", 1654, len(nso), "Luhn MW rows (3.4-02)")
check("3.14-02", "NSO file: first and last decimal year (2 dec)", "1966.59-1995.42",
      f"{year_nso.min():.2f}-{year_nso.max():.2f}", "Luhn MW range (3.4-07)")
check("3.14-03", "max |S_NSO - S_Luhn(MW)| after sorting both by time", 0.0,
      round(float(np.max(np.abs(np.sort(nso_s) - np.sort(mw.s.values)))), 4),
      "A10 §2.2 ('No offset applied')", tol=0.0001)
check("3.14-04", "max |year_NSO - year_Luhn(MW)| after sorting (yr)", 0.0,
      round(float(np.max(np.abs(np.sort(year_nso) - np.sort(mw.y.values)))), 3), SRC, tol=0.001)
check("3.14-05", "NSO observations after 1995.5 (the archive stops in mid-1995)", 0,
      int((year_nso > 1995.5).sum()), "README.pdf of doi:10.7910/DVN/ZRJ6NT")
write_out("14_dataverse_hd166620.txt", f"rows={len(nso)} first={year_nso.min():.3f} last={year_nso.max():.3f}\n")
