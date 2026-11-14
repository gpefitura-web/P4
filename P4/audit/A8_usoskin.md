# Audit A8 — Usoskin et al. 2017, Living Rev. Sol. Phys. 14, 3

| | |
|---|---|
| **Data** | 2026-11-14 |
| **Estado** | **fechada, com leitura parcial declarada** |
| **Método de extração** | texto nativo (`pdftotext`); busca literal em `inspecao/scripts/06_pdf_quotes.py` (`3.11-36` a `3.11-38`) |
| **Páginas lidas** | PDF pp. 1–8 (resumo e §1), §2 até o fim de §2.4.3 (PDF p. 23), §4 inteiro (PDF pp. 55–66) e os parágrafos-resumo que repetem o §4. **Não lidos página a página:** §3 (física dos isótopos cosmogênicos), §5 (partículas energéticas solares) e as referências. Nada deles é citado abaixo |
| **Arquivo** | `Usoskin et al. 2017, Living Rev. Sol. Phys. 14, 3.pdf` (raiz do repositório; título e DOI `10.1007/s41116-017-0006-9` conferidos na página 1; é a versão revista de `10.12942/lrsp-2013-1`, Crossref: `new_version`) |

## Valores extraídos

| Quantidade | Valor | Localização (página do PDF) | Grau |
|---|---|---|---|
| Previsibilidade de grandes mínimos | "a grand minimum should appear soon or later, but presently we are hardly able to predict its occurrence" | p. 23 (§2.4.3) | **A** |
| Previsão para além da escala de um ciclo | "so far there is no evidence of any method giving a reasonable prediction of solar activity beyond the solar-cycle scale … probably because of the intrinsic limit of solar-activity predictability due to its stochastic/chaotic nature" | p. 23 | **A** |
| Precursor do mínimo de Maunder | "Until recently, it was believed … that transition from the normal high activity to the deep minimum did not have any apparent precursor before MM. However, newly recovered data suggest that the start of the Maunder minimum might had been not very sudden but via a regular cycle of reduced height (Vaquero et al. 2011)" | p. 58 | **A** |
| Comprimento do ciclo antes de um grande mínimo | "an indication that the length of solar cycle may slightly extend during and already slightly before a grand minimum (Miyahara et al. 2004; Nagaya et al. 2012)" | p. 58 | **A** (citação); fonte primária não auditada |
| Número de grandes mínimos no Holoceno | 25 listados na Tabela 2 (reconstrução de 11 000 anos); "27 grand minima identified during the Holocene" na discussão estatística | pp. 59, 61 | A (os dois números aparecem no texto) |
| Fração do tempo em grande mínimo | duração cumulativa ≈ 1 900 anos, ~1/6 (17 %); nas conclusões "15–20 %" | pp. 59, 66 | A |
| Duração dos grandes mínimos | média 70 anos; distribuição bimodal: curtos (30–90 anos, tipo Maunder) e longos (> 100 anos, tipo Spörer) | p. 61 | **A** |
| Definição operacional | o modo de baixa atividade da distribuição bimodal do número de manchas decenal ("decadal sunspot numbers below 20") correspondente a grandes mínimos; "the definition of grand minima is quite robust"; a de grandes máximos é menos robusta (média suavizada de 50 anos acima de 50) | pp. 59, 63 | **A** |
| Entrada num grande mínimo | **não definida** como evento datado; o artigo lista centros e durações (Tabela 2) | p. 60 | — |
| Ocorrência | modelos de dínamo estocásticos predizem ocorrência poissoniana; os dados mostram desvio ("memory" ou aglomeração em torno do ciclo de Hallstatt de ~2400 anos), mas "can be an artefact of the small statistics (only 27 grand minima)" | p. 61 | **A** |
| Natureza do estado | "Once falling into a grand minimum as a result of a stochastic/chaotic, but non-Poisson process, the dynamo is 'trapped' in this state" | p. 61 | A |
| Mínimo solar de 2008–2009 | "unusual for the space era but may be quite typical for the normal activity"; o ciclo 24 "indicates the return to the normal moderate level of solar activity" | p. 4 | **A** |
| Grande mínimo em curso | "contrary to some predictions, a Grand minimum of activity has no started" (sic) | p. 4 | **A** |
| Grande máximo moderno | média do número de grupos 75 ± 3 em 1950–2000 contra 35 ± 9 em 1750–1900; "has ceased after solar cycle 23" | pp. 62, 66 | A |
| Amplitude do ciclo 24 frente aos ciclos 15–23 | só qualitativa ("moderate, much more shallow than for the previous cycles"); o número está em Egeland+2017 (A3, D19): amplitude 0.0178 no ciclo 22 e 0.0089 no 24 | Usoskin p. 62; Egeland Tabela 2 | A (Egeland) |

