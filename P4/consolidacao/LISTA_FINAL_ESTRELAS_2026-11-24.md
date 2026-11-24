# Lista final de estrelas — RASCUNHO PARA ASSINATURA (2026-11-24)

**Estado:** preparada por Claude a pedido do pesquisador; **não assinada**. Cumpre R2 (D102): a lista é escrita e datada **antes de calcular qualquer indicador temporal**; até esta data **nenhum AR(1), variância em janela ou τ de Kendall foi calculado em estrela real** (o que existe são estatísticas descritivas e testes sintéticos sem valores de S).

**Catálogo:** `consolidacao/p4_star_catalog.csv`, sha256 `ab480cb3d2fae1cd2bc053d45636b816e169c09ef1d58e189c525d2b5bf962ed`; catálogo congelado `baliunas_table2_full.csv`, sha256 `9ab820d56eae87245e442a92f5a4e25777f051197cd6e37bac544df20c3575af` (inalterado).
**Regras aplicadas (só as decididas):** D13 (padrões excluídas); R1 (cinco `Flat`); R11 (HD 81809 e 219834A fora); D95 opção (v) (Baum e v2001, Sol por Egeland); D98 (lacunas); D100 (segmento ≥ 24 anos). Nada foi escolhido olhando valores de S.

## Contagem por grupo e situação

| Grupo | Situação | n |
|---|---|---|
| CYCLE_Excellent | excluida | 1 |
| CYCLE_Excellent | incluida | 9 |
| CYCLE_Excellent | sem_serie | 3 |
| Flat_limpa | incluida | 4 |
| Flat_limpa | sem_serie | 1 |
| Long | excluida | 7 |
| Long | incluida | 4 |
| Long | sem_serie | 5 |
| Var | incluida | 11 |
| Var | sem_serie | 18 |
| fora_dos_grupos | excluida | 11 |
| fora_dos_grupos | fora_dos_grupos | 38 |

## Estrelas incluídas, por grupo

| HD | Grupo | Série | Segmento Mount Wilson (anos) | Segmento Keck (anos) | Indicador (D100) | Confirmar |
|---|---|---|---|---|---|---|
| 10700 | Flat_limpa | Baum | 29 | 20 | sim |  |
| 23249 | Flat_limpa | Baum | 29 | 24 | sim |  |
| 182572 | Flat_limpa | Baum | 35 | 16 | sim |  |
| 190360 | Flat_limpa | Baum | 28 | 25 | sim |  |
| (Sun) | CYCLE_Excellent | Egeland2017_T4 |  |  | ver_P4_SOURCE_VALUES |  |
| 4628 | CYCLE_Excellent | Baum | 30 | 14 | sim |  |
| 10476 | CYCLE_Excellent | Baum | 36 | 24 | sim |  |
| 26965 | CYCLE_Excellent | Baum | 29 | 20 | sim |  |
| 103095 | CYCLE_Excellent | v2001 | 34 |  | sim |  |
| 152391 | CYCLE_Excellent | Baum | 36 | 11 | sim |  |
| 160346 | CYCLE_Excellent | v2001 | 36 |  | sim |  |
| 166620 | CYCLE_Excellent | Baum | 30 | 17 | sim |  |
| 201091 | CYCLE_Excellent | v2001 | 35 |  | sim |  |
| 3795 | Var | Baum | 29 | 9 | sim | sim |
| 22072 | Var | Baum | 18 | 10 | nao | sim |
| 39587 | Var | v2001 | 36 |  | sim | sim |
| 72905 | Var | Baum | 13 | 18 | nao | sim |
| 75332 | Var | v2001 | 36 |  | sim | sim |
| 101501 | Var | Baum | 28 | 9 | sim | sim |
| 115383 | Var | v2001 | 36 |  | sim | sim |
| 115617 | Var | Baum | 18 | 16 | nao | sim |
| 129333 | Var | v2001 | 14 |  | nao | sim |
| 217014 | Var | Baum | 30 | 14 | sim | sim |
| 131156A | Var | v2001 | 35 |  | sim | sim |
| 25998 | Long | v2001 | 36 |  | sim | sim |
| 35296 | Long | v2001 | 36 |  | sim | sim |
| 141004 | Long | Baum | 30 | 15 | sim | sim |
| 176095 | Long | v2001 | 36 |  | sim | sim |

## Fora da amostra e por quê

| HD | Grupo | Motivo |
|---|---|---|
| 43587 | Flat_limpa | sem_serie: sem serie em Baum nem em v2001 |
| 16160 | CYCLE_Excellent | sem_serie: sem serie em Baum nem em v2001 |
| 32147 | CYCLE_Excellent | sem_serie: sem serie em Baum nem em v2001 |
| 81809 | CYCLE_Excellent | excluida: R11 (D102): binaria composta/resolvida nos controles |
| 219834B | CYCLE_Excellent | sem_serie: sem serie em Baum nem em v2001 |
| 2454 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 3443 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 6920 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 12235 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 16673 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 22049 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 26923 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 30495 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 61421 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 88355 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 95735 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 97344 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 100563 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 106516 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 115043 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 155886 | Var | sem_serie: sem serie em Baum nem em v2001 |
| 165341B | Var | sem_serie: sem serie em Baum nem em v2001 |
| 137107AB | Var | sem_serie: sem serie em Baum nem em v2001 |
| 9562 | Long | excluida: D13: estrela-padrao de calibracao |
| 17925 | Long | sem_serie: sem serie em Baum nem em v2001 |
| 29645 | Long | excluida: D13: estrela-padrao de calibracao |
| 33608 | Long | sem_serie: sem serie em Baum nem em v2001 |
| 107213 | Long | excluida: D13: estrela-padrao de calibracao |
| 114378 | Long | sem_serie: sem serie em Baum nem em v2001 |
| 124850 | Long | sem_serie: sem serie em Baum nem em v2001 |
| 136202 | Long | excluida: D13: estrela-padrao de calibracao |
| 143761 | Long | excluida: D13: estrela-padrao de calibracao |
| 187013 | Long | excluida: D13: estrela-padrao de calibracao |
| 212754 | Long | excluida: D13: estrela-padrao de calibracao |
| 131156B | Long | sem_serie: sem serie em Baum nem em v2001 |

(As 49 estrelas do catálogo sem grupo definido em v5/v6 ficam no CSV com `status_amostra = fora_dos_grupos` ou `excluida`.)

## Pontos a confirmar na assinatura (não decididos por Claude)
1. **Var e Long entram como grupos de referência?** D102 não o diz; v5/v6 usam os quatro grupos (Flat, CYCLE+Excellent, Var, Long). Marcadas com `Confirmar = sim` na tabela. [ ] sim  [ ] não  [ ] só alguns
2. **HD 219834B** consta em Baum mas não tem linhas na Tabela 1: fica `sem_serie`. [ ] de acordo
3. **Sol:** entra por Egeland (Tabela 4, 1966–2016), série exploratória (R10); o critério de segmento de D100 não se aplica à série composta. [ ] de acordo
4. **O indicador temporal só roda nas estrelas com segmento Mount Wilson ≥ 24 anos** (coluna "Indicador"). [ ] de acordo

## Assinatura (REG-01)
Aprovo esta lista e o `p4_star_catalog.csv` e o `P4_SOURCE_VALUES.md` correspondentes como a consolidação do P4, e autorizo a etapa seguinte (reconstrução do pipeline em passada única, contra esta referência congelada).

Nome: ____________________   Data: ____/____/______   Assinatura: ____________________
