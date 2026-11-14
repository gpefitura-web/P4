# <Título do paper>

`<paper>.py` is the source of the notebook `<paper>.ipynb` (jupytext percent format). The physics and the decision rules are described in `ESPECIFICACAO_FISICA.md`.

## Running
```
pip install -r requirements.txt
jupytext --to ipynb <paper>.py
jupyter nbconvert --to notebook --execute <paper>.ipynb
```
Run the commands from this folder so that the notebook finds `fonts/`. A complete run takes about N minutes on four cores. Setting `<PAPER>_MODE=fast` runs the same steps with fewer replicates and marks the outputs as not valid for publication.

The notebook downloads the catalogs from VizieR/other sources at run time; no data file is stored in this repository. Downloads are cached in `data_cache/`, which git ignores.

## Outputs
* `analysis_results.md`: every table of the analysis, the validation summary and the limitations found by the run.
* `results_macros.tex`: one LaTeX macro for each number of the manuscript.
* `figures/figureN.eps` and PDF copies.

## Fonts
Courier Prime is released under the SIL Open Font License; its files and licence are in `fonts/`. The notebook stops with a message when the font is not found.
