# REPORT — fatos do pipeline_v2 (execução única, sem interpretação)

Cada tabela cita o arquivo de origem em `pipeline_v2/results/`. Sementes fixas (base 20261124), 1 000 surrogates ARMA(p,q), p, q ∈ {0,1,2} por AIC. `p_upper` = P(τ* ≥ τ) (direção CSD); `p_D22` = P(τ* ≤ τ) (D22 literal). Configurações de tendência: none, s1, s3, s5 (σ em anos). Concordância = nº de configurações com τ > 0 e p_upper < 0.05.

## 1. Segmentos e amostra (`segments.csv`)

| HD | grupo | fonte | seg_year0 | L | n_filled | precisao | rodou | motivo | bv | bv_fonte | banda_Rphot | exploratorio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3795 | Var | Baum | 1966.000 | 29.000 | 1.000 | baixa | sim |  | 0.684 | CLS V | DENTRO | sim |
| 4628 | CYCLE_Excellent | Baum | 1966.000 | 30.000 | 0.000 | baixa | sim |  | 0.850 | CLS V | EXTRAPOLADO (0.82-1.0) | sim |
| 10476 | CYCLE_Excellent | Baum | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.801 | CLS V | DENTRO | sim |
| 10700 | Flat_limpa | Baum | 1967.000 | 29.000 | 0.000 | baixa | sim |  | 0.664 | CLS V | DENTRO | sim |
| 22072 | Var | Baum |  |  |  |  | nao | indicador_elegivel_D100 = nao (segmento MW < 24 anos): so descricao |  |  |  |  |
| 23249 | Flat_limpa | Baum | 1967.000 | 29.000 | 0.000 | baixa | sim |  | 0.882 | CLS V | EXTRAPOLADO (0.82-1.0) | sim |
| 25998 | Long | v2001 | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.460 | B95 | DENTRO | sim |
| 26965 | CYCLE_Excellent | Baum | 1967.000 | 29.000 | 0.000 | baixa | sim |  | 0.762 | CLS V | DENTRO | sim |
| 35296 | Long | v2001 | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.530 | B95 | DENTRO | sim |
| 39587 | Var | v2001 | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.590 | B95 | DENTRO | sim |
| 72905 | Var | Baum |  |  |  |  | nao | indicador_elegivel_D100 = nao (segmento MW < 24 anos): so descricao |  |  |  |  |
| 75332 | Var | v2001 | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.490 | B95 | DENTRO | sim |
| 101501 | Var | Baum | 1968.000 | 28.000 | 0.000 | baixa | sim |  | 0.701 | CLS V | DENTRO | sim |
| 103095 | CYCLE_Excellent | v2001 | 1968.000 | 34.000 | 0.000 | baixa | sim |  | 0.665 | CLS V | DENTRO | sim |
| 115383 | Var | v2001 | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.580 | B95 | DENTRO | sim |
| 115617 | Var | Baum |  |  |  |  | nao | indicador_elegivel_D100 = nao (segmento MW < 24 anos): so descricao |  |  |  |  |
| 129333 | Var | v2001 |  |  |  |  | nao | indicador_elegivel_D100 = nao (segmento MW < 24 anos): so descricao |  |  |  |  |
| 131156A | Var | v2001 | 1967.000 | 35.000 | 0.000 | baixa | sim |  | 0.760 | B95 | DENTRO | sim |
| 141004 | Long | Baum | 1966.000 | 30.000 | 1.000 | baixa | sim |  | 0.592 | CLS V | DENTRO | sim |
| 152391 | CYCLE_Excellent | Baum | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.725 | CLS V | DENTRO | sim |
| 160346 | CYCLE_Excellent | v2001 | 1966.000 | 36.000 | 0.000 | baixa | sim |  | 0.960 | B95 | EXTRAPOLADO (0.82-1.0) | sim |
| 166620 | CYCLE_Excellent | Baum | 1966.000 | 30.000 | 0.000 | baixa | sim |  | 0.827 | CLS V | EXTRAPOLADO (0.82-1.0) | sim |
| 176095 | Long | v2001 | 1966.000 | 36.000 | 1.000 | baixa | sim |  | 0.460 | B95 | DENTRO | sim |
| 182572 | Flat_limpa | Baum | 1967.000 | 35.000 | 10.000 | baixa | sim |  | 0.728 | CLS V | DENTRO | sim |
| 190360 | Flat_limpa | Baum | 1967.000 | 28.000 | 5.000 | baixa | sim |  | 0.725 | CLS V | DENTRO | sim |
| 201091 | CYCLE_Excellent | v2001 | 1967.000 | 35.000 | 0.000 | baixa | sim |  | 1.153 | CLS V | EXTRAPOLADO (>1.0, incerteza ate 20 %) | sim |
| 217014 | Var | Baum | 1966.000 | 30.000 | 4.000 | baixa | sim |  | 0.653 | CLS V | DENTRO | sim |
| (Sun) | CYCLE_Excellent | Egeland2017_T4 | 1966.000 | 51.000 | 2.000 | adequada | sim |  | 0.660 | B95 | DENTRO | sim |

