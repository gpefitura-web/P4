# Decisões novas D41–D54 — para incorporação ao `P4_RESEARCH_NOTEBOOK.md`

**Origem:** segunda rodada de auditoria, unidades A9–A12 · **Data:** 2026-08-01
**Convenção (D31):** o caderno é atualizado apenas no fecho da conversa; decisões são imutáveis; uma revogação recebe `status: revogada` e uma entrada nova.

> **Instrução de incorporação.** Inserir a §4c abaixo após a §4b existente do caderno; substituir a tabela da §5 (questões abertas) pela versão dada em C; acrescentar as linhas de B à §8 (questões fechadas); acrescentar a linha de D à §9 (log de entradas).

---

## A · Bloco de decisões

### § 4c · Decisões da segunda rodada de auditoria (A9–A12), 2026-08-01

---

### D41 — Os `.tsv` VizieR da raiz são identificados e passam a ser a fonte numérica primária das séries estendidas
**Data:** 2026-08-01 · **Base:** A9 §0; quatro checksums exatos contra o texto nativo · **Status:** ativa · **Grau:** A

| Arquivo | Catálogo | Artigo | Conteúdo | Linhas |
|---|---|---|---|---|
| `J:AJ:163:183:table1.tsv` | J/AJ/163/183/table1 | Baum+2022 | séries de S-value | 62 135 |
| `J:163:183:table2.tsv` | J/AJ/163/183/table2 | Baum+2022 | parâmetros e classificações | 59 |
| `J:ApJ:936:L23:table2.tsv` | J/ApJ/936/L23/table2 | Luhn+2022 | S_HK de HD 166620 | 1 885 |
| `J:ApJ:936:L23:table3.tsv` | J/ApJ/936/L23/table3 | Luhn+2022 | fotometria APT T4 | 1 278 |
| `J:ApJS:274:35:table2.tsv` | J/ApJS/274/35/table2 | Isaacson+2024 | 710 estrelas, S e σ_S | 710 |
| `J:ApJS:274:35:table3.tsv` | J/ApJS/274/35/table3 | Isaacson+2024 | séries S do Keck | 52 380 |
| `J:ApJS:274:35:table4.tsv` | J/ApJS/274/35/table4 | Isaacson+2024 | 138 ciclos | 138 |

Validação: `Nobs` da Tabela 2 = contagem na Tabela 1, estrela a estrela, 59/59, soma 62 135; `Cadence` = `Nobs`/baseline exato (máx. |Δ| = 0.005); contagens por instrumento de HD 166620 reproduzem exatamente Luhn+2022 §2.1 (107 / 1 547 / 9 / 103).
**Consequência:** o lado **estelar** deixa de depender de rede. O item de ação da Tabela 4 de Egeland (trilha solar) continua bloqueado.

---

### D42 — Os períodos de Baum ficam ao lado dos de Baliunas e de Saar, nunca fundidos, e com o método explícito
**Data:** 2026-08-01 · **Base:** D15, D36, A9-F3, A9-F7 · **Status:** ativa
`baum2022_cycle_periods.csv` tem 14 linhas com a coluna `metodo_baum` distinguindo **10 por periodograma** de **4 estimados a olho** (marcados `?` pelo próprio Baum). Baum **não publica FAP nem qualquer medida de significância**; o período é simplesmente o pico de maior potência. Os períodos de Baum são grau **B** e **não são equiparáveis** a `CYCLE` + FAP Excellent de B95.
**Descartado:** tratar os dois conjuntos de períodos como comensuráveis.

---

### D43 — As classificações de Baum entram como camada época-dependente para todas as 26 estrelas em comum, não só para HD 166620
**Data:** 2026-08-01 · **Base:** D34 generalizada; A9 §2 · **Status:** ativa · **Grau:** A
Das 26 estrelas em comum, **14 receberam nova classificação** (checksum §4.2 de Baum reproduzido). O catálogo `baliunas_table2_full.csv` **permanece congelado**. As classificações de Baum vivem em `baum2022_59stars.csv`, coluna `class_Baum`, ao lado de `class_A1`.
**Descartado:** corrigir A1 com as classificações de 2022.

---

