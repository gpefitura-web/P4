#!/usr/bin/env bash
# Regenerates macros, table and figures from pipeline_v2/results, then compiles main.tex (needs pdflatex and bibtex).
# Usage: PYTHON=/path/to/python bash manuscrito/build.sh
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; PY="${PYTHON:-python3}"
for s in make_macros.py make_tables.py make_figures.py; do "$PY" -I "$HERE/../pipeline_v2/$s"; done
cd "$HERE"; pdflatex -interaction=nonstopmode main.tex >/dev/null; bibtex main >/dev/null || true
pdflatex -interaction=nonstopmode main.tex >/dev/null; pdflatex -interaction=nonstopmode main.tex | tail -2
