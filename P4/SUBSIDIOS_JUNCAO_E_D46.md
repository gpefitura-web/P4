# Subsídios para decidir: (item 4) a junção instrumental 2001→2004 e (item 5) aceitar D46

**Pedido do pesquisador (2026-11-14):** "Subsídios para decidir." Este arquivo **não escolhe** e não recomenda. Fatos com id de checagem (`inspecao/checks.csv`) ou arquivo e seção.

---

## Item 4 — a junção instrumental (D44)

### O que a fonte fez (Baum+2022 §2.1; A9 §1.5)
- Sem transformação funcional, termo de cor ou escala: **apenas um deslocamento aditivo constante que alinha medianas**.
- HKP-1 → HKP-2: HD 22072, 23249, 217014 nomeadas (§2.1.1). MW → HIRES-1: HD 3795, 10145, 65583 nomeadas (§2.1.2). MW/HIRES-1 → HIRES-2: "Fourteen stars … in the same manner", **não nomeadas** (§2.1.3). HD 34411 e 142267 deliberadamente **não** corrigidas, por poder ser mudança real de atividade.
- **Não publicado:** o valor de cada offset, a incerteza, a identidade das 14, qualquer erro residual. As séries da Tabela 1 só têm valores corrigidos. Grau X (D44).

### O que se mede nos dados (`audit/a9_instrument_step.csv`, 51 estrelas com ≥ 10 pontos em HKP-2 e em HIRES-2; `3.5-01`, `3.5-21`)
| Medida | Valor | Id |
|---|---|---|
| degrau relativo HKP-2 → HIRES-2, σ entre estrelas (ddof = 1) | 4.47 % | `3.5-02`, `3.5-14` |
| mediana | 0.00 % | `3.5-04` |
| média | −0.61 % | `3.5-05` |
| \|degrau\| > 1.2 % (precisão de longo prazo de D14) | 25 de 51 | `3.5-06` |
| \|degrau\| > 5 % | 10 de 51 | `3.5-07` |
| HD 166620 | −8.78 % | `3.5-08` |
| HD 4628 (ainda cíclica, maior \|degrau\|) | −16.3 % | `3.5-09`, `3.5-10` |
| degrau exatamente 0 (medianas iguais a 4 casas) | 5 estrelas: 10697, 132142, 179957, 217014, 22072 | `3.5-19` |
| \|degrau\| < 0.2 % | 17 estrelas | `3.5-19b` |
| σ do degrau nas 34 restantes | 5.48 % | `3.5-19c` (grau C) |
| dispersão robusta (1.4826 × MAD) das 51 | 1.23 % | `3.5-22` (grau C) |

**Leitura que os números permitem (grau C):** a mediana 0.00 % e a σ de 4.47 % misturam estrelas cujo degrau é zero por construção (alinhamento de medianas, que Baum declara para 14) com estrelas não alinhadas. A coincidência de medianas não prova alinhamento: é inferência. A regra de filtragem que reproduz os números (remover pontos `sigma`) não estava escrita em A9 (`3.5-11`).

### O que isso implica para cada alternativa
| Alternativa | O que oferece | O que custa |
|---|---|---|
| **(a) Descontinuidade declarada** (regra operacional de D44) | Não inventa um offset; honesto com o grau X | Nenhuma janela atravessa a junção; cada série fica em duas metades, cada uma mais curta (HKP-2 termina em 2001.77; A9 §1.1) |
| **(b) Degrau estimado e removido** | Séries contínuas | O degrau de HD 166620 (−8.78 %) está na faixa de estrelas ainda cíclicas (HD 4628, −16.3 %), então o degrau sozinho não separa instrumento de astrofísica (A9-F6); incerteza residual grau X; Baum já fez deslocamentos em 14 estrelas não nomeadas, e uma segunda correção as sobrepõe |
| **(c) Um instrumento por estrela** | Sem junção | Série mais curta; exclui o HIRES pré-2004 e muda o N por estrela; para HD 101501 não há perda, porque o estado plano e o retorno estão dentro de Mount Wilson (D59; `3.3-50`) |

