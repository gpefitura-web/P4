"""Builds submissao_new_astronomy/ (and .zip): the files for the Elsevier submission system, with the figures under logical names
Figure_1 ... Figure_11 in the order of the text, main.tex pointing at them, and the alternative text renumbered the same way.
Source of truth stays in manuscrito/. Deterministic.   Usage: python3 make_submission_folder.py"""
import os, re, shutil, zipfile, glob
ROOT = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(ROOT, "manuscrito"); OUT = os.path.join(ROOT, "submissao_new_astronomy")
MAP = {"cal_fig4_qq": 1, "cal_fig1_controls": 2, "cal_fig2_power_grid": 3, "cal_fig3_design": 4, "cal_fig6_step": 5, "Figure_1": 6,
       "cal_fig5_sigma_f": 7, "cal_fig7_dalton": 8, "Figure_2": 9, "Figure_3": 10, "Figure_4": 11}
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, "figures"))
tex = open(os.path.join(M, "main.tex"), encoding="utf-8").read()
used = re.findall(r"figures/(\w+)\}", tex)
assert sorted(set(used)) == sorted(MAP), (sorted(set(used)), sorted(MAP))
order = [MAP[u] for u in used]
assert order == sorted(order), "figures are not in order of appearance in main.tex: " + str(order)   # LaTeX numbers them by position
tex = re.sub(r"figures/(\w+)\}", lambda m: f"figures/Figure_{MAP[m.group(1)]}}}", tex)
open(os.path.join(OUT, "main.tex"), "w", encoding="utf-8").write(tex)
for old, n in MAP.items():
    for ext in ("pdf", "eps"):
        shutil.copy2(os.path.join(M, "figures", f"{old}.{ext}"), os.path.join(OUT, "figures", f"Figure_{n}.{ext}"))
for f in ("calibration_macros.tex", "cal_table_stars.tex", "cal_table_simulations.tex", "references.bib", "highlights.docx", "highlights.tex"):
    shutil.copy2(os.path.join(M, f), os.path.join(OUT, f))
alt = open(os.path.join(M, "alt_text.md"), encoding="utf-8").read()
alt = re.sub(r"## Figure (\d+) \(`[^`]+`\)", lambda m: f"## Figure {m.group(1)} (`Figure_{m.group(1)}`)", alt)
open(os.path.join(OUT, "alt_text.md"), "w", encoding="utf-8").write(alt)
files = sorted(os.path.relpath(os.path.join(d, f), OUT) for d, _, fs in os.walk(OUT) for f in fs)
zp = os.path.join(ROOT, "submissao_new_astronomy.zip")
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for p in files:
        zi = zipfile.ZipInfo(p, date_time=(2026, 11, 28, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
        z.writestr(zi, open(os.path.join(OUT, p), "rb").read())
print(len(files), "files ->", zp, os.path.getsize(zp) // 1024, "KB")
