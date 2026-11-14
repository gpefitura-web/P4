"""Assemble P4_RESEARCH_NOTEBOOK.md = proposal (original + D41-D54 incorporation) + additions of 2026-11-14.
Not part of run_all.sh: it writes the notebook. Run once with `python -I`."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import INSP, ROOT


def rd(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


nb = rd(os.path.join(INSP, "NOTEBOOK_proposta_D41_D54.md"))
nb = re.sub(r"\A<!--.*?-->\n", "", nb, flags=re.S)
A = os.path.join(INSP, "notebook_adicoes")
old = "**Última entrada:** 2026-08-01 (fecho da conversa de consolidação)"
assert old in nb
nb = nb.replace(old, "**Última entrada:** 2026-11-14 (inspeção e resolução; D55–D67)")
head = "## 5 · Questões abertas"
assert nb.count(head) == 1
nb = nb.replace(head, rd(os.path.join(A, "4d_D55_D67.md")).rstrip() + "\n\n---\n\n" + head)
i = nb.index("## 6 · Itens de ação")
j = nb.index("## 7 · Arquitetura")
nb = nb[:i] + rd(os.path.join(A, "6_blocos.md")).rstrip() + "\n\n---\n\n" + nb[j:]
k = nb.index("---\n\n## 8 · Questões")
nb = nb[:k].rstrip() + "\n" + rd(os.path.join(A, "7_extra.md")) + "\n" + nb[k:]
nb = nb.rstrip() + "\n" + rd(os.path.join(A, "9_log.md"))
nb = nb.rstrip() + "\n" + rd(os.path.join(A, "10_11.md"))
with open(os.path.join(ROOT, "P4_RESEARCH_NOTEBOOK.md"), "w", encoding="utf-8") as fh:
    fh.write(nb)
print("written", len(nb.splitlines()), "lines")
