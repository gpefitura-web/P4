#!/usr/bin/env bash
# Reproduces every number, table and figure of the manuscript from the input data and compares them with the published outputs.
# Usage: PYTHON=/path/to/python [VAQUERO_FILE=/path/to/GNobservations_JV_V1-12.csv] bash reproduce.sh [--full]
# Default: about 12 minutes (Python 3.13 with requirements.txt). The calibration simulations run in a reduced form (same seeds, fewer series) and are
# checked against the stored full outputs by sha256 and by agreement of the rejection rates. --full re-runs them in full (about 1.5 hours) and
# requires the stored outputs to be reproduced byte for byte. Without VAQUERO_FILE the sunspot analysis is not re-run (its stored result is checked by hash).
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
PY="${PYTHON:-python3}"
FULL=0; if [ "${1:-}" = "--full" ]; then FULL=1; fi
export SOURCE_DATE_EPOCH=0 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
"$PY" -I pipeline_v2/fetch_egeland_table4.py       # Table 4 of Egeland et al. is downloaded, not redistributed (needs network; or: --from FILE)
"$PY" -I verify_reproduction.py --manifest        # the folder is exactly the published one
if [ -n "${VAQUERO_FILE:-}" ]; then "$PY" -I pipeline_v2/fetch_vaquero.py --from "$VAQUERO_FILE"; fi   # sunspot group numbers, not redistributed
"$PY" -I verify_reproduction.py --snapshot        # keep the published outputs in _published/ and clear them
cd pipeline_v2
for t in 1 2 3 4 6 7; do echo "test_step$t: $("$PY" -I test_step$t.py | tail -1)"; done
echo "test_step5 (size of the surrogate test, ~2 min): $("$PY" -I test_step5.py | tail -1)"
"$PY" -I power_simulation.py > /dev/null
"$PY" -I run_all.py                                # the single stellar run, fixed seeds (~1 min)
"$PY" -I group_primary.py > /dev/null
"$PY" -I report.py
"$PY" -I robustness.py > /dev/null
"$PY" -I compare_runs.py > /dev/null
"$PY" -I power_cycle.py > /dev/null          # surrogate test with a cycle (~3 min)
"$PY" -I power_grid.py > /dev/null           # grid over cycle period and amplitude (~4 min)
"$PY" -I positive_control.py > /dev/null     # noisy Hopf oscillator losing its cycle (~4 min)
"$PY" -I h1_bootstrap.py > /dev/null         # bootstrap over observing seasons for H1 (seconds)
"$PY" -I scale_sensitivity.py > /dev/null            # does the ARMA order depend on the scale of the series? (~1 min)
# --- calibration analyses (positive controls, power, instrumental step, data choices, sunspot numbers)
HAVE_VAQ=0; if [ -f ../data/Vaquero2016_GNobservations_JV_V1-12.csv ]; then HAVE_VAQ=1; fi
Q="--quick"; if [ "$FULL" = 1 ]; then
  Q=""
  rm -f results_calibration/{robustness_data,power_bilateral,positive_control_full,power_design,step_injection}.{csv,txt} results_calibration/robustness_post.txt
  if [ "$HAVE_VAQ" = 1 ]; then rm -f results_calibration/dalton_*; fi
fi
for s in robustness_data power_bilateral positive_control_full power_design step_injection; do "$PY" -I calibration/$s.py $Q > /dev/null; done
"$PY" -I calibration/robustness_post.py $Q > /dev/null
if [ "$HAVE_VAQ" = 1 ]; then "$PY" -I calibration/dalton_control.py $Q > /dev/null; else echo "sunspot analysis not re-run (no Vaquero file); stored result checked by hash"; fi
"$PY" -I calibration/f_sensitivity.py > /dev/null
"$PY" -I calibration/qq_pvalues.py > /dev/null
"$PY" -I calibration/example_series.py > /dev/null
if [ "$FULL" = 1 ]; then "$PY" -I verify_calibration.py --manifest; else "$PY" -I verify_calibration.py --manifest --quick; fi
"$PY" -I make_macros.py
"$PY" -I make_tables.py
"$PY" -I make_figures.py
"$PY" -I make_macros_calibration.py
"$PY" -I make_tables_calibration.py
"$PY" -I make_figures_calibration.py
"$PY" -I check_manuscript_constants.py | tail -1   # design constants written in main.tex vs the code
cd ..
"$PY" -I verify_reproduction.py --compare
if command -v pdflatex >/dev/null; then
  cd manuscrito && pdflatex -interaction=nonstopmode main.tex >/dev/null && bibtex main >/dev/null || true
  pdflatex -interaction=nonstopmode main.tex >/dev/null; pdflatex -interaction=nonstopmode main.tex | tail -2
fi
