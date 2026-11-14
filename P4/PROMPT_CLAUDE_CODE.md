# Prompt de inspeção para o Claude Code

Cole o texto abaixo (tudo dentro do bloco) numa sessão do Claude Code aberta na pasta `P4/` já extraída do zip.

```
Estamos retomando o Paper P4 ("Critical Slowing Down Near Stellar Activity Minima"). Esta pasta contém todos os arquivos de estado do projeto. Sua tarefa agora é uma INSPEÇÃO completa, só de leitura e verificação. Não é uma tarefa de desenvolvimento.

Antes de qualquer coisa, leia nesta ordem: CLAUDE.md, README_HANDOFF.md, paper_state_v6.md, DECISOES_D41_D54.md, P4_RESEARCH_NOTEBOOK.md, P4_AUDIT_PROTOCOL.md. Depois abra o que precisar de audit/, data/ e dos CSVs da raiz.

REGRAS DA INSPEÇÃO
- Você só escreve dentro de uma pasta nova, inspecao/. Não edite nenhum arquivo existente, nem o pipeline (p4_pipeline.ipynb, congelado), nem as auditorias, nem os CSVs, nem o caderno.
- Não decida nenhuma questão Q# aberta e não reabra nenhuma questão fechada (§8 do caderno). Se achar que algo fechado deveria reabrir, escreva isso como achado com a evidência e pare aí.
- Nenhum valor astronômico vem da sua memória. Todo número que você citar ou conferir tem de apontar para um arquivo deste diretório (arquivo e seção, ou arquivo e comando).
- Contradições entre documentos entram no relatório com as duas versões lado a lado. Não escolha uma em silêncio.
- Cada achado leva um grau de evidência (A, B, C ou X, como no protocolo) e uma gravidade: BLOQUEANTE (invalida um valor ou uma decisão), IMPORTANTE (inconsistência que afeta o manuscrito), MENOR (cosmético ou de organização).
- Código e comentários em inglês. Rode Python com `python -I` quando ele ler arquivos de data/. Scripts ficam em inspecao/scripts/. O relatório é em português.

ETAPA 1 — Inventário e integridade
Liste o que existe e o que os documentos citam e não está no pacote. Já sabemos que faltam P4_DECISION_SUPPORT_6.1.md, COWORK_PROMPT_A9_A12.md, P4_SOURCE_VALUES.md e p4_star_catalog.csv (os dois últimos ainda nem foram gerados), as auditorias A7 e A8 e os PDFs de bib/. Confirme essa lista, procure outras referências quebradas (arquivos, seções, números de achado A#-F#, decisões D##, questões Q#) e diga quais ausências bloqueiam alguma verificação abaixo. Os TSVs do VizieR estão em data/ com "_" no lugar de ":" no nome; faça a correspondência pela tabela do README_HANDOFF.md.

ETAPA 2 — Consistência entre documentos
Verifique, documento contra documento:
a) Toda decisão D01–D54 aparece uma única vez, com status, e toda referência a D## aponta para uma decisão que existe. DECISOES_D41_D54.md traz uma "instrução de incorporação" ao caderno que ainda não foi aplicada: confirme o que falta (D41–D54, Q10 e Q11, novas linhas da §8 e do log) e escreva a versão incorporada em inspecao/NOTEBOOK_proposta_D41_D54.md, sem tocar no original.
b) A lista de questões abertas Q1–Q11 é a mesma em paper_state_v6.md, no caderno e em DECISOES_D41_D54.md (§C). Aponte diferenças de estado.
c) As contagens que o estado v6 e as auditorias repetem (59 estrelas, 62 135 observações, 26 em comum com Baliunas, 14 reclassificadas, 14 períodos de Baum, 112 linhas do catálogo, 52/31/29, 82/17/6/2/5 na faixa de validade de Noyes, 48 estrelas do arquivo isaacson2024) batem entre si e com os arquivos de dados.
d) Há inconsistências já suspeitas para você olhar: (i) A9-F1 cita HD 4628 duas vezes ao contar os períodos estimados a olho; (ii) o caderno ainda descreve a amostra em termos de A1–A6 e não menciona Baum/Luhn nas obrigações de Methods; (iii) A10 §6 menciona bib/aa28479-16.pdf (Oláh+2016), que não está no pacote nem na raiz do repositório clonado, confirme onde ele deveria estar; (iv) as auditorias A1–A4 vieram do Project e A5, A6, A9–A12 do repositório GitHub, então confira que as tabelas de auditoria de cada uma (log de unidades, contagem de achados F#) não se contradizem entre si. Registre também qualquer outra que encontrar.
e) O que o v6 diz estar "congelado" ou "decidido" bate com o que o caderno registra.

ETAPA 3 — Reprodução numérica contra os dados (o centro da inspeção)
Escreva scripts reproduzíveis em inspecao/scripts/ e guarde as saídas em inspecao/checks.csv (colunas: id, descrição, valor esperado, valor obtido, fonte do esperado, resultado). No mínimo:
1. baliunas_table2_full.csv: 112 linhas; contagem por classe reproduz 52 ciclos, 31 (Flat 11 + Flat? 4 + Long 16) e 29 Var; nenhuma linha em grau C ou X; confirme os defeitos de catálogo registrados em paper_state_v4 §2 (HD 219834A sem período, HD 76572 sem período, as seis CYCLE sem FAP, resíduos de OCR na coluna secondary).
2. Tabela 1 de Baum (data/J_AJ_163_183_table1.tsv): 62 135 linhas, 59 estrelas, 1966.18–2020.19; contagem por instrumento (HKP-1 2 207, HKP-2 50 223, HIRES-1 1 772, HIRES-2 7 933); flags (none 58 880, 1day 2 782, sigma 444, 1day/sigma 29); soma de Nobs da Tabela 2 igual à contagem da Tabela 1 estrela a estrela.
3. N por estrela: mediana de observações 698, mediana de estações anuais 27, 56 de 59 acima de 100 observações, 0 de 59 acima de 100 estações; maior lacuna interna mediana 7.17 anos, 42 de 59 com lacuna maior que 5 anos. Compare com baum2022_59stars.csv.
4. Luhn+2022 (data/J_ApJ_936_L23_table2.tsv): 1 885 linhas; contagens de HD 166620 por instrumento 107 / 1 547 / 9 / 103; reproduza σ_S dos três estados com a receita de D45 (quadratura com 1.2 % para Mount Wilson e 0.3 % para Keck, F-test) e compare com 0.0027, 0.0054 e 0.0019 e com ⟨S_HK⟩ 0.1810, 0.1724, 0.1705. Se não reproduzir, diga exatamente onde diverge. Não ajuste a receita para forçar o resultado.
5. Degrau instrumental (audit/a9_instrument_step.csv): 51 estrelas, σ ≈ 4.47 %, 25 de 51 acima de 1.2 %, 10 de 51 acima de 5 %, HD 166620 em −8.78 %, HD 4628 em −16.3 %. Recalcule a partir da Tabela 1 de Baum e compare.
6. Isaacson+2024 (data/J_ApJS_274_35_table2.tsv e table4): 710 estrelas, 138 ciclos, e o critério que gera as 48 estrelas de isaacson2024_least_active_50.csv. Reproduza o filtro e diga se o número é 48 ou outro.
7. noyes1984_validade_cor.csv: 112 linhas, distribuição 82 dentro de 0.44–0.82, 17 em 0.82–1.0, 6 acima de 1.0, 2 acima de 1.2, 5 abaixo de 0.44. Recalcule a partir do B−V de baliunas_table2_full.csv e aplique as fórmulas de D52 para pelo menos HD 10700, HD 32147 e HD 201091 (mostre o cálculo, sem inventar B−V).
8. Cruzamentos: 27 estrelas de Baum no catálogo A1 por HD contra 26 declaradas por Baum (HD 185144 é a diferença, A9-F2); os 14 períodos de baum2022_cycle_periods.csv e os Δ/σ da tabela de A9-F3; audit/saar_baliunas_crossmatch.csv (70 linhas) contra A6.
9. Grupos do P4: reconstrua os cinco Flat limpos e os treze CYCLE+Excellent citados em A9 §2.1 a partir dos CSVs e confirme quais estão em Baum (4 de 5 e 6 de 13). Reproduza as medianas de B−V por grupo do paper_state_v5 §4 (0,88 / 0,73 / 0,61 / 0,49) e diga se dependem de como o grupo é definido.
10. Para cada checagem que falhar, diga se a falha está no dado, no texto da auditoria ou na sua reprodução, e mostre o diff.

ETAPA 4 — Pipeline contra as decisões (somente leitura)
Leia p4_pipeline.ipynb célula por célula e compare com D08, D20–D27 e D29. Liste, com número da célula, tudo o que ainda contradiz uma decisão ativa: p-valores de Kendall do scipy no lugar de surrogates ARMA (D22), janela e faixa de sensibilidade (D20), bandwidth em anos e não em percentual (Q3), n_max = N//4 e falta de checagem de crossover (D26), uso de H = (β+1)/2 (D28), nolds (D29), catálogo e grupos antigos (D01, D07, D13), constantes solares (D16, D17). Diga também o que o notebook já faz certo. Não corrija nada: o resultado é um mapa para o desenvolvimento que virá depois da consolidação.

ETAPA 5 — Bloqueios e decisões humanas
Monte uma tabela única com: (i) itens grau X e C em aberto, com a unidade de origem; (ii) bloqueios de rede ou de dados (tabela 4 de Egeland, Dataverse, série NSO); (iii) as decisões humanas da §E de DECISOES_D41_D54.md, na ordem de dependência, indicando para cada uma quais verificações da etapa 3 são relevantes para quem vai decidir. Não recomende além do que já está registrado; se a sua reprodução numérica mudar o balanço de alguma recomendação já registrada (por exemplo a de não migrar para R′_HK, ou a de usar HD 101501), diga isso explicitamente como achado.

ENTREGÁVEIS (tudo em inspecao/)
- RELATORIO_INSPECAO.md: resumo de uma página no topo (quantas checagens passaram, quantas falharam, os BLOQUEANTES), depois achados numerados I-01, I-02… com gravidade, grau, evidência (arquivo e seção ou comando) e o que precisa ser decidido ou corrigido e por quem. Nada de narrativa sobre o que você fez; só o que foi encontrado.
- checks.csv e scripts/
- NOTEBOOK_proposta_D41_D54.md
- MAPA_PIPELINE.md (etapa 4)

Se algo travar (arquivo ilegível, dado ausente, ambiguidade que muda o resultado), registre como achado grau X e continue com as demais etapas. Ao terminar, mostre só o resumo de uma página e a lista de arquivos criados.
```
