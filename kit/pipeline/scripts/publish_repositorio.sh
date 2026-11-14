#!/bin/bash
# Exporta SÓ repositorio/ para um diretório limpo (futuro repositório público), com verificações.
# O repositório do paper (kit, caderno, referências, histórico) permanece privado. Nada é enviado ao GitHub aqui.
# Uso: bash scripts/publish_repositorio.sh <diretorio_destino_vazio>
set -e
cd "$(dirname "$0")/.."
DEST="${1:?informe o diretório de destino (vazio ou inexistente)}"
[ -d "$DEST" ] && [ -n "$(ls -A "$DEST")" ] && { echo "destino não está vazio: $DEST" >&2; exit 1; }
python3 scripts/check_manuscript.py manuscrito > /dev/null || { echo "check_manuscript.py reprovou; corrija antes de publicar" >&2; exit 1; }
BAD=$(find repositorio -type f \( -name '*.pdf' -o -size +5M \) ! -path '*/figures/*' ! -path '*/fonts/*' | head)
[ -n "$BAD" ] && { echo "arquivos suspeitos (PDF fora de figures/ ou > 5 MB):"; echo "$BAD"; exit 1; }
if grep -rIlE '(ADS_DEV_KEY|api[_-]?key|secret|token)[[:space:]]*[:=][[:space:]]*[A-Za-z0-9]{16,}' repositorio; then
  echo "possível segredo em repositorio/ (arquivos acima)" >&2; exit 1
fi
if grep -rIlE 'CADERNO_PESQUISA|DECISIONS\.md|PAPER_STATE|fora_repositorio|\bkit/' repositorio; then
  echo "repositorio/ menciona arquivos privados (acima); remova as menções" >&2; exit 1
fi
mkdir -p "$DEST"
(cd repositorio && tar --exclude=data_cache --exclude=__pycache__ --exclude=.ipynb_checkpoints -cf - .) | (cd "$DEST" && tar xf -)
(cd "$DEST" && git init -q && git add -A && echo "Pronto em $DEST. Revise 'git -C $DEST status', crie o repositório público vazio, adicione o remoto e faça o commit/push com a sua autoria. DOI: ligue o repositório ao Zenodo.")
