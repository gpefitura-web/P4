"""Verifies the calibration results (D126).
  --write-manifest : records sha256 of the full outputs in results_calibration/CALIBRATION_MANIFEST.sha256
  --manifest       : the full outputs are exactly the recorded ones
  --quick          : the reduced run (results_calibration_quick/, produced with --quick) agrees with the full run: every rejection rate
                     within 4 standard errors of the difference (binomial, both sample sizes), and the statistics that do not depend on the
                     surrogates (Kendall tau of the data in robustness_data and dalton_control) identical.
Usage: python -I verify_calibration.py --manifest --quick"""
import os, sys, hashlib
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); FULL = os.path.join(HERE, "results_calibration"); QUICK = os.path.join(HERE, "results_calibration_quick")
MAN = os.path.join(FULL, "CALIBRATION_MANIFEST.sha256")
FILES = ["positive_control_full.csv", "positive_control_full.txt", "power_bilateral.csv", "power_bilateral.txt", "power_design.csv", "power_design.txt",
         "step_injection.csv", "step_injection.txt", "robustness_data.csv", "robustness_data.txt", "robustness_post.txt", "dalton_control.csv", "dalton_control.txt",
         "qq_pvalues.csv", "qq_pvalues.txt", "f_sensitivity.txt", "example_series.csv"]
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""): h.update(ch)
    return h.hexdigest()
def rates(df, keys, cols):
    out = {}
    for k, g in df.groupby(keys):
        for name, f in cols.items(): out[(k if isinstance(k, tuple) else (k,)) + (name,)] = (f(g).mean(), len(g))
    return out
def agree(full, quick, label, fails):
    n = 0
    for k, (pf, nf) in full.items():
        if k not in quick: fails.append(f"{label}: missing {k}"); continue
        pq, nq = quick[k]; se = np.sqrt(pf * (1 - pf) / nq + pf * (1 - pf) / nf + 1.0 / (nq * nf)); n += 1
        if abs(pq - pf) > 4 * se + 1.0 / nq: fails.append(f"{label} {k}: full {pf:.3f} (n={nf}) quick {pq:.3f} (n={nq})")
    print(f"{label}: {n} rates compared")
if "--write-manifest" in sys.argv:
    open(MAN, "w").write("".join(f"{sha(os.path.join(FULL, f))}  {f}\n" for f in FILES)); print("manifest written:", len(FILES), "files")
if "--manifest" in sys.argv:
    bad = [f for h, f in (ln.split() for ln in open(MAN)) if sha(os.path.join(FULL, f)) != h]
    print("manifest:", "OK" if not bad else f"DIFFERENT {bad}"); sys.exit(1 if bad else 0) if bad else None
if "--quick" in sys.argv:
    fails = []
    rd = lambda n: (pd.read_csv(os.path.join(FULL, n)), pd.read_csv(os.path.join(QUICK, n)))
    f, q = rd("positive_control_full.csv"); cols = {f"{t}_{s}": (lambda g, t=t, s=s: g[f"{t}_{s}"] < .05) for t in ("plow", "pup") for s in ("ac1", "var")}
    agree(rates(f, ["model", "lost"], cols), rates(q, ["model", "lost"], cols), "positive_control_full", fails)
    f, q = rd("power_bilateral.csv"); agree(rates(f, ["case", "P", "s0"], cols), rates(q, ["case", "P", "s0"], cols), "power_bilateral", fails)
    f, q = rd("power_design.csv"); cd = {f"pup_{s}": (lambda g, s=s: g[f"pup_{s}"] < .05) for s in ("ac1", "var")}
    agree(rates(f, ["L", "r", "cyc", "trend"], cd), rates(q, ["L", "r", "cyc", "trend"], cd), "power_design", fails)
    f, q = rd("step_injection.csv"); cs = {f"{t}_{s}": (lambda g, t=t, s=s: g[f"{t}_{s}"] < .05) for t in ("plow", "pup") for s in ("ac1", "var")}
    agree(rates(f, ["case"], cs), rates(q, ["case"], cs), "step_injection", fails)
    f, q = rd("robustness_data.csv"); cr = {"p_upper": lambda g: g.p_upper < .05, "p_D22": lambda g: g.p_D22 < .05}
    agree(rates(f, ["variant"], cr), rates(q, ["variant"], cr), "robustness_data", fails)
    k = ["variant", "HD", "seg_year0", "config", "frac", "stat"]; m = f.merge(q, on=k, suffixes=("_f", "_q"))
    if len(m) != len(f) or np.abs(m.tau_f - m.tau_q).max() > 1e-12: fails.append("robustness_data: tau of the data differs between full and quick")
    f, q = rd("dalton_control.csv"); m = f.merge(q, on=["block", "transform", "config", "stat"], suffixes=("_f", "_q"))
    if len(m) != len(f) or np.abs(m.tau_f - m.tau_q).max() > 1e-12: fails.append("dalton_control: tau of the data differs between full and quick")
    print("quick vs full:", "OK" if not fails else "FAIL"); [print("  ", x) for x in fails[:20]]; sys.exit(1 if fails else 0)
