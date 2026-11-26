"""Calibration figures (D126) from pipeline_v2/results_calibration, in the style of make_figures.py. No Greek letters or mathtext in labels.
Output: manuscrito/figures/cal_*.pdf and .eps.   Usage: python -I make_figures_calibration.py [--preview DIR]  (PNG previews, not for the package)"""
import os, sys, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np, pandas as pd
from figstyle import *
import matplotlib as mpl
import matplotlib.ticker
import state_comparison as sc

R = os.path.join(HERE, "results_calibration"); RES = os.path.join(HERE, "results")
OUT = os.path.join(os.path.dirname(HERE), "manuscrito", "figures")
PREV = sys.argv[sys.argv.index("--preview") + 1] if "--preview" in sys.argv else None
def save(fig, name):
    for ext in ("pdf", "eps"): fig.savefig(os.path.join(OUT, f"{name}.{ext}"))
    if PREV: fig.savefig(os.path.join(PREV, f"{name}.png"), dpi=110)
    plt.close(fig)
def lab(ax, t): ax.text(0.02, 0.96, t, transform=ax.transAxes, va="top", ha="left", fontweight="bold")
def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    return (pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()

# ---- Fig. 1: example series and rolling indicators of the three positive controls ----
ex = pd.read_csv(os.path.join(R, "example_series.csv"))
names = {"super": "supercritical", "sub": "subcritical", "mult": "multiplicative noise"}
fig, axs = plt.subplots(3, 3, figsize=(TW, 6.6), sharex=True)
for i, m in enumerate(("super", "sub", "mult")):
    for lost, col, ls in ((False, GRAY, "-"), (True, BLUE, "-")):
        g = ex[(ex.model == m) & (ex.lost == lost)]
        axs[i, 0].plot(g.year, g.S, ls, color=col, label="cycle lost" if lost else "cycle persists")
        axs[i, 1].plot(g.year, g.ac1, ls, color=col); axs[i, 2].plot(g.year, g["var"], ls, color=col)
    axs[i, 0].set_ylabel(names[m] + "\nannual mean")
h_, l_ = axs[0, 0].get_legend_handles_labels(); fig.legend(h_, l_, frameon=False, loc="lower center", ncol=2); axs[0, 1].set_title("lag-1 autocorrelation"); axs[0, 2].set_title("variance"); axs[0, 0].set_title("series")
for ax in axs[2]: ax.set_xlabel("year")
fig.tight_layout(rect=(0, 0.04, 1, 1)); save(fig, "cal_fig1_controls")

# ---- Fig. 2: AUC and lower-tail rejection of the positive control, by period and dynamical noise ----
bi = pd.read_csv(os.path.join(R, "power_bilateral.csv"))
fig, axs = plt.subplots(2, 2, figsize=(TW, 5.4), sharex=True)
cols = {8.0: BLUE, 11.0: ORANGE, 15.0: AQUA}; mk = {8.0: "o", 11.0: "s", 15.0: "^"}
for j, (s, nmx) in enumerate((("ac1", "lag-1 autocorrelation"), ("var", "variance"))):
    for P in (8.0, 11.0, 15.0):
        xs, au, rj = [], [], []
        for s0 in (0.10, 0.15, 0.30):
            a = bi[(bi.case == "hopf_lost") & (bi.P == P) & (bi.s0 == s0)]; b = bi[(bi.case == "hopf_persist") & (bi.P == P) & (bi.s0 == s0)]
            xs.append(s0); au.append(auc(-a[f"plow_{s}"], -b[f"plow_{s}"])); rj.append(100 * (a[f"plow_{s}"] < .05).mean())
        axs[0, j].plot(xs, au, "-" + mk[P], color=cols[P], label=f"period {P:g} yr"); axs[1, j].plot(xs, rj, "-" + mk[P], color=cols[P])
    axs[0, j].set_title(nmx); axs[0, j].axhline(0.5, color=LIGHT, lw=0.8); axs[0, j].set_ylim(0.45, 1.02); axs[1, j].axhline(5, color=LIGHT, lw=0.8); axs[1, j].set_ylim(0, 65)
    axs[1, j].set_xlabel("dynamical noise"); axs[1, j].set_xticks([0.10, 0.15, 0.30])
axs[0, 0].set_ylabel("AUC, lost vs persists"); axs[1, 0].set_ylabel("rejection, lower tail (%)"); axs[0, 0].legend(frameon=False, loc="lower left")
fig.tight_layout(); save(fig, "cal_fig2_power_grid")

# ---- Fig. 3: design power curve for true CSD ----
de = pd.read_csv(os.path.join(R, "power_design.csv"))
fig, axs = plt.subplots(1, 2, figsize=(TW, 3.5), sharey=True)
nc = {0.0: BLUE, 0.5: ORANGE, 1.0: AQUA}
for j, cyc in enumerate((False, True)):
    for r in (0.0, 0.5, 1.0):
        for s, ls in (("ac1", "-"), ("var", "--")):
            pw = [100 * (de[(de.L == L) & (de.r == r) & (de.cyc == cyc) & de.trend][f"pup_{s}"] < .05).mean() for L in (30, 50, 100, 200)]
            axs[j].plot((30, 50, 100, 200), pw, ls + "o", color=nc[r], label=f"{'autocorr.' if s == 'ac1' else 'variance'}, noise {r:g}")
    axs[j].axhline(5, color=LIGHT, lw=0.8); axs[j].set_title("with an 11-yr cycle" if cyc else "no cycle"); axs[j].set_xlabel("record length (yr)"); axs[j].set_xscale("log"); axs[j].xaxis.set_minor_locator(mpl.ticker.NullLocator()); axs[j].set_xticks([30, 50, 100, 200]); axs[j].set_xticklabels(["30", "50", "100", "200"])
axs[0].set_ylabel("power for true CSD (%)"); axs[0].legend(frameon=False, ncol=1, fontsize=8, loc="upper left")
fig.tight_layout(); save(fig, "cal_fig3_design")

# ---- Fig. 4: QQ of the 192 stellar p values ----
q = pd.read_csv(os.path.join(R, "qq_pvalues.csv"))
fig, axs = plt.subplots(1, 2, figsize=(TW, 3.5), sharey=True)
for ax, tail, t in zip(axs, ("upper", "lower"), ("upper tail (CSD direction)", "lower tail")):
    g = q[q["tail"] == tail]; ax.plot([0, 1], [0, 1], "-", color=LIGHT, lw=1); ax.plot(g.p_unif, g.p_obs, "o", color=BLUE, ms=3)
    ax.set_title(t); ax.set_xlabel("uniform quantile"); ax.set_aspect("equal"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
axs[0].set_ylabel("observed p value (192 cells)")
fig.tight_layout(); save(fig, "cal_fig4_qq")

# ---- Fig. 5: sigma_S ratios of HD 166620 against the noise fraction f ----
d = sc.load_luhn()
def sig(name, f):
    a, b, _ = sc.STATES[name]; g = d[(d.y >= a) & (d.y < b)]; v = g.s.var(ddof=1) - (f * g.s.mean()) ** 2
    return math.sqrt(v) if v > 0 else float("nan")
sg_ = sig("grand", sc.STATES["grand"][2]); fs = np.arange(0.008, 0.0194, 0.0002)
fig, ax = plt.subplots(figsize=(TW, 3.6))
ax.plot(100 * fs, [sig("min1", f) / sg_ for f in fs], "-", color=ORANGE, label="minimum 1 / grand minimum")
ax.plot(100 * fs, [sig("min2", f) / sg_ for f in fs], "-", color=BLUE, label="minimum 2 / grand minimum")
ax.axhline(1, color=GRAY, lw=0.8); ax.axvline(1.2, color=LIGHT, lw=1); ax.axvline(1.7, color=LIGHT, lw=1, ls="--")
ax.text(1.21, 3.15, "1.2 %", color=GRAY, fontsize=9); ax.text(1.71, 3.15, "1.7 %", color=GRAY, fontsize=9)
ax.set_xlabel("instrumental noise fraction of the Mount Wilson states (% of mean S)"); ax.set_ylabel("ratio of corrected sigma_S"); ax.set_ylim(0, 3.3); ax.legend(frameon=False, loc="lower left")
fig.tight_layout(); save(fig, "cal_fig5_sigma_f")

# ---- Fig. 6: instrumental step ----
st = pd.read_csv(os.path.join(R, "step_injection.csv"))
cases = ["none", "level 0.5sd", "level 1sd", "level 2sd", "noise x0.5", "noise x1.5", "level 1sd + noise x0.5"]
lbl = ["none", "level 0.5 sd", "level 1 sd", "level 2 sd", "noise x0.5", "noise x1.5", "level 1 sd\n+ noise x0.5"]
fig, ax = plt.subplots(figsize=(TW, 3.8)); y = np.arange(len(cases))[::-1]
for s, col, mkr, dy in (("ac1", BLUE, "o", 0.12), ("var", ORANGE, "s", -0.12)):
    ax.plot([st[st.case == c][f"tau_{s}"].median() for c in cases], y + dy, mkr, color=col, label="autocorrelation" if s == "ac1" else "variance")
ax.axvline(0, color=GRAY, lw=0.8); ax.set_yticks(y); ax.set_yticklabels(lbl); ax.set_xlabel("median Kendall tau of the rolling indicator"); ax.legend(frameon=False, loc="lower right")
fig.tight_layout(); save(fig, "cal_fig6_step")

# ---- Fig. 7: Dalton Minimum, sunspot group numbers ----
an = pd.read_csv(os.path.join(R, "dalton_annual.csv")).set_index("year").rename(columns={"S": "mean", "n": "size"}); an = an[(an.index >= 1740) & (an.index <= 1900)]
dc = pd.read_csv(os.path.join(R, "dalton_control.csv"))
fig, (a1, a2) = plt.subplots(2, 1, figsize=(TW, 5.4), gridspec_kw=dict(height_ratios=[1.2, 1]))
ok = an["size"] >= 50
yy = an["mean"].where(ok).reindex(range(1740, 1901)); a1.plot(yy.index, yy.values, "-", color=BLUE, lw=1.2); a1.plot(an.index[~ok], an["mean"][~ok], "o", color=LIGHT, ms=3, label="fewer than 50 days")
a1.axvspan(1795, 1830, color="#e6e6e6", lw=0, zorder=0); a1.set_ylabel("annual mean of group number"); a1.set_xlabel("year"); a1.legend(frameon=False, loc="upper left")
blocks = sorted(dc.block.unique()); xs = np.arange(len(blocks))
for s, col, mkr, dx in (("ac1", BLUE, "o", -0.1), ("var", ORANGE, "s", 0.1)):
    g = dc[(dc["transform"] == "raw") & (dc["stat"] == s)]
    for i, b in enumerate(blocks):
        t = g[g.block == b].tau; a2.plot([i + dx] * len(t), t, mkr, color=col, label=("autocorrelation" if s == "ac1" else "variance") if i == 0 else None)
a2.axhline(0, color=GRAY, lw=0.8); a2.set_xticks(xs); a2.set_xticklabels(blocks, fontsize=8); a2.set_ylabel("Kendall tau (4 configurations)"); a2.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2)
fig.tight_layout(); save(fig, "cal_fig7_dalton")
print("figures ->", OUT)
