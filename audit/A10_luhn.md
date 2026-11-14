# Audit A10 — Luhn, Wright, Henry, Saar & Baum 2022, ApJL 936, L23

**DOI** 10.3847/2041-8213/ac8b13 · arXiv:2207.00612 · *HD 166620: Portrait of a Star Entering a Grand Magnetic Minimum*

| | |
|---|---|
| **Data** | 2026-08-01 |
| **Método de extração** | (1) texto nativo do PDF (`pdftotext -layout`); (2) tabelas machine-readable VizieR `J/ApJ/936/L23` — `J:ApJ:936:L23:table2.tsv` (S_HK, 1 885 linhas) e `J:ApJ:936:L23:table3.tsv` (fotometria APT T4, 1 278 linhas). **Todos os valores numéricos do texto foram recalculados a partir das tabelas** — segundo passe aritmético independente |
| **Páginas lidas** | 1–6 (íntegra), Tabelas 1–3 e as notas de rodapé 8, 9 e 10 |

---

## 1 · Valores extraídos

### 1.1 Composição da série (item 1 da unidade — a lacuna e como é preenchida)

| Conjunto | N declarado (§2) | N na Tabela 2 | Cobertura | Grau |
|---|---|---|---|---|
| MW HKP-1 | 107 | — (agregado) | 1966 – 1977 | **A** |
| MW HKP-2 | 1 547 | — (agregado) | 1977 – 1995 | **A** |
| **MW total (`Inst = MW`)** | 107 + 1 547 = **1 654** | **1 654** ✔ | 1966.593 – 1995.423 | **A** — checksum exato |
| **MW adicional, Oláh+2016 (`new_MW`)** | **158** | **119** ⚠ | 1995.447 – 2002.486 | **X** — ver A10-F1 |
| Keck HIRES-1 | 9 | — | jun–set 1997 | **A** |
| Keck HIRES-2 | 103 | — | 2004 – 2020 mar | **A** |
| **HIRES total (`Inst = HIRES`)** | 9 + 103 = **112** | **112** ✔ | 1997.418 – 2020.185 | **A** — checksum exato |
| **Fotometria APT T4 (Tabela 3)** | **1 278**, 17 estações | **1 278**, **17** ✔ | 1993.29 – 2020.84 | **A** — checksum exato |

Os 107 / 1 547 / 9 / 103 reproduzem **exatamente** a contagem por instrumento que A9 obteve da Tabela 1 de Baum. Duas fontes independentes concordam → grau **A** para a estrutura da série de HD 166620.

**Procedência dos dados de Oláh+2016 (§2.2, literal):** versão binada por noite dos dados completos de Mount Wilson (1966–2002), publicada **numa figura** em Oláh et al. 2016, obtida "courtesy of K. Oláh and W. Soon". Não é um catálogo público — é uma comunicação privada dos autores. **Isto é relevante para o P4: o preenchimento da lacuna não tem fonte numérica publicada independente de Luhn+2022.**

**Regra de junção adotada por Luhn (§2.2, literal):** "We therefore choose to **retain the B22 data for observations prior to 1995 June 4** (the final MW observation in that data set). We use the MW data in Oláh et al. (2016) for observations **after that date**." Nenhum ajuste de timestamp foi aplicado; a discrepância de meio-dia entre os dois conjuntos é atribuída a erros prévios de conversão MJD/JD e deixada como está. Nenhum offset de S_HK foi aplicado a nada.

**Instrumento e precisão do APT T4 (§2.3):** telescópio automático de 0.75 m, Fairborn Observatory, fotômetro de canal único com PMT bi-alcalino EMI 9124QB, bandas Strömgren *b* e *y*, combinadas em (b+y)/2. Fotometria diferencial contra HD 166640 (estrela "b"), única das três comparações constante ao limite da precisão. **Precisão de uma observação: 0.0015–0.0020 mag** em noites fotométricas boas. Desvio-padrão intra-sazonal das observações noturnas: **0.0009 a 0.002 mag**. Estações **2005 a 2015 não observadas** — verificado na Tabela 3 (salto 2004 → 2016).

### 1.2 Cobertura resultante, ponto a ponto — **item 2, a pergunta que decide a viabilidade do teste de CSD**

Médias anuais de S_HK recalculadas da Tabela 2, janela crítica:

