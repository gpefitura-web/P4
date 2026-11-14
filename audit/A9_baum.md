# Audit A9 — Baum, Wright, Luhn & Isaacson 2022, AJ 163, 183

**DOI** 10.3847/1538-3881/ac5683 · *Five Decades of Chromospheric Activity in 59 Sun-like Stars and New Maunder Minimum Candidate HD 166620*

| | |
|---|---|
| **Data** | 2026-08-01 |
| **Método de extração** | (1) camada de texto nativa do PDF via `pdftotext -layout` (PDF gerado por IOPP, texto nativo, não scan); (2) tabelas machine-readable do VizieR `J/AJ/163/183` (arquivos `J:AJ:163:183:table1.tsv`, 62 135 linhas; `J:163:183:table2.tsv`, 59 linhas) — **fonte independente da camada de texto**, com checksums aritméticos exatos entre as duas |
| **Páginas lidas** | 1–9 (íntegra), com atenção a §2.1 (offsets), §2.3–2.6 (seleção), §3–3.1 (classificação e periodogramas), §4.1 (HD 166620), §4.2, Tabelas 1 e 2 e todas as notas de rodapé |
| **Regra dos dois passes** | satisfeita por **texto nativo × tabela VizieR**, e reforçada por **quatro checksums internos exatos** (§"Checks") e por uma **verificação cruzada externa contra Luhn+2022 §2.1** (A10) |

---

## 0 · Identificação dos arquivos `.tsv` da raiz do projeto

Conforme solicitado, o mapeamento arquivo → artigo:

| Arquivo na raiz | Catálogo VizieR | Artigo | Conteúdo | Linhas de dados |
|---|---|---|---|---|
| `J:AJ:163:183:table1.tsv` | `J/AJ/163/183/table1` | **Baum+2022** (A9) | Séries temporais curadas de S-value: HD, Svalue, Time (ano decimal), Inst, Flag | 62 135 |
| `J:163:183:table2.tsv` | `J/AJ/163/183/table2` | **Baum+2022** (A9) | Parâmetros e classificações das 59 estrelas (+ coluna `Nobs` derivada pelo CDS) | 59 |
| `J:ApJ:936:L23:table2.tsv` | `J/ApJ/936/L23/table2` | **Luhn+2022** (A10) | Toda a série S_HK de HD 166620: BJD, Year, SHK, Inst ∈ {MW, new_MW, HIRES} | 1 885 |
| `J:ApJ:936:L23:table3.tsv` | `J/ApJ/936/L23/table3` | **Luhn+2022** (A10) | Fotometria APT T4 de HD 166620: BJD, Year, mag (d−b), Inst | 1 278 |
| `J:ApJS:274:35:table2.tsv` | `J/ApJS/274/35/table2` | **Isaacson+2024, CLS V** (A11b) | 710 estrelas: Smin, Smax, Smed, SSD, Nobs, B−V, logR′_HK, idade, I10, C, Act | 710 |
| `J:ApJS:274:35:table3.tsv` | `J/ApJS/274/35/table3` | **Isaacson+2024, CLS V** (A11b) | Séries temporais S do Keck/HIRES: Name, FileName, BJD, S, SNR, Decker, Seeing | 52 380 |
| `J:ApJS:274:35:table4.tsv` | `J/ApJS/274/35/table4` | **Isaacson+2024, CLS V** (A11b) | 138 ciclos detectados: Amp, Per, Thresh, Peak1, Peak2 | 138 |

**Consequência de arquitetura (registrada como decisão D41):** com esses sete arquivos, as séries estendidas estão disponíveis *localmente e em forma numérica*. O item de ação "Tabela 4 de Egeland" continua bloqueado (IOP), mas o lado **estelar** deixou de depender de rede.

---

## 1 · Valores extraídos

### 1.1 Amostra e proveniência

