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
# Colour roles of figures 2-3 (blue = original series, orange = sigma 1 yr treatment) are NOT reused here:
# raw = hollow gray square, account A = ink circle, account B = aqua triangle (aqua only appears in this figure).
AQUA_EDGE = "#007a63"
fig, ax = plt.subplots(figsize=(4.6, 3.5))
keys = ("min1", "min2", "grand")
x = np.arange(3)
ax.plot(x - 0.15, [h1[k]["sigma_raw"] for k in keys], "s", ms=7, mfc="white", mec=GRAY, mew=1.4, ls="", label="raw interval")
ax.plot(x, [h1[k]["sigma_A"] for k in keys], "o", ms=7, mfc=INK, mec=INK, ls="", label="corrected, A")
ax.plot(x + 0.15, [h1[k]["sigma_B"] for k in keys], "^", ms=8, mfc=AQUA, mec=AQUA_EDGE, mew=1.0, ls="", label="corrected, B")
ax.set_xticks(x); ax.set_xticklabels([f"min 1\n1971-75\nN={h1['min1']['n']}", f"min 2\n1987-91\nN={h1['min2']['n']}",
                                        f"grand min\n2004 on\nN={h1['grand']['n']}"])
ax.set_xlim(-0.5, 2.5); ax.set_ylim(0, 0.0085); ax.set_ylabel("sigma of S")
ax.legend(frameon=False, loc="upper right", fontsize=10)
save(fig, "Figure_1")

# ---- Figures 2 and 3: annual series and rolling AR(1), one file per series (HD 166620; the Sun) -------------------
from matplotlib.ticker import MultipleLocator
from matplotlib.lines import Line2D
for hd, fname, title, ytick, xtick in (("166620", "Figure_2", "HD 166620 (Mount Wilson)", 0.02, 5),
                                       ("(Sun)", "Figure_3", "Sun (Egeland 2017)", 0.005, 10)):
    row = cat[cat.HD == hd].iloc[0]
    sun = hd == "(Sun)"
    a_ = annual.annual_means(p4io.load_star(hd, row), None if sun else "MW")
    sg = max(annual.segments(a_), key=lambda s_: len(s_["years"]))
    yrs, S, filled = sg["years"], sg["S"], sg["filled"]
    fig, axs = plt.subplots(2, 1, figsize=(5.2, 5.4))
    ax = axs[0]
    ax.plot(yrs, S, "-", color=BLUE, lw=1.4, zorder=2)
    ax.plot(yrs, S - dt.residual(S, 1), "--", color=ORANGE, lw=2.0, dashes=(4, 2), zorder=3)
    if filled.any():
        ax.plot(yrs[filled], S[filled], "o", mfc="white", mec=INK, ms=5, mew=1.2, ls="", zorder=4)
    ax.set_ylabel("annual mean S"); ax.set_xlabel("year")
    ax.yaxis.set_major_locator(MultipleLocator(ytick))
    if not sun:
        ax.set_ylim(0.165, 0.235)
    ax = axs[1]
    w = ind.window_size(len(S), 0.5)
    for cfg, ls, cl, dsh in ((None, "-", BLUE, None), (1, "--", ORANGE, (4, 2))):
        roll = ind.rolling(dt.residual(S, cfg), 0.5)
        kw = {"dashes": dsh} if dsh else {}
        ax.plot(yrs[w - 1:], roll, ls, color=cl, lw=2.0, **kw)
    ax.axhline(0, color=GRAY, lw=0.6); ax.set_xlabel("year at window end"); ax.set_ylabel("lag-1 AC"); ax.set_ylim(-1.05, 1.05); ax.yaxis.set_major_locator(MultipleLocator(0.5))
    for ax_ in axs:
        ax_.xaxis.set_major_locator(MultipleLocator(xtick))
    fig.align_ylabels(axs)
    handles = [Line2D([], [], color=BLUE, lw=2.0, label="original series"),
               Line2D([], [], color=ORANGE, lw=2.0, dashes=(4, 2), label="sigma = 1 yr: smooth (top), residual (bottom)")]
    if filled.any():
        handles.append(Line2D([], [], color=INK, marker="o", mfc="white", ls="", ms=5, label="interpolated year"))
    axs[0].set_title(title, fontsize=12)
    fig.tight_layout(rect=(0, 0.14 if sun else 0.11, 1, 1))
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, 0.0), ncol=1, frameon=False, fontsize=9.5, handlelength=2.2)
    save(fig, fname)

# ---- Figure 4: tau per star, AR(1), window 50 % ---------------------------------------------------------------
d = res[(res.series == "S") & (res.frac == 0.5) & (res["stat"] == "ac1") & (res.config.isin(["none", "s1"]))]
order = ["Flat_limpa", "CYCLE_Excellent", "Var", "Long"]
lab = {"Flat_limpa": "Flat", "CYCLE_Excellent": "Cycle", "Var": "Var", "Long": "Long"}
stars = []
for g in order:
    hds = sorted(d[(d.grupo == g) & (d.HD != "(Sun)")].HD.unique(), key=lambda h: int("".join(c for c in h if c.isdigit())))
    stars += [(g, h) for h in hds]
stars.append(("Sun", "(Sun)"))
STAR = (6, 2, 0)    # asterisk marker, same glyph in plot and legend
fig, ax = plt.subplots(figsize=(7.2, 3.6))
for i, (g, h) in enumerate(stars):
    for cfg, mk, mc, dx, ms in (("none", "o", BLUE, -0.17, 6), ("s1", "D", ORANGE, 0.17, 5.5)):
        r = d[(d.HD == h) & (d.config == cfg)].iloc[0]
        ax.plot(i + dx, r.tau, mk, mfc=mc, mec=mc, ms=ms, ls="")
        if r.p_upper < 0.05:
            ax.plot(i + dx, r.tau + 0.12, marker=STAR, color=INK, ms=9, mew=1.3, ls="")
ax.axhline(0, color=GRAY, lw=0.6)
gs = [g for g, _ in stars]
for i in range(1, len(stars)):
    if gs[i] != gs[i - 1]:
        ax.axvline(i - 0.5, color="#9a9a9a", lw=1.0, ls=(0, (1, 2)))
ax.set_xticks(range(len(stars))); ax.set_xticklabels([h.strip("()") for _, h in stars], rotation=90)
for g in order:
    idx = [i for i, x in enumerate(gs) if x == g]
    ax.text(np.mean(idx), 1.02, lab[g], ha="center", va="bottom", transform=ax.get_xaxis_transform())
ax.set_ylim(-1.05, 1.05); ax.set_xlim(-0.7, len(stars) - 0.3); ax.set_ylabel("Kendall tau")
handles = [Line2D([], [], marker="o", color=BLUE, ls="", ms=6, label="original series"),
           Line2D([], [], marker="D", color=ORANGE, ls="", ms=5.5, label="sigma = 1 yr residual"),
           Line2D([], [], marker=STAR, color=INK, ls="", ms=9, mew=1.3, label="p < 0.05")]
ax.legend(handles=handles, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.30), ncol=3, fontsize=10.5)
save(fig, "Figure_4")
open(os.path.join(OUT, "README.txt"), "w").write(f"Figures from pipeline_v2/make_figures.py. Font used: {FONT} (OFL; files and licence in pipeline_v2/fonts).\n"
                                                    "Super Mongo style, colour (D111). No figure number or caption inside the files. EPS and PDF.\n")
print("figures written; font", FONT)