### Exceção já registrada
D45b: para **HD 166620** a calibração é robusta, por sobreposição temporal com os dados de Oláh e por fotometria APT independente (Luhn §3.1/§4). **Atenção (D58):** a sobreposição de Oláh de 1995–2002 é a parte digitalizada, grau C; a fotometria APT é independente dela e tem 12 estações em 1993–2004 (`3.4-19`).

### Fatos que independem da alternativa
- Das 59 estrelas de Baum, 8 ficam fora da estatística do degrau por terem < 10 pontos em um instrumento (`3.5-21`).
- Em HD 166620, as linhas de Mount Wilson de Luhn coincidem exatamente com as de Baum (diferença máxima 0; `3.4-06e`); "No offset of S_HK applied" por Luhn.
- Em HD 101501 a série é 99.73 % de Mount Wilson, com a lacuna de 13.82 anos antes do Keck (`3.3-50`, `3.3-52`).

---

## Item 5 — aceitar D46

### O que D46 diz
O teste temporal de CSD no formato de Dakos (janela deslizante de 50 %, τ de Kendall, surrogates ARMA) não é executável em HD 166620; a unidade de análise é a comparação de variabilidade entre estados, como em Luhn+2022 §3.1. Deve ser dito no manuscrito como limitação, não contornado (A10-F2).

### Os números
| Fato | Valor | Id |
|---|---|---|
| médias anuais de S_HK em 1995–2002 | 8 | `3.4-13` |
| observações brutas em 1995.0 ≤ t < 2002.0 | 132 | `3.4-14`; outras leituras de "1995–2002": 137 (anos civis, inclusive), 128 (sem HIRES), 119 (só `new_MW`) (`3.4-15`) |
| linhas `new_MW` (digitalizadas, 1995.447–2002.486) | 119 | `3.4-04`, `3.4-08`; D58 |
| maior lacuna em S_HK na série de Luhn | 2.82 anos (2005.64–2008.46) | `3.4-10`, `3.4-11` |
| lacuna de Baum antes dos dados de Oláh | 6.91 anos (1997.73–2004.64) | A13-F3; A10 §1.2 |
| anos de APT com dados | 17; 12 em 1993–2004; nenhum em 2005–2015 | `3.4-17` a `3.4-19` |

### O que depende de dado grau C (D58)
Dependem das 119 linhas digitalizadas: as 8 médias anuais de 1995–2002, a redução da lacuna de 6.91 para 2.82 anos e a frase "a aproximação à transição está amostrada". Não dependem: σ_S dos três estados, as médias de S_HK e o F-test de Luhn (A13-F3).

### O que as fontes de teoria dizem sobre séries curtas (A7)
- Scheffer+2009 (PDF pp. 5–6): "the detection of increased autocorrelation may require long time series"; resultados "depend on parameter choices in filtering"; exige um conjunto de procedimentos estatísticos (`3.11-31` a `3.11-33`; A7 §5).
- Boulton+2014: sinais significativos só após cerca de 550 anos de dados anuais, 250 antes do colapso, e médias decenais dão estatística pior por terem menos pontos (A7 §5, linha 14).
- Dakos+2012 (PDF p. 17): janelas de 25–75 % do registro e 1 000 surrogates ARMA (`3.11-41`). Com 8 pontos anuais, uma janela de 50 % tem 4 pontos (aritmética, não medida aqui).

### Alternativas e o que cada uma exige
| Alternativa | Exige no manuscrito |
|---|---|
| Aceitar e declarar | A limitação de D46, como em A10-F2; Methods com a comparação entre estados (receita de σ_S: item 7, ainda aberto, D70) |
| Aceitar com ressalva de grau C | O acima, mais a declaração de que as médias anuais de 1995–2002 vêm de dados digitalizados por Luhn a partir da Figura 2 de Oláh+2016 |
| Pedir os dados reais antes | Pedido a K. Oláh e W. Soon; até chegar, as 119 linhas ficam grau C e o item fica bloqueado |

Estado: **itens 4 e 5 com subsídios entregues; escolhas pendentes (D72, D73).**