| Quantidade | Valor | Localização | Grau | Notas |
|---|---|---|---|---|
| Tamanho da amostra final | **59 estrelas** | Resumo; §2.6; Tabela 2 | **A** | 59 linhas exatas na Tabela 2 do VizieR |
| Amostra de partida (Mount Wilson) | 2 326 estrelas | §2.3 | B | "2300 stars" no §2.1 e no Resumo — arredondamento, não contradição |
| Após cruzar com Brewer+2016 | **189 estrelas** | §2.3 | B | corte por disponibilidade de parâmetros espectroscópicos |
| Das 59, também avaliadas em B95 | **26** | §2.3 (fim); §4.2 | **A** | reproduzido: 26 linhas com `ClassB95` preenchida |
| Novas classificações atribuídas | **33** | §4.2 | **A** | 26 + 33 = 59 ✔ |
| Total de observações curadas | **62 135** | Tabela 1 (VizieR) | **A** | soma das 59 linhas de `Nobs` = 62 135, exato |
| Cobertura temporal global | **1966.18 – 2020.19** | Tabela 1 | **A** | calculado da série; §1 diz "1966–present" |
| Fonte dos dados MW | Radick & Pevtsov 2018b/c, Harvard Dataverse (`HK_Project_v1995_NSO` doi:10.7910/DVN/ZRJ6NT; `HK_Project_v2001_NSO` doi:10.7910/DVN/H85QPF) | §2.1.1; Agradecimentos; Refs | **A** | |
| Fonte HIRES-1 (1996–2004) | Wright et al. 2004, ApJS 152, 261 | §2.1.2 | **A** | |
| Fonte HIRES-2 (2004–2010) | Isaacson & Fischer 2010, ApJ 725, 875 | §2.1.3 | **A** | |
| Fonte pós-2010 | novas medidas CPS, mesmos métodos de I&F 2010 | §2.1.4 | **A** | |
| Precisão de longo prazo declarada | **1.2 % (B95)**, verificada por R. Radick em **1 %–2 %** (Radick & Pevtsov 2018a) | §1.2 | **A** | corrobora D14 e a ressalva de Q6 |

### 1.2 Cobertura por instrumento (calculada da Tabela 1, todas as 59 estrelas)

| Instrumento | N obs | Intervalo | N estrelas |
|---|---|---|---|
| HKP-1 | 2 207 | 1966.18 – 1977.57 | 22 |
| HKP-2 | 50 223 | 1977.25 – 2001.77 | 59 |
| HIRES-1 | 1 772 | 1996.53 – 2003.54 | 49 |
| HIRES-2 | 7 933 | 2004.63 – 2020.18 | 59 |

Grau **A** (contagem sobre a tabela machine-readable; consistente com as datas de instrumentação dadas em §1.2 e §1.3).

**Flags na Tabela 1:** `none` 58 880 · `1day` 2 782 · `sigma` 444 · `1day/sigma` 29. Total 62 135. Os 473 pontos com marcador `sigma` foram *rejeitados da análise* de Baum mas **permanecem** na tabela (§2.4) — ou seja, a série "limpa" tem 61 662 pontos.

### 1.3 N por estrela — **o número que a questão Q9 depende**

Duas contagens diferentes, e a distinção é a questão inteira:

| Métrica | mín | mediana | máx | **> 100 pontos** |
|---|---|---|---|---|
| **N observações individuais** (cadência bruta) | 43 | **698** | 4 676 | **56 / 59** |
| **N estações anuais** (anos distintos com ≥1 obs) | 9 | **27** | 54 | **0 / 59** |

Grau **A** (calculado da Tabela 1; `Nobs` do VizieR bate exatamente estrela a estrela — checksum 1).

As três estrelas com N ≤ 100 observações: HD 145958A (84), HD 145958B (76), HD 178911B (43) — as mesmas que §2.3 identifica como tendo parâmetros não-físicos.

Baseline: mín 24 yr, mediana 41 yr, máx 54 yr. Maior lacuna interna por estrela: mediana **7.17 anos**; **42 das 59 estrelas têm lacuna > 5 anos**.

Tabela completa estrela a estrela em **`baum2022_59stars.csv`** (raiz), com `N_obs_total`, `N_obs_limpo`, `N_estacoes_anuais`, `N_HKP1/HKP2/HIRES1/HIRES2`, `t_min`, `t_max`, `maior_lacuna_yr`.

### 1.4 Sistema de classificação de Baum (§3)

Baum separa **sequência principal** de **subgigantes** por gravidade superficial: log g > 4.2 → MS; log g ≤ 4.2 → subgigante (§3, grau **A**).

A avaliação inicial é **feita a olho**, com critérios "loosely based on those used in B95" (§3, textual). Para classificar uma estrela como **cíclica** ela precisa de:

1. variação periódica clara;
2. número significativo de observações;
3. pelo menos dois períodos completos (*preferencialmente*);
4. amplitudes de picos e vales semelhantes e consistentes — caso contrário rotula-se `insuf` ou `var`.

Demais classes (§3, textual):

