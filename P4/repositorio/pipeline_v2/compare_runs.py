"""Compares the first stellar run (raw-scale ARMA fit, archive/star_results_run1.csv) with the current one (standardized ARMA fit, D121).
Output: results/run_comparison.txt (key: value lines).   Usage: python -I compare_runs.py"""
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
K = ["HD", "seg_year0", "series", "config", "frac", "stat"]
o = pd.read_csv(os.path.join(HERE, "archive", "star_results_run1.csv"), dtype={"HD": str}).set_index(K)
n = pd.read_csv(os.path.join(HERE, "results", "star_results.csv"), dtype={"HD": str}).set_index(K)
d = (o.p_upper - n.p_upper).abs()
S = lambda df: df[(df.index.get_level_values("series") == "S") & (df.index.get_level_values("frac") == 0.5)]
fl = lambda df: S(df)[(S(df).tau > 0) & (S(df).p_upper < 0.05)]
same_cells = sorted(set(fl(o).index) & set(fl(n).index))
out = [f"cells: {len(n)}", f"tau_max_abs_difference: {(o.tau - n.tau).abs().max():.1e}", f"p_upper_max_abs_difference: {d.max():.2f}",
       f"share_of_cells_with_p_change_over_0.05: {100 * (d > 0.05).mean():.0f}", f"arma_order_changed_share: {100 * (o.arma != n.arma).mean():.0f}",
       f"flagged_cells_run1: {len(fl(o))}", f"flagged_cells_run2: {len(fl(n))}", f"flagged_cells_in_both: {len(same_cells)}"]
open(os.path.join(HERE, "results", "run_comparison.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