| Ano | ⟨S_HK⟩ | σ | N | Instrumento |
|---|---|---|---|---|
| 1990 | 0.1747 | 0.0041 | 57 | MW |
| 1991 | 0.1815 | 0.0061 | 63 | MW |
| 1992 | 0.1821 | 0.0045 | 132 | MW |
| 1993 | 0.1924 | 0.0123 | 84 | MW |
| 1994 | 0.1993 | 0.0113 | 100 | MW |
| **1995** | **0.2126** | 0.0113 | 23 | MW + new_MW ← **máximo do último ciclo** |
| 1996 | 0.1966 | 0.0087 | 22 | new_MW |
| 1997 | 0.1850 | 0.0053 | 32 | new_MW + HIRES-1 |
| 1998 | 0.1838 | 0.0087 | 16 | new_MW |
| 1999 | 0.1812 | 0.0090 | 12 | new_MW |
| 2000 | 0.1735 | 0.0049 | 12 | new_MW |
| 2001 | 0.1784 | 0.0094 | 15 | new_MW |
| 2002 | 0.1815 | 0.0066 | 5 | new_MW |
| — | *lacuna 2002.49 → 2004.64 (2.15 yr)* | | | |
| 2004 | 0.1713 | 0.0015 | 3 | HIRES-2 ← **já plano** |
| 2005 | 0.1707 | 0.0005 | 6 | HIRES-2 |
| *2006–2007* | *lacuna 2005.64 → 2008.46 (2.82 yr)* | | | |
| 2008 | 0.1708 | 0.0029 | 10 | HIRES-2 |
| 2009 | 0.1706 | 0.0009 | 36 | HIRES-2 |
| 2010 | 0.1693 | 0.0016 | 22 | HIRES-2 |

Maior lacuna em S_HK: **2.82 anos** (2005.64 → 2008.46). Em Baum era **6.91 anos** (1997.73 → 2004.64). A lacuna foi de fato fechada. Grau **A**.

**Resposta direta à pergunta da unidade:**

> **A aproximação está amostrada — mas com oito médias anuais.**

O que se tem entre o último máximo (1995) e o primeiro estado plano confirmado (2004) são **8 pontos anuais de S_HK** (1995–2002) e, em paralelo, **12 estações consecutivas de fotometria APT** (1993–2004), estas com amostragem interna densa (47–119 noites por estação).

**O que isso permite e o que não permite:**

- **Não permite** a maquinaria de janela deslizante do P4 na trilha anual. Com D20 (janela = 50 % do comprimento), 8 pontos dão janelas de 4 pontos e **5 janelas** ao todo — φ₁ estimado sobre 4 pontos não tem sentido estatístico, e uma tendência de Kendall sobre 5 valores fortemente sobrepostos não é testável nem pelo procedimento de surrogates de D22.
- **Permite** o teste na trilha **sazonal**: variância intra-sazonal por estação, 12 estações APT + 8 estações S_HK. É exatamente o que Luhn faz (§1.4 abaixo) e é o precedente citável.
- **A conclusão honesta para o manuscrito:** HD 166620 é o único caso conhecido de aproximação amostrada, e mesmo nele o **teste temporal de CSD no formato de Dakos não é executável**. O que é executável é uma comparação de variabilidade entre estados. Isso precisa ser dito, não contornado.

### 1.3 Nível de atividade e brilho no grande mínimo (item 3) — **verificado**

Luhn identifica dois mínimos de ciclo pré-transição e compara com o estado plano (§3.1):

| Estado | Intervalo | ⟨S_HK⟩ declarado | **Recalculado da Tabela 2** | N |
|---|---|---|---|---|
| Mínimo de ciclo 1 | 1971.0 – 1975.0 | 0.181 ± 0.004 | **0.1810 ± 0.0035** ✔ | 44 |
| Mínimo de ciclo 2 | 1987.0 – 1991.0 | 0.172 ± 0.006 | **0.1724 ± 0.0058** ✔ | 315 |
| **Grande mínimo** | 2004 em diante | 0.171 ± 0.002 | **0.1705 ± 0.0020** ✔ | 103 |

Três checksums aritméticos exatos → grau **A**.

**Afirmação verificada (§3.1, literal):** "the period of flat activity associated with the grand magnetic minimum is **not significantly lower** than what the star exhibits during regular cycling behavior."

**Idem no Resumo (literal):** "neither the overall brightness nor the chromospheric activity level (as measured by S_HK) is significantly lower during the grand magnetic minimum than its activity cycle minimum, implying that **an anomalously low mean or instantaneous activity levels are not a good diagnostic or criterion for identifying additional Maunder minimum candidates**."