| Classe Baum | Definição literal | Análogo em Baliunas (A1 §1.3) |
|---|---|---|
| `flat` | "no observed variation in activity" | `Flat` / `Flat?` — mas **sem limiar numérico**; B95 usa σ_S/S < 1–1.5 % |
| `long` | "possible long-term cycle" | `Long` |
| `var` | "clear, nonperiodic variations" | `Var` |
| `insuf` | "insufficient data to make a classification" | **sem análogo em B95** |
| *número* | período estimado em anos | `CYCLE` + grau de FAP |
| *número* + `?` | período **estimado a olho**, não por periodograma | — |

**Diferença metodológica decisiva (A9-F1, abaixo):** B95 grada cada ciclo por *false-alarm probability* (Excellent/Good/Fair/Poor). Baum **não reporta FAP alguma**. O periodograma serve "to assist in classification" (§3.1) e o período é simplesmente o pico de maior potência. Não há teste de significância publicado. Os períodos de Baum são, portanto, **não comparáveis em estatuto** aos de Baliunas.

Nota de rodapé *g* da Tabela 2: "All periods listed are rough estimates, and are estimated only to the precision of one-10th of a year" — mesma convenção de B95.

Distribuição das 59 classificações (`ClassTP`): `flat` 24 · `var` 17 · período numérico 14 · `long` 4 · `insuf` **0**.

### 1.5 Tratamento dos offsets entre instrumentos (§2.1) — **crítico para P4**

Extração literal do que foi feito:

| Junção | O que Baum fez | Estrelas nomeadas | Localização |
|---|---|---|---|
| **HKP-1 → HKP-2** (pré/pós-1977) | "We remedied these offsets by **shifting the median of the pre-1977 measurements to align with the median of the more extensive post-1977 measurements**" | HD 22072, HD 23249, HD 217014 | §2.1.1 |
| **MW → HIRES-1** (Wright+2004) | "we adjusted the Wright et al. (2004) data with a **constant shift** to have a consistent median S-value with the Mount Wilson data set" | HD 3795, HD 10145, HD 65583 | §2.1.2 |
| **MW/HIRES-1 → HIRES-2** (I&F 2010 e posteriores) | "**Fourteen stars** in the post-2010 CPS data showed a clear offset … and were shifted accordingly, **in the same manner**" | **não nomeadas** | §2.1.3 |
| Não corrigidas deliberadamente | "we chose **not** to correct them because the more recent data are sparse enough that the difference could be a **real change in the star's activity level**" | HD 34411, HD 142267 | §2.1.2 |

**Há transformação?** Não. Não há transformação funcional, nem termo de cor, nem escala. **Apenas um deslocamento aditivo constante que alinha medianas.**

**Justificação da fonte:** "These offsets can be explained by the **calibration uncertainty between the very different instruments**" (§2.1.2).

**Incerteza residual: NÃO PUBLICADA.** Baum não reporta (a) o valor de nenhum offset aplicado, (b) a incerteza do offset, (c) a identidade das catorze estrelas de §2.1.3, (d) qualquer estimativa de erro residual. As séries da Tabela 1 contêm **apenas os valores já corrigidos**, sem coluna de offset. **Grau X** para "incerteza residual do offset" — escalado (§5).

Limpeza adicional que também altera a variância: rejeição a **3σ** da média (§2.4), remoção manual de pontos em HD 140144 / HD 1461 / HD 182572, remoção de S = 0.00, e remoção de todas as observações com decker C2 e seeing > 1.″5 (§2.5). Sobre HD 182572 o próprio texto anota "a high density of points at an S-value around 3σ from the mean … a possible activity burst" — pontos removidos da análise.

### 1.6 HD 166620 (§4.1) — parâmetros e transição

