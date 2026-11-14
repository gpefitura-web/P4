# LAYOUT DO REPOSITÓRIO DE UM PAPER

```
<repo-do-paper>/                  # PRIVADO sempre, inclusive depois da submissão
├── kit/                          # cópia do kit (docs, pipeline, templates, revistas, programas, evolucao). Privada
├── CLAUDE.md                     # instruções permanentes: aponta para kit/CLAUDE.md + regras do paper
├── kit.yml                       # parâmetros e kit_version
├── CADERNO_PESQUISA.md  DECISIONS.md  PAPER_STATE.md  BACKLOG.md  PROMPT_PROXIMO_CHAT.md  FICHA_PAPER.md  LICOES_PENDENTES.md
├── .github/workflows/            # fetch_refs.yml, fetch_template.yml (branch no gatilho)
├── scripts/                      # pipeline instanciado + refs_list.yml
├── referencias/                  # PDFs, bib/, vizier/ (só ReadMe), web/, MANIFEST.json, DOWNLOAD_LOG.md. Privada
├── manuscrito/                   # SOMENTE o que vai ao Overleaf
├── repositorio/                  # ÚNICA pasta que vira pública
└── fora_repositorio/             # cálculos suplementares e exploração. Privada
```

## Regras por pasta

### `manuscrito/` (vai ao Overleaf)
- Autocontida: **nenhum caminho `../`** nos `.tex`. `scripts/sync_overleaf.sh` copia `repositorio/results_macros.tex` e `repositorio/figures/*` para dentro de `manuscrito/` (o P1 apontava para `../repositorio`, o que não funciona no Overleaf).
- Conteúdo: `main.tex`, `sec_*.tex` (neutros quanto à revista), `references.bib` (gerado), `journal_macros.tex` (gerado), `results_macros.tex` (copiado), `figures/`, classe e `.bst` da revista, `README.md`.
- `bash scripts/sync_overleaf.sh` gera `manuscrito_overleaf.zip` para enviar ao Overleaf. `template/` (arquivos baixados) não vai no zip.
- Varrida por `check_manuscript.py` (estilo e marcas de IA, conforme `kit.yml`).

### `repositorio/` (a única pública)
- O que o revisor precisa para reproduzir: notebook (jupytext `.py` + `.ipynb`), `requirements.txt`, `README.md`, `results_macros.tex`, `analysis_results.md`, `figures/`, `fonts/`.
- **Nada** de dados brutos (REG-DADOS), PDFs, caderno, decisões, menção ao kit ou a `fora_repositorio/`. `publish_repositorio.sh` recusa se encontrar.
- Varrida por `check_manuscript.py` (marcas de IA) e escrita em inglês (REG-IDIOMA).

### `fora_repositorio/` (privada)
- Exploração, diagnósticos, testes de ideias, cálculos suplementares que não vão a ninguém. Livre de formato.
- **REG-PROMOCAO**: nenhum número daqui entra no manuscrito. Se um resultado é útil, ele é reimplementado/formalizado no notebook de `repositorio/` (com especificação e aprovação) e reproduzido por lá.

### `kit/` (na raiz, privada)
- Cópia versionada junto com o paper para que qualquer sessão fria ache regras e scripts. Atualiza por `scripts/kit_sync.sh`.
- Não é editada durante a escrita: lições vão para `LICOES_PENDENTES.md`.

## Como publicar só `repositorio/`

O repositório do paper contém PDFs com direitos autorais, o caderno, o kit e todo o histórico: ele **não** se torna público.

1. `bash scripts/publish_repositorio.sh /caminho/para/<paper>-code`: roda `check_manuscript.py`, procura PDFs, arquivos grandes, segredos e menções a arquivos privados em `repositorio/`, e copia o conteúdo para um diretório limpo com um `git init` novo (sem histórico). Alternativa `publicacao.modo: subtree` em `kit.yml` (histórico do `repositorio/` via `git subtree split --prefix=repositorio`; confira se o histórico não tem arquivos que não devem ser públicos).
2. O usuário cria o repositório público vazio, adiciona o remoto e envia (com a sua autoria).
3. Liga o repositório ao Zenodo e obtém o DOI; o DOI entra na seção "Data availability" e na carta.
4. Depois de uma revisão ou erratum: repetir o passo 1 em um diretório novo e comparar.

## Visibilidade e GitHub
- Criar o repositório do paper como **privado**. Se o plano da conta não permitir Actions em privados, avisar o usuário (limites de minutos).
- Uma branch não torna nada público; só o repositório inteiro tem visibilidade.
