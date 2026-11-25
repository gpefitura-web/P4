"""Assembles repositorio/ : the exact folder to be published, i.e. the code, input data, reference outputs and manuscript
sources that reproduce every number, table and figure of the manuscript. Source of truth stays in pipeline_v2/, manuscrito/,
data/ and consolidacao/; run this script again after any change and then verify with repositorio/reproduce.sh.
Usage: python3 make_repositorio.py"""
import os, shutil, hashlib, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "repositorio")
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)


def cp(src, dst=None):
    dst = dst or src
    d = os.path.join(OUT, dst)
    os.makedirs(os.path.dirname(d), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, src), d)


# input data and the frozen catalogue
cp("consolidacao/p4_star_catalog.csv")
for f in ("J_AJ_163_183_table1.tsv", "J_ApJ_936_L23_table2.tsv"):
    cp(f"data/{f}")
for f in sorted(glob.glob(os.path.join(ROOT, "data/HK_Project_v2001_NSO/*"))):
    cp(os.path.relpath(f, ROOT))
# code, tests, fonts
for f in ("fetch_egeland_table4", "p4io", "annual", "indicators", "detrend", "surrogates", "state_comparison", "rhk", "run_all", "group_primary",
          "report", "check_manuscript_constants", "make_macros", "make_tables", "make_figures", "power_simulation",
          "test_step1", "test_step2", "test_step3", "test_step4", "test_step5", "test_step6", "test_step7"):
    cp(f"pipeline_v2/{f}.py")
for f in ("CourierPrime-Regular.ttf", "CourierPrime-Bold.ttf", "CourierPrime-Italic.ttf", "OFL.txt"):
    cp(f"pipeline_v2/fonts/{f}")
# reference outputs (deterministic ones only; run_log.txt and run_stdout.txt carry timings)
for f in ("star_results.csv", "segments.csv", "star_metrics.csv", "h1.json", "group_primary.csv", "group_holm.csv",
          "power_simulation.txt", "autotest_step5.txt", "REPORT.md"):
    cp(f"pipeline_v2/results/{f}")
# manuscript sources
for f in ("main.tex", "references.bib", "highlights.docx", "highlights.tex", "build.sh"):
    cp(f"manuscrito/{f}")
for f in sorted(glob.glob(os.path.join(ROOT, "manuscrito/figures/Figure_*"))):
    cp(os.path.relpath(f, ROOT))


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


data_rows = "\n".join(f"| `{os.path.relpath(p, OUT)}` | `{sha(p)[:16]}…` |" for p in
                      [os.path.join(OUT, "consolidacao/p4_star_catalog.csv"), os.path.join(OUT, "data/J_AJ_163_183_table1.tsv"),
                       os.path.join(OUT, "data/J_ApJ_936_L23_table2.tsv")])

open(os.path.join(OUT, "requirements.txt"), "w").write("numpy==2.5.5\npandas==3.1.1\nscipy==1.18.1\nstatsmodels==0.15.0\nmatplotlib==3.11.2\nfonttools==4.68.0\npython-docx==1.2.0\n")

open(os.path.join(OUT, "reproduce.sh"), "w").write('''#!/usr/bin/env bash
# Reproduces every number, table and figure of the manuscript from the input data and compares them with the published outputs.
# Usage: PYTHON=/path/to/python bash reproduce.sh      (about 6 minutes; Python 3.13 with requirements.txt)
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"
PY="${PYTHON:-python3}"
export SOURCE_DATE_EPOCH=0
"$PY" -I pipeline_v2/fetch_egeland_table4.py       # Table 4 of Egeland et al. is downloaded, not redistributed (needs network; or: --from FILE)
"$PY" -I verify_reproduction.py --manifest        # the folder is exactly the published one
"$PY" -I verify_reproduction.py --snapshot        # keep the published outputs in _published/ and clear them
cd pipeline_v2
for t in 1 2 3 4 6 7; do echo "test_step$t: $("$PY" -I test_step$t.py | tail -1)"; done
echo "test_step5 (size of the surrogate test, ~2 min): $("$PY" -I test_step5.py | tail -1)"
"$PY" -I power_simulation.py > /dev/null
"$PY" -I run_all.py                                # the single stellar run, fixed seeds (~1 min)
"$PY" -I group_primary.py > /dev/null
"$PY" -I report.py
"$PY" -I make_macros.py
"$PY" -I make_tables.py
"$PY" -I make_figures.py
"$PY" -I check_manuscript_constants.py | tail -1   # design constants written in main.tex vs the code
cd ..
"$PY" -I verify_reproduction.py --compare
if command -v pdflatex >/dev/null; then
  cd manuscrito && pdflatex -interaction=nonstopmode main.tex >/dev/null && bibtex main >/dev/null || true
  pdflatex -interaction=nonstopmode main.tex >/dev/null; pdflatex -interaction=nonstopmode main.tex | tail -2
fi
''')
os.chmod(os.path.join(OUT, "reproduce.sh"), 0o755)

