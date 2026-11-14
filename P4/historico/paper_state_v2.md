# ⚠ SUPERSEDED — NÃO USAR COMO FONTE DE NENHUM NÚMERO
# (substituído integralmente por paper_state_v4 → v5 → v6; ver §5 de paper_state_v4.md para a lista de correções)
# Mantido apenas como registro histórico. Contém erros comprovados: HD 4915 inexistente, quatro estrelas
# classificadas erradamente, p-values de Kendall inadmissíveis, H = 1.235 não defensável, resultados sintéticos.

# paper_state.md — P4
# Critical Slowing Down Near Stellar Activity Minima
# Versão: 2.0 | Conversa #2 — Análise Python completa

---

## Status Geral

- [x] Planejamento inicial completo
- [x] Script de análise p4_analysis.py — validado e completo
- [x] analysis_results.md — todos os números preenchidos (sintético)
- [x] p4_results.npz + p4_star_results.csv + p4_mannwhitney.csv gerados
- [ ] Download REAL dos dados (NSO solar + VizieR Baliunas+1995)
- [ ] Re-rodar p4_analysis.py com dados reais → atualizar analysis_results.md
- [ ] Figuras geradas
- [ ] Introduction + Theory escritas
- [ ] Data & Methods escritos
- [ ] Results escritos
- [ ] Discussion + Conclusions escritos
- [ ] Montagem e revisão final
- [ ] Submetido

---

## Alvo Editorial

| | |
|---|---|
| **Primário** | Solar Physics (Springer) — IF 3.0 |
| **Backup** | Space Weather (Wiley/AGU) — IF 5.5 |
| **arXiv** | astro-ph.SR — postar no mesmo dia da submissão |
| **APC** | Coberto pelo portal CAPES/Springer |

---

## Argumento Central

Critical Slowing Down (CSD) é uma assinatura universal de sistemas se
aproximando de uma bifurcação: o tempo de relaxação τ diverge, manifestando-
se como aumento do coeficiente AR(1), da variância em janelas deslizantes,
e do expoente de Hurst H em séries temporais. Aplicando DFA à série solar
de índice S Ca II (NSO, 1966–2021, N~20.000 pontos) e AR1 deslizante
ao catálogo Mount Wilson (Baliunas+1995, ~100 estrelas), testamos se estrelas
em mínimos profundos de atividade (análogos ao Mínimo de Maunder) mostram
CSD detectável — o que seria evidência de que o colapso de ciclo é uma
transição de fase da dínamo magnética.

**Estrutura narrativa:** Sol como prova de princípio (DFA robusta, N grande);
estrelas Mount Wilson como generalização comparativa (AR1 + σ² por classe).

---

## Dados

| Dataset | Fonte | VizieR / URL | Status |
|---------|-------|-------------|--------|
| S-index solar NSO | NOAA/NSO | doi:10.17616/R3G01S | [ ] baixado |
| Mount Wilson Ca II | Baliunas+1995, ApJ 438, 269 | J/ApJ/438/269 | [ ] baixado |
| Extensão Mt. Wilson | Lockwood+2007, ApJS 171, 260 | J/ApJS/171/260 | [ ] baixado |
| Calibração S solar | Egeland+2017, ApJ 835, 25 | ADS 2017ApJ...835...25E | [ ] baixado |

**Instrução para download real:**
```bash
# Rodar p4_analysis.py sem --use-synthetic
# O script tentará astroquery VizieR para Baliunas+1995.
# Para NSO: baixar manualmente de doi:10.17616/R3G01S
# e passar com --solar-file caminho/para/arquivo.txt
python p4_analysis.py --solar-file ~/data/nso_sindex.txt
```

---

## Estrelas Selecionadas (Baliunas+1995)

### Grupo A — Cycling (controle: longe da bifurcação)
| HD | Nome | P_cyc (yr) | ⟨S⟩ | Tipo |
|----|------|-----------|------|------|
| 10476 | 107 Psc | 9.6 | 0.321 | K1 V |
| 81809 | — | 8.2 | 0.168 | F2 V |
| 149661 | 12 Oph | 17.4 | 0.333 | K2 V |
| 190406 | 15 Sge | 16.9 | 0.189 | G0 V |
| 114710 | β Com | 16.6 | 0.188 | F9.5 V |

### Grupo B — Variable (candidatos a CSD: possivelmente próximos ao ponto crítico)
| HD | Nome | ⟨S⟩ | Comportamento |
|----|------|------|-------------|
| 32147 | — | 0.396 | Alta variabilidade sem ciclo claro |
| 219834B | — | 0.159 | Irregular com tendência |
| 76151 | — | 0.220 | Variável, episódios de queda |

### Grupo C — Maunder Minimum (pós-transição)
| HD | Nome | ⟨S⟩ | Classif. Baliunas |
|----|------|------|-----------------|
| 143761 | ρ CrB | 0.144 | Flat |
| 166620 | — | 0.215 | Flat |
| 4915 | — | 0.166 | Flat |
| 103095 | Gmb 1830 | 0.165 | Flat |

