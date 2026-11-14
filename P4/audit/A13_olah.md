# Audit A13 — Oláh et al. 2016, A&A 590, A133 (Mount Wilson, análise tempo-frequência)

| | |
|---|---|
| **Data** | 2026-11-14 |
| **Estado** | **fechada** |
| **Arquivo** | `bib/Olah_2016_AA_590_A133_arXiv1604.06701.pdf` — **manuscrito do arXiv** (a versão publicada devolve HTTP 403; DOI `10.1051/0004-6361/201628479`, Crossref: título, volume 590, A133 conferidos) |
| **Método** | texto nativo (`pdftotext`); Tabela 1 lida por `inspecao/scripts/05_olah_periods.py` (`3.10-01` a `3.10-08`) |
| **Páginas** | manuscrito inteiro (12 páginas) |
| **Motivo da unidade** | prevista em `paper_state_v6.md` §11 item 6; torna-se necessária porque a fonte dos dados de HD 166620 em 1995–2002 é a Figura 2 deste artigo (A13-F2) |

## Valores extraídos

| Quantidade | Valor | Localização | Grau |
|---|---|---|---|
| Amostra | 29 estrelas G–K do levantamento de Mount Wilson, 36 anos | Resumo; §2 | A |
| Método | transformada de Fourier de tempo curto (STFT) e distribuição de Choi–Williams (CWD); períodos de rotação por MuFrAn | Resumo; §2 | A |
| Resultado | pelo menos um ciclo em 28 das 29; 12 estrelas com ciclos simples (P_rot 39.7 ± 6.0 d; ciclos 9.7 ± 1.9 anos) e as demais com ciclos complexos (P_rot 18.1 ± 12.2 d; 7.6 ± 4.9 anos) | Resumo; §3 | A |
| Divisão por idade | simples contra complexo separa-se perto de 2 a 3 Gyr, a idade do hiato de Vaughan–Preston | Resumo; §4 | A |
| Períodos por estrela | Tabela 1: período de rotação, ciclo dominante e faixa, secundários, tendência de longo prazo (`lt`) e o período de Baliunas+1995 | Tabela 1 | A (lida por script) |
| HD 166620 | grupo de ciclos simples; P_rot = 41.5 d; ciclo dominante 13.6 (9.6–17.6) anos; Baliunas 15.8 ± 0.3 | Tabela 1 | A |
| Tendências de longo prazo | marcadas `lt` para HD 3651, 32147, 103095, 160346, 201091, entre outras: componentes longas junto do ciclo são comuns | Tabela 1 | A |

## Achados

**A13-F1 · uma quarta série independente de períodos reforça A9-F3. `A`**
Para 25 estrelas comparáveis com B95, o período dominante de Oláh difere do de B95 por mais de 2 dP em 23; nas 12 `CYCLE` + FAP Excellent comparadas, em 11 (só HD 26965 fica dentro). Reforça a leitura (a) de A9-F3 (o dP de B95 não é incerteza realista) sem excluir (b) (períodos que mudam). Nas estrelas de ciclos complicados (HD 76151, 100180, 149661, 156026, 165341A, 190406) o período dominante de Oláh não é o primário de B95 e a comparação não é equivalente. Em `saidas/05_olah_periods.txt`. Para HD 3651: B95 13.8, Saar 14.6, Oláh 11.6 (9.57–13.7), CLS V 10.01, quatro valores para a estrela que A1-F5 aponta como a candidata a transição.

**A13-F2 · os dados de Mount Wilson de HD 166620 em 1995–2002 que entram em Luhn+2022 foram **digitalizados da Figura 2 deste artigo**. `A` (fato) / `C` (dados)**
O manuscrito de Luhn (arXiv:2207.00612, versão de 5 de julho de 2022) diz: "The full Mount Wilson data (from 1966–2002) were not published, except for a figure in Oláh et al. (2016). We used a web application to scrape the data from Figure 2 of Oláh et al. (2016) for HD 166620. As a result of the scraping process, the scraped data is reliable, but not exact. For example, due to the marker size, dense sampling, and long time baseline of the plot, the scraping procedure was forced to find the mean x and y positions over several points when markers overlapped." e "contains 119 (scraped) observations". A versão publicada troca isso por "A nightly binned version of the full Mount Wilson data … were published in a figure in Oláh et al. (2016) and we have acquired this data courtesy of K. Oláh and W. Soon" e "contain 158 observations".
A tabela do VizieR (`data/J_ApJ_936_L23_table2.tsv`) tem **119** linhas `new_MW`, com S_HK de 6 a 8 casas decimais (por exemplo `0.18682914`) contra no máximo 4 casas nas linhas `MW` e `HIRES`, instantes fora do padrão das linhas de Mount Wilson (72 frações de dia distintas em 119 linhas) e pares com o mesmo instante e S diferentes (`2449942.82`). Esse é o padrão numérico de uma digitalização, e coincide com o manuscrito. Em `inspecao/scripts/03d_luhn.py` e `saidas/`.
Consequência: as 119 linhas são **grau C** pelo protocolo §4 (valor lido de figura) e a regra 8 do `CLAUDE.md` proíbe derivar valores digitalizando figuras; aqui a digitalização é de terceiros e é herdada. Resolve a contradição A10-F1 (158 contra 119): a tabela é o conjunto digitalizado; os 158 são o texto revisado, e a tabela não foi atualizada, ou os dados cedidos pelos autores nunca chegaram ao VizieR (não distinguível com estas fontes).

**A13-F3 · o que não depende dos dados digitalizados. `A`**
σ_S dos três estados e as médias de S_HK usam Mount Wilson de B22 (exato) e HIRES; o F-test também. A lacuna de Baum de 6.91 anos (1997.73 a 2004.64) é real. O que depende dos dados digitalizados: as oito médias anuais de 1995 a 2002, a lacuna de 2.82 anos, o "máximo de 1995" e a afirmação de que a aproximação à transição está amostrada (A10 §1.2, D46, `DECISOES_D41_D54.md` §B).

## Decisões tomadas, com base

1. **As 119 linhas `new_MW` são tratadas como grau C** até que os dados reais (Oláh e Soon) sejam obtidos. *Base:* A13-F2. *(→ D58 no caderno)*
2. **Oláh+2016 entra como fonte de período independente de B95, Baum e Saar, ao lado, não fundida** (D15, D36). *Base:* A13-F1.

## Não resolvido (grau C ou X)

| Quantidade | Por que | Resolução proposta |
|---|---|---|
| Dados reais de Mount Wilson de HD 166620 em 1995–2002 | **C** — só existe a versão digitalizada | pedir a K. Oláh e W. Soon, ou usar só B22 e HIRES |
| Versão publicada de Oláh+2016 | manuscrito do arXiv usado | subir o PDF publicado (DOI acima) |
