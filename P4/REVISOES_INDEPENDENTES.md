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