## 2. H1 — HD 166620, σ_S por estado (`h1.json`; fonte: Luhn+2022 Tabela 2)

| estado | n | mean | sigma_raw | noise | sigma_A | sigma_B | n_seasons |
|---|---|---|---|---|---|---|---|
| min1 | 44 | 0.18104 | 0.0034562 | 0.0021725 | 0.0026881 | 0.0027903 | 4 |
| min2 | 315 | 0.17239 | 0.0057978 | 0.0020687 | 0.0054162 | 0.0047894 | 4 |
| grand | 103 | 0.17054 | 0.0020138 | 0.00051163 | 0.0019477 | 0.0015457 | 9 |

| comparacao | variancias | F | p_unilateral | p_bilateral |
|---|---|---|---|---|
| min1_vs_grand | raw | 2.946 | 4.399e-06 | 8.798e-06 |
| min1_vs_grand | corrected_A | 1.905 | 0.004341 | 0.008682 |
| min1_vs_grand | corrected_B | 3.259 | 5.603e-07 | 1.121e-06 |
| min2_vs_grand | raw | 8.289 | 7.084e-27 | 1.417e-26 |
| min2_vs_grand | corrected_A | 7.733 | 1.41e-25 | 2.82e-25 |
| min2_vs_grand | corrected_B | 9.6 | 1.132e-29 | 2.263e-29 |

## 3. Indicador temporal por segmento, série S, janela 50 % (`star_results.csv`)

H2 (exploratório, n = 1): linhas de HD 166620. Sol: exploratório (série composta de Egeland).

### 3.1 AR(1) lag-1

