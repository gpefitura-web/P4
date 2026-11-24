# P4_SOURCE_VALUES.md — RASCUNHO PARA ASSINATURA (2026-11-24)

**Estado:** rascunho preparado por Claude a pedido do pesquisador ("Sim, preparar a consolidação"); **não assinado**; o pipeline permanece congelado. Regra de rastreabilidade (caderno §7): todo número do manuscrito → esta tabela → `D##` → seção de um artigo-fonte. Só entram valores de grau **A** ou **B**; o que é **C** ou **X** está no Apêndice e **não chega ao manuscrito**. Página = página do PDF; "Check" = id em `inspecao/checks.csv` (reprodução numérica) ou citação literal (`3.11-xx`).

## 1. Catálogo e amostra
| ID | Quantidade | Valor | Fonte e local | Check | D## | Grau |
|---|---|---|---|---|---|---|
| V01 | Linhas do catálogo congelado | 112 | Baliunas+1995, Tabela 2 (`baliunas_table2_full.csv`) | 3.1-01 | D01, D36 | A |
| V02 | Classes `CYCLE` / `Var` / `Long` / `Flat` / `Flat?` | 52 / 29 / 16 / 11 / 4 | idem | 3.1-02 a 3.1-07 | D09 | A |
| V03 | Cinco `Flat` limpas | HD 10700, 23249, 43587, 182572, 190360 | D13 mais Apêndice B de B95 (12 binárias) | 3.20-03 | D13, D102 R1 | A |
| V04 | Estrelas-padrão excluídas | 17 | Baliunas+1995, Tabela 1 (A6 §3) | 3.20-08 | D13, D14 | A |
| V05 | Estrelas do catálogo com série (Baum, v2001 ou Egeland) incluídas | ver `p4_star_catalog.csv` (`status_amostra = incluida`) | D95 opção (v) | 3.20-06, 3.20-07 | D95, D102 | A |
| V06 | Extensão Baum: estrelas e observações | 59 estrelas; 62 135 observações | Baum+2022, Tabela 1 (VizieR J/AJ/163/183) | 3.2-01, 3.2-02 | D41 | A |
| V07 | Mediana de observações por estrela (Baum) | 698 | idem | 3.3-01 | D41 | A |
| V08 | Camada v2001: estrelas | 35 (sem HD 166620) | HK Project v2001 NSO, README p. 1 | 3.15-01, 3.15-02 | D85 | A |
| V09 | Linhas HKP de Baum reproduzidas no v2001 (6 estrelas comuns) | 14 233 de 14 295 | data/HK_Project_v2001_NSO | 3.15-04 | D85 | A |
| V10 | CLS V: estrelas; linhas da Tabela 3 | 710; 52 372 | Isaacson+2024, Tabelas 2 e 3 (VizieR) | 3.6-01, 3.6-06 | D41, D55 | A |
| V11 | CLS V: estrelas com Nobs ≥ 45 | 290 (tabela; o texto diz 285, I-42) | idem | 3.6-07 | D41, D67 | B |
| V12 | CLS V: ciclos detectados (Tabela 4) | 138 | idem | 3.6-03 | D41 | A |
| V13 | CLS VI: estrelas analisadas | 91, em quatro faixas de massa | Isaacson+2025, resumo, p. 1 | 3.11-19, 3.11-20 | D60 | A |

## 2. Constantes solares (Egeland+2017)
| ID | Quantidade | Valor | Fonte e local | Check | D## | Grau |
|---|---|---|---|---|---|---|
| V14 | ⟨S⟩ solar | 0.1694 ± 0.0005 | Egeland+2017, resumo e p. 11 | 3.11-39 | D16 | A |
| V15 | Médias de ciclo (mínimo, máximo) | 0.1621; 0.177 | idem | 3.11-39 | D19 | A |
| V16 | Amplitude ciclo 22; ciclo 24 | 0.0178; 0.0089 | Egeland, Tabela 2 | 3.11-39 | D19 | A |
| V17 | ⟨ΔS_cyc⟩ | 0.0145 ± 0.0012 (resumo e Tabela 2; o texto do §6 traz ± 0.0014) | Egeland, p. 1 e p. 11 | 3.11-40 | D19, D67 | B |
| V18 | Série solar calibrada (Tabela 4) | 6 349 linhas, 1966.669–2016.153, ciclos 20–24 | Egeland, Tabela 4 e §4.6 p. 9 | 3.12-01, 3.12-03, 3.12-07 | D65 | A |

