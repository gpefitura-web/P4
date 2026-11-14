"""Baixa as páginas de normas/template de uma revista e os arquivos de template ligados a elas.

Roda no GitHub Actions (o ambiente do chat costuma não alcançar os sites das revistas).
As fontes vêm de um YAML por revista (padrão: kit/revistas/<revista>/fontes.yml, com <revista>
lido de kit.yml), com as chaves:
  paginas: [URLs de páginas HTML a baixar em bruto]
  diretos: [URLs que devem ser tentadas como download direto, ex.: zip de template]
  inspecionar: [URLs de páginas cujos links para .zip/.cls/.bst/.doc/.pdf serão seguidos]
Grava tudo em manuscrito/template/ com manifesto de tamanhos e SHA-256 e um log legível.

Uso: python3 scripts/fetch_template.py [caminho/fontes.yml]
"""
import hashlib
import io
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
if len(sys.argv) > 1:
    SRC = Path(sys.argv[1])
else:
    cfg = yaml.safe_load((ROOT / "kit.yml").read_text(encoding="utf-8"))
    SRC = ROOT / "kit" / "revistas" / cfg["revista"] / "fontes.yml"
fontes = yaml.safe_load(SRC.read_text(encoding="utf-8"))

OUT = ROOT / "manuscrito" / "template"
PAGES = fontes.get("paginas", [])
INSPECT = fontes.get("inspecionar", [])
DIRECT = fontes.get("diretos", [])
EXT = (".zip", ".tex", ".cls", ".bst", ".sty", ".doc", ".docx", ".pdf", ".tar", ".gz")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}
MAX_BYTES = 30 * 1024 * 1024

log, manifest = [], []


def say(msg):
    print(msg)
    log.append(msg)


def get(url):
    return requests.get(url, headers=UA, timeout=90, allow_redirects=True)


(OUT / "paginas").mkdir(parents=True, exist_ok=True)
(OUT / "arquivos").mkdir(exist_ok=True)
links, seen = {}, set()
for i, url in enumerate(PAGES + INSPECT):
    try:
        r = get(url)
    except Exception as err:
        say(f"PAGINA falhou {url}: {err}")
        continue
    say(f"PAGINA {r.status_code} {url} ({len(r.content)} bytes)")
    (OUT / "paginas" / f"pagina{i}.html").write_bytes(r.content)
    if url in INSPECT or url in PAGES:
        for href in re.findall(r'href=["\']([^"\']+)["\']', r.text):
            full = urljoin(url, href.replace("&#038;", "&").replace("&amp;", "&"))
            low = full.lower().split("?")[0]
            if low.endswith(EXT):
                links.setdefault(full, url)
            elif ("overleaf" in low or "template" in low) and full not in PAGES + INSPECT and full not in seen:
                seen.add(full)
                say("  link de interesse (não baixado, conferir): " + full)

for extra in DIRECT:
    links.setdefault(extra, "download direto")
say(f"{len(links)} arquivos candidatos")
for full, origem in sorted(links.items()):
    say(f"LINK {full}  (em {origem})")
    low = full.lower().split("?")[0]
    try:
        r = get(full)
    except Exception as err:
        say(f"  falhou: {err}")
        continue
    ok = r.status_code == 200 and len(r.content) <= MAX_BYTES
    name = re.sub(r"[^A-Za-z0-9._-]", "_", low.rsplit("/", 1)[-1]) or "arquivo"
    entry = {"url": full, "status": r.status_code, "bytes": len(r.content), "arquivo": name if ok else None,
             "sha256": hashlib.sha256(r.content).hexdigest() if ok else None}
    manifest.append(entry)
    say(f"  {r.status_code} {len(r.content)} bytes")
    if not ok:
        continue
    (OUT / "arquivos" / name).write_bytes(r.content)
    if name.lower().endswith(".zip"):
        try:
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                dest = OUT / "extraido" / name[:-4]
                z.extractall(dest)
                say("  extraido em " + str(dest) + ": " + ", ".join(sorted(z.namelist())[:40]))
        except Exception as err:
            say(f"  zip invalido: {err}")

(OUT / "manifesto.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
(OUT / "LOG.md").write_text(f"# Download do template ({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC)\n\n" +
                            "\n".join("* " + m for m in log) + "\n", encoding="utf-8")
