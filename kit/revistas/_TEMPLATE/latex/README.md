Ponha aqui o esqueleto `main.tex` (sem prosa), a classe, os `.bst` e `ORIGEM.md` (URL, data, sha256, licença) da revista.
O contrato com o núcleo: `\input{sec_*}`, `\input{results_macros}` (e `results_extra`), `\graphicspath{{figures/}}`, bibliografia `references` (BibTeX do ADS) e um `.bst` que respeite a ordem de citação da revista.
`scripts/apply_journal.sh <revista>` copia esta pasta para `manuscrito/`.
