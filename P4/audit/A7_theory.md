# Audit A7 — Scheffer et al. 2009 (Nature 461, 53) e a fonte de Held & Kleinen 2004

| | |
|---|---|
| **Data** | 2026-11-14 |
| **Estado** | **fechada parcialmente.** Scheffer+2009 auditado por inteiro. Held & Kleinen+2004: **não auditado** (o arquivo do repositório é outro artigo, ver A7-F1). Boulton, Allison & Lenton 2014 auditado como fonte complementar |
| **Método de extração** | texto nativo do PDF (`pdftotext`), conferido por busca literal em `inspecao/scripts/06_pdf_quotes.py` (`3.11-31` a `3.11-35`) e por leitura integral do texto. Equações das Caixas 1 a 3 são imagens ou texto quebrado e **não foram lidas** |
| **Páginas** | Scheffer: PDF pp. 1–7 (Nature pp. 53–59; página do PDF n = página da revista 52 + n). Boulton: PDF pp. 1–9 |
| **Arquivos** | `Scheffer et al. 2009, Nature 461, 53.pdf` (raiz do repositório); `Held & Kleinen 2004, GRL 31, L23207.pdf` (raiz; é Boulton+2014); DOI de Held & Kleinen: `10.1029/2004GL020972` (Crossref: título, volume 31, L23207 conferidos) |

## Valores e afirmações extraídos (mapa afirmação → citação, para a Introdução)

| # | Afirmação | Localização | Grau |
|---|---|---|---|
| 1 | Desaceleração crítica: num ponto de bifurcação *fold* o autovalor dominante se anula; o sistema se recupera cada vez mais devagar de pequenas perturbações; "It can be proven that this phenomenon will occur in any continuous model approaching a fold bifurcation" | Scheffer, PDF p. 1 | **A** (Boulton p. 1 diz o mesmo em termos próprios: "become more sluggish in its response to small perturbations") |
| 2 | A desaceleração produz aumento da autocorrelação de lag 1, interpretável diretamente como lentidão da recuperação sob perturbações naturais | Scheffer, PDF p. 1 | **A** |
| 3 | Aumento da variância é consequência usual, com ressalva: "In principle, critical slowing down could reduce the ability of the system to track the fluctuations, and thereby produce an opposite effect on the variance"; modelos mostram que normalmente aumenta | Scheffer, PDF p. 2 | **A** |
| 4 | Variância e AR(1) não são independentes ("not independent of lag-1 autocorrelation") | Boulton, PDF p. 1 | A |
| 5 | Relação formal AR(1), variância e taxa de recuperação: Caixa 3 | Scheffer, PDF p. 3 | **não lida** (equações ilegíveis no texto) |
| 6 | Assimetria e *flickering*: perto de uma bifurcação catastrófica, com ruído forte, o sistema alterna entre as bacias; aparece como aumento de variância e de assimetria e como bimodalidade | Scheffer, PDF p. 3 | **A** |
| 7 | Sistemas cíclicos e caóticos: "Critical transitions in cyclic and chaotic systems are less well studied" | Scheffer, PDF p. 3 | **A** |
| 8 | Hopf: "the transition from a stable system to an oscillatory system. Like the fold bifurcation, this bifurcation is signalled by critical slowing down: close to the bifurcation, perturbations lead to long transient oscillations before …" | Scheffer, PDF p. 4 | **A** (citação); o **sentido** é o estável → oscilante |
| 9 | Bifurcações não locais (colisão de bacias): "We know of no explicit work on early-warning signals for such transitions"; autocorrelação pode aumentar porque as oscilações se "esticam" perto da fronteira da bacia (conjectura) | Scheffer, PDF p. 4 | **A** |
| 10 | Onde foi demonstrado: oito transições climáticas passadas com aumento de autocorrelação; lagos, pescarias, vegetação, convulsões epilépticas, finanças; "empirical proof that critical slowing down occurs at bifurcations has been provided by controlled experiments with lasers and neurons" | Scheffer, PDF pp. 4–5 | A |
| 11 | Falsos negativos: transição sem aproximação gradual (evento extremo raro) ou por mudança externa rápida e permanente; dificuldade estatística; "the detection of increased autocorrelation may require long time series"; mudança no regime de perturbações distorce os sinais | Scheffer, PDF pp. 5–6 | **A** |
| 12 | Falsos positivos: tendência de confusão no sistema ou no regime externo; resultados "depend on parameter choices in filtering"; é preciso um conjunto de procedimentos estatísticos para testar a significância | Scheffer, PDF pp. 5–6 | **A** |
| 13 | Sinais devem ser lidos em sentido relativo; "the actual moment of a transition remains difficult to predict" | Scheffer, PDF p. 6 | **A** |
| 14 | Boulton: AR(1) e variância crescentes antes do colapso da AMOC num modelo acoplado; significância por 1 000 séries nulas obtidas por *bootstrap*; sinais significativos após ~550 anos de dados anuais, 250 antes do colapso; médias decenais dão estatística pior por terem menos pontos | Boulton, PDF pp. 1, 3, 4 | A |
| 15 | Boulton: a teoria de CSD vale perto do equilíbrio; "If anthropogenic forcing is faster than the intrinsic timescale of the ocean, then the early warning signals should not work as well as the system will not be near to equilibrium" | Boulton, PDF p. 5 | **A** |
| 16 | Held & Kleinen 2004 (aumento de autocorrelação perto de uma bifurcação, "degenerate fingerprinting") | citado em Scheffer, ref. 21, e em Boulton, ref. 20 | **X** — artigo não lido |

