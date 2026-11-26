#!/usr/bin/env bash
# Regenerates the marked blocks of main.tex (macros, table), calibration_macros.tex, cal_table_*.tex and the figures from pipeline_v2/results and results_calibration, then compiles.
# main.tex holds the whole manuscript; only the figures and references.bib are separate files.
# Usage: PYTHON=/path/to/python bash manuscrito/build.sh   (needs pdflatex, bibtex, lmodern)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; PY="${PYTHON:-python3}"
for s in make_macros.py make_tables.py make_figures.py make_macros_calibration.py make_tables_calibration.py make_figures_calibration.py; do "$PY" -I "$HERE/../pipeline_v2/$s"; done
cd "$HERE"; pdflatex -interaction=nonstopmode main.tex >/dev/null; bibtex main >/dev/null || true
pdflatex -interaction=nonstopmode main.tex >/dev/null; pdflatex -interaction=nonstopmode main.tex | tail -2
