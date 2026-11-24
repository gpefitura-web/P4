
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
- CDS principal (, ) responde (200), mas as consultas  voltam vazias e a pasta  dá **404**; Harvard oscila ("not found" / "database not reachable"); o espelho NAO () dá 503 pelo proxy deste ambiente.
- O pesquisador baixou do espelho NAO  e  (, sha256 , 3 215 linhas, consulta de 2026-11-24 11:24). **Conferido linha a linha contra : idêntico** (1 885 linhas: 1 654 , 112 , **119 **); a tabela 3 tem as mesmas 1 278 linhas . **Nenhuma linha nova, nenhuma série de 158 pontos.** O arquivo não foi copiado para  (duplicata).