| Parâmetro | Valor | Fonte declarada | Grau |
|---|---|---|---|
| T_eff | 4970 K (± 25 K) | Brewer+2016, via Tabela 2 e nota *b* | **A** (bate com Luhn Tabela 1) |
| log g | 4.51 (± 0.028) | idem | **A** |
| v sin i | 0.100 km/s (± 0.7) | idem | **A** — incerteza **maior que o valor** |
| [Fe/H] | −0.16 (± 0.010) | idem | **A** |
| Massa | 0.760 M☉ | idem | **A** (Luhn dá 0.78 M☉ — ver A10) |
| Idade | 12.4 Gyr | idem | **A** |
| Tipo espectral | K2V | SIMBAD | **A** |
| S mediano | 0.185 | Tabela 2, nota *a* | **A** |
| Baseline / cadência | 54 yr / 32.95 obs·yr⁻¹ | Tabela 2 | **A** (checksums 1–3) |
| N observações | 1 766 | VizieR `Nobs` | **A** |
| Classe B95 (por Baum) | `excl-15.8` = FAP Excellent, P = 15.8 yr | Tabela 2, col. 12 | **A** — bate com A1 |
| **Classe Baum** | **`17.0?`** — período 17 yr, **estimado a olho** | Tabela 2, col. 13 | **A** |
| Período pré-transição | **"we estimate the cycle period for this main-sequence star prior to entering a minimum state to be 17 yr"** | §4.1, textual | **B** — "based on our visual analysis and curve-fitting" |
| **Período de rotação** | **não fornecido** por Baum | — | **X** — vem de A10 (Luhn) |

**Descrição da transição (§4.1, literal):** "the star's activity 'turned off' **while there was a gap in data collection and a switch in our data stream from one instrument to another, between the years of 1995 and 2004**." Baum chama a coincidência de "very suspicious" e enumera as verificações feitas: inspeção dos logs de observação do HIRES (nada), e uma reconstrução da posição no céu a partir da hora sideral mediana das observações, calibrada em τ Ceti (HKP-1 erra 52 m, HKP-2 erra 23 m para τ Cet; para HD 166620 as diferenças são 29 m e 1h13m). Conclusão: "a simple transcription error in the star name or routine pointing error is exceedingly unlikely."

**Ressalva que Baum faz contra si mesmo (§4.1, literal):** "The data at face value argue that the grand minimum is not at a lower level than the local minima, which would have strong implications for the nature of magnetic grand minima (they are merely the end of cycling, not a shutdown of the dynamo). **However, some other stars required offsets between instruments, so this conclusion is not robust.**" — Luhn+2022 (A10) é precisamente a resposta a essa ressalva.

**Segundo caso citado no mesmo §4.1:** **HD 101501** teria passado ~10 anos (≈1980–1990) em baixa atividade com pouca variação e depois retornado ao ciclo, **defasada em 180°** em relação ao ciclo original — motivo pelo qual não foi ajustada curva. Classificada `4.2?`. É o único caso na literatura auditada de *saída* de um estado plano.

### 1.7 Estatística do degrau instrumental residual (derivada, não publicada)

Como Baum não publica os offsets, o degrau residual foi **medido** a partir da Tabela 1: diferença entre a mediana de HKP-2 e a mediana de HIRES-2, por estrela, nas 51 estrelas com ≥ 10 pontos em ambos (`a9_instrument_step.csv`, gerado; ver §5).

| Estatística | Valor |
|---|---|
| Δ relativo mediano | **+0.00 %** |
| Δ relativo médio | −0.61 % |
| **Dispersão (σ) dos Δ entre estrelas** | **± 4.47 %** |
| Estrelas com \|Δ\| > 1.2 % (precisão de longo prazo B95) | **25 / 51** |
| Estrelas com \|Δ\| > 5 % | **10 / 51** |
| HD 166620 | **−8.78 %** |
| Maior: HD 4628 | −16.3 % (e Baum a classifica como **ainda cíclica**, `10.0?`) |

Grau **B** (cálculo próprio sobre dados grau A; mistura variação astrofísica real com resíduo instrumental e **não os separa** — é por isso que é um limite superior, não uma medida do erro). Ver achado A9-F6.

---

## 2 · Cruzamento com `baliunas_table2_full.csv`

| Pergunta | Resposta |
|---|---|
| Quantas das 59 estão nas 112 linhas de A1? | **27** por HD |
| Quantas Baum reconhece como estando em B95? | **26** (coluna `ClassB95` preenchida) |
| Discrepância | **HD 185144 (σ Dra)** está no catálogo A1 como `CYCLE` grau A, mas Baum deixa `ClassB95` **em branco** — ver A9-F2 |

As 26 com classe B95 e a comparação classe-a-classe estão em `baum2022_59stars.csv` (colunas `class_B95_por_Baum`, `class_Baum`, `class_A1`, `P_cyc_A1`, `FAP_A1`, `bv_A1`).

**Reclassificações (14 das 26).** Mudam de tipo de classe: HD 100180, 101501, 10780, 115617, 126053, 143761, 182572, 188512, 190406, 217014, 22072, 37394, 3795, 9562 — treze — **mais HD 10700**, cujo `flat?` → `flat` é usado pelo próprio §4.2 como exemplo de reclassificação. Total **14** ✔ (checksum 6).

