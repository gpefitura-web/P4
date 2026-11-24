# Audit A7b — Held & Kleinen 2004, GRL 31, L23207 (complemento de A7)

| | |
|---|---|
| **Data** | 2026-11-24 |
| **Estado** | **fechada.** Completa o item 16 e o A7-F1 de `audit/A7_theory.md` (que não é editado) |
| **Arquivo** | `bib/Held_2004_GRL_31_L23207.pdf` (4 páginas; título "Detection of climate system bifurcations by degenerate fingerprinting", autores H. Held e T. Kleinen e DOI `10.1029/2004GL020972` conferidos na página 1; enviado pelo pesquisador em 2026-11-24; `bib/MANIFEST.json`) |
| **Método** | texto nativo (`pdftotext`), busca literal em `inspecao/scripts/06_pdf_quotes.py` (`3.11-50` a `3.11-53`); página = página do PDF (1 a 4) |
| **Páginas lidas** | 1 a 4 inteiras; as equações (1) e (2) saem quebradas no texto e foram lidas só pelo que as frases ao redor afirmam |

## Valores e afirmações extraídos

| # | Afirmação | Local | Grau |
|---|---|---|---|
| 1 | "the smallest system-immanent decay rate κ for perturbations of the equilibrium vanishes and the variability of the related mode diverges" em qualquer bifurcação ("most fundamental, model-independent property of any bifurcation") | p. 1, §1 [3] (`3.11-50`) | **A** |
| 2 | A variância do modo crítico diverge como 1/κ no limite de ruído pequeno | p. 1–2, §3 [5] | **A** |
| 3 | O indicador é o decaimento: modelo AR(1) unidimensional y_{n+1} = c·y_n + σ·η_n, c = exp(κΔt); c obtido da autocorrelação de lag 1, depois de subtrair uma tendência linear; Δt-agregação para eliminar ruído de tempo | p. 2, §3 [6] | **A** |
| 4 | **"Hereby we assume that oscillatory modes do not play a major role in CLIMBER2. They could be easily included, however, by a 2D ansatz."** Não há tratamento de modos oscilatórios nem de perda de ciclo limite | p. 2, §3 [6] (`3.11-51`) | **A** |
| 5 | Erro da taxa de decaimento estimada δκ ≈ √(2κ/T), T = comprimento da série; o comprimento mínimo T_min sai da inversão (eq. 1); para a série de 10 000 anos do modelo o ganho de informação é de fator 2 a 6 | p. 3, §4 [11], §5 [13] (`3.11-53`) | A (a fórmula pela frase) / B (eq. 1 lida só pelo texto) |
| 6 | Resultado do modelo CLIMBER2: c aproxima-se de 1 ao se aproximar do limiar; com forçamento transiente "although noisy, allows to conclude where that threshold is roughly to be expected"; segmentos quase descorrelacionados de 1/κ(c ≈ 0.9) ≈ 500 anos | p. 3, §5 [12] | A |
| 7 | **Três obstáculos em dados reais:** (i) "the system may not be as close to a bifurcation such that our unimodal approximation was justified"; (ii) dados de paleo reconstroem só parte do campo; (iii) ruído observacional | p. 4, §6 [19] (`3.11-52`) | **A** |
| 8 | Aproximação válida "in the small-noise limit" e perto do equilíbrio: tratamento linearizado | p. 1, §3 [5] | A |

## Verificações
- Título, autores, DOI e volume na página 1 → passa. Crossref: título, volume 31 e L23207 conferidos nas duas fontes anteriores (A7).
- O arquivo do repositório com este nome (A7-F1) continua sendo Boulton+2014; o novo arquivo tem nome distinto em `bib/`.

## Achados

**A7b-F1 · Held & Kleinen fundamenta o indicador de decaimento para bifurcações de ponto fixo, não para a perda de um ciclo limite. `A`**
O argumento é sobre o autovalor dominante que se anula e a variância que diverge (itens 1–3). Os modos oscilatórios ficam fora de propósito ("do not play a major role… could be easily included by a 2D ansatz", item 4), sem tratamento. Isto confirma, com a fonte primária que A7 não tinha, a ressalva de A7-F2: **nenhuma das três fontes teóricas lidas (Scheffer, Boulton, Held & Kleinen) apresenta sinal precursor para a perda de um ciclo limite**; a aplicação ao P4 é por analogia.

**A7b-F2 · a quantidade de dados pedida é medida em tempos de decaimento. `A`** (fórmula) / `C` (aplicação ao P4)
δκ ≈ √(2κ/T) (item 5) dá T ≈ 2κ/δκ², isto é, T/(1/κ) ≈ 2(κ/δκ)². Para um erro relativo δκ/κ = 0.3 a série precisa ter cerca de 22 tempos de decaimento (aritmética da fórmula impressa, grau C quanto ao uso). O tempo de decaimento de uma estrela perto de um mínimo de Maunder **não é conhecido** em nenhuma fonte auditada, portanto não se sabe se 27 estações anuais ou 8 pontos de aproximação (D46) correspondem a 1 ou a 20 tempos de decaimento. Relaciona-se com Q10 (a escala da transição) e com D50 (A7-F3).

**A7b-F3 · as ressalvas do artigo coincidem com as de Scheffer e Boulton. `A`**
Proximidade ao equilíbrio e ruído pequeno (itens 7–8) são as condições de falso negativo de A7-F3; o artigo as lista como obstáculos, não como resolvidas.

## Decisões tomadas, com base
1. **A7 fecha por inteiro**; Held & Kleinen entra por A7b. *Base:* acima. *(→ D81 no caderno)*
2. **D50 e o item 6 do memorando voltam a ser decidíveis pelo pesquisador** com este subsídio; **nenhuma decisão de mérito tomada aqui.** D74 (esperar Held & Kleinen) está cumprida na condição; a escolha continua do pesquisador.

## Não resolvido (grau C ou X)
| Quantidade | Por que | Resolução proposta |
|---|---|---|
| Sinal precursor para perda de ciclo limite | **X** — ausente nas três fontes teóricas | declarar como analogia; buscar fonte (por exemplo, bifurcação de Hopf supercrítica com ruído) só se a Discussão a exigir |
| Equações (1) e (2) | lidas só pelo texto | ler a imagem de página se forem citadas |
| Tempo de decaimento de estrelas perto de um mínimo | **X** — nenhuma fonte auditada | Q10 |
