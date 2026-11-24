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
