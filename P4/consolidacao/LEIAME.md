# consolidacao/ — rascunho da consolidação (2026-11-24), NÃO ASSINADO

| Arquivo | O que é | Estado |
|---|---|---|
| `p4_star_catalog.csv` | catálogo do P4: as 112 linhas do catálogo congelado, com os reparos de `rascunho_reparos_catalogo.csv`, grupos (D102 R1), série disponível (D95), segmentos (D98, D100) e situação na amostra | rascunho para assinatura; gerado por `inspecao/scripts/18_build_consolidation.py` |
| `P4_SOURCE_VALUES.md` | tabela de valores com fonte, página, check, D## e grau (só A e B); C e X no apêndice | rascunho para assinatura |
| `LISTA_FINAL_ESTRELAS_2026-11-24.md` | lista datada das estrelas, com pontos a confirmar e bloco de assinatura | aguarda assinatura |
| `rascunho_reparos_catalogo.csv` | reparos mecânicos do catálogo (D64) | usado pelo catálogo |
| `PEDIDO_DADOS_OLAH_SOON.md` | rascunho de pedido de dados | **arquivado** (D86) |

O catálogo congelado `baliunas_table2_full.csv` não é alterado (D36). O pipeline permanece congelado até a assinatura (REG-01). Para regenerar: `bash inspecao/scripts/run_all.sh`.
