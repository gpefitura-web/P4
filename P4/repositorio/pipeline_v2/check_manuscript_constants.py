"""Confronts the design constants written by hand in manuscrito/main.tex with the code and the published outputs.
Reads main.tex outside the generated blocks and outside comments, extracts each constant with a pattern that must match exactly once,
and fails if the value differs from the one in the code (imported, inspected or parsed from source). Numbers that are results are not
checked here: they come from make_macros.py.
Usage: python -I check_manuscript_constants.py"""
import os, re, sys, inspect
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indicators as ind, detrend as dt, surrogates as sg, rhk, annual, run_all, state_comparison as sc

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TEX = os.path.join(ROOT, "manuscrito", "main.tex")


def source(name):
    return open(os.path.join(HERE, name), encoding="utf-8").read()


raw = open(TEX, encoding="utf-8").read()
for beg, end in (("%%% BEGIN GENERATED MACROS", "%%% END GENERATED MACROS"), ("%%% BEGIN GENERATED TABLE", "%%% END GENERATED TABLE")):
    raw = raw[:raw.index(beg)] + raw[raw.index(end) + len(end):]
text = "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in raw.splitlines())   # comments removed
WORD = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
ok = True


def num(x):
    return WORD.get(x, x) if isinstance(x, str) and x in WORD else (float(x) if re.fullmatch(r"[\d.]+", str(x)) else x)


def grab(pattern):
    m = re.findall(pattern, text, re.S)
    if len(m) != 1:
        return None
    return m[0] if isinstance(m[0], tuple) else (m[0],)


def check(name, pattern, expected):
    """expected: tuple of values the captured groups must equal (words one..five are read as numbers)."""
    global ok
    g = grab(pattern)
    if g is None:
        ok = False; print(f"FAIL {name}: pattern not found exactly once in main.tex"); return
    got = tuple(num(x) for x in g)
    exp = tuple(expected)
    good = len(got) == len(exp) and all((abs(a - b) < 1e-12 if isinstance(a, float) and isinstance(b, (int, float)) else a == b) for a, b in zip(got, exp))
    ok &= good
    print(f"{'PASS' if good else 'FAIL'} {name}: text {got} code {exp}")


def macro(name):
    m = re.search(r"\\newcommand\{\\" + name + r"\}\{([^}]*)\}", text)
    return float(m.group(1)) if m else None