**Lado fotométrico (§3.2), recalculado:** amplitude das médias sazonais pré-2004 = **2.8 mmag** de faixa (declarado "2–3 mmag") ✔; dispersão das médias sazonais pós-2004 = **0.22 mmag** calculado sobre 2004+2016–2020 vs **0.35 mmag** declarado — divergência menor, provavelmente diferença no conjunto de estações incluídas. Grau **B** para os 0.35 mmag; a ordem de grandeza (≈ 10× menor que antes) é grau **A**.

**Consequência direta para o P4, e é grande:** o discriminante entre estado cíclico e grande mínimo **não é a média** — é a **variabilidade**. Isto é exatamente a tese do P4 e é agora uma afirmação publicada, revisada por pares, sobre o único análogo confirmado de mínimo de Maunder. **É a citação mais forte disponível para a motivação do P4.** Ao mesmo tempo elimina, para sempre, qualquer seleção de amostra baseada em ⟨S⟩ baixo — o que também derruba a base da lista de Baliunas & Jastrow (1990) e é coerente com A9-F8.

### 1.4 Variabilidade intra-sazonal como diagnóstico (item 4) — definição operacional

Este é o item mais reutilizável da unidade. Extração literal do procedimento (§3.1):

1. **Objeto:** σ_S calculado **dentro de cada estação de observação** (não sobre a série toda).
2. **Correção de ruído:** subtrai-se em **quadratura** uma estimativa do ruído aleatório. Luhn adota como limite superior do ruído sazonal do Keck **0.3 %** — "The calculated σ_S is less than this in six of the nine seasons with more than one S_HK(Keck) measurement. The lowest seasonal σ_S values approach 0.3%; we adopt this as an upper limit to the seasonal noise for Keck." Para o Mount Wilson usa o valor de **Baliunas et al. 1995: σ_S ≈ 1.2 %** "from observations of their least variable stars", notando que Wright et al. 2004 dá valor semelhante mas que "when looking on the timescale of a single season … it seems this is an overestimate".
3. **Resultado (§3.1):** σ_S(mín 1) = **0.0027** · σ_S(mín 2) = **0.0054** · σ_S(grande mínimo) = **0.0019**.
4. **Teste:** F-test dá **8.78 × 10⁻⁶** de chance de σ_S(grande) vir da mesma distribuição de σ_S(mín 1).

**Reprodução independente (segundo passe, sobre a Tabela 2 do VizieR):** aplicando ruído = 1.2 % de ⟨S⟩ para os mínimos MW e 0.3 % para o estado Keck, e subtraindo em quadratura do desvio-padrão bruto do intervalo:

| Estado | σ bruto | ruído assumido | **σ corrigido** | Luhn |
|---|---|---|---|---|
| mín 1 | 0.0035 | 0.0022 | **0.0027** | 0.0027 ✔ |
| mín 2 | 0.0058 | 0.0021 | **0.0054** | 0.0054 ✔ |
| grande | 0.0020 | 0.0005 | **0.0019** | 0.0019 ✔ |

**Três reproduções exatas. Grau A.** A receita está totalmente especificada e é implementável.

**Interpretação que Luhn dá (§3.1, literal):** "In the Sun, S_HK in cycle minima are dominated by the roughly spatially uniform network, with occasional small active regions providing limited variability … If we assume that cycle minima in HD 166620 are similarly dominated by the network, the lower S_HK variability observed during the grand minimum is consistent with the hypothesis that there were **even fewer active regions** during this time."

**Estatuto que Luhn atribui (Resumo, literal):** "Intraseasonal variability in S_HK, however, is lower in the star's grand minimum; **this may prove a useful symptom of the phenomenon**." E na §4: "Lower variability in S_HK, though, may prove useful in diagnosing grand minima; **more observed minima are needed to test this, however**."

**Valor para o P4:** é um **precedente publicado, quantitativo e com receita completa**, para usar variância como diagnóstico de estado magnético — a variável exata do P4. A ressalva "more observed minima are needed" é o espaço que o P4 ocupa. Recomenda-se citá-lo em Introduction *e* em Methods (a correção de ruído em quadratura é diretamente adotável e resolve parte de Q6).

### 1.5 Período de rotação (item 5) — verificado