### 2.1 As candidatas do P4 nas 59 de Baum — **o dado que Q1 esperava**

**Grupo `Flat` limpo (5 estrelas, pós-D13):**

| HD | Em Baum? | N obs | Baseline | Classe B95 | **Classe Baum** |
|---|---|---|---|---|---|
| 43587 | **AUSENTE** | — | — | `Flat?` | — |
| 10700 (τ Cet) | sim | 2 526 | 52 yr | `flat?` | `flat` |
| 190360 | sim | 1 659 | 53 yr | `flat` | `flat` |
| 182572 | sim | 2 161 | 52 yr | `flat` | **`var`** ⚠ |
| 23249 | sim | 1 337 | 52 yr | `flat?` | `flat` |

**Grupo de controle `CYCLE` + FAP Excellent (13 no catálogo A1, incluindo a linha do Sol):**

| HD | P (A1) | B−V | Em Baum? | Classe Baum |
|---|---|---|---|---|
| 4628 | 8.37 ± 0.08 | 0.88 | sim | `10.0?` |
| 10476 | 9.6 ± 0.1 | 0.84 | sim | `10.3` |
| 16160 | 13.2 ± 0.2 | 0.98 | **ausente** | — |
| 26965 | 10.1 ± 0.1 | 0.82 | sim | `9.9` |
| 32147 | 11.1 ± 0.2 | 1.06 | **ausente** | — |
| 81809 | 8.17 ± 0.08 | 0.64 | **ausente** | — |
| 103095 | 7.3 ± 0.08 | 0.75 | **ausente** | — |
| 152391 | 10.9 ± 0.2 | 0.76 | sim | `9.1` |
| 160346 | 7.0 ± 0.08 | 0.96 | **ausente** | — |
| 166620 | 15.8 ± 0.3 | 0.87 | sim | `17.0?` |
| 201091 | 7.3 ± 0.1 | 1.18 | **ausente** | — |
| 219834B | 10.0 ± 0.2 | 0.91 | sim | `9.4` |
| (Sol) | 10.0 ± 0.1 | 0.66 | — | — |

**Resumo:** 4 de 5 `Flat` e 6 de 13 controles `CYCLE` Excellent estão em Baum. Ver A9-F5.

---

## 3 · Verificações realizadas

| # | Verificação | Resultado |
|---|---|---|
| 1 | `Nobs` (Tabela 2 VizieR) × contagem de linhas na Tabela 1, estrela a estrela | **passa exato, 59/59**; somas 62 135 = 62 135 |
| 2 | `Cadence` = `Nobs` / baseline exato (t_max − t_min) | **passa**, máx \|Δ\| = 0.005 obs·yr⁻¹ |
| 3 | `Base` (anos, inteiro) = t_max − t_min | **passa**, é o arredondamento; Δ médio −0.05 yr |
| 4 | §2.3/§4.2: "26 em ambos, 33 novas" = 59 | **passa exato** |
| 5 | Resumo/§6: **"analisamos 29 estrelas com ciclos periódicos"** | **FALHA** — a Tabela 2 tem 14 períodos numéricos; 18 com `long`. Ver A9-F1 |
| 6 | §4.2: "das 26, 14 receberam nova classificação" | **passa** (13 por mudança de tipo + HD 10700 `flat?`→`flat`, que o próprio §4.2 exemplifica) |
| 7 | Contagens por instrumento de HD 166620 × Luhn+2022 §2.1 (fonte externa independente) | **passa exato**: 107 / 1 547 / 9 / 103 |
| 8 | Cruzamento das 59 contra `baliunas_table2_full.csv` | 27 por HD vs 26 declaradas — ver A9-F2 |

---

## 4 · Achados

**A9-F1 · O número "29 estrelas com ciclos periódicos" não é reproduzível da Tabela 2. `X`**
O Resumo e a §6 afirmam "We have analyzed 29 stars with periodic cycles using the Lomb–Scargle periodogram." A Tabela 2 contém **14** estrelas com estimativa numérica de período, e dessas **4 são marcadas `?` — estimadas a olho, não por periodograma** (HD 101501, 166620, 190406, 4628, mais HD 4628; ver `baum2022_cycle_periods.csv`). Somando as 4 `long` chega-se a 18. **Não se chega a 29 por nenhuma combinação das classes publicadas.** Duas leituras possíveis — 29 séries *submetidas* ao periodograma vs 29 ciclos *reportados* — mas o texto diz "analyzed 29 stars with periodic cycles". Registrado como contradição interna, não resolvido (protocolo regra 4). **Consequência prática: o pedido "os 29 períodos de Lomb-Scargle" da unidade não é executável; existem 14, dos quais 10 por periodograma.**

