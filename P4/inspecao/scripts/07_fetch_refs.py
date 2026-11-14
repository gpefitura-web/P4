"""Phase 1 - download and validate the sources approved for the P4 resolution round.

REG-ACT / REG-R2 / REG-R8: each item gets at most 2 attempts; a PDF is accepted only if
the first pages contain the expected title pattern (and none of the forbidden ones).
Accepted files go to bib/, with sha256 and provenance appended to bib/MANIFEST.json and
bib/DOWNLOAD_LOG.md. Rejected files are not kept.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import hashlib
import json
import re
import subprocess
import tempfile
import unicodedata
import datetime

from common import ROOT

BIB = os.path.join(ROOT, "bib")
UA = "Mozilla/5.0 (X11; Linux x86_64) research-fetch"
# key, filename, doi, version, url, must-match, must-not-match
ITEMS = [
    ("shah2018", "Shah_2018_ApJL_863_L26.pdf", "10.3847/2041-8213/aad40c", "published",
     "https://iopscience.iop.org/article/10.3847/2041-8213/aad40c/pdf", r"HD 4915", None),
    ("brandenburg1998", "Brandenburg_1998_ApJL_498_L51.pdf", "10.1086/311297", "published",
     "https://iopscience.iop.org/article/10.1086/311297/pdf",
     r"Time Evolution of the Magnetic Activity Cycle Period", r"Results for an Expanded"),
    ("korolik2023", "Korolik_2023_AJ_166.pdf", "10.3847/1538-3881/ace906", "published",
     "https://iopscience.iop.org/article/10.3847/1538-3881/ace906/pdf",
     r"Pole-on Solar Analog", None),
    ("egeland2017_arxiv", "Egeland_2017_arXiv1611.04540.pdf", "10.3847/1538-4357/835/1/25",
     "manuscript (arXiv:1611.04540)", "https://arxiv.org/pdf/1611.04540",
     r"S-index of the Sun", None),
    ("luhn2022_arxiv", "Luhn_2022_arXiv2207.00612.pdf", "10.3847/2041-8213/ac8b13",
     "manuscript (arXiv:2207.00612)", "https://arxiv.org/pdf/2207.00612",
     r"Portrait of a Star Entering a Grand Magnetic Minimum", None),
    ("baum2022_arxiv", "Baum_2022_arXiv2203.13376.pdf", "10.3847/1538-3881/ac5683",
     "manuscript (arXiv:2203.13376)", "https://arxiv.org/pdf/2203.13376",
     r"Five Decades of Chromospheric Activity", None),
]


# Not fetched: HTTP 403 twice from Wiley (REG-R8), the PIK copy of Held & Kleinen is flagged
# PRIVATE in the repository record (not circumvented), Peng 1993 is closed access.
MANUAL = [("Held & Kleinen 2004, GRL 31, L23207", "10.1029/2004GL020972"),
          ("Livina & Lenton 2007, GRL 34, L03712", "10.1029/2006GL028672"),
          ("Peng et al. 1993, Phys. Rev. E 47, 3730", "10.1103/PhysRevE.47.3730"),
          ("Jarvinen & Strassmeier 2025, A&A 698, A93 (published version)", "10.1051/0004-6361/202554111"),
          ("Olah et al. 2016, A&A 590, A133 (published version)", "10.1051/0004-6361/201628479")]


def norm(t):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", t))


def fetch(url, out):
    r = subprocess.run(["curl", "-s", "-m", "90", "-L", "-A", UA, "-o", out, "-w", "%{http_code}", url],
                       capture_output=True, text=True)
    return r.stdout.strip()


def first_pages(path):
    r = subprocess.run(["pdftotext", "-l", "2", path, "-"], capture_output=True, text=True)
    return norm(r.stdout)


man_path = os.path.join(BIB, "MANIFEST.json")
manifest = json.load(open(man_path)) if os.path.exists(man_path) else {}
log = []
today = datetime.date.today().isoformat()
for key, fname, doi, ver, url, ok_rx, bad_rx in ITEMS:
    dest = os.path.join(BIB, fname)
    if os.path.exists(dest):
        log.append(f"| {key} | já presente | {fname} |")
        continue
    status = "falhou"
    for attempt in (1, 2):
        with tempfile.TemporaryDirectory() as td:
            tmp = os.path.join(td, "x.pdf")
            code = fetch(url, tmp)
            head = open(tmp, "rb").read(5) if os.path.exists(tmp) else b""
            if code.startswith("2") and head == b"%PDF-":
                txt = first_pages(tmp)
                if re.search(ok_rx, txt, re.I) and not (bad_rx and re.search(bad_rx, txt, re.I)):
                    with open(tmp, "rb") as fh:
                        data = fh.read()
                    with open(dest, "wb") as fh:
                        fh.write(data)
                    os.chmod(dest, 0o644)
                    manifest[fname] = {"key": key, "doi": doi, "versao": ver, "url": url,
                                       "sha256": hashlib.sha256(data).hexdigest(),
                                       "bytes": len(data), "baixado_em": today,
                                       "validacao": f"padrão de título /{ok_rx}/ nas páginas 1-2"}
                    status = f"ok (tentativa {attempt})"
                    break
                status = f"REPROVADO na validação de título (HTTP {code})"
            else:
                status = f"HTTP {code}, não é PDF"
    log.append(f"| {key} | {status} | {url} |")
log += [f"| MANUAL | subir pelo pesquisador | {n}, DOI {d} |" for n, d in MANUAL]
json.dump(manifest, open(man_path, "w"), indent=1, ensure_ascii=False, sort_keys=True)
with open(os.path.join(BIB, "DOWNLOAD_LOG.md"), "a", encoding="utf-8") as fh:
    fh.write(f"\n## {today} (resolução pós-inspeção)\n| item | resultado | origem |\n|---|---|---|\n"
             + "\n".join(log) + "\n")
print("\n".join(log))