| Quantidade | Valor | Localização | Grau |
|---|---|---|---|
| **⟨P_rot⟩** | **45.06 ± 4.07 d** | §3.3, textual | **A** |
| N de estações com período significativo | **nove** | §3.3 | **A** |
| Faixa das detecções | 37.96 – 50.99 d | §3.3 | **A** |
| Método | periodograma Lomb–Scargle de média flutuante, por estação com > 10 observações | §3.3 | **A** |
| Limiar | **FAP ≤ 5 × 10⁻⁵** | §3.3 | **A** |
| Janela de busca | ± ≈ 20 % de P_rot = 42.4 d (Donahue+1996) **e** ± 20 % de P_rot/2 = 21.2 d (longitudes ativas duplas, Basri & Nguyen 2018); harmônicos e função-janela comparados para descartar aliases; média não-ponderada **incluindo as detecções de P_rot/2 dobradas** | §3.3 | **A** |
| Valor anterior superado | Donahue+1996: 42.4 d (sete estações) | §3.3 | **A** |
| Interpretação da dispersão | "complex combination of surface differential rotation, plus activity growth and decay" | §3.3 | **A** |

**Confirmado.** Note que a incerteza de ± 4.07 d é o desvio-padrão de nove estimativas sazonais, não um erro de medida.

**Parâmetros correlatos (§4):**
- **log R′_HK = −5.03** (Brewer+2016); **−5.07** após corrigir por metalicidade seguindo Saar & Testa 2012 (nota 9). Grau **A**. Isto está "at about the level identified by Brandenburg et al. (2017) and Metcalfe & van Saders (2017) as the threshold for experiencing Maunder minimum behavior" (limiar log R′_HK ≈ **−4.95**, dado no §1).
- **Número de Rossby: 2.08** (com P_rot = 42.4 d) ou **2.21** (com 45.06 d), contra **1.99 para o Sol**, "using a turnover time τ_C from **Noyes et al. 1984**". Grau **A**. — *Nota de ligação:* este é o mesmo τ_C(B−V) cuja calibração A12 audita.
- **log L_X = 26.96** (ROSAT HRI, fim de 1996, Schmitt & Liefke 2004); com R = 0.80 R☉ (Brewer+2016) → **F_X = 4.7 × 10⁴ erg cm⁻² s⁻¹**, acima do piso de dwarfs (10⁴) e abaixo do nível solar médio (≈ 1.3 × 10⁵). Grau **B**.
- Massa **0.78 M☉** na Tabela 1 de Luhn, contra **0.760 M☉** na Tabela 2 de Baum — e Luhn diz "All stellar parameters from B22". Divergência de arredondamento, registrada.

### 1.6 HD 4915 (item 6)

**Nota de rodapé 8, literal:** "This interpretation lends additional evidence that HD 4915 (Shah et al. 2018a) **may soon be entering its own grand magnetic minimum**."

A "interpretação" a que se refere é a do §3.1: "these values also suggest that the cycle minima **decayed** in the final cycles before the transition into grand magnetic minimum (and this is also suggested by the decaying cycle maxima in 1980 and 1995). Thus, it may be the case that we have caught this star at the end of a **much larger interval of decaying cycles**." Grau **B** (especulação explicitamente rotulada como tal, em nota de rodapé).

**⚠ Esta afirmação é contraditada por fonte posterior.** Isaacson+2024 (A11b, §5.6) afirma, com linha de base estendida: "HD 4915 is a candidate star in a Maunder minimum–like state (Shah et al. 2018), but **our extended time baseline shows two cycles. One periodicity is at 4.9 yr, and the second is more than 40 yr, and the longer-period cycle is now turning higher.**" Ver A10-F3 e A11.

---

## 2 · Verificações realizadas

| # | Verificação | Resultado |
|---|---|---|
| 1 | 107 + 1 547 = 1 654 = linhas `MW` na Tabela 2 | **passa exato** |
| 2 | 9 + 103 = 112 = linhas `HIRES` na Tabela 2 | **passa exato** |
| 3 | Contagens por instrumento × Tabela 1 de Baum (fonte independente, A9) | **passa exato**, 4/4 |
| 4 | Tabela 3: 1 278 pontos, 17 estações, sem 2005–2015 | **passa exato** |
| 5 | ⟨S_HK⟩ dos três estados recalculado da Tabela 2 | **passa**, 3/3 até a 4ª casa |
| 6 | σ_S corrigido em quadratura, três estados | **passa**, 3/3 exato |
| 7 | **158 observações novas de Oláh+2016** | **FALHA** — a Tabela 2 tem **119** linhas `new_MW`. Ver A10-F1 |
| 8 | Dispersão das médias sazonais pós-2004 = 0.35 mmag | **parcial** — recalculo dá 0.22 mmag; ordem de grandeza confirmada |
| 9 | Maior lacuna em S_HK após inclusão de Oláh | **2.82 yr** (era 6.91 em Baum) — a lacuna está fechada |

