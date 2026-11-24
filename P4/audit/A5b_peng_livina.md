# Audit A5b — Livina & Lenton 2007 e Peng+1993 (completam os X de A5 §6)

| | |
|---|---|
| **Data** | 2026-11-24 |
| **Estado** | **fechada.** Resolve dois dos três graus X de `audit/A5_peng.md` §6 (reescalonamento do DFA; viés de comprimento finito); o terceiro (`H = (β+1)/2`) continua X |
| **Arquivos** | `bib/Livina_2007_GRL_34_L03712.pdf` (5 pp.; título, DOI `10.1029/2006GL028672` e volume 34 na p. 1) e `bib/Peng_1993_PRE_47_3730.pdf` (4 pp.; título "Finite-size effects on long-range correlations: Implications for analyzing DNA sequences", PRE 47, 3730–3733, maio de 1993; título, volume e páginas conferidos também no Crossref). Enviados pelo pesquisador em 2026-11-24 |
| **Método** | texto nativo (`pdftotext`; o de Peng tem OCR ruidoso e as equações não saem), busca literal em `inspecao/scripts/06_pdf_quotes.py` (`3.11-54` a `3.11-62`); página = página do PDF |
| **Observação** | O artigo de Peng+1993 trata do **método de caminhada de DNA** (rms F(ℓ) da caminhada), anterior ao DFA de Peng+1994 (`Peng et al. 1994, Phys. Rev. E 49, 1685.pdf`, A5). O resultado de comprimento finito vale para o mesmo tipo de estimador de expoente por log-log de F(ℓ); a extensão ao DFA é do próprio Peng 1994 (nota [16], A5 §1.5) |

## Valores extraídos

### Livina & Lenton 2007
| # | Afirmação | Local | Grau |
|---|---|---|---|
| 1 | O DFA entra como modificação do degenerate fingerprinting; "the conventional degenerate fingerprinting is not applicable due to the short length of the series" (série de gelo da Groenlândia) | p. 1, resumo (`3.11-54`) | A |
| 2 | Janela de ACF de **10 % do comprimento da série** ("bigger windows would provide poor final statistics… smaller windows would be insufficient") | p. 2, §2.1 [11] (`3.11-55`) | A |
| 3 | Para AR(1) com c → 1, o expoente DFA α → 1.5, "a random walk state of the system"; não estacionariedade "is a necessary but not sufficient condition for bifurcation" | p. 3, §2.3 [16] (`3.11-57`) | A |
| 4 | **Requisito de tamanho:** "The series should have at least several hundred points per window… the record should be at least of order a thousand points" | p. 3, §2.3 [18] (`3.11-56`) | **A** |
| 5 | **Calibração DFA → c** ("DFA-propagator ζ"): α = 0.91c³ − 0.37c² + 0.49c + 0.52 para 0 < c ≤ 0.936; α = −12.38c² + 25.14c − 11.28 para 0.936 < c ≤ 0.967; α = 0.72c + 0.75 para 0.967 < c < 1; ajustada em AR(1) de 20 000 pontos, 20 amostras por c; "the present calibration might be inappropriate" para dados não lineares | p. 3, §2.4 [19]–[20] | **A**/B: os sinais saíram do texto e foram conferidos por continuidade nas junções c = 0.936 (1.40 nos dois ramos) e c = 0.967 (1.45); em c = 1 dá 1.47 e não 1.50 |
| 6 | ACF e DFA têm acurácia comparável em 20 000 pontos; em 200 pontos o ACF-propagator desvia mais em c baixo e tem barras menores perto de c = 1 | p. 3, §2.5 [21] | A |
| 7 | Série da Groenlândia: 1586 pontos, **não equidistantes**; DFA em janelas de 500 pontos | p. 4, §3 (`3.11-58`) | A |