**A9-F2 · HD 185144 (σ Dra): Baum declara ausente de B95; o catálogo A1 a tem. `contradição, grau A dos dois lados`**
`baliunas_table2_full.csv` lista HD 185144 como `CYCLE`, grau A (extração de A1, `n_pass` = 8, confirmada em Fig. 1). Baum deixa a coluna "Baliunas et al. (1995)" em branco para essa estrela, e atribui `6.2` yr. Note que na extração A1 essa linha tem `P_cyc` e `FAP` vazios — isto é, é uma `CYCLE` **sem período nem FAP publicados em B95**, o que provavelmente explica por que Baum a tratou como não classificada. **Não resolvido aqui**; item para a consolidação. Não afeta o congelamento de A1.

**A9-F3 · Todos os períodos que se sobrepõem a Baliunas divergem por ≥ 2 σ do dP publicado por B95. `A`**

| HD | Baliunas | FAP | Baum | Δ | Δ/σ(B95) |
|---|---|---|---|---|---|
| 26965 | 10.1 ± 0.1 | Excellent | 9.9 | −0.2 | **−2.0** |
| 219834B | 10.0 ± 0.2 | Excellent | 9.4 | −0.6 | **−3.0** |
| **166620** | **15.8 ± 0.3** | **Excellent** | **17.0 ?** | +1.2 | **+4.0** |
| 10476 | 9.6 ± 0.1 | Excellent | 10.3 | +0.7 | **+7.0** |
| 152391 | 10.9 ± 0.2 | Excellent | 9.1 | −1.8 | **−9.0** |
| 4628 | 8.37 ± 0.08 | Excellent | 10.0 ? | +1.63 | **+20** |
| 190406 | 2.60 ± 0.02 | Fair | 17.2 ? | +14.6 | (troca de primário) |

Seis dos sete são FAP **Excellent** em B95 — a categoria mais confiável. Duas leituras: (a) o `dP` de Baliunas é um erro de ajuste do periodograma, não uma incerteza realista sobre o período do ciclo; (b) os períodos mudaram genuinamente ao longo de cinco décadas, que é o que Oláh+2009 afirma e o que Baum endossa em §3.1 ("many of the stars appear to have a cycle that changes over time"). **As duas são compatíveis e nenhuma é decidida aqui.** Registrado ao lado, não fundido (D15/D36).
**Consequência para P4:** qualquer teste que trate P_cyc de B95 como quantidade com barra de erro de 1 % está mal calibrado. Isto reforça D15.

**A9-F4 · HD 190406 confirma D10 pelo lado oposto. `A`**
B95 dá primário 2.60 ± 0.02 (Fair) e secundário 16.9 (Good). Baum transcreve corretamente (`fair-2.6+good-16.9`) e atribui **17.2 ?** — isto é, **promove o secundário a primário**. D10 (coluna 7 = primário) continua correta como leitura de B95; mas a leitura *física* de 2026 é que o ciclo dominante é o de ~17 anos. Divergência registrada.

**A9-F5 · A extensão de Baum é fortemente não-uniforme entre os grupos candidatos do P4. `A`**
`Flat` limpo: 4/5 presentes. Controles `CYCLE` Excellent: 6/13 presentes — e os sete ausentes são sistematicamente os **mais vermelhos** (16160 B−V = 0.98, 32147 = 1.06, 160346 = 0.96, 201091 = 1.18) ou binários (81809), porque a CPS "notably omits very active stars" e seleciona alvos de planeta (§1.3). **Se o P4 usar séries de Baum, N passa a ser correlacionado com grupo — exatamente o confundimento que D12 declarou impossível por construção sob Baliunas-apenas.** D12 permanece válida *para o catálogo Baliunas*; ela **não** se estende ao subconjunto Baum. Este é o preço da extensão e tem de entrar em Q1 explicitamente.