---

## 3 · Achados

**A10-F1 · O texto declara 158 observações novas de Mount Wilson; a tabela machine-readable traz 119. `X`**
§2.2: "The new MW data therefore span from 1995 June to 2002 June and **contain 158 observations**." A Tabela 2 do VizieR (`J/ApJ/936/L23/table2`) tem **119** linhas com `Inst = new_MW`, cobrindo 1995.447 – 2002.486 — o intervalo declarado bate, a contagem não. Diferença: 39 pontos (25 %). Possibilidades não testadas: binagem noturna aplicada na publicação, ou deduplicação pelo CDS. **Registrado, não resolvido** (protocolo regra 4). Não altera nenhuma conclusão desta unidade: a cobertura temporal e as médias anuais são as mesmas em ambas as leituras, e todos os valores de §1.3 e §1.4 foram reproduzidos exatamente a partir das 119 linhas.

**A10-F2 · A transição está traçada, mas a janela de aproximação tem ~8 pontos anuais. `A`**
Ver §1.2. É o achado que decide a viabilidade do teste temporal. **O teste de CSD no formato do P4 (janela deslizante de 50 %, τ de Kendall, surrogates ARMA) não é executável em HD 166620.** O que é executável é a comparação de variabilidade entre estados, no formato de Luhn §3.1. Isto tem de ser dito no manuscrito como limitação declarada, não contornado.

**A10-F3 · Contradição documentada sobre HD 4915. `contradição entre fontes`**
Shah+2018 → candidata a mínimo de Maunder. Luhn+2022 nota 8 → "may soon be entering its own grand magnetic minimum" (especulativo). Isaacson+2024 §5.6 → **dois ciclos, 4.9 yr e > 40 yr, com o longo agora subindo**; Tabela 4 da CLS V registra P = 4.86 yr. Cronologicamente a fonte mais recente e com a maior linha de base **desfaz** a candidatura. **D35 permanece correta** (a proveniência de HD 4915 está registrada; a estrela não está em Baliunas+1995) mas ganha uma camada: **a candidatura de HD 4915 a mínimo de Maunder está desmentida na literatura de 2024.** Qualquer menção a HD 4915 no manuscrito precisa citar as três fontes em ordem.

**A10-F4 · Luhn dissolve a ressalva de calibração que Baum levantou contra si mesmo. `A`**
Baum §4.1 dizia que a conclusão "o grande mínimo não está mais baixo que os mínimos locais" não era robusta porque outras estrelas exigiram offsets. Luhn §4: "The new Mount Wilson data here are **contemporaneous with the pre-2004 HIRES data** in B22 and are consistent with it, demonstrating that the **mutual calibration there is robust**"; e §3.1: "the HIRES-1 data … are consistently calibrated with both the HIRES-2 observations and all Mount Wilson observations, thus **dispelling any doubts about potential offset errors**". A fotometria APT, que atravessa os três conjuntos, remove independentemente "any concern that the sets might not be of the same star or that large calibration offsets exist among them."
**Alcance da conclusão:** vale **para HD 166620**, por sobreposição temporal e por uma segunda observável (fotometria). **Não se estende** às outras 58 estrelas de Baum, para as quais A9-F6 permanece de pé — nenhuma delas tem dados de Oláh nem fotometria APT publicada nesta série.

**A10-F5 · O grande mínimo não é um colapso do dínamo. `A`**
§4, literal: "the grand minimum is **not the result of a dramatically weaker surface magnetic field** than is present during ordinary magnetic minima, for instance due to a complete collapse of the dynamo, but is **essentially an ordinary minimum extended in time**, perhaps with fewer residual active regions to explain the further reduced variability." Coerente com o Sol: poucas manchas durante o mínimo de Maunder (Ribes & Nesme-Ribes 1993) e ¹⁰Be continuou a variar (Beer et al. 1998, 2018) porque a produção liga-se mais à **geometria global** do campo do que à sua intensidade.
**Consequência para a estrutura teórica do P4:** se o grande mínimo é "um mínimo ordinário estendido no tempo", então o objeto que sofre a bifurcação **não é a intensidade do campo, é a periodicidade** — o sistema deixa de oscilar sem deixar de ter campo. Isso é uma bifurcação de Hopf (perda do ciclo limite), não uma sela-nó. CSD aplica-se a ambas, mas os indicadores e a assinatura esperada diferem, e A7 (Scheffer, Held & Kleinen) precisa ser lido com essa distinção em mente. **Item para a consolidação.**

