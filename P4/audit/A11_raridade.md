# Audit A11 — Contexto de raridade e amostras modernas

Três fontes, tratadas em (a), (b), (c).

| | |
|---|---|
| **Data** | 2026-08-01 |
| **Método de extração** | texto nativo (`pdftotext -layout`) de três PDFs em `bib/`, mais as tabelas machine-readable VizieR `J/ApJS/274/35` para (b). Segundo passe: recontagem aritmética sobre as tabelas do CDS contra os totais declarados no texto |
| **PDFs** | `bib/aa54111-25.pdf` · `bib/Isaacson_2024_ApJS_274_35.pdf` · `bib/Isaacson_2025_AJ_170_181.pdf` |

**Identificação do arquivo:** `Isaacson_2025_AJ_170_181.pdf` **é** a CLS VI (AJ 170, 181, 2025; DOI 10.3847/1538-3881/adf2a8). O DOI dado no prompt está correto e corresponde a este arquivo.

---

# (a) Järvinen & Strassmeier 2025, A&A 698, A93 — *A search for Maunder-minimum candidate stars*

**Esta é a fonte que responde Q7 e a que mais desafia a tese do P4.**

## a.1 · Valores extraídos

| Quantidade | Valor | Localização | Grau |
|---|---|---|---|
| Indicador usado | **fluxo relativo nos núcleos do tripleto infravermelho de Ca II (IRT)**, λ8498/8542/8662, convertido em fluxo de linha absoluto | Resumo; §3 | **A** |
| Levantamento base | **RAVE**, DR6 | §2 | **A** |
| Seleção de anãs | log g ≥ 4.0 (DR6), S/N > 15 | §2 | **A** |
| Amostra de anãs bona fide | **78 111** estrelas | Resumo; §2; §4 | **A** |
| Amostra de alta resolução para correção | **123** estrelas STELLA + PEPSI | Resumo | **A** |
| Viés de resolução do RAVE | fluxos RAVE mais **altos** que STELLA/PEPSI em média **19 % (IRT-1), 21 % (IRT-2), 25 % (IRT-3)** | Resumo | **A** |
| Faixa de metalicidade coberta | [Fe/H] de **−1.5 a +0.5** dex | Resumo | **A** |
| **Efeito da metalicidade** | dependência forte, quantificada em **no máximo ±14 %** na faixa B−V 0.53–0.73 | Resumo | **A** |
| Efeito de não corrigir | "practically **all** very-low-activity RAVE dwarfs show a **super-solar metallicity**" — artefato | Resumo | **A** |
| Amostra final (F8–G8 de sequência principal, B−V 0.53–0.73) | **13 326** | Resumo; §6 | **A** |
| Alvos abaixo do limite empírico | **13** (= **0.1 %**) | Resumo; §6; Tabela 2 | **A** |
| Destes, **evoluídos** por paralaxe Gaia DR3 | **11** | Resumo; §6 | **A** |
| **Candidatas finais** | **2**: TIC 352227373 (G2V) e TYC 7560-477-1 (G7V) | Resumo; §6 | **A** |
| Luminosidades das duas | 0.98 e ≈1 L☉; T_eff 5786 K e 5509 K | §5.5 | **B** |
| Incerteza dessas luminosidades | "**≈10–20 %**", dominada por T_eff e correção de absorção interestelar | §5.5 | **A** |
| Nível de atividade do corte | para B−V solar, **log R_IRT = −4.13**, ≈ **20 % abaixo do valor de mínimo solar de fim de 2016** | Resumo | **A** |

**Critério de identificação (§5.4, Fig. 7):** define-se um **limite inferior empírico** de fluxo IRT-1 corrigido por resolução, ajustado em função de B−V a partir da amostra de alta resolução; alvos que caem **abaixo do limite 1σ original** desse envelope, após correção de metalicidade, são candidatos. Não há critério temporal — é uma seleção **de época única**, por nível instantâneo. Grau **A**.

