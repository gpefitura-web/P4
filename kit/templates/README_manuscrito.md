# Manuscrito

Esta pasta é enviada ao Overleaf (`bash scripts/sync_overleaf.sh` gera `manuscrito_overleaf.zip`). Ela é autocontida: nenhum caminho `../`.

## Compilar localmente
```
bash scripts/build_manuscript.sh
```
Monta `references.bib` e `journal_macros.tex` a partir das chaves citadas, copia macros e figuras de `../repositorio`, roda pdflatex e bibtex, mostra o número de páginas e executa `scripts/check_manuscript.py`.
Pacotes Debian/Ubuntu: `texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-bibtex-extra texlive-science poppler-utils` (apt-get update antes).

## Regras
* Os números vêm de `results_macros.tex` e nunca são digitados no texto (REG-MAC).
* Cada chave citada precisa ter BibTeX do ADS em `referencias/bib` e PDF em `referencias` (REG-R2, REG-R6).
* Estilo da prosa e política de IA: `kit.yml` e `kit/docs/REGRAS_PROCESSO.md`.
* O esqueleto e o estilo bibliográfico vêm do módulo da revista (`kit/revistas/<revista>/`).