**A10-F6 · Correlação positiva entre brilho e atividade — a estrela escurece ao ficar menos ativa. `A`**
§3.2 e §4: "when the star transitioned from cycling to flat behavior, the star also became slightly fainter", com "excellent agreement" entre as duas séries quando postas em escala comum (fator arbitrário de 10 na fotometria; "scale factors of 8–12 all looked similarly consistent"). Interpretação: superfície dominada por **fáculas e rede magnética brilhante**, não por manchas — regime "faculae-dominated" à la Lockwood+2007. Grau **A**.
**Relevância para A2:** Lockwood+2007 foi auditado (A2) e concluiu-se que não estende as séries; mas a *relação* fotometria–atividade que ele estabelece é aqui confirmada num caso limpo. Se o P4 quiser uma segunda observável, a fotometria APT de HD 166620 (Tabela 3, já obtida) é a única disponível.

**A10-F7 · Não há evidência de variabilidade residual após ≈2005. `A/C`**
§4: "We see **no clear evidence of variability** in either S or in photometry in HD 166620 after ≈2005. It is possible that cyclic activity of some type continues on HD 166620 below our current ability to clearly detect it; indeed, **the tiny, poorly resolved increase in S in 2014 may be a hint** of such residual activity." O ponto de 2014 é uma **única observação** (verificado na Tabela 2: N = 1 em 2014, S = 0.1776). Grau **C** para o "hint"; não usar.

---

## 4 · Decisões tomadas, com base

1. **A definição operacional de variabilidade intra-sazonal de Luhn §3.1 é adotada como precedente citável e como receita de correção de ruído** — base: §1.4, reproduzida exatamente. A subtração em quadratura de um ruído instrumental estimado é o tratamento que Q6 pedia. *(→ D45)*
2. **O teste temporal de CSD no formato de Dakos não é executável em HD 166620; a unidade de análise é a comparação de variabilidade entre estados** — base: A10-F2. *(→ D46)*
3. **HD 4915 não é tratada como candidata a mínimo de Maunder no manuscrito sem citar Isaacson+2024** — base: A10-F3. *(→ D47)*
4. **A validade da calibração instrumental de Luhn é restrita a HD 166620** — base: A10-F4. Para as outras 58 estrelas de Baum, A9-F6 vale. *(→ complementa D44)*

---

## 5 · Não resolvido (grau C ou X)

| Quantidade | Por que não resolvido | Resolução proposta |
|---|---|---|
| **158 vs 119 observações `new_MW`** (A10-F1) | **X** — texto e tabela do mesmo artigo discordam | citar a cobertura temporal, não a contagem; ou consultar os autores. Não afeta nenhum valor derivado |
| Dispersão sazonal pós-2004 = 0.35 mmag | **C** — recalculo dá 0.22 mmag com estações 2004+2016–2020 | citar a razão (~10× menor), não o número absoluto |
| Dados de Oláh+2016 como fonte independente | **C** — são comunicação privada dos autores, publicados originalmente apenas **numa figura** | inevitável; declarar a proveniência ao citar |
| "hint" de atividade residual em 2014 (A10-F7) | **C** — ponto único | não usar |
| Massa 0.78 (Luhn T1) vs 0.760 (Baum T2) M☉ | **C** — trivial, arredondamento | usar Baum, que é a fonte declarada |

---

## 6 · Nota sobre o arquivo `aa28479-16.pdf` em `bib/`

Corresponde a **Oláh et al. 2016, A&A 590, A133** — a fonte dos dados que preenchem a lacuna (§2.2 de Luhn) e a referência que Isaacson+2024 e a CLS VI citam para a afirmação de que ciclos são múltiplos e mutáveis. Está em `bib/` e disponível; **não foi auditado nesta unidade** (não estava no escopo de A9–A12). Recomenda-se uma unidade A13 se o P4 vier a usar decomposição tempo-frequência, já que Oláh usa transformada de Fourier de tempo curto e distribuição de Choi–Williams — métodos que Isaacson+2024 §5.8 aponta como capazes de detectar ciclos que os periodogramas perdem.