### D44 — A incerteza residual dos offsets instrumentais de Baum é grau X; a junção 2001→2004 é tratada como descontinuidade declarada
**Data:** 2026-08-01 · **Base:** A9 §1.5, A9-F6 · **Status:** ativa · **Grau:** X
Baum corrige offsets por **deslocamento aditivo constante que alinha medianas** (§2.1.1–2.1.3). **Não publica** os valores dos offsets, a sua incerteza, nem a identidade das catorze estrelas de §2.1.3. As séries da Tabela 1 contêm apenas valores já corrigidos.
Medição própria do resíduo (`audit/a9_instrument_step.csv`, 51 estrelas): degrau relativo HKP-2 → HIRES-2 com **σ = ±4.47 %** entre estrelas; **25/51 excedem 1.2 %** (precisão de longo prazo, D14); 10/51 excedem 5 %; HD 166620 dá −8.8 % e HD 4628 — que Baum classifica como **ainda cíclica** — dá −16.3 %.
**Regra operacional:** nenhuma janela deslizante atravessa a junção sem decisão explícita registrada.
**Exceção, por D45b:** para **HD 166620** a calibração é robusta, estabelecida por Luhn+2022 §3.1/§4 via sobreposição temporal com os dados de Oláh+2016 e via fotometria APT independente. **A exceção não se estende às outras 58 estrelas.**

---

### D45 — A definição operacional de variabilidade intra-sazonal de Luhn+2022 §3.1 é adotada como receita e como precedente citável
**Data:** 2026-08-01 · **Base:** A10 §1.4, reproduzida exatamente · **Status:** ativa · **Grau:** A
Receita: (1) σ_S calculado **dentro de cada estação**; (2) subtração **em quadratura** de uma estimativa do ruído instrumental — Luhn adota 1.2 % para Mount Wilson (Baliunas+1995, "least variable stars") e **0.3 %** como limite superior do ruído sazonal do Keck; (3) comparação por **F-test**.
Reprodução independente sobre `J:ApJ:936:L23:table2.tsv`: σ_S(mín 1) = **0.0027**, σ_S(mín 2) = **0.0054**, σ_S(grande mínimo) = **0.0019** — os três valores publicados, exatos.
**Consequência:** resolve parcialmente **Q6**, ao dar um tratamento publicado para separar variabilidade astrofísica de ruído instrumental. É a citação mais forte disponível para a escolha de indicador do P4.

---

### D45b — A robustez de calibração estabelecida por Luhn é restrita a HD 166620
**Data:** 2026-08-01 · **Base:** A10-F4 · **Status:** ativa · **Grau:** A
Luhn §4: "the mutual calibration there is robust"; §3.1: "dispelling any doubts about potential offset errors". A conclusão apoia-se em (a) dados de Mount Wilson **contemporâneos** dos dados HIRES pré-2004, e (b) fotometria APT que **atravessa os três conjuntos**. Nenhuma das outras 58 estrelas de Baum tem qualquer dos dois. **D44 permanece em vigor para elas.**

---

### D46 — O teste temporal de CSD no formato de Dakos não é executável em HD 166620; a unidade de análise é a comparação de variabilidade entre estados
**Data:** 2026-08-01 · **Base:** A10-F2 · **Status:** ativa · **Grau:** A
Com os dados de Oláh+2016 a lacuna caiu de 6.91 para **2.82 anos** e a aproximação **está amostrada** — mas com **8 médias anuais de S_HK** (1995–2002) e **12 estações fotométricas APT** (1993–2004). Sob D20 (janela = 50 % do comprimento), 8 pontos dão 5 janelas de 4 pontos: φ₁ sobre 4 pontos não tem sentido estatístico e uma tendência de Kendall sobre 5 valores sobrepostos não é testável pelo procedimento de surrogates de D22.
**Isto entra no manuscrito como limitação declarada, não é contornado.**
**Descartado:** aplicar a maquinaria de janela deslizante do P4 à série anual de HD 166620.

---

### D47 — HD 4915 não é apresentada como candidata a mínimo de Maunder sem citar Isaacson+2024
**Data:** 2026-08-01 · **Base:** A10-F3, A11b-F3 · **Status:** ativa · **Grau:** A
Cadeia cronológica obrigatória: **Shah+2018** propõe a candidatura → **Luhn+2022 nota 8** especula que "may soon be entering its own grand magnetic minimum" → **Isaacson+2024 §5.6**, com linha de base estendida: "our extended time baseline shows **two cycles**. One periodicity is at 4.9 yr, and the second is more than 40 yr, and **the longer-period cycle is now turning higher**." A Tabela 4 da CLS V registra P = 4.86 yr.
**D07 permanece ativa** (HD 4915 removida do catálogo por não estar em Baliunas+1995) e **D35 permanece correta**; o que se acrescenta é que **a candidatura está desmentida na literatura de 2024**.

