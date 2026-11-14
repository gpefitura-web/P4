"""Stage 2a - apply the 'instrucao de incorporacao' of DECISOES_D41_D54.md to a COPY of
the notebook and write inspecao/NOTEBOOK_proposta_D41_D54.md. The original is not touched.

Exactly four operations, as the instruction states:
  1. insert block A (§4c, D41-D54) after the existing §4b;
  2. replace the table of §5 with the table of block C;
  3. append the rows of block B to the table of §8;
  4. append the row of block D to the table of §9.
Nothing else is changed (see the preface written at the top of the output).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import re

from common import INSP, ROOT, check

# the notebook was edited after the inspection (incorporation, 2026-11-14); the proposal is rebuilt from the saved original
with open(os.path.join(INSP, "saidas", "notebook_original_2026-08-01.md"), encoding="utf-8") as fh:
    nb = fh.read()
with open(os.path.join(ROOT, "DECISOES_D41_D54.md"), encoding="utf-8") as fh:
    dec = fh.read()


def between(txt, start, end):
    a = txt.index(start)
    b = txt.index(end, a)
    return txt[a:b]


def table_rows(block):
    """Data rows of the first markdown table in block (header and rule dropped)."""
    rows = [ln for ln in block.splitlines() if ln.startswith("|")]
    return rows[2:]


blkA = between(dec, "### § 4c ·", "## B ·").rstrip().rstrip("-").rstrip()
blkA = blkA.replace("### § 4c ·", "## 4c ·", 1)
rowsB = table_rows(between(dec, "## B ·", "## C ·"))
tabC = [ln for ln in between(dec, "## C ·", "## D ·").splitlines() if ln.startswith("|")]
rowsD = table_rows(between(dec, "## D ·", "## E ·"))

# 1. §4c after §4b (i.e. immediately before the '---' that precedes §5)
s5 = nb.index("## 5 · Questões abertas")
sep = nb.rindex("---", 0, s5)
out = nb[:sep] + "---\n\n" + blkA + "\n\n" + nb[sep:]

# 2. replace the §5 table
s5 = out.index("## 5 · Questões abertas")
s6 = out.index("## 6 ·", s5)
sec5 = out[s5:s6]
old_tab = [ln for ln in sec5.splitlines() if ln.startswith("|")]
sec5_new = sec5.replace("\n".join(old_tab), "\n".join(tabC))
assert sec5_new != sec5
out = out[:s5] + sec5_new + out[s6:]

# 3. append B rows to the §8 table
s8 = out.index("## 8 · Questões **fechadas**")
s9 = out.index("## 9 · Log de entradas", s8)
sec8 = out[s8:s9]
last8 = [ln for ln in sec8.splitlines() if ln.startswith("|")][-1]
sec8_new = sec8.replace(last8, last8 + "\n" + "\n".join(rowsB), 1)
out = out[:s8] + sec8_new + out[s9:]

# 4. append D row to the §9 table
s9 = out.index("## 9 · Log de entradas")
sec9 = out[s9:]
last9 = [ln for ln in sec9.splitlines() if ln.startswith("|")][-1]
sec9_new = sec9.replace(last9, last9 + "\n" + "\n".join(rowsD), 1)
out = out[:s9] + sec9_new

preface = """<!--
PROPOSTA - gerada por inspecao/scripts/02_build_notebook_proposal.py. NAO e o caderno.
Copia de P4_RESEARCH_NOTEBOOK.md com a "instrucao de incorporacao" de DECISOES_D41_D54.md
aplicada literalmente: (1) §4c inserida apos a §4b; (2) tabela da §5 substituida pela de C;
(3) linhas de B acrescentadas a §8; (4) linha de D acrescentada a §9.
Nada mais foi alterado. O que a instrucao NAO cobre e continua como no original esta listado
em inspecao/RELATORIO_INSPECAO.md (achado I-18): cabecalho "Ultima entrada", §6
(itens bloqueados), §7 (papeis dos documentos e obrigacoes de Methods), a linha de DFA da §8,
e a perda da coluna "Subsidios" na tabela da §5.
-->
"""
with open(os.path.join(INSP, "NOTEBOOK_proposta_D41_D54.md"), "w", encoding="utf-8") as fh:
    fh.write(preface + out)

n = lambda rx, t: len(re.findall(rx, t, re.M))
check("2a-20", "decision headers in the proposed notebook (D01-D54 + D45b)", 55,
      n(r"^### D\d+b? — ", out), "DECISOES_D41_D54.md instruction")
check("2a-21", "Q rows in §5 of the proposed notebook", 11,
      n(r"^\| \*\*Q\d+\*\* \|", out), "DECISOES_D41_D54.md §C")
check("2a-22", "rows added to §8", 10, len(rowsB), "DECISOES_D41_D54.md §B")
check("2a-23", "rows added to §9", 1, len(rowsD), "DECISOES_D41_D54.md §D")
orig_lines = nb.splitlines()
new_lines = out.splitlines()
removed = [ln for ln in orig_lines if ln not in new_lines]
check("2a-24", "lines of the original notebook absent from the proposal (the 11 replaced "
      "lines of the §5 table: header, rule, Q1-Q9)", 11, len(removed),
      "diff P4_RESEARCH_NOTEBOOK.md NOTEBOOK_proposta_D41_D54.md")
