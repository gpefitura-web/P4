#!/usr/bin/env python3
"""Baixa PDFs do arXiv e BibTeX do ADS para as referências do lote atual."""
import difflib
import hashlib
import io
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "referencias"
PEND = REFS / "_pendentes"
BIB = REFS / "bib"
ADS = "https://api.adsabs.harvard.edu/v1"
TOKEN = os.environ.get("ADS_DEV_KEY", "").strip()
HEAD = {"Authorization": f"Bearer {TOKEN}"}
MIN_BYTES = 50_000


def norm(t):
    return re.sub(r"[^a-z0-9 ]", " ", re.sub(r"<[^>]+>", "", t).lower()).split()


def sim(a, b):
    return difflib.SequenceMatcher(None, " ".join(norm(a)), " ".join(norm(b))).ratio()


def ads_query(q):
    r = requests.get(f"{ADS}/search/query", headers=HEAD, timeout=60, params={
        "q": q, "rows": 5, "fl": "bibcode,title,author,year,pub,volume,page,identifier,doi,doctype,esources"})
    r.raise_for_status()
    return r.json()["response"]["docs"]


def ads_search(entry):
    if entry.get("bibcode"):
        docs = ads_query(f'bibcode:"{entry["bibcode"]}"')
        if docs:
            entry["title"] = docs[0]["title"][0]
            return docs[0], 1.0, docs
        return None, 0, []
    fa, yr = entry["first_author"], entry["year"]
    docs = ads_query(f'first_author:"{fa}" year:{yr} title:"{entry["title"]}"')
    if not docs:
        words = sorted({w for w in norm(entry["title"]) if len(w) > 4}, key=len, reverse=True)[:3]
        docs = ads_query(f'first_author:"{fa}" year:{yr} title:({" ".join(words)})')
    best, score = None, 0
    for d in docs:
        if d.get("doctype") not in ("article", "eprint", "inproceedings", "book", None):
            continue
        s = sim(entry["title"], d["title"][0])
        if s > score:
            best, score = d, s
    return best, score, docs


def arxiv_id(doc):
    for i in doc.get("identifier", []):
        m = re.match(r"arXiv:(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})$", i)
        if m:
            return m.group(1)
    return None


def validate_pdf(data, title, tokens=None):
    if not data.startswith(b"%PDF"):
        return False, "não começa com %PDF"
    if len(data) < MIN_BYTES:
        return False, f"muito pequeno ({len(data)} B)"
    pages = PdfReader(io.BytesIO(data)).pages
    text = " ".join((p.extract_text() or "") for p in pages[:2]).lower()
    if len(text.strip()) < 200:
        return False, "SEM TEXTO (scan): conferir visualmente"
    toks = tokens or [t for t in norm(title) if len(t) > 3]
    hit = sum(t.lower() in text for t in toks) / max(len(toks), 1)
    if hit < 0.8:
        return False, f"título não confere nas páginas 1-2 ({hit:.0%})"
    return True, f"título confere ({hit:.0%})"


def ads_bibtex(bibcode, bibkey):
    r = requests.post(f"{ADS}/export/bibtex", headers=HEAD, timeout=60, json={"bibcode": [bibcode]})
    r.raise_for_status()
    txt = r.json()["export"].strip()
    return re.sub(r"^(@\w+\{)[^,]+,", rf"\1{bibkey},", txt, count=1)