---

### D48 — A raridade publicada entra na Discussion como taxa-base, com a ressalva de que mede nível instantâneo
**Data:** 2026-08-01 · **Base:** Järvinen & Strassmeier 2025 §6; A11a-F1, A11a-F2 · **Status:** ativa · **Grau:** A
Número a citar: **13 candidatas em 13 326 alvos F8–G8 de sequência principal (0.1 %)**, das quais **11 são estrelas evoluídas** por paralaxe Gaia DR3 → **2 candidatas, 0.015 %**. Sentença: "Contrary to the initial suggestion from the Mount-Wilson H&K Survey, we conclude that such stars are very rare."
**Ressalva obrigatória e sustentada por duas fontes grau A:** o critério de Järvinen & Strassmeier é de **nível instantâneo**, e Luhn+2022 demonstrou que o nível **não cai** num grande mínimo (⟨S_HK⟩ = 0.171 no grande mínimo vs 0.172 no mínimo de ciclo). **HD 166620 não seria selecionada por aquele critério.** Logo o 0.1 % mede a frequência de estrelas *anomalamente fracas*, não de estrelas *em grande mínimo* — quantidades identificadas na literatura antiga e desidentificadas por Luhn+2022.

---

### D49 — A hipótese *aged out* entra na Discussion como nula concorrente; HD 101501 é o discriminante empírico
**Data:** 2026-08-01 · **Base:** CLS VI §3.3, §4; Baum §4.1; A11 §c.1 · **Status:** ativa · **Grau:** A
CLS VI: "noncycling stars that **may have aged out** of their cycles". Explica as mesmas observações sem bifurcação: perda monotônica e irreversível do ciclo por evolução. **Difere do quadro do P4 na reversibilidade e na existência de precursor.**
**Discriminante:** o retorno ao ciclo. **HD 101501** — dez anos de estado plano (≈1980–1990) seguidos de retorno à atividade cíclica **defasado em 180°** (Baum §4.1), 2 239 observações, baseline de 49 anos, presente em `baum2022_59stars.csv` — é o único caso conhecido e **falsifica *aged out* para aquele objeto**. A própria CLS VI §4 declara a lacuna: "Whether or not stars reach a noncycling level that is inescapable or if they can begin cycling again will require additional observations."

---

### D50 — A afirmação de estocasticidade e de transição rápida é citada textualmente e respondida, não omitida
**Data:** 2026-08-01 · **Base:** CLS VI §3.3.1, §3.3; A11 §c.2 · **Status:** ativa · **Grau:** A
Sentenças a citar na íntegra: "**The mechanisms that cause a star to enter and exit a magnetic minimum requires a stochastic process that is poorly understood**" e "suggestive of a **rapid (on stellar timescales) transition** … these transitions can occur **quickly, on order of years**".
**Por que é a objeção mais séria:** CSD exige aproximação lenta em relação à amostragem; transição "na ordem de anos" com amostragem anual não deixa janela — e A10-F2 chegou à mesma conclusão empiricamente no único caso amostrado.
**Resposta registrada, e é teórica:** a CLS VI descreve uma **distribuição bimodal de S-STD**, assinatura de sistema **biestável**. Biestabilidade forçada por ruído produz transições de aparência estocástica que **ainda exibem CSD**, porque a barreira de potencial encolhe antes do salto. **Este argumento exige base auditada em A7 (Scheffer 2009; Held & Kleinen 2004), que ainda não foi executada.** Registrado como dependência.

---

