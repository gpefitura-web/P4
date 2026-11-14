#!/bin/bash
# Compila manuscrito/main.tex: sincroniza macros/figuras, monta references.bib, roda pdflatex e bibtex, verifica estilo.
# Uso: bash scripts/build_manuscript.sh
set -e
cd "$(dirname "$0")/.."
bash scripts/sync_overleaf.sh --no-zip
cd manuscrito
python3 ../scripts/make_references_bib.py .
pdflatex -interaction=nonstopmode -halt-on-error main.tex > build.log || { tail -30 build.log; exit 1; }
if grep -q "\\\\citation" main.aux; then
  bibtex main >> build.log || true
  pdflatex -interaction=nonstopmode -halt-on-error main.tex >> build.log
fi
pdflatex -interaction=nonstopmode -halt-on-error main.tex > build_last.log
cat build_last.log >> build.log
# só o último passe vale para avisos: os intermediários sempre acusam citações indefinidas
grep -i -E "undefined|Warning.*(Citation|Reference)|Overfull \\\\hbox \(([2-9][0-9]|[0-9]{3})" build_last.log | head -20 || true
echo "Paginas: $(pdfinfo main.pdf | awk '/Pages/ {print $2}')"
python3 ../scripts/check_manuscript.py .
