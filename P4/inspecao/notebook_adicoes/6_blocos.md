## 6 · Itens de ação e bloqueios (atualizado em 2026-11-14)

Ambiente testado em 2026-11-14 (REG-08): respondem Crossref, arXiv, IOP (download público), Semantic Scholar, OpenAlex; **bloqueados** (HTTP 403): Wiley/AGU, site da A&A; Peng+1993 é de acesso fechado; a cópia do PIK de Held & Kleinen é privada (não contornada). `pdftotext` disponível; `tesseract` não (usado RapidOCR e leitura visual).

| Item | Estado | Necessário para |
|---|---|---|
| **Tabela 4 de Egeland+2017** | **resolvida** (D65): `data/Egeland2017_table4_apjaa4e49t4_mrt.txt`, 6 349 linhas, 1966–2016 | D18 |
| **Held & Kleinen 2004**, GRL 31, L23207, DOI 10.1029/2004GL020972 | **pendente — o pesquisador sobe o PDF** (o arquivo que tinha esse nome era Boulton+2014, D63) | A7, D50, Q10 |
| Livina & Lenton 2007, GRL 34, L03712, DOI 10.1029/2006GL028672 | pendente — o pesquisador sobe o PDF (reescalonamento do DFA) | A5, Q9 |
| Peng et al. 1993, Phys. Rev. E 47, 3730, DOI 10.1103/PhysRevE.47.3730 | pendente — o pesquisador sobe o PDF (viés de comprimento finito do DFA) | A5, Q9 |
| Järvinen & Strassmeier 2025, versão publicada, DOI 10.1051/0004-6361/202554111 | opcional — há o manuscrito do arXiv | citação final |
| Oláh+2016, versão publicada, DOI 10.1051/0004-6361/201628479 | opcional — há o manuscrito do arXiv | citação final |
| Dados reais de Mount Wilson de HD 166620 em 1995–2002 (Oláh e Soon) | pendente — grau C até lá (D58) | D46 |
| Harvard Dataverse: Radick & Pevtsov (10.7910/DVN/ZRJ6NT, 10.7910/DVN/H85QPF); Pevtsov 2016 (10.7910/DVN/VF5BMO) | não testados; opcional | offsets de Baum (D44); contexto de D18 |
| Série S solar NSO | dispensada pela D65 (Tabela 4) | — |

Obtidos e validados nesta rodada, em `bib/` (ver `bib/MANIFEST.json`): Shah+2018 (HD 4915), Brandenburg+1998 (Paper I), Korolik+2023 (τ Ceti), Egeland+2017 (arXiv), Luhn+2022 (arXiv), Baum+2022 (arXiv).