### D51 — A inclinação estelar entra como confundidor declarado do grupo `Flat`
**Data:** 2026-08-01 · **Base:** CLS VI §3.2; A11 §c.3 · **Status:** ativa · **Grau:** A (para τ Cet) / X (para as demais)
CLS VI, literal: "τ Ceti … is known to have a **pole-on inclination** (Korolik et al. 2023) that **precludes us from identifying its chromospheric activity cycle or rotational modulation** via S-STD."
**τ Cet (HD 10700) é uma das cinco `Flat` limpas do P4 e a estrela-padrão de dispersão.** Uma estrela vista de polo tem variabilidade suprimida **por geometria**, sem relação com o dínamo. Nenhuma unidade de auditoria anterior registrou este confundidor.
**Consequência:** afeta Q1, Q2 e Q6. A inclinação das demais `Flat` do P4 **não foi medida em nenhuma fonte auditada** — grau X, item de ação.

---

### D52 — A receita S → R′_HK fica estabelecida em grau A, com faixa de validade
**Data:** 2026-08-01 · **Base:** A12 §2, três passes de verificação · **Status:** ativa · **Grau:** A

```
R_HK      = 1.340 × 10⁻⁴ · C_cf(B−V) · S
log C_cf  = 1.13(B−V)³ − 3.91(B−V)² + 2.84(B−V) − 0.47
log C′_cf = log C_cf + Δ log C ;  Δ log C = 0                                    se B−V > 0.63
                                  Δ log C = 0.135x − 0.814x² + 6.03x³,  x ≡ 0.63 − (B−V) > 0
log R_phot = −4.898 + 1.918(B−V)² − 2.893(B−V)³
R′_HK     = R_HK − R_phot
```

Verificação: o PDF é scan com OCR de origem defeituoso (`10⁻⁴` lido como `Kr4`, `B−V` como `B—F`). Três passes: texto nativo, Tesseract a 400 DPI em `--psm 6/4/11`, e **inspeção visual direta das imagens de página ampliadas** — o passe que fixou expoentes e sinais.
Forma alternativa de Duncan, "fits the one used in this paper to within observational errors": **log R_phot = −4.02 − 1.40(B−V)** (grau B).
A constante 1.340 × 10⁻⁴ absorve a constante de Stefan-Boltzmann e um fator de normalização de 10¹⁴.

---

### D53 — A faixa de validade é 0.44 < B−V < 0.82 para R_phot, com extrapolação declarada acima e até 20 % de incerteza acima de 1.0
**Data:** 2026-08-01 · **Base:** A12 §3, Apêndice *b* e §II de Noyes+1984 · **Status:** ativa · **Grau:** A

| Faixa | Estatuto declarado pela fonte |
|---|---|
| B−V < 0.44 | fora do ajuste de R_phot |
| B−V < 0.63 | requer Δ log C (máximo não-físico de C_cf em 0.43) |
| **0.44 – 0.82** | **faixa em que R_phot foi ajustada** |
| 0.82 – 1.0 | extrapolação declarada; C_cf ainda "quite consistent" com espectrofotometria independente |
| **> 1.0** | "**the calibration may be uncertain by as much as 20 %**"; R_phot "becomes negligible" e "less certain for the coolest stars" |
| ≳ 1.2 | "**the worst discrepancy** in the various attempts at calibration" |

Aplicação ao catálogo congelado de A1 → `noyes1984_validade_cor.csv` (112 linhas). Distribuição: 82 dentro · 17 em 0.82–1.0 · 6 acima de 1.0 · 2 acima de 1.2 · 5 abaixo de 0.44.

---

### D54 — A migração para R′_HK deixa de ser melhoria presumida e passa a trade-off quantificado; a recomendação registrada é **não migrar**
**Data:** 2026-08-01 · **Base:** A12-F1, A12-F2, A12-F5; CLS VI §5 e §3.1 · **Status:** ativa · **Decisão final: humana (Q8 continua aberta)**

Três evidências contrárias novas, todas grau A:

1. **A validade da calibração é correlacionada com o grupo (A12-F1).** Das cinco `Flat` limpas, **quatro estão dentro** de 0.44–0.82; das treze `CYCLE` + FAP Excellent, **apenas cinco estão dentro e oito extrapolam**, duas (HD 32147 B−V = 1.06 e HD 201091 = 1.18) na região de até 20 % de incerteza declarada. Converter trocaria um confundimento de cor **conhecido e declarável** por um **erro sistemático concentrado num só braço da comparação** — que é pior.
2. **A fonte se desautoriza para o regime do P4 (A12-F2).** Noyes+1984, Apêndice *b*: a subtração de R_phot "does not have a large effect for active chromosphere stars, but **it can be a very significant correction for the chromospherically less active stars. For these stars in particular it is important to determine the photospheric correction more rigorously than has been done here.**" A amostra inteira do P4 está nesse regime.
3. **A comparação já foi feita e deu o resultado oposto ao esperado.** CLS VI §5, sobre 710 estrelas com séries de 20 anos: "neither average activity metrics of S-value, **log(R′_HK)-N1984**, nor the revised log(R′_HK) metric from Lorenzo-Oliveira et al. (2018) are able to identify [as não-cíclicas]. **More so than these two types of log(R′_HK), the S-value itself best correlates with S-value variability.**" E §3.1: "**the S-value plus the stellar mass is the best metric**."

