# Reproduction package (version 2.0.0): critical slowing down indicators and the loss of a stellar activity cycle

This folder holds everything needed to reproduce every number, table and figure of the manuscript (`manuscrito/main.tex`), and nothing else:
the input data, the code, the reference outputs and the manuscript sources. `MANIFEST.sha256` lists every file; `reproduce.sh` checks it.

## Run
```
pip install -r requirements.txt                  # Python 3.13
PYTHON=python3 bash reproduce.sh                 # about 12 minutes
PYTHON=python3 bash reproduce.sh --full          # about 1.5 hours; also re-runs the calibration simulations in full
```
`reproduce.sh` (1) checks the manifest, (2) saves the published outputs to `_published/` and clears them, (3) runs the checks, the size test of the
surrogate procedure, the power simulation and the single stellar run (fixed seeds), (4) runs the calibration analyses, (5) rewrites the generated
blocks of `main.tex`, the macros, tables and figures, (6) compares everything with the published outputs (`REPRODUCTION OK`), and (7) compiles the
manuscript if `pdflatex` is installed (class `elsarticle`).

The calibration simulations (positive controls, power curves, instrumental step, data choices) are large. By default they run in a reduced form
(`--quick`: same seeds, fewer series and surrogates) in `pipeline_v2/results_calibration_quick/`, and `verify_calibration.py` checks that every
rejection rate agrees with the stored full run within four standard errors and that the statistics computed on the data alone are identical. The stored
full outputs in `pipeline_v2/results_calibration/` are checked by sha256 (`CALIBRATION_MANIFEST.sha256`); with `--full` they are regenerated and must
match byte for byte. The macros, tables and figures are always rebuilt from the stored full outputs.

The sunspot group numbers of Vaquero et al. (2016) are not redistributed (terms of use not yet checked). Give the file with `VAQUERO_FILE=...` to re-run the
sunspot analysis; without it, the stored result and the derived annual series (`results_calibration/dalton_annual.csv`) are used.

## Layout
| Path | Content |
|---|---|
| `consolidacao/p4_star_catalog.csv` | frozen star catalog (groups, B-V, eligibility) |
| `baum2022_59stars.csv` | stellar parameters of the 59 stars of Baum et al. (spectral type, log g), read by `make_tables_calibration.py` |
| `data/` | input series: Baum et al. Table 1 (VizieR J/AJ/163/183), Luhn et al. Table 2 (VizieR J/ApJ/936/L23), Isaacson et al. Table 4 (VizieR J/ApJS/274/35; used only to count how many stars have a cycle amplitude), HK_Project_v2001_NSO (Harvard Dataverse) |
| `pipeline_v2/` | stellar pipeline (`p4io`, `annual`, `indicators`, `detrend`, `surrogates`, `state_comparison`, `rhk`, `run_all`, `group_primary`, `report`, `power_simulation`), tests, figure fonts, `results/` |
| `pipeline_v2/calibration/` | calibration analyses; stored full outputs in `pipeline_v2/results_calibration/` |
| `manuscrito/` | `main.tex`, `calibration_macros.tex`, `cal_table_*.tex`, `references.bib`, highlights, `figures/` (PDF and EPS), `build.sh` |

## From the manuscript to the code
| Manuscript item | Produced by | Output |
|---|---|---|
| Sample and segments (Sect. 2.1; Table 1) | `p4io.py`, `annual.py` (via `run_all.py`), `make_tables_calibration.py` | `results/segments.csv`, `manuscrito/cal_table_stars.tex` |
| Indicators, detrending, surrogate test (Sect. 2.2) | `indicators.py`, `detrend.py`, `surrogates.py`, `run_all.py` | `results/star_results.csv` |
| Simulations (Sect. 2.3; Table 2) | `calibration/*.py`, `make_tables_calibration.py` | `manuscrito/cal_table_simulations.tex` |
| Size of the test (Sect. 3.1) | `test_step5.py`, `calibration/power_bilateral.py` | `results/autotest_step5.txt`, `results_calibration/power_bilateral.*` |
| Distribution of the stellar p values (Sect. 3.1; Fig. 1) | `calibration/qq_pvalues.py` | `results_calibration/qq_pvalues.*` |
| Positive controls (Sect. 3.2; Table 3; Figs. 2, 3) | `calibration/positive_control_full.py`, `example_series.py`, `power_bilateral.py` | `results_calibration/positive_control_full.*`, `example_series.csv`, `power_bilateral.*` |
| Power against a true rise (Sect. 3.3; Fig. 4) | `calibration/power_design.py`, `power_bilateral.py` | `results_calibration/power_design.*` |
| Instrumental step and data choices (Sect. 3.4; Fig. 5) | `calibration/step_injection.py`, `robustness_data.py`, `robustness_post.py` | `results_calibration/step_injection.*`, `robustness_data.*`, `robustness_post.txt` |
| Stellar scan (Sect. 3.5) | `run_all.py`, `make_macros.py` | `results/star_results.csv` |
| HD 166620 by state (Sect. 3.6; Table 4; Figs. 6, 7) | `state_comparison.py` (via `run_all.py`), `h1_bootstrap.py`, `calibration/f_sensitivity.py` | `results/h1.json`, `results/h1_bootstrap.*`, `results_calibration/f_sensitivity.txt` |
| Sunspot numbers, Dalton Minimum (Sect. 3.7; Fig. 8) | `calibration/dalton_control.py`, `fetch_vaquero.py` | `results_calibration/dalton_control.*`, `dalton_annual.csv`, `dalton_meta.txt` |
| Conversion to R'_HK (Appendix A) | `rhk.py`, `run_all.py`, `scale_sensitivity.py` | `results/star_results.csv` (series `RHK`), `results/scale_sensitivity.txt` |
| Group tests (Appendix B) | `run_all.py`, `group_primary.py` | `results/star_metrics.csv`, `group_primary.csv`, `group_holm.csv` |
| Table of indicators by segment, Figs. 9-11 (Appendix C) | `make_tables.py`, `make_figures.py` | block between `%%% BEGIN/END GENERATED TABLE`, `manuscrito/figures/Figure_2-4` |
| Analysis log (Sect. 2.6): first run against the second | `compare_runs.py`, `archive/star_results_run1.csv` | `results/run_comparison.txt` |
| Earlier power studies (power with a cycle, grid, first positive control, coverage) | `power_simulation.py`, `power_cycle.py`, `power_grid.py`, `positive_control.py`, `robustness.py` | `results/*.txt` |
| Numbers in the text | `make_macros.py`, `make_macros_calibration.py` | block between `%%% BEGIN/END GENERATED MACROS`, `manuscrito/calibration_macros.tex` |
| Design constants written in the text | `check_manuscript_constants.py` | fails if `main.tex` and the code disagree |
| Figure 6 and Figures 9 to 11 | `make_figures.py` | `manuscrito/figures/Figure_N.pdf` and `.eps` |
| Figures 1 to 5, 7, 8 | `make_figures_calibration.py` | `manuscrito/figures/cal_fig*.pdf` and `.eps` |
| Facts report | `report.py` | `results/REPORT.md` |

Seeds: stellar run 20261124; size test 5050; power simulation 1600 + L; calibration simulations 20261126 to 20261130 (one per script, listed in Table 2 of the manuscript);
example series 20261201. The figure files are byte-for-byte reproducible (`SOURCE_DATE_EPOCH=0`).
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
