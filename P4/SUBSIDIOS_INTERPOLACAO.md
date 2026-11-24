# Interpolar anos faltantes: teste, justificativa física e referências

**Pedido do pesquisador (2026-11-24):** "Testar com interpolação e sem. Obter justificativa física para isto, juntamente com referências na área que já fizeram isto." Este arquivo **não escolhe**. O que vem de fonte tem página; o que é raciocínio meu está marcado (grau C).

## 1. O teste (sintético, sobre as lacunas reais)
**Desenho** (`inspecao/scripts/15_gap_interpolation_test.py`; saída `inspecao/saidas/15_gap_interpolation_test.txt`; `3.17-01` a `3.17-03`): processo AR(1) estacionário com coeficiente c conhecido, amostrado nos anos que as 10 estrelas dos grupos do P4 de fato têm (só a **presença** de cada ano é usada; **nenhum valor de S**, então D04 e D11 não são tocados). Métodos: *oracle* (sem lacunas), *naive* (ignora as lacunas, junta os anos vizinhos), *pairs* (só pares de anos consecutivos), *lin_short* (interpola linearmente lacunas de 1–2 anos e deixa as longas vazias), *lin_all* (interpola todas). Sementes fixas; 400 simulações por célula (viés) e 150 (janela de 50 % e τ de Kendall).
**Limites do teste:** AR(1) estacionário, sem ciclo de 10 anos, sem ruído de medida, sem remoção de tendência (D21); mede o tratamento das lacunas, não as estrelas.

| Resultado (mediana sobre as 10 estrelas) | oracle | naive | pairs | lin_short | lin_all |
|---|---|---|---|---|---|
| Viés do AR(1) da série inteira, c = 0.3 | −0.037 | −0.063 | −0.047 | −0.001 | +0.053 |
| idem, c = 0.5 | −0.047 | −0.079 | −0.054 | −0.020 | +0.013 |
| idem, c = 0.7 | −0.065 | −0.098 | −0.079 | −0.053 | −0.021 |
| τ de Kendall médio do AR(1) em janela, **nulo** (c = 0.5 constante) | +0.02 | **−0.14** | −0.03 | +0.00 | **+0.18** |
| τ médio, **tendência** (c de 0.3 a 0.7) | +0.28 | +0.17 | +0.22 | +0.27 | **+0.39** |

**O que o teste mostra** (fatos da simulação): (a) ignorar as lacunas (*naive*) subestima o AR(1) e inventa tendência **negativa**; (b) interpolar **todas** as lacunas (*lin_all*) cria tendência **positiva** sob hipótese nula (τ médio +0.18) e infla a tendência real (+0.39 contra +0.28); (c) interpolar só as curtas (*lin_short*) fica o mais perto do *oracle* na mediana (viés e τ); (d) mesmo o *oracle* tem viés negativo de amostra finita (−0.04 a −0.07), de modo que parte do bom resultado de *lin_short* é compensação entre dois erros de sinal contrário; (e) **nas estrelas de lacuna longa nenhum método recupera o *oracle***: HD 101501 (lacuna de 13 anos) tem τ nulo −0.36 (*naive*), −0.26 (*pairs*), −0.02 (*lin_short*) e +0.26 (*lin_all*); HD 166620 (6 anos): −0.16, −0.03, +0.16, +0.29; HD 4628 (10 anos): −0.16, −0.09, −0.07, +0.19. A mesma máscara aplicada a séries reais **não** foi feita.

## 2. Justificativa física (o que se pode sustentar)
1. **O AR(1) é um modelo de memória: c = exp(−κΔt)** (Held & Kleinen p. 2; Livina & Lenton p. 2; A7b item 3). Preencher um ano faltante por interpolação só é neutro se a memória do indicador ao longo da lacuna for alta, isto é, se **1/κ ≫ tamanho da lacuna**. Para uma estrela esse tempo de memória **não é conhecido** em nenhuma fonte auditada (A7b-F2; Q10). *Raciocínio (C):* para lacunas de 1–2 anos a interpolação é plausível se o índice varia suavemente na escala do ciclo (anos); para lacunas de 6–13 anos não o é.
2. **A interpolação suaviza e aumenta a autocorrelação:** "linear interpolation may impose artificially smooth dynamics, obscuring true variability" (Liu et al., manuscrito arXiv, pp. 7–8; `3.11-78`); a interpolação padrão reduz a variância de alta frequência (Rehfeld et al. 2011, p. 2) e "persistence time (memory) is strongly overestimated when using the standard, interpolation-based, approach" (p. 1; `3.11-79`). **É o mesmo sentido do sinal de CSD** (AR(1) crescente), o que concorda com o *lin_all* do teste.
3. **Uma lacuna afeta o AR(1) mais que a variância:** "a single missing value removes two consecutive data points from the AC1 calculation, whereas only one data point is excluded from the variance estimate" (Liu et al. p. 4; `3.11-77`); a concordância entre os indicadores de CSD piora com a fração de valores faltantes.
4. **Variabilidade estelar em escalas curtas:** o dado anual é uma média de muitas observações por temporada, três por noite desde ~1980 (README do HK Project, p. 1; `3.11-76`), logo o ruído de rotação e de regiões ativas já foi promediado; a interpolação age sobre o valor anual, não sobre o ruído (*raciocínio, C*).

