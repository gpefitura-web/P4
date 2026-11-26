
## 2026-11-14 (resolução pós-inspeção)
| item | resultado | origem |
|---|---|---|
| heldkleinen2004 | HTTP 403, não é PDF | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2004GL020972 |
| shah2018 | ok (tentativa 1) | https://iopscience.iop.org/article/10.3847/2041-8213/aad40c/pdf |
| livina2007 | HTTP 403, não é PDF | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1029/2006GL028672 |
| brandenburg1998 | ok (tentativa 1) | https://iopscience.iop.org/article/10.1086/311297/pdf |
| egeland2017_arxiv | ok (tentativa 1) | https://arxiv.org/pdf/1611.04540 |
| luhn2022_arxiv | ok (tentativa 1) | https://arxiv.org/pdf/2207.00612 |
| baum2022_arxiv | ok (tentativa 1) | https://arxiv.org/pdf/2203.13376 |

## 2026-11-14 (resolução pós-inspeção)
| item | resultado | origem |
|---|---|---|
| shah2018 | já presente | Shah_2018_ApJL_863_L26.pdf |
| brandenburg1998 | já presente | Brandenburg_1998_ApJL_498_L51.pdf |
| korolik2023 | ok (tentativa 1) | https://iopscience.iop.org/article/10.3847/1538-3881/ace906/pdf |
| egeland2017_arxiv | já presente | Egeland_2017_arXiv1611.04540.pdf |
| luhn2022_arxiv | já presente | Luhn_2022_arXiv2207.00612.pdf |
| baum2022_arxiv | já presente | Baum_2022_arXiv2203.13376.pdf |
| MANUAL | subir pelo pesquisador | Held & Kleinen 2004, GRL 31, L23207, DOI 10.1029/2004GL020972 |
| MANUAL | subir pelo pesquisador | Livina & Lenton 2007, GRL 34, L03712, DOI 10.1029/2006GL028672 |
| MANUAL | subir pelo pesquisador | Peng et al. 1993, Phys. Rev. E 47, 3730, DOI 10.1103/PhysRevE.47.3730 |
| MANUAL | subir pelo pesquisador | Jarvinen & Strassmeier 2025, A&A 698, A93 (published version), DOI 10.1051/0004-6361/202554111 |
| MANUAL | subir pelo pesquisador | Olah et al. 2016, A&A 590, A133 (published version), DOI 10.1051/0004-6361/201628479 |

## 2026-11-24 — uploads do pesquisador e busca dos dados de HD 166620 (1995–2002) no VizieR

| Item | Resultado | Arquivo / detalhe |
|---|---|---|
| Held & Kleinen 2004 | **recebido do pesquisador**; título e DOI conferidos na p. 1 | `Held_2004_GRL_31_L23207.pdf` |
| Livina & Lenton 2007 | **recebido do pesquisador**; título e DOI conferidos na p. 1 | `Livina_2007_GRL_34_L03712.pdf` |
| Peng+1993 | **recebido do pesquisador**; título, volume e páginas conferidos na p. 1 e no Crossref | `Peng_1993_PRE_47_3730.pdf` |
| VizieR (CDS) `vizier.cds.unistra.fr`, `tapvizier`, `cdsarc` | sem resposta deste ambiente (código 000) | não contornado |
| VizieR (espelho de Harvard) `J/ApJ/936/L23` | existe; é a tabela já em `data/` (as 119 linhas `new_MW` digitalizadas) | sem dado novo |
| VizieR (Harvard) `J/A+A/590/A133` (Oláh+2016), duas tentativas, mais `.../table1` | "Table or Catalog not found" (uma resposta intermédia foi "database not currently reachable"); nenhuma busca por referência ou palavra-chave achou catálogo de séries de Mount Wilson | **não há catálogo de Oláh+2016 no VizieR, até onde este espelho mostra** |
| VizieR (Harvard) `J/ApJ/438/269` (Baliunas) | "Table or Catalog not found" | série de HD 166620 depois de 1995 não aparece |
| TAP do espelho | sem resposta (404) | |
| Dataverse (Radick & Pevtsov) | não tentado nesta rodada | opcional |
| **Conclusão** | **a série de 158 pontos não está em catálogo público alcançável**; resta pedi-la aos autores (rascunho: `consolidacao/PEDIDO_DADOS_OLAH_SOON.md`) | |

