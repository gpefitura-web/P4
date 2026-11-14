# paper_state_v6.md

**Paper P4 — *Critical Slowing Down Near Stellar Activity Minima***
**Estado em:** 2026-08-01, fecho da segunda rodada de auditoria (A9–A12)
**Substitui:** `paper_state_v5.md` · **Memória longa:** `P4_RESEARCH_NOTEBOOK.md`

---

## 1 · O que mudou nesta rodada

Quatro unidades executadas: **A9** (Baum+2022), **A10** (Luhn+2022), **A11** (Järvinen & Strassmeier 2025 + CLS V + CLS VI), **A12** (Noyes+1984). Dez decisões novas, **D41–D51**, mais três de método (D52–D54). Nenhuma unidade decidiu Q1, Q8 ou D24 — todas alimentam.

**A mudança de estado mais importante não é um valor; é a estrutura do problema.** Antes desta rodada o P4 tinha um catálogo de 1995 e uma hipótese. Agora tem:

- **séries estendidas, numéricas e locais** para 59 estrelas (62 135 observações, 1966–2020), com quatro checksums exatos;
- **um análogo de mínimo de Maunder confirmado** (HD 166620) com a transição traçada ponto a ponto;
- **um precedente publicado para a própria variável do P4** — Luhn+2022 usa variabilidade intra-sazonal como diagnóstico de estado, com receita completa e reproduzida exatamente;
- **e três objeções publicadas sérias** que não existiam no registro: raridade de 0.1 %, a hipótese *aged out*, e a afirmação de que a transição é estocástica e ocorre "na ordem de anos".

O P4 saiu desta rodada **melhor equipado e mais cercado**. As duas coisas são verdadeiras.

---

## 2 · O achado que reorganiza tudo

> **Luhn+2022, Resumo:** "neither the overall brightness nor the chromospheric activity level (as measured by S_HK) is significantly lower during the grand magnetic minimum than its activity cycle minimum, implying that **an anomalously low mean or instantaneous activity levels are not a good diagnostic or criterion for identifying additional Maunder minimum candidates**."
>
> **CLS VI, Resumo:** "the average chromospheric activity remains **nearly constant** while the **variation** in a star's activity decreases by an **order of magnitude**."

Verificado por recálculo independente (A10 §1.3): ⟨S_HK⟩ = 0.1810 (mín. de ciclo 1) · 0.1724 (mín. 2) · **0.1705 (grande mínimo)**. O estado de mínimo de Maunder **não é mais fraco** que um mínimo de ciclo ordinário. O que muda é a **variância**: σ_S corrigido cai de 0.0027 / 0.0054 para **0.0019**, com F-test de 8.78 × 10⁻⁶.

**Consequência para o P4, em três linhas:**
1. A premissa central do P4 — que o discriminante é a variabilidade, não a média — deixa de ser uma aposta e passa a ser uma **afirmação publicada e revisada por pares sobre o único caso confirmado**.
2. Toda seleção de amostra por ⟨S⟩ baixo está morta, incluindo a de Baliunas & Jastrow (1990). Isto reforça D13 e complica Q2.
3. **A parte que continua sendo do P4 e de mais ninguém é o eixo temporal:** Luhn e a CLS VI comparam *estados*; ninguém testou se a variabilidade **cresce antes** da transição. Esse é o espaço que resta, e é estreito — ver §4.

---

## 3 · Q1 (composição da amostra) — subsídios novos, decisão ainda humana

D32 suspendeu Q1 até A9. **A9 está fechada. Q1 volta à mesa com o seguinte quadro.**

### 3.1 Quem sobrevive à extensão

| Grupo do P4 | Em Baliunas | Em Baum+2022 | Em CLS V |
|---|---|---|---|
| `Flat` limpo (pós-D13) | 5 | **4** (falta HD 43587) | 4 (faltam 43587, 160346) |
| `CYCLE` + FAP Excellent | 13 (c/ Sol) | **6** | parcial |