### Peng+1993
| # | Afirmação | Local | Grau |
|---|---|---|---|
| 8 | O expoente de correlação estimado em sequência de comprimento finito flutua "prominently" de amostra para amostra e dentro de uma mesma amostra; é preciso comparar com um controle sintético de mesmo comprimento | p. 1, resumo; p. 4, conclusão | A |
| 9 | O desvio-padrão do expoente local, Δα_local(ℓ, N), "decreases with the length of N" e **não depende da amplitude do ruído** | p. 2, §III | A |
| 10 | Argumento de escala: N/ℓ subsequências independentes; a flutuação "is inversely proportional to the square root of the number of independent samples" (`3.11-59`) | p. 2, §III | A |
| 11 | Eq. (7) confirmada numericamente: na Fig. 3, "the solid line has slope 1/2, the value predicted by Eq. (7)", para N = 1024, 8192 e 65 536 (`3.11-60`); o prefator não é derivado | p. 3, Fig. 3 | A (inclinação) / B (forma de Eq. 7, só pela legenda) |
| 12 | Exemplo: N = 25 759; a faixa de ajuste usa menos de 1/10 da sequência (menos de três décadas) (`3.11-62`) | pp. 2–3 | A |
| 13 | A caminhada (soma dupla da correlação) tem menos ruído que o espectro de potência ou a função de correlação; estes dão flutuações maiores (`3.11-61`) | p. 1, resumo; p. 4 | A |
| 14 | Procedimento para uma sequência única: dividir em M subsequências independentes e estimar a flutuação esperada por Eq. (7) | p. 3, §III | A |

## Verificações
- Títulos, autores, DOI/volume/páginas conferidos nas primeiras páginas; Peng também no Crossref → passa.
- Continuidade da calibração de Livina (item 5) → passa nas duas junções (conferência por cálculo, não por leitura de imagem).

## Achados

**A5b-F1 · o reescalonamento do indicador DFA tem fonte: Livina & Lenton 2007, §2.4. Fecha o X de A5 §6. `A`**
A fonte é a calibração por partes de α (item 5), ajustada em AR(1) de 20 000 pontos; o ponto crítico é α → 1.5 (c → 1), o que é a razão de Dakos reescalar para "1 = transição". A calibração é **empírica e do próprio artigo**, não uma relação analítica, e o artigo avisa que pode ser inadequada para dados com dinâmica desconhecida e fortemente não linear (item 5). D25 (reportar α cru) não é contrariada: o artigo trata a calibração como passo adicional opcional.

**A5b-F2 · o piso de comprimento do DFA em Livina é de ordem de mil pontos. `A`**
"at least of order a thousand points" e "several hundred points per window" (item 4). É maior que o piso de D24 (> 100 pontos, fonte A5/Peng 1994) e **muito** maior que N ≈ 27 estações anuais; a série bruta do subconjunto Baum tem mediana de 698 observações (`3.3-01`), abaixo do "ordem de mil" e irregularmente espaçada (item 7: o próprio Livina trata a série irregular com janelas de 500 pontos). Subsídio para Q9 e D76; não decide.

**A5b-F3 · o viés/flutuação de comprimento finito escala como (ℓ/N)^(1/2) e é independente da amplitude do ruído. `A`/B**
Itens 9–11. A incerteza do expoente cai com √N e cresce com √ℓ: com N ≈ 27 e ℓ de uma fração apreciável de N, a incerteza do expoente é da ordem do próprio efeito. É um argumento de escala do artigo e a legenda da Fig. 3, não um cálculo para a DFA do P4. Procedimento de controle sintético de mesmo comprimento (item 14) é o que a fonte pede antes de interpretar um expoente.

**A5b-F4 · Peng+1993 não trata de DFA nem de séries irregulares. `A`**
O estimador é o rms F(ℓ) da caminhada de DNA; o DFA é de Peng 1994. A afirmação de A5 "Peng note [16] delega o viés de comprimento finito a Peng et al. 1993" está confirmada em seu conteúdo, mas a quantificação é para sequências de 10³ a 10⁵ pontos, não para N ≈ 26.

## Decisões tomadas, com base
1. **Os X de A5 §6 sobre o reescalonamento e o viés de comprimento finito ficam resolvidos por estas fontes**; o X de `H = (β+1)/2` permanece. *(→ D81)*
2. **Q9 e D24 não são decididos aqui.** Os subsídios novos (A5b-F2, A5b-F3) vão para `SUBSIDIOS_PAPEIS_SERIES.md` por nova entrada no caderno, sem editar o arquivo anterior.

## Não resolvido (grau C ou X)
| Quantidade | Por que | Resolução proposta |
|---|---|---|
| `H = (β+1)/2` | **X** — Schroeder 1991 (livro) não obtido | descartar a afirmação (D28) |
| Eq. (7) de Peng 1993 | forma lida só pela legenda | ler a imagem de página se a fórmula for citada |
| Aplicabilidade da calibração de Livina a séries cromosféricas irregulares | **C** — o artigo só testa AR(1) e dois conjuntos | teste próprio só se Q9 for reaberta |
