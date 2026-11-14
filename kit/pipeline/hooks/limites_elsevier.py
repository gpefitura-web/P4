"""Hook limites_elsevier: limites do guia de autores da New Astronomy (Elsevier), conferidos depois de expandir os macros.

Ative em kit.yml: verificacao.extra: [..., limites_elsevier]. Confere em manuscrito/main.tex:
  - resumo (ambiente abstract) com no máximo 250 palavras (guia, p6);
  - destaques (ambiente highlights) com 3 a 5 itens de no máximo 85 caracteres cada, com espaços (guia, p6);
  - palavras-chave (ambiente keyword) em número de 1 a 7 (guia, p6).
Os macros \\Nome vêm de results_macros.tex e results_extra.tex. Sem os ambientes (placeholders), o hook não acusa nada.
"""
import re
from pathlib import Path


def _macros(ms):
    m = {}
    for f in ("results_macros.tex", "results_extra.tex"):
        p = ms / f
        if p.exists():
            for name, val in re.findall(r"\\newcommand\{\\([A-Za-z]+)\}\{([^}]*)\}", re.sub(r"(?m)(?<!\\)%.*$", "", p.read_text(encoding="utf-8", errors="ignore"))):
                m[name] = val
    return m


def _plain(text, macros):
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    text = re.sub(r"\\([A-Za-z]+)\\?(?![A-Za-z])", lambda x: macros.get(x.group(1), ""), text)
    text = re.sub(r"\$[^$]*\$", "x", text)
    text = text.replace("\\,", " ").replace("~", " ")
    text = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", text)
    return re.sub(r"[{}]", "", text)


def check(root):
    ms = Path(root) / "manuscrito"
    main = ms / "main.tex"
    if not main.exists():
        return []
    t = main.read_text(encoding="utf-8", errors="ignore")
    mac = _macros(ms)
    out = []
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", t, re.S)
    if m and "[E9b" not in m.group(1):
        n = len(_plain(m.group(1), mac).split())
        if n > 250:
            out.append(f"manuscrito: resumo com {n} palavras (limite 250)")
    m = re.search(r"\\begin\{highlights\}(.*?)\\end\{highlights\}", t, re.S)
    if m:
        items = [i.strip() for i in re.split(r"\\item", m.group(1)) if i.strip()]
        if not 3 <= len(items) <= 5:
            out.append(f"manuscrito: {len(items)} destaques (o guia pede de 3 a 5)")
        for i in items:
            s = re.sub(r"\s+", " ", _plain(i, mac)).strip()
            if len(s) > 85:
                out.append(f"manuscrito: destaque com {len(s)} caracteres (limite 85): {s[:40]}...")
    m = re.search(r"\\begin\{keyword\}(.*?)\\end\{keyword\}", t, re.S)
    if m:
        n = len([k for k in re.split(r"\\sep", m.group(1)) if k.strip()])
        if not 1 <= n <= 7:
            out.append(f"manuscrito: {n} palavras-chave (o guia pede de 1 a 7)")
    return out