**Custo declarado (A9-F5):** a extensão é **fortemente não-uniforme entre grupos**, e os sete controles ausentes são sistematicamente os mais vermelhos (B−V 0.96–1.18) ou binários — a CPS "notably omits very active stars" e seleciona alvos de planetas. **Se o P4 usar Baum, N passa a ser correlacionado com grupo.** D12 (N uniforme por construção) continua correta *para o catálogo Baliunas*; **não se estende ao subconjunto Baum**. Este era o cenário que A2 §5 identificou como "fatal em revisão" — reaparece, agora pelo lado da extensão.

### 3.2 Reclassificações que mexem nos grupos

- **HD 182572**: `Flat` (Baliunas) → **`var`** (Baum). σ_S/S = 1.49 % na CLS V — a mais alta das quatro `Flat` medidas, na fronteira do limiar de 1–1.5 %. **Duas fontes independentes questionam a sua planura.**
- **HD 10700 (τ Cet)**: `Flat?` → `flat` confirmada por Baum e sem ciclo detectado na CLS V (σ_S/S = 0.72 %, 944 obs). **Mas** a CLS VI §3.2 nota que τ Cet tem **inclinação polo-on** (Korolik+2023) "that precludes us from identifying its chromospheric activity cycle" — **um confundidor geométrico completo, novo, que não estava em nenhuma unidade anterior** (D51).
- **HD 166620**: continua `CYCLE` FAP Excellent em 1966–1991 e transiciona depois. D34 permanece. Baum atribui `17.0?`, Baliunas 15.8 ± 0.3.

### 3.3 Q6 recebe o seu primeiro subsídio concreto

| Referência | σ_S/S | Fonte |
|---|---|---|
| Piso instrumental HIRES moderno (HD 55575) | **0.45 %** | CLS V §5.6 |
| Piso estimado em A2-F6 | 0.8 % | A2 |
| τ Cet, baseline moderno | 0.72–0.83 % | CLS V; Gomes da Silva 2021 |
| Precisão de longo prazo de Mount Wilson (D14) | **1.2–1.4 %** | A6 |
| **Limiar `Flat` de Baliunas** | **1–1.5 %** | A1 §1.3 |

O piso moderno está **3× abaixo** do limiar `Flat`. Isto **não** valida a classificação de 1995 — que continua a viver dentro do erro dos dados de 1995 — mas mostra que **é testável hoje**, e quatro das cinco `Flat` do P4 já têm a medida feita (A11 §b.3): 0.72 %, 0.86 %, 0.95 %, 1.49 %. Três sobrevivem; HD 182572 não.

### 3.4 O que a decisão de Q1 tem de escolher entre

| Opção | Ganho | Custo |
|---|---|---|
| **(i)** Catálogo Baliunas congelado, N uniforme | D12 intacta; nenhum confundimento de comprimento | N ≈ 26; sem transição; sem teste temporal real |
| **(ii)** Subconjunto Baum (59 estrelas, cinco décadas) | 5× o baseline; HD 166620 e HD 101501 disponíveis | A9-F5 (N × grupo); A9-F6 (degrau instrumental ±4.5 %); só 4/5 `Flat` e 6/13 controles |
| **(iii)** CLS V (285 estrelas, ≥45 obs, um só detector) | homogeneidade instrumental; piso de 0.45 % | apenas ~19 anos (2005–2023); **exclui todo o HIRES pré-2005** |
| **(iv)** Estudo de caso: HD 166620 + HD 101501 | os dois únicos casos de transição documentados; fotometria APT independente para 166620 | n = 2; A10-F2 limita o que se pode testar |

**Recomendação registrada, não decisão:** as opções (ii) e (iv) não são exclusivas, e (iv) é a que sobrevive melhor às objeções de §4. **HD 101501 — dez anos de estado plano seguidos de retorno ao ciclo com defasagem de 180° (Baum §4.1), 2 239 observações, 49 anos** — é o único objeto conhecido que **falsifica *aged out*** e é o teste discriminante que a própria CLS VI §4 diz faltar.

---

## 4 · As três objeções publicadas que o manuscrito tem de responder

Registradas textualmente em A11. Nenhuma é fatal; nenhuma é ignorável.

### 4.1 Raridade — taxa-base de 0.1 %

