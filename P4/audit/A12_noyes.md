# Audit A12 — Noyes, Hartmann, Baliunas, Duncan & Vaughan 1984, ApJ 279, 763

*Rotation, Convection, and Magnetic Activity in Lower Main-Sequence Stars* · ADS `1984ApJ...279..763N`

| | |
|---|---|
| **Data** | 2026-08-01 |
| **Documento** | `bib/Noyes1984.pdf` — **scan**, comprimido com LuraTech PDF Compressor. Tem camada de texto, mas é OCR de origem: colunas entrelaçadas, `B−V` lido como `B—F`, `10⁻⁴` lido como `Kr4`, `C_cf` lido como `C,,`. **A regra dos dois passes é obrigatória e foi aplicada com rigor máximo.** |
| **Método de extração — três passes independentes** | (1) camada de texto nativa do PDF (`pdftotext -layout`); (2) **re-render a 400 DPI + Tesseract**, colunas separadas, `--psm 6`, `--psm 4` e `--psm 11`; (3) **inspeção visual direta das imagens de página ampliadas** — o passe que resolve expoentes e sinais, e que o protocolo §5 prescreve explicitamente para desacordos |
| **Páginas lidas** | 764 (§II, definição), 774–775 (Apêndice, alíneas *a* e *b*) |
| **Escopo** | Estabelecer a receita e os seus limites. **Nenhuma conversão foi executada** (D39, e instrução explícita da unidade). |

---

## 1 · A definição de R′_HK (§II, p. 764)

**R′_HK** é a razão entre a emissão da **cromosfera** nos núcleos das linhas H e K de Ca II e a **emissão bolométrica total** da estrela. A linha (`′`) denota a subtração da contribuição fotosférica.

Cadeia completa, em três etapas:

```
S  →  R_HK  =  1.340 × 10⁻⁴ · C_cf(B−V) · S      [conversão em razão de fluxo]
R_phot        =  10^( −4.898 + 1.918(B−V)² − 2.893(B−V)³ )   [contribuição fotosférica]
R′_HK         =  R_HK − R_phot                    [emissão puramente cromosférica]
```

**Justificação física dada pelos autores (§II):**
- S é "proportional to the ratio of measured flux within the 1 Å H and K bandpasses of the Mount Wilson H-K photometer to that in two continuum windows equidistant to the red and violet of the H and K lines. **It is sensitive to the integrated emission over these windows, which is very dependent on spectral type. It is also sensitive to the amount of photospheric radiation transmitted by the H and K instrumental passbands.** To determine the level of true chromospheric emission in the H and K lines quantitatively, it is necessary to correct for **both** of these effects."
- C_cf corrige o **primeiro** efeito (variação com B−V da radiação fotosférica **nas janelas de contínuo**).
- R_phot corrige o **segundo** (fração da emissão **dentro** das passagens H e K que é fotosférica, não cromosférica).
- Sentido de R′_HK: "R′_HK is proportional to that fraction of the nonradiative energy flux in the convective zone (essentially equal to the entire stellar bolometric luminosity throughout most of the convection zone) which is ultimately converted into magnetic field–associated chromospheric emission."

Grau **A** (três passes concordantes).

---

## 2 · Receita completa

### 2.1 Conversão S → R_HK (Apêndice, alínea *a*, p. 774–775)

**Verificado visualmente, caractere a caractere:**

> R_HK = 1.340 × 10⁻⁴ C_cf S ,
>
> where log C_cf(B−V) = 1.13(B−V)³ − 3.91(B−V)² + 2.84 × (B−V) − 0.47.

| Termo | Valor | Grau |
|---|---|---|
| Constante | **1.340 × 10⁻⁴** | **A** — visual + 2 OCR |
| Coeficiente de (B−V)³ | **+1.13** | **A** |
| Coeficiente de (B−V)² | **−3.91** | **A** |
| Coeficiente de (B−V)¹ | **+2.84** | **A** |
| Termo constante | **−0.47** | **A** |

**O que a constante absorve (nota parentética, literal):** "The factor 1.34 × 10⁻⁴ in the first equation above absorbs the **Stefan-Boltzmann constant**, as well as a **normalizing factor of 10¹⁴**, into Middelkoop's coefficient." Grau **A** (o expoente 14 foi confirmado visualmente; o OCR nativo o lia como `10**`).

