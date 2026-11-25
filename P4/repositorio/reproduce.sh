#!/usr/bin/env bash
# Reproduces every number, table and figure of the manuscript from the input data and compares them with the published outputs.
# Usage: PYTHON=/path/to/python bash reproduce.sh      (about 6 minutes; Python 3.13 with requirements.txt)
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
PY="${PYTHON:-python3}"
export SOURCE_DATE_EPOCH=0
"$PY" -I pipeline_v2/fetch_egeland_table4.py       # Table 4 of Egeland et al. is downloaded, not redistributed (needs network; or: --from FILE)
"$PY" -I verify_reproduction.py --manifest        # the folder is exactly the published one
"$PY" -I verify_reproduction.py --snapshot        # keep the published outputs in _published/ and clear them
cd pipeline_v2
for t in 1 2 3 4 6 7; do echo "test_step$t: $("$PY" -I test_step$t.py | tail -1)"; done
echo "test_step5 (size of the surrogate test, ~2 min): $("$PY" -I test_step5.py | tail -1)"
"$PY" -I power_simulation.py > /dev/null
"$PY" -I run_all.py                                # the single stellar run, fixed seeds (~1 min)
"$PY" -I group_primary.py > /dev/null
"$PY" -I report.py
"$PY" -I make_macros.py
"$PY" -I make_tables.py
"$PY" -I make_figures.py
cd ..
"$PY" -I verify_reproduction.py --compare
if command -v pdflatex >/dev/null; then
  cd manuscrito && pdflatex -interaction=nonstopmode main.tex >/dev/null && bibtex main >/dev/null || true
  pdflatex -interaction=nonstopmode main.tex >/dev/null; pdflatex -interaction=nonstopmode main.tex | tail -2
fi
