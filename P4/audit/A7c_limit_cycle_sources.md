# Audit A7c — fontes sobre sinais precursores perto de bifurcações de Hopf e perda de ciclo limite

| | |
|---|---|
| **Data** | 2026-11-24 |
| **Estado** | **fechada com leitura parcial declarada.** Resposta à pergunta do pesquisador "buscar fonte sobre ciclo limite antes" (item 6, D87). Complementa A7 e A7b |
| **Busca** | OpenAlex (4 consultas sobre sinais precursores, Hopf, ciclo limite, estrutura matemática de transições críticas), 2026-11-24; escolhidas quatro fontes por relevância e acesso aberto; baixadas por `inspecao/scripts/12_fetch_hopf_refs.py` (validação de título nas páginas 1–2, REG-R2); registro em `bib/MANIFEST.json` e `bib/DOWNLOAD_LOG.md` |
| **Fontes lidas** | Kuehn 2011, *Physica D* 240, 1020 (manuscrito arXiv:1101.2899, 38 pp.); Kuehn 2013, *J. Nonlinear Sci.* 23, 457 (manuscrito arXiv:1101.2908, 67 pp.); Boettiger, Ross & Hastings 2013, *Theor. Ecol.* 6, 255 (manuscrito arXiv:1305.6700, 12 pp.) |
| **Não obtida** | Bury et al. 2020, *J. R. Soc. Interface* 17, 20200482 ("Detecting and distinguishing tipping points using spectral early warning signals", DOI `10.1098/rsif.2020.0482`): o PMC devolve página HTML e não PDF em duas tentativas; **o pesquisador pode subir o PDF** |
| **Páginas lidas** | só as passagens sobre Hopf, ciclo limite e oscilação (busca por termo e leitura do entorno): Kuehn 2011 pp. 8, 12 (atraso de Hopf) e 32; Kuehn 2013 §3 (formas normais, p. 11), Teorema 5.2 e discussão (p. 32); Boettiger pp. 1, 5. **Não lido por inteiro:** o restante de Kuehn 2011 e 2013 (demonstrações, aplicações) e Boettiger |
| **Método** | texto nativo (`pdftotext`); citações literais em `06_pdf_quotes.py` (`3.11-63` a `3.11-70`) |

## Valores e afirmações extraídos

| # | Afirmação | Local | Grau |
|---|---|---|---|
| 1 | Hopf como "critical transition" **só se subcrítica** (l₁ > 0); "If it is supercritical (l₁ < 0) then the transition is not critical" | Kuehn 2011, Prop. 2.6, p. 8 (`3.11-63`) | **A** |
| 2 | Na forma normal usada, o equilíbrio é estável para y < 0 e perde a estabilidade em y = 0 (par de autovalores complexos cruza o eixo imaginário); a variedade lenta é atraente do lado y < 0: a aproximação analisada é **pelo lado estável** | Kuehn 2011, p. 8 (`3.11-65`); Kuehn 2013, §3, p. 11 (eq. 12–13) | **A** |
| 3 | Variância das coordenadas cresce como O(1/y) ao se aproximar do Hopf (ruído aditivo fixo); com difusão igual nas duas coordenadas, a **covariância tende a zero** | Kuehn 2013, comentário ao Teorema 5.2, p. 32 (`3.11-66`, `3.11-67`) | **A** |
| 4 | "The analysis of stochastic Hopf bifurcation is much more complicated than one-dimensional stochastic bifurcations … noise correlated between the two fast variables" | Kuehn 2011, p. 32 (`3.11-64`) | A |
| 5 | Hopf subcrítica: transição de equilíbrio estável a ciclo estável; a autovalor dominante → 0 e há CSD; **mas a transição é gradual** (os ciclos crescem a partir de zero), e do lado do limiar "the system behavior observed on either side may be indistinguishable" | Boettiger+2013, p. 5 (`3.11-68`) | **A** |
| 6 | "not all systems that show regime shifts exhibit critical slowing down, or vice versa"; "a positive indication for some systems is a negative indication in others" | Boettiger+2013, p. 1, resumo (`3.11-69`, `3.11-70`) | A |
| 7 | Atraso de bifurcação (*delayed Hopf*): perto de Hopf e de pitchfork o sistema permanece perto do equilíbrio instável por tempo finito após o cruzamento | Kuehn 2011, p. 12 (linhas "For Hopf, pitchfork and transcritical bifurcations we also observe bifurcation delay") | A (existência); resultado quantitativo não lido |

