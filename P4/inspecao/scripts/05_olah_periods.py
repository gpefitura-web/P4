"""Stage 3.10 - independent cycle periods of Olah+2016 (Table 1) against B95, Baum+2022, Saar & Brandenburg.

Reads bib/Olah_2016_AA_590_A133_arXiv1604.06701.pdf through pdftotext at run time
(poppler-utils must be installed). The dominant period is the first number after P_rot
in each Table 1 row. Appends rows to checks.csv and writes saidas/05_olah_periods.txt.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import re
import subprocess

from common import ROOT, check, isnum, read_csv, write_out

OLAH = "bib/Olah_2016_AA_590_A133_arXiv1604.06701.pdf (Table 1)"
txt = subprocess.run(["pdftotext", "-layout", os.path.join(ROOT, "bib",
                      "Olah_2016_AA_590_A133_arXiv1604.06701.pdf"), "-"],
                     capture_output=True, text=True, check=True).stdout
rows = {}
for ln in txt.splitlines():
    m = re.match(r"^\s*HD (\d+[AB]?)\s+\S+\s+(\d+(?:\.\d+)?)b?\s+(\d+(?:\.\d+)?)", ln)
    if m:
        rows[m.group(1)] = (float(m.group(2)), float(m.group(3)))
check("3.10-01", "stars with a dominant period parsed from Olah Table 1 (29 stars, 28 with a "
      "cycle; HD 95735 and HD 131156A/B have no B95 row)", 28, len(rows), OLAH)
b = read_csv("baliunas_table2_full.csv").set_index("HD")
bm = read_csv("baum2022_cycle_periods.csv").set_index("HD")
sa = read_csv("audit/saar_baliunas_crossmatch.csv").set_index("HD")
out = ["HD | Prot_Olah | P_Olah | P_B95 | dP_B95 | (Olah-B95)/dP | P_Baum | P_Saar"]
sig = []
for hd, (prot, p) in sorted(rows.items(), key=lambda kv: int(re.sub(r"\D", "", kv[0]))):
    if hd in b.index and isnum(b.loc[hd, "P_cyc"]) and isnum(b.loc[hd, "dP"]):
        pb, dp = float(b.loc[hd, "P_cyc"]), float(b.loc[hd, "dP"])
        z = (p - pb) / dp
        sig.append((hd, z, b.loc[hd, "FAP"]))
        out.append(f"{hd} | {prot} | {p} | {pb} | {dp} | {z:+.1f} | "
                   f"{bm.loc[hd, 'P_baum_yr'] if hd in bm.index else ''} | "
                   f"{sa.loc[hd, 'saar_Pcyc'] if hd in sa.index else ''}")
n2 = sum(1 for _, z, _ in sig if abs(z) >= 2)
check("3.10-02", "Olah dominant period vs B95 period: stars compared", "", len(sig), OLAH,
      info=True)
check("3.10-03", "of those, |Olah - B95| >= 2 x dP(B95)", "", f"{n2}/{len(sig)}", OLAH,
      info=True)
exc = [(hd, z) for hd, z, f in sig if f == "Excellent"]
check("3.10-04", "CYCLE + FAP Excellent stars compared | with |diff| >= 2 sigma", "",
      f"{len(exc)} | {sum(1 for _, z in exc if abs(z) >= 2)}", OLAH, info=True)
for cid, hd, exp in (("3.10-05", "166620", "13.6"), ("3.10-06", "3651", "11.6"),
                     ("3.10-07", "4628", "8.94")):
    check(cid, f"HD {hd}: dominant period in Olah Table 1", exp, rows[hd][1], OLAH, tol=1e-9)
check("3.10-08", "HD 166620 rotation period in Olah Table 1 (Luhn 45.06 +- 4.07 d; Donahue 42.4 d)",
      "", rows["166620"][0], "bib/Luhn_2022_ApJL_936_L23.pdf §3.3", info=True)
write_out("05_olah_periods.txt", "\n".join(out) + "\n")
