# Reproduction package: testing critical slowing down in Mount Wilson S-index series of Sun-like stars

This folder holds everything needed to reproduce every number, table and figure of the manuscript (`manuscrito/main.tex`), and nothing else:
the input data, the code, the reference outputs and the manuscript sources. `MANIFEST.sha256` lists every file; `reproduce.sh` checks it.

## Run
```
pip install -r requirements.txt          # Python 3.13
PYTHON=python3 bash reproduce.sh         # about 6 minutes
```
`reproduce.sh` (1) checks the manifest, (2) saves the published outputs to `_published/` and clears them, (3) runs the checks, the size test of the
surrogate procedure, the power simulation and the single stellar run (fixed seeds), (4) rewrites the generated blocks of `main.tex` and the figures,
(5) compares everything with the published outputs (`REPRODUCTION OK`), and (6) compiles the manuscript if `pdflatex` is installed (class `elsarticle`).

## Layout
| Path | Content |
|---|---|
| `consolidacao/p4_star_catalog.csv` | frozen star catalog (groups, B-V, eligibility) |
| `data/` | input series: Baum et al. Table 1 (VizieR J/AJ/163/183), Luhn et al. Table 2 (VizieR J/ApJ/936/L23), HK_Project_v2001_NSO (Harvard Dataverse, doi:10.7910/DVN/H85QPF). Table 4 of Egeland et al. is **not** included: `pipeline_v2/fetch_egeland_table4.py` downloads it |
| `pipeline_v2/` | code (`p4io`, `annual`, `indicators`, `detrend`, `surrogates`, `state_comparison`, `rhk`, `run_all`, `group_primary`, `report`, `power_simulation`), tests, figure fonts, `results/` |
| `manuscrito/` | `main.tex`, `references.bib`, highlights, `figures/Figure_1-4` (PDF and EPS), `build.sh` |

## From the manuscript to the code
| Manuscript item | Produced by | Output |
|---|---|---|
| Sample, segments (Sect. 2.1; Table 2 columns L, Interp.) | `p4io.py`, `annual.py` (via `run_all.py`) | `results/segments.csv` |
| Indicators, detrending, surrogate p values (Sects. 2.2, 2.3, 3.3; Table 2) | `indicators.py`, `detrend.py`, `surrogates.py`, `run_all.py` | `results/star_results.csv` |
| Size of the surrogate test (Sect. 3.1) | `test_step5.py` | `results/autotest_step5.txt` |
| Power (AUC; Sect. 3.1) | `power_simulation.py` | `results/power_simulation.txt` |
| H1, Table 1, Figure 1 | `state_comparison.py` (via `run_all.py`) | `results/h1.json` |
| R'_HK (Sect. 3.3) | `rhk.py`, `run_all.py` | `results/star_results.csv` (series `RHK`) |
| Group tests (Sect. 3.4) | `run_all.py`, `group_primary.py` | `results/star_metrics.csv`, `group_primary.csv`, `group_holm.csv` |
| All numbers in the text | `make_macros.py` | block between `%%% BEGIN/END GENERATED MACROS` in `manuscrito/main.tex` |
| Design constants written in the text (windows, widths, ARMA grid, size test, power design, B-V band, states) | `check_manuscript_constants.py` | fails if `main.tex` and the code disagree |
| Table 2 | `make_tables.py` | block between `%%% BEGIN/END GENERATED TABLE` |
| Figures 1 to 4 | `make_figures.py` | `manuscrito/figures/Figure_N.pdf` and `.eps` |
| Facts report | `report.py` | `results/REPORT.md` |

Seeds: stellar run 20261124; size test 5050; power simulation 1600 + L. The figure files are byte-for-byte reproducible (`SOURCE_DATE_EPOCH=0`).
Tables and JSON are compared numerically (relative tolerance 1e-9): the ARMA fits depend on the `statsmodels` version, so use the pinned versions.

## Table 4 of Egeland et al. (2017): downloaded, not redistributed
The calibrated solar S-index series (machine-readable Table 4 of the article) is fetched by `reproduce.sh` from the journal's public server
(`https://content.cld.iop.org/journals/0004-637X/835/1/25/revision1/apjaa4e49t4_mrt.txt`) and checked against
sha256 `6e2746d535d7d9e3e69ebc860b840494b5efca5460e613cc43fc46e060a90548` (6349 rows, 1966-2016). Without network access, download it by other means and run
`python pipeline_v2/fetch_egeland_table4.py --from <file>`. The Sun row of Table 2, Figure 3 and the solar numbers need this file; the rest does not.

## Input data shipped here (frozen hashes, first 16 hex digits)
| File | sha256 |
|---|---|
| `consolidacao/p4_star_catalog.csv` | `ab480cb3d2fae1cd…` |
| `data/J_AJ_163_183_table1.tsv` | `7703efab4bdb8ac5…` |
| `data/J_ApJ_936_L23_table2.tsv` | `b48502d68daa55be…` |

## Acknowledgements and terms of the data
The HK_Project_v2001_NSO data derive from the Mount Wilson Observatory HK Project, which was supported by both public and private funds through the
Carnegie Observatories, the Mount Wilson Institute, and the Harvard-Smithsonian Center for Astrophysics starting in 1966 and continuing for over 36 years.
These data are the result of the dedicated work of O. Wilson, A. Vaughan, G. Preston, D. Duncan, S. Baliunas, and many others (`data/HK_Project_v2001_NSO/README.pdf`).
This research has made use of the VizieR catalogue access tool, CDS, Strasbourg, France (doi:10.26093/cds/vizier).

## License
- **Code, derived results and figures produced by it:** MIT License (`LICENSE`), copyright 2026 Airton M. S. Borin Junior.
- **Input data (`data/`, `consolidacao/`):** not covered by the MIT License. Copied unaltered from the sources cited above; the terms of use of each original source apply (the acknowledgement required by the HK Project authors is reproduced above). Table 4 of Egeland et al. is not redistributed.
- **Fonts (`pipeline_v2/fonts/`):** Courier Prime, SIL Open Font License 1.1 (`pipeline_v2/fonts/OFL.txt`).
- **Manuscript sources (`manuscrito/`):** included only so that the numbers, table and figures can be rebuilt; the text is the author's, and the published version will be under the journal's terms.

## How to cite
See `CITATION.cff`. Cite the archived version by its DOI (Zenodo) and the article.
