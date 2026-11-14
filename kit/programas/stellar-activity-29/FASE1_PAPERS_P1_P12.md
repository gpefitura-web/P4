# Fase 1 — Especificação Detalhada dos Papers P1–P12
## Núcleo do Programa: SOC, Transições de Fase, Scaling, Ciclos

> **Como usar:** Carregue junto com `UNIVERSAL_PAPER_CONTEXT.md` no Project
> Knowledge do projeto individual de cada paper desta fase. Consulte a seção
> específica do paper ao abrir cada conversa de planejamento ou escrita.

---

## P1 — Universality in Stellar Flare Frequency Distributions

### Argumento central
A distribuição de frequência de flares estelares dN/dE ~ E^{-α} é prevista
pela teoria de criticalidade auto-organizada (SOC). O expoente α é uma
assinatura da classe de universalidade do sistema. Este paper testa se α
é o mesmo para estrelas M, K e G — o que indicaria universalidade — ou se
difere entre tipos espectrais, apontando para classes de universalidade
distintas como em sistemas críticos da física do estado sólido.

### Dados
| Catálogo | Referência | VizieR ID | Colunas necessárias |
|---------|-----------|----------|-------------------|
| Kepler Flare Catalog | Davenport 2016, ApJ 829, 23 | J/ApJ/829/23 | KIC ID, flare energy (erg), peak amplitude, stellar Teff |
| Kepler Input Catalog | Brown+2011, AJ 142, 112 | J/AJ/142/112 | KIC, Teff, logg, mass |

**Carregamento:**
```python
from astroquery.vizier import Vizier
Vizier.ROW_LIMIT = -1
flares = Vizier.get_catalogs('J/ApJ/829/23')[0].to_pandas()
kic    = Vizier.get_catalogs('J/AJ/142/112')[0].to_pandas()
df = flares.merge(kic[['KIC','Teff']], on='KIC', how='left')
```

### Pipeline de análise
1. Classificar estrelas por Teff: M (< 3900 K), K (3900–5200 K), G (5200–6000 K)
2. Filtrar estrelas com N_flares ≥ 10 (estatística mínima confiável)
3. Para cada grupo espectral, ajustar lei de potência via MLE:
   ```python
   import powerlaw
   fit = powerlaw.Fit(energies, discrete=False, xmin=1e32)
   alpha = fit.alpha
   sigma = fit.sigma
   R, p = fit.distribution_compare('power_law', 'lognormal')
   ```
4. Teste KS entre distribuições de grupos diferentes
5. Bootstrap (N=1000) para incertezas em α
6. Comparar α com previsões SOC: campo médio α=1.5, BTW d=2 α≈1.8