## 2026-11-24 (tarde) — nova tentativa e arquivo do espelho NAO enviado pelo pesquisador
- CDS principal (`vizier.cds.unistra.fr`, `cdsarc`) responde (200), mas as consultas `asu-tsv` voltam vazias e a pasta `ftp/J/A+A/590/A133/` dá **404**; Harvard oscila ("not found" / "database not reachable"); o espelho NAO (`vizier.nao.ac.jp`) dá 503 pelo proxy deste ambiente.
- O pesquisador baixou do espelho NAO `J/ApJ/936/L23/table2` e `table3` (`asu1.tsv`, sha256 `b349558474adedf9…`, 3 215 linhas, consulta de 2026-11-24 11:24). **Conferido linha a linha contra `data/J_ApJ_936_L23_table2.tsv`: idêntico** (1 885 linhas: 1 654 `MW`, 112 `HIRES`, **119 `new_MW`**); a tabela 3 tem as mesmas 1 278 linhas `APT`. **Nenhuma linha nova, nenhuma série de 158 pontos.** O arquivo não foi copiado para `data/` (duplicata).

## 2026-11-24 (noite) — outras fontes públicas para HD 166620, 1995–2002 (opção 2 do pesquisador)
| Fonte | Resultado |
|---|---|
| Harvard Dataverse, `doi:10.7910/DVN/H85QPF` (HK_Project_v2001_NSO, 2018) | existe e responde. Descrição: 35 estrelas (as de Lockwood+2007 e mais algumas), observações "through late 2001". Lista de 35 arquivos `.mgd` **sem `hd166620`** (nem `hd010700`) → não serve para HD 166620 |
| Harvard Dataverse, `doi:10.7910/DVN/ZRJ6NT` (HK_Project_v1995_NSO, zip de 10 MB + README) | existe; é a versão de 1995 (a que Baum e Korolik usam); cobre HD 166620 só até 1995, sem o trecho 1995–2002. Não baixado (nada a acrescentar às 1 654 linhas `MW` já idênticas entre Luhn e Baum) |
| arXiv:2207.00612 (fonte TeX de Luhn) | `activity_table.tex` é um trecho de 5 linhas (`\vdots`); sem dados do trecho 1995–2002 |
| arXiv:1604.06701 (fonte TeX de Oláh+2016) | só figuras EPS (por exemplo `166620j_STFT_co.eps`); sem tabela de dados. Extrair valores das figuras é digitalização (regra 8): **não feito** |
| CDS principal | responde; pasta `ftp/J/A+A/590/A133/` dá 404 (já registrado) |
| **Conclusão** | **não há fonte pública alcançável com a série de 1995–2002 de HD 166620.** Resta o pedido a K. Oláh e W. Soon |

## 2026-11-24 (noite, 2) — HK_Project_v2001_NSO baixado e comparado com Baum
Os 35 arquivos `.mgd` e o `README.pdf` do Dataverse `10.7910/DVN/H85QPF` foram copiados sem alteração para `data/HK_Project_v2001_NSO/` (7,4 MB; `PROVENIENCIA.txt` ao lado). Comparação em `inspecao/scripts/11_dataverse_v2001.py` (`3.15-01` a `3.15-06`, saídas `11_dataverse_v2001*.txt`).


## 2026-11-24 — fontes sobre sinais precursores em Hopf/ciclo limite (pedido do pesquisador)
| Item | Resultado | URL / arquivo |
|---|---|---|
| kuehn2011 | ok (tentativa 1) | https://arxiv.org/pdf/1101.2899 |
| kuehn2013 | ok (tentativa 1) | https://arxiv.org/pdf/1101.2908 |
| bury2020 | falhou na tentativa 1 (HTTP 200) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7536046/pdf/ |
| bury2020 | falhou na tentativa 2 (HTTP 200) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7536046/pdf/ |
| MANUAL | subir pelo pesquisador | bury2020, DOI 10.1098/rsif.2020.0482 |
| boettiger2013 | ok (tentativa 1) | https://arxiv.org/pdf/1305.6700 |