Origem: **Middelkoop 1982**. R_HK ≡ F_HK / (σT_eff⁴), onde F_HK é o fluxo por cm² na superfície estelar nas passagens H e K.

### 2.2 A correção C′_cf de Noyes (mesma alínea) — **este é o C_cf que se usa na prática**

**Verificado visualmente:**

> We have corrected C_cf for a non-physical maximum at B−V = 0.43 by setting
> log C′_cf = log C_cf + Δ log C, where Δ log C = 0 for B−V > 0.63, and
> Δ log C = 0.135x − 0.814x² + 6.03x³ for x ≡ 0.63 − (B−V) > 0.

| Termo | Valor | Grau |
|---|---|---|
| Ponto de descontinuidade | **B−V = 0.63** | **A** |
| Definição de x | **x ≡ 0.63 − (B−V)**, aplicável só se x > 0 | **A** |
| Coeficiente de x | **+0.135** | **A** |
| Coeficiente de x² | **−0.814** | **A** |
| Coeficiente de x³ | **+6.03** | **A** |
| Motivo da correção | máximo **não-físico** de C_cf em B−V = 0.43 | **A** |

**Atenção de implementação:** a correção é **aditiva no logaritmo** e aplica-se **somente a estrelas mais azuis que B−V = 0.63**. Para B−V ≥ 0.63, C′_cf = C_cf. §II confirma: "we use it here, with only a **very small modification for stars with B−V < 0.6**". Como quase toda a amostra P4 tem B−V ≥ 0.63, **Δ log C é irrelevante para o P4** — o que importa é a validade de C_cf no extremo **vermelho**, tratada em §3.

### 2.3 A subtração fotosférica (Apêndice, alínea *b*, p. 775)

**Definição conservadora adotada (literal):** "Given the complexity of the problem, it seems safest to adopt a **conservative definition of the photospheric radiation, namely, that it consists only of the radiation exterior to the H1 and K1 minima.** This definition has the virtue of producing a clear way of determining the photospheric correction empirically."

**Verificado visualmente:**

> log R_phot = −4.898 + 1.918(B−V)² − 2.893(B−V)³
>
> in the range 0.44 < (B−V) < 0.82.

| Termo | Valor | Grau |
|---|---|---|
| Termo constante | **−4.898** | **A** |
| Coeficiente de (B−V)² | **+1.918** | **A** |
| Coeficiente de (B−V)³ | **−2.893** | **A** |
| **Não há termo linear em (B−V)** | confirmado visualmente | **A** |
| **Faixa de validade declarada** | **0.44 < (B−V) < 0.82** | **A** |

Derivação: Hartmann et al. 1984 (referenciado no ponto).

**Forma alternativa (mesma alínea, literal):** "In an independent analysis, one of us (D. D.) recently obtained an alternative form for the photospheric correction, **which fits the one used in this paper to within observational errors**:
> log R_phot = −4.02 − 1.40(B−V).
Because of its simple form, this expression **may be preferable for future use**."
Grau **B** (OCR de dois passes concordante; não verificada visualmente — os coeficientes são simples e não há ambiguidade de expoente). Autor: D. Duncan.

---

## 3 · Faixa de validade em B−V — **o item decisivo da unidade**

Consolidando **todas** as declarações de domínio e de incerteza do artigo, com localização:

| Faixa em B−V | O que a fonte diz | Localização |
|---|---|---|
| **B−V < 0.44** | fora do ajuste de R_phot | Apêndice *b* |
| B−V < 0.6 (≈0.63) | requer a correção Δ log C do máximo não-físico | §II; Apêndice *a* |
| **0.44 < B−V < 0.82** | **faixa em que R_phot foi ajustada** | Apêndice *b* |
| B−V > 0.82 | "We have also **used the same expression** for B−V > 0.82" — **extrapolação declarada** | Apêndice *b* |
| B−V < 1.0 | C_cf de Middelkoop "**quite consistent** with independent spectrophotometric measurements" | §II |
| **B−V > 1.0** | "**the calibration for B−V > 1.0 may be uncertain by as much as 20 %**" | §II (com remissão ao Apêndice) |
| B−V ≳ 1.0 | a correção fotosférica "**becomes negligible**"; Hartmann et al. 1984 estimam contribuição **menor**; "the magnitude of the correction is **less certain for the coolest stars**, and in any case it is so small as to be relatively unimportant" | Apêndice *b* |
| **B−V ≳ 1.2** | "**The worst discrepancy** in the various attempts at calibration occurs for B−V ≳ 1.2", porque o índice de cor C_rv das passagens de contínuo "shows an increasingly large scatter as a function of spectral type" (Vaughan & Preston 1980) | Apêndice *a* |

