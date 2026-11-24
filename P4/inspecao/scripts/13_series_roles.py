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

# ---- consecutive-year structure of the annual series (feasibility of rolling windows, D92) ----------------
from collections import defaultdict

yrs = defaultdict(set)
for ln in open(os.path.join(ROOT, "data", "J_AJ_163_183_table1.tsv"), encoding="utf-8"):
    if ln.startswith("#") or ";" not in ln:
        continue
    p = [x.strip() for x in ln.rstrip("\n").split(";")]
    if p[0].isdigit() and p[4] != "sigma":
        yrs[p[0]].add(int(float(p[2])))


def run_info(s):
    s = sorted(s)
    best = cur = 1
    gaps = []
    for a, b in zip(s, s[1:]):
        if b == a + 1:
            cur += 1
        else:
            gaps.append(b - a - 1)
            cur = 1
        best = max(best, cur)
    return len(s), best, gaps


lines = ["HD | group | annual seasons | longest run of consecutive years | missing-year gaps | half of seasons"]
worse = 0
for grp, l in (("Flat", [h for h in FLAT5 if h in yrs]), ("CYCLE+Excellent", [h for h in CTRL if h in yrs]), ("case", ["101501"])):
    for h in l:
        n, best, gaps = run_info(yrs[h])
        lines.append(f"{h} | {grp} | {n} | {best} | {gaps} | {n // 2}")
        if best < n // 2:
            worse += 1
write_out("13_annual_runs.txt", "\n".join(lines) + "\n")
check("3.16-05", "stars (Flat, CYCLE+Excellent, HD 101501 with Table 1 rows) whose longest consecutive-year run is shorter than half of their seasons",
      "", f"{worse}/{len(lines) - 1}", "data/J_AJ_163_183_table1.tsv (sigma-flagged rows removed)", info=True)

# ---- gap-length census for the interpolation question (D95) -------------------------------------
allg = []
for grp, l in (("Flat", [h for h in FLAT5 if h in yrs]), ("CYCLE+Excellent", [h for h in CTRL if h in yrs]), ("case", ["101501"])):
    for h in l:
        allg += run_info(yrs[h])[2]
check("3.16-06", "missing-year gaps in the annual series of the 10 stars: total | of 1-2 years | of 3 years or more", "",
      f"{len(allg)} | {sum(1 for g in allg if g <= 2)} | {sum(1 for g in allg if g >= 3)}",
      "data/J_AJ_163_183_table1.tsv; saidas/13_annual_runs.txt", info=True)
