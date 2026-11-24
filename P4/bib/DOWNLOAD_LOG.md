
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