## Verificações
- Títulos e DOI conferidos nas páginas 1–2 de cada PDF (`bib/MANIFEST.json`); DOI de Kuehn 2011 `10.1016/j.physd.2011.02.012` e de Kuehn 2013 `10.1007/s00332-012-9158-x` batem com o OpenAlex; **o primeiro nome do arquivo de Boettiger tinha "Dakos" por engano e foi corrigido** (autores: Boettiger, Ross & Hastings).
- Os três PDFs são manuscritos do arXiv, não as versões publicadas; os números de página acima são do arquivo.

## Achados

**A7c-F1 · a literatura de CSD em Hopf trata a aproximação pelo lado estável. `A`**
Nas duas fontes matemáticas (Kuehn), o equilíbrio é estável antes do limiar e a quantidade analisada (variância, covariância, autovalor) é a do **ponto fixo que perde a estabilidade** (itens 1–3). Boettiger descreve o mesmo sentido: equilíbrio → ciclo (item 5). **Nenhuma das três fontes analisa o sentido ciclo → equilíbrio.** Reforça A7-F2 e A7b-F1 com uma terceira linha de fontes.

**A7c-F2 · a Hopf supercrítica não é "transição crítica" para esta literatura. `A`**
Kuehn 2011 Prop. 2.6 (item 1). Se a perda do ciclo estelar for uma Hopf supercrítica (hipótese; nada nas fontes a estabelece), a literatura a trata como **não crítica**, sem salto, e o sinal de aproximação pelo lado oscilatório não é analisado. O P4 chama o fenômeno de "transição" e usa CSD: esta fonte diz que, nesse tipo de bifurcação, os dois lados do limiar podem ser indistinguíveis sob ruído (item 5).

**A7c-F3 · há um alerta explícito de que o sinal pode não existir ou inverter. `A`**
Boettiger itens 6: nem toda transição tem CSD e "um indício positivo para uns é negativo para outros". O mesmo vale para a covariância de Kuehn, que **diminui** ao se aproximar do Hopf (item 3), contra a variância que aumenta. O indicador escolhido muda o sinal esperado.

**A7c-F4 · ainda não há fonte direta para a perda de um ciclo limite estelar. `X`**
O que foi encontrado é teoria de pontos fixos que se tornam instáveis. Nenhuma fonte lida descreve o comportamento da variância, da autocorrelação ou da amplitude **do lado do ciclo** ao se aproximar do ponto em que ele desaparece. Pode existir em fontes não lidas (Bury+2020, o restante de Kuehn, a literatura de termoacústica e de neurociência que o OpenAlex listou); **não foram lidas** e nada se afirma sobre elas.

## Decisões tomadas, com base
1. **A pergunta "buscar fonte sobre ciclo limite" tem resposta provisória: não foi achada fonte direta.** *Base:* A7c-F1 e F4. *(→ D88 no caderno)*
2. **D50 e o item 6 não são decididos aqui.**

## Não resolvido (grau C ou X)
| Quantidade | Por que | Resolução proposta |
|---|---|---|
| Sinal precursor do lado do ciclo | **X** — nenhuma fonte lida | o pesquisador sobe Bury+2020 (DOI acima); ou aceita declarar como lacuna |
| Resto de Kuehn 2011/2013 e Boettiger | não lidos por inteiro | ler as seções de Hopf com demonstração se forem citadas |
| Versões publicadas | só manuscritos | citar a versão publicada na bibliografia |

---

## Adendo de 2026-11-24: Bury et al. 2020 (enviado pelo pesquisador)

