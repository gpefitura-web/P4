# Subsídios para definir os papéis da série anual e da série bruta (D68, D76)

**Pedido do pesquisador (2026-11-14):** "Definir depois dos subsídios." Este arquivo **não escolhe** a distribuição e não recomenda nenhuma. Reúne, por métrica, o que a fonte exige, o que cada série dá e o que custa. Fatos com id (`inspecao/checks.csv`) ou decisão/auditoria.

## 1. O que cada série é nos dados

| Característica | Série anual (médias por estação) | Série bruta (observações) |
|---|---|---|
| Subconjunto Baum, mediana por estrela | **27** estações anuais (`3.3-05`) | **698** observações (`3.3-01`) |
| Baseline por estrela (mín./mediana/máx.) | 24 / 41 / 54 anos (`3.3-12`) | o mesmo |
| Maior lacuna interna, mediana | 7.17 anos (`3.3-09`) | a mesma; a lacuna não depende da escolha |
| Catálogo Baliunas congelado | N ≈ 26 médias anuais por estrela (D08, D12) | não existe (A2-F1: Lockwood não estende a série) |
| Solar (Egeland, Tabela 4) | 49 anos com dados em 1966–2016 (`3.12-09`) | 6 349 linhas; mediana de 152 por ano (`3.12-09`) |
| HD 166620, aproximação à transição | **8** médias anuais em 1995–2002 (`3.4-13`), dependentes de 119 linhas grau C (D58) | 132 observações em 1995.0 ≤ t < 2002.0 (`3.4-14`) |
| Instrumentos | junção HKP-2 → HIRES-2 (D44; ver `SUBSIDIOS_JUNCAO_E_D46.md`) | a mesma junção |

## 2. Por métrica

| Métrica | O que a fonte exige | Anual | Bruta |
|---|---|---|---|
| **DFA** | D24: piso de > 100 pontos; D26: n_max reduzido de N/4 e checagem de crossover; D25: α na convenção crua de Peng (A5) | N ≈ 27 ainda fica abaixo do piso (fator ~4 contra o piso, D24) | ≈ 698 acima do piso; **reabre Q9 e D24** para este subconjunto; a amostragem é irregular e a DFA de Peng supõe série igualmente espaçada (pergunta a registrar; não verificada em A5) |
| **AR(1), variância, τ de Kendall em janelas (CSD, Dakos)** | D20: janela de 50 % do comprimento, sensibilidade 25–75 %; D21: suavização gaussiana só nestas trilhas; D22: 1 000 surrogates ARMA por AIC (A4); A4 Tabela 3 nota 1: os métodos servem a séries irregulares, com interpolação "only when there are too many missing values" | janela de 50 % de 27 pontos = 13 a 14 pontos; para HD 166620 a aproximação tem 8 pontos (D46) | janela em tempo, muitos pontos por janela; lacunas de mediana 7.17 anos exigem decidir como tratá-las (interpolar ou deixar a janela sem dado) |
| **σ por estado (Luhn §3.1)** | D45 e D57: a conta publicada usa o intervalo inteiro, em observações; subtração do ruído em quadratura (D70: receita ainda aberta) | a variante "por estação" (conta B) usa médias de σ por estação | a conta A usa observações brutas (`3.4-25`, `3.4-32`, `3.4-39`) |
| **Ciclo e média de ciclo** | D08: ⟨S⟩ é a média anual sobre todos os anos; D19: estabilidade da média do ciclo e declínio da amplitude reportados separadamente; períodos de B95 e Baum são de periodogramas (D15, D42) | natural para ⟨S⟩ e amplitude (D08, D19) | periodogramas de Lomb–Scargle (como Korolik, A14) usam observações brutas |
| **Comparação de estados (D46)** | a unidade de análise é a comparação de variabilidade entre estados | só 8 pontos em 1995–2002 | as 119 linhas digitalizadas entram só aqui (D58, grau C) |

## 3. Interações com outras decisões

- **D69 (S e R′_HK):** a conversão para R′_HK (D52) é por observação, usando B−V; a faixa de validade de D53 e o escopo de Noyes (D61: nível médio, não flutuação) valem para qualquer das duas séries, mas Noyes define ⟨S⟩ como nível médio, o que favorece a anual para R′_HK.
- **D72 (junção):** as duas séries carregam o degrau; a bruta o carrega em cada observação, a anual em cada média.
- **Q1:** o N efetivo depende da série (ver acima); a escolha de amostra (subconjunto Baum, CLS V, catálogo Baliunas) é a pergunta seguinte e depende destes papéis. A CLS V tem Nobs ≥ 45 por estrela em cerca de 19 anos (2005–2023, v6 §3.4), logo é naturalmente "bruta".
- **Protocolo e regra 8:** nenhuma das duas séries exige fotometria própria; ambas vêm de tabelas públicas já reduzidas.

