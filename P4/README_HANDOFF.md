# P4 — pacote de estado para continuar no Claude Code

Gerado em 2026-11-14 a partir do Project "P4" (claude.ai) e do repositório github.com/gpefitura-web/P4 (único commit, "Add files via upload"). O estado reflete o fecho da segunda rodada de auditoria, 2026-08-01.

## Ordem de leitura
1. `CLAUDE.md` — regras permanentes
2. `paper_state_v6.md` — estado corrente
3. `DECISOES_D41_D54.md` — decisões novas, ainda não incorporadas ao caderno
4. `P4_RESEARCH_NOTEBOOK.md` — memória longa, D01–D40, questões abertas e fechadas
5. `P4_AUDIT_PROTOCOL.md` — regras da auditoria, graus A/B/C/X
6. `audit/` — uma auditoria por fonte

## Conteúdo
| Onde | O quê | Origem |
|---|---|---|
| raiz | `paper_state_v6.md`, `paper_state_v5.md`, `paper_state_v4.md` | v4 e v6 do repositório, v5 do Project |
| raiz | `P4_RESEARCH_NOTEBOOK.md`, `P4_AUDIT_PROTOCOL.md` | Project |
| raiz | `DECISOES_D41_D54.md` | repositório (idêntico ao do Project) |
| raiz | `p4_pipeline.ipynb` | repositório, congelado |
| raiz | `baliunas_table2_full.csv`, `baum2022_59stars.csv`, `baum2022_cycle_periods.csv`, `isaacson2024_least_active_50.csv`, `noyes1984_validade_cor.csv` | repositório (os dois primeiros conferidos byte a byte com os do Project) |
| `audit/` | A1 a A4 | Project |
| `audit/` | A5, A6, A9 a A12, `saar_baliunas_crossmatch.csv`, `a9_instrument_step.csv` | repositório |
| `data/` | sete TSVs do VizieR | repositório |
| `historico/` | `paper_state_v2.md`, superado | Project |

## Nomes dos TSVs
No repositório os nomes têm dois-pontos, que o Windows não aceita. Aqui os `:` viraram `_`. Os documentos usam o nome antigo.

| Nome nos documentos | Nome em `data/` | Artigo |
|---|---|---|
| `J:AJ:163:183:table1.tsv` | `J_AJ_163_183_table1.tsv` | Baum+2022, séries de S (62 135 obs.) |
| `J:163:183:table2.tsv` | `J_163_183_table2.tsv` | Baum+2022, parâmetros (59 estrelas) |
| `J:ApJ:936:L23:table2.tsv` | `J_ApJ_936_L23_table2.tsv` | Luhn+2022, S_HK de HD 166620 |
| `J:ApJ:936:L23:table3.tsv` | `J_ApJ_936_L23_table3.tsv` | Luhn+2022, fotometria APT |
| `J:ApJS:274:35:table2.tsv` | `J_ApJS_274_35_table2.tsv` | Isaacson+2024 (CLS V), 710 estrelas |
| `J:ApJS:274:35:table3.tsv` | `J_ApJS_274_35_table3.tsv` | Isaacson+2024, séries do Keck |
| `J:ApJS:274:35:table4.tsv` | `J_ApJS_274_35_table4.tsv` | Isaacson+2024, 138 ciclos |

## O que ficou de fora
- **PDFs** (85 MB): estão no repositório GitHub. `bib/` vai vazio. O PDF de Oláh+2016, citado em A10 §6 como `bib/aa28479-16.pdf`, não apareceu na raiz do repositório clonado.
- **Documentos do programa geral**, que continuam só no Project: `UNIVERSAL_PAPER_CONTEXT.md` (inclui o estilo Super Mongo das figuras e o template LaTeX), `FASE1_PAPERS_P1_P12.md`, `SUBMISSION_STRATEGY_TIMELINE.md`. Quando chegar a etapa de figuras, copie o `UNIVERSAL_PAPER_CONTEXT.md` para esta pasta.
- **Não existem em lugar nenhum**: `P4_DECISION_SUPPORT_6.1.md` e `COWORK_PROMPT_A9_A12.md` (citados no caderno), `P4_SOURCE_VALUES.md` e `p4_star_catalog.csv` (só nascem na consolidação), `audit/A7_theory.md` e `audit/A8_usoskin.md` (unidades não executadas).

## Pendência de documentação
O caderno `P4_RESEARCH_NOTEBOOK.md` ainda não recebeu D41–D54, Q10 e Q11. A instrução de incorporação está no topo de `DECISOES_D41_D54.md`. O prompt de inspeção pede ao Claude Code uma versão proposta, sem sobrescrever o original.

## Se for atualizar o Project depois
O Project tem `paper_state_v2`, `v4`, `v5` e `v6` e os documentos A1 a A12. As cópias deste pacote vêm de lá ou do repositório sem alteração de conteúdo. Só os dois arquivos novos (`CLAUDE.md` e este README) e o prompt não existem no Project.