open(os.path.join(OUT, "verify_reproduction.py"), "w").write('''"""Checks the published folder and the reproduction.
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
EXACT = [RES + f for f in ("power_simulation.txt", "autotest_step5.txt", "REPORT.md")] + ["manuscrito/main.tex"] + \\
        [f"manuscrito/figures/Figure_{n}.{e}" for n in (1, 2, 3, 4) for e in ("pdf", "eps")]
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
        h, p = ln.rstrip("\\n").split("  ", 1)
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
        i = src.index(b); i = src.index("\\n", i) + 1; j = src.index(e)
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
''')

open(os.path.join(OUT, "README.md"), "w").write(f'''# Reproduction package: testing critical slowing down in Mount Wilson S-index series of Sun-like stars

This folder holds everything needed to reproduce every number, table and figure of the manuscript (`manuscrito/main.tex`), and nothing else:
the input data, the code, the reference outputs and the manuscript sources. `MANIFEST.sha256` lists every file; `reproduce.sh` checks it.

## Run
```
pip install -r requirements.txt          # Python 3.13
PYTHON=python3 bash reproduce.sh         # about 6 minutes
```
`reproduce.sh` (1) checks the manifest, (2) saves the published outputs to `_published/` and clears them, (3) runs the checks, the size test of the
surrogate procedure, the power simulation and the single stellar run (fixed seeds), (4) rewrites the generated blocks of `main.tex` and the figures,
(5) compares everything with the published outputs (`REPRODUCTION OK`), and (6) compiles the manuscript if `pdflatex` is installed (class `elsarticle`).

## Layout
| Path | Content |
|---|---|
| `consolidacao/p4_star_catalog.csv` | frozen star catalog (groups, B-V, eligibility) |
| `data/` | input series: Baum et al. Table 1 (VizieR J/AJ/163/183), Luhn et al. Table 2 (VizieR J/ApJ/936/L23), HK_Project_v2001_NSO (Harvard Dataverse, doi:10.7910/DVN/H85QPF). Table 4 of Egeland et al. is **not** included: `pipeline_v2/fetch_egeland_table4.py` downloads it |
| `pipeline_v2/` | code (`p4io`, `annual`, `indicators`, `detrend`, `surrogates`, `state_comparison`, `rhk`, `run_all`, `group_primary`, `report`, `power_simulation`), tests, figure fonts, `results/` |
| `manuscrito/` | `main.tex`, `references.bib`, highlights, `figures/Figure_1-4` (PDF and EPS), `build.sh` |

## From the manuscript to the code
| Manuscript item | Produced by | Output |
|---|---|---|
| Sample, segments (Sect. 2.1; Table 2 columns L, Interp.) | `p4io.py`, `annual.py` (via `run_all.py`) | `results/segments.csv` |
| Indicators, detrending, surrogate p values (Sects. 2.2, 2.3, 3.3; Table 2) | `indicators.py`, `detrend.py`, `surrogates.py`, `run_all.py` | `results/star_results.csv` |
| Size of the surrogate test (Sect. 3.1) | `test_step5.py` | `results/autotest_step5.txt` |
| Power (AUC; Sect. 3.1) | `power_simulation.py` | `results/power_simulation.txt` |
| H1, Table 1, Figure 1 | `state_comparison.py` (via `run_all.py`) | `results/h1.json` |
| R'_HK (Sect. 3.3) | `rhk.py`, `run_all.py` | `results/star_results.csv` (series `RHK`) |
| Group tests (Sect. 3.4) | `run_all.py`, `group_primary.py` | `results/star_metrics.csv`, `group_primary.csv`, `group_holm.csv` |
| All numbers in the text | `make_macros.py` | block between `%%% BEGIN/END GENERATED MACROS` in `manuscrito/main.tex` |
| Design constants written in the text (windows, widths, ARMA grid, size test, power design, B-V band, states) | `check_manuscript_constants.py` | fails if `main.tex` and the code disagree |
| Table 2 | `make_tables.py` | block between `%%% BEGIN/END GENERATED TABLE` |
| Figures 1 to 4 | `make_figures.py` | `manuscrito/figures/Figure_N.pdf` and `.eps` |
| Facts report | `report.py` | `results/REPORT.md` |

Seeds: stellar run 20261124; size test 5050; power simulation 1600 + L. The figure files are byte-for-byte reproducible (`SOURCE_DATE_EPOCH=0`).
Tables and JSON are compared numerically (relative tolerance 1e-9): the ARMA fits depend on the `statsmodels` version, so use the pinned versions.

## Table 4 of Egeland et al. (2017): downloaded, not redistributed
The calibrated solar S-index series (machine-readable Table 4 of the article) is fetched by `reproduce.sh` from the journal's public server
(`https://content.cld.iop.org/journals/0004-637X/835/1/25/revision1/apjaa4e49t4_mrt.txt`) and checked against
sha256 `6e2746d535d7d9e3e69ebc860b840494b5efca5460e613cc43fc46e060a90548` (6349 rows, 1966-2016). Without network access, download it by other means and run
`python pipeline_v2/fetch_egeland_table4.py --from <file>`. The Sun row of Table 2, Figure 3 and the solar numbers need this file; the rest does not.

## Input data shipped here (frozen hashes, first 16 hex digits)
| File | sha256 |
|---|---|
{data_rows}

## Acknowledgements and terms of the data
The HK_Project_v2001_NSO data derive from the Mount Wilson Observatory HK Project, which was supported by both public and private funds through the
Carnegie Observatories, the Mount Wilson Institute, and the Harvard-Smithsonian Center for Astrophysics starting in 1966 and continuing for over 36 years.
These data are the result of the dedicated work of O. Wilson, A. Vaughan, G. Preston, D. Duncan, S. Baliunas, and many others (`data/HK_Project_v2001_NSO/README.pdf`).
This research has made use of the VizieR catalogue access tool, CDS, Strasbourg, France (doi:10.26093/cds/vizier).

## License
- **Code, derived results and figures produced by it:** MIT License (`LICENSE`), copyright 2026 Airton M. S. Borin Junior.
- **Input data (`data/`, `consolidacao/`):** not covered by the MIT License. Copied unaltered from the sources cited above; the terms of use of each original source apply (the acknowledgement required by the HK Project authors is reproduced above). Table 4 of Egeland et al. is not redistributed.
- **Fonts (`pipeline_v2/fonts/`):** Courier Prime, SIL Open Font License 1.1 (`pipeline_v2/fonts/OFL.txt`).
- **Manuscript sources (`manuscrito/`):** included only so that the numbers, table and figures can be rebuilt; the text is the author's, and the published version will be under the journal's terms.

## How to cite
See `CITATION.cff`. Cite the archived version by its DOI (Zenodo) and the article.
''')