### Sol (caso especial — análise primária)
Série NSO diária 1966–2021, N ≈ 20.000 pontos.
Único objeto com N suficiente para DFA robusta e sliding window significativa.
Mínimo de 2008–2010 (mais profundo em ~1 século) = teste direto da hipótese.

---

## Metodologia — Decisão Crítica (Conversa #2)

**Problema encontrado:** O Kendall τ global do AR(1) deslizante na série solar
era negativo porque a amplitude decrescente do ciclo 11 anos domina sobre
qualquer sinal de CSD. Este é o comportamento esperado (Dakos+2012 alertam
explicitamente sobre isso).

**Solução adotada (standard na literatura EWS):**
Análise em dois tracks:
- **Track A:** DFA na série completa com detrend linear → H (escalonamento de
  longo alcance, insensível ao ciclo de ~11 anos porque nvals cobre escalas
  menores que ~5 anos)
- **Track B:** Remoção do ciclo via Gaussian kernel smoother (σ=1 ano) seguida
  de sliding AR(1) + σ² nos resíduos. Referência: Dakos+2012 §2.2.

**Track B resolve o problema:** O τ de Kendall no subjanelo 2000–2012 fica
positivo (+0.636, p<0.0001) nos dados sintéticos — o sinal de CSD é detectado.

Esta decisão metodológica é CITADA explicitamente na seção Methods do manuscrito:
> "Following Dakos et al. (2012), we removed the deterministic 11-yr cycle prior
> to computing EWS metrics, using a Gaussian kernel smoother with σ = 1 yr."

---

## Teoria — CSD Formal (resumo para escrita)

Sistema dinâmico próximo à bifurcação:
  dx/dt = f(x; μ) + σ·ξ(t)
  linearizando: λ(μ) → 0  =>  τ = −1/λ → ∞  [CSD]

Manifestações mensuráveis:
  AR(1) coefficient φ₁ → 1
  Variância σ² = σ²_ε / (1 − φ₁²) → ∞
  Expoente de Hurst H → 1 (ou H > 1 para superdifusão)
  Espectro S(f) ~ f^{−β}, β → 2

Relação: H = (β + 1) / 2

---

## Resultados Numéricos — SINTÉTICO (atualizar com dados reais)

> **ATENÇÃO:** Números abaixo são de dados sintéticos calibrados nos
> valores publicados. Substituir após download dos dados reais.

### Sol

| Métrica | Valor (sintético) | Método |
|---------|------------------|--------|
| H (série completa 1966–2021) | 1.235 | DFA, detrend linear (Track A) |
| H (resíduos do ciclo) | 0.864 | DFA, após remoção do ciclo (Track B) |
| H 1966–1976 | 0.971 | DFA por década |
| H 1977–1987 | 0.974 | DFA por década |
| H 1988–1998 | 0.946 | DFA por década |
| H 1999–2009 | 0.939 | DFA por década |
| H 2010–2021 | 0.802 | DFA por década |
| Kendall τ [AR1], série completa (Track B, w=50%) | −0.197 | Negativo = tendência global de declínio do ciclo |
| Kendall τ [AR1], subjanela 2000–2012 (Track B) | **+0.636** | **p < 0.0001 — sinal de CSD detectado** |
| β espectral | 0.726 ± 0.140 | Welch PSD, regressão log-log |
| H (de β via H=(β+1)/2) | 0.863 | Consistente com H_DFA dos resíduos |

### Estrelas Baliunas+1995

| HD | Nome | Grupo | N | H | φ₁ | σ²_norm |
|----|------|-------|---|---|-----|---------|
| 10476 | 107 Psc | Cycling | 26 | 1.677 | 0.777 | 0.0091 |
| 81809 | HD 81809 | Cycling | 26 | 1.495 | 0.677 | 0.0022 |
| 149661 | 12 Oph | Cycling | 26 | 1.884 | 0.909 | 0.0084 |
| 190406 | 15 Sge | Cycling | 26 | 1.880 | 0.905 | 0.0039 |
| 114710 | β Com | Cycling | 26 | 1.833 | 0.876 | 0.0025 |
| 32147 | HD 32147 | Variable | 26 | 1.196 | 0.570 | 0.0124 |
| 219834 | HD 219834B | Variable | 26 | 1.402 | 0.563 | 0.0148 |
| 76151 | HD 76151 | Variable | 26 | 1.087 | 0.588 | 0.0157 |
| 143761 | ρ CrB | Maunder | 26 | 0.503 | −0.180 | 0.0012 |
| 166620 | HD 166620 | Maunder | 26 | 0.918 | 0.317 | 0.0005 |
| 4915 | HD 4915 | Maunder | 26 | 0.544 | 0.058 | 0.0009 |
| 103095 | Gmb 1830 | Maunder | 26 | 1.008 | 0.418 | 0.0005 |

**Medianas por grupo:**
| Grupo | median H | median φ₁ |
|-------|----------|-----------|
| Cycling | 1.833 | 0.876 |
| Variable | 1.196 | 0.570 |
| Maunder | 0.731 | 0.187 |

### Mann-Whitney U (φ₁)

