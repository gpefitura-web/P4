# Revisões independentes do manuscrito e das figuras (2026-11-25)

Seis revisores independentes (agentes sem contexto prévio, só leitura): três para as figuras (layout, cor e acessibilidade, correção científica) e três para o texto (checagem de afirmações contra os dados e as fontes, linguagem e estilo, parecerista estatístico). As saídas dos revisores são pareceres do modelo, não decisões; abaixo, o que foi aplicado e o que ficou fora.

## Figuras
| Achado | Destino |
|---|---|
| Legenda sobre os dados, rótulos cortados, fontes pequenas, ticks apertados (Fig. 2); legenda distante e rótulo longo (Fig. 3) | Aplicado: legenda única acima, rótulos curtos, escala de anos comum (largura proporcional ao comprimento), ticks de 10 em 10 anos |
| Azul tinha dois sentidos (Fig. 1 contra Figs. 2–3) | Aplicado: azul = série original e laranja = resíduo/suave com σ = 1 ano em todas; na Fig. 1, método A em preto e B em verde-água (só nessa figura) |
| Laranja tracejado fraco; asteriscos ambíguos e com glifo diferente na legenda | Aplicado: traço mais grosso e acima; asterisco como o mesmo marcador na legenda e no gráfico, sobre o próprio marcador (deslocamento horizontal por configuração) |
| Legendas sem definições (método A/B, janela, caso do Sol, cauda do p, nº de testes, ordem das estrelas) | Aplicado em todas as legendas |
| Rótulo "2004-" truncado | Aplicado: "2004 on" |
| Incertezas na Fig. 1 | Não aplicado: sem incerteza definida para σ; dito na legenda |
| Texto alternativo (alt text) | Pendente: depende da revista |

## Texto
| Achado | Destino |
|---|---|
| "Baixo poder" sem número; só havia teste de tamanho | Aplicado: AUC de simulação anterior (0.59, 0.60, 0.63 para 24, 30, 40 anos) em Métodos, Resultados e Discussão; afirmação de poder com ciclo ficou como limitação, sem número |
| Hipótese H2 não era testável (registro de HD 166620 termina antes da transição) | Aplicado: resumo, Discussão e Conclusões dizem isso; as outras 23 séries são varredura nula |
| Diferenças de grupo "refletem a amplitude do ciclo" | Aplicado: "atribuímos", interpretação não testada; ambas as famílias de Holm relatadas e a mudança de família declarada |
| F-test com observações correlacionadas (p = 1e-26) | Aplicado: p com um algarismo, mínimo 2 como "< 10^-3", ressalvas (ruído fixo, instrumento diferente no grande mínimo); H1 descritivo; reconhecido como re-análise de valores já publicados |
| "Nenhum segmento cruza a junção" | Aplicado: restrito à passagem Mount Wilson–Keck; troca HKP-1/HKP-2 e composição do Sol declaradas |
| Tabela sem marcas de B−V fora da faixa e do Sol composto | Aplicado (notas a e b) |
| R′_HK: p diferem entre as duas execuções | Aplicado: relatado (até 0.39; 3 contra 2 células) como medida de instabilidade do ajuste ARMA |
| Premissa de sinal (CSD em perda de ciclo limite sem previsão) estava nos Limites | Aplicado: movida para a Introdução |
| Siglas, termos (série original, resíduo σ = 1, método A/B), minuses, ortografia | Aplicado (ortografia americana); ligaturas do PDF corrigidas com fonte Type 1 |
| Métodos incompletos (média anual, borda do filtro, motor ARMA, τ, p +1, janelas, "mais longo", fonte do ruído, log pré/pós) | Aplicado, com subseção "Analysis log" |
| Números digitados à mão | Parcial: constantes de projeto em `results_extra.tex` com a origem de cada uma; resto vem de `results_macros.tex` |
| Cobertura de modos de falha: poder com ciclo, sensibilidade à interpolação, taxa nula da regra 3 de 4, bootstrap em blocos para H1, curva de poder | Não feito: análise nova, fora do escopo; listado como limitação e próximo passo |
| Título promete mais do que a análise entrega ("varredura nula") | **Decisão sua**: título mantido; sugestões abaixo |