| HD | grupo | seg_year0 | L | tau_none | tau_s1 | tau_s3 | tau_s5 | p_upper_none | p_upper_s1 | p_upper_s3 | p_upper_s5 | p_D22_none | p_D22_s1 | p_D22_s3 | p_D22_s5 | concordantes_de_4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (Sun) | CYCLE_Excellent | 1966 | 51 | 0.255 | 0.249 | 0.249 | 0.255 | 0.321 | 0.272 | 0.329 | 0.306 | 0.683 | 0.731 | 0.677 | 0.698 | 0 |
| 101501 | Var | 1968 | 28 | 0.714 | 0.352 | 0.410 | 0.695 | 0.065 | 0.278 | 0.272 | 0.106 | 0.943 | 0.731 | 0.740 | 0.907 | 0 |
| 103095 | CYCLE_Excellent | 1968 | 34 | -0.438 | -0.686 | -0.503 | -0.451 | 0.796 | 0.925 | 0.835 | 0.850 | 0.214 | 0.083 | 0.173 | 0.156 | 0 |
| 10476 | CYCLE_Excellent | 1966 | 36 | 0.135 | -0.345 | -0.228 | -0.088 | 0.396 | 0.712 | 0.686 | 0.614 | 0.619 | 0.296 | 0.323 | 0.399 | 0 |
| 10700 | Flat_limpa | 1967 | 29 | -0.100 | -0.567 | -0.617 | -0.450 | 0.566 | 0.852 | 0.885 | 0.809 | 0.447 | 0.159 | 0.129 | 0.206 | 0 |
| 115383 | Var | 1966 | 36 | 0.263 | -0.053 | -0.053 | -0.170 | 0.323 | 0.544 | 0.532 | 0.617 | 0.683 | 0.461 | 0.476 | 0.393 | 0 |
| 131156A | Var | 1967 | 35 | 0.150 | 0.046 | 0.229 | 0.294 | 0.413 | 0.495 | 0.378 | 0.318 | 0.596 | 0.510 | 0.633 | 0.689 | 0 |
| 141004 | Long | 1966 | 30 | 0.700 | -0.367 | -0.150 | 0.183 | 0.064 | 0.696 | 0.580 | 0.371 | 0.946 | 0.318 | 0.430 | 0.641 | 0 |
| 152391 | CYCLE_Excellent | 1966 | 36 | -0.474 | 0.439 | -0.392 | -0.544 | 0.814 | 0.253 | 0.707 | 0.781 | 0.199 | 0.755 | 0.304 | 0.226 | 0 |
| 160346 | CYCLE_Excellent | 1966 | 36 | -0.111 | -0.263 | 0.088 | 0.228 | 0.606 | 0.667 | 0.419 | 0.365 | 0.402 | 0.344 | 0.593 | 0.643 | 0 |
| 166620 | CYCLE_Excellent | 1966 | 30 | 0.400 | 0.550 | 0.267 | 0.333 | 0.276 | 0.197 | 0.345 | 0.335 | 0.731 | 0.814 | 0.670 | 0.678 | 0 |
| 176095 | Long | 1966 | 36 | -0.240 | -0.333 | -0.193 | -0.158 | 0.564 | 0.522 | 0.528 | 0.485 | 0.446 | 0.489 | 0.477 | 0.520 | 0 |
| 182572 | Flat_limpa | 1967 | 35 | -0.399 | -0.582 | -0.569 | -0.438 | 0.766 | 0.577 | 0.810 | 0.758 | 0.243 | 0.449 | 0.197 | 0.250 | 0 |
| 190360 | Flat_limpa | 1967 | 28 | -0.829 | -0.352 | -0.848 | -0.810 | 0.988 | 0.297 | 0.978 | 0.967 | 0.019 | 0.722 | 0.030 | 0.046 | 0 |
| 201091 | CYCLE_Excellent | 1967 | 35 | -0.046 | 0.242 | 0.046 | 0.111 | 0.537 | 0.391 | 0.473 | 0.424 | 0.476 | 0.620 | 0.532 | 0.581 | 0 |
| 217014 | Var | 1966 | 30 | 0.067 | 0.183 | -0.250 | -0.317 | 0.225 | 0.026 | 0.327 | 0.461 | 0.781 | 0.976 | 0.681 | 0.556 | 1 |
| 23249 | Flat_limpa | 1967 | 29 | 0.750 | 0.383 | 0.533 | 0.717 | 0.032 | 0.268 | 0.173 | 0.060 | 0.972 | 0.739 | 0.838 | 0.948 | 1 |
| 25998 | Long | 1966 | 36 | -0.602 | 0.333 | 0.544 | 0.439 | 0.905 | 0.298 | 0.193 | 0.237 | 0.105 | 0.712 | 0.816 | 0.767 | 0 |
| 26965 | CYCLE_Excellent | 1967 | 29 | 0.500 | 0.417 | 0.433 | 0.417 | 0.157 | 0.246 | 0.239 | 0.245 | 0.856 | 0.767 | 0.772 | 0.762 | 0 |
| 35296 | Long | 1966 | 36 | -0.731 | -0.696 | -0.626 | -0.357 | 0.975 | 0.933 | 0.901 | 0.694 | 0.029 | 0.078 | 0.105 | 0.316 | 0 |
| 3795 | Var | 1966 | 29 | -0.200 | -0.183 | -0.550 | -0.517 | 0.628 | 0.604 | 0.849 | 0.838 | 0.385 | 0.408 | 0.168 | 0.170 | 0 |
| 39587 | Var | 1966 | 36 | -0.228 | -0.287 | 0.298 | 0.579 | 0.653 | 0.648 | 0.341 | 0.146 | 0.357 | 0.359 | 0.672 | 0.858 | 0 |
| 4628 | CYCLE_Excellent | 1966 | 30 | 0.567 | 0.333 | 0.350 | 0.567 | 0.102 | 0.369 | 0.281 | 0.141 | 0.905 | 0.645 | 0.733 | 0.867 | 0 |
| 75332 | Var | 1966 | 36 | -0.427 | -0.099 | -0.462 | -0.170 | 0.745 | 0.561 | 0.773 | 0.588 | 0.263 | 0.451 | 0.237 | 0.420 | 0 |

### 3.2 variância