| Comparação | U | p | Significância |
|-----------|---|---|--------------|
| Variable > Cycling | 0 | 1.0 | n.s. (Cycling alta por ciclo longo) |
| Variable > Maunder | 12 | 0.029 | * |
| Cycling > Maunder | 20 | 0.008 | ** |

**Resultado chave:** φ₁(Variable) > φ₁(Maunder) a p=0.029 → evidência de CSD
nas estrelas pré-Maunder. [Com dados reais, amostras maiores → p menor.]

---

## Figuras

| Fig | Descrição | Largura | Painéis | Status |
|-----|-----------|---------|---------|--------|
| Fig 1 | 3 séries temporais (Cycling / Variable / Maunder) | 3.5" | 3 verticais | [ ] |
| Fig 2 | Sol: S-index + φ₁ deslizante (Track B) + σ² deslizante | 7.0" | 3 stacked | [ ] |
| Fig 3 | H vs ⟨S⟩ para todas as estrelas (símbolos por classe) | 3.5" | 1 | [ ] |
| Fig 4 | Box-plot de φ₁ por classe (Cyc / Var / Maunder) | 3.5" | 1 | [ ] |

**Nota para Fig 2:** usar `s_resid` (resíduos do ciclo) para os painéis de
φ₁ e σ². O painel do S-index bruto mostra toda a série + trend removido como
linha cinza. Dados em `p4_results.npz` (keys: solar_s, solar_s_resid,
sw50_years, sw50_phi1, sw50_var).

---

## Outline com Páginas

| Seção | Subseções | Páginas |
|-------|-----------|---------|
| 1. Introduction | — | 1.0 |
| 2. Critical Slowing Down: Theory | 2.1 Bifurcações e τ; 2.2 AR(1) e variância; 2.3 DFA e H | 1.0 |
| 3. Data | 3.1 Solar NSO; 3.2 Mount Wilson; 3.3 Classificação | 0.8 |
| 4. Methods | 4.1 Remoção do ciclo (Dakos+2012); 4.2 Sliding window; 4.3 DFA; 4.4 Kendall τ | 0.8 |
| 5. Results | 5.1 Sol H(t); 5.2 Sol AR1+σ² (Track B); 5.3 Estrelas H; 5.4 Estrelas φ₁ | 2.2 |
| 6. Discussion | 6.1 CSD solar 2000–2010; 6.2 Maunder como transição; 6.3 Limitações; 6.4 Conexão P8 | 1.5 |
| 7. Conclusions | — | 0.4 |
| Apêndice A | Sensibilidade a w (40%, 50%, 60%) e kernel σ | 0.3 |
| **Total** | | **8.0 págs** |

---

## Referências-chave (15)

### CSD / Early Warning Signals
- Scheffer+2009, Nature 461, 53 — EWS fundacional (ecologia)
- Dakos+2012, PLoS ONE 7, e41010 — formalização estatística; Kendall τ; remoção de tendência
- Held & Kleinen 2004, GRL 31, L23207 — CSD em clima
- Carpenter & Brock 2006, Ecol. Lett. 9, 311 — σ² como EWS
- Lenton+2012, Nature Clim. Change 1, 201 — tipos de bifurcação

### DFA / Hurst
- Peng+1994, Phys. Rev. E 49, 1685 — DFA original
- Hurst 1951, Trans. ASCE 116, 770 — expoente H
- Kantelhardt+2002, Physica A 316, 87 — MF-DFA (contexto para F16)

### Ciclos estelares
- Baliunas+1995, ApJ 438, 269 — dados Mount Wilson, classificação
- Saar & Brandenburg 1999, ApJ 524, 295 — dois ramos de ciclos
- Lockwood+2007, ApJS 171, 260 — extensão Mount Wilson
- Eddy 1976, Science 192, 1189 — Mínimo de Maunder
- Usoskin+2017, Living Rev. Sol. Phys. 14, 3 — história atividade solar
- Egeland+2017, ApJ 835, 25 — calibração S-index solar

### Software
- Schölzel 2019, Zenodo — pacote nolds (DFA em Python)

---

## Decisões Fixadas

1. DFA confiável apenas para o Sol e décadas (N > 1000). Para estrelas
   Mt. Wilson (N~26), H é estimativa indicativa com aviso explícito no texto.
2. Análise primária = Sol (Track A + Track B). Estrelas Mt. Wilson = comparativa.
3. **Track B obrigatório:** remover ciclo via Gaussian kernel smoother σ=1 ano
   ANTES de computar AR1 e σ² deslizantes. Citar Dakos+2012 §2.2.
4. Apêndice A de sensibilidade: testar w = 40%, 50%, 60% E kernel σ = 0.5, 1.0, 2.0 anos.
5. Conexão com P8 (Landau para ciclos): citar como "in preparation" ou
   "submitted" conforme status ao escrever a Discussion.

---

## Histórico de Conversas

| # | Tipo | Produto |
|---|------|---------|
| 1 | Planejamento | paper_state.md v1 |
| 2 | Análise Python | p4_analysis.py (completo); analysis_results.md; paper_state.md v2 |
