#!/bin/bash
# Aplica o módulo de uma revista ao manuscrito: copia kit/revistas/<revista>/latex/* para manuscrito/ (sem sobrescrever sec_*.tex
# nem main.tex existentes, a menos que --force-main). Troca de revista nas etapas finais = rodar de novo com --force-main.
# Uso: bash scripts/apply_journal.sh [revista] [--force-main]
set -e
cd "$(dirname "$0")/.."
REV="${1:-$(grep -E '^revista:' kit.yml | awk '{print $2}' | tr -d '"')}"
FORCE="$2"
SRC="kit/revistas/$REV/latex"
[ -d "$SRC" ] || { echo "módulo $SRC não existe (copie kit/revistas/_TEMPLATE)" >&2; exit 1; }
mkdir -p manuscrito
for f in "$SRC"/*; do
  b=$(basename "$f")
  case "$b" in
    main.tex) [ -f manuscrito/main.tex ] && [ "$FORCE" != "--force-main" ] && { echo "main.tex existe; use --force-main para trocar (faça backup)"; continue; } ;;
    ORIGEM.md) cp -r "$f" manuscrito/template_ORIGEM.md; continue ;;
  esac
  cp -r "$f" manuscrito/
done
for s in intro methods results discussion conclusions backmatter; do
  [ -f manuscrito/sec_$s.tex ] || cp kit/templates/manuscrito_neutro/sec_$s.tex manuscrito/
done
for f in results_extra.tex results_macros.tex; do
  [ -f manuscrito/$f ] || { [ -f kit/templates/manuscrito_neutro/$f ] && cp kit/templates/manuscrito_neutro/$f manuscrito/; } || true
done
touch manuscrito/results_macros.tex
echo "revista $REV aplicada em manuscrito/. Edite kit.yml: revista, se mudou."