| HD | grupo | seg_year0 | L | tau_none | tau_s1 | tau_s3 | tau_s5 | p_upper_none | p_upper_s1 | p_upper_s3 | p_upper_s5 | p_D22_none | p_D22_s1 | p_D22_s3 | p_D22_s5 | concordantes_de_4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (Sun) | CYCLE_Excellent | 1966 | 51 | -0.526 | -0.834 | -0.625 | -0.612 | 0.744 | 0.990 | 0.764 | 0.738 | 0.258 | 0.012 | 0.239 | 0.267 | 0 |
| 101501 | Var | 1968 | 28 | -0.295 | -0.829 | -0.600 | -0.429 | 0.678 | 0.955 | 0.842 | 0.726 | 0.339 | 0.054 | 0.173 | 0.296 | 0 |
| 103095 | CYCLE_Excellent | 1968 | 34 | -0.569 | -0.059 | -0.542 | -0.595 | 0.762 | 0.534 | 0.688 | 0.807 | 0.250 | 0.470 | 0.321 | 0.202 | 0 |
| 10476 | CYCLE_Excellent | 1966 | 36 | -0.556 | -0.626 | -0.766 | -0.766 | 0.765 | 0.881 | 0.848 | 0.836 | 0.240 | 0.128 | 0.165 | 0.171 | 0 |
| 10700 | Flat_limpa | 1967 | 29 | -0.033 | 0.250 | -0.517 | -0.400 | 0.525 | 0.404 | 0.784 | 0.721 | 0.485 | 0.617 | 0.222 | 0.290 | 0 |
| 115383 | Var | 1966 | 36 | -0.158 | -0.170 | -0.673 | -0.684 | 0.566 | 0.574 | 0.871 | 0.881 | 0.447 | 0.431 | 0.134 | 0.124 | 0 |
| 131156A | Var | 1967 | 35 | 0.242 | 0.399 | 0.255 | 0.477 | 0.360 | 0.294 | 0.364 | 0.240 | 0.647 | 0.719 | 0.641 | 0.771 | 0 |
| 141004 | Long | 1966 | 30 | 0.583 | 0.300 | 0.117 | 0.500 | 0.185 | 0.345 | 0.454 | 0.220 | 0.822 | 0.662 | 0.556 | 0.794 | 0 |
| 152391 | CYCLE_Excellent | 1966 | 36 | -0.158 | 0.380 | 0.415 | -0.380 | 0.580 | 0.313 | 0.289 | 0.672 | 0.428 | 0.692 | 0.718 | 0.335 | 0 |
| 160346 | CYCLE_Excellent | 1966 | 36 | -0.649 | -0.193 | -0.240 | -0.228 | 0.845 | 0.590 | 0.554 | 0.588 | 0.164 | 0.417 | 0.450 | 0.416 | 0 |
| 166620 | CYCLE_Excellent | 1966 | 30 | 0.083 | -0.750 | -0.683 | -0.383 | 0.470 | 0.914 | 0.910 | 0.693 | 0.536 | 0.097 | 0.104 | 0.323 | 0 |
| 176095 | Long | 1966 | 36 | 0.404 | 0.427 | 0.462 | 0.450 | 0.277 | 0.314 | 0.274 | 0.296 | 0.731 | 0.690 | 0.735 | 0.715 | 0 |
| 182572 | Flat_limpa | 1967 | 35 | -0.804 | -0.320 | -0.935 | -0.882 | 0.937 | 0.825 | 0.999 | 0.981 | 0.071 | 0.184 | 0.002 | 0.025 | 0 |
| 190360 | Flat_limpa | 1967 | 28 | -0.676 | -0.600 | -0.752 | -0.752 | 0.901 | 0.939 | 0.971 | 0.961 | 0.107 | 0.065 | 0.033 | 0.046 | 0 |
| 201091 | CYCLE_Excellent | 1967 | 35 | -0.242 | -0.333 | -0.294 | -0.281 | 0.625 | 0.647 | 0.615 | 0.654 | 0.378 | 0.358 | 0.393 | 0.352 | 0 |
| 217014 | Var | 1966 | 30 | -0.017 | 0.050 | -0.117 | -0.200 | 0.628 | 0.634 | 0.748 | 0.697 | 0.381 | 0.373 | 0.259 | 0.314 | 0 |
| 23249 | Flat_limpa | 1967 | 29 | -0.400 | -0.900 | -0.667 | -0.467 | 0.706 | 0.996 | 0.894 | 0.778 | 0.307 | 0.009 | 0.116 | 0.235 | 0 |
| 25998 | Long | 1966 | 36 | -0.719 | 0.251 | 0.240 | 0.181 | 0.897 | 0.373 | 0.380 | 0.424 | 0.106 | 0.637 | 0.630 | 0.581 | 0 |
| 26965 | CYCLE_Excellent | 1967 | 29 | 0.583 | 0.133 | 0.733 | 0.800 | 0.259 | 0.431 | 0.121 | 0.102 | 0.753 | 0.579 | 0.887 | 0.910 | 0 |
| 35296 | Long | 1966 | 36 | -0.906 | 0.064 | -0.520 | -0.404 | 0.994 | 0.473 | 0.813 | 0.736 | 0.008 | 0.536 | 0.191 | 0.268 | 0 |
| 3795 | Var | 1966 | 29 | -0.383 | 0.150 | -0.367 | -0.550 | 0.691 | 0.407 | 0.644 | 0.819 | 0.321 | 0.600 | 0.371 | 0.190 | 0 |
| 39587 | Var | 1966 | 36 | -0.474 | -0.602 | -0.415 | -0.053 | 0.783 | 0.827 | 0.728 | 0.534 | 0.224 | 0.181 | 0.278 | 0.472 | 0 |
| 4628 | CYCLE_Excellent | 1966 | 30 | 0.550 | 0.217 | 0.433 | 0.483 | 0.307 | 0.428 | 0.321 | 0.327 | 0.698 | 0.579 | 0.688 | 0.684 | 0 |
| 75332 | Var | 1966 | 36 | -0.193 | 0.345 | 0.053 | 0.076 | 0.578 | 0.313 | 0.494 | 0.479 | 0.428 | 0.691 | 0.513 | 0.532 | 0 |

