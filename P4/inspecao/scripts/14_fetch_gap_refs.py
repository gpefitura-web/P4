"""Round 2026-11-24 (2): sources on early-warning indicators with data gaps / irregular sampling / interpolation.
Same rules as 12_fetch_hopf_refs.py (REG-R2 title check on pages 1-2, REG-R8 max 2 attempts). The PDF URL is read
from OpenAlex at run time. Not part of run_all.sh. Run with `python -I`."""
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT

BIB = os.path.join(ROOT, "bib")
UA = "Mozilla/5.0 (X11; Linux x86_64) research-fetch"
ITEMS = [
    ("gaps2026", "DataGaps_2026_SciAdv_aee1916.pdf", "10.1126/sciadv.aee1916", r"Data gaps and outliers"),
    ("rehfeld2011", "Rehfeld_2011_NPG_18_389.pdf", "10.5194/npg-18-389-2011", r"irregularly sampled time series"),
    ("do2025", "Inconclusive_2025_ESD_16_2035.pdf", "10.5194/esd-16-2035-2025", r"Inconclusive early warning"),
    ("srca2022", "SamplingRateCorrected_2022_PRE_105_024206.pdf", "10.1103/physreve.105.024206", r"Sampling rate"),
]


def head(path):
    t = subprocess.run(["pdftotext", "-l", "2", path, "-"], capture_output=True, text=True).stdout
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", t))


def pdf_urls(doi):
    r = subprocess.run(["curl", "-s", "-m", "40", "-A", "P4-research/1.0",
                        f"https://api.openalex.org/works/doi:{doi}?select=locations"], capture_output=True, text=True)
    try:
        return [l["pdf_url"] for l in json.loads(r.stdout)["locations"] if l.get("pdf_url")]
    except Exception:
        return []


man_p = os.path.join(BIB, "MANIFEST.json")
man = json.load(open(man_p, encoding="utf-8"))
log = []
for key, fn, doi, pat in ITEMS:
    dest = os.path.join(BIB, fn)
    if os.path.exists(dest):
        log.append(f"| {key} | já presente | {fn} |")
        continue
    urls = pdf_urls(doi)[:2] or ["(sem URL de PDF no OpenAlex)"]
    ok = False
    for attempt, url in enumerate(urls, 1):
        with tempfile.TemporaryDirectory() as td:
            tmp = os.path.join(td, "x.pdf")
            r = subprocess.run(["curl", "-s", "-L", "-m", "120", "-A", UA, "-o", tmp, "-w", "%{http_code}", url],
                               capture_output=True, text=True)
            code = r.stdout.strip()
            if code == "200" and open(tmp, "rb").read(5) == b"%PDF-" and re.search(pat, head(tmp), re.I):
                data = open(tmp, "rb").read()
                open(dest, "wb").write(data)
                man[fn] = {"baixado_em": str(datetime.date.today()), "bytes": len(data), "doi": doi,
                           "sha256": hashlib.sha256(data).hexdigest(), "url": url,
                           "validacao": f"padrão de título /{pat}/ nas páginas 1-2", "versao": "open access (OpenAlex)"}
                log.append(f"| {key} | ok (tentativa {attempt}) | {url} |")
                ok = True
                break
            log.append(f"| {key} | falhou na tentativa {attempt} (HTTP {code}) | {url} |")
    if not ok:
        log.append(f"| MANUAL | subir pelo pesquisador | {key}, DOI {doi} |")
json.dump(dict(sorted(man.items())), open(man_p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
with open(os.path.join(BIB, "DOWNLOAD_LOG.md"), "a", encoding="utf-8") as fh:
    fh.write("\n## 2026-11-24 — fontes sobre lacunas, amostragem irregular e interpolação em indicadores de CSD\n"
             "| Item | Resultado | URL / arquivo |\n|---|---|---|\n" + "\n".join(log) + "\n")
print("\n".join(log))
