"""Figures 1-3 of the manuscript, in colour (D111), from pipeline_v2/results and the pipeline modules.
Palette: first three slots of the reference palette of the dataviz skill (blue, orange, aqua), validated with its
validate_palette.js for all pairs, light surface (PASS; contrast WARN for orange and aqua -> every series also has its own
marker or line style and a legend). Colour roles are fixed across figures: blue = original series (no removal),
orange = sigma = 1 year residual/smooth, aqua = account B, neutral gray = reference/raw. Ticks inward on 4 sides, no grid.
Usage: python -I make_figures.py"""
import os, sys, json
import numpy as np, pandas as pd
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import p4io, annual, indicators as ind, detrend as dt
R = os.path.join(HERE, "results"); OUT = os.path.join(os.path.dirname(HERE), "manuscrito", "figures")
BLUE, ORANGE, AQUA, INK, GRAY, LIGHT = "#257de0", "#f47230", "#00b894", "#191919", "#666666", "#c8c8c8"
# Super Mongo style (kit/docs/ESTILO_FIGURAS.md): Courier Prime only (OFL, files in pipeline_v2/fonts), ticks inward on
# 4 sides, no grid, no mathtext (no Greek letters: write sigma, tau in words), colour from the validated palette above.
for fn in ("CourierPrime-Regular.ttf", "CourierPrime-Bold.ttf", "CourierPrime-Italic.ttf"):
    fm.fontManager.addfont(os.path.join(HERE, "fonts", fn))
FONT = "Courier Prime"
assert FONT in {f.name for f in fm.fontManager.ttflist}, "Courier Prime not found"
mpl.rcParams.update({
    "font.family": "monospace", "font.monospace": [FONT], "font.size": 12, "axes.labelsize": 12, "axes.titlesize": 12,
    "xtick.labelsize": 11, "ytick.labelsize": 11, "legend.fontsize": 10.5, "text.usetex": False,
    "text.color": INK, "axes.labelcolor": INK, "axes.edgecolor": INK, "xtick.color": INK, "ytick.color": INK,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "xtick.direction": "in", "ytick.direction": "in", "xtick.top": True, "ytick.right": True,
    "xtick.major.size": 6, "xtick.minor.size": 3, "ytick.major.size": 6, "ytick.minor.size": 3,
    "xtick.major.width": 0.8, "ytick.major.width": 0.8, "axes.grid": False,
    "lines.linewidth": 1.2, "lines.markersize": 5, "figure.dpi": 150, "savefig.dpi": 300, "savefig.bbox": "tight",
    "pdf.fonttype": 42, "ps.fonttype": 42})
res = pd.read_csv(os.path.join(R, "star_results.csv"), dtype={"HD": str})
h1 = json.load(open(os.path.join(R, "h1.json")))["states"]
cat = p4io.load_catalog()


def save(fig, name):
    for ext in ("pdf", "eps"):
        fig.savefig(os.path.join(OUT, f"{name}.{ext}"))
    plt.close(fig)


# ---- Figure 1: sigma_S per state (H1) ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4.6, 3.8))
keys = ("min1", "min2", "grand")
x = np.arange(3)
ax.plot(x - 0.12, [h1[k]["sigma_raw"] for k in keys], "s", mfc="white", mec=GRAY, mew=1.3, label="raw interval sigma")
ax.plot(x, [h1[k]["sigma_A"] for k in keys], "o", mfc=BLUE, mec=BLUE, label="corrected, account A")
ax.plot(x + 0.12, [h1[k]["sigma_B"] for k in keys], "^", mfc=AQUA, mec=AQUA, label="corrected, account B")
ax.set_xticks(x); ax.set_xticklabels([f"min 1\n1971-75\nN={h1['min1']['n']}", f"min 2\n1987-91\nN={h1['min2']['n']}",
                                        f"grand min\n2004-\nN={h1['grand']['n']}"])
ax.set_xlim(-0.5, 2.5); ax.set_ylim(0, 0.0072); ax.set_ylabel("sigma of S (HD 166620)")
ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=1)
save(fig, "figure1")

