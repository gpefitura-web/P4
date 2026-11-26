"""Checks the published folder and the reproduction.
  --manifest : every file listed in MANIFEST.sha256 is present with the same hash, and nothing else is in the folder
  --snapshot : copies the published outputs to _published/ and clears them (so that nothing can pass by being left over)
  --compare  : regenerated outputs against _published/ (CSV and JSON numerically, text and figures byte for byte)"""
import os, sys, json, shutil, hashlib
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, "_published")
RES = "pipeline_v2/results/"
TABULAR = [RES + f for f in ("star_results.csv", "segments.csv", "star_metrics.csv", "group_primary.csv", "group_holm.csv")]
JSONS = [RES + "h1.json"]
EXACT = [RES + f for f in ("power_simulation.txt", "autotest_step5.txt", "REPORT.md", "scale_sensitivity.txt", "power_cycle.txt", "power_grid.txt", "positive_control.txt", "h1_bootstrap.txt", "robustness.txt", "run_comparison.txt")] + ["manuscrito/main.tex"] + \
        [f"manuscrito/figures/Figure_{n}.{e}" for n in (1, 2, 3, 4) for e in ("pdf", "eps")]
CAL = ["manuscrito/calibration_macros.tex", "manuscrito/cal_table_stars.tex", "manuscrito/cal_table_simulations.tex"] + \
      [f"manuscrito/figures/{n}.{e}" for n in ("cal_fig1_controls", "cal_fig2_power_grid", "cal_fig3_design", "cal_fig4_qq", "cal_fig5_sigma_f", "cal_fig6_step", "cal_fig7_dalton") for e in ("pdf", "eps")] + \
      ["pipeline_v2/results_calibration/" + f for f in ("f_sensitivity.txt", "qq_pvalues.csv", "qq_pvalues.txt", "example_series.csv")]   # regenerated every run
EXACT += CAL
FETCHED = "data/Egeland2017_table4_apjaa4e49t4_mrt.txt"; FETCHED_SHA = "6e2746d535d7d9e3e69ebc860b840494b5efca5460e613cc43fc46e060a90548"
BLOCKS = [("%%% BEGIN GENERATED MACROS", "%%% END GENERATED MACROS"), ("%%% BEGIN GENERATED TABLE", "%%% END GENERATED TABLE")]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


def manifest():
    listed = {}
    for ln in open(os.path.join(HERE, "MANIFEST.sha256")):
        h, p = ln.rstrip("\n").split("  ", 1)
        listed[p] = h
    present = set()
    for d, dirs, files in os.walk(HERE):
        dirs[:] = [x for x in dirs if x not in ("_published", "__pycache__")]
        for f in files:
            p = os.path.relpath(os.path.join(d, f), HERE)
            if p == FETCHED:
                continue
            if p != "MANIFEST.sha256" and not p.endswith((".aux", ".log", ".bbl", ".blg", ".out")) and p != "manuscrito/main.pdf":
                present.add(p)
    bad = [p for p in listed if p not in present or sha(os.path.join(HERE, p)) != listed[p]]
    extra = sorted(present - set(listed))
    if os.path.exists(os.path.join(HERE, FETCHED)):
        okf = sha(os.path.join(HERE, FETCHED)) == FETCHED_SHA
        print("downloaded Egeland Table 4:", "hash OK" if okf else "HASH MISMATCH")
        if not okf:
            sys.exit(1)
    print(f"manifest: {len(listed)} files listed; changed or missing: {bad or 'none'}; not listed: {extra or 'none'}")
    sys.exit(1 if bad or extra else 0)


def snapshot():
    for p in TABULAR + JSONS + EXACT:
        os.makedirs(os.path.dirname(os.path.join(SNAP, p)), exist_ok=True)
        shutil.copy2(os.path.join(HERE, p), os.path.join(SNAP, p))
        if p != "manuscrito/main.tex":
            os.remove(os.path.join(HERE, p))
    src = open(os.path.join(HERE, "manuscrito/main.tex"), encoding="utf-8").read()
    for b, e in BLOCKS:                              # blank the generated blocks: they must be rewritten
        i = src.index(b); i = src.index("\n", i) + 1; j = src.index(e)
        src = src[:i] + src[j:]
    open(os.path.join(HERE, "manuscrito/main.tex"), "w", encoding="utf-8").write(src)
    print("published outputs saved to _published/ and cleared")


def close(a, b):
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(close(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(close(x, y) for x, y in zip(a, b))
    if isinstance(a, float) or isinstance(b, float):
        return bool(np.isclose(a, b, rtol=1e-9, atol=1e-12, equal_nan=True))
    return a == b


def compare():
    ok = True
    rows = []
    for p in TABULAR:
        a, b = pd.read_csv(os.path.join(HERE, p), dtype={"HD": str}), pd.read_csv(os.path.join(SNAP, p), dtype={"HD": str})
        good = list(a.columns) == list(b.columns) and a.shape == b.shape and all(
            np.allclose(a[c], b[c], rtol=1e-9, atol=1e-12, equal_nan=True) if a[c].dtype.kind in "fi" else (a[c].fillna("").astype(str) == b[c].fillna("").astype(str)).all()
            for c in a.columns)
        rows.append((p, "numerically equal" if good else "DIFFERENT")); ok &= good
    for p in JSONS:
        good = close(json.load(open(os.path.join(HERE, p))), json.load(open(os.path.join(SNAP, p))))
        rows.append((p, "numerically equal" if good else "DIFFERENT")); ok &= good
    for p in EXACT:
        good = sha(os.path.join(HERE, p)) == sha(os.path.join(SNAP, p))
        rows.append((p, "identical" if good else "DIFFERENT")); ok &= good
    for p, r in rows:
        print(f"{r:18} {p}")
    print("REPRODUCTION OK" if ok else "REPRODUCTION FAILED")
    sys.exit(0 if ok else 1)


{"--manifest": manifest, "--snapshot": snapshot, "--compare": compare}[sys.argv[1]]()