def get_pdf(entry, doc, aid, k, log):
    """Devolve (bytes, origem) ou (None, None)."""
    fonte = entry.get("fonte", "arxiv")
    if fonte == "manual":
        p = REFS / f"{k}.pdf"
        if not p.exists():
            log.append(f"- {k}: PDF manual ausente")
            return None, None
        return p.read_bytes(), "manual (Portal CAPES)"
    if fonte in ("ads_scan", "pub_pdf"):
        tipo = "ADS_PDF" if fonte == "ads_scan" else "PUB_PDF"
        url = f"https://ui.adsabs.harvard.edu/link_gateway/{doc['bibcode']}/{tipo}"
        origem = "ADS scan" if fonte == "ads_scan" else "PDF do editor via ADS"
    else:
        if not aid:
            log.append(f"- {k}: {doc['bibcode']} sem arXiv no ADS -> não baixado, NÃO citável (REG-R2)")
            return None, None
        url, origem = f"https://arxiv.org/pdf/{aid}", f"arXiv:{aid}"
        time.sleep(3)
    r = requests.get(url, timeout=120, headers={"User-Agent": "refs-fetch/1.0", **(HEAD if fonte in ("ads_scan", "pub_pdf") else {})},
                     allow_redirects=True)
    if r.status_code != 200:
        log.append(f"- {k}: {origem} HTTP {r.status_code}")
        return None, None
    return r.content, origem


def process(entry, log):
    k = entry["bibkey"]
    doc, score, cands = ads_search(entry)
    if not doc or score < 0.9:
        log.append(f"- {k}: FALHA ADS (melhor similaridade {score:.2f}); candidatos: "
                   + "; ".join(f'{d["bibcode"]}|{d["title"][0][:60]}' for d in cands))
        return None
    aid = arxiv_id(doc)
    rec = {"bibkey": k, "bibcode": doc["bibcode"], "ads_title": doc["title"][0],
           "year": doc["year"], "pub": doc.get("pub"), "arxiv": aid}
    data, origem = get_pdf(entry, doc, aid, k, log)
    if data is None:
        return None
    ok, why = validate_pdf(data, entry["title"], entry.get("validar_com"))
    if not ok and why.startswith("SEM TEXTO") and entry.get("validacao_visual"):
        ok, why = True, "scan sem texto; conferido visualmente (pág. 1: título e autores)"
    if not ok:
        PEND.mkdir(parents=True, exist_ok=True)
        (PEND / f"{k}.pdf").write_bytes(data)
        log.append(f"- {k}: REPROVADO ({why}) -> _pendentes/ ({origem})")
        return None
    REFS.mkdir(exist_ok=True)
    BIB.mkdir(exist_ok=True)
    (REFS / f"{k}.pdf").write_bytes(data)
    (BIB / f"{k}.bib").write_text(ads_bibtex(doc["bibcode"], k) + "\n")
    rec.update(sha256=hashlib.sha256(data).hexdigest(), bytes=len(data), origem=origem, validacao=why)
    log.append(f"- {k}: OK {doc['bibcode']} {origem} ({why}, {len(data)//1024} kB)")
    return rec