**D40 confirmada e delimitada (A12-F5):** para B−V fixo a transformação é monotônica, logo τ é **exatamente** invariante, φ₁ muda pouco e σ² apenas reescala. O eixo **temporal** nada sofre com a migração — e nada ganha. O ganho seria todo no eixo **comparativo**, que é exatamente onde as três evidências acima incidem. Acresce que a receita tem **duas descontinuidades** (B−V = 0.63 e 0.82) **no interior da amostra P4** (A12-F3): um índice com costuras internas não é um índice unificador.

**Recomendação registrada:** manter S; tratar massa ou T_eff como covariável, seguindo a CLS VI; citar A12-F1 e A12-F2 como justificação explícita em Methods. **A decisão continua sendo humana.**

---

## B · Linhas a acrescentar à §8 (questões fechadas)

| Questão | Resposta | Fechada por |
|---|---|---|
| Baum+2022 estende as séries de forma utilizável? | **Sim, numericamente.** 62 135 observações, 59 estrelas, 1966–2020, machine-readable e locais. **Mas a extensão é não-uniforme entre os grupos do P4** e a incerteza dos offsets não é publicada | A9 §1.1–1.3; A9-F5; D41, D44 |
| A média de atividade discrimina um grande mínimo? | **Não.** ⟨S_HK⟩ = 0.171 no grande mínimo vs 0.172 no mínimo de ciclo. O discriminante é a **variabilidade** | A10 §1.3, três checksums exatos |
| A lacuna observacional em HD 166620 foi fechada? | **Sim.** De 6.91 para 2.82 anos, com os dados de Oláh+2016 | A10 §1.2 |
| A aproximação à transição está amostrada? | **Sim — com 8 médias anuais e 12 estações fotométricas.** Suficiente para comparar estados, **insuficiente** para a maquinaria de janela deslizante do P4 | A10-F2; D46 |
| Existe precedente publicado para usar variabilidade como diagnóstico de estado magnético? | **Sim.** Luhn+2022 §3.1, com receita completa, reproduzida exatamente | A10 §1.4; D45 |
| Alguém já afirmou que grandes mínimos são estocásticos/imprevisíveis? | **Sim, em 2025.** CLS VI §3.3.1: "requires a stochastic process that is poorly understood"; transições "on order of years" | A11 §c.2; D50 |
| Qual a taxa-base publicada de estrelas em estado tipo mínimo de Maunder? | **0.1 %** antes do corte evolutivo, **0.015 %** depois — **mas por critério de nível instantâneo**, que Luhn+2022 declara inválido | A11a-F1/F2; D48 |
| HD 4915 é candidata a mínimo de Maunder? | **Não, segundo a fonte mais recente.** Isaacson+2024: dois ciclos, 4.9 yr e > 40 yr, com o longo subindo | A11b-F3; D47 |
| Qual a receita de conversão S → R′_HK e a sua faixa de validade? | **Estabelecida em grau A.** R_phot ajustada em 0.44 < B−V < 0.82; até 20 % de incerteza acima de B−V = 1.0 | A12 §2–3; D52, D53 |
| R′_HK é melhor que S como correlato de variabilidade? | **Não, segundo teste publicado em 710 estrelas.** S + massa estelar é a melhor métrica | CLS VI §5; A12-F1/F2; D54 |

---

## C · §5 revista — questões abertas