## 3. Quem já fez isto
**No campo da atividade estelar e solar** (interpolação para análise espectral ou reescalonamento, **não** para indicadores de CSD):
- Oláh et al. 2016, sobre os dados de Mount Wilson: "The data were binned (and if necessary, interpolated) to 30 days" (p. 2; `3.11-82`) e, na Figura 2, "the datasets and spline interpolation we used are plotted" (p. 5; `3.11-83`), para a análise tempo-frequência.
- Egeland et al. 2017: reescala a região de dados perdidos de modo que sua mediana caia "on a linear interpolation of the cycle across the region" (p. 5; `3.11-84`); a conclusão não depende de manter ou remover a região.
- Nenhuma das fontes estelares lidas (Baum, CLS V, CLS VI, Luhn, Baliunas, Lockwood) usa a palavra "interpolat-" (verificado por busca de texto).
**No campo de CSD e de séries irregulares:**
- Dakos et al. 2012: a interpolação é "necessary only when there are too many missing values", e os métodos servem a séries irregulares (A4, Tabela 3, nota 1; p. 14).
- Liu et al. (dados faltantes e *outliers*): documenta o viés acima e diz que métodos tradicionais de preenchimento, incluindo a interpolação linear, "can introduce systematic biases in the higher-order statistics … even if the mean is unbiased" (pp. 7–8).
- Rehfeld et al. 2011: compara interpolação linear, Lomb–Scargle e **núcleo gaussiano**; em séries muito irregulares o erro do lag-1 é 40 % menor com o núcleo gaussiano que com interpolação linear (p. 1; resumo); "it is controversial if, when and how missing observations can be appropriately approximated" (p. 2; `3.11-80`).
- Estudo de eventos de Dansgaard–Oeschger (ESD 2025): "To circumvent potential interpolation effects, we further conduct a similar study on the raw NGRIP record applying an approach adapted specifically for the analysis of irregularly sampled time series" (p. 4; `3.11-81`).
- Braun et al. 2022 (*Phys. Rev. E* 105, 024206; manuscrito arXiv:2112.04843) trata de análise com correção da taxa de amostragem em séries irregulares; **baixado, não lido**.

## 4. Alternativas atualizadas (nenhuma recomendada)
| Alternativa | O que o teste e as fontes dizem |
|---|---|
| 1. Sem interpolar; janelas só em sequências contínuas de anos | evita o viés; 2 das 10 estrelas ficam sem janela de 50 % (`3.16-05`) |
| 2. Interpolar só lacunas de 1–2 anos, marcando os pontos; não atravessar as longas | mais perto do *oracle* na mediana (teste), com a ressalva de compensação (d) e de que Liu e Rehfeld advertem contra a interpolação linear; os *surrogates* (D22) devem passar pela mesma interpolação |
| 3. AR(1) só com pares de anos consecutivos | viés um pouco pior que o *oracle*, sem tendência espúria na mediana (τ nulo −0.03); descarta pares |
| 4. **Estimador para amostragem irregular, sem interpolar** (núcleo gaussiano, Rehfeld 2011; ou abordagem de série irregular, ESD 2025) | tem precedente publicado em CSD e é a alternativa que as fontes recomendam contra a interpolação; **não foi testado aqui** |
| 5. Série bruta em janelas de tempo | fora de D92; tripletos noturnos (D91) |

**O que não se pode afirmar:** que a interpolação seja fisicamente justificada para estrelas (o tempo de memória é desconhecido); que algum método recupere o resultado correto nas estrelas de lacuna longa (o teste diz que não).

Estado: **teste, justificativa e referências entregues; regra para anos faltantes pendente (D96).**
