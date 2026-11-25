"""Power of the rolling lag-1 Kendall-tau indicator on synthetic AR(1) series (no cycle, no stellar values).
Null: AR(1) coefficient constant at 0.5. Trend: coefficient rising linearly from 0.3 to 0.7. Window = 50 % of the length L (at least 5 points).
600 series per length and per hypothesis, fixed seeds. Output: results/power_simulation.txt (AUC of tau for trend against null).
Usage: python -I power_simulation.py"""
import os
import numpy as np
from scipy.stats import kendalltau

HERE = os.path.dirname(os.path.abspath(__file__))
LENGTHS = (24, 30, 40)       # the lengths quoted in the manuscript; the seed depends only on L


def ac1(x):
    m = x.mean()
    return np.sum((x[:-1] - m) * (x[1:] - m)) / np.sum((x - m) ** 2)


def sim(path, rng):
    n = len(path)
    x = np.zeros(n)
    x[0] = rng.normal() / np.sqrt(1 - path[0] ** 2)
    for t in range(1, n):
        x[t] = path[t] * x[t - 1] + rng.normal()
    return x


def auc(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return float(np.mean([(x > b).mean() + 0.5 * (x == b).mean() for x in a]))


lines = ["Discrimination null (c = 0.5) vs trend (c 0.3 -> 0.7) by Kendall tau of the rolling lag-1 estimate,",
         "window = 50 % of the segment length L (min 5 points), 600 simulations per cell",
         "L | window | n windows | tau null mean | tau null SD | tau trend mean | AUC(trend > null) | share trend tau >= 0.5 | share null tau >= 0.5"]
for L in LENGTHS:
    w = max(5, int(round(L * 0.5)))
    nw = L - w + 1
    tn, tt = [], []
    rng = np.random.default_rng(1600 + L)
    for _ in range(600):
        for path, store in ((np.full(L, 0.5), tn), (np.linspace(0.3, 0.7, L), tt)):
            x = sim(path, rng)
            r = np.array([ac1(x[s:s + w]) for s in range(nw)])
            store.append(kendalltau(np.arange(nw), r)[0] if nw > 2 else np.nan)
    tn, tt = np.array(tn), np.array(tt)
    a = auc(tt[np.isfinite(tt)], tn[np.isfinite(tn)])
    lines.append(f"{L} | {w} | {nw} | {np.nanmean(tn):+.2f} | {np.nanstd(tn):.2f} | {np.nanmean(tt):+.2f} | {a:.2f} | "
                 f"{np.nanmean(tt >= 0.5):.2f} | {np.nanmean(tn >= 0.5):.2f}")
os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
with open(os.path.join(HERE, "results", "power_simulation.txt"), "w") as fh:
    fh.write("\n".join(lines) + "\n")
print("\n".join(lines))
