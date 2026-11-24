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