**Etapas do funil, na ordem:** 78 111 anãs (S/N > 15) → correção de resolução → correção de metalicidade → recorte a B−V 0.53–0.73 e F8–G8 de sequência principal → 13 326 → 13 abaixo do limite → paralaxes Gaia DR3 → **2**.

## a.2 · Afirmações textuais sobre raridade e previsibilidade — **registro literal**

Estas são as sentenças que o P4 tem de engajar. Reproduzidas na íntegra, com localização.

> **§6 (Conclusões):** "The small number of very-low-activity stars from our metallicity-corrected Ca II IRT flux sample in Fig. 7, 13 candidates out of the 13 326 main-sequence F8–G8 targets, indicates that **stars in a Maunder-like minimum must be very rare**. This means that **at most ≈0.1 % of the main-sequence stars in the B–V range of ±0.1 of the Sun show levels of magnetic activity significantly (≈20 %) below solar minimum**. Even more devastatingly, **11 of these 13 stars have Gaia DR3 parallaxes and visual brightnesses that identify them as evolved stars rather than main-sequence dwarfs.**"

> **Resumo:** "**Contrary to the initial suggestion from the Mount-Wilson H&K Survey, we conclude that such stars are very rare.**"

> **§1 (Introdução) — a afirmação sobre previsibilidade:** "A major observational problem with the validation of a successful cycle forecast is that **it takes many decades to observe the cycle if only the Sun is used as a benchmark**. Furthermore, **it is still not clear whether the same processes that produce cycle-to-cycle fluctuations also sometimes bring down the activity levels to produce grand minima episodes such as the Maunder minimum**."

> **§1 — sobre as "flat stars" de Mount Wilson:** "The Mount Wilson Observatory (MWO) H&K survey revealed a significant number of solar-type stars with chromospheric emission-line fluxes smaller than even the Sun's in its activity minimum but without cyclic variations (so called 'flat' stars; Baliunas et al. 1995). Some of these stars were interpreted as being in a MM-like state and numerous questions were raised… However, **further studies have shown that almost all of these flat stars were in fact older sub-giants** (Wright …)."

**Leitura para o P4 — importante ser preciso aqui.** A frase publicada **não é** "grandes mínimos são imprevisíveis". A afirmação epistêmica exata é mais fraca e mais precisa: *não se sabe se o mecanismo que produz flutuação ciclo-a-ciclo é o mesmo que produz grandes mínimos*. Isto **não fecha** a porta ao P4 — abre-a, porque é exatamente uma questão de mecanismo que um teste de precursor dinâmico poderia informar. O que o P4 **não pode** fazer é afirmar que a literatura considera grandes mínimos previsíveis: não considera, e a citação de raridade (0.1 %, e ~0.015 % se descontados os evoluídos) tem de aparecer na Discussion.

**A afirmação forte de estocasticidade não está aqui — está na CLS VI, item (c).**

## a.3 · Achados

**A11a-F1 · A raridade medida é ~0.1 % *antes* do corte evolutivo, e ~2/13 326 = 0.015 % *depois*. `A`**
Se o P4 propuser que um subconjunto identificável de estrelas está a caminho de um grande mínimo, a taxa-base publicada é **de uma a duas em dez mil**. Qualquer classificador com falso-positivo não desprezível produz mais falsos que verdadeiros nessa taxa-base. **Isto é uma objeção de prior, não de método, e tem de ser respondida numericamente.**

**A11a-F2 · A seleção de Järvinen & Strassmeier é de nível instantâneo — exatamente o critério que Luhn+2022 declara inválido. `contradição metodológica, ambas grau A`**
Järvinen & Strassmeier selecionam por fluxo IRT baixo numa época. Luhn+2022 (A10 §1.3): "an anomalously low mean or instantaneous activity levels are **not a good diagnostic or criterion** for identifying additional Maunder minimum candidates", tendo mostrado no único análogo confirmado que ⟨S_HK⟩ no grande mínimo (0.171) **não é significativamente menor** que no mínimo de ciclo (0.172). **HD 166620 não seria selecionada pelo critério de Järvinen & Strassmeier.**
**Consequência:** o número "≈0.1 %" é a taxa de estrelas **anomalamente fracas**, não a taxa de estrelas **em grande mínimo**. As duas quantidades foram identificadas na literatura antiga e desidentificadas por Luhn+2022. **A raridade continua a valer como objeção**, mas o P4 pode — e deve — apontar que a busca por nível não mede a quantidade que o P4 discute, e que uma busca por *variabilidade* ainda não foi feita em escala de levantamento. **Este é o espaço argumentativo do P4 e é defensável com duas fontes grau A.**