## 4. Varredura de janela 25–75 % (`star_results.csv`): configurações concordantes (de 20 = 4 tendências × 5 janelas)

| HD | seg_year0 | ac1_de_20 | var_de_20 |
|---|---|---|---|
| (Sun) | 1966 | 0 | 0 |
| 101501 | 1968 | 1 | 0 |
| 103095 | 1968 | 0 | 0 |
| 10476 | 1966 | 0 | 0 |
| 10700 | 1967 | 0 | 0 |
| 115383 | 1966 | 0 | 0 |
| 131156A | 1967 | 0 | 0 |
| 141004 | 1966 | 1 | 1 |
| 152391 | 1966 | 0 | 0 |
| 160346 | 1966 | 0 | 0 |
| 166620 | 1966 | 0 | 0 |
| 176095 | 1966 | 0 | 0 |
| 182572 | 1967 | 0 | 0 |
| 190360 | 1967 | 0 | 0 |
| 201091 | 1967 | 0 | 0 |
| 217014 | 1966 | 0 | 4 |
| 23249 | 1967 | 0 | 4 |
| 25998 | 1966 | 0 | 0 |
| 26965 | 1967 | 0 | 0 |
| 35296 | 1966 | 0 | 0 |
| 3795 | 1966 | 0 | 0 |
| 39587 | 1966 | 0 | 0 |
| 4628 | 1966 | 0 | 2 |
| 75332 | 1966 | 0 | 0 |

## 5. R′_HK contra S (`star_results.csv`)

Linhas comparadas: 960; |τ(R′_HK) − τ(S)| máximo = 0. Segmentos com banda de R_phot e fonte de B−V: ver seção 1 (`banda_Rphot`, `bv_fonte`).

## 6. Testes entre grupos (lógica da célula 20 do pipeline antigo; `star_metrics.csv`)

Uma linha por estrela (segmento MW mais longo; Sol excluído por ser exploratório). Mann–Whitney unilateral (greater).

