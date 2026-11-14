#!/bin/bash
# Torna manuscrito/ autocontido para o Overleaf: copia macros de resultados e figuras de repositorio/ para dentro dele
# e, por padrão, gera manuscrito_overleaf.zip (sem artefatos de compilação). REG-LAYOUT: nenhum caminho '../' no .tex.
# Uso: bash scripts/sync_overleaf.sh [--no-zip]
set -e
cd "$(dirname "$0")/.."
mkdir -p manuscrito/figures
[ -f repositorio/results_macros.tex ] && cp repositorio/results_macros.tex manuscrito/results_macros.tex
for f in repositorio/figures/*.pdf repositorio/figures/*.eps; do [ -f "$f" ] && cp "$f" manuscrito/figures/; done
if grep -rn --include=*.tex '\.\./' manuscrito | grep -v '^manuscrito/template/' | grep -v '%'; then
  echo "AVISO: caminho '../' em manuscrito/*.tex quebra no Overleaf" >&2
fi
if [ "$1" != "--no-zip" ]; then
  rm -f manuscrito_overleaf.zip
  (cd manuscrito && zip -rq ../manuscrito_overleaf.zip . -x 'template/*' '*.aux' '*.log' '*.out' '*.bbl' '*.blg' '*.toc' 'main.pdf' 'build.log' '.gitignore')
  echo "manuscrito_overleaf.zip pronto ($(du -h manuscrito_overleaf.zip | cut -f1))"
fi
