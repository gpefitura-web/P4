"""Hook ordem_floats: figuras e tabelas citadas no texto na ordem em que aparecem (DEC-41 do P1_ext).

Ative em kit.yml: verificacao.extra: [eprime, ordem_floats].

Lê manuscrito/main.tex depois de \\begin{document}, expande \\input e \\include na ordem em que aparecem e confere, para
figuras e tabelas separadamente (ambientes figure, figure*, table, table*):
  1. todo float tem \\label e pelo menos uma citação (\\ref, \\autoref, \\cref, \\Cref, \\eqref não conta);
  2. a primeira citação de cada float vem antes da posição do float no texto;
  3. as primeiras citações seguem a ordem dos floats (o float 1 é citado antes do 2, e assim por diante);
  4. numa citação com vários rótulos (\\cref{a,b}) vale a ordem escrita;
  5. todo rótulo citado existe;
  6. se o arquivo de imagem se chama figure<N>, o N do k-ésimo float de figura é k (a numeração do notebook segue a ordem
     de citação do manuscrito); figuras depois de \\appendix têm numeração própria (Fig. A.1) e ficam fora desta regra.
Sem float no texto, o hook não acusa nada. Comentários ficam de fora.
"""
import re
from pathlib import Path

ENV = re.compile(r"\\begin\{(figure|table)\*?\}(.*?)\\end\{\1\*?\}", re.S)
LABEL = re.compile(r"\\label\{([^}]*)\}")
INCLUDE = re.compile(r"\\includegraphics\*?(?:\[[^\]]*\])?\{([^}]*)\}")
CITE = re.compile(r"\\(?:ref|autoref|cref|Cref|vref|cpageref)\*?\{([^}]*)\}")
INPUT = re.compile(r"\\(?:input|include)\{([^}]*)\}")


def _strip(text):
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def _expand(path, root, seen=()):
    """Texto de `path` com os \\input e \\include substituídos, na ordem."""
    try:
        text = _strip(path.read_text(encoding="utf-8", errors="ignore"))
    except OSError:
        return ""
    if path.name == "main.tex" and "\\begin{document}" in text:
        text = text.split("\\begin{document}", 1)[1]

    def sub(m):
        name = m.group(1)
        cand = root / (name if name.endswith(".tex") else name + ".tex")
        if cand in seen or not cand.exists():
            return ""
        return _expand(cand, root, seen + (cand,))
    return INPUT.sub(sub, text)


def check(root):
    ms = Path(root) / "manuscrito"
    main = ms / "main.tex"
    if not main.exists():
        return []
    text = _expand(main, ms, (main,))
    problems = []
    app = text.find("\\appendix")
    floats = {"figure": [], "table": []}
    for m in ENV.finditer(text):
        kind, body = m.group(1), m.group(2)
        lab = LABEL.search(body)
        inc = INCLUDE.search(body)
        floats[kind].append({"pos": m.start(), "label": lab.group(1) if lab else None,
                             "file": inc.group(1) if inc else None, "app": app >= 0 and m.start() > app})
    cites = {}
    for m in CITE.finditer(text):
        for k, lab in enumerate(x.strip() for x in m.group(1).split(",")):
            cites.setdefault(lab, m.start() + k * 1e-3)   # primeira posição; a ordem interna vale pelo acréscimo
    defined = {f["label"] for kind in floats.values() for f in kind if f["label"]}
    for lab in sorted(cites):
        if lab not in defined and (lab.startswith(("fig:", "tab:")) or lab.startswith(("fig", "tab"))):
            problems.append(f"manuscrito: citação de rótulo sem float definido: {lab}")
    for kind, nome in (("figure", "figura"), ("table", "tabela")):
        last = -1.0
        for k, f in enumerate(floats[kind], 1):
            lab = f["label"]
            if not lab:
                problems.append(f"manuscrito: {nome} {k} sem \\label")
                continue
            first = cites.get(lab)
            if first is None:
                problems.append(f"manuscrito: {nome} {k} ({lab}) nunca é citada no texto")
                continue
            if first > f["pos"]:
                problems.append(f"manuscrito: {nome} {k} ({lab}) aparece antes da primeira citação")
            if first < last:
                problems.append(f"manuscrito: {nome} {k} ({lab}) é citada antes da {nome} anterior (fora de ordem)")
            last = max(last, first)
            if kind == "figure" and f["file"] and not f.get("app"):
                n = re.search(r"figure(\d+)", Path(f["file"]).name)
                if n and int(n.group(1)) != k:
                    problems.append(f"manuscrito: {nome} {k} usa o arquivo {Path(f['file']).name}; "
                                    f"o número do arquivo deve ser {k} (ordem de citação)")
    return problems
