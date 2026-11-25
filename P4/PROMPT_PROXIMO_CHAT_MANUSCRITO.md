# PROMPT_PROXIMO_CHAT_MANUSCRITO: modificações e correções do manuscrito P4 (2026-11-25)

**Para colar na abertura da próxima conversa.** Português nas conversas; código, comentários e saídas de script em inglês; `python -I` ao ler `data/`. Repositório `gpefitura-web/P4`, branch de trabalho `claude/focused-ramanujan-rchb37`, pacote em `P4/`. Último commit de conteúdo antes do fecho: `be93d62`; o commit de fecho vem depois (`git log -3`). Não criar pull request.

## 0. Regra principal desta etapa
**Tudo que vai para o manuscrito precisa ser sustentado no repositório (`P4/repositorio/`).** Números: macros gerados de `pipeline_v2/results/` (nunca digitados). Figuras e tabelas: scripts do pacote. Afirmações sobre dados, código ou escolhas de análise: arquivo do pacote que as sustente, ou citação declarada com PDF e página. **Fluxo obrigatório para qualquer mudança:** editar a fonte (`pipeline_v2/`, `manuscrito/`, `data/`, `consolidacao/`) → `python3 P4/make_repositorio.py` → `bash repositorio/reproduce.sh` numa **cópia limpa** fora do projeto (exige `REPRODUCTION OK`) → só então atualizar `manuscrito_overleaf.zip` e `repositorio_zenodo_v1.0.0.zip` e registrar. O que o pacote não sustenta hoje está listado em `RASTREABILIDADE_PENDENTE.md`.

## 1. Antes de qualquer coisa (ordem fixa)
1. `git pull`; ler **só**: `P4/CLAUDE.md` → `P4/paper_state_v9.md` → `P4/MANUSCRITO_PENDENCIAS.md` → `P4/RASTREABILIDADE_PENDENTE.md` → `P4/repositorio/README.md` → `P4/kit/revistas/new-astronomy/ficha.md` (em `kit/revistas/...` na raiz do repositório) → este arquivo. O caderno (`P4_RESEARCH_NOTEBOOK.md`, D01–D118) é consulta: buscar por D## com Grep.
2. Conferir os hashes da referência congelada (`consolidacao/APROVACAO_2026-11-24.md`: catálogo `ab480cb3…`, SOURCE_VALUES, lista final, `baliunas_table2_full.csv`, `p4_pipeline.ipynb`). Se algum não bater, parar e avisar.
3. Ambiente (some entre sessões): `python3 -m venv <scratchpad>/venv && pip install -r P4/repositorio/requirements.txt` (Python 3.13); TeX: `apt-get install -y --no-install-recommends texlive-latex-base texlive-latex-recommended texlive-fonts-recommended texlive-publishers lmodern cm-super`; o download da Tabela 4 de Egeland exige `SSL_CERT_FILE=/root/.ccr/ca-bundle.crt` neste ambiente.

## 2. O que está feito (D105–D118; detalhe em `paper_state_v9.md`)
- Pipeline `pipeline_v2/` executado **uma vez** (semente 20261124); resultados em `pipeline_v2/results/`. Reexecutar `run_all.py` no projeto **não** é permitido sem pedido explícito (é a execução oficial, D04); reproduzir em cópia limpa é o caminho.
- Manuscrito: `manuscrito/main.tex` (classe `elsarticle`, New Astronomy; **todo o texto num arquivo**; blocos `%%% BEGIN/END GENERATED MACROS` e `TABLE` regravados por `make_macros.py` e `make_tables.py`; **não editar dentro dos blocos**), `references.bib` (Crossref), `figures/Figure_1-4.{pdf,eps}` (Courier Prime, cor), `highlights.docx/.tex`. Título em uso: "Testing critical slowing down in Mount Wilson S-index of Sun-like stars".
- Pacote `repositorio/` (95 arquivos, MIT, `MANIFEST.sha256`, `reproduce.sh` de cerca de 6 minutos, Tabela 4 de Egeland **baixada**, não copiada) com prova em pasta limpa `REPRODUCTION OK`.
- Revisões independentes de figuras e texto aplicadas (`REVISOES_INDEPENDENTES.md`); guia da New Astronomy conferido (`ficha.md`).

## 3. Trabalho da próxima conversa (em ordem; um commit por item)
1. **Rastreabilidade** (`RASTREABILIDADE_PENDENTE.md`): transformar em macros gerados as contagens digitadas à mão (2 de 192 combinações e os dois casos HD 23249 e HD 217014; "23 segmentos", "51 anos", "28 a 36 pontos", "12 a 26 pontos", "de 20"); criar `check_manuscript_constants.py` no pacote que confronte as constantes de projeto do texto com o código e falhe se divergirem; incluí-lo em `reproduce.sh`; ligar "112" e "5 Flat limpas" a um teste do catálogo. Depois: `make_repositorio.py`, prova em pasta limpa, zips.
2. **Modificações e correções que o pesquisador trouxer** (texto, figuras, tabelas), sempre pelo fluxo da seção 0.
3. **Texto alternativo das figuras** (em `main.tex` ou arquivo à parte, conforme o guia); revisão de leitura final com PDF recompilado **depois** da última edição (conferir a data do PDF).
4. Manter atualizados `MANUSCRITO_PENDENCIAS.md`, `paper_state_v9.md` (ou v10), o caderno (nova D## por etapa) e `LICOES_PENDENTES.md`.

## 4. ANTILOOP e limites
- Não reabrir o que está decidido (D105–D118; e D01–D104 como estão). Decisão revogada = nova D## com `status: revogada` na antiga, nunca edição.
- No máximo 2 tentativas por falha; na segunda, registrar o bloqueio e seguir com o que é independente. Sem sleep nem polling; tarefas longas em segundo plano, com aviso de conclusão.
- **Não editar** `p4_pipeline.ipynb`, `baliunas_table2_full.csv`, `consolidacao/*` congelados nem resultados de `pipeline_v2/results/` fora do fluxo da seção 0.
- Nenhum nome de ferramenta ou de modelo de IA em arquivos do repositório, do pacote ou do manuscrito; a **declaração de IA é do pesquisador** (escreve no Overleaf). Financiamento, conflito de interesses e CRediT são afirmações dele: não alterar sem pedido.
- Commits terminam com as linhas de atribuição indicadas pela sessão. Push na branch de trabalho; nenhum pull request.

## 5. Com o pesquisador (não fazer por ele)
Declaração de IA no Overleaf; e-mail do autor correspondente e endereço postal; publicação no Zenodo e DOI (roteiro em `ZENODO_DEPOSITO.md`; depois pôr o DOI em `main.tex` e em `references.bib` e refazer o pacote); licença dos artigos de Baum e de Luhn; lista de elegíveis do acordo CAPES–Elsevier e participação do IFTM; título final; consulta opcional ao editor da New Astronomy.

## 6. Entregáveis de cada etapa
`REPRODUCTION OK` em pasta limpa, manifesto e zips atualizados, `MANUSCRITO_PENDENCIAS.md` em dia, commit e push. Ao terminar: relatório curto em português com os arquivos alterados e o que ficou pendente; **nada de novas frentes**.
