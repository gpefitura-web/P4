"""Shared helpers for the P4 inspection scripts.

All scripts are read-only with respect to the project: they read CSV/TSV files
from the package root and append rows to inspecao/checks.csv.
Run with `python -I` (see run_all.sh).
"""
import csv
import math
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
INSP = os.path.dirname(HERE)
ROOT = os.path.dirname(INSP)
DATA = os.path.join(ROOT, "data")
AUDIT = os.path.join(ROOT, "audit")
CHECKS = os.path.join(INSP, "checks.csv")
OUT = os.path.join(INSP, "saidas")

HEADER = ["id", "descricao", "valor_esperado", "valor_obtido",
          "fonte_do_esperado", "resultado"]


def read_vizier(name):
    """Read a VizieR ';'-separated TSV, skipping comments, units and dash rows."""
    path = os.path.join(DATA, name)
    rows = []
    with open(path, encoding="utf-8") as fh:
        lines = [ln.rstrip("\n") for ln in fh
                 if ln.strip() and not ln.startswith("#")]
    header = [c.strip() for c in lines[0].split(";")]
    # lines[1] = units, lines[2] = dashes
    assert set(lines[2].replace(";", "").strip()) <= {"-"}, "unexpected layout"
    for ln in lines[3:]:
        rows.append([c.strip() for c in ln.split(";")])
    return pd.DataFrame(rows, columns=header)


def read_csv(relpath):
    """Read a project CSV as strings (no type guessing, no NA conversion)."""
    return pd.read_csv(os.path.join(ROOT, relpath), dtype=str,
                       keep_default_na=False)


def _fmt(v):
    if isinstance(v, float):
        return f"{v:.6g}"
    return str(v)


def check(cid, desc, expected, obtained, source, tol=None, info=False):
    """Append one row to checks.csv and echo it.

    tol: absolute tolerance for numeric comparison (None = exact equality).
    info=True records a value with no pass/fail judgement.
    """
    if info:
        res = "INFO"
    elif tol is not None:
        try:
            res = "PASS" if abs(float(obtained) - float(expected)) <= tol else "FAIL"
        except (TypeError, ValueError):
            res = "FAIL"
    else:
        res = "PASS" if _fmt(expected) == _fmt(obtained) else "FAIL"
    new = not os.path.exists(CHECKS)
    with open(CHECKS, "a", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(HEADER)
        w.writerow([cid, desc, _fmt(expected), _fmt(obtained), source, res])
    print(f"[{res}] {cid}: {desc} | expected={_fmt(expected)} obtained={_fmt(obtained)}")
    return res


def hd_key(s):
    """Normalise an HD identifier ('HD 10700', '10700 ', '219834B')."""
    return str(s).replace("HD", "").strip()


def isnum(s):
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        return False


def write_out(name, text):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(text)


__all__ = ["read_vizier", "read_csv", "check", "hd_key", "isnum", "write_out",
           "ROOT", "DATA", "AUDIT", "INSP", "OUT", "math", "pd"]
