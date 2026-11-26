"""Three checks that need no new stellar run (D121), from results/ and the input series. Output: results/robustness.txt (key: value lines).
(1) Coverage: observations per calendar year in each analyzed star segment (the Sun is left out: its annual means are composite values).
(2) Interpolation: how many of the cells flagged at a window of 50 % lie in segments with more than two interpolated years.
(3) Lag-1 autocorrelation expected for white noise after the Gaussian high-pass of width sigma (residual = series minus smooth), computed
    exactly from the filter kernel: what the residual would show with no structure at all.
Usage: python -I robustness.py"""
import os, sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scipy.ndimage import gaussian_filter1d
import p4io, annual, run_all

HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, "results")
out = []
# (1) coverage
mins, meds, lowseg, nseg = [], [], 0, 0
for _, r in p4io.load_catalog().iterrows():
    if r.serie_fonte == "Egeland2017_T4" or r.indicador_elegivel_D100 != "sim":
        continue
    ann = annual.annual_means(p4io.load_star(r.HD, r), "MW").set_index("year")
    for seg in annual.segments(ann.reset_index()):
        if len(seg["years"]) < run_all.MIN_SEG:
            continue
        n = ann.loc[[y for y, f in zip(seg["years"], seg["filled"]) if not f], "n"]
        mins.append(int(n.min())); meds.append(float(n.median())); nseg += 1; lowseg += int((n < 5).any())
out += [f"coverage_segments: {nseg}", f"coverage_min_obs_per_year: {min(mins)}", f"coverage_median_of_medians: {np.median(meds):.0f}",
        f"coverage_segments_with_a_year_below_5: {lowseg}"]
# (2) interpolation
res = pd.read_csv(os.path.join(R, "star_results.csv"), dtype={"HD": str}); seg = pd.read_csv(os.path.join(R, "segments.csv"), dtype={"HD": str})
m5 = res[(res.series == "S") & (res.frac == 0.5)].merge(seg[["HD", "seg_year0", "n_filled"]], on=["HD", "seg_year0"])
m5 = m5.assign(flag=(m5.tau > 0) & (m5.p_upper < 0.05))
out += [f"interp_segments_over_2: {m5[m5.n_filled > 2].drop_duplicates(['HD', 'seg_year0']).shape[0]}",
        f"interp_cells_flagged_all: {int(m5.flag.sum())}", f"interp_cells_flagged_in_segments_up_to_2: {int(m5[m5.n_filled <= 2].flag.sum())}",
        f"interp_cells_in_segments_up_to_2: {len(m5[m5.n_filled <= 2])}"]
# (3) white noise through the high-pass
for s in (1, 3, 5):
    imp = np.zeros(1201); imp[600] = 1.0
    h = imp - gaussian_filter1d(imp, s, truncate=8.0)
    out.append(f"whitenoise_ac1_sigma{s}: {np.sum(h[:-1] * h[1:]) / np.sum(h * h):.3f}")
# (4) cycle amplitude in a homogeneous source (CLS V, Isaacson et al. 2024, Table 4) for the analyzed stars
rows_ = [l.rstrip("\n").split(";") for l in open(os.path.join(os.path.dirname(HERE), "data", "J_ApJS_274_35_table4.tsv"), encoding="utf-8") if l.strip() and not l.startswith("#")]
amp = {r_[0].replace("HD", "").strip() for r_ in rows_[3:]}
stars = set(seg[(seg.rodou == "sim") & (seg.HD != "(Sun)")].HD)
out.append(f"amplitude_stars_with_CLSV_cycle_amplitude: {len(stars & amp)}"); out.append(f"amplitude_stars_analyzed: {len(stars)}")
open(os.path.join(R, "robustness.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
