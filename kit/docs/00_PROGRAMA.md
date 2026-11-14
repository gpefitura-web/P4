# PROGRAMA E RESTRIÇÕES FIXAS

Destilado de `UNIVERSAL_PAPER_CONTEXT.md` (programa "Critical Phenomena in Stellar Magnetic Activity"). O programa de papers concreto fica em `programas/<nome>/` e é opcional; o resto vale para qualquer paper que use este kit na linha de trabalho do usuário (física de atividade estelar com dados públicos).

## Restrições (REG-PROG)
**Dados**: proibida qualquer redução fotométrica (aperture, PSF, detrending de curvas de luz brutas, detecção de flares em pixels). Usar só dados já públicos e reduzidos (catálogos publicados, tabelas de artigos, VizieR, MAST, ADS, HEASARC). Formatos aceitos: CSV, FITS de catálogos, ASCII, séries de índices já calculados.

**Análise**: pipeline em Python (numpy, scipy, astropy, pandas, powerlaw). Leis de potência sempre por **MLE**, nunca regressão linear em log-log. Incertezas por bootstrap ou propagação analítica, nunca omitidas.

**Escrita**: manuscrito em inglês (variante conforme a revista), tom conciso e científico, sem rodeios (evitar "it is interesting to note", "it is worth mentioning", "in this paper we will show"). Presente para resultados estabelecidos e passado para o que foi feito. Estilo da prosa: REG-ESTILO.

## Itens superados pelo P1 (não seguir o documento original)
| Original | O que valeu no P1 |
|---|---|
| "Documento imutável; atualizar só o `paper_state.md`" | O estado vive em `CADERNO`, `DECISIONS`, `PAPER_STATE`; o kit evolui por versão (docs/EVOLUCAO.md) |
| "American English, padrão AAS/IOP" | A revista decide (EPL: britânico consistente) |
| Template LaTeX AAS (`aastex`), `\citep` natbib, abreviações AAS | Módulo por revista em `revistas/<rev>/`; o BibTeX do ADS usa macros de periódico que o `make_references_bib.py` define |
| Figuras "fig1.pdf", 3,5/5/7 polegadas | `figure1.eps` + PDF, larguras da revista (EPL: 80 e 165 mm) |
| Project Knowledge do claude.ai | Arquivos versionados no repositório (kit + estado), lidos por qualquer sessão |
| Uma conversa por tipo (planejamento, análise, figuras, escrita, revisão) | Etapas E0 a E11 (docs/ARQUITETURA.md) com aprovação em cada uma |
| Checklist de submissão ApJ | `docs/SUBMISSAO.md` + ficha da revista |
| Hipótese de valores como "α BTW 1,8 ou 2" | Não usar valores sem fonte lida (REG-03; P1: DEC-24 D-G) |

## Estratégia de publicação (opcional, por programa)
Ver `programas/stellar-activity-29/`: tabela mestre de periódicos, trilhas paralelas, "escrever enquanto espera", RNAAS para prioridade, arXiv no dia da submissão, plano de desk rejection. O núcleo do kit não depende disso; a revista de cada paper é decidida com o usuário (P1: EPL).