| config | metric | g1 | g2 | U | p | med1 | med2 | sig | n1 | n2 |
|---|---|---|---|---|---|---|---|---|---|---|
| none | ac1 | Var | Flat_limpa | 14 | 0.5364 | 0.4267 | 0.5808 | n.s. | 7 | 4 |
| none | ac1 | Long | Flat_limpa | 10 | 0.3429 | 0.6989 | 0.5808 | n.s. | 4 | 4 |
| none | ac1 | CYCLE_Excellent | Flat_limpa | 16 | 0.5333 | 0.607 | 0.5808 | n.s. | 8 | 4 |
| none | ac1 | Var | CYCLE_Excellent | 15 | 0.9397 | 0.4267 | 0.607 | n.s. | 7 | 8 |
| none | ac1 | Long | CYCLE_Excellent | 17 | 0.4667 | 0.6989 | 0.607 | n.s. | 4 | 8 |
| none | var_norm | Var | Flat_limpa | 19 | 0.2061 | 0.002623 | 0.001416 | n.s. | 7 | 4 |
| none | var_norm | Long | Flat_limpa | 12 | 0.1714 | 0.004138 | 0.001416 | n.s. | 4 | 4 |
| none | var_norm | CYCLE_Excellent | Flat_limpa | 30 | 0.008081 | 0.008488 | 0.001416 | ** | 8 | 4 |
| none | var_norm | Var | CYCLE_Excellent | 4 | 0.9989 | 0.002623 | 0.008488 | n.s. | 7 | 8 |
| none | var_norm | Long | CYCLE_Excellent | 5 | 0.9758 | 0.004138 | 0.008488 | n.s. | 4 | 8 |
| s1 | ac1 | Var | Flat_limpa | 10 | 0.7939 | -0.3443 | -0.2908 | n.s. | 7 | 4 |
| s1 | ac1 | Long | Flat_limpa | 3 | 0.9429 | -0.3865 | -0.2908 | n.s. | 4 | 4 |
| s1 | ac1 | CYCLE_Excellent | Flat_limpa | 22 | 0.1838 | 0.04947 | -0.2908 | n.s. | 8 | 4 |
| s1 | ac1 | Var | CYCLE_Excellent | 12 | 0.973 | -0.3443 | 0.04947 | n.s. | 7 | 8 |
| s1 | ac1 | Long | CYCLE_Excellent | 6 | 0.9636 | -0.3865 | 0.04947 | n.s. | 4 | 8 |
| s1 | var_norm | Var | Flat_limpa | 22 | 0.08182 | 0.0002879 | 6.173e-05 | n.s. | 7 | 4 |
| s1 | var_norm | Long | Flat_limpa | 15 | 0.02857 | 0.0001781 | 6.173e-05 | * | 4 | 4 |
| s1 | var_norm | CYCLE_Excellent | Flat_limpa | 32 | 0.00202 | 0.0007377 | 6.173e-05 | ** | 8 | 4 |
| s1 | var_norm | Var | CYCLE_Excellent | 13 | 0.9639 | 0.0002879 | 0.0007377 | n.s. | 7 | 8 |
| s1 | var_norm | Long | CYCLE_Excellent | 3 | 0.9919 | 0.0001781 | 0.0007377 | n.s. | 4 | 8 |
| s3 | ac1 | Var | Flat_limpa | 6 | 0.9455 | 0.1133 | 0.3449 | n.s. | 7 | 4 |
| s3 | ac1 | Long | Flat_limpa | 2 | 0.9714 | 0.09914 | 0.3449 | n.s. | 4 | 4 |
| s3 | ac1 | CYCLE_Excellent | Flat_limpa | 23 | 0.1414 | 0.5208 | 0.3449 | n.s. | 8 | 4 |
| s3 | ac1 | Var | CYCLE_Excellent | 2 | 0.9997 | 0.1133 | 0.5208 | n.s. | 7 | 8 |
| s3 | ac1 | Long | CYCLE_Excellent | 0 | 1 | 0.09914 | 0.5208 | n.s. | 4 | 8 |
| s5 | ac1 | Var | Flat_limpa | 8 | 0.8848 | 0.2641 | 0.5097 | n.s. | 7 | 4 |
| s5 | ac1 | Long | Flat_limpa | 4 | 0.9 | 0.2177 | 0.5097 | n.s. | 4 | 4 |
| s5 | ac1 | CYCLE_Excellent | Flat_limpa | 18 | 0.404 | 0.5572 | 0.5097 | n.s. | 8 | 4 |
| s5 | ac1 | Var | CYCLE_Excellent | 0 | 1 | 0.2641 | 0.5572 | n.s. | 7 | 8 |
| s5 | ac1 | Long | CYCLE_Excellent | 0 | 1 | 0.2177 | 0.5572 | n.s. | 4 | 8 |


## 7. Par primário e Holm (D108; `group_primary.py` → `group_primary.csv`, `group_holm.csv`)

Par primário (fixado em D108): Var ∪ Long > Flat_limpa, AR(1) do segmento MW mais longo, σ = 1, Mann–Whitney unilateral (greater): n = 11 e 4, U = 13, **p = 0.887**; medianas −0.372 e −0.291 (sem correção, par único).

Holm por bloco métrica × configuração, 5 pares por bloco (D109; o par primário fica fora): 2 dos 30 testes com p_Holm < 0.05, ambos CYCLE_Excellent > Flat na variância normalizada (σ = 1: p = 0.0020, p_Holm = 0.0101; sem remoção: p = 0.0081, p_Holm = 0.0404); Long > Flat, variância normalizada, σ = 1: p = 0.0286, p_Holm = 0.114. Tabela completa em `results/group_holm.csv` (`p_holm` = D109; `p_holm_30` = família de 30 testes do primeiro cálculo, superada).
