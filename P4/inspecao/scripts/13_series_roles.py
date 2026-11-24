"""Series sizes for the P4 groups in the Baum+2022 subset: raw observations vs annual seasons,
against the thresholds quoted by the sources (Livina & Lenton: ~1000 points; D24: > 100 points;
D20: windows of 50 % of the record). Read-only. Run with `python -I`."""
import csv
import os
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, check, write_out

rows = list(csv.DictReader(open(os.path.join(ROOT, "baum2022_59stars.csv"), encoding="utf-8")))
by = {r["HD"]: r for r in rows}
FLAT5 = ["10700", "23249", "43587", "182572", "190360"]          # five clean Flat (03h_crossmatch_groups.txt)
CTRL = [r["HD"] for r in rows if r["class_A1"] == "CYCLE" and r["FAP_A1"] == "Excellent"]
CASES = ["166620", "101501"]


def f(x):
    return float(x)


def stats(hds, label):
    sel = [by[h] for h in hds if h in by]
    if not sel:
        return f"{label}: none present"
    raw = [f(r["N_obs_limpo"]) for r in sel]
    ann = [f(r["N_estacoes_anuais"]) for r in sel]
    gap = [f(r["maior_lacuna_yr"]) for r in sel]
    return (f"{label}: n={len(sel)}/{len(hds)} | raw median {st.median(raw):.0f} (min {min(raw):.0f}, max {max(raw):.0f}) | "
            f"annual seasons median {st.median(ann):.0f} (min {min(ann):.0f}, max {max(ann):.0f}) | "
            f"raw>=1000: {sum(1 for x in raw if x >= 1000)} | annual>=100: {sum(1 for x in ann if x >= 100)} | "
            f"half-record window (annual): {st.median(ann) / 2:.0f} points | largest gap median {st.median(gap):.2f} yr")


out = [stats(FLAT5, "five clean Flat (Baum has 4 of 5)"), stats(CTRL_ := CTRL, "CYCLE+Excellent controls in Baum"),
       stats([r["HD"] for r in rows], "all 59 Baum stars")]
for h in CASES:
    r = by[h]
    out.append(f"HD {h}: raw {r['N_obs_limpo']}, annual seasons {r['N_estacoes_anuais']}, HKP-1 {r['N_HKP1']}, HKP-2 {r['N_HKP2']}, "
               f"HIRES-1 {r['N_HIRES1']}, HIRES-2 {r['N_HIRES2']}, largest gap {r['maior_lacuna_yr']} yr, "
               f"t {r['t_min']}-{r['t_max']}")
write_out("13_series_roles.txt", "\n".join(out) + "\n")
n_raw1000 = sum(1 for r in rows if f(r["N_obs_limpo"]) >= 1000)
check("3.16-01", "stars in the Baum subset with >= 1000 raw observations (Livina & Lenton DFA floor 'of order a thousand points')", "",
      f"{n_raw1000}/59", "baum2022_59stars.csv; Livina & Lenton 2007 p. 3", info=True)
check("3.16-02", "stars in the Baum subset with >= 100 annual seasons (D24 floor)", "",
      f"{sum(1 for r in rows if f(r['N_estacoes_anuais']) >= 100)}/59", "baum2022_59stars.csv; D24", info=True)
check("3.16-03", "five clean Flat present in the Baum subset", "4/5", f"{sum(1 for h in FLAT5 if h in by)}/5",
      "audit/ERRATA_2026-11-14.md E-I12", info=True)
check("3.16-04", "CYCLE+Excellent controls present in the Baum subset", "6/13", f"{len(CTRL)}/13", "paper_state_v6.md §3.1", info=True)
