# Memorando de decisão: reestruturação do manuscrito P4 (2026-11-26)

Status: **RASCUNHO, seção 3 (poder bilateral) pendente.** Tudo abaixo é exploratório (D125): as análises foram decididas depois de ver os dados e das duas revisões, e não podem ser apresentadas como confirmatórias. Scripts em `pipeline_v2/explore/`, saídas em `pipeline_v2/results_explore/`. `run_all.py`, o notebook e os congelados não foram tocados.

## 1. Sensibilidade de σS de HD 166620 ao ruído instrumental f (feito)
Fonte: `results_explore/f_sensitivity.txt`. Estados: mín. 1 (1971–75, n=44), mín. 2 (1987–91, n=315), grande mínimo (2004–, n=103; f Keck = 0,3%).

| f (Mount Wilson) | σS mín. 1 | σS mín. 2 | σS grande | mín.1/grande | mín.2/grande |
|---|---|---|---|---|---|
| 1,2% (publicado) | 0,0027 | 0,0054 | 0,0019 | 1,38 | 2,78 |
| 1,4% | 0,0023 | 0,0053 | 0,0019 | 1,21 | 2,71 |
| 1,7% | 0,0016 | 0,0050 | 0,0019 | 0,81 | 2,57 |
| 1,9% | 0,0003 | 0,0048 | 0,0019 | 0,17 | 2,46 |

- A razão mín. 1/grande mínimo **inverte em f ≈ 1,58%**; a variância corrigida do mín. 1 some em f ≈ 1,93%. Os valores dos pareceres se confirmam.
- O mín. 2 não depende de f: a razão fica entre 2,4 e 2,9 em todo o intervalo (0,8–1,9%). Variar o f do Keck (0,1–0,6%) não muda a conclusão; com 1,0% a razão do mín. 2 sobe para 4,7–5,1.
- **Consequência:** só se pode afirmar que a variabilidade é menor no grande mínimo do que no mín. 2. O mín. 1 depende de uma suposição instrumental (f < ~1,5%) que as fontes não resolvem (1,2% vs 1,7–1,9%).

## 2. Robustez dos indicadores às escolhas de dados (feito, parcial)
Fonte: `robustness_data.txt`, `robustness_post.txt`. A variante base reproduz `star_results.csv` exatamente (960 células, |Δτ| = 0). Contagens são de **células brutas** com p < 0,05 (série S, 4 configurações × 4 janelas × 2 indicadores), não o critério de marcação da v1 (2 de 192); servem para comparar variantes, não para substituir aquele resultado.

| Variante | Segmentos | Células | p_upper < 0,05 | p_inferior < 0,05 | τ mediano AC1 / var |
|---|---|---|---|---|---|
| base | 24 | 960 | 1,5% | 5,5% | −0,04 / −0,22 |
| sem 1966–67 | 24 | 960 | 2,3% | 5,0% | −0,06 / −0,10 |
| ≥ 5 obs/ano | 20 | 800 | 1,3% | 4,0% | 0,00 / −0,09 (12 de 440 sinais invertidos) |
| sem 182572, 190360, 217014 | 21 | 840 | 1,1% | 3,7% | +0,02 / −0,16 |
| só HKP-2 (≥ 1977) | 14 | 560 | **5,9%** | 3,9% | +0,09 / −0,05 |

Leitura:
- **A era do instrumento pesa.** Restringindo a HKP-2 (14 estrelas com ≥ 24 anos), 176 de 560 células (31%) invertem o sinal de τ em relação ao base, e a correlação de τ entre as duas versões é baixa (AC1: 0,29; variância: 0,58). O τ mediano da autocorrelação passa de −0,13 para +0,09. Isso apoia o ponto 1 do Revisor 2 (a troca HKP-1 → HKP-2 cai no meio dos segmentos). **Ressalva:** a variante HKP-2 também encurta as séries (janelas e poder diferentes), então a mudança não é atribuível só ao degrau instrumental. Falta o teste de injeção de degrau em séries sintéticas.
- A taxa de células marcadas na cauda superior com HKP-2 (5,9%) é próxima do nominal, concentrada em 6 estrelas (131156A: 11 células, 176095: 6, 25998: 5, 39587: 5, 115383: 4, 182572: 2). Não é um sinal confirmado; as células não são independentes.
- Excluir 1966–67, exigir ≥ 5 obs/ano ou excluir os três segmentos interpolados não muda o quadro geral (sem excesso na cauda superior).
- Não feito: médias por estação, estágio evolutivo (Gaia), coluna "fonte" na tabela.