## 3. HD 166620 (Luhn+2022 e Baum+2022)
| ID | Quantidade | Valor | Fonte e local | Check | D## | Grau |
|---|---|---|---|---|---|---|
| V19 | N por estado (mínimo 1; mínimo 2; grande mínimo) | 44; 315; 103 | Luhn, Tabela 2 (VizieR) | 3.4-21, 3.4-28, 3.4-35 | D45 | A |
| V20 | ⟨S_HK⟩ por estado | 0.1810; 0.1724; 0.1705 | idem | 3.4-22, 3.4-29, 3.4-36 | D45 | A |
| V21 | σ bruto do intervalo | 0.0035; 0.0058; 0.0020 | idem | 3.4-23, 3.4-30, 3.4-37 | D45, D102 R4 | A |
| V22 | σ_S corrigido (conta A: σ do intervalo menos ruído em quadratura) | 0.0027; 0.0054; 0.0019 | Luhn §3.1, p. 4 (receita); reproduzido | 3.4-25, 3.4-32, 3.4-39; 3.11-01 | D45, D57, D102 R4 | A |
| V23 | Ruído instrumental subtraído | 1.2 % (Mount Wilson); 0.3 % (Keck) de ⟨S_HK⟩ | Luhn §3.1, p. 4 | 3.11-01 | D45 | A |
| V24 | σ_S pela conta B (sensibilidade) | 0.0028; 0.0048; 0.0015 | reprodução desta inspeção | 3.4-27, 3.4-34, 3.4-41 | D57 | B |
| V25 | F-test mínimo 1 contra grande mínimo | p = 8.78 × 10⁻⁶ publicado, que reproduz com variâncias brutas (8.80 × 10⁻⁶); com σ corrigidos 8.7 × 10⁻³ | Luhn §3.1, p. 4 | 3.4-50, 3.4-52 | D57 | A |
| V26 | Janela do mínimo 2 | 1987.0–1991.0 | Luhn §3.1 (o texto também cita 1986–1990) | 3.4-28 a 3.4-30 | D57 | B |
| V27 | Lacuna de Baum antes de 2004 | 6.91 anos (1997.73–2004.64) | Baum+2022, Tabela 1 | A13-F3 | D46 | A |
| V28 | HD 101501: cobertura | 2 239 observações; 49 anos; lacuna 13.82 anos; 99.73 % Mount Wilson | Baum+2022 Tabela 1; Baum §4.1, p. 7 | 3.3-40, 3.3-50, 3.3-52, 3.11-10 | D49, D59 | A |

## 4. Piso, limiar e precisão
| ID | Quantidade | Valor | Fonte e local | Check | D## | Grau |
|---|---|---|---|---|---|---|
| V29 | Menor SSD/Smed com Nobs ≥ 45 (CLS V, tabela) | HD 187923 0.372 %; HD 144579 0.397 %; HD 55575 0.448 % | Isaacson+2024, Tabela 2 | 3.6-24 a 3.6-26 | D67, D75 | A |
| V30 | Piso instrumental citado | faixa 0.37–0.45 % (tabela e texto do artigo) | idem | idem | D75 | A |
| V31 | σ_S/S médio das 17 padrões; sem os 4 com marcador | 1.4 %; 1.2 % | Baliunas+1995, Tabela 1 | A6 §3 (checksum) | D14 | A |
| V32 | Limiar `Flat` de B95 | σ_S/S < 1–1.5 % | Baliunas+1995 | A6-F6 | D102 R12 | A |
| V33 | σ_S/S das quatro `Flat` na CLS V | 0.72; 0.86; 0.95; 1.49 % | Isaacson+2024, Tabela 2 | A11 §b.3 | D102 R12 | A |
| V34 | Degrau HKP-2 → HIRES-2: σ entre estrelas; > 1.2 %; > 5 % | 4.47 %; 25 de 51; 10 de 51 | Baum Tabela 1 (derivado) | 3.5-02, 3.5-06, 3.5-07 | D44, D102 R5 | B |

## 5. R′_HK e validade (Noyes+1984)
| ID | Quantidade | Valor | Fonte e local | Check | D## | Grau |
|---|---|---|---|---|---|---|
| V35 | Receita S → R′_HK | R_HK = 1.340 × 10⁻⁴·C_cf(B−V)·S; log C_cf = 1.13(B−V)³ − 3.91(B−V)² + 2.84(B−V) − 0.47; log C′_cf = log C_cf + Δlog C (Δlog C = 0 se B−V > 0.63; = 0.135x − 0.814x² + 6.03x³, x = 0.63 − (B−V), caso contrário); log R_phot = −4.898 + 1.918(B−V)² − 2.893(B−V)³; R′_HK = R_HK − R_phot | Noyes+1984, pp. 13–14 (A12 §2, três passes) | 3.7-12 a 3.7-14 | D52 | A |
| V36 | Faixa de validade de R_phot | 0.44 < B−V < 0.82; extrapolação 0.82–1.0; > 1.0 até 20 % de incerteza | Noyes+1984, pp. 2 e 13 | 3.11-29, 3.11-30 | D53 | A |
| V37 | Escopo da calibração | "mean level of activity" (nível médio, não flutuação) | Noyes+1984, p. 2 | 3.11-27 | D61 | A |
| V38 | Estrelas na faixa aberta 0.44–0.82 do catálogo | 78 (82 pela faixa fechada) | `noyes1984_validade_cor.csv` | 3.7-10 | D53, D62 | A |