## 4. Combinações em uso na literatura auditada (fatos, sem preferência)
| Fonte | O que faz | Série |
|---|---|---|
| Luhn+2022 §3.1 | σ_S por estado, ⟨S_HK⟩ por estado; médias anuais para o gráfico | bruta e anual |
| Baum+2022 | classificação por periodograma de toda a série; HD 101501 e HD 166620 por inspeção da série | bruta |
| Isaacson+2024 (CLS V) | S-STD (SSD/Smed) por estrela e ciclos por periodograma | bruta |
| Dakos+2012 | indicadores em janelas deslizantes sobre séries (inclui irregulares) | a série como dada |
| Egeland+2017 | médias de ciclo e amplitude por ciclo sobre a série composta | bruta e média por ciclo |

## 5. Perguntas a responder para fechar D68 (sem sugerir a resposta)
1. Qual série roda o indicador de CSD em janelas (AR(1), variância, τ)?
2. Qual série roda a DFA, e Q9 se reabre para o subconjunto Baum?
3. Qual série calcula σ por estado (item 7, D70) e a média de ciclo?
4. Como tratar as lacunas (mediana 7.17 anos) na série bruta?

Estado: **papéis com subsídios entregues; escolha pendente (D76).**

## Adendo de 2026-11-24 (Livina & Lenton, Peng+1993; D81)
- **DFA:** Livina & Lenton pedem "at least of order a thousand points" e "several hundred points per window" (p. 3; `3.11-56`); a mediana bruta do subconjunto Baum é 698 (`3.3-01`) e a anual 27 (`3.3-05`). A série da Groenlândia deles é irregular (1586 pontos, janelas de 500; p. 4, `3.11-58`). A calibração DFA → c do §2.4 foi ajustada em AR(1) regular de 20 000 pontos (p. 3).
- **Incerteza de expoentes:** a flutuação do expoente de uma sequência finita cai com √N e não depende da amplitude do ruído (Peng+1993, pp. 2–3; `3.11-59`, `3.11-60`). Peng+1993 usa o estimador da caminhada de DNA, não o DFA.
- **CSD em janelas:** Livina usa janela de ACF de 10 % da série (p. 2; `3.11-55`), contra 50 % de D20; Held & Kleinen estimam κ com erro √(2κ/T) (p. 3; `3.11-53`), que pede muitos tempos de decaimento (A7b-F2).

## Adendo de 2026-11-24 (2): subsídios para decidir os papéis, à luz de D90, D86, D85 e D81
**Pedido do pesquisador:** "Subsídios para decidir os papéis das séries." Não escolhe e não recomenda. Números de `inspecao/saidas/13_series_roles.txt` (`3.16-01` a `3.16-04`, script `13_series_roles.py`) e das fontes com página.

### 1. Os tamanhos, nos grupos do P4 (e não na mediana das 59)
| Conjunto (subconjunto de Baum) | Estrelas | Observações brutas (mediana; mín.–máx.) | Estações anuais (mediana; mín.–máx.) | Janela de 50 % em estações | Maior lacuna (mediana) |
|---|---|---|---|---|---|
| `Flat` limpas (5; Baum tem 4) | 4 | 1 795 (1 337–2 520) | 48 (39–49) | 24 | 3.68 anos |
| Controles `CYCLE`+Excellent (13; Baum tem 6) | 6 | 1 822 (1 340–3 870) | 46 (43–53) | 23 | 6.83 anos |
| Todas as 59 de Baum | 59 | 698 (43–4 627) | 27 (9–54) | 14 | 7.17 anos |
| HD 166620 | 1 | 1 762 | 45 | 22 | 6.91 anos |
| HD 101501 | 1 | 2 217 | 32 | 16 | 13.82 anos |

**Correção do quadro anterior:** os 27 anuais e 698 brutos eram a mediana das 59; nos grupos do P4 as séries são maiores (cerca de 46–48 estações; 1 800 observações). Nenhuma estrela tem 100 estações anuais (`3.16-02`: 0 de 59); 22 de 59 têm ≥ 1 000 observações brutas (`3.16-01`), incluindo as quatro `Flat` e os seis controles presentes.