**A11a-F3 · Corrobora Q7 (subgigantes) de fonte independente. `A`**
"almost all of these flat stars were in fact older sub-giants" (§1) e 11 de 13 candidatas eliminadas por serem evoluídas (§6). Combinado com A9-F8 (Baum: "the subgiants we did study exhibit the lowest activity levels") e com Wright (2004), são **três** fontes independentes. **Q7 deixa de ser uma preocupação interna e passa a ser uma objeção publicada que o manuscrito tem de neutralizar por construção da amostra, não por argumento.**

**A11a-F4 · A metalicidade produz um artefato do tamanho do efeito procurado. `A`**
±14 % em B−V 0.53–0.73, e sem correção "practically all very-low-activity dwarfs show super-solar metallicity". O P4 usa S de Mount Wilson, não IRT, mas o mecanismo (blanketing na janela de contínuo) é o mesmo em espécie. **Nem A1 nem A6 registraram [Fe/H] para a amostra P4.** Item de ação: os [Fe/H] estão disponíveis em `baum2022_59stars.csv` (Brewer+2016, ±0.010) para 59 estrelas e em `J:ApJS:274:35:table2.tsv` para 710. Ver também A10 §1.5: log R′_HK de HD 166620 muda de −5.03 para **−5.07** ao corrigir por metalicidade (Saar & Testa 2012) — 0.04 dex, ~10 %.

---

# (b) Isaacson et al. 2024, ApJS 274, 35 — *California Legacy Survey V*

## b.1 · Valores extraídos

| Quantidade | Valor | Localização | Grau |
|---|---|---|---|
| Amostra | **710** estrelas da vizinhança solar, 20 anos de espectroscopia Keck/HIRES | Resumo | **A** |
| Observações retidas | **52 372** S-values, 2005 – out/2023 | Resumo; §2 item 5 | **A** (VizieR T3 tem 52 380 linhas; Δ = 8) |
| Dados **excluídos** | S-values do Lick; **todos os HIRES pré-2005**; APF (sem baseline adicional) | §2 | **A** |
| Critério de "bem amostrada" | **≥ 45 observações desde 2005** | §2; §5.6 | **A** |
| Justificação do critério | busca de ciclos de **2 a 25 yr**; "Stars with fewer, often sporadically timed, observations are insufficient for robustly detecting activity cycles" | §2 | **A** |
| Estrelas buscadas por ciclo | **285** | Resumo; §2 | **A** (recontagem VizieR com Nobs ≥ 45 dá 290; Δ = 5, cortes adicionais de §2) |
| **Estrelas com ciclo detectado** | **138** | Resumo; Tabela 4 | **A** — Tabela 4 do VizieR tem 138 linhas exatas |
| Estrelas só na análise de média | 425 (mín. 5 medidas) | §2 | **A** |
| Piso de busca | não se busca ciclo se rms de S < **0.002** | §5.7 | **A** |

**Nota importante para o P4:** ao **excluir todo o HIRES pré-2005 e o Lick**, a CLS V é uma série de **~19 anos**, não de cinco décadas. Ela **não** substitui Baum; é complementar e mais homogênea (um único detector, HIRES-2).

## b.2 · Dispersões relativas — o número que Q6 precisa