# ---- Figure 2: annual series and rolling AR(1): HD 166620 and the Sun ---------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(7.0, 4.6))
for col, hd in enumerate(("166620", "(Sun)")):
    row = cat[cat.HD == hd].iloc[0]
    obs = p4io.load_star(hd, row)
    sun = hd == "(Sun)"
    a = annual.annual_means(obs, None if sun else "MW")
    sg = max(annual.segments(a), key=lambda s: len(s["years"]))
    yrs, S, filled = sg["years"], sg["S"], sg["filled"]
    ax = axs[0, col]
    ax.plot(yrs, S, "-", color=INK, lw=0.9)
    ax.plot(yrs[filled], S[filled], "o", mfc="white", mec=INK, ms=4.5, mew=1.2)
    ax.plot(yrs, S - dt.residual(S, 1), "--", color=ORANGE, lw=1.3)
    ax.set_ylabel("annual mean S"); ax.set_xlabel("year")
    ax.set_title("Sun (Egeland 2017)" if sun else "HD 166620 (Mount Wilson)", fontsize=9)
    ax = axs[1, col]
    for cfg, ls, cl in ((None, "-", BLUE), (1, "--", ORANGE)):
        r = dt.residual(S, cfg); w = ind.window_size(len(S), 0.5)
        roll = ind.rolling(r, 0.5)
        ax.plot(yrs[w - 1:], roll, ls, color=cl, lw=1.5)
    ax.axhline(0, color=GRAY, lw=0.6); ax.set_ylabel("rolling lag-1 AC (window 50 %)"); ax.set_xlabel("year at window end")
    ax.set_ylim(-1.4, 1)
axs[0, 0].plot([], [], "-", color=INK, label="annual mean"); axs[0, 0].plot([], [], "--", color=ORANGE, lw=1.3, label="Gaussian smooth, sigma = 1 yr")
axs[0, 0].plot([], [], "o", mfc="white", mec=INK, label="interpolated year")
axs[0, 0].legend(frameon=False, loc="upper right", fontsize=7)
axs[1, 0].plot([], [], "-", color=BLUE, lw=1.5, label="no removal"); axs[1, 0].plot([], [], "--", color=ORANGE, lw=1.5, label="residual, sigma = 1 yr")
axs[1, 0].legend(frameon=False, loc="lower left", fontsize=7)
axs[0, 0].set_ylim(0.165, 0.262)
from matplotlib.ticker import MaxNLocator
for a_ in axs.ravel():
    a_.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
fig.tight_layout()
save(fig, "figure2")

# ---- Figure 3: tau per star, AR(1), window 50 % ---------------------------------------------------------------
d = res[(res.series == "S") & (res.frac == 0.5) & (res["stat"] == "ac1") & (res.config.isin(["none", "s1"]))]
order = ["Flat_limpa", "CYCLE_Excellent", "Var", "Long"]
lab = {"Flat_limpa": "Flat", "CYCLE_Excellent": "Cycle", "Var": "Var", "Long": "Long"}
stars = []
for g in order:
    hds = sorted(d[(d.grupo == g) & (d.HD != "(Sun)")].HD.unique(), key=lambda h: int("".join(c for c in h if c.isdigit())))
    stars += [(g, h) for h in hds]
stars.append(("Sun", "(Sun)"))
fig, ax = plt.subplots(figsize=(7.0, 3.2))
for i, (g, h) in enumerate(stars):
    for cfg, mk, mf in (("none", "o", BLUE), ("s1", "D", ORANGE)):
        r = d[(d.HD == h) & (d.config == cfg)].iloc[0]
        ax.plot(i, r.tau, mk, mfc=mf, mec=mf, ms=5 if mk == "o" else 4.5)
        if r.p_upper < 0.05:
            ax.text(i, r.tau + 0.07, "*", ha="center", fontsize=12, color=INK)
ax.axhline(0, color=GRAY, lw=0.6)
gs = [g for g, _ in stars]
for i in range(1, len(stars)):
    if gs[i] != gs[i - 1]:
        ax.axvline(i - 0.5, color=LIGHT, lw=0.8, ls=":")
ax.set_xticks(range(len(stars))); ax.set_xticklabels([h for _, h in stars], rotation=90)
for g in order + ["Sun"]:
    idx = [i for i, x in enumerate(gs) if x == g]
    ax.text(np.mean(idx), 1.12, lab.get(g, g), ha="center", va="bottom")
ax.set_ylim(-1.05, 1.05); ax.set_xlim(-0.7, len(stars) - 0.3); ax.set_ylabel("Kendall tau of rolling lag-1 AC")
ax.plot([], [], "o", color=BLUE, ls="", label="no removal"); ax.plot([], [], "D", color=ORANGE, ls="", ms=4.5, label="sigma = 1 yr residual")
ax.plot([], [], "*", color=INK, ms=8, ls="", label="p < 0.05 (surrogates)")
ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.28), ncol=3, fontsize=7)
save(fig, "figure3")
open(os.path.join(OUT, "README.txt"), "w").write(f"Figures from pipeline_v2/make_figures.py. Font used: {FONT} (OFL; files and licence in pipeline_v2/fonts).\n"
                                                    "Super Mongo style, colour (D111). No figure number or caption inside the files. EPS and PDF.\n")
print("figures written; font", FONT)