Grau **A** para todas as linhas.

### 3.1 Onde caem as estrelas do P4

Aplicando as faixas ao catálogo congelado de A1 (112 linhas) → **`noyes1984_validade_cor.csv`** (raiz).

**Distribuição das 112:**

| Faixa | N |
|---|---|
| DENTRO (0.44–0.82, faixa ajustada de R_phot) | **82** |
| EXTRAPOLADO (0.82–1.0; C_cf ainda consistente) | 17 |
| EXTRAPOLADO + C_cf incerto até 20 % (B−V > 1.0) | 6 |
| EXTRAPOLADO + pior discrepância declarada (B−V > 1.2) | 2 |
| FORA (abaixo de 0.44) | 5 |

**E agora o resultado que muda Q8.** Estrelas de interesse do P4, ordenadas por cor:

| HD | B−V | Grupo (A1) | Faixa de Noyes+1984 |
|---|---|---|---|
| 43587 | 0.61 | `Flat?` | **DENTRO** |
| 81809 | 0.64 | CYCLE Excellent | **DENTRO** |
| 10700 (τ Cet) | 0.72 | `Flat?` | **DENTRO** |
| 190360 | 0.73 | `Flat` | **DENTRO** |
| 103095 | 0.75 | CYCLE Excellent | **DENTRO** |
| 152391 | 0.76 | CYCLE Excellent | **DENTRO** |
| 182572 | 0.77 | `Flat` | **DENTRO** |
| 26965 | 0.82 | CYCLE Excellent | **DENTRO** (na fronteira) |
| 10476 | 0.84 | CYCLE Excellent | extrapolado |
| 3651 | 0.85 | CYCLE Good | extrapolado |
| **166620** | 0.87 | CYCLE Excellent | extrapolado |
| 4628 | 0.88 | CYCLE Excellent | extrapolado |
| 219834B | 0.91 | CYCLE Excellent | extrapolado |
| **23249** | **0.92** | `Flat?` | extrapolado |
| **160346** | **0.96** | CYCLE Excellent | extrapolado |
| 16160 | 0.98 | CYCLE Excellent | extrapolado |
| **32147** | **1.06** | CYCLE Excellent | **extrapolado + C_cf incerto até 20 %** |
| 201091 (61 Cyg) | 1.18 | CYCLE Excellent | **extrapolado + C_cf incerto até 20 %** |

**Medianas de B−V, confirmadas por cálculo sobre o catálogo A1:**
`Long` 0.525 · `Flat` (11 estrelas) 0.560 · **`Flat` limpo (5, pós-D13) 0.73** · `Flat?` 0.665 · `Var` 0.610 · `CYCLE` (todas as 52) 0.725 · **`CYCLE` + FAP Excellent 0.88**.
As medianas citadas no enunciado da unidade (Long 0.49 · Flat 0.73 · CYCLE Excellent 0.88) são reproduzidas para os subconjuntos relevantes. Grau **A**.

---

## 4 · Incertezas declaradas pela fonte