| Estrela / referência | Dispersão relativa de S | Localização | Grau |
|---|---|---|---|
| **HD 10700 (τ Cet)**, CLS V, baseline estendido | **0.75 %** = 0.00125 / 0.1674 | §5.6 | **A** (texto) / ver nota |
| HD 10700, Isaacson & Fischer 2010 | **1 %** — usada então como incerteza sistemática | §5.6 | **A** |
| HD 10700, Gomes da Silva et al. 2021 (HARPS-AMBRE) | **0.83 %** | §5.6 | **A** |
| HD 10700, medida em §2 com extração restrita | **0.82 %** | §2 | **A** |
| **HD 55575**, a menos ativa com ≥ 45 obs | **0.45 %** = 0.0007 / 0.1562 | §5.6 | **A** |

*Nota de segundo passe:* a Tabela 2 do VizieR dá para HD 10700 `SSD = 0.00121`, `Smed = 0.1674` → **0.723 %**; o texto diz 0.00125 → 0.75 %. Divergência de 3 % no terceiro dígito entre o texto do artigo e a sua própria tabela publicada. **Grau B** para o valor exato; grau **A** para "≈0.75 %". Consequência aritmética: ver A11b-F1.

**Comparação obrigatória, pedida pela unidade:**

| Referência | Valor | Origem |
|---|---|---|
| Piso instrumental HIRES/Keck moderno | **0.45 %** (HD 55575) | A11b, §5.6 |
| Piso instrumental estimado em A2-F6 | **0.8 %** | A2 |
| τ Cet, medido com baseline moderno | **0.72–0.83 %** | A11b; Gomes da Silva 2021 |
| Precisão de longo prazo de Mount Wilson (D14) | **1.2 %** (13 padrões) / **1.4 %** (17 padrões) | A6, Baliunas Tabela 1 |
| Idem, verificada por Radick | **1 %–2 %** | Baum §1.2 (A9) |
| **Limiar de "flat" de Baliunas** | **σ_S/S < 1–1.5 %** | A1 §1.3 |

**Leitura:** o piso instrumental moderno (0.45 %) está **três vezes abaixo** do limiar `Flat` de Baliunas (1–1.5 %) e **2.7×** abaixo da precisão de longo prazo de Mount Wilson (1.2 %). Isto **não resolve Q6 para o catálogo Baliunas** — a definição `Flat` continua a viver dentro do erro de medida dos dados de 1995 — mas mostra que **a questão é resolvível com dados modernos**: uma estrela `Flat` de Baliunas pode hoje ser medida a 0.45 % e a classificação, testada. Das cinco `Flat` limpas do P4, **quatro têm medida na CLS V** (ver b.3). **Isto é o subsídio mais concreto que Q6 já recebeu.**

## b.3 · As candidatas do P4 na CLS V

| HD | S mediano | σ_S | **σ_S/S** | N | B−V | log R′_HK | Ciclo detectado (Tabela 4) | Menos disperso que τ Cet? |
|---|---|---|---|---|---|---|---|---|
| 10700 (τ Cet) | 0.1674 | 0.00121 | **0.72 %** | 944 | 0.664 | −4.958 | **não** | — |
| 23249 | 0.1361 | 0.00117 | **0.86 %** | 75 | 0.882 | −5.178 | **não** | **sim** |
| 190360 | 0.1460 | 0.00139 | **0.95 %** | 280 | 0.725 | −5.105 | **não** | não |
| **166620** | 0.1706 | 0.00190 | **1.11 %** | 149 | 0.827 | −5.002 | **não** | não |
| 115617 | 0.1698 | 0.00191 | **1.12 %** | 609 | 0.680 | −4.951 | **não** | não |
| 182572 | 0.1673 | 0.00250 | **1.49 %** | 80 | 0.728 | −4.981 | **não** | não |
| 3651 | 0.1665 | 0.00665 | 3.99 % | 157 | 0.829 | −5.020 | não | não |
| 10476 | 0.1926 | 0.00798 | 4.14 % | 180 | 0.801 | −4.905 | **9.11 yr** | não |
| 4915 | 0.1887 | 0.01108 | 5.87 % | 98 | 0.632 | −4.838 | **4.86 yr** | não |
| 32147 | 0.2598 | 0.02310 | 8.89 % | 625 | 0.993 | −4.905 | — | não |
| 43587 | **ausente** | | | | | | | |
| 160346 | **ausente** | | | | | | | |

