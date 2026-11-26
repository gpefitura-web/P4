"""Figure style shared by the calibration figures: same as make_figures.py (Courier Prime, inward ticks on four sides, no grid, validated
palette, drawn at the printed text width). Import for its side effects (rcParams) and the constants."""
import os
os.environ.setdefault("SOURCE_DATE_EPOCH", "0")   # deterministic PDF/EPS metadata
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

HERE = os.path.dirname(os.path.abspath(__file__))
BLUE, ORANGE, AQUA, INK, GRAY, LIGHT = "#257de0", "#f47230", "#00b894", "#191919", "#666666", "#c8c8c8"
TW = 390.0 / 72.27
for fn in ("CourierPrime-Regular.ttf", "CourierPrime-Bold.ttf", "CourierPrime-Italic.ttf"):
    fm.fontManager.addfont(os.path.join(HERE, "fonts", fn))
FONT = "Courier Prime"
assert FONT in {f.name for f in fm.fontManager.ttflist}, "Courier Prime not found"
mpl.rcParams.update({
    "font.family": "monospace", "font.monospace": [FONT], "font.size": 11, "axes.labelsize": 11, "axes.titlesize": 11,
    "xtick.labelsize": 10, "ytick.labelsize": 10, "legend.fontsize": 9.5, "text.usetex": False,
    "text.color": INK, "axes.labelcolor": INK, "axes.edgecolor": INK, "xtick.color": INK, "ytick.color": INK,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "xtick.direction": "in", "ytick.direction": "in", "xtick.top": True, "ytick.right": True,
    "xtick.major.size": 5, "xtick.minor.size": 2.5, "ytick.major.size": 5, "ytick.minor.size": 2.5,
    "xtick.major.width": 0.8, "ytick.major.width": 0.8, "axes.grid": False,
    "lines.linewidth": 1.2, "lines.markersize": 4.5, "figure.dpi": 150, "savefig.dpi": 300, "savefig.bbox": "tight",
    "pdf.fonttype": 42, "ps.fonttype": 42})
