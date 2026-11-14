"""Hook (REG-MAC): acusa números soltos na prosa de manuscrito/main.tex (depois de \\begin{document}) e de sec_*.tex que não vêm de macro.

Ative em kit.yml: verificacao.extra: [numeros_via_macro]. Aceita números de 1 dígito, anos (19xx/20xx), referências a
figuras/tabelas/equações e itens dentro de matemática. É uma heurística: revise os avisos, não os ignore.
"""
import re
from pathlib import Path

PROSA = re.compile(r"\$[^$\n]*\$|\\[A-Za-z]+\*?(\[[^\]]*\])*(\{[^}]*\})?")


def check(root):
    out = []
    files = sorted((Path(root) / "manuscrito").glob("sec_*.tex")) + [Path(root) / "manuscrito" / "main.tex"]
    for p in files:
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        first = 1
        if p.name == "main.tex" and "\\begin{document}" in text:
            first = text.split("\\begin{document}")[0].count("\n") + 2
        for n, line in enumerate(text.split("\n"), 1):
            if n < first:
                continue
            line = re.sub(r"(?<!\\)%.*$", "", line)
            line = PROSA.sub(" ", line)
            for m in re.finditer(r"(?<![\w.])\d+(?:[.,]\d+)?(?![\w])", line):
                tok = m.group(0)
                if len(tok.replace(".", "").replace(",", "")) <= 1 or re.fullmatch(r"(19|20)\d\d", tok):
                    continue
                out.append(f"{p.name}:{n}: número fora de macro: {tok}")
    return out
