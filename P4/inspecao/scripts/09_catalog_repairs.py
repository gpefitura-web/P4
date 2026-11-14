"""Phase 3 - mechanical repairs of baliunas_table2_full.csv, as a side file (D36).

The frozen catalogue is NOT modified. The output lists, per star and field, the current value,
the proposed value, the source with page and the grade. Values come from the printed Table 2
of Baliunas+1995 (PDF pp. 12-13 = journal pp. 280-281), read twice: visual inspection of the
400 dpi render and RapidOCR on the same render (see audit/ERRATA_2026-11-14.md, E-41).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import csv
import re

from common import ROOT, check, read_csv

b = read_csv("baliunas_table2_full.csv").set_index("HD")
SRC = "Baliunas+1995 Table 2, journal p. {}"
# HD, field, proposed value, journal page, grade, note
VALUES = [
    ("10780", "P_cyc_tentativo", ">7", 280, "A", "nota de rodape s ('Sparse data prior to 1980, not included in periodogram analysis'); sem FAP"),
    ("88737", "P_cyc_tentativo", "24?", 280, "A", "sem FAP"),
    ("111456", "P_cyc_tentativo", "7?", 280, "B", "nota s; o '7' foi lido por um motor de OCR como 'T'; sem FAP"),
    ("126053", "P_cyc_tentativo", "22?", 280, "A", "sem FAP"),
    ("176051", "P_cyc_tentativo", "10?", 281, "B", "nota s; o segundo motor leu \"10'?\"; sem FAP"),
    ("185144", "P_cyc_tentativo", "7?", 281, "B", "nota s; o '7' foi lido por um motor de OCR como 'T'; sem FAP"),
    ("219834A", "P_cyc", "21", 281, "A", "21 +- 1, Good; v4 §2 defeito a"),
    ("219834A", "dP", "1", 281, "A", ""),
    ("76572", "P_cyc", "7.1", 280, "A", "7.1 +- 0.2, Poor; v4 §2 defeito b (a linha tem n_pass = 1 no CSV)"),
    ("76572", "dP", "0.2", 280, "A", ""),
]
rows = []
for hd, field, new, page, grade, note in VALUES:
    cur = b.loc[hd, field] if field in b.columns else "(campo novo)"
    rows.append([hd, field, cur, new, SRC.format(page), grade, note])
legit = re.compile(r"^(Long|\d+(\.\d+)?\s*\+\s*\d+(\.\d+)?,\s*(excellent|good|fair|poor))$", re.I)
nsec = 0
for hd, r in b.iterrows():
    s = r.secondary
    if s != "" and not legit.match(s):
        rows.append([hd, "secondary", s, "", "A6 §5 F14c; A1 §1.1", "A",
                     "residuo de OCR de uma celula impressa vazia ('...'); normalizar para vazio"])
        nsec += 1
out = os.path.join(ROOT, "consolidacao")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "rascunho_reparos_catalogo.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["HD", "campo", "valor_atual", "valor_proposto", "fonte", "grau", "nota"])
    w.writerows(rows)
check("3.13-01", "value repairs proposed (6 tentative periods + 219834A x2 + 76572 x2)", 10, len(VALUES),
      "audit/ERRATA_2026-11-14.md E-I41")
check("3.13-02", "secondary-column normalisations proposed", 33, nsec, "inspecao/scripts/03a_baliunas.py (3.1-15)")
check("3.13-03", "repairs with grade A | B", "", f"{sum(1 for r in rows if r[5]=='A')} | {sum(1 for r in rows if r[5]=='B')}",
      "consolidacao/rascunho_reparos_catalogo.csv", info=True)
check("3.13-04", "frozen catalogue untouched (rows | columns)", "112 | 14",
      f"{len(b)} | {len(b.columns) + 1}", "baliunas_table2_full.csv")