> Järvinen & Strassmeier 2025 §6: "at most ≈0.1 % of the main-sequence stars in the B−V range of ±0.1 of the Sun show levels of magnetic activity significantly (≈20 %) below solar minimum… 11 of these 13 stars … [são] evolved stars." → **2 candidatas em 13 326 = 0.015 %.**

**Resposta disponível (A11a-F2), e é boa:** aquele critério é de **nível instantâneo**, e Luhn+2022 mostrou que o nível **não cai** num grande mínimo. **HD 166620 não seria selecionada por ele.** Logo o 0.1 % mede a frequência de estrelas *anomalamente fracas*, não de estrelas *em grande mínimo*. Uma busca por **variabilidade** em escala de levantamento ainda não foi feita — e é isso que o P4 propõe. Duas fontes grau A sustentam o argumento.

### 4.2 *Aged out* — a hipótese nula concorrente

> CLS VI §3.3: "noncycling stars that **may have aged out** of their cycles."

Explica a mesma observação sem bifurcação: estrelas velhas perdem o ciclo monotonicamente e irreversivelmente. **Discriminante:** o retorno ao ciclo. **HD 101501 é o caso.** Ver §3.4.

### 4.3 Estocasticidade e rapidez — a objeção mais séria

> CLS VI §3.3.1: "The mechanisms that cause a star to enter and exit a magnetic minimum **requires a stochastic process that is poorly understood**."
> CLS VI §3.3: "suggestive of a **rapid (on stellar timescales) transition** … these transitions can occur **quickly, on order of years**."

**Por que é séria:** CSD exige aproximação **lenta** em relação à amostragem. Transição "na ordem de anos" com amostragem anual não deixa janela. E A10-F2 chegou empiricamente à mesma conclusão a partir do único caso amostrado.

**Resposta disponível, e é teórica, não observacional:** a CLS VI descreve uma **distribuição bimodal de S-STD**, que é a assinatura de um sistema **biestável**. Biestabilidade + ruído produz transições que *parecem* estocásticas mas ainda exibem CSD, porque a barreira de potencial encolhe antes do salto. **Este argumento precisa de apoio em A7 (Scheffer 2009; Held & Kleinen 2004) e A7 ainda não foi executada.** Ver §7.

---

## 5 · A viabilidade do teste temporal — o número duro

**A9/A10 respondem a pergunta que a rodada existia para responder.**

Com os dados de Oláh+2016, a lacuna de HD 166620 caiu de **6.91 para 2.82 anos**. A aproximação **está amostrada**. Mas:

| Trilha | N na janela de aproximação | Janelas com D20 (50 %) | Executável? |
|---|---|---|---|
| Médias anuais de S_HK, 1995–2002 | **8** | 5 janelas de 4 pontos | **não** |
| Estações fotométricas APT, 1993–2004 | **12** | 7 janelas de 6 pontos | **marginal** |
| S_HK a cadência bruta, 1995–2002 | 132 | — | irregular; ver §6 |

**A conclusão que o manuscrito tem de declarar (D46):** o teste de CSD no formato de Dakos — janela deslizante de 50 %, τ de Kendall, 1 000 surrogates ARMA — **não é executável em HD 166620**. O que é executável é a comparação de variabilidade entre estados, no formato de Luhn §3.1. **Isto não é uma falha do P4; é uma propriedade do único dado que existe.** Declará-lo é mais forte do que contorná-lo, e é o que separa este manuscrito das duas rodadas anteriores.

---

## 6 · Q9 (DFA) — reportada, devolvida ao status Q

Conforme a regra anti-loop e a instrução da unidade, **nada foi decidido**. O número:

| Série | N por estrela (mediana) | Contra o piso de > 100 (A4-F4 / A5-F5) |
|---|---|---|
| Médias anuais (D08) | **27** | abaixo, fator ~4 — igual a Baliunas |
| Cadência bruta de Baum | **698** (56/59 acima de 100) | acima, fator ~7 |

