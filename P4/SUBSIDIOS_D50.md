# Subsídios para decidir o item 6: a resposta teórica de D50

**Pedido do pesquisador (2026-11-24):** "Subsídios para decidir." Este arquivo **não escolhe** e não recomenda. Fontes: `audit/A7_theory.md` (Scheffer, Boulton), `audit/A7b_held_kleinen.md`, `audit/A8_usoskin.md`, `audit/A11_raridade.md` (CLS VI), com ids de `inspecao/checks.csv`. Páginas são as do PDF.

## 1. O que D50 afirma e de que depende
D50 (grau A para as citações) manda citar na íntegra duas frases da CLS VI: "The mechanisms that cause a star to enter and exit a magnetic minimum requires a stochastic process that is poorly understood" (§3.3.1; `3.11-22`) e "suggestive of a rapid (on stellar timescales) transition … these transitions can occur quickly, on order of years" (§3.3; `3.11-21`). A **resposta** é teórica: a bimodalidade de S-STD indicaria biestabilidade, e a biestabilidade forçada por ruído "ainda exibe CSD porque a barreira de potencial encolhe antes do salto". A resposta depende de três elos: (a) biestabilidade; (b) CSD antes do salto em biestáveis com ruído; (c) aplicabilidade a um sistema que **perde um ciclo limite**.

## 2. Elo a elo: o que as fontes lidas dizem

### (a) Biestabilidade da bimodalidade de S-STD
| Fato | Fonte | Efeito |
|---|---|---|
| A CLS VI descreve um vazio em S-STD que separa estrelas com e sem ciclo (faixa 0.9–1.0 M☉) e um acúmulo perto de S-STD ≈ 0.01 (1.0–1.1 M☉); sobre este último escreve: "perhaps a stochastic mechanism requires a bimodal distribution of S-STDs" | CLS VI §3.3 (A11 c.2) | a própria fonte liga bimodalidade a um mecanismo **estocástico** |
| A bimodalidade é **entre estrelas** (distribuição transversal). O *flickering* de Scheffer é a bimodalidade de **um mesmo sistema ao longo do tempo** | A7-F4; Scheffer p. 3 (`3.11-31` a `3.11-33`) | não é o mesmo observável; uma distribuição populacional pode vir de estrelas em estágios diferentes |
| Usoskin: a distribuição decenal do número de manchas do Sol tem um modo de grande mínimo separado do modo moderado; "grand minimum … trapped in this state" | Usoskin pp. 59, 61 (A8-F4) | paralelo solar de distribuição de estados, no tempo de um sistema, mas sem sinal precursor |

### (b) CSD antes do salto, em biestáveis com ruído
| Fato | Fonte | Efeito |
|---|---|---|
| Perto de uma bifurcação *fold* o autovalor dominante se anula; recuperação cada vez mais lenta; "can be proven … in any continuous model approaching a fold bifurcation" | Scheffer p. 1 (A7 item 1) | sustenta (b) para fold |
| O decaimento κ se anula e a variância do modo diverge (∝ 1/κ) em **qualquer bifurcação**, no limite de ruído pequeno e perto do equilíbrio | Held & Kleinen pp. 1–2 (`3.11-50`; A7b) | sustenta (b) em pontos fixos |
| **Falsos negativos:** transição sem aproximação gradual (evento extremo raro) ou por mudança externa rápida e permanente | Scheffer pp. 5–6 (A7-F3) | é a condição que "na ordem de anos" pode satisfazer |
| Boulton: se o forçamento é mais rápido que a escala intrínseca, os sinais "should not work as well" | Boulton p. 5 (A7 item 15) | idem |
| Held & Kleinen: três obstáculos em dados reais, entre eles "the system may not be as close to a bifurcation such that our unimodal approximation was justified" | HK p. 4 (`3.11-52`) | idem |
| O erro do decaimento estimado é δκ ≈ √(2κ/T); a série precisa de dezenas de tempos de decaimento | HK p. 3 (`3.11-53`; A7b-F2) | o tempo de decaimento estelar **não é conhecido** |

**Leitura própria (não está nas fontes):** "na ordem de anos" descreve a **duração da transição**, e o argumento da barreira que encolhe supõe que o **parâmetro de controle** derive lentamente antes dela. As fontes não dizem qual é a deriva do parâmetro em uma estrela, e nenhuma observação auditada mede isso (Q10).

