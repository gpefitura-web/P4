# Subsídios: layout atual do P4 e layout do Kit (item 10, I-27, D77)

**Pedido do pesquisador (2026-11-14):** "Subsídios." **Não escolhe.** Fonte: `kit/docs/LAYOUT_REPO.md`; estado atual medido por `inspecao/saidas/01_inventory.txt` (`1-01`, `1-02`, `1-03`).

## Mapa arquivo a arquivo
| Kit espera (raiz) | Hoje no P4 | Observação |
|---|---|---|
| `CLAUDE.md` (aponta para `kit/CLAUDE.md` e traz regras do paper) | `P4/CLAUDE.md` | o do P4 não aponta para o kit |
| `kit.yml` | só em `kit/kit.yml` (com campos `__PAPER_ID__`) | nunca preenchido para o P4 |
| `CADERNO_PESQUISA.md` | `P4/P4_RESEARCH_NOTEBOOK.md` | no Kit o caderno guarda estado atual e fatos por artigo; as decisões vão para `DECISIONS.md` (DEC-nn) |
| `DECISIONS.md` (DEC-01…) | decisões **D##** dentro do caderno (D01–D77) | numeração e arquivo diferentes; REG-CR do Kit pede Change Request em `DECISIONS.md` |
| `PAPER_STATE.md` (versão única atualizada) | `P4/paper_state_v4…v7.md` (um arquivo por versão) | v7 é o corrente |
| `BACKLOG.md`, `PROMPT_PROXIMO_CHAT.md`, `FICHA_PAPER.md` | não existem | |
| `LICOES_PENDENTES.md` | `P4/LICOES_PENDENTES.md` (criado em 2026-11-14) | no Kit fica na raiz |
| `referencias/` (PDFs, bib, vizier, web, `MANIFEST.json`, `DOWNLOAD_LOG.md`) | PDFs soltos na raiz do repositório (9) e `P4/bib/` (15 PDFs com `MANIFEST.json` e `DOWNLOAD_LOG.md`); TSVs do VizieR em `P4/data/` | D38 fixa `bib/` para PDFs e raiz para tabelas; o Kit manda dados brutos fora do repositório público (REG-DADOS) |
| `scripts/` (pipeline instanciado) | `P4/p4_pipeline.ipynb` (congelado) e `P4/inspecao/scripts/` | o pipeline do Kit é outro formato (jupytext .py + .ipynb, PADRAO_NOTEBOOK) |
| `manuscrito/`, `repositorio/`, `fora_repositorio/` | não existem | `P4/inspecao/` e `P4/consolidacao/` seriam `fora_repositorio/` (privados) |
| `.github/workflows/` | não existe | |

## Estado dos arquivos (medido)
- 24 dos arquivos do pacote têm cópia byte a byte na raiz do repositório e **nenhuma cópia diverge** (`1-02`, `1-03`).
- Só existem no pacote (`P4/`): `CLAUDE.md`, `README_HANDOFF.md`, o caderno, o protocolo, `paper_state_v5…v7`, A1–A14, `historico/`, `bib/`.
- O repositório está na branch de trabalho `claude/focused-ramanujan-rchb37`; o kit na raiz tem `VERSION` próprio (`kit/VERSION`).

## Conflitos entre o que o P4 decidiu e o que o Kit espera
1. **D38** (`bib/` para PDFs, tabelas na raiz) contra `referencias/`.
2. **D31** (o caderno só se atualiza no fecho) contra o Kit (caderno com seção "Estado atual" lida primeiro por qualquer sessão fria).
3. **D##** contra **DEC-nn**; as D01–D77 são imutáveis (regra 4 do CLAUDE.md do P4), de modo que uma migração só poderia **referenciar** as D## e não renumerá-las.
4. **Regra 7 do P4** ("dados de entrada ficam como estão; Python com `-I`") é compatível com REG-DADOS, mas o Kit tira dados brutos do repositório público.

## Alternativas e o que cada uma implica
| Alternativa | Implica |
|---|---|
| **Manter o layout** | acrescentar arquivos em `P4/`; nada se move; a consolidação assinada gera `p4_star_catalog.csv` e `P4_SOURCE_VALUES.md` no layout atual; migração só ao começar o manuscrito |
| **Migrar já** | rodada própria: mover (sem editar) PDFs e tabelas para `referencias/`, criar `kit.yml`, `DECISIONS.md` com remissão às D##, `PAPER_STATE.md` a partir do v7, `BACKLOG.md`, `PROMPT_PROXIMO_CHAT.md`, `FICHA_PAPER.md`; atualizar os caminhos citados em todos os documentos (`1-07` lista 23 nomes de arquivo citados e ausentes, que a migração reabre); exige decisão sobre D31 e D38 |
| **Migração parcial** | só `referencias/` e `LICOES_PENDENTES.md` na raiz, sem mexer no caderno nem nas D## |

Estado: **subsídios entregues; escolha pendente (D77).**
