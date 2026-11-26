"""Block bootstrap by observing season for the variability of HD 166620 by state (H1; D122). The observations inside a season are strongly
correlated, so whole seasons (calendar years) are resampled with replacement within each state, and sigma (raw and method A) is recomputed;
the instrumental noise fraction of each state is the one of state_comparison.STATES. 4000 resamples, seed 8080.
Output: results/h1_bootstrap.txt (key: value lines) and results/h1_bootstrap.csv (state, method, estimate, low, high).
Usage: python -I h1_bootstrap.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
import state_comparison as sc

HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, "results")
NB, rng = 4000, np.random.default_rng(8080)
d = sc.load_luhn()
seasons = {}
for k, (a, b, noise) in sc.STATES.items():
    g = d[(d.y >= a) & (d.y < b)]
    seasons[k] = [grp.s.values for _, grp in g.groupby("yr")]


def sig(vals, noise):
    x = np.concatenate(vals); m, s1 = x.mean(), x.std(ddof=1)
    return s1, np.sqrt(max(s1 ** 2 - (noise * m) ** 2, 0.0))


boot = {k: [] for k in seasons}
for k, (a, b, noise) in sc.STATES.items():
    blocks = seasons[k]
    for _ in range(NB):
        pick = rng.integers(0, len(blocks), len(blocks))
        boot[k].append(sig([blocks[i] for i in pick], noise))
    boot[k] = np.array(boot[k])
rows, out = [], []
for k, (a, b, noise) in sc.STATES.items():
    est = sig(seasons[k], noise)
    for j, meth in enumerate(("raw", "A")):
        lo, hi = np.percentile(boot[k][:, j], [2.5, 97.5])
        rows.append((k, meth, est[j], lo, hi))
    out.append(f"seasons_{k}: {len(seasons[k])}")
for meth, j in (("raw", 0), ("A", 1)):
    for s in ("min1", "min2"):
        ratio = boot[s][:, j] / boot["grand"][:, j]
        out.append(f"boot_share_sigma_{s}_not_above_grand_{meth}: {100 * np.mean(ratio <= 1):.1f}")
        out.append(f"boot_ratio_{s}_over_grand_{meth}_low_high: {np.percentile(ratio, 2.5):.1f} {np.percentile(ratio, 97.5):.1f}")
pd.DataFrame(rows, columns=["state", "method", "estimate", "low", "high"]).to_csv(os.path.join(R, "h1_bootstrap.csv"), index=False, float_format="%.6g")
open(os.path.join(R, "h1_bootstrap.txt"), "w").write("\n".join(out) + "\n")
print("\n".join(out)); print(pd.DataFrame(rows, columns=["state", "method", "estimate", "low", "high"]).round(4).to_string())
