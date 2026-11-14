#!/bin/bash
# Instancia o kit em um repositório de paper novo.
# Uso: bash bootstrap.sh <paper_id> <diretorio_do_repo_do_paper> [branch_de_trabalho]
# Rode a partir de um clone da branch kit/paper-workflow. O diretório de destino deve ser um repositório git
# (pode estar vazio). Nada é enviado ao GitHub.
set -e
KIT="$(cd "$(dirname "$0")" && pwd)"
ID="${1:?paper_id (ex.: P2)}"
DEST="${2:?diretório do repositório do paper}"
BRANCH="${3:-claude/${ID,,}-trabalho}"
mkdir -p "$DEST" && DEST="$(cd "$DEST" && pwd)"
[ "$DEST" = "$KIT" ] && { echo "destino não pode ser o próprio kit" >&2; exit 1; }
[ -e "$DEST/kit.yml" ] && { echo "$DEST já foi instanciado (kit.yml existe)" >&2; exit 1; }
VER=$(cat "$KIT/VERSION")

mkdir -p "$DEST"/{kit,scripts,.github/workflows,referencias/bib,referencias/web,manuscrito,repositorio/figures,fora_repositorio}
# 1. cópia do kit (privada, versionada junto)
(cd "$KIT" && tar --exclude=.git -cf - .) | (cd "$DEST/kit" && tar xf -)
# 2. pipeline instanciado
cp "$KIT"/pipeline/scripts/* "$DEST/scripts/"
for w in "$KIT"/pipeline/workflows/*.yml; do
  sed "s#__BRANCH__#$BRANCH#g" "$w" > "$DEST/.github/workflows/$(basename "$w")"
done
cp "$KIT/pipeline/refs_list.template.yml" "$DEST/scripts/refs_list.yml"
# 3. estado do paper (privado)
cp "$KIT/templates/CADERNO.template.md"          "$DEST/CADERNO_PESQUISA.md"
cp "$KIT/templates/DECISIONS.template.md"        "$DEST/DECISIONS.md"
cp "$KIT/templates/PAPER_STATE.template.md"      "$DEST/PAPER_STATE.md"
cp "$KIT/templates/BACKLOG.template.md"          "$DEST/BACKLOG.md"
cp "$KIT/templates/PROMPT_ABERTURA.template.md"  "$DEST/PROMPT_PROXIMO_CHAT.md"
cp "$KIT/templates/FICHA_PAPER.template.md"      "$DEST/FICHA_PAPER.md"
cp "$KIT/templates/LICOES_PENDENTES.template.md" "$DEST/LICOES_PENDENTES.md"
cp "$KIT/templates/CLAUDE.paper.md"              "$DEST/CLAUDE.md"
# 4. pastas
cp "$KIT/templates/README_manuscrito.md"  "$DEST/manuscrito/README.md"
cp "$KIT/templates/README_repositorio.md" "$DEST/repositorio/README.md"
cp "$KIT/templates/gitignore_manuscrito"  "$DEST/manuscrito/.gitignore"
cp "$KIT/templates/gitignore_repositorio" "$DEST/repositorio/.gitignore"
cp "$KIT/templates/gitignore_raiz"        "$DEST/.gitignore"
touch "$DEST/fora_repositorio/.gitkeep" "$DEST/referencias/.gitkeep"
cp "$KIT/templates/manuscrito_neutro"/sec_*.tex "$KIT/templates/manuscrito_neutro/results_extra.tex" "$DEST/manuscrito/"
# 5. parâmetros
sed -e "s#__PAPER_ID__#$ID#; s#__BRANCH__#$BRANCH#; s#__KIT_VERSION__#$VER#" "$KIT/kit.yml" > "$DEST/kit.yml"
sed -i "s#__PAPER_ID__#$ID#g" "$DEST/CLAUDE.md" "$DEST/PAPER_STATE.md" "$DEST/CADERNO_PESQUISA.md" "$DEST/DECISIONS.md" "$DEST/PROMPT_PROXIMO_CHAT.md" "$DEST/FICHA_PAPER.md"
sed -i "s#__BRANCH__#$BRANCH#g" "$DEST/PROMPT_PROXIMO_CHAT.md" "$DEST/CLAUDE.md"

(cd "$DEST" && bash scripts/apply_journal.sh >/dev/null && echo "módulo da revista aplicado ($(grep -E '^revista:' kit.yml | awk '{print $2}'))")
cat <<MSG
Paper $ID instanciado em $DEST (kit $VER, branch de trabalho $BRANCH).

Passos manuais (o bootstrap não faz nada fora da pasta):
  1. Repositório PRIVADO no GitHub e criação da branch $BRANCH (os workflows só disparam nela, por 'push' com 'paths').
  2. Secret ADS_DEV_KEY em Settings > Secrets and variables > Actions (chave do ADS: ui.adsabs.harvard.edu > Settings > API Token).
  3. Preencher FICHA_PAPER.md e scripts/refs_list.yml e levar a lista para aprovação (E3). NÃO baixar antes.
  4. Abrir a sessão do Claude Code na raiz e colar o conteúdo de PROMPT_PROXIMO_CHAT.md.
MSG
