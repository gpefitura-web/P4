"""Monta manuscrito/references.bib e verifica as referências citadas (regra REG-R6).

Para cada chave citada nos arquivos .tex de manuscrito/ (fora de template/), confere que existem
referencias/bib/<chave>.bib (exportado do ADS), referencias/<chave>.pdf e a entrada no MANIFEST.json.
Escreve references.bib na ordem de primeira citação e journal_macros.tex com as macros de periódico
que as entradas usam. Sai com código 1 se faltar algo.

Uso: python3 scripts/make_references_bib.py [pasta_do_manuscrito]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MS = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "manuscrito"
REFS = ROOT / "referencias"

JOURNALS = {
    "apj": "The Astrophysical Journal",
    "apjs": "The Astrophysical Journal Supplement Series",
    "apjl": "The Astrophysical Journal Letters",
    "aj": "The Astronomical Journal",
    "mnras": "Monthly Notices of the Royal Astronomical Society",
    "nat": "Nature",
    "physrep": "Physics Reports",
    "solphys": "Solar Physics",
    "ssr": "Space Science Reviews",
}
CITE = re.compile(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]+)\}")


def tex_files():
    return [p for p in sorted(MS.rglob("*.tex")) if "template" not in p.parts and p.name != "journal_macros.tex"]


def cited_keys():
    keys = []
    for p in tex_files():
        text = re.sub(r"(?m)(?<!\\)%.*$", "", p.read_text(encoding="utf-8", errors="ignore"))
        for m in CITE.finditer(text):
            for k in m.group(1).split(","):
                k = k.strip()
                if k and k not in keys:
                    keys.append(k)
    return keys


def main():
    keys = cited_keys()
    mf = REFS / "MANIFEST.json"
    manifest = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else {}
    problems, entries, macros = [], [], set()
    for k in keys:
        bib = REFS / "bib" / f"{k}.bib"
        if not bib.exists():
            problems.append(f"{k}: sem BibTeX do ADS em referencias/bib")
            continue
        if not (REFS / f"{k}.pdf").exists():
            problems.append(f"{k}: sem PDF em referencias (regra REG-R2)")
        if k not in manifest:
            problems.append(f"{k}: fora do MANIFEST.json")
        text = bib.read_text(encoding="utf-8").strip()
        entries.append(text)
        macros.update(re.findall(r"journal\s*=\s*\{\\([a-z]+)\}", text))
    MS.mkdir(exist_ok=True)
    (MS / "references.bib").write_text("\n\n".join(entries) + ("\n" if entries else ""), encoding="utf-8")
    lines = ["% Macros de periodico usadas nas entradas do ADS. Gerado por scripts/make_references_bib.py."]
    for m in sorted(macros):
        if m not in JOURNALS:
            problems.append(f"macro de periodico desconhecida: \\{m}")
            continue
        lines.append("\\providecommand{\\" + m + "}{" + JOURNALS[m] + "}")
    (MS / "journal_macros.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(keys)} chaves citadas, {len(entries)} entradas escritas em {MS / 'references.bib'}")
    uncited = sorted(p.stem for p in (REFS / "bib").glob("*.bib") if p.stem not in keys)
    print(f"{len(uncited)} referências da coleção não citadas (informativo)")
    for p in problems:
        print("PROBLEMA:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