def resolve(todo, batch):
    out = [f"# Resolução ADS — lote {batch} ({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC)",
           "Nenhum PDF baixado. Conferir cada linha antes de aprovar (REG-R7).", "",
           "| bibkey | similaridade | bibcode | arXiv | DOI | acesso (ADS) | título no ADS |",
           "|---|---|---|---|---|---|---|"]
    for e in todo:
        try:
            doc, score, cands = ads_search(e)
        except Exception as exc:
            out.append(f"| {e['bibkey']} | ERRO | {exc} | | | | |")
            continue
        if not doc:
            out.append(f"| {e['bibkey']} | 0 | NÃO ENCONTRADO | | | | |")
            continue
        out.append("| {} | {:.2f} | {} | {} | {} | {} | {} |".format(
            e["bibkey"], score, doc["bibcode"], arxiv_id(doc) or "-",
            (doc.get("doi") or ["-"])[0], ",".join(doc.get("esources", [])) or "-",
            doc["title"][0][:80]))
        if True:
            for d in cands[:4]:
                out.append(f"|  ↳ candidato | {sim(e['title'], d['title'][0]):.2f} | {d['bibcode']} | {arxiv_id(d) or '-'} | | | {d['title'][0][:80]} |")
        time.sleep(0.5)
    REFS.mkdir(exist_ok=True)
    (REFS / f"RESOLVE_{batch}.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


def metadados(bibcodes):
    out = [f"# Metadados ADS — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC", ""]
    for bc in bibcodes:
        r = requests.get(f"{ADS}/search/query", headers=HEAD, timeout=60, params={
            "q": f'bibcode:"{bc}"', "fl": "bibcode,title,author,abstract,doi,identifier,pub,pubdate,volume,page,doctype,property,esources,comment"})
        docs = r.json()["response"]["docs"]
        out.append(f"## {bc}")
        out.append(json.dumps(docs[0] if docs else "NÃO ENCONTRADO", indent=1, ensure_ascii=False))
        # relações (erratum <-> artigo)
        rr = requests.get(f"{ADS}/search/query", headers=HEAD, timeout=60, params={
            "q": f'identifier:"{bc}" OR references(bibcode:"{bc}")', "fl": "bibcode,title,doctype", "rows": 5})
        out.append("relacionados: " + json.dumps(rr.json().get("response", {}).get("docs", []), ensure_ascii=False))
        out.append("")
    (REFS / "METADADOS_ADS.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


def verificar(chaves):
    mf = json.loads((REFS / "MANIFEST.json").read_text())
    if chaves == "todos":
        chaves = list(mf)
    out = [f"# Verificação de publicação (ADS) — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC", "",
           "| bibkey | bibcode | refereed | tipo | periódico | data | vol | pág | DOI |", "|---|---|---|---|---|---|---|---|---|"]
    for k in chaves:
        bc = mf[k]["bibcode"]
        docs = ads_query(f'bibcode:"{bc}"')
        d = docs[0] if docs else {}
        r = requests.get(f"{ADS}/search/query", headers=HEAD, timeout=60, params={
            "q": f'bibcode:"{bc}"', "fl": "bibcode,property,doctype,pub,pubdate,volume,page,doi,title,esources"})
        d = r.json()["response"]["docs"][0]
        out.append("| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            k, d["bibcode"], "sim" if "REFEREED" in d.get("property", []) else "NÃO",
            d.get("doctype"), d.get("pub"), d.get("pubdate"), d.get("volume"),
            (d.get("page") or ["-"])[0], (d.get("doi") or ["-"])[0]))
    (REFS / "VERIFICACAO_PUBLICACAO.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


def buscar(consultas):
    out = [f"# Busca ADS — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC", ""]
    for q in consultas:
        r = requests.get(f"{ADS}/search/query", headers=HEAD, timeout=60, params={
            "q": q, "rows": 6, "fl": "bibcode,title,author,year,pub,identifier,doi,esources", "sort": "citation_count desc"})
        docs = r.json().get("response", {}).get("docs", [])
        out.append(f"## {q}")
        for d in docs:
            ax = [i for i in d.get("identifier", []) if i.startswith("arXiv:")]
            out.append("- {} | {} | {} | {} | {} | {}".format(d["bibcode"], d["title"][0][:90], "; ".join(d.get("author", [])[:2]), d.get("pub"), ax[:1], ",".join(d.get("esources", []))))
        out.append("")
    (REFS / "BUSCA_ADS.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


def paginas(urls):
    """Baixa páginas web (HTML->texto) e PDFs de normas para referencias/web/."""
    outdir = REFS / "web"
    outdir.mkdir(parents=True, exist_ok=True)
    log = []
    for u in urls:
        nome = re.sub(r"[^A-Za-z0-9]+", "_", u.split("://")[1])[:90]
        try:
            r = requests.get(u, timeout=120, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) refs-fetch/1.0"})
        except Exception as exc:
            log.append(f"- {u}: ERRO {exc}")
            continue
        if r.status_code != 200:
            log.append(f"- {u}: HTTP {r.status_code}")
            continue
        if r.content.startswith(b"%PDF"):
            (outdir / f"{nome}.pdf").write_bytes(r.content)
            log.append(f"- {u}: PDF OK ({len(r.content)//1024} kB)")
            continue
        html = r.text
        links = sorted(set(re.findall(r'href="([^"]+)"', html)))
        txt = re.sub(r"(?is)<(script|style).*?</\1>", " ", html)
        txt = re.sub(r"<[^>]+>", "\n", txt)
        txt = re.sub(r"\n\s*\n+", "\n", txt)
        captcha = "captcha" in html.lower()[:3000]
        (outdir / f"{nome}.txt").write_text(f"URL: {u}\n\n{txt}\n\n=== LINKS ===\n" + "\n".join(links))
        log.append(f"- {u}: HTML OK ({len(txt)} caracteres){' [CAPTCHA]' if captcha else ''}")
    with open(REFS / "DOWNLOAD_LOG.md", "a") as f:
        f.write(f"\n## Páginas web — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n" + "\n".join(log) + "\n")
    print("\n".join(log))


def cfg_modo():
    return yaml.safe_load((ROOT / "scripts/refs_list.yml").read_text()).get("modo")


def vizier_readme(cats):
    """Salva apenas ReadMe e listagem de diretório do CDS (nenhum dado)."""
    base = "https://cdsarc.cds.unistra.fr/ftp/cats/"
    outdir = REFS / "vizier"
    outdir.mkdir(parents=True, exist_ok=True)
    log = []
    for c in cats:
        tag = c.replace("/", "_")
        for nome, url in (("ReadMe", f"{base}{c}/ReadMe"), ("DIRLIST", f"{base}{c}/")):
            r = requests.get(url, timeout=120, headers={"User-Agent": "refs-fetch/1.0"})
            if r.status_code == 200:
                (outdir / f"{tag}_{nome}.txt").write_text(r.text)
                log.append(f"- {c}: {nome} OK ({len(r.text)} caracteres)")
            else:
                log.append(f"- {c}: {nome} HTTP {r.status_code} ({url})")
    with open(REFS / "DOWNLOAD_LOG.md", "a") as f:
        f.write(f"\n## VizieR ReadMe — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n" + "\n".join(log) + "\n")
    print("\n".join(log))


def main():
    if cfg_modo() in ("readme", "ambos"):
        cfg1 = yaml.safe_load((ROOT / "scripts/refs_list.yml").read_text())
        if cfg1.get("paginas"):
            paginas(cfg1["paginas"])
        cfg0 = yaml.safe_load((ROOT / "scripts/refs_list.yml").read_text())
        vizier_readme(cfg0.get("vizier", []))
        if cfg_modo() == "readme":
            return
    if not TOKEN:
        sys.exit("ADS_DEV_KEY ausente: sem token não há BibTeX (REG-R6)")
    cfg = yaml.safe_load((ROOT / "scripts/refs_list.yml").read_text())
    todo = [e for e in cfg["refs"] if e["batch"] == cfg["batch_atual"]]
    if cfg.get("modo") == "ambos":
        if cfg.get("verificar"):
            verificar(cfg["verificar"])
        if cfg.get("metadados"):
            metadados(cfg["metadados"])
        if cfg.get("consultas"):
            buscar(cfg["consultas"])
        cfg["modo"] = "baixar"
    if cfg.get("modo") == "verificar":
        return verificar(cfg.get("verificar", []))
    if cfg.get("modo") == "resolver":
        return resolve(todo, cfg["batch_atual"])
    mf_path = REFS / "MANIFEST.json"
    manifest = json.loads(mf_path.read_text()) if mf_path.exists() else {}
    log = []
    for e in todo:
        if e["bibkey"] in manifest:
            log.append(f"- {e['bibkey']}: já baixado, ignorado")
            continue
        rec = process(e, log)
        if rec:
            manifest[e["bibkey"]] = rec
    REFS.mkdir(exist_ok=True)
    mf_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
    with open(REFS / "DOWNLOAD_LOG.md", "a") as f:
        f.write(f"\n## Lote {cfg['batch_atual']} — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n")
        f.write("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()