**A9-F6 · O degrau residual entre HKP-2 e HIRES-2 é da ordem de ± 4.5 %, ~4× a precisão de longo prazo. `B`**
Ver §1.7. Como Baum não publica offsets nem incertezas, o resíduo instrumental e a variação astrofísica são **inseparáveis com os dados publicados**. O valor de HD 166620 (−8.8 %) está dentro da faixa observada em estrelas que Baum classifica como **ainda cíclicas** (HD 4628, −16.3 %). Isto **não** desmente a transição de HD 166620 — A10 a estabelece por outra via — mas significa que **a estatística "diferença de nível entre instrumentos" sozinha não é diagnóstica**, e que um φ₁ ou σ² calculado sobre a junção HKP-2/HIRES-2 sem tratamento carrega um degrau de vários por cento. **Consequência direta para P4:** o indicador de variância não pode atravessar a junção 2001→2004 sem uma decisão explícita.

**A9-F7 · Baum não publica FAP nem qualquer medida de significância dos períodos. `A`**
§3.1: o período é "that which had the most power in the periodogram"; o ajuste senoidal serve para "verify", mas "This could not always produce a good fit because stellar activity variation is not strictly periodic". Não há teste de hipótese, nem nível de confiança. Os períodos de Baum são grau **B** por leitura limpa, e **não podem ser tratados como equivalentes** a `CYCLE` FAP Excellent de B95.

**A9-F8 · Baum endossa a explicação evolutiva concorrente. `A`**
§1.3 e §5.5: Wright (2004) "showed that the low-activity flat stars were all subgiants, and **we see hints of this in our own analysis as well**, but our sample of subgiants is small. The subgiants we did study exhibit the lowest activity levels, with consistently lower log⟨S⟩ than main-sequence stars." §1.3 registra também a preocupação de Wright (2004) com "the (mis)identification by Baliunas & Jastrow (1990) of low-activity stars as Maunder minimum candidates **on the basis of their low activity levels**". **Isto é Q7, e vem de dentro da fonte que estende a série.** Ver também A11.

**A9-F9 · Recomendação de cadência publicada. `B`**
§5.2: "A cadence of about **10 observations per year is ideal**." Útil como referência citável para justificar a média anual (D08). 39 das 59 estrelas superam 10 obs/yr.

**A9-F10 · A limpeza de Baum remove precisamente o tipo de evento que P4 mede. `A`**
Rejeição a 3σ (§2.4) + remoção manual + corte por seeing (§2.5). O próprio texto reconhece: "our sigma-clipping outlier rejection may have removed possible activity peaks or stellar flares … we are interested in the curated time series to identify low-frequency long-term changes in activity, so the rejection of flares is not of concern to us." Para um estudo de **variância** isso não é inócuo: 473 pontos (0.76 %) foram removidos, concentrados nas estrelas mais variáveis. Os pontos permanecem na Tabela 1 com a flag `sigma`, logo **a decisão de reinclui-los é reversível** — e deve ser tomada explicitamente.

---

## 5 · Q9 — DFA volta a ser admissível? **Reportado, não decidido**

Conforme instrução da unidade (protocolo §1; "não reabrir D24 por conta própria"), registra-se apenas o número e devolve-se a questão ao status Q.

**O fato:** a resposta depende inteiramente de **qual série** o P4 usa.

| Série | N por estrela | Contra o piso de > 100 pontos (A4-F4 / A5-F5) |
|---|---|---|
| Médias anuais (convenção D08) | mediana **27** (mín 9, máx 54) | **abaixo do piso, fator ~4** — igual a Baliunas |
| Cadência bruta de Baum | mediana **698** (56/59 acima de 100) | **acima do piso, fator ~7** |

**Três observações que a decisão humana precisa ter à mão, todas grau A:**

1. **A cadência bruta é irregular.** Peng+1994 (A5) define DFA sobre uma série **igualmente espaçada**; a Tabela 1 tem lacunas internas de mediana 7.17 anos e 42 das 59 estrelas têm lacuna > 5 anos. Interpolar para grade regular introduz correlação artificial — exatamente o viés que α mede. O piso de 100 pontos de A4/A5 pressupõe amostragem regular; **N = 698 pontos irregulares não é o mesmo objeto que N = 698 pontos regulares.**
2. **A cadência bruta é dominada pela modulação rotacional** (P_rot ≈ 45 d em HD 166620, A10), que é ruído para a escala de ciclo, e por sazonalidade observacional. O expoente α numa banda de escalas de dias-a-meses não é o mesmo α da banda de anos-a-décadas — D26 já obriga a checagem de crossover.
3. **A junção instrumental (A9-F6) injeta um degrau** que, num integrando cumulativo, aparece como tendência — e DFA é definida sobre a soma cumulativa.

