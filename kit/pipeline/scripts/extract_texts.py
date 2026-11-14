#!/usr/bin/env python3
"""Extrai o texto de todos os PDFs de referencias/ para um diretório de trabalho.

Uso: python3 -I scripts/extract_texts.py <diretorio_saida>
Cada arquivo de saída recebe marcadores '=====PAGE n=====' para citar páginas.
"""
import sys
from pathlib import Path
from pypdf import PdfReader

root = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
for pdf in sorted((root / "referencias").glob("*.pdf")):
    try:
        pages = PdfReader(pdf).pages
        with open(out / f"{pdf.stem}.txt", "w") as f:
            for i, p in enumerate(pages, 1):
                f.write(f"\n=====PAGE {i}=====\n" + (p.extract_text() or ""))
        print(pdf.stem, len(pages))
    except Exception as exc:
        print(pdf.stem, "erro", exc)