## Verificações

- Título e DOI na página 1 → passa.
- Crossref: sem errata; `new_version` aponta o artigo de 2013, o que o próprio PDF declara → passa.

## Achados

**A8-F1 · a literatura diz que a previsão de um grande mínimo não é possível hoje. `A`**
"hardly able to predict its occurrence" e "no evidence of any method" além da escala de um ciclo (p. 23). Este é o enunciado mais próximo da hipótese do P4 e tem de ser tratado na Discussão, conforme o protocolo §6 (A8). O artigo se refere a métodos de previsão baseados em índices solares e em dínamos, não a indicadores de desaceleração crítica; esses últimos não aparecem nele.

**A8-F2 · há indícios de precursor no Maunder, mas com fonte primária não auditada. `A` (citação) / `X` (fonte primária)**
Ciclo de altura reduzida antes do mínimo (Vaquero+2011) e alongamento do ciclo antes de um grande mínimo (Miyahara+2004, Nagaya+2012). São os únicos sinais precursores citados. Nenhum é de tipo CSD (autocorrelação ou variância); Vaquero, Miyahara e Nagaya não foram auditados.

**A8-F3 · a série solar de 1966 a 2016 cobre o fim de um grande máximo, não a aproximação de um grande mínimo. `A`**
O ciclo 24 é descrito como retorno à atividade moderada e o grande mínimo "has not started". O mínimo de 2008–2009 é "incomum para a era espacial", e não excepcional em contexto secular. O protocolo (A8) pedia número e fonte para a afirmação de que o mínimo de 2008–2010 foi excepcional: a fonte dá o contexto qualitativo acima, sem número de excepcionalidade. Quem escreve a Introdução precisa de outra fonte ou de outra formulação.

**A8-F4 · bimodalidade do Sol e das estrelas. `A` (citação) / leitura própria**
A distribuição do número de manchas decenal tem modo de grande mínimo separado do modo de atividade moderada (p. 59). É o paralelo solar da bimodalidade de S-STD da CLS VI, ambas **distribuições de estados**, não séries temporais com sinal precursor (ver A7-F4).

**A8-F5 · estatística pequena. `A`**
Os próprios autores avisam que a ocorrência não poissoniana pode ser artefato de 27 eventos (p. 61).

## Decisões tomadas, com base

1. **A8 fecha com a ressalva de leitura parcial** (§3 e §5 não lidos). *Base:* tabela de páginas lidas.
2. **A frase sobre o mínimo de 2008–2010 como "excepcional" não é sustentada por esta fonte** (A8-F3); é registro de fato, não decisão de redação. *Base:* p. 4.

## Não resolvido (grau C ou X)

| Quantidade | Por que | Resolução proposta |
|---|---|---|
| Quantificação da excepcionalidade do mínimo de 2008–2010 em contexto de um século | **X** — Usoskin só dá contexto qualitativo | buscar fonte quantitativa, ou reformular |
| Fontes primárias de precursor (Vaquero+2011, Miyahara+2004, Nagaya+2012) | **X** — não auditadas | auditar se a Discussão for citá-las |
| §3 e §5 de Usoskin | não lidos | ler só se algum dado deles for usado |
