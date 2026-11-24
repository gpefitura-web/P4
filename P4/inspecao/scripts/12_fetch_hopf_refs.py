"""Round 2026-11-24: download and validate sources on early-warning signals near Hopf bifurcations / limit cycles.
Same rules as 07_fetch_refs.py (REG-R2, REG-R8: max 2 attempts, title pattern on the first two pages).
Not part of run_all.sh. Run with `python -I`."""
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
    ("kuehn2011", "Kuehn_2011_PhysD_240_1020_arXiv1101.2899.pdf", "10.1016/j.physd.2011.02.012", "manuscript (arXiv:1101.2899)",
     "https://arxiv.org/pdf/1101.2899", r"critical transitions"),
    ("kuehn2013", "Kuehn_2013_JNonlinSci_23_457_arXiv1101.2908.pdf", "10.1007/s00332-012-9158-x", "manuscript (arXiv:1101.2908)",
     "https://arxiv.org/pdf/1101.2908", r"Normal Forms, Variance"),
    ("bury2020", "Bury_2020_JRSocInterface_17_20200482.pdf", "10.1098/rsif.2020.0482", "published (PMC)",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC7536046/pdf/", r"spectral early warning signals"),
    ("boettiger2013", "Boettiger_2013_TheorEcol_6_255_arXiv1305.6700.pdf", "10.1007/s12080-013-0192-6", "manuscript (arXiv:1305.6700)",
     "https://arxiv.org/pdf/1305.6700", r"charted and uncharted"),
]


def head(path):
    t = subprocess.run(["pdftotext", "-l", "2", path, "-"], capture_output=True, text=True).stdout
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", t))


man_p = os.path.join(BIB, "MANIFEST.json")
man = json.load(open(man_p, encoding="utf-8"))
log = []
for key, fn, doi, ver, url, pat in ITEMS:
    dest = os.path.join(BIB, fn)
    if os.path.exists(dest):
        log.append(f"| {key} | já presente | {fn} |")
        continue
    ok = False
    for attempt in (1, 2):
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
                           "validacao": f"padrão de título /{pat}/ nas páginas 1-2", "versao": ver}
                log.append(f"| {key} | ok (tentativa {attempt}) | {url} |")
                ok = True
                break
            log.append(f"| {key} | falhou na tentativa {attempt} (HTTP {code}) | {url} |")
    if not ok:
        log.append(f"| MANUAL | subir pelo pesquisador | {key}, DOI {doi} |")
json.dump(dict(sorted(man.items())), open(man_p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
with open(os.path.join(BIB, "DOWNLOAD_LOG.md"), "a", encoding="utf-8") as fh:
    fh.write("\n## 2026-11-24 — fontes sobre sinais precursores em Hopf/ciclo limite (pedido do pesquisador)\n"
             "| Item | Resultado | URL / arquivo |\n|---|---|---|\n" + "\n".join(log) + "\n")
print("\n".join(log))