# --- segment rule and precision bands
check("minimum segment (macro MinSeg)", r"\\newcommand\{\\MinSeg\}\{(\d+)\}", (run_all.MIN_SEG,))
lo, hi = macro("LowMax"), macro("AdeqMin")
good = run_all.precision(int(lo)) == "baixa" and run_all.precision(int(lo) + 1) == "adequada" and hi == lo + 1
ok &= good; print(f"{'PASS' if good else 'FAIL'} precision bands: low up to {lo:g}, adequate from {hi:g}")
w = ind.window_size(run_all.MIN_SEG, 0.5)
check("points at the minimum segment", r"has at least (\d+) points", (w,))
# --- windows and detrending
m = re.search(r"with \$f = (0\.25)\$, ([\d., and]+); \$f = ([\d.]+)\$ is the default", text)
fr = tuple(float(x) for x in re.findall(r"[\d.]+\d", m.group(1) + ", " + m.group(2))) if m else None
good = fr == tuple(ind.FRACS) and m is not None and float(m.group(3)) == inspect.signature(ind.window_size).parameters["frac"].default
ok &= good; print(f"{'PASS' if good else 'FAIL'} window fractions {fr} and default vs code {tuple(ind.FRACS)}")
check("smoothing widths", r"Gaussian smooth with \$\\sigma = (\d+)\$, (\d+) or (\d+) years", tuple(s for s in dt.CONFIGS if s))
check("number of configurations", r"analyzed in (\w+) configurations", (len(dt.CONFIGS),))
check("configurations needed for a flag", r"in at least (\w+) of the four configurations", (3,))
good = re.search(r"conc >= 3", source("make_macros.py")) is not None
ok &= good; print(f"{'PASS' if good else 'FAIL'} make_macros counts segments with at least 3 concordant configurations")
# --- gaps
ms = inspect.signature(annual.segments).parameters["max_fill"].default
check("gap rule", r"Gaps of (\w+) or (\w+) missing years are filled by linear interpolation and the filled points are marked; gaps of (\w+) or more", (1, ms, ms + 1))
# --- surrogates
check("ARMA orders", r"ARMA\(\$p,q\$\) model with \$p,q \\le (\d)\$", (max(max(o) for o in sg.ORDERS),))
good = max(max(o) for o in sg.ORDERS) == 2 and min(min(o) for o in sg.ORDERS) == 0 and len(sg.ORDERS) == 9
ok &= good; print(f"{'PASS' if good else 'FAIL'} ARMA grid is p,q in 0..2 (9 models)")
burn = inspect.signature(sg.simulate).parameters["burn"].default
check("burn-in", r"burn-in of (\d+) steps", (burn,))
good = "burn=" not in source("run_all.py")
ok &= good; print(f"{'PASS' if good else 'FAIL'} run_all does not override the burn-in")
# --- size test (test_step5.py is a script; parsed, and compared with the published output)
t5 = source("test_step5.py")
nrep, ns, L = (int(x) for x in re.search(r"NREP, NS, L = (\d+), (\d+), (\d+)", t5).groups())
nfill = len(re.search(r"filled\[\[([^\]]+)\]\] = True", t5).group(1).split(","))
coef = float(re.search(r"ar1\(L, ([\d.]+), rng\)", t5).group(1))
check("size test design", r"\((\d+) series of (\d+) years, (\w+) interpolated points, coefficient ([\d.]+)\)", (nrep, L, nfill, coef))
pub = open(os.path.join(HERE, "results", "autotest_step5.txt"), encoding="utf-8").read()
good = f"{nrep} null AR(1) series (c={coef:g}, L={L}, {nfill} interpolated points), {ns} ARMA surrogates" in pub
ok &= good; print(f"{'PASS' if good else 'FAIL'} published size test header matches the script design")
a, b = (float(x) for x in re.search(r"0\.03 <= up <= 0\.07", t5) and (0.03, 0.07))
check("size acceptance range (percent)", r"\\newcommand\{\\SizeLo\}\{(\d+)\}", (round(100 * a),))
check("size acceptance range (percent), upper", r"\\newcommand\{\\SizeHi\}\{(\d+)\}", (round(100 * b),))
# --- calibration simulations (D126): constants written by hand in the text against the scripts in pipeline_v2/calibration
CAL = os.path.join(HERE, "calibration")
def csrc(name):
    return open(os.path.join(CAL, name), encoding="utf-8").read()