**Três ressalvas grau A que a decisão precisa ter à mão (A9 §5):** a cadência bruta é **irregular** (lacuna interna mediana de 7.17 anos; 42/59 com lacuna > 5 anos) e o piso de A4/A5 pressupõe amostragem regular; é **dominada por modulação rotacional** (P_rot ≈ 45 d) que é ruído na escala de ciclo; e **atravessa a junção instrumental** (A9-F6), cujo degrau aparece como tendência numa soma cumulativa.

**A pergunta é anterior a "DFA sim ou não":** *a série anual ou a série bruta é o objeto do P4?* D08 diz anual. Se D08 for mantida, **D24 não muda e Q9 fecha sem decisão nova**. Se D08 for revogada, mudam também D20–D23 e o cálculo de φ₁ e σ².

---

## 7 · Q8 (migrar para R′_HK) — o balanço mudou de sinal

A12 estabeleceu a receita completa em grau A (três passes: texto nativo, Tesseract em três configurações, **inspeção visual das imagens de página a 400 DPI**):

```
R_HK   = 1.340 × 10⁻⁴ · C_cf(B−V) · S
log C_cf = 1.13(B−V)³ − 3.91(B−V)² + 2.84(B−V) − 0.47
log C′_cf = log C_cf + Δlog C ;  Δlog C = 0 se B−V > 0.63
                                 Δlog C = 0.135x − 0.814x² + 6.03x³,  x ≡ 0.63 − (B−V) > 0
log R_phot = −4.898 + 1.918(B−V)² − 2.893(B−V)³      [válida em 0.44 < B−V < 0.82]
R′_HK  = R_HK − R_phot
```

**Três evidências contrárias novas, todas grau A:**

1. **A12-F1 — a validade é correlacionada com o grupo.** 4 das 5 `Flat` estão **dentro** de 0.44–0.82; **8 das 13** `CYCLE` Excellent estão **fora**, duas na região de até 20 % de incerteza declarada. Converter trocaria um confundimento de cor conhecido por um **erro sistemático concentrado num só braço da comparação** — que é pior.
2. **A12-F2 — a própria fonte se desautoriza para o regime do P4.** Apêndice *b*: a subtração de R_phot "does not have a large effect for active chromosphere stars, but it **can be a very significant correction for the chromospherically less active stars. For these stars in particular it is important to determine the photospheric correction more rigorously than has been done here.**"
3. **CLS VI §5 — testado em 710 estrelas com séries de 20 anos:** "neither average activity metrics of S-value, log(R′_HK)-N1984, nor the revised log(R′_HK) metric from Lorenzo-Oliveira et al. (2018) are able to identify [as não-cíclicas]. **More so than these two types of log(R′_HK), the S-value itself best correlates with S-value variability.**" — e "the S-value plus the stellar mass is the best metric".

**D40 confirmada e delimitada (A12-F5):** para B−V fixo a transformação é monotônica, logo τ é exatamente invariante e o eixo temporal nada sofre. O ganho seria todo no eixo **comparativo** — e é aí que as três evidências acima incidem.

**Q8 permanece aberta e é decisão humana.** Mas a recomendação registrada é: **não migrar**; usar S com massa/T_eff como covariável, seguindo a CLS VI, e citar A12-F1/F2 como justificação.

---

## 8 · O que ficou grau X e precisa de decisão ou de escalada

| # | Item | Unidade | Impacto |
|---|---|---|---|
| 1 | **Incerteza residual dos offsets instrumentais de Baum** — não publicada; nem os valores, nem as 14 estrelas de §2.1.3 | A9 §1.5 | **alto** — o degrau residual medido é ±4.5 %, ~4× a precisão de longo prazo. Nenhuma janela deslizante pode atravessar a junção 2001→2004 sem decisão explícita |
| 2 | "**29 estrelas com ciclos periódicos**" (Baum, Resumo) — a Tabela 2 tem 14; Isaacson+2024 §4.2.2 conta 13 | A9-F1, A11b-F2 | médio — **nunca citar 29**; citar 13–14 |
| 3 | **158 vs 119** observações `new_MW` (Luhn §2.2 vs a própria tabela) | A10-F1 | baixo — nenhum valor derivado é afetado |
| 4 | **HD 185144** está em B95 (catálogo A1) ou não (Baum deixa em branco)? | A9-F2 | baixo — resolver na consolidação |
| 5 | "**50 estrelas menos dispersas que τ Cet**" — 48 ou 52 conforme o limiar; texto e tabela do próprio artigo discordam no σ de τ Cet | A11b-F1 | baixo — CSV usa o critério reproduzível (48) |
| 6 | **Incerteza formal de R′_HK** — o artigo não publica propagação | A12 §4 | médio, se Q8 for para migração |
| 7 | **Inclinação estelar** das `Flat` do P4 — não medida em fonte auditada, exceto τ Cet | A11 §c.3 | **alto para Q1/Q2** — confundidor geométrico completo da variabilidade |
| 8 | **[Fe/H]** da amostra P4 — ausente de A1 e A6 | A11a-F4 | médio — disponível em `baum2022_59stars.csv` e na Tabela 2 da CLS V; incorporar na consolidação |