YEAR, HOLDER = "2026", "Airton M. S. Borin Junior"
open(os.path.join(OUT, "LICENSE"), "w").write(f"""MIT License

Copyright (c) {YEAR} {HOLDER}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")
ABSTRACT = ("Code, input data, reference outputs and manuscript sources that reproduce every number, table and figure of the article "
            "on rolling-window early-warning indicators of critical slowing down in annual Mount Wilson S-index series of Sun-like stars and the Sun. "
            "Run reproduce.sh (about 6 minutes). Third-party input data keep the terms of their original sources; code is MIT. Needs network access once, to download Table 4 of Egeland et al. (2017).")
open(os.path.join(OUT, "CITATION.cff"), "w").write(f"""cff-version: 1.2.0
message: "If you use this software, please cite it using the metadata below."
title: "Reproduction package: testing critical slowing down in Mount Wilson S-index of Sun-like stars"
version: 1.0.0
date-released: 2026-11-25
license: MIT
authors:
  - family-names: "Borin Junior"
    given-names: "Airton M. S."
    affiliation: "Instituto Federal do Triangulo Mineiro (IFTM), Uberaba, Brazil"
abstract: "{ABSTRACT}"
keywords:
  - critical slowing down
  - early-warning signals
  - stellar activity cycles
  - chromospheric activity
  - S index
  - Maunder minimum
repository-code: "https://github.com/gpefitura-web/P4"
# doi: "10.5281/zenodo.XXXXXXX"   (add the DOI reserved on Zenodo)
""")
import json
json.dump({"title": "Reproduction package: testing critical slowing down in Mount Wilson S-index of Sun-like stars",
           "upload_type": "software", "access_right": "open", "license": "mit", "language": "eng", "version": "1.0.0",
           "publication_date": "2026-11-25",
           "creators": [{"name": "Borin Junior, Airton M. S.", "affiliation": "Instituto Federal do Triangulo Mineiro (IFTM), Uberaba, Brazil"}],
           "description": ABSTRACT + " Contents: pipeline code and tests, input series (Baum et al. 2022; Luhn et al. 2022; HK_Project_v2001_NSO; the solar table of Egeland et al. 2017 is downloaded at run time, not redistributed), "
                          "reference outputs, figures and manuscript sources, with a sha256 manifest.",
           "keywords": ["critical slowing down", "early-warning signals", "stellar activity cycles", "chromospheric activity", "S index", "Maunder minimum"]},
          open(os.path.join(OUT, ".zenodo.json"), "w"), indent=2, ensure_ascii=False)

# manifest, last
files = []
for d, dirs, fs in os.walk(OUT):
    for f in fs:
        p = os.path.relpath(os.path.join(d, f), OUT)
        if p != "MANIFEST.sha256":
            files.append(p)
with open(os.path.join(OUT, "MANIFEST.sha256"), "w") as fh:
    for p in sorted(files):
        fh.write(f"{sha(os.path.join(OUT, p))}  {p}\n")
print(len(files), "files in", OUT, sum(os.path.getsize(os.path.join(OUT, p)) for p in files) // 1024, "KB")

import zipfile
ZIP = os.path.join(ROOT, "repositorio_zenodo_v1.0.0.zip")
with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(files + ["MANIFEST.sha256"]):
        zi = zipfile.ZipInfo(os.path.join("p4-repositorio-v1.0.0", p), date_time=(2026, 11, 25, 0, 0, 0))
        zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
        z.writestr(zi, open(os.path.join(OUT, p), "rb").read())
print("zip for Zenodo:", os.path.basename(ZIP), os.path.getsize(ZIP) // 1024, "KB, sha256", sha(ZIP))