Grau **A** (tabela machine-readable). Todas as quatro `Flat` presentes têm σ_S/S entre 0.72 % e 1.49 % — isto é, **dentro ou logo acima da faixa 1–1.5 % que define `Flat` em Baliunas**, medida agora com um piso instrumental de 0.45 %. **Nenhuma tem ciclo detectado.** A classificação `Flat` de 1995 sobrevive ao teste moderno para 10700, 23249, 190360; **HD 182572 (1.49 %) fica na fronteira**, o que é coerente com Baum tê-la reclassificado como `var` (A9 §2.1).

**Lista das 48–50 menos dispersas → `isaacson2024_least_active_50.csv` (raiz).** Ver A11b-F1 quanto ao número.

## b.4 · Achados

**A11b-F1 · "Cinquenta estrelas têm σ_S menor que HD 10700" não é reproduzível da tabela publicada. `C`**
§5.6: "**Fifty stars** have a smaller S-value standard deviation than HD 10700 and should be considered the least active well-sampled (45 observations or more) stars in our sample (Table 2)." Recontagem sobre `J/ApJS/274/35/table2`: com `SSD < 0.00121` (valor tabelado para HD 10700) e `Nobs ≥ 45` → **48** estrelas. Com o limiar `SSD < 0.00125` que o texto usa → **52**. Nenhum dos dois dá 50. A discrepância vem inteiramente da inconsistência 0.00121 vs 0.00125 entre a tabela e o texto do mesmo artigo. **O CSV entregue usa o critério reproduzível (SSD < 0.00121 tabelado, Nobs ≥ 45) e contém 48 linhas**, com o critério documentado na própria coluna `fonte`. Registrado, não resolvido.

**A11b-F2 · Terceira contagem independente dos ciclos de Baum+2022 — e não é 29. `A`**
§4.2.2: "We cross-check the **13 cycles from 59 stars** examined in Baum et al. (2022), adding two years of HIRES data, and find **10 of the 13** cycles. Of those not detected, **HD 166620 is in the well-studied minimum phase of its cycle** (Luhn et al. 2022), while **HD 101501 and HD 152391 have fewer than 45 observations**."
Isaacson é **co-autor de Baum+2022** e conta **13** ciclos. A extração A9 da Tabela 2 conta **14** períodos numéricos. O Resumo de Baum diz **29**. **A11b-F2 confirma A9-F1 de fonte praticamente interna: o número 29 do Resumo de Baum não corresponde ao conteúdo do artigo.** O manuscrito do P4 deve citar "13–14 ciclos" e nunca 29.

**A11b-F3 · HD 4915 tem dois ciclos, e o longo está subindo — a candidatura a mínimo de Maunder está desfeita. `A`**
§5.6, literal: "HD 4915 is a candidate star in a Maunder minimum–like state (Shah et al. 2018), but **our extended time baseline shows two cycles. One periodicity is at 4.9 yr, and the second is more than 40 yr, and the longer-period cycle is now turning higher.** We detect the 4.9 yr period but cannot limit the period of the second cycle with Keck data alone." Tabela 4: P = **4.86 yr**, amplitude 0.2046. Ver A10-F3. **Contradiz Shah+2018 e a nota 8 de Luhn+2022.**

**A11b-F4 · HD 166620 corroborada como o único caso convincente. `A`**
§5.6: "**HD 166620 is the most convincing to have strong evidence in favor of being a Maunder minimum–like star** (Baum et al. 2022; Luhn et al. 2022), and it continues to show very low variation in our extended time series." σ_S/S = 1.11 % em 149 observações independentes do Keck, 2005–2023.