pcs, pds, sis, pbs, dcs = csrc("positive_control_full.py"), csrc("power_design.py"), csrc("step_injection.py"), csrc("power_bilateral.py"), csrc("dalton_control.py")
good = re.search(r"for _ in range\(40 \* SPY\)", pcs) is not None
ok &= good; print(f"{'PASS' if good else 'FAIL'} positive control burn-in of 40 years is in the script")
check("burn-in of the oscillator", r"after a (\d+)-year burn-in", (40,))
good = re.search(r"cub = 1\.0 if model == \"sub\" else -1\.0", pcs) and re.search(r"abs\(z\) \*\* 4 \* z if model == \"sub\"", pcs) and re.search(r"\(1 \+ abs\(z\)\) if model == \"mult\"", pcs)
ok &= good is not None; print(f"{'PASS' if good else 'FAIL'} oscillator models of the text (a, b, multiplicative 1 + |z|) match the script")
good = all(x in text for x in ("supercritical model ($a = -1$, $b = 0$)", "subcritical model ($a = 1$, $b = 1$)", "multiplied by $1 + |z|$"))
ok &= good; print(f"{'PASS' if good else 'FAIL'} text states the coefficients a, b of the three models")
good = "np.linspace(0.3, 0.7, L)" in pds and "np.full(L, 0.5)" in pds and "(30, 50, 100, 200)" in pds and "0.3 to 0.7" in text and "constant at 0.5" in text and "from 30 to 200 years" in text
ok &= good; print(f"{'PASS' if good else 'FAIL'} true-CSD AR(1) design (0.5 constant, 0.3 to 0.7, lengths 30-200) in text and script")
good = "x[K:] = x[K:] * g + d * SD" in sis and re.search(r"L, K, NS, NREP, SD = 30, 11,", sis) is not None
ok &= good; print(f"{'PASS' if good else 'FAIL'} step injected after year 11 of 30 (macros SIStepYear and SIL read the script)")
import pandas as _pd
_bi = _pd.read_csv(os.path.join(HERE, "results_calibration", "power_bilateral.csv"))
good = tuple(sorted(_bi[_bi.P > 0].P.unique())) == (8.0, 11.0, 15.0) and tuple(sorted(_bi[_bi.s0 > 0].s0.unique())) == (0.10, 0.15, 0.30) and "(8.0, 11.0, 15.0)" in pbs and "(0.10, 0.15, 0.30)" in pbs
ok &= good; print(f"{'PASS' if good else 'FAIL'} period and noise grid of the two-sided power experiment: script and stored results agree")
good = "BLOCKS" in dcs and re.search(r"1795 \+ 36 \* i", dcs) is not None and "n >= 50" in dcs
ok &= good; print(f"{'PASS' if good else 'FAIL'} Dalton blocks of 36 years from 1795 and the 50-day rule are in the script (macros DALBlockLen, DALDaysMin)")
blk = int(re.search(r"1795 \+ (\d+) \* i", dcs).group(1)); days = int(re.search(r"n >= (\d+)", dcs).group(1))
mm = open(os.path.join(HERE, "make_macros_calibration.py")).read()
good = re.search(rf'put\("DALBlockLen", {blk}\)', mm) is not None and re.search(rf'put\("DALDaysMin", {days}\)', mm) is not None
ok &= good; print(f"{'PASS' if good else 'FAIL'} Dalton block length {blk} and day rule {days} in the script equal the macros")
# --- B-V band of the R'_HK conversion
m = re.search(r"valid for \$([\d.]+) < B\\!-\\!V < ([\d.]+)\$", text); blo, bhi = float(m.group(1)), float(m.group(2))
good = (rhk.band(blo - 1e-6).startswith("FORA") and rhk.band(blo + 1e-6) == "DENTRO" and rhk.band(bhi - 1e-6) == "DENTRO"
        and rhk.band(bhi + 1e-6).startswith("EXTRAPOLADO"))
ok &= good; print(f"{'PASS' if good else 'FAIL'} B-V validity band {blo}-{bhi} vs rhk.band")
check("B-V band, table footnote", r"outside ([\d.]+)--([\d.]+)\.", (blo, bhi))
# --- states of HD 166620 and instrumental noise (H1)
st = sc.STATES
check("states", r"minimum~1 \((\d{4})--(\d{4})\), minimum~2 \((\d{4})--(\d{4})\) and the grand minimum \(from (\d{4})\)",
      (st["min1"][0], st["min1"][1], st["min2"][0], st["min2"][1], st["grand"][0]))
check("states, Table 1 rows", r"Minimum 1 \((\d{4})--(\d\d)\).*?Minimum 2 \((\d{4})--(\d\d)\).*?Grand minimum \((\d{4})--\)",
      (st["min1"][0], st["min1"][1] % 100, st["min2"][0], st["min2"][1] % 100, st["grand"][0]))
good = abs(macro("NoiseMW") - 100 * st["min1"][2]) < 1e-9 and st["min1"][2] == st["min2"][2] and abs(macro("NoiseKeck") - 100 * st["grand"][2]) < 1e-9
ok &= good; print(f"{'PASS' if good else 'FAIL'} instrumental noise MW {macro('NoiseMW'):g} % and Keck {macro('NoiseKeck'):g} % vs state_comparison.STATES")
print("ALL OK" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