## Verificações

- Título, autores e DOI de Scheffer conferidos na página 1 → passa.
- Título do arquivo "Held & Kleinen 2004" contra o conteúdo → **falha** (A7-F1). Os outros oito PDFs da raiz batem com o nome.
- Crossref: Scheffer sem errata (relação `has-review` apenas); Boulton sem errata → passa.

## Achados

**A7-F1 · o arquivo `Held & Kleinen 2004, GRL 31, L23207.pdf` é Boulton, Allison & Lenton 2014, *Nature Communications* 5:5752. `A`**
Metadados do PDF (título, autor) e texto da primeira página; Held & Kleinen aparece só como referência 20. Foi enviado num único commit (`3c6e6ca`). O protocolo §6 define A7 como Scheffer **mais** Held & Kleinen. Para o segundo, o DOI é `10.1029/2004GL020972`; a Wiley devolve HTTP 403 a este ambiente, a cópia do PIK está marcada como privada no registro do repositório e a cópia da Universidade de East Anglia não é pública. O artigo precisa ser subido pelo pesquisador (`fonte: manual`, REG-R3).

**A7-F2 · o sentido da bifurcação de Hopf em Scheffer é estável → oscilante; o caso do P4 é oscilante → estável. `A` (citação) / leitura própria**
A10-F5 já pedia que A7 distinguisse Hopf de sela-nó, porque o objeto que bifurca no P4 é a periodicidade. Scheffer descreve a Hopf como a passagem de um sistema estável a um oscilatório, com transientes oscilatórios longos perto da bifurcação, e afirma que sistemas cíclicos são menos estudados. A perda de um ciclo limite (ciclo → plano) é o sentido oposto. **Nenhuma das duas fontes lidas (Scheffer, Boulton) apresenta sinal precursor para a perda de um ciclo limite**; a extensão é por analogia. A afirmação de que o sentido pesa é interpretação minha; o que cada artigo diz está nas linhas 7–9 da tabela.

**A7-F3 · as condições de falso negativo de Scheffer e de Boulton são as de D46 e D50. `A` (citação)**
Transição por mudança rápida, ou sem aproximação gradual, é falso negativo declarado. Boulton acrescenta que, se o forçamento é mais rápido que a escala intrínseca, os sinais "should not work as well". CLS VI §3.3 fala de transição "on order of years" (inferida de uma lacuna na distribuição de S-STD entre estrelas, não de uma série temporal) e Luhn+2022 mostra uma transição entre observações separadas por anos. Que a escala de aproximação do P4 seja lenta ou rápida em relação à amostragem é a pergunta Q10 e não está respondida por estas fontes.

**A7-F4 · bimodalidade e *flickering*: apoio qualitativo ao argumento de biestabilidade de D50, com ressalva de observável. `A` (citação) / leitura própria**
Scheffer: perto de uma bifurcação catastrófica o *flickering* aparece como aumento de variância, de assimetria e bimodalidade na distribuição de estados **de um mesmo sistema ao longo do tempo**. A bimodalidade citada pela CLS VI é a distribuição de S-STD **entre estrelas** (transversal). Não são o mesmo observável; o paralelo mais direto é o de Usoskin (A8): a distribuição bimodal do número de manchas decenal do Sol ao longo do Holoceno, em que os grandes mínimos formam um modo separado.

**A7-F5 · exigências estatísticas. `A`**
Séries longas, escolha de filtragem e janela que afeta o resultado, significância por conjunto nulo (Scheffer pede "a set of reliable statistical procedures"; Boulton usa 1 000 membros por *bootstrap*; Dakos+2012, A4, usa 1 000 *surrogates* ARMA). Boulton registra que médias decenais (menos pontos) dão estatística pior. D46 (8 médias anuais) e D22 não são contraditos por nenhuma delas.

## Decisões tomadas, com base

1. **A7 fecha parcialmente.** Scheffer e Boulton auditados; Held & Kleinen pendente (A7-F1). *Base:* verificações acima.
2. **A resposta teórica de D50 fica com apoio parcial e uma lacuna declarada** (A7-F2, A7-F4). Nenhuma decisão de mérito: a avaliação de se a resposta é sustentável é do pesquisador (item 6 da §E de `DECISOES_D41_D54.md`).
3. **Todo PDF novo é validado pela primeira página antes de entrar** (REG-R2). *Base:* A7-F1.

## Não resolvido (grau C ou X)

| Quantidade | Por que | Resolução proposta |
|---|---|---|
| Held & Kleinen 2004: conteúdo | **X** — arquivo trocado, acesso bloqueado | o pesquisador sobe o PDF (DOI `10.1029/2004GL020972`) |
| Equações das Caixas 1 a 3 de Scheffer | **X** — ilegíveis no texto extraído | ler as imagens de página se a Introdução for citar a forma analítica |
| Sinal precursor para perda de ciclo limite | **X** — não encontrado nas fontes lidas | declarar como extensão por analogia |
