"""Stage 4 helper - dump the frozen notebook's cell sources with cell and line numbers.

Read-only: writes saidas/04_pipeline_cells.txt. Cell numbers are 0-based indices
into nb['cells'], the numbering used in MAPA_PIPELINE.md.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import json

from common import ROOT, write_out

with open(os.path.join(ROOT, "p4_pipeline.ipynb"), encoding="utf-8") as fh:
    nb = json.load(fh)
out = []
for i, c in enumerate(nb["cells"]):
    src = "".join(c["source"]).splitlines()
    out.append(f"===== cell {i} [{c['cell_type']}] exec_count={c.get('execution_count')} "
               f"outputs={len(c.get('outputs', []))} =====")
    out += [f"{i}:{n+1:03d}  {ln}" for n, ln in enumerate(src)]
    for o in c.get("outputs", []):
        if o.get("output_type") == "stream":
            txt = "".join(o.get("text", "")).splitlines()
            out += [f"{i}:out  {ln}" for ln in txt[:40]]
        elif o.get("output_type") == "error":
            out.append(f"{i}:ERR  {o.get('ename')}: {o.get('evalue')}")
write_out("04_pipeline_cells.txt", "\n".join(out) + "\n")
print(f"{len(nb['cells'])} cells dumped")

# ---- static checks of the notebook against the frozen catalogue ------------
import ast
import re

from common import check, read_csv

code = {i: "".join(c["source"]) for i, c in enumerate(nb["cells"]) if c["cell_type"] == "code"}
tree = ast.parse(code[8])
meta = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "BALIUNAS_STARS_META":
        meta = ast.literal_eval(node.value)
cat = read_csv("baliunas_table2_full.csv").set_index("HD")
STD17 = ("9562 13421 29645 45067 76572 89744 107213 124570 136202 142373 143761 159332 "
         "187013 187691 207978 212754 216385").split()  # audit/A6_saar.md §3
APPB = "3443 39587 76572 81809 88355 114378 124570 137107 141004 156026 158614 178428".split()
rows = []
for hd, name, sp, smean, sstd, pcyc, grp in meta:
    key = "219834B" if hd == 219834 else str(hd)
    r = cat.loc[key]
    rows.append(dict(hd=key, grp=grp, S_nb=smean, S_cat=float(r.S), P_nb=pcyc,
                     P_cat=r.P_cyc, cls=r.primary_class, fap=r.FAP,
                     std=key in STD17, appb=key in APPB))
check("4-01", "stars hard-coded in notebook cell 8", "", len(rows), "p4_pipeline.ipynb cell 8",
      info=True)
check("4-02", "cell 8 rows whose S_mean differs from the catalogue <S>", 0,
      sum(1 for r in rows if abs(r["S_nb"] - r["S_cat"]) > 1e-9),
      "baliunas_table2_full.csv (D08)")
check("4-03", "cell 8 'Cycling' rows whose catalogue class is not CYCLE with FAP Good/Excellent",
      0, sum(1 for r in rows if r["grp"] == "Cycling"
             and not (r["cls"] == "CYCLE" and r["fap"] in ("Good", "Excellent"))),
      "p4_pipeline.ipynb cell 7 (group definition) vs catalogue")
check("4-04", "cell 8 'Irregular' rows (defined in cell 7 as Long or Var): catalogue class",
      "Long or Var for all", "; ".join(f"{r['hd']}={r['cls']}"
                                         + (f"/{r['fap']} P={r['P_cat']}" if r['cls'] == 'CYCLE' else "")
                                         for r in rows if r["grp"] == "Irregular"),
      "baliunas_table2_full.csv; P4_RESEARCH_NOTEBOOK.md D09")
check("4-05", "cell 8 'Flat' rows: catalogue class | standard star (D13) | Appendix B binary",
      "", "; ".join(f"{r['hd']}={r['cls']}|std={r['std']}|bin={r['appb']}"
                    for r in rows if r["grp"] == "Flat"),
      "P4_RESEARCH_NOTEBOOK.md D13; audit/A6_saar.md §3; audit/A1_baliunas.md §2.5", info=True)
check("4-06", "cell 8 rows with P_cyc = 0.00 while the catalogue has a period", 0,
      sum(1 for r in rows if r["P_nb"] == 0 and r["P_cat"] != ""),
      "baliunas_table2_full.csv")
check("4-07", "cell 8 contains HD 4915", "no", "yes" if any(r["hd"] == "4915" for r in rows) else "no",
      "P4_RESEARCH_NOTEBOOK.md D07")
allcode = "\n".join(code.values())
pats = {"4-08": ("stats.kendalltau used for p-values (D22)", r"stats\.kendalltau"),
        "4-09": ("ARMA / surrogate code present (D22)", r"(?i)arma|surrogate"),
        "4-10": ("n_max = N // 4 (D26)", r"N // 4"),
        "4-11": ("crossover check present (D26)", r"(?i)crossover"),
        "4-12": ("H = (beta + 1) / 2 computed (D28)", r"\(beta \+ ?1\) ?/ ?2"),
        "4-13": ("nolds imported or called (D29)", r"\bnolds\b"),
        "4-14": ("0.179 present as a constant (D17)", r"=\s*0\.179\b"),
        "4-15": ("S_SUN_MEAN = 0.1694 (D16)", r"S_SUN_MEAN\s*=\s*0\.1694"),
        "4-16": ("mannwhitneyu between groups", r"mannwhitneyu"),
        "4-17": ("sensitivity windows (0.25, 0.40, 0.50, 0.60, 0.75) (D20)",
                 r"\(0\.25, 0\.40, 0\.50, 0\.60, 0\.75\)"),
        "4-18": ("Gaussian sigma fixed at 1.0 yr, no sweep (Q3)", r"sigma_yr=1\.0")}
for cid, (desc, rx) in pats.items():
    cells = [i for i, s in code.items() if re.search(rx, s)]
    check(cid, f"notebook: {desc} - code cells", "", ",".join(map(str, cells)) or "none",
          "p4_pipeline.ipynb", info=True)
err = [(i, o.get("ename")) for i, c in enumerate(nb["cells"]) for o in c.get("outputs", [])
       if o.get("output_type") == "error"]
executed = [i for i, c in enumerate(nb["cells"]) if c.get("execution_count")]
check("4-19", "cells with a stored execution count | cells whose stored output is an error", "",
      f"{executed} | {err}", "p4_pipeline.ipynb", info=True)
