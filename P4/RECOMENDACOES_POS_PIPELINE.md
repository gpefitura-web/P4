# RECOMENDAÇÕES_POS_PIPELINE — verificação final e recomendações (2026-11-24)

Recomendações **não são decisões**: cada ponto abaixo é do pesquisador (regra 5 do CLAUDE.md). Nada aqui altera D## nem resultados.

## 1. Verificação feita
| Item | Resultado |
|---|---|
| Hashes da referência congelada (catálogo, SOURCE_VALUES, lista final, catálogo congelado, notebook antigo) | iguais aos de `APROVACAO_2026-11-24.md` no início, depois do `run_all.sh` e agora |
| Testes dos passos 1, 2, 3, 4, 6, 7 (`pipeline_v2/test_step*.py`) | todos ALL OK, reexecutados na verificação final |
| Passo 5 (autoteste dos surrogates) | não reexecutado (100 s; registro em `results/autotest_step5.txt`): 3.2 % e 4.2 %, faixa 3–7 % |
| Integridade de `star_results.csv` | 1 920 linhas, 24 segmentos × 80 linhas, 0 valores ausentes, p em [0.005, 1.0], motor statsmodels em todas |
| Contagem de segmentos | 24 rodados (23 estrelas + Sol); 4 estrelas descritas sem τ (segmento < 24 anos) |
| Precisão | 23 segmentos em 24–39 anos ("baixa", exploratórios); só o Sol (51 anos) é "adequada" |
| Execução oficial | uma só, semente 20261124; nada ajustado depois |

**Duas observações de fato que pedem atenção ao ler os resultados:**
- Na janela de 50 % (série S), só 2 de 192 combinações estrela × tendência × indicador têm p_upper < 0.05 (HD 23249 AR(1) sem remoção, τ = 0.75, p = 0.032; HD 217014 AR(1) σ = 1, τ = 0.18, p = 0.026); nenhuma tem concordância ≥ 3 de 4. Sob hipótese nula calibrada esperariam-se cerca de 10 (as células não são independentes). Junto com o autoteste (3.2 % no limite inferior), indica um teste conservador, coerente com o poder baixo já declarado em D100.
- A variância normalizada de CYCLE_Excellent supera a de Flat (p = 0.008 sem remoção, p = 0.002 com σ = 1), o que é o que a amplitude do ciclo produziria sem qualquer CSD (confundidor de Q4/D30).

## 2. Recomendações
**R-A — Cauda do p (ACHADOS #4).** Adotar `p_upper = P(τ* ≥ τ)` como p do texto (τ crescente é a direção de CSD) e registrar uma D## que diga que D22, ao escrever P(τ* ≤ τ), usa a convenção de sinal oposta; manter `p_D22` no material suplementar. Os dois passaram no autoteste. Custo: nenhum, tudo já está calculado.

**R-B — Testes entre grupos (ACHADOS #7).** Tratar `REPORT.md` §6 como exploratório, com n = 4 a 8 por grupo. Se o texto os citar: (i) fixar **antes** de olhar um par primário (a hipótese do notebook antigo, "irregular > Flat" em φ₁, traduz-se como Var ∪ Long contra Flat, AR(1) com σ = 1); (ii) aplicar Holm aos demais pares; (iii) declarar que o AR(1) de uma série inteira depois de σ = 1 sai negativo por construção (mediana ≈ −0.3) e não é comparável ao AR(1) em janela; (iv) nomear a variância de ciclo como confundidor (Q4). Alternativa mais enxuta: omitir os testes entre grupos do manuscrito e manter só H1 e H2, que são o que D90 declara.

**R-C — Poder (D100).** Manter a frase de Methods que já existe (poder baixo; "não suportado" ≠ refutação) e acrescentar o número observado: autoteste 3.2 % de rejeição e 2 de 192 p < 0.05. Não reabrir o piso de 24 anos nem a grade ARMA.

**R-D — Sol.** Manter exploratório. É o único segmento "adequado" (51 anos); o resultado dele não deve ser lido como confirmação do grupo.

**R-E — 1day/sigma.** Resolvido em D106. Se quiser a regra só para HD 190360, é preciso reexecutar (HD 217014 mudaria de 30 para 29 anos, sem efeito de elegibilidade).

## 3. Ordem sugerida para a próxima conversa
1. Registrar as respostas a R-A e R-B como D107 e D108 (decisões suas).
2. Só depois, figuras e manuscrito, em conversa nova, com `REPORT.md` e `P4_SOURCE_VALUES.md` como únicas fontes de número.