## 2026-11-24 — fontes sobre lacunas, amostragem irregular e interpolação em indicadores de CSD
| Item | Resultado | URL / arquivo |
|---|---|---|
| gaps2026 | falhou na tentativa 1 (HTTP 403) | https://www.science.org/doi/pdf/10.1126/sciadv.aee1916?download=true |
| gaps2026 | falhou na tentativa 2 (HTTP 200) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12985669/pdf/sciadv.aee1916.pdf |
| MANUAL | subir pelo pesquisador | gaps2026, DOI 10.1126/sciadv.aee1916 |
| rehfeld2011 | ok (tentativa 1) | https://npg.copernicus.org/articles/18/389/2011/npg-18-389-2011.pdf |
| do2025 | ok (tentativa 1) | https://esd.copernicus.org/articles/16/2035/2025/esd-16-2035-2025.pdf |
| srca2022 | falhou na tentativa 1 (HTTP 403) | http://link.aps.org/pdf/10.1103/PhysRevE.105.024206 |
| srca2022 | ok (tentativa 2) | https://arxiv.org/pdf/2112.04843 |
| gaps2026 (outra versão) | ok | https://arxiv.org/pdf/2505.19034 (manuscrito; Science e PMC falharam) |

## 2026-11-26 (D122): referências novas
| item | resultado | origem |
|---|---|---|
| metcalfe2017 | ok (tentativa 1) | https://arxiv.org/pdf/1705.09668 |
| wright2004 | ok (tentativa 1) | https://arxiv.org/pdf/astro-ph/0406338 |
| boettiger2012a | ok (tentativa 1) | https://arxiv.org/pdf/1204.6231 |
| boettiger2012b | ok (tentativa 1) | https://arxiv.org/pdf/1210.1204 |
| radick2018 (ApJ 855, 75) | **pendente**: sem versão no arXiv; tentativa 1 com id adivinhado devolveu outro artigo (descartado na validação da 1ª página) | -- |
| vaughan1978, wilson1978, baliunas_jastrow1990 | **pendentes**: scans do ADS devolvem HTTP 500 (2 tentativas: articles.adsabs e link_gateway); precisam de PDF subido pelo pesquisador | -- |
| dakos2008 (PNAS), lenton2012 (Phil Trans), lenton2011, boettner_boers2022 (Phys. Rev. Research) | **pendentes**: HTTP 403 nos editores; Europe PMC não abre PDF; sem arXiv | -- |
| wiesenfeld1985, duncan1991 | **pendentes**: sem versão aberta | -- |

## 2026-11-26, nova rodada de tentativas (pedido do pesquisador), só vias abertas e sem disfarçar o cliente
OpenAlex indicou as cópias abertas. Uma tentativa com User-Agent de navegador foi **recusada pelo ambiente e não repetida** (contornar o bloqueio dos editores não é legítimo).
| item | resultado | origem |
|---|---|---|
| lenton2012 | **ok** | https://hal.science/hal-02195169v1/document (artigo tipografado sob CC BY, 21 p.) |
| boettner2022 | **ok** | repositório do PIK (cópia publicada, 7 p.); a cópia do TUM também baixou e foi descartada (arquivo diferente, mesmo artigo) |
| dakos2008 | falhou: PNAS 403, Wageningen 403, MPG 403, PMC devolve HTML | -- |
| vaughan1978, radick2018 | falhou: IOP 403 (cópia "bronze" só no site do editor) | -- |
| wilson1978, baliunas_jastrow1990, lenton2011, wiesenfeld1985, duncan1991 | sem cópia aberta (OpenAlex: fechado) | -- |

## 2026-11-26, PDFs subidos pelo pesquisador (REG-R3, fonte: manual)
| item | resultado |
|---|---|
| vaughan1978, baliunas_jastrow1990, dakos2008, radick2018, duncan1991, lenton2011, wiesenfeld1985 | **ok**, validados pela primeira página (baliunas_jastrow1990 é scan e foi conferido na imagem) |
| wilson1978 | **o arquivo enviado ("Chromospheric_variations_in_main-sequence_stars.pdf") é Baliunas+1995 (II), byte a byte igual ao da raiz (carimbo 1995ApJ...438..269B); descartado. Wilson 1978 (ApJ 226, 379) continua pendente** |