**A11b-F5 · Múltiplos ciclos são a regra, não a exceção — e o método de detecção é o fator limitante. `A`**
§5.5: HD 22049, HD 32147, HD 4915, HD 219234, HD 4628, HD 45184, HD 100180, HD 201091, HD 201092, HD 18803, HD 219834B "all show evidence of a second cycle", e "our search method does not recover **any** of the known occurrences… The shorter of the cycles is typically not represented well by a sinusoid, so our **nondetections are limited by our search method not our data quality**."
**Consequência direta para D30 e Q4 (a componente solar de 44 anos):** a existência de uma segunda componente longa, quase degenerada com uma tendência monótona, é o caso **típico**, não uma peculiaridade solar. Isso fortalece a obrigação de Methods em D30 e transforma Q4 numa questão genérica do método, não numa idiossincrasia do Sol.

---

# (c) Isaacson, Kane, Carter & Howard 2025, AJ 170, 181 — *California Legacy Survey VI: The Fate of Activity Cycles in Sun-like Stars*

**Esta é a fonte que compete mais diretamente com o P4 — e que, ao mesmo tempo, valida a sua variável.**

## c.1 · A explicação concorrente: *aged out*

| Quantidade | Valor / afirmação | Localização | Grau |
|---|---|---|---|
| Amostra | FGK de sequência principal **mais velhas que o Sol**, em bins de massa 0.7–1.1 M☉ | Resumo; §3 | **A** |
| Métrica central | **S-STD** — desvio-padrão da série temporal de S | Resumo; §3 | **A** |
| Formulação da hipótese concorrente | "…whether any of these properties can differentiate the cycling stars from **noncycling stars that may have aged out of their cycles**" | §3.3 | **A** |
| Limiar de atividade | log R′_HK = **−4.90** separa o regime bem-comportado do regime esporádico | Resumo; §4 | **A** |

**A afirmação central do artigo (Resumo, literal):** "We present evidence that **the average chromospheric activity remains nearly constant while the variation in a star's activity decreases by an order of magnitude**. Measurable changes to the stellar dynamo are suggested that are **not strongly correlated with the average stellar activity, but instead correlated with the amplitude of activity variations** for stars beyond the age of the Sun."

**Como a hipótese *aged out* compete com a bifurcação do P4.** Ambas explicam a mesma observação — estrelas velhas que não ciclam e têm variabilidade baixa. A diferença é a **estrutura temporal**:

| | *Aged out* (CLS VI) | Bifurcação / CSD (P4) |
|---|---|---|
| Natureza | monotônica, irreversível, escala evolutiva | reversível, escala de décadas |
| Precursor | nenhum; o ciclo simplesmente cai abaixo da detecção | φ₁ e σ² crescem antes da transição |
| Retorno ao ciclo | não previsto | previsto |
| Preditor | idade / rotação / log g | dinâmica da própria série |

**O discriminante empírico está identificado e é acessível:** HD 101501 (A9 §1.6) — dez anos de estado plano seguidos de retorno ao ciclo, **defasado em 180°**. Uma estrela que sai do estado plano **falsifica** *aged out* para aquele caso. **É o único exemplo conhecido e está na amostra de Baum, com 2 239 observações e 49 anos de baseline.** A CLS VI reconhece a lacuna: "Whether or not stars reach a noncycling level that is inescapable or **if they can begin cycling again** will require additional observations of these already well-observed stars" (§4). *(Item de consolidação: HD 101501 pode ser o caso de teste do P4, não HD 166620.)*

## c.2 · A afirmação de estocasticidade — **registro literal, é o desafio central a Q7**

> **§3.3.1:** "**The mechanisms that cause a star to enter and exit a magnetic minimum requires a stochastic process that is poorly understood.** We do have one example in HD 166620 and we know that inclination angle also plays a role in cycle detection."

> **§3.3 (bin 0.9–1.0 M☉):** "a gap in S-STD vertically separates the cycling and noncycling stars (with two exceptions) and is **suggestive of a rapid (on stellar timescales) transition from a cycling state to a noncycling state** … we have evidence that these **transitions can occur quickly, on order of years**."

> **§3.3 (bin 1.0–1.1 M☉):** "The pileup of stars near an S-STD value of 0.01 that is not present in any other mass bin, may reveal a change in the stellar dynamo in this mass bin that happens over astrophysically short timescales. **Or if stars move between cycling and noncycling phases, perhaps a stochastic mechanism requires a bimodal distribution of S-STDs.**"