### (c) Perda de um ciclo limite
| Fato | Fonte | Efeito |
|---|---|---|
| Hopf em Scheffer: "transition from a stable system to an oscillatory system", sinalizada por desaceleração crítica; o P4 é o sentido oposto (oscilatório → estável) | Scheffer p. 4 (`3.11-31`; A7-F2) | o sentido não coincide |
| "Critical transitions in cyclic and chaotic systems are less well studied"; para bifurcações não locais: "We know of no explicit work on early-warning signals for such transitions" | Scheffer pp. 3–4 (`3.11-32`, `3.11-33`) | admite a lacuna |
| Held & Kleinen: "oscillatory modes do not play a major role … could be easily included, however, by a 2D ansatz" | HK p. 2 (`3.11-51`; A7b-F1) | modos oscilatórios fora do escopo |
| Usoskin: precursores solares do mínimo de Maunder só qualitativos (ciclo de altura reduzida, alongamento do ciclo), de tipo diferente de CSD; "hardly able to predict" | Usoskin pp. 23, 58 (A8-F1, A8-F2) | o único precursor observacional citado não é CSD |
| **Nenhuma** das três fontes teóricas lidas dá sinal precursor para a perda de ciclo limite | A7-F2, A7b-F1 | (c) é extensão por analogia |

## 3. Resumo do balanço (fatos, sem juízo)
- **Sustentado por fonte:** (b) para fold e pontos fixos, com as ressalvas de ruído pequeno, proximidade ao equilíbrio e aproximação gradual.
- **Não sustentado por fonte lida:** (a) como biestabilidade temporal de uma estrela, e (c) para ciclo limite.
- **Não conhecido:** o tempo de decaimento e a deriva do parâmetro em estrelas (Q10).

## 4. Alternativas e o que cada uma exige no manuscrito
| Alternativa | O que o texto precisa dizer | Consequências |
|---|---|---|
| **Manter como extensão por analogia declarada** | citar as duas frases da CLS VI; apresentar a resposta (fold, biestabilidade) como **analogia**, dizendo que Scheffer e Held & Kleinen tratam pontos fixos e que não há fonte para ciclo limite | a objeção fica "respondida por analogia"; o revisor pode atacar (c) |
| **Reformular como hipótese testável** | a biestabilidade é hipótese do P4; declarar que a CSD na perda de ciclo limite não tem precedente nas fontes lidas e que o teste é a contribuição | liga D50 ao Q10 e ao desenho do teste; a limitação de D46 (8 pontos, grau C) entra como limite do teste |
| **Retirar a resposta, manter só a objeção citada** | citar as duas frases e admitir que não são respondidas com as fontes lidas | texto mais curto; enfraquece a motivação do P4 |
| **Buscar fonte sobre ciclo limite antes (A7c)** | nada até a leitura | adia; a lacuna pode persistir (A7-F2: "não encontrado nas fontes lidas") |

## 5. Pontos que valem para qualquer alternativa
- D46 já diz que o teste de janela deslizante não é executável em HD 166620, com ou sem as 119 linhas (D86); isso restringe qualquer afirmação de precursor temporal a esse caso.
- D58 e D86: nada que dependa das 119 linhas digitalizadas pode afirmar a aproximação com grau A.
- A recomendação "HD 101501 como discriminante de *aged out*" (D49) é independente de D50.

Estado: **subsídios entregues; escolha pendente (D87).**

## Adendo de 2026-11-24 (busca "ciclo limite", A7c, D88)
Três fontes novas foram lidas (`audit/A7c_limit_cycle_sources.md`). Para o elo (c): Kuehn 2011 diz que a Hopf supercrítica "is not critical" (p. 8; `3.11-63`) e que a análise estocástica da Hopf é "much more complicated" que a unidimensional (p. 32; `3.11-64`); Kuehn 2013 analisa a aproximação pelo lado estável, com variância crescendo como O(1/y) e covariância tendendo a zero com difusão igual (p. 32; `3.11-66`, `3.11-67`); Boettiger+2013 diz que na Hopf subcrítica os dois lados do limiar podem ser indistinguíveis sob ruído (p. 5; `3.11-68`) e que um indício positivo num sistema é negativo noutro (p. 1; `3.11-70`). **Nenhuma trata o sentido ciclo → equilíbrio**; (c) segue sem fonte direta. Efeito nas alternativas: a de "buscar fonte" está cumprida sem achado; Bury+2020 (não obtida) pode ainda ser subida.