| Fonte de incerteza | Magnitude | Localização | Grau |
|---|---|---|---|
| Concordância entre as três calibrações S → R_HK (Middelkoop; O'Connell 1973; Faÿ, Stein & Warren 1974) | "**remarkably good** for most of the B−V range of interest — **≲ 10 %**" | Apêndice *a* | **A** |
| C_cf para **B−V > 1.0** | "**uncertain by as much as 20 %**" | §II | **A** |
| Comparação com Linsky et al. 1979 (8 estrelas do programa) | "Their fluxes agree with ours **to within ~20 %**", atribuído à dificuldade de calibrar espectros fotográficos de fenda | Apêndice *a* | **A** |
| Correção fotosférica de Linsky & Ayres 1978 vs a adotada | "their photospheric correction is about **25 % larger than ours on average**"; a fórmula deste artigo "forms a **lower bound** to the Linsky and Ayres points" | Apêndice *b* | **A** |
| Impacto de usar Linsky & Ayres em vez desta | "would **not** be expected to make a significant change in the conclusions drawn here" | Apêndice *b* | **A** |
| Forma alternativa de Duncan | "fits the one used in this paper **to within observational errors**" | Apêndice *b* | **A** |
| Natureza da calibração de Middelkoop | **relativa, não absoluta**: sem espectrofotometria absoluta, sem correções de extinção (minimizadas por diferenciação) | §II; Apêndice *a* | **A** |
| Método de checagem próprio dos autores | também **relativo**: "Note that this method provides a **relative, not an absolute, calibration**" | Apêndice *a* | **A** |

**Não há barra de erro formal publicada para R′_HK.** As incertezas acima são declarações de concordância entre calibrações, não uma propagação. **Grau X** para "incerteza formal de R′_HK".

---

## 5 · Achados

**A12-F1 · A faixa de validade da correção fotosférica cobre o grupo `Flat` do P4 e *não* cobre o grupo de controle. `A`**
Das cinco `Flat` limpas, **quatro estão dentro** da faixa ajustada (B−V 0.61 a 0.77) e apenas HD 23249 (0.92) extrapola. Das treze `CYCLE` + FAP Excellent (incluindo a linha do Sol, B−V = 0.66), **apenas cinco estão dentro e oito extrapolam** — duas delas (HD 32147 com 1.06 e HD 201091 com 1.18) na região onde o próprio artigo declara **até 20 % de incerteza**.
**Consequência para Q8, e é o oposto do que se esperava.** A motivação de Q8 era que R′_HK removeria o confundimento de cor entre grupos. Mas aplicar a receita converteria o confundimento de cor num **confundimento de validade de calibração**: o grupo `Flat` seria convertido dentro do domínio ajustado, o grupo de controle fora dele, com erro sistemático de até 20 % concentrado num só braço da comparação. **Um erro sistemático correlacionado com o grupo é pior que um confundidor conhecido e declarado.**

**A12-F2 · A subtração fotosférica é "muito significativa" precisamente para as estrelas de baixa atividade — a amostra inteira do P4. `A`**
Apêndice *b*, literal: "We note that subtraction of R_phot from the total H-K emission R_HK **does not have a large effect for active chromosphere stars, but it can be a very significant correction for the chromospherically less active stars**. **For these stars in particular it is important to determine the photospheric correction more rigorously than has been done here**, both by [métodos que o texto passa a discutir]."
**Este é o próprio artigo declarando que a sua correção é menos confiável exatamente no regime que o P4 estuda.** Nenhuma unidade anterior tinha esta informação. É a ressalva mais forte contra a migração para R′_HK e tem de estar em qualquer decisão sobre Q8.

**A12-F3 · A receita tem duas descontinuidades, ambas dentro da faixa de cor da amostra P4. `A`**
Em **B−V = 0.63** a correção Δ log C liga/desliga; em **B−V = 0.82** termina o domínio ajustado de R_phot. A amostra P4 tem estrelas dos dois lados de ambas (HD 43587 em 0.61 e 190360 em 0.73 cruzam a primeira; 26965 em 0.82 e 10476 em 0.84 cruzam a segunda). **Um índice com descontinuidades no interior da amostra não é um índice unificador** — é uma reparametrização por partes, e qualquer comparação entre grupos herda a costura.

**A12-F4 · Todas as calibrações são relativas; a escala absoluta não é estabelecida por este artigo. `A`**
Nem Middelkoop nem a checagem própria dos autores são absolutas. Para o P4 isto é **inócuo no eixo temporal** (uma constante multiplicativa desconhecida não afeta φ₁ nem τ) mas **não é inócuo** se se quiser comparar valores absolutos de R′_HK entre o Sol e as estrelas, ou com os limiares publicados (log R′_HK ≈ −4.95 de Brandenburg+2017; −4.90 da CLS VI).

**A12-F5 · A propriedade de invariância registrada em D40 é confirmada — e limitada. `A`**
Para B−V **fixo**, S → R′_HK é monotônica (C_cf > 0, R_phot constante), logo τ de Kendall é exatamente invariante. **Confirmado.** Mas D40 vale **por estrela**, não entre estrelas: a transformação difere de estrela para estrela através de B−V, e é **por partes** em 0.63 e 0.82 (A12-F3). Portanto:
- **eixo temporal por estrela:** τ invariante, φ₁ quase invariante, σ² reescalado por (1.340×10⁻⁴·C_cf)². Migrar não estraga nada;
- **eixo comparativo entre grupos:** é justamente aqui que se ganharia — e é aqui que A12-F1 e A12-F2 dizem que se perde de outro modo.

**A12-F6 · Existe uma segunda receita, mais simples, ajustada aos mesmos dados. `B`**
log R_phot = −4.02 − 1.40(B−V), de Duncan, "fits the one used in this paper to within observational errors" e "may be preferable for future use". **Se a conversão for feita, calcular pelas duas e reportar a diferença é um teste de robustez barato e citável.** (Não executado aqui, por D39.)

**A12-F7 · Ligação com A10.** O número de Rossby de HD 166620 em Luhn+2022 §4 (2.08 ou 2.21, contra 1.99 do Sol) usa o tempo de *turnover* convectivo **τ_C de Noyes et al. 1984** — a mesma calibração, aplicada em B−V = 0.87, isto é, **fora do domínio ajustado de R_phot**. Não invalida o τ_C (que é outra relação do mesmo artigo, não auditada aqui) mas registra-se que a literatura moderna aplica correlações de Noyes+1984 rotineiramente em extrapolação. Grau **B**.

---

## 6 · Decisões tomadas, com base

1. **A receita S → R′_HK fica estabelecida e documentada, com os cinco coeficientes de C_cf, os três de Δ log C e os três de R_phot em grau A, verificados por três passes** — base: §2 desta unidade. *(→ D52)*
2. **A faixa de validade é registrada como 0.44 < B−V < 0.82 para R_phot, com extrapolação declarada acima de 0.82 e incerteza de até 20 % acima de 1.0** — base: Apêndice *b* e §II. *(→ D53)*
3. **Nenhuma conversão executada** — D39 cumprida. *(sem decisão nova)*
4. **A migração para R′_HK deixa de ser uma melhoria presumida e passa a ser um trade-off quantificado**, com três evidências contrárias novas: A12-F1 (validade correlacionada com grupo), A12-F2 (a fonte declara a correção menos confiável para estrelas inativas) e CLS VI §5 (S + massa supera log R′_HK como correlato de variabilidade). **A decisão continua sendo humana e Q8 continua aberta** — mas o balanço mudou de sinal. *(→ D54)*

---

## 7 · Não resolvido (grau C ou X)

| Quantidade | Por que | Resolução proposta |
|---|---|---|
| **Incerteza formal de R′_HK** | **X** — o artigo não publica propagação de erro | usar as declarações de concordância (≲10 % geral; 20 % para B−V > 1.0; 25 % de diferença sistemática na correção fotosférica) como envelope; declarar que não é um erro formal |
| Coeficientes da forma alternativa de Duncan | **B** — dois passes de OCR concordantes, sem verificação visual | verificar visualmente se a forma alternativa for usada |
| Comportamento de C_cf abaixo de B−V = 0.43 | **C** — o máximo não-físico é corrigido, mas a validade abaixo de 0.44 não é declarada | 5 estrelas do catálogo A1 estão aí; nenhuma é candidata do P4 |
| Calibração absoluta de R_HK | **X** — todas as calibrações são relativas | irrelevante para o eixo temporal (A12-F5); declarar se valores absolutos forem comparados a limiares publicados |
| Faixa de validade de τ_C(B−V) (Noyes+1984) | **não auditada** | fora do escopo desta unidade; auditar se o número de Rossby entrar na argumentação (A12-F7) |

---

## 8 · Produtos desta unidade

- `noyes1984_validade_cor.csv` (raiz) — 112 linhas do catálogo congelado de A1, cada uma com B−V, classe primária, FAP e a faixa de validade de Noyes+1984 em que cai.
- Recortes de página usados na verificação visual: as regiões das equações nas p. 774–775, renderizadas a 400 DPI (efêmeros; reprodutíveis com `pdftoppm -r 400 -png -f 12 -l 14`).