| | |
|---|---|
| **Arquivo** | `bib/Bury_2020_JRSocInterface_17_20200482.pdf` (10 pp.; versão publicada; título, autores T. M. Bury, C. T. Bauch e M. Anand, e DOI `10.1098/rsif.2020.0482` conferidos na p. 1; sha256 em `bib/MANIFEST.json`) |
| **Páginas lidas** | resumo, introdução, §2.4 (aplicação empírica), Figura 5 (renderizada e vista) e discussão (pp. 1, 2, 4, 5, 7, 8); **não lidas por inteiro:** a derivação analítica (§2.1–2.3) |
| **Citações** | `3.11-71` a `3.11-74` |

| # | Afirmação | Local | Grau |
|---|---|---|---|
| 8 | "conventional EWS … may fail to distinguish the onset of oscillations (e.g. Hopf bifurcation) from a transition to a distant attractor (e.g. Fold bifurcation)"; os EWS espectrais baseados em "spectral reddening" não funcionam antes de transições com componente oscilatória | p. 1, resumo (`3.11-71`) | **A** |
| 9 | Transcrítica, Hopf e fold "are all accompanied by critical slowing down and so cannot be distinguished by the conventional critical slowing down methodology" | p. 2 (`3.11-72`) | A |
| 10 | Aplicação a um quimióstato presa–predador com **dois** pontos de Hopf (H1, H2) ao variar a taxa de diluição; "Preceding both Hopf bifurcations … Smax shows an upward trend, and w_Hopf is the significant AIC weight"; "Unlike for H2, variance and Smax do fluctuate prior to H1" | p. 5, §2.4 (`3.11-73`) | **A** |
| 11 | O espectro permite estimar o período das oscilações antes da bifurcação (≈ 19 dias, H1) | p. 5 | A |
| 12 | Limitação declarada: os EWS espectrais só separam oscilatório de não oscilatório; Hopf supercrítica e subcrítica "give rise to the same spectral EWS" mas a supercrítica "yields a smooth, reversible transition to small oscillations" (`3.11-74`); distinguir exige termos não lineares, "which this study has assumed to be negligible" | p. 8 | A |
| 13 | Os dados empíricos exigem ambiente controlado, parâmetro fixo por série e perturbações grandes; o autor pede teste em dados naturais de alta resolução com condições variáveis | p. 7 | A |

**Leitura da Figura 5 (qualitativa, grau C, não analisada pelos autores).** Figura 5a mostra a região oscilatória (H1 a H2) com taxa de diluição crescente. Nas curvas de variância, S_max e autocorrelação (5b, 5c), os valores **crescem** ao se aproximar de H1 e de H2 **pelo lado do equilíbrio**: para H2, os pontos à direita (equilíbrio) têm valores baixos e sobem ao se aproximar de H2. Do lado **oscilatório** de H2 (diluição de cerca de 0.7 a 1.17) as curvas de S_max e de autocorrelação de lag 1 caem ao se aproximar de H2. A leitura é de tendência visual numa figura, sem uso de valores (regra 8); os autores não discutem este trecho. O texto diz "Preceding both Hopf bifurcations" no sentido do lado do equilíbrio.

**A7c-F5 · o dado empírico que mais se aproxima do sentido do P4 existe e vai na direção oposta à do CSD. `A` (texto) / `C` (leitura da figura)**
A única observação de bifurcação de Hopf com os dois lados num experimento é o quimióstato de Bury: aproximando-se de H2 pelo lado oscilatório, as medidas parecem **diminuir**, não aumentar (leitura visual, grau C), e os autores só analisam a aproximação pelo lado do equilíbrio (item 10). Isto é consistente com A7c-F3 (o indicador pode inverter), mas **não** é teste do P4: é um experimento controlado com parâmetro fixo por série (item 13), de população e não de dínamo, e H2 aqui não é demonstrada supercrítica nem subcrítica.

**A7c-F4 atualizada:** a fonte direta para a perda de um ciclo limite estelar continua não achada (X), mas agora há **uma fonte com os dois sentidos num dado real**, que não os analisa. A sugestão do próprio artigo (item 13) é testar em dados naturais de alta resolução com condições variáveis.