**Q9 permanece aberta.** A questão que o pesquisador precisa responder é anterior a "DFA sim ou não": **é a série anual ou a série bruta o objeto do P4?** D08 diz anual. Se D08 for mantida, D24 não muda e Q9 fecha de novo sem nova decisão. Se D08 for revogada, muda também D20–D23 e o cálculo de φ₁ e σ².

---

## 6 · Disponibilidade machine-readable

| Item | Estado | Localização |
|---|---|---|
| Tabela 1 (séries S, 59 estrelas) | **OBTIDA** | `J:AJ:163:183:table1.tsv` (raiz) · VizieR `J/AJ/163/183/table1` · doi:10.26093/cds/vizier.51630183 |
| Tabela 2 (parâmetros e classificações) | **OBTIDA** | `J:163:183:table2.tsv` (raiz) |
| Figure set (59 imagens) | não obtido | IOP, "available in the online journal" — **não necessário**; a informação está nas tabelas |
| Dados MW originais | não obtidos | Harvard Dataverse doi:10.7910/DVN/ZRJ6NT e /H85QPF — **item de ação**, domínio bloqueado; relevante apenas se se quiser auditar os offsets de Baum por conta própria (ver A9-F6) |

Nenhum item necessário à unidade ficou grau X por falta de acesso.

---

## 7 · Decisões tomadas, com base

1. **Os `.tsv` da raiz são identificados e passam a ser a fonte numérica primária das séries estendidas** — base: §0 desta unidade; VizieR bate com o texto nativo por quatro checksums exatos. *(→ D41)*
2. **Os períodos de Baum são registrados ao lado dos de Baliunas e de Saar, nunca fundidos** — base: D15, D36, A9-F3, A9-F7. Ficam em `baum2022_cycle_periods.csv` com a coluna `metodo_baum` distinguindo periodograma de estimativa a olho. *(→ D42)*
3. **As classificações de Baum entram como camada época-dependente, não como correção de A1** — base: D34 estendida do caso HD 166620 a todas as 26 estrelas em comum. O catálogo A1 permanece congelado. *(→ D43)*
4. **A incerteza residual dos offsets instrumentais de Baum é grau X e a junção 2001→2004 é tratada como descontinuidade declarada** — base: §1.5, A9-F6. *(→ D44)*
5. **A não-uniformidade da extensão entre grupos (A9-F5) entra em Q1 como custo explícito** — base: A9-F5; D12 não se estende ao subconjunto Baum. *(→ subsídio de Q1)*

---

## 8 · Não resolvido (grau C ou X)

| Quantidade | Por que não resolvido | Resolução proposta |
|---|---|---|
| **Incerteza residual dos offsets** entre os quatro instrumentos | **X** — não publicada. Nem os valores dos offsets, nem as 14 estrelas de §2.1.3 | (a) tratar a junção como descontinuidade e nunca deixar uma janela deslizante atravessá-la; (b) recalcular offsets a partir do Dataverse (bloqueado); (c) restringir o P4 à era HKP-2, onde não há junção. **Decisão humana.** |
| **"29 estrelas com ciclos periódicos"** (A9-F1) | **X** — contradiz a própria Tabela 2 | citar "14 estimativas de período, 10 por periodograma" e não repetir o número 29; ou consultar os autores |
| **HD 185144 em B95 ou não** (A9-F2) | **X** — duas fontes grau A discordam | resolver na consolidação relendo a linha de B95; não afeta A1 |
| Identidade das 14 estrelas com offset pós-2010 | **X** | não publicada |
| **P_rot das 59 estrelas** | **X** em Baum | vem de A10 para HD 166620; para as demais, fora do escopo auditado |
| Separação entre degrau instrumental e variação astrofísica (A9-F6) | **C** — o cálculo mistura as duas | irredutível com os dados publicados; declarar como limitação |

---

## 9 · Produtos desta unidade

- `baum2022_59stars.csv` (raiz) — 59 linhas × 33 colunas: parâmetros, N por instrumento, N de estações anuais, baseline, lacuna máxima, classificações Baum e B95, cruzamento com A1, grau.
- `baum2022_cycle_periods.csv` (raiz) — 14 períodos, com método (periodograma vs a olho), comparação com Baliunas e Δ/σ.
- `audit/a9_instrument_step.csv` — degrau HKP-2 → HIRES-2 por estrela (51 estrelas).
