"""Step 1 - data input for the P4 pipeline v2. Read-only on data/ and consolidacao/.
Run with `python -I` (path set by the caller via sys.path of this folder)."""
import os
import glob
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")


def load_catalog(only_included=True):
    """Frozen consolidation catalogue; keeps status_amostra == 'incluida' by default."""
    df = pd.read_csv(os.path.join(ROOT, "consolidacao", "p4_star_catalog.csv"),
                     dtype=str, keep_default_na=False)
    return df[df.status_amostra == "incluida"].reset_index(drop=True) if only_included else df


def load_baum(drop_sigma=True, rule="contains"):
    """Baum+2022 Table 1 (VizieR J/AJ/163/183). Columns: HD, S, t (decimal year), inst, flag."""
    rows = []
    with open(os.path.join(DATA, "J_AJ_163_183_table1.tsv"), encoding="utf-8") as fh:
        for ln in fh:
            if ln.startswith("#") or ";" not in ln:
                continue
            p = [x.strip() for x in ln.rstrip("\n").split(";")]
            if len(p) < 5 or not p[0] or p[0] == "HD" or set(p[0]) <= set("-"):
                continue
            try:
                float(p[2])
            except ValueError:
                continue
            rows.append((p[0], float(p[1]), float(p[2]), p[3], p[4]))
    df = pd.DataFrame(rows, columns=["HD", "S", "t", "inst", "flag"])
    if drop_sigma:
        # rule "contains": drops 'sigma' and '1day/sigma' (N_obs_limpo, 61662 rows, step-1 check)
        # rule "catalog": drops only flag == 'sigma' (61691 rows); this is the rule behind the frozen
        # catalogue segment lengths (inspecao/scripts/17_recommendation_support.py). See ACHADOS #3.
        bad = df.flag.str.contains("sigma") if rule == "contains" else (df.flag == "sigma")
        df = df[~bad].reset_index(drop=True)
    df["era"] = np.where(df.inst.str.startswith("HKP"), "MW", "Keck")
    return df


def load_v2001():
    """HK_Project_v2001_NSO .mgd files: field 2 = S, field 3 = JD - 2444000, field 8 = instrument."""
    rows = []
    for fn in sorted(glob.glob(os.path.join(DATA, "HK_Project_v2001_NSO", "*.mgd"))):
        hd = os.path.basename(fn)[2:-4].lstrip("0")          # e.g. '131156a'
        hd = hd.upper() if hd[-1].isalpha() else hd
        with open(fn, encoding="latin-1") as fh:
            for ln in fh:
                f = ln.split()
                if len(f) < 10:
                    continue
                jd = 2444000.0 + float(f[2])
                rows.append((hd, float(f[1]), 2000.0 + (jd - 2451544.5) / 365.25, f[7]))
    df = pd.DataFrame(rows, columns=["HD", "S", "t", "inst"])
    df["era"] = "MW"
    return df


def load_egeland():
    """Egeland+2017 Table 4: JD-2400000, original S, calibrated S, instrument."""
    rows = []
    with open(os.path.join(DATA, "Egeland2017_table4_apjaa4e49t4_mrt.txt"), encoding="utf-8") as fh:
        for ln in fh:
            f = ln.split()
            if len(f) == 4 and f[0].replace(".", "").isdigit() and f[3].startswith(("MWO", "NSO", "SSS")):
                jd = 2400000.0 + float(f[0])
                rows.append((float(f[2]), 2000.0 + (jd - 2451544.5) / 365.25, f[3], float(f[1])))
    return pd.DataFrame(rows, columns=["S", "t", "inst", "S_orig"])


def load_star(hd, cat_row=None):
    """Raw observations (columns S, t, era) of one catalogue star from its declared source."""
    src = cat_row["serie_fonte"]
    if src == "Baum":
        return _BAUM_CACHE().query("HD == @hd")[["S", "t", "era"]].reset_index(drop=True)
    if src == "v2001":
        return _V_CACHE().query("HD == @hd")[["S", "t", "era"]].reset_index(drop=True)
    if src == "Egeland2017_T4":
        e = load_egeland()
        return pd.DataFrame({"S": e.S, "t": e.t, "era": "Sun"})
    raise ValueError(src)


_cache = {}
def _BAUM_CACHE():
    return _cache.setdefault("b", load_baum(rule="catalog"))
def _V_CACHE():
    return _cache.setdefault("v", load_v2001())
