#!/usr/bin/env bash
# Regenerate inspecao/checks.csv and inspecao/saidas/ from scratch.
# Usage: PYTHON=/path/to/python bash inspecao/scripts/run_all.sh
# Needs numpy, pandas and scipy. All scripts are run with -I (isolated mode).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="${PYTHON:-python3}"
rm -f "$HERE/../checks.csv"
for s in 01_inventory.py 02_build_notebook_proposal.py 03a_baliunas.py 03b_baum.py 03d_luhn.py 03f_isaacson_noyes.py \
         03h_crossmatch_groups.py 04_dump_notebook.py 05_olah_periods.py 06_pdf_quotes.py 08_egeland_t4.py 09_catalog_repairs.py 10_dataverse_hd166620.py 11_dataverse_v2001.py 13_series_roles.py; do
  echo "== $s"
  "$PY" -I "$HERE/$s" > "$HERE/../saidas/log_${s%.py}.txt" 2>&1 || { echo "FAILED: $s"; exit 1; }
done
"$PY" -I - "$HERE/../checks.csv" <<'PYEOF'
import csv, sys, collections
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
c = collections.Counter(r["resultado"] for r in rows)
print(f"checks: {len(rows)}  PASS={c['PASS']}  FAIL={c['FAIL']}  INFO={c['INFO']}")
for r in rows:
    if r["resultado"] == "FAIL":
        print("  FAIL", r["id"], "|", r["descricao"][:90], "| exp", r["valor_esperado"][:40],
              "| got", r["valor_obtido"][:60])
PYEOF