**Leitura honesta para o P4 — não há como suavizar isto.** "Estocástico" e "rápido, na ordem de anos" são, juntos, a objeção mais séria a um precursor de CSD:
- **CSD exige que o sistema se aproxime da bifurcação lentamente em relação à amostragem.** Uma transição "on order of years" com amostragem anual não deixa janela de aproximação. Isto é a mesma conclusão que A10-F2 alcançou empiricamente em HD 166620 — a partir do único caso amostrado — e agora aparece como afirmação populacional independente.
- **A distribuição bimodal de S-STD** que a CLS VI descreve é o que se esperaria de um sistema **biestável** — o que é, na verdade, *compatível* com um quadro de bifurcação. Biestabilidade e estocasticidade não são a mesma coisa: um sistema biestável forçado por ruído tem transições que parecem estocásticas mas ainda exibem CSD, porque a barreira de potencial encolhe antes do salto. **Este é o contra-argumento disponível ao P4, e é legítimo** — mas é um argumento teórico, não uma observação, e exige apoio em A7 (Scheffer, Held & Kleinen).

## c.3 · Achados de estrutura de amostra

**A lista de menos ativas (§3.9, literal):** cruzando a CLS1 com a lista de imageamento da NASA ExEP (Mamajek & Stapelfeldt 2024), com log R′_HK < −4.90 e **sem ciclo** em Isaacson+2024:
**HD 10700 (τ Ceti), HD 110897, HD 115617, HD 136352, HD 166620, HD 38858, HD 4614, HD 86728, HD 95128.** Grau **A**.
Confirma o que o prompt antecipava: contém HD 10700, HD 115617 e HD 166620 — **três** estrelas relevantes ao P4, não duas. HD 86728 também está entre as 59 de Baum (classe `flat`).

**Ressalva sobre τ Ceti (§3.2), grau A e importante:** "τ Ceti … is known to have a **pole-on inclination** (Korolik et al. 2023) that **precludes us from identifying its chromospheric activity cycle or rotational modulation** via S-STD." **Isto é uma explicação alternativa completa para a "planura" de τ Cet que não tem nada a ver com dínamo.** τ Cet é uma das cinco `Flat` limpas do P4 e a estrela-padrão de referência de dispersão. A inclinação como confundidor de variabilidade **não está em nenhuma unidade de auditoria anterior** e afeta todo o grupo `Flat`: uma estrela vista de polo tem variabilidade suprimida por geometria. **Novo subsídio para Q2 e Q6, e um novo confundidor para Q1.**

## c.4 · Sobre a migração para R′_HK — **subsídio decisivo para Q8**

> **§5 (Sumário), literal:** "We find that stars without a detected cycle are identified with the S-STD activity metric, but **neither average activity metrics of S-value, log(R′_HK)-N1984, nor the revised log(R′_HK) metric from Lorenzo-Oliveira et al. (2018) are able to identify them**. **More so than these two types of log(R′_HK), the S-value itself best correlates with S-value variability.**"

> **§3.1:** "**Using the S-value is a better solution for every mass bin** because they have the highest [P-CC values] … when average activity is available, **the S-value plus the stellar mass is the best metric**."

Grau **A**. "log(R′_HK)-N1984" é explicitamente a calibração de **Noyes et al. 1984**, o objeto de A12.

**Consequência para Q8:** existe uma comparação publicada, sobre 710 estrelas com séries de 20 anos, que testou exatamente a escolha de índice que Q8 coloca — e concluiu que **S + massa estelar** correlaciona melhor com variabilidade que qualquer das duas versões de log R′_HK. A CLS VI ainda sugere a direção oposta à que Q8 assumia: "we argue that instead **using the variation of the activity values as an independent variable** could further their analysis" — isto é, propõe que a variabilidade entre como variável independente, exatamente o programa do P4.
**A justificação original de Q8 — que R′_HK removeria o confundimento de cor — permanece válida para o eixo *comparativo*.** Mas a expectativa de que também melhore o eixo *de variabilidade* está contradita por dados. **Combinado com A12 (faixa de validade), isto muda o balanço de Q8 substancialmente.**

