#!/bin/bash
# Compara kit_version de kit.yml com kit/VERSION e atualiza SÓ pipeline e docs a partir de uma cópia nova do kit.
# Nunca toca em CADERNO, DECISIONS, PAPER_STATE, referencias/, manuscrito/, repositorio/, fora_repositorio/.
# Uso: bash scripts/kit_sync.sh <caminho_do_kit_novo>   (clone da branch kit/paper-workflow)
set -e
cd "$(dirname "$0")/.."
NEW="${1:?caminho do clone novo do kit}"
OLDV=$(grep -E '^kit_version:' kit.yml | awk '{print $2}' | tr -d '"')
NEWV=$(cat "$NEW/VERSION")
echo "kit do paper: $OLDV  |  kit novo: $NEWV"
[ "$OLDV" = "$NEWV" ] && { echo "nada a atualizar"; exit 0; }
echo "--- CHANGELOG novo ---"; cat "$NEW/evolucao/CHANGELOG.md"; echo "-----------------------"
read -r -p "Aplicar (sobrescreve kit/, scripts/ e workflows)? [s/N] " ok
[ "$ok" = "s" ] || exit 0
rm -rf kit && mkdir kit && (cd "$NEW" && tar --exclude=.git -cf - .) | (cd kit && tar xf -)
cp kit/pipeline/scripts/* scripts/
for w in kit/pipeline/workflows/*.yml; do
  B=$(grep -E '^branch:' kit.yml | awk '{print $2}')
  sed "s#__BRANCH__#$B#g" "$w" > ".github/workflows/$(basename "$w")"
done
sed -i "s/^kit_version:.*/kit_version: \"$NEWV\"/" kit.yml
echo "Atualizado para $NEWV. Revise 'git diff' e registre em DECISIONS.md se mudou alguma regra."