---

## 9 · Contradições registradas, não resolvidas (protocolo regra 4)

| # | Contradição | Estatuto |
|---|---|---|
| 1 | **Todos** os períodos de Baum que se sobrepõem a Baliunas divergem por ≥ 2σ do dP publicado (até 20σ em HD 4628); seis dos sete são FAP **Excellent** | A9-F3 — ou o dP de B95 não é uma incerteza realista, ou os períodos mudaram. **Ambas compatíveis.** Reforça D15 |
| 2 | **HD 4915**: candidata a mínimo de Maunder (Shah+2018) → "may soon be entering" (Luhn nota 8) → **dois ciclos, 4.9 yr e >40 yr, o longo subindo** (Isaacson+2024 §5.6) | A10-F3, A11b-F3 — a fonte mais recente e com maior baseline **desfaz** a candidatura. D35 permanece; ganha camada (D47) |
| 3 | Contagem de ciclos em Baum+2022: **29** (Resumo) vs **14** (Tabela 2) vs **13** (Isaacson, co-autor) | três leituras |
| 4 | **HD 190406**: B95 dá primário 2.60 ± 0.02 (Fair) + secundário 16.9 (Good); Baum promove o secundário e dá 17.2 | A9-F4 — D10 continua correta como leitura de B95; a leitura física de 2026 é outra |
| 5 | HD 166620 é classificada `17.0?` (cíclica) na Tabela 2 de Baum, **e** proposta como candidata a mínimo de Maunder na §4.1 do mesmo artigo | tensão interna, resolvida por D34 (época-dependente) |

---

## 10 · Estado dos arquivos

### Novos nesta rodada

| Arquivo | Conteúdo |
|---|---|
| `audit/A9_baum.md` | 59 estrelas, N por instrumento e por estação, offsets, HD 166620, 10 achados, Q9 reportada |
| `audit/A10_luhn.md` | a transição ponto a ponto, os três estados, a receita de variabilidade intra-sazonal, 7 achados |
| `audit/A11_raridade.md` | raridade (a), CLS V (b), CLS VI e *aged out* (c), 9 achados |
| `audit/A12_noyes.md` | receita S → R′_HK completa em grau A, faixa de validade, 7 achados |
| `baum2022_59stars.csv` | 59 × 33 — parâmetros, N, baselines, lacunas, classificações, cruzamento com A1 |
| `baum2022_cycle_periods.csv` | 14 períodos (10 por periodograma, 4 a olho), Δ contra Baliunas em unidades de σ |
| `isaacson2024_least_active_50.csv` | 48 estrelas menos dispersas que τ Cet com ≥45 obs, critério documentado |
| `noyes1984_validade_cor.csv` | as 112 do catálogo A1 com a faixa de validade de Noyes+1984 |
| `audit/a9_instrument_step.csv` | degrau HKP-2 → HIRES-2 por estrela (51) |

### Os `.tsv` da raiz, identificados (D41)