### 2. O que as fontes dizem sobre agregar ou não
| Fato | Fonte | Efeito |
|---|---|---|
| A autocorrelação de lag 1 "is related to the shortest time scale and is more vulnerable to the influence of noise", "therefore the aggregation of the series is required" | Livina & Lenton p. 3 (`3.11-75`) | favorece agregar antes de AR(1) |
| Δt-agregação (soma em janelas disjuntas) "eliminates weather noise"; Δt escolhido com Δt ≫ 1/κᵢ (modos menores) e 1/κ ≫ Δt | Livina p. 2, Held & Kleinen p. 2 (A7b item 3) | o passo anual é uma Δt-agregação; a escolha de Δt é do método |
| Depois de ~1980 há tipicamente **três observações por estrela por noite**, em sequência rápida | README do HK Project, p. 1 (`3.11-76`) | na série bruta, o lag mais curto é dominado por observações da mesma noite |
| O DFA pede "at least of order a thousand points" e várias centenas por janela | Livina p. 3 (`3.11-56`) | 22 estrelas da amostra de 59, e todas as presentes dos dois grupos, passam; a série é irregular |
| Janela de ACF de 10 % da série em Livina; 25–75 % em Dakos (D20) | Livina p. 2 (`3.11-55`); Dakos p. 17 (`3.11-41`) | com 46–48 estações, 10 % = cerca de 5 pontos; 25 % = cerca de 12; 50 % = cerca de 24 |
| A flutuação do expoente cai com √N, independentemente da amplitude do ruído | Peng+1993 pp. 2–3 (`3.11-59`, `3.11-60`) | mais pontos reduzem a incerteza, mas só se forem independentes |
| CSD exige muitos tempos de decaimento (δκ ≈ √(2κ/T)) | Held & Kleinen p. 3 (`3.11-53`) | o tempo de decaimento estelar não é conhecido (Q10) |

### 3. O que a hipótese de D90 pede de cada série (sem definir a hipótese)
| Parte do teste | Quantidade necessária | Anual | Bruta |
|---|---|---|---|
| Tendência temporal de um indicador (AR(1), variância, τ) antes da transição | uma janela deslizante com muitos pontos; passo Δt ≫ tempos de modos rápidos | 39–49 estações nos grupos; janela de 50 % ≈ 23–24 pontos; HD 166620 tem 8 pontos na aproximação, grau C (D46, D86), HD 101501 tem 16 de janela e lacuna de 13.8 anos | milhares de pontos, mas lag mais curto dominado por tripletos noturnos e lacunas de até 3.7 a 6.8 anos (mediana por grupo) |
| Comparação de variabilidade entre estados (Luhn §3.1) | σ por estado | a variante "por estação" (D57, conta B) | a conta A (σ do intervalo, D57) |
| DFA (Q9) | mil pontos ou mais, série regular | abaixo do piso de D24 | acima do piso de Livina em 22 de 59; irregular, Livina testou séries irregulares só com janelas de 500 pontos e sem calibração própria |
| Índice (D69: S e R′_HK) | por observação, com B−V (D52) | média anual do índice, perde a distinção por observação | R′_HK por observação; faixa de validade de D53 vale para os dois |

### 4. Três distribuições possíveis (nenhuma recomendada)
| Distribuição | O que dá | O que custa |
|---|---|---|
| **A.** Anual para as tendências temporais; bruta só para σ por estado e períodos | segue Δt-agregação de Livina e Held & Kleinen; janelas de 23–24 pontos | N ≈ 40–49 limita D20 (10–37 pontos na faixa 25–75 %); HD 166620 e HD 101501 ficam fora do teste temporal (D46, lacuna); DFA continua fora (D24) |
| **B.** Bruta para tudo (janelas em tempo) | uso total dos dados; DFA possível em 22 estrelas | exige método para lacunas e para os tripletos noturnos; calibração de Livina não testada em irregular; reabre D24 e Q9 |
| **C.** Anual para CSD; bruta para σ por estado e DFA, com Q9 decidida à parte | combina A e B por métrica; é o que "ambas com papéis distintos" (D68) descreve em termos gerais | exige declarar a regra por métrica e tratar de forma separada o DFA em Methods; mais texto |

### 5. Pontos independentes da escolha
- A junção HKP-2 → HIRES-2 (D44, D72) entra nas duas séries.
- As 119 linhas `new_MW` (D58, D86) não entram como valor em nenhuma.
- O `HK_Project_v2001_NSO` (D85) é bruto e termina em 2001; se entrasse como camada ao lado, fica no mesmo regime.
- A decisão dos papéis fixa D68/D76 e destrava Q1 (D79), o enunciado da hipótese de D90 e as escolhas adiadas de σ_S (D70), D46 (D73) e junção (D72).

Estado: **papéis com subsídios completos; escolha pendente (D91).**