| # | Questão | Estado após A9–A12 |
|---|---|---|
| **Q1** | **Composição da amostra** | **aberta — desbloqueada.** D32 cumprida. Subsídios: `paper_state_v6.md` §3, com quatro opções e os custos de cada uma. Custo novo e decisivo: A9-F5 (N × grupo no subconjunto Baum) |
| **Q2** | O que conta como "flat" | **aberta — subsídio novo.** Quatro das cinco `Flat` têm agora medida moderna: σ_S/S = 0.72 / 0.86 / 0.95 / **1.49 %** (A11 §b.3). HD 182572 falha. **E D51 acrescenta a inclinação como confundidor geométrico completo** |
| **Q3** | Largura de banda gaussiana | **aberta — inalterada** |
| **Q4** | A componente de 44 anos | **aberta — reforçada.** A11b-F5: componentes longas quase degeneradas com tendência são o caso **típico**, não uma idiossincrasia solar. Isso transforma Q4 numa questão genérica do método |
| **Q5** | Binárias | **aberta — inalterada.** Nota: HD 81809 está **ausente** de Baum |
| **Q6** | O grupo `Flat` tem problema de medida | **aberta — grande avanço.** Piso instrumental moderno = **0.45 %**, três vezes abaixo do limiar `Flat`. **D45** dá o tratamento de subtração de ruído em quadratura. Continua a exigir decisão de apresentação |
| **Q7** | Subgigantes no grupo `Flat` | **aberta — agora é objeção publicada.** Três fontes independentes: Wright 2004, Baum §5.5 (A9-F8), Järvinen & Strassmeier §1 e §6 (11 de 13 candidatas eliminadas por serem evoluídas). Tem de ser neutralizada **por construção da amostra**, não por argumento |
| **Q8** | Migrar para log R′_HK? | **aberta — balanço invertido.** D54: três evidências contrárias grau A. Recomendação registrada: **não migrar** |
| **Q9** | DFA volta a ser admissível para o subconjunto Baum? | **aberta — reportada, não decidida.** N mediano = **27 estações anuais** (abaixo do piso) vs **698 observações brutas** (acima). **A pergunta é anterior:** a série anual ou a bruta é o objeto do P4? (`paper_state_v6.md` §6) |
| **Q10** | **NOVA — a transição é lenta o bastante para ter precursor detectável?** | **aberta.** CLS VI: "on order of years". A10-F2: 8 pontos anuais na aproximação do único caso amostrado. **Se a resposta for não, a tese central do P4 não é testável com os dados existentes.** Depende de A7 |
| **Q11** | **NOVA — a inclinação estelar confunde o grupo `Flat`?** | **aberta.** D51. Confirmada para τ Cet; não medida para as demais |

---

## D · Linha a acrescentar à §9 (log de entradas)

| Data | Entrada | Decisões |
|---|---|---|
| 2026-08-01 | **Segunda rodada de auditoria: A9 (Baum+2022), A10 (Luhn+2022), A11 (Järvinen & Strassmeier 2025 + CLS V + CLS VI), A12 (Noyes+1984) fechadas em Cowork.** Q1 desbloqueada; Q9 reportada e devolvida; Q8 com balanço invertido; duas questões novas (Q10, Q11). Séries estendidas obtidas em forma numérica local. Cinco contradições registradas | D41–D54 |

---

## E · O que passou a ser decisão humana

Explicitamente, e em ordem de dependência:

1. **A série anual ou a série bruta é o objeto do P4?** — governa Q9/D24, D20–D23 e todo o cálculo de φ₁ e σ². **É a decisão-raiz desta rodada e nenhuma outra pode ser tomada antes dela.**
2. **Q1 — composição da amostra.** Quatro opções com custos quantificados em `paper_state_v6.md` §3.4. Recomendação registrada: as opções (ii) e (iv) não são exclusivas, e **HD 101501** é o objeto que melhor sobrevive às objeções publicadas.
3. **Q8 — migrar ou não para R′_HK.** Recomendação registrada em D54: **não migrar**.
4. **Como tratar a junção instrumental 2001→2004** se a opção (ii) de Q1 for escolhida (D44).
5. **Se D46 é aceite** — declarar no manuscrito que o teste temporal no formato de Dakos não é executável no único caso amostrado.
6. **Se a resposta teórica a D50** (biestabilidade vs estocasticidade) é sustentável — **depende de A7, que precisa ser executada antes.**
7. **Q2, Q3, Q4, Q5, Q6, Q7, Q11** — todas continuam humanas.

**Nenhuma unidade desta rodada decidiu Q1, Q8 ou D24.** O pipeline permanece congelado.
