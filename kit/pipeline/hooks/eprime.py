"""Hook E-Prime: acusa formas do verbo 'to be' na prosa em inglês de manuscrito/*.tex.

Ative em kit.yml: verificacao.extra: [eprime].

E-Prime é o inglês sem nenhuma palavra derivada de 'to be' (be, being, been, am, is, are, was, were e assim por diante).
A página de referência (gandhiviswanathan.wordpress.com, 2016-05-16) não trata de contrações. Aqui elas contam como formas
de 'is' e 'are', porque as contêm. A voz passiva sem 'to be' ('gets measured') não é proibida, mas a voz ativa com 'we' é
preferível.

Escopo: o texto depois de \\begin{document} em main.tex e em sec_*.tex, cover_letter.tex etc. Ficam fora comentários,
matemática, citações, referências cruzadas, rótulos, caminhos de arquivo e os nomes de comandos e ambientes do LaTeX. O
texto de legendas, títulos, resumo e texto alternativo de figuras entra na verificação.

Exceção rara e justificada: escreva '% eprime-ok' no fim da linha. Cada uso desse marcador deve constar em DECISIONS.md.
"""
import re
from pathlib import Path

FORMS = re.compile(r"\b(?:am|is|are|was|were|be|been|being)\b", re.I)
CONTRACTIONS = re.compile(
    r"\b(?:i['’]m|you['’]re|we['’]re|they['’]re|(?:he|she|it|that|there|here|what|who|where|how)['’]s|"
    r"(?:is|are|was|were)n['’]t|ain['’]t)\b", re.I)
SKIP_FILES = {"journal_macros.tex", "results_macros.tex", "results_extra.tex"}

DROP = [
    re.compile(r"\$\$.*?\$\$|\\\[.*?\\\]", re.S),
    re.compile(r"\\begin\{(?:equation|align|eqnarray|gather|multline)\*?\}.*?\\end\{(?:equation|align|eqnarray|gather|multline)\*?\}", re.S),
    re.compile(r"\$[^$]*\$"),
    re.compile(r"\\(?:cite[a-zA-Z]*|ref|eqref|label|input|include|includegraphics|bibliography|bibliographystyle|url|"
               r"graphicspath|DeclareGraphicsExtensions|newcommand|renewcommand|usepackage|documentclass)\*?(?:\[[^\]]*\])*(?:\{[^{}]*\})+"),
    re.compile(r"\\(?:begin|end)\{[^}]*\}"),
]
COMMAND = re.compile(r"\\[A-Za-z]+\*?")


def prose(text):
    if "\\begin{document}" in text:
        head, tail = text.split("\\begin{document}", 1)
        text = "\n" * head.count("\n") + tail
    for rx in DROP:
        text = rx.sub(lambda m: " " * len(m.group(0)) if "\n" not in m.group(0) else re.sub(r"[^\n]", " ", m.group(0)), text)
    return text


def scan_text(text, name):
    out = []
    raw = text.split("\n")
    stripped = [re.sub(r"(?<!\\)%.*$", "", l) for l in raw]
    body = prose("\n".join(stripped)).split("\n")
    for n, line in enumerate(body, 1):
        if "eprime-ok" in raw[n - 1] if n - 1 < len(raw) else False:
            continue
        line = COMMAND.sub(" ", line)
        for rx in (FORMS, CONTRACTIONS):
            for m in rx.finditer(line):
                out.append(f"{name}:{n}: forma de 'to be' (E-Prime): {m.group(0)}")
    return out


def check(root):
    out = []
    base = Path(root) / "manuscrito"
    for p in sorted(base.rglob("*.tex")):
        if "template" in p.parts or p.name in SKIP_FILES:
            continue
        out.extend(scan_text(p.read_text(encoding="utf-8", errors="ignore"), f"manuscrito/{p.relative_to(base)}"))
    return out