---

## Verificações realizadas (A11 inteira)

| # | Verificação | Resultado |
|---|---|---|
| 1 | 138 ciclos declarados × linhas da Tabela 4 do VizieR | **passa exato** |
| 2 | 710 estrelas × linhas da Tabela 2 do VizieR | **passa exato** |
| 3 | 52 372 S-values × linhas da Tabela 3 do VizieR | 52 380 — Δ = 8 (0.015 %), **passa em substância** |
| 4 | 285 buscadas × recontagem `Nobs ≥ 45` | 290 — Δ = 5, cortes adicionais de §2, **passa em substância** |
| 5 | 0.75 % = 0.00125/0.1674 para HD 10700 × Tabela 2 | **FALHA leve** — tabela dá 0.00121 → 0.723 %. Ver A11b-F1 |
| 6 | "50 estrelas menos dispersas que HD 10700" | **FALHA** — 48 pelo critério tabelado, 52 pelo critério textual |
| 7 | HD 55575: 0.0007/0.1562 = 0.45 % × Tabela 2 | **passa** (0.00070 / 0.1562 = 0.448 %) |
| 8 | Funil de Järvinen & Strassmeier: 78 111 → 13 326 → 13 → 2 | **consistente** entre Resumo, §5.4, §5.5 e §6 |
| 9 | Contagem de ciclos de Baum: 29 (Resumo) vs 14 (Tabela 2, A9) vs 13 (Isaacson §4.2.2) | **contradição de três leituras** — ver A11b-F2 |

---

## Decisões tomadas, com base

1. **A raridade publicada (0.1 %, ou 0.015 % após corte evolutivo) entra na Discussion como taxa-base, com a ressalva A11a-F2 de que mede nível instantâneo e não estado dinâmico** — base: Järvinen & Strassmeier §6; Luhn §1.3. *(→ D48)*
2. **A explicação *aged out* entra na Discussion como hipótese nula concorrente, com HD 101501 identificada como o discriminante empírico** — base: CLS VI §3.3, §4; Baum §4.1. *(→ D49)*
3. **A afirmação de estocasticidade e de transição "on order of years" é citada textualmente e respondida, não omitida** — base: CLS VI §3.3.1. *(→ D50)*
4. **Q8 recebe evidência contrária publicada: S + massa supera log R′_HK como correlato de variabilidade** — base: CLS VI §5, §3.1. *(→ subsídio de Q8, ver A12)*
5. **Inclinação estelar entra como confundidor declarado do grupo `Flat`** — base: CLS VI §3.2 sobre τ Ceti. *(→ D51, novo)*

---

## Não resolvido (grau C ou X)

| Quantidade | Por que | Resolução proposta |
|---|---|---|
| "50 estrelas menos dispersas que τ Cet" (A11b-F1) | **C** — 48 ou 52 conforme o limiar; texto e tabela do artigo discordam no σ de τ Cet | usar o CSV entregue (48, critério documentado) e citar "cerca de 50" |
| σ_S de HD 10700: 0.00121 (tabela) vs 0.00125 (texto) | **C** | citar "≈0.75 %" |
| Contagem de ciclos em Baum+2022: 29 / 14 / 13 | **X** — três leituras | citar 13–14; nunca 29 |
| Inclinação das estrelas `Flat` do P4 | **X** — não medida em nenhuma fonte auditada, exceto τ Cet (Korolik+2023, não auditado) | declarar como limitação; auditar Korolik+2023 se a inclinação entrar na argumentação |
| [Fe/H] da amostra P4 | **X** em A1/A6 | disponível em `baum2022_59stars.csv` (59) e `J:ApJS:274:35:table2.tsv` (710); incorporar na consolidação |

---

## Produtos desta unidade

- `isaacson2024_least_active_50.csv` (raiz) — 48 estrelas com σ_S menor que τ Cet e ≥ 45 observações, com S mediano, σ_S, dispersão relativa em %, N, B−V, log R′_HK, critério documentado.
