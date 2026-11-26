"""Builds manuscrito_overleaf.zip: the files to upload to Overleaf (main.tex and the generated pieces it inputs, references, highlights,
alternative text of the figures, and the figures in PDF and EPS). Deterministic (fixed timestamps).   Usage: python3 make_overleaf_zip.py"""
import os, zipfile, glob
ROOT = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(ROOT, "manuscrito")
files = ["main.tex", "calibration_macros.tex", "cal_table_stars.tex", "cal_table_simulations.tex", "references.bib", "highlights.docx", "highlights.tex", "alt_text.md"]
files += sorted(os.path.relpath(f, M) for f in glob.glob(os.path.join(M, "figures", "*")))
out = os.path.join(ROOT, "manuscrito_overleaf.zip")
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in files:
        zi = zipfile.ZipInfo(p, date_time=(2026, 11, 26, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
        z.writestr(zi, open(os.path.join(M, p), "rb").read())
print(len(files), "files ->", out, os.path.getsize(out) // 1024, "KB")