## 3. Poder bilateral e AUC (PENDENTE)
`pipeline_v2/explore/power_bilateral.py` foi reiniciado após a queda do contêiner (saída esperada em `results_explore/power_bilateral.txt`). Até lá, vale só a evidência da v1 com 200 séries (`results/positive_control.txt`): na perda de ciclo, a cauda inferior rejeita 14% (AC1) e 35,5% (variância), contra 1–2% na cauda superior. O erro de amostragem com 200 séries é ≈ 1,5–3 pp; **não afirmar poder bilateral antes de ver os resultados com 1000 séries.**

## 4. Eixos possíveis (o que cada um sustenta hoje)
**Eixo 1: calibração e poder do CSD em séries anuais de S (recomendado, condicionado à seção 3).** Pergunta: indicadores de CSD podem detectar perda de ciclo nestas séries? Centro: tamanho nominal do teste, controle positivo (Hopf), teste bilateral, AUC por período e amplitude, violação da separação de escalas (janelas ≈ 1 ciclo; passo ≈ 1/10 do ciclo), e a sensibilidade a degrau instrumental (seção 2). Sustentado: tamanho (3,2%, 4,2%), sinal oposto no controle positivo, varredura nula sem excesso, e agora a dependência da era instrumental. HD 166620 e a varredura entram como aplicações.

**Eixo 2: teste bilateral com nulo com ciclo explícito.** Só se justifica se um protótipo de nulo (senoide + AR(1) ou fase aleatória) elevar o poder; não foi testado (A4). Exige nova rodada estelar, só com seu pedido e arquivo da saída antiga.

**Eixo 3: dois artigos.** Artigo 2, curto, sobre σS de HD 166620 por estado. A seção 1 diz que o resultado só vale frente ao mín. 2, com n pequeno e dependente do instrumento; isso o enfraquece como artigo próprio, mas é um bom subresultado do Eixo 1.

## 5. Reaproveitamento da v1
- **Fica:** pipeline (`pipeline_v2/`), bibliografia de 36 itens, pacote de reprodução, controle positivo (a especificar: equação, ruídos, taxa de variação, cruzamento, janelas), poder com ciclo (refeito com ≥ 1000 séries).
- **Vira apêndice ou limite:** R′HK (τ não muda); comparação por grupos (variância normalizada é o próprio critério da classe Flat; AR(1) de séries Flat tem confundimento por razão sinal/ruído).
- **Reescrever:** título, resumo e Discussão (condensar; mover o design das simulações para Métodos com tabela-resumo); H1 reduzido a "só frente ao mín. 2", com a análise de f.
- **Corrigir/conferir:** DOIs de [9] e [14]; "tamanho medido 4,2%" implica ~8 células (não ~10) em 192; nome de `scale_sensitivity.py` para Data availability; método A no resumo.

## 6. Revista (decidir depois)
New Astronomy aceita o enquadramento metodológico; periódicos de métodos/análise de dados (por exemplo, Astronomy and Computing) ajustam melhor o escopo de um resultado nulo com calibração. Os dois pareceres veem o valor na calibração, não na astrofísica.

## 7. Decisões que dependem de você
1. Eixo (1, 2 ou 3) depois de ver a seção 3.
2. Autorizar A4 (protótipo de nulo com ciclo) e o teste de injeção de degrau.
3. Autorizar nova rodada estelar completa, se o Eixo 2 for escolhido.
4. Revista. 5. Pendências administrativas: afiliação, DOI do repositório, declaração de IA.