### Figuras
- **Fig 1:** Distribuição cumulativa complementar (CCDF) log-log para
  M, K, G em um único painel. 3 curvas com estilos de linha distintos
  (sólido, tracejado, pontilhado). Power-law fit sobreposto.
  Eixos: E (erg) × P(E' > E). Largura: 3.5"
- **Fig 2:** α vs Teff (ou tipo espectral no eixo x) com barras de erro
  1σ do bootstrap. Linha horizontal tracejada = média. Região sombreada
  (hachura) = 1σ da média. Largura: 3.5"

### Resultados esperados
- α ≈ 1.75–1.85 para todos os tipos (universalidade)
- Ou α(M) > α(G) indicando sistemas mais energéticos têm distribuições
  mais rasas (classes de universalidade diferentes)
- Ambos os resultados são publicáveis e interessantes

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.8 | SOC em flares solares (Lu & Hamilton 1991), gap: comparação cross-spectral |
| Data & Methods | 1.0 | Davenport 2016, critérios de seleção, método MLE, bootstrap |
| Results | 1.8 | Tabela 1 (α por tipo), Fig 1, Fig 2, teste KS |
| Discussion | 1.2 | Universalidade, dimensão SOC efetiva, comparação BTW/Ising |
| Conclusions | 0.4 | 3–4 pontos |

### Alvo: ApJ Letters | Backup: Solar Physics
### Referências-chave específicas
- Lu & Hamilton 1991 (SOC em flares solares — fundação)
- Bak, Tang & Wiesenfeld 1987 (SOC original)
- Davenport 2016 (dados)
- Shibayama+2013 (expoente α~1.8 para G dwarfs Kepler)
- Alstott+2014 (pacote powerlaw — citar obrigatório)
- Crosby+1993 (α solar = 1.53)

---

## P2 — The Stellar Activity–Rotation Transition as a Second-Order Phase Transition

### Argumento central
A relação atividade-rotação mostra dois regimes: saturação (Ro < Ro_crit)
e lei de potência Lx/Lbol ∝ Ro^{-β} (Ro > Ro_crit). Esta estrutura é
formalmente idêntica a uma transição de segunda ordem: Lx/Lbol é o
parâmetro de ordem φ, Ro é o parâmetro de controle análogo à temperatura
reduzida t = (T-Tc)/Tc, e Ro_crit é o ponto crítico. O paper extrai β
(análogo ao expoente de magnetização) e testa a relação de escala de
Rushbrooke: α + 2β + γ ≥ 2.

### Dados
| Catálogo | Referência | VizieR ID | Colunas |
|---------|-----------|----------|---------|
| Activity–rotation survey | Wright+2011, ApJ 743, 48 | J/ApJ/743/48 | Prot, Lx, Lbol, τ_conv, Rossby |
| M-dwarf activity | Reiners+2014, ApJ 794, 144 | J/ApJ/794/144 | Prot, Lx/Lbol, mass |
| Stellar ages+activity | Mamajek & Hillenbrand 2008 | via ADS | B-V, Prot, age |

**Nota:** Wright+2011 já fornece Ro calculado. Usar diretamente.

### Pipeline de análise
1. Combinar Wright+2011 + Reiners+2014 (~320 estrelas total)
2. Identificar Ro_crit visualmente (onde a lei de potência começa)
3. Ajuste simultâneo dos dois regimes com `scipy.optimize.curve_fit`:
   ```python
   def activity_model(Ro, Ro_crit, phi_sat, beta):
       return np.where(Ro < Ro_crit,
                       phi_sat,
                       phi_sat * (Ro/Ro_crit)**(-beta))
   ```
4. Extrair β com incerteza (covariância do fit)
5. Estimar γ (expoente de "susceptibilidade") via variância de Lx/Lbol
   em bins de Ro próximos a Ro_crit
6. Calcular α via calorimetria análoga: variância de dLx/dRo
7. Testar Rushbrooke: α_est + 2β + γ ≥ 2
8. Comparar β com: campo médio (0.5), Ising 2D (0.125), Ising 3D (0.326),
   XY 3D (0.345), Heisenberg 3D (0.365)

### Figuras
- **Fig 1:** Lx/Lbol vs Ro em log-log. Pontos = estrelas (diferentes
  símbolos para FGK e M). Linhas: saturação horizontal + lei de potência.
  Seta vertical em Ro_crit. Largura: 3.5"
- **Fig 2:** Resíduos do fit vs Ro próximo a Ro_crit. Mostra flutuações
  aumentando ao se aproximar do ponto crítico (critical fluctuations).
  Largura: 3.5"
- **Fig 3 (opcional):** Diagrama de comparação de β com classes de
  universalidade conhecidas (barras horizontais com valores de β para
  cada classe, ponto com barra de erro para este trabalho). Largura: 3.5"

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 1.0 | Relação atividade-rotação, Rossby number, transições de fase na astrofísica |
| Theory | 0.8 | Analogia formal: parâmetro de ordem, expoentes críticos, scaling |
| Data & Methods | 1.0 | Wright+2011, Reiners+2014, método de fit, definição de β, γ |
| Results | 2.0 | β medido, teste Rushbrooke, Fig 1, Fig 2, Tab 1 |
| Discussion | 1.5 | Classe de universalidade, limitações, implicações para dínamo |
| Conclusions | 0.5 | 4 pontos |

### Alvo: ApJ | Backup: New Astronomy
### Referências-chave específicas
- Wright+2011 (dados fundamentais)
- Reiners+2014 (dados M dwarfs)
- Pizzolato+2003 (relação atividade-rotação original)
- Pallavicini+1981 (Lx ∝ v_rot^2, primeira lei de potência)
- Noyes+1984 (número de Rossby)
- Binney+1992 Cap. 3 (expoentes críticos e classes de universalidade)

---

## P3 — Scaling Relations Among Stellar Activity Indicators

### Argumento central
As correlações empíricas entre indicadores de atividade (F_X ∝ F_MgII^3,
F_UV ∝ F_MgII^{1.5}, F_CaII ∝ F_MgII^1) formam um sistema fechado de
leis de potência. O paper demonstra que estes expoentes satisfazem uma
álgebra de consistência análoga às relações de escala de Widom e Fisher
em fenômenos críticos: se F_X ∝ F_MgII^a e F_UV ∝ F_MgII^b, então
F_X ∝ F_UV^{a/b}, e este expoente derivado deve ser consistente com a
correlação direta X vs UV. Este teste é rigoroso, quantitativo e verificável
sem nenhum dado novo.

### Dados
Paper analítico — nenhum download de catálogo necessário. Todos os
expoentes são compilados da literatura:

| Correlação | Expoente m | Referência |
|-----------|-----------|-----------|
| F_X vs F_MgII | 3.0 ± 0.2 | Ayres+1981 |
| F_UV (C IV) vs F_MgII | 1.5 ± 0.1 | Ayres+1981 |
| F_CaII vs F_MgII | 1.0 ± 0.05 | Ayres+1981 |
| F_X vs F_MgII (K/M dwarfs) | 0.75–1.27 | Youngblood+2017 |
| F_Lyα vs F_MgII | 0.82 ± 0.04 | Wood+2005 |
| F_EUV vs F_X | 0.86 ± 0.07 | Sanz-Forcada+2011 |
| F_radio vs F_X | 1.02 ± 0.17 | Güdel & Benz 1993 |

### Pipeline de análise
1. Montar matriz de expoentes (tabela acima)
2. Calcular expoentes derivados via composição:
   m_derived(X vs UV) = m(X vs MgII) / m(UV vs MgII) = 3.0/1.5 = 2.0
3. Comparar m_derived com m_direct (correlações diretas na literatura)
4. Calcular resíduo: Δm = m_direct - m_derived, com propagação de erros
5. Testar analogia com relação de Fisher: γ = ν(2-η)
   Reinterpretar: m(X vs CaII) = m(X vs MgII) × [m(CaII vs MgII)]^{-1}
6. Construir "diagrama de fases da atividade": eixos F_CaII vs F_X,
   com isólinhas de F_MgII constante

### Figuras
- **Fig 1:** Diagrama esquemático 2×2 mostrando as correlações como
  setas em um grafo (CaII → MgII → UV → X, com setas de atalho).
  Cada seta rotulada com o expoente. Estilo: SVG gerado em matplotlib
  como diagrama de rede. Largura: 3.5"
- **Fig 2:** Comparação entre m_derived e m_direct para cada par de
  indicadores. Eixo x: valor derivado; eixo y: valor direto. Linha de
  referência y=x (consistência perfeita). Largura: 3.5"

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.6 | Correlações de indicadores, lacuna: nunca testadas como scaling relations |
| Theory | 1.0 | Analogia com Widom/Fisher, definição formal de consistência algébrica |
| Analysis | 1.5 | Tabela de expoentes, cálculo de derivados, Fig 1, Fig 2 |
| Discussion | 1.0 | Implicações: estrutura térmica estelar, previsão de indicadores não observados |
| Conclusions | 0.4 | 3 pontos |

### Alvo: ApJ Letters | Backup: Astrophysics & Space Science
### Referências-chave específicas
- Ayres+1981 (correlações fundamentais)
- Youngblood+2017 (MUSCLES, K/M dwarfs)
- Wood+2005 (Lyα vs MgII)
- Güdel & Benz 1993 (rádio vs X)
- Schrijver+1987 (basal flux e correlações)
- Binney+1992 Cap. 2 (relações de escala de Widom, Fisher)

---

## P4 — Critical Slowing Down Near Stellar Activity Minima

### Argumento central
Em sistemas físicos próximos a um ponto crítico ou transição de fase,
o tempo de relaxação τ diverge (critical slowing down). Uma assinatura
observacional é o aumento do expoente de Hurst H em séries temporais:
H > 0.5 indica persistência temporal crescente. O paper aplica análise
DFA (Detrended Fluctuation Analysis) a séries longas de Ca II (Mount
Wilson HK Project) para testar se estrelas em mínimos profundos de
atividade (análogos ao Mínimo de Maunder) mostram H maior do que estrelas
em ciclos regulares — indicando que o mínimo de Maunder é uma transição
de fase da dínamo magnética.

### Dados
| Série | Fonte | Acesso | Conteúdo |
|-------|-------|--------|---------|
| S-index solar | NOAA/NSO | ftp ou doi:10.17616/R3G01S | Índice S diário, 1966–2021 |
| Mount Wilson HK | Baliunas+1995, ApJ 438, 269 | VizieR J/ApJ/438/269 | S-index anual ~100 estrelas, 1966–1991 |
| HK Project extensão | Lockwood+2007, ApJS 171, 260 | VizieR | Dados estendidos algumas estrelas |

**Nota:** Dados em formato texto simples, fáceis de carregar com `pandas.read_csv`.

### Pipeline de análise
```python
import nolds  # pip install nolds

# Para cada estrela com série temporal suficientemente longa (N > 100 pontos):
def compute_hurst(series):
    """DFA - Detrended Fluctuation Analysis."""
    H = nolds.dfa(series, nvals=None, overlap=True)
    return H

# Classificação das estrelas:
# Grupo 1: ciclos regulares (S-index varia periodicamente)
# Grupo 2: alto nível de atividade sem ciclo aparente
# Grupo 3: mínimo de Maunder (S-index muito baixo, sem ciclo)

# Para o Sol especificamente:
# Janelas: ciclo ativo (1990-2000), mínimo 2008-2010, ciclo normal 2012-2019
```

1. Baixar e parsear séries temporais do Mount Wilson
2. Classificar estrelas: Ciclo Regular / Maunder Minimum / Very Active
   (usando classificação de Baliunas+1995 como ground truth)
3. Calcular H via DFA para cada estrela (série completa)
4. Para o Sol: calcular H em janelas deslizantes (rolling window, W=5 anos)
   e verificar se H aumenta durante mínimos profundos
5. Comparar H entre os três grupos via teste Mann-Whitney U
6. Calcular também: expoente espectral β da PSD (relacionado: H = (β+1)/2)

### Figuras
- **Fig 1:** Série temporal do índice S para 3 estrelas representativas
  (uma de cada grupo), em 3 painéis verticais. Escala de tempo: anos.
  Largura: 3.5"
- **Fig 2:** H vs nível médio de atividade ⟨S⟩ para todas as estrelas.
  Símbolos diferentes para cada grupo. Linha horizontal H=0.5
  (ruído branco = sem persistência). Largura: 3.5"
- **Fig 3:** Para o Sol: H calculado em janela deslizante vs tempo
  (1966–2021). Barras verticais tracejadas marcando mínimos de ciclo.
  Largura: 7.0" (2 colunas)

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.8 | Mínimos de Maunder, DFA e critical slowing down, hipótese |
| Data & Methods | 1.0 | Mount Wilson, NSO Solar S-index, DFA, classificação dos grupos |
| Results | 2.0 | Fig 1, Fig 2, Fig 3, Tabela 1 (H por estrela) |
| Discussion | 1.2 | Interpretação como transição de fase, mínimo de Maunder como fase distinta |
| Conclusions | 0.5 | 4 pontos |

### Alvo: Solar Physics (Springer) | Backup: Space Weather (Wiley/AGU)
### Referências-chave específicas
- Baliunas+1995 (Mount Wilson, classificação de ciclos)
- Lockwood+2007 (extensão do HK Project)
- Peng+1994 (DFA original)
- Hurst 1951 (expoente H original)
- Strassmeier+1997 (revisão de ciclos estelares)
- Saar & Brandenburg 1999 (dois ramos de ciclos)

---

## P5 — The Magnetic Flux–X-ray Luminosity Power Law as a Renormalization Group Fixed Point

### Argumento central
Pevtsov+2003 mostraram que L_X ∝ Φ^{1.13±0.05} sobre 12 ordens de
magnitude, para regiões solares, o Sol inteiro e estrelas diversas.
No grupo de renormalização, um expoente de lei de potência que persiste
sobre tantas décadas para sistemas tão diferentes é a assinatura de um
ponto fixo não-trivial. O expoente p=1.13 é um expoente anômalo η≠0.
O paper analisa: (1) o valor exato de p via MLE (em vez de regressão
linear); (2) as "correções ao scaling" para valores extremos de Φ;
(3) a interpretação dos desvios como efeitos de operadores irrelevantes
no Hamiltoniano efetivo.

### Dados
| Dataset | Fonte | Acesso | Conteúdo |
|---------|-------|--------|---------|
| Tabela Pevtsov+2003 | Fig 1 do artigo | WebPlotDigitizer + tabela eletrônica ADS | Φ (Mx), L_X (erg/s) para ~300 pontos |
| Dados estelares adicionais | Vidotto+2014 | VizieR J/MNRAS/441/2361 | Φ, L_X para ~70 estrelas M |

**Extração de dados da figura:**
Usar WebPlotDigitizer (https://automeris.io/WebPlotDigitizer/) na Fig 1
de Pevtsov+2003 para extrair os pontos do gráfico log-log. Exportar CSV.

### Pipeline de análise
```python
import powerlaw
import numpy as np
from scipy import stats

# Carregar dados extraídos
phi = data['phi_Mx']      # fluxo magnético em Maxwells
lx  = data['lx_erg_s']   # luminosidade X em erg/s

# 1. Fit MLE (correto)
fit = powerlaw.Fit(lx, xmin=np.percentile(lx, 10))
# Não adequado direto — usar scipy para power-law bivariada:
log_phi = np.log10(phi)
log_lx  = np.log10(lx)

# Regressão em log-log com OLS (comparação)
slope_ols, intercept, r, p_val, se = stats.linregress(log_phi, log_lx)

# Fit com incertezas simétricas via ODR (orthogonal distance regression)
from scipy.odr import ODR, Model, Data, RealData
def power_law(B, x): return B[0] * x + B[1]
model = Model(power_law)
odr_data = RealData(log_phi, log_lx, sx=0.05, sy=0.05)
odr = ODR(odr_data, model, beta0=[1.1, 5.0])
result = odr.run()
slope_odr = result.beta[0]
slope_err = result.sd_beta[0]

# 2. Correções ao scaling: ajustar resíduos vs log(Phi)
residuals = log_lx - (slope_odr * log_phi + result.beta[1])
# Fit polinomial nos resíduos para estimar ω (expoente de correção)
```

### Figuras
- **Fig 1:** L_X vs Φ log-log (reprodução melhorada de Pevtsov+2003)
  com fit ODR. Diferentes símbolos para: regiões solares quietas, regiões
  ativas, Sol médio, estrelas G/K/M, estrelas T Tauri. Largura: 3.5"
- **Fig 2:** Resíduos do fit vs log(Φ). Mostra desvios sistemáticos
  para Φ muito baixo (regiões quietas) e muito alto (estrelas super-ativas).
  Ajuste quadrático nos resíduos. Largura: 3.5"

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.8 | Pevtsov+2003, importância da escala, motivação RG |
| Theory | 1.2 | Ponto fixo RG, expoente anômalo, correções ao scaling |
| Data & Analysis | 1.5 | Dados, método ODR, correções, Fig 1, Fig 2 |
| Discussion | 1.5 | Interpretação RG, qual campo perturbativo quebra o scaling |
| Conclusions | 0.5 | 4 pontos |

### Alvo: ApJ | Backup: New Astronomy
### Referências-chave específicas
- Pevtsov+2003 (dados fundamentais deste paper)
- Binney+1992 Cap. 4-5 (ponto fixo RG, expoente anômalo η)
- Fisher 1974 (relações de escala e expoentes anômalos)
- Vidotto+2014 (dados estelares complementares)
- Reiners+2014 (dados M dwarfs adicionais)

---

## P6 — The Basal Chromospheric Flux as a Non-Trivial Fixed Point

### Argumento central
O fluxo basal (mínimo) das linhas Ca II e Mg II depende apenas de T_eff
e g, independendo do campo magnético. No grupo de renormalização, um
comportamento que persiste independentemente da perturbação magnética é
a assinatura de um ponto fixo: o sistema sempre "flui" para o mesmo valor
mínimo quando a atividade magnética é removida. O paper distingue
formalmente dois pontos fixos: o "trivial" (fluxo basal = aquecimento
acústico puro) e o "não-trivial" (ponto de saturação = máximo de atividade
magnética), e discute qual perturbação é relevante para cada um.

### Dados
Paper analítico — compilação da literatura:

| Quantidade | Valor | Referência |
|-----------|-------|-----------|
| Fluxo basal Ca II H (K2V) | 4.5 × 10^5 erg cm^{-2} s^{-1} | Schrijver 1987 |
| Fluxo basal Mg II k (K2V) | 1.2 × 10^6 erg cm^{-2} s^{-1} | Oranje & Zwaan 1985 |
| Dependência T_eff do basal | ∝ T_eff^{4.3} | Pérez Martínez+2014 |
| Fluxo de saturação Ca II | ~10^7 erg cm^{-2} s^{-1} | Noyes+1984 |
| Fluxo basal C II (upper chrom) | 4–7× acima da previsão acústica | Judge+2003 |

### Pipeline de análise
1. Compilar fluxos basais de Ca II e Mg II para estrelas de diferentes
   T_eff (dados de Schrijver 1987, tabela extraída do ADS)
2. Ajustar F_basal(T_eff) = A × T_eff^γ para cada linha
3. Calcular a razão F_basal / F_sat como função de T_eff
4. Mostrar que essa razão é constante (independente de outros parâmetros)
5. Formalizar: definir o "espaço de teoria" com eixos (F_mag, T_eff)
   e mostrar o fluxo RG esquemático (diagrama qualitativo)
6. Discutir o papel do aquecimento acústico como "operador irrelevante"
   que não muda a classe de universalidade

### Figuras
- **Fig 1:** F_basal vs T_eff para Ca II e Mg II. Pontos = observações.
  Linha = fit de lei de potência. Dois painéis lado a lado. Largura: 7.0"
- **Fig 2:** Diagrama esquemático do "espaço de teoria" com fluxo RG.
  Eixo x: intensidade do campo magnético. Eixo y: fluxo de atividade.
  Setas mostrando o fluxo em direção aos dois pontos fixos (basal e
  saturação). Estilo: diagrama de fase qualitativo. Largura: 3.5"

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.7 | Fluxo basal, aquecimento acústico vs magnético |
| Theory | 1.0 | Pontos fixos RG, operadores relevantes e irrelevantes |
| Analysis | 1.3 | Dados de fluxo basal, fits, razão basal/saturação |
| Discussion | 1.0 | Interpretação RG, implicações para modelos de cromosfera |
| Conclusions | 0.4 | 3 pontos |

### Alvo: ApJ Letters | Backup: Astrophysics & Space Science
### Referências-chave específicas
- Schrijver 1987 (fluxo basal, referência fundamental)
- Pérez Martínez+2014 (cálculos PHOENIX para fluxo basal)
- Oranje & Zwaan 1985 (fluxo basal original)
- Judge+2003 (aquecimento magnético residual no upper chromosphere)
- Schröder+2012 (fluxo basal durante mínimo solar 2009-2010)
- Binney+1992 Cap. 5 (pontos fixos e operadores irrelevantes)

---

## P7 — Finite-Size Scaling in Stellar Flare Statistics

### Argumento central
Em sistemas críticos finitos, a distribuição em lei de potência tem um
cutoff exponencial em E_max que escala com o "tamanho" do sistema:
E_max ∝ L^{d_f}. Para flares estelares, E_max deve escalar com parâmetros
da estrela. O paper determina empiricamente como E_max escala com massa
estelar, raio e proxy de campo magnético (usando L_X como proxy de B),
e testa se a distribuição normalizada por E_max colapsa sobre uma curva
universal (finite-size scaling collapse).

### Dados
| Catálogo | Referência | VizieR ID | Colunas |
|---------|-----------|----------|---------|
| Kepler Flare Catalog | Davenport 2016 | J/ApJ/829/23 | KIC, flare energy |
| KIC stellar parameters | Brown+2011 | J/AJ/142/112 | KIC, mass, radius, Teff |
| Kepler rotation | McQuillan+2014 | J/ApJS/211/24 | KIC, Prot |

**Cruzamento dos catálogos:**
```python
df = flares.merge(kic_params, on='KIC').merge(prot_catalog, on='KIC', how='left')
# Filtrar: N_flares >= 20 por estrela para estimar E_max de forma robusta
# E_max estimado como percentil 99 das energias de flares por estrela
```

### Pipeline de análise
```python
# Para cada estrela com N_flares >= 20:
star_stats = df.groupby('KIC').agg(
    E_max = ('flare_energy', lambda x: np.percentile(x, 99)),
    E_mean = ('flare_energy', 'mean'),
    N = ('flare_energy', 'count'),
    mass = ('mass', 'first'),
    radius = ('radius', 'first'),
    Lx_proxy = ('Lx', 'first')  # se disponível
)

# Ajuste: E_max ∝ mass^a * radius^b
from scipy.optimize import curve_fit
def emax_model(X, a, b, C):
    mass, radius = X
    return C * mass**a * radius**b

# Finite-size scaling collapse:
# Normalizar energias: e = E / E_max(star)
# Plotar P(e) para todas as estrelas — devem colapsar
```

### Figuras
- **Fig 1:** E_max vs massa estelar (estrelas individuais como pontos).
  Ajuste lei de potência. Largura: 3.5"
- **Fig 2:** Finite-size scaling collapse: distribuições P(E/E_max) para
  estrelas de diferentes massas em um mesmo gráfico log-log. Se colapsam
  → scaling universal. Largura: 3.5"

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.8 | Finite-size scaling em física, flares e parâmetros estelares |
| Theory | 0.8 | Hipótese de scaling, definição de E_max, predições |
| Data & Methods | 1.0 | Davenport+2016, KIC, critérios de seleção, estimativa E_max |
| Results | 2.0 | Fig 1, Fig 2, expoentes a e b, qualidade do colapso |
| Discussion | 1.2 | Interpretação, dimensão fractal d_f implícita, comparação com BTW |
| Conclusions | 0.4 | 3–4 pontos |

### Alvo: ApJ | Backup: New Astronomy
### Referências-chave específicas
- Davenport 2016 (dados)
- Binder 1981 (finite-size scaling em física estatística)
- Cardy 1988 (finite-size scaling: teoria)
- Shibayama+2013 (E_max para G dwarfs Kepler)
- Aschwanden+2012 (SOC em flares solares, finite-size effects)

---

## P8 — Landau Theory of Stellar Activity Cycles

### Argumento central
Os ciclos de atividade estelar podem ser descritos por uma teoria de
Landau: o campo magnético médio B̄ é o parâmetro de ordem, e a energia
livre tem a forma F(B̄) = a(Ro)B̄² + bB̄⁴. A transição de B̄=0 (estrela
sem ciclo ou em Maunder minimum) para B̄≠0 (ciclo ativo) é uma bifurcação
de pitchfork supercrítica. Os coeficientes a e b, expressos em função do
número de Rossby, permitem predizer o período e amplitude dos ciclos em
função de Ro. O paper ajusta a(Ro) aos dados de ciclos do Mount Wilson
e testa a predição de amplitude de ciclo.

### Dados
| Catálogo | Conteúdo | Acesso |
|---------|---------|--------|
| Baliunas+1995 | Períodos de ciclo, amplitude ΔS, Prot para ~40 estrelas | VizieR J/ApJ/438/269 |
| Saar & Brandenburg 1999 | Dois ramos de ciclos (active/inactive) | Tabela no artigo |
| Wright+2011 | Ro para as estrelas do Mount Wilson | VizieR J/ApJ/743/48 |
| Böhm-Vitense 2007 | Extensão dos dois ramos | Tabela no artigo |

### Pipeline de análise
```python
# Modelo de Landau para o período de ciclo:
# P_cyc ∝ |a(Ro)|^{-1/2} (período diverge ao se aproximar da transição)
# Amplitude: ΔB ∝ |a(Ro)|^{1/2} (ordem do parâmetro de ordem)

# 1. Para cada estrela: calcular Ro usando Prot e τ_conv (Wright+2011)
# 2. Ajustar a(Ro) = a0 * (Ro - Ro_cyc) onde Ro_cyc é o Rossby crítico
#    para o início dos ciclos
# 3. Predição do período: P_cyc = C / sqrt(a0 * |Ro - Ro_cyc|)
# 4. Comparar com P_cyc observado

from scipy.optimize import minimize

def landau_period(Ro, Ro_cyc, a0, C):
    """Período de ciclo predito pela teoria de Landau."""
    epsilon = Ro - Ro_cyc
    return C / np.sqrt(a0 * np.abs(epsilon))

# Também ajustar amplitude:
def landau_amplitude(Ro, Ro_cyc, a0, A):
    epsilon = Ro - Ro_cyc
    return A * np.sqrt(a0 * np.abs(epsilon))
```

### Figuras
- **Fig 1:** Período de ciclo P_cyc vs número de Rossby Ro. Dois ramos
  (active e inactive). Curvas de ajuste do modelo de Landau. Linha
  vertical em Ro_cyc. Largura: 3.5"
- **Fig 2:** Amplitude do ciclo ΔS vs Ro. Comparação com predição
  de Landau (amplitude ∝ |Ro - Ro_cyc|^{1/2}). Largura: 3.5"
- **Fig 3:** Esquema da energia livre F(B̄) para Ro > Ro_cyc (um mínimo
  em B̄=0), Ro = Ro_cyc (inflexão), e Ro < Ro_cyc (dois mínimos).
  Diagrama qualitativo tipo "Mexican hat". Largura: 3.5"

### Outline do manuscrito
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.8 | Ciclos estelares, dois ramos, gap de Vaughan-Preston |
| Theory | 1.5 | Teoria de Landau, F(φ), bifurcação, predições de período e amplitude |
| Data & Methods | 0.8 | Mount Wilson, Ro calculado, método de ajuste |
| Results | 2.0 | Fig 1, Fig 2, Fig 3, Tabela de coeficientes |
| Discussion | 1.5 | Implicações para dínamo, limitações, conexão com P9 |
| Conclusions | 0.5 | 4 pontos |

### Alvo: Solar Physics (Springer) | Backup: ApJ
### Referências-chave específicas
- Baliunas+1995 (dados de ciclos)
- Saar & Brandenburg 1999 (dois ramos de ciclos)
- Böhm-Vitense 2007 (extensão dos ramos)
- Noyes+1984 (Rossby number)
- Binney+1992 Cap. 3 (teoria de Landau, bifurcações)
- Brandenburg+2017 (revisão de ciclos estelares)

---

## P9 — The Rossby Number as SOC Control Parameter in K and M Dwarfs

### Argumento central (versão reformulada — sem fotometria)
Se o expoente α da distribuição de flares é o parâmetro de ordem de uma
transição SOC, e o número de Rossby Ro controla a intensidade da atividade
magnética, então α deve variar sistematicamente com Ro. Paper reformulado
(v. original substituído por ser fotometria-free): usa o catálogo de flares
Kepler (Davenport 2016) cruzado com rotações McQuillan+2014 e τ_conv de
Wright+2011 para medir α como função de Ro, e testa se α(Ro) tem a
assinatura de um parâmetro de ordem crítico.

### Dados
| Catálogo | VizieR ID | Colunas |
|---------|----------|---------|
| Davenport 2016 | J/ApJ/829/23 | KIC, flare energy, N flares |
| McQuillan+2014 | J/ApJS/211/24 | KIC, Prot |
| Wright+2011 | J/ApJ/743/48 | Teff→τ_conv via tabela de convection |

**Cruzamento:**
```python
df = flares.groupby('KIC').agg(
    energies = ('flare_energy', list),
    N = ('flare_energy', 'count')
).reset_index()
df = df.merge(prot[['KIC','Prot']], on='KIC')
df = df.merge(wright_tconv[['KIC','tau_conv']], on='KIC', how='left')
df['Ro'] = df['Prot'] / df['tau_conv']
```

### Pipeline de análise
```python
# Para cada estrela com N_flares >= 15:
results = []
for idx, row in df[df['N'] >= 15].iterrows():
    fit = powerlaw.Fit(row['energies'], discrete=False, xmin=1e32)
    results.append({'KIC': row['KIC'], 'alpha': fit.alpha,
                    'sigma': fit.sigma, 'Ro': row['Ro']})

res = pd.DataFrame(results)

# Binning em Ro e ajuste α(Ro):
ro_bins = np.logspace(np.log10(res.Ro.min()), np.log10(res.Ro.max()), 10)
binned = res.groupby(pd.cut(res.Ro, ro_bins)).agg(
    alpha_mean=('alpha','mean'),
    alpha_std=('alpha','std'),
    Ro_mid=('Ro','median')
)
```

### Figuras
- **Fig 1:** α vs Ro (pontos individuais + médias em bins). Barra de erro.
  Linha tracejada = α = 2 (previsão BTW). Largura: 3.5"
- **Fig 2:** α vs L_X/L_bol (usando L_X de Wright+2011 onde disponível).
  Conexão com P2. Largura: 3.5"

### Outline
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.8 | SOC e parâmetros de controle, motivação |
| Data & Methods | 1.0 | Davenport+McQuillan+Wright, cruzamento, powerlaw MLE |
| Results | 2.0 | α(Ro), Fig 1, Fig 2 |
| Discussion | 1.2 | α como parâmetro de ordem, conexão com P2 (saturação) |
| Conclusions | 0.4 | 3 pontos |

### Alvo: ApJ Letters | Backup: New Astronomy
### Referências-chave específicas
- Davenport 2016, McQuillan+2014, Wright+2011 (dados)
- Noyes+1984 (Rossby number)
- Lu & Hamilton 1991 (SOC como mecanismo)
- Aschwanden+2014 (SOC em astrofísica, revisão)

---

## P10 — Activity Indicator Power-Law Correlations in MUSCLES K and M Dwarfs

### Argumento central
Os 11 sistemas estelares do MUSCLES Treasury Survey têm os espectros UV/X
mais completos e de maior qualidade disponíveis para estrelas K e M. Este
paper usa esses dados para refinar os índices de potência entre indicadores
de atividade com alta precisão, e testa formalmente se os expoentes
satisfazem as relações de consistência algébrica derivadas em P3.

### Dados
| Dataset | Repositório | Acesso | Conteúdo |
|---------|------------|--------|---------|
| MUSCLES Spectral Archive | MAST (STScI) | mast.stsci.edu/search/hst | Fluxos UV+X tabulados para 11 estrelas |
| Youngblood+2017 Tabela 3 | ApJS 229, 43 | ADS | Fluxos de linhas individuais |
| France+2016 Tabela 1 | ApJ 820, 89 | ADS | FUV/NUV fluxos por estrela |

**Download MAST:**
```python
from astroquery.mast import Observations
obs = Observations.query_criteria(
    project='MUSCLES',
    dataproduct_type='spectrum'
)
# Ou usar diretamente as tabelas do artigo Youngblood+2017
```

### Pipeline de análise
```python
# Indicadores de atividade disponíveis no MUSCLES:
# Lyα, Mg II h+k, C II, C IV, N V, Si III, Si IV (UV)
# X-ray flux (Chandra/XMM integrado)
# He II 30.4 nm (EUV reconstruído)

# Para cada par (linha_1, linha_2):
from scipy.stats import spearmanr
from scipy.optimize import curve_fit

def powerlaw_fit(x, y):
    """Ajuste log-log com OLS."""
    log_x, log_y = np.log10(x), np.log10(y)
    slope, intercept, r, p, se = stats.linregress(log_x, log_y)
    return slope, se, r**2

# Construir matriz de expoentes N×N onde N = número de indicadores
# Testar consistência: m(A vs C) = m(A vs B) × m(B vs C)?
```

### Figuras
- **Fig 1:** Painel 3×3 de correlações (Lyα, CIV, X-ray) vs (MgII, CaII,
  Hα). 9 subpainéis em log-log. Power-law fits. Largura: 7.0"
- **Fig 2:** Matriz de expoentes derivados vs medidos. Diagrama de
  consistência (análogo ao Fig 2 de P3, mas com dados reais MUSCLES).
  Largura: 3.5"

### Outline
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 0.7 | MUSCLES, correlações de indicadores, hipótese de consistência |
| Data | 0.8 | MUSCLES 11 estrelas, linhas usadas, fluxos |
| Analysis | 2.0 | Matriz de expoentes, Fig 1, Fig 2, teste de consistência |
| Discussion | 1.0 | Comparação com Ayres+1981, implicações para estrutura atmosférica |
| Conclusions | 0.4 | 3 pontos |

### Alvo: AJ (IOP) | Backup: New Astronomy
### Referências-chave específicas
- France+2016 (MUSCLES survey overview)
- Youngblood+2016, 2017 (MUSCLES fluxes)
- Ayres+1981 (correlações originais — comparação)
- Linsky+2013 (Lyα correlations)

---

## P11 — Universality Class of the Stellar Activity–Rossby Transition

### Argumento central
Extensão rigorosa de P2: usando o catálogo combinado Wright+2011 +
Pizzolato+2003 + Reiners+2014 + Vidotto+2014 (~250 estrelas total), este
paper calcula múltiplos expoentes críticos (β, γ, δ, ν̂) para a transição
de atividade-rotação e testa se o conjunto {β, γ, δ, ν̂} satisfaz as
relações de escala termodinâmicas de Widom (γ = β(δ-1)), Rushbrooke
(α + 2β + γ = 2) e Fisher (γ = ν(2-η)). A identificação da classe de
universalidade (campo médio vs Ising 3D vs XY 3D) é o resultado central.

### Dados
| Catálogo | VizieR ID | N estrelas | Conteúdo |
|---------|----------|-----------|---------|
| Wright+2011 | J/ApJ/743/48 | ~820 | Lx, Lbol, Prot, Ro |
| Pizzolato+2003 | J/A+A/397/147 | ~150 | Lx, Lbol, Prot |
| Reiners+2014 | J/ApJ/794/144 | ~800 estrelas M | Lx/Lbol, Prot |
| Vidotto+2014 | J/MNRAS/441/2361 | ~70 | B, Lx, Prot |

### Pipeline de análise
```python
# Combinar catálogos, remover duplicatas por coordenadas

# Definições dos expoentes:
# β: Lx/Lbol ∝ |Ro - Ro_c|^β  (regime Ro > Ro_c)
# γ: d(Lx/Lbol)/dRo ∝ |Ro - Ro_c|^{-γ}  (susceptibility analog)
# δ: Lx/Lbol|_{Ro=Ro_c} ∝ h^{1/δ}  onde h = external field proxy
# ν: correlation length ξ ∝ |Ro - Ro_c|^{-ν}
#    proxy: scatter em Lx/Lbol como função de Ro

# Verificar relações de escala:
# Widom:    gamma = beta * (delta - 1)
# Rushbrooke: alpha + 2*beta + gamma >= 2
# Fisher:   gamma = nu * (2 - eta)

# Comparação com universality classes:
classes = {
    'Mean field': {'beta':0.5, 'gamma':1.0, 'delta':3.0, 'nu':0.5, 'eta':0.0},
    'Ising 3D':   {'beta':0.326, 'gamma':1.237, 'delta':4.79, 'nu':0.630, 'eta':0.036},
    'XY 3D':      {'beta':0.345, 'gamma':1.316, 'delta':4.81, 'nu':0.671, 'eta':0.038},
    'Heisenberg': {'beta':0.365, 'gamma':1.395, 'delta':4.82, 'nu':0.705, 'eta':0.036},
}
```

### Figuras
- **Fig 1:** Diagrama de fase: Lx/Lbol vs Ro com todos os ~250 pontos.
  Fit duplo (saturação + lei de potência). Largura: 7.0"
- **Fig 2:** Gráfico de "spider web" ou radar comparando os expoentes
  medidos com as 4 classes de universalidade. Alternativa: tabela visual
  com código de cores para ±1σ de consistência. Largura: 3.5"
- **Fig 3:** Verificação das relações de escala: gráfico de Widom
  γ_obs vs β_obs(δ_obs-1) com linha de referência y=x. Largura: 3.5"

### Outline
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 1.0 | Relação atividade-rotação, P2 como base, questão da universalidade |
| Theory | 1.2 | Expoentes críticos, relações de escala, classes de universalidade |
| Data & Methods | 1.0 | Catálogos combinados, definição operacional dos expoentes |
| Results | 2.5 | Fig 1, Fig 2, Fig 3, Tabela de expoentes |
| Discussion | 1.5 | Identificação da classe, implicações para física da dínamo |
| Conclusions | 0.5 | 4 pontos |

### Alvo: ApJ | Backup: Astrophysics & Space Science
### Referências-chave específicas
- Wright+2011, Pizzolato+2003, Reiners+2014 (dados)
- Binney+1992 Cap. 2 (relações de escala, classes de universalidade)
- Wilson 1974 (RG e universalidade — Nobel lecture)
- Fisher 1974 (expoentes críticos, relações de escala)

---

## P12 — From Stellar Activity to Exoplanet Habitability: A Critical Phase Diagram

### Argumento central
A taxa de escape atmosférico de um exoplanet depende do fluxo EUV/X da
estrela hospedeira, que por sua vez depende da atividade (Lx/Lbol) e da
idade. Usando os resultados dos papers P1–P11 (atividade como parâmetro
de ordem com dependência em Ro e tempo), o paper constrói um "diagrama
de fases da habitabilidade" no espaço (Ro, idade): regiões onde a atmosfera
de um planeta tipo Terra é estável vs regiões onde é destruída. A fronteira
entre essas regiões é uma "linha crítica" no espaço de parâmetros — análoga
a uma linha de coexistência de fases.

### Dados
Paper de síntese — combina resultados dos papers P1–P11 com modelos
de fuga atmosférica da literatura:

| Quantidade | Fonte |
|-----------|-------|
| L_X(Ro, t) | Resultados de P2 + P11 + Ribas+2005 |
| L_EUV(Ro, t) | Sanz-Forcada+2011, Ribas+2005 |
| Modelos de fuga | Owen & Jackson 2012, Lopez+2012 |
| Zona habitável | Kopparapu+2013 |
| τ_conv(M) | Wright+2011, Cranmer & Saar 2011 |

### Pipeline de análise
```python
import numpy as np

# Grade de parâmetros: massa estelar M e Ro inicial
M_grid = np.linspace(0.3, 1.2, 50)  # M_sun
Ro_grid = np.logspace(-2, 0, 50)    # adimensional

# Para cada ponto (M, Ro):
# 1. Calcular evolução temporal: Ro(t) via Skumanich + Wright+2011
# 2. Integrar fluência EUV/X de t=0.1 Gyr até t=5 Gyr:
#    F_EUV(t) = F_EUV,0 * (t/t0)^alpha  (Ribas+2005)
#    Fluência = integral de F_EUV dt
# 3. Calcular perda de atmosfera total:
#    dM_atm/dt ∝ L_X * R_p^3 / (G * M_p * rho_p * a^2)
# 4. Classificar: atmosfera retida (> 50% massa inicial) ou destruída

# Linha crítica: lugar geométrico dos pontos (M, Ro_ini) onde
# a atmosfera é marginalmente retida após 5 Gyr
```

### Figuras
- **Fig 1:** Diagrama de fases no plano (M_estelar, Ro_inicial).
  Regiões coloridas por hachura: "habitável" (atmosfera retida) e
  "hostil" (atmosfera destruída). Linha crítica tracejada na fronteira.
  Pontos: sistemas conhecidos (Proxima Cen b, TRAPPIST-1e, etc.).
  Largura: 7.0"
- **Fig 2:** L_EUV(t) para 3 estrelas representativas (Ro alto, médio,
  baixo). Integral sombreada = fluência total. Largura: 3.5"

### Outline
| Seção | Páginas | Conteúdo |
|-------|---------|---------|
| Introduction | 1.0 | Fuga atmosférica, papel da atividade, diagrama de fases |
| Theory & Modeling | 2.0 | L_X(Ro,t), fuga atmosférica, definição da linha crítica |
| Results | 2.5 | Fig 1, Fig 2, sistemas conhecidos no diagrama |
| Discussion | 1.5 | Implicações para habitabilidade, limitações, predições |
| Conclusions | 0.5 | 4 pontos |

### Alvo: ApJ | Backup: Advances in Space Research (Elsevier)
### Referências-chave específicas
- Ribas+2005 (evolução temporal do fluxo EUV/X)
- Owen & Jackson 2012 (modelos de fuga atmosférica)
- Kopparapu+2013 (zona habitável)
- Linsky 2019 (Caps 11, 12 — habitabilidade e flares)
- Sanz-Forcada+2011 (L_EUV vs L_X)
- Skumanich 1972 (lei de decaimento rotacional)

---

## Ordem de Execução Recomendada na Fase 1

| Prioridade | Paper | Justificativa |
|-----------|-------|--------------|
| 1º | **P3** | Analítico puro, sem download de dados — escreve em 1 semana |
| 2º | **P6** | Analítico puro, estabelece vocabulário RG — escreve em 1 semana |
| 3º | **P1** | Pipeline base (powerlaw + Davenport) — todos os outros usam isso |
| 4º | **P2** | Usa metodologia de P1, dados simples (Wright+2011) |
| 5º | **P9** | Extensão natural de P1+P2 |
| 6º | **P4** | Dados espectroscópicos (Mount Wilson), metodologia DFA |
| 7º | **P5** | Mais teórico, depende de entender P2 bem |
| 8º | **P7** | Usa pipeline de P1 + cruzamento de catálogos |
| 9º | **P8** | Modelo de Landau — precisa entender a linguagem de P2+P5 |
| 10º | **P10** | Dados MAST, extensão de P3 com dados reais |
| 11º | **P11** | Extensão de P2 — escrever depois que P2 foi aceito |
| 12º | **P12** | Síntese de toda a Fase 1 — escrever por último |

---

*Fase 1 — Versão 1.0 | Usar junto com UNIVERSAL_PAPER_CONTEXT.md*