## Sugestões de título (sua decisão)
1. "A null scan for critical slowing down in Mount Wilson S-index series"
2. "Looking for critical slowing down before the loss of a stellar activity cycle: a null result from Mount Wilson series"

## Rodada de revisão de leitura (2026-11-25, formato New Astronomy)
Um revisor independente leu o PDF compilado de ponta a ponta. Aplicado: títulos de parágrafo sem ponto duplo, "23 segmentos" (e não 24) na Discussão, conclusão 2 sem a afirmação "só detectaria tendência forte" (o texto agora diz "pouco poder contra a elevação modesta simulada"), tabelas dos artigos citados escritas como "their Table N" para não colidir com as tabelas deste, hipótese H2 igual na Introdução e nos Métodos, 30 testes de Holm explicados (5 pares × 6 blocos), variância normalizada definida, AIC, AC e HD definidos, F-test do método B descrito, linha do Sol rotulada "Sun", legenda da Tabela 2, abstract com "grand minimum" e "Holm multiple-test correction", ortografia americana ("catalog"). Verificado por mim: o p do F-test bruto (F = 2.95, 43 e 102 graus de liberdade, p bilateral 8.8e-6) reproduz o valor publicado. Não aplicado: DOI de Noyes et al. (não há DOI nos arquivos do projeto; completar do ADS).
Título provisório em uso (v2): "Testing early-warning indicators of critical slowing down in Mount Wilson S-index series of Sun-like stars"; alternativas em `SUGESTOES_TITULO.md`.

## Segunda rodada (2026-11-26, D120): dois pareceres simulados (séries temporais; atividade estelar)
Cada ponto foi conferido contra os dados e o texto antes de decidir.

**Corrigido no texto:**
- R1-M1 (p dos surrogates entre S e R'HK): **procede, e é mais grave do que o parecer supõe.** A ordem do ARMA difere entre S e R'HK em 77 de 96 pares segmento-configuração e, dentro de S, padronizar o resíduo muda a ordem em 33 de 92 casos (`scale_sensitivity.py`). Com a mesma ordem, os p diferem no máximo 0,12; com ordens diferentes, até 0,49 (todas as cinco janelas; 0,39 na janela de 50 %). Logo o texto não podia atribuir a diferença à "instabilidade do ajuste em séries curtas". Reescrito; a correção do pipeline é decisão do pesquisador (ver `paper_state_v10.md`, seção 3).
- R1-m5 (esperado por acaso): procede; com o tamanho medido (3,2 %) são cerca de 6, não 10. Texto traz os dois.
- R1-M5 (premissa de CSD): parcialmente. O projeto já havia lido Kuehn 2011 e 2013, Boettiger 2013 e Bury 2020 (D88–D89) e nenhuma trata ciclo → equilíbrio, mas a introdução dizia só "não conhecemos" sem citar. Agora cita as três fontes. Wiesenfeld e outras do parecer não estão no projeto e não foram acrescentadas.
- R2-M5 (média × σ em HD 166620): procede. Média do grande mínimo 1,1 % abaixo da do mínimo 2; σ_S cai por fator 2,8. Frase acrescentada à Discussão. A observação sobre a "declividade do ciclo" no mínimo 2 não está sustentada no pacote e não foi usada.
- R2-m1 (definir S index): procede; definição na introdução (sem página citada).

**Já tratado no texto, sem mudança:** R1-m4 (H1 já é dito "re-test, not blind"); R2-M3 (o resumo já diz que o registro termina antes da transição); R2-M6 (a atribuição à amplitude já é declarada como não testada); R1-M6 (o texto já diz que os p do teste F não são interpretáveis); R1-M4 em parte (o texto já diz que o resíduo é passa-alta).

**Não reabertos (decisões já tomadas):** R1-m1 (família do Holm: D108 e D109); R1-m2 e m3 (escolhas de apresentação, D110).

**Procedem mas são análise nova (decisão do pesquisador; ver lista em `paper_state_v10.md`):** R1-M2, M3, M7; R2-M1, M2, M4, M6; R2-m3 e m4 (figuras). Sobre R1-M7: os surrogates recebem as mesmas posições de lacuna e a mesma interpolação dos dados, o que mitiga parte do viés citado, mas não foi medido.

**Não aplicados:** referências novas (R2-m2) sem PDF lido; numeração de linhas (R2-m5) até a revista pedir.