## 6. Parâmetros de método (com citação de seção)
| ID | Parâmetro | Valor | Fonte e local | Check | D## | Grau |
|---|---|---|---|---|---|---|
| V39 | Janela deslizante | 50 % do segmento, varredura 25–75 % | Dakos+2012, p. 17 | 3.11-41 | D20 | A |
| V40 | Significância | 1 000 surrogates ARMA(p,q) por AIC, sobre os resíduos | Dakos+2012, p. 17 | 3.11-41 | D22 | A |
| V41 | Anos faltantes | interpolação linear só de lacunas de 1–2 anos, pontos marcados; lacunas ≥ 3 anos dividem a série; surrogates com a mesma regra | decisão do pesquisador; Liu+; Rehfeld+2011 pp. 1–2 | 3.17-02, 3.17-03, 3.11-77 a 3.11-80 | D98 | A |
| V42 | Segmento mínimo para o indicador | 24 anos (janela ≥ 12 pontos, ≥ 13 janelas); 24–39 anos "precisão baixa"; ≥ 40 "adequada" | simulação; Held & Kleinen p. 3 | 3.18-01 a 3.18-06, 3.11-53 | D99, D100 | A |
| V43 | Erro do AR(1) numa janela de w pontos | SD ≈ √((1−c²)/w) (0.25 em w = 12; 0.18 em w = 24, c = 0.5) | Held & Kleinen p. 3; simulação | 3.11-53, 3.18-06 | D100 | A |
| V44 | Remoção de tendência | σ ∈ {1, 3, 5} anos mais "sem remoção"; σ = 1 padrão; destaque só com concordância em ≥ 3 de 4 | simulação; Dakos A4-F2 | 3.19-03 a 3.19-05 | D21, D102 R9 | A |
| V45 | Convenção de α do DFA (se usado; DFA fora) | α cru de Peng; piso > 100 pontos; Livina: ordem de 1 000 pontos | Peng+1994; Livina & Lenton p. 3 | 3.11-56 | D24, D25, D102 R14 | A |
| V46 | Calibração DFA → c | α = 0.91c³ − 0.37c² + 0.49c + 0.52 (c ≤ 0.936); −12.38c² + 25.14c − 11.28 (0.936 < c ≤ 0.967); 0.72c + 0.75 (c > 0.967) | Livina & Lenton p. 3 | conferido por continuidade nas junções | A5b | B |
| V47 | Incerteza de expoente em sequência finita | cai com √N, independente da amplitude do ruído | Peng+1993, pp. 2–3 | 3.11-59, 3.11-60 | A5b | A |
| V48 | Inclinação de τ Ceti | 7° ± 7° (v sin i = 0.1 ± 0.1 km/s) | Korolik+2023, resumo p. 1 e Tabela 3 | A14 | D51, D102 R16 | A |

## 7. Condição de assinatura (protocolo §7)
- **Nenhum valor das seções 1–6 está em grau C ou X** (verificado por `inspecao/scripts/18_build_consolidation.py`, checagem `3.20-09`).
- **Todo parâmetro de método carrega citação de seção ou página** (seção 6).
- **O que foi deixado de fora por ser C ou X** está no Apêndice.

---

## Apêndice — NÃO chega ao manuscrito (grau C ou X)
| Item | Grau | Por que | Onde |
|---|---|---|---|
| As 119 linhas `new_MW` de HD 166620 (1995–2002), as oito médias anuais e a lacuna de 2.82 anos | C | digitalizadas de figura (Luhn arquivo); dados reais não obtidos (D86) | D58, D86 |
| Incerteza residual dos offsets de Baum e a identidade das 14 estrelas deslocadas | X | não publicada | D44 |
| Os períodos tentativos de B95 (6 estrelas `CYCLE`) como valor de ciclo | B (leitura única da imagem) | registrados só como campo `P_cyc_tentativo`, nunca como `P_cyc` | D64 |
| Períodos de HD 3651 (B95 13.8, Saar 14.6, Oláh 11.6, CLS V 10.01) | X (fontes discordam) | lado a lado, sem fusão | D15, D42 |
| Inclinação das `Flat` além de HD 10700 | X | nenhuma fonte auditada | D51, D102 R16 |
| Tempo de decaimento e deriva do parâmetro em estrelas | X | nenhuma fonte | D102 R15 |
| Sinal precursor para a perda de um ciclo limite | X | nenhuma fonte lida | D90, D88, D89 |
| ⟨ΔS_cyc⟩ ± 0.0014 (texto) contra ± 0.0012 (tabela) | A/B com divergência interna | V17 usa 0.0012 e registra | D67 |