| Arquivo | Artigo | Conteúdo |
|---|---|---|
| `J:AJ:163:183:table1.tsv` | Baum+2022 | séries de S, 62 135 obs, 59 estrelas |
| `J:163:183:table2.tsv` | Baum+2022 | parâmetros e classificações, 59 |
| `J:ApJ:936:L23:table2.tsv` | Luhn+2022 | S_HK de HD 166620, 1 885 |
| `J:ApJ:936:L23:table3.tsv` | Luhn+2022 | fotometria APT T4, 1 278 |
| `J:ApJS:274:35:table2.tsv` | Isaacson+2024 CLS V | 710 estrelas, S e σ_S |
| `J:ApJS:274:35:table3.tsv` | Isaacson+2024 CLS V | séries S do Keck, 52 380 |
| `J:ApJS:274:35:table4.tsv` | Isaacson+2024 CLS V | 138 ciclos |

### Congelados, inalterados

`baliunas_table2_full.csv` (A1, referência congelada) · `audit/saar_baliunas_crossmatch.csv` · `audit/A5_peng.md` · `audit/A6_saar.md` · e A1–A4 no Project Knowledge.

### Itens de ação ainda bloqueados

| Item | Domínio | Necessário para |
|---|---|---|
| **Tabela 4 de Egeland+2017** — série S solar calibrada, ciclos 15–24 | IOP | D18; a trilha solar |
| Harvard Dataverse (Radick & Pevtsov 2018b/c) — dados MW originais | Dataverse | **novo**: auditar os offsets de Baum por conta própria (A9-F6) |
| Série S solar do NSO | NOAA | alternativa a Egeland T4 |

**O lado estelar deixou de depender de rede.** Só a trilha solar continua bloqueada.

---

## 11 · Próximos passos, em ordem de dependência

| # | Ação | Depende de | Natureza |
|---|---|---|---|
| 1 | **Decidir se o objeto do P4 é a série anual ou a série bruta** | — | **humana.** Governa Q9/D24, D20–D23 e todo o cálculo de φ₁ e σ² |
| 2 | **Decidir Q1** com o quadro do §3 | (1) | **humana.** Recomendação registrada em §3.4 |
| 3 | **Decidir Q8** com o balanço do §7 | — | **humana.** Recomendação registrada: não migrar |
| 4 | **Executar A7** (Scheffer 2009 + Held & Kleinen 2004) | — | **auditoria.** Virou crítica: é onde vive a resposta a §4.3, e A10-F5 exige distinguir bifurcação de Hopf de sela-nó |
| 5 | Executar **A8** (Usoskin 2017) | — | auditoria. Contexto solar; Q7 |
| 6 | Considerar **A13** (Oláh+2016, `bib/aa28479-16.pdf`) | — | auditoria opcional. Métodos tempo-frequência que os periodogramas perdem (A11b-F5); relevante a D30/Q4 |
| 7 | Decidir Q2 (`ρ CrB`), Q3 (largura de banda), Q4 (44 anos), Q5 (binárias), Q6 (medida do `Flat`), Q7 (subgigantes) | (1)(2) | humanas |
| 8 | Consolidação → `P4_SOURCE_VALUES.md` + `p4_star_catalog.csv` | tudo acima | congelamento |
| 9 | Atualizar o pipeline, num único passe, contra referência congelada | (8) | protocolo §5 regra 5 |

**O pipeline permanece congelado.** Nenhuma linha de código foi tocada nesta rodada.

---

## 12 · Registro de honestidade

Três coisas que esta rodada tornou mais difíceis para o P4, registradas para que não sejam esquecidas na redação:

1. **O teste temporal de CSD não é executável no único caso amostrado** (§5). Comparação de estados, sim; precursor dinâmico, não — com os dados que existem.
2. **A literatura de 2025 afirma que a transição é estocástica e rápida** (§4.3). O contra-argumento do P4 é teórico (biestabilidade), não observacional, e ainda não tem base auditada.
3. **A taxa-base é de 1 a 2 em 10 000** (§4.1). Qualquer proposta de classificador tem de ser avaliada contra esse prior, numericamente.

E uma que ficou mais fácil:

4. **A variável central do P4 foi validada por terceiros.** Luhn+2022 e a CLS VI mostram que a média não discrimina e a variabilidade discrimina — sobre o único análogo confirmado e sobre 710 estrelas. **O P4 não precisa mais defender a escolha do indicador; precisa defender o uso temporal dele.**
