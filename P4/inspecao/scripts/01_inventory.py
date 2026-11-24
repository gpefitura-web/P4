"""Stages 1 and 2 (mechanical part) - inventory, broken references, D##/Q#/F# bookkeeping.

Writes saidas/01_inventory.txt and appends summary rows to checks.csv.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import hashlib
import json
import re
from collections import defaultdict

from common import INSP, ROOT, check, write_out

REPO = os.path.dirname(ROOT)
out = []


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


# ---- file inventory ------------------------------------------------------
pkg = []
for d, dirs, files in os.walk(ROOT):
    dirs[:] = [x for x in dirs if not (os.path.join(d, x) == INSP)]
    for f in files:
        pkg.append(os.path.relpath(os.path.join(d, f), ROOT))
pkg.sort()
out.append("## Package files (relative to the package root)")
for f in pkg:
    p = os.path.join(ROOT, f)
    out.append(f"{os.path.getsize(p):>10}  {sha(p)[:16]}  {f}")
check("1-01", "files in the package (inspecao/ excluded)", "", len(pkg), "inventory", info=True)

# duplicates in the repository root
out.append("\n## Repository-root copies")
same = diff = 0
TSV = {"J_AJ_163_183_table1.tsv": "J:AJ:163:183:table1.tsv",
       "J_163_183_table2.tsv": "J:163:183:table2.tsv",
       "J_ApJ_936_L23_table2.tsv": "J:ApJ:936:L23:table2.tsv",
       "J_ApJ_936_L23_table3.tsv": "J:ApJ:936:L23:table3.tsv",
       "J_ApJS_274_35_table2.tsv": "J:ApJS:274:35:table2.tsv",
       "J_ApJS_274_35_table3.tsv": "J:ApJS:274:35:table3.tsv",
       "J_ApJS_274_35_table4.tsv": "J:ApJS:274:35:table4.tsv"}  # README_HANDOFF.md table
only_pkg = []
for f in pkg:
    base = os.path.basename(f)
    cand = os.path.join(REPO, TSV.get(base, base)) if f.startswith("data/") else os.path.join(REPO, f)
    if os.path.isfile(cand):
        eq = sha(cand) == sha(os.path.join(ROOT, f))
        same += eq
        diff += not eq
        out.append(f"{'IDENTICAL' if eq else 'DIFFERENT'}  {f}  <->  {os.path.relpath(cand, REPO)}")
    else:
        only_pkg.append(f)
out.append("only in the package: " + ", ".join(only_pkg))
root_files = sorted(f for f in os.listdir(REPO) if os.path.isfile(os.path.join(REPO, f)))
pdfs = [f for f in root_files if f.lower().endswith(".pdf")]
out.append("PDFs in the repository root: " + " | ".join(pdfs))
check("1-02", "package files with a byte-identical copy in the repository root", "", same,
      "sha256", info=True)
check("1-03", "package files whose repository-root copy differs", 0, diff, "sha256")
check("1-04", "VizieR TSVs in data/ matched to the ':' names of README_HANDOFF.md", 7,
      sum(1 for f in pkg if f.startswith("data/") and os.path.basename(f) in TSV),
      "README_HANDOFF.md 'Nomes dos TSVs'")
check("1-05", "PDFs in the repository root", 9, len(pdfs),
      "P4_AUDIT_PROTOCOL.md §2 ('Nine PDFs')")
check("1-06", "PDFs in bib/ (README_HANDOFF.md: none at hand-off; PDFs were added to bib/ "
      "during the inspection, see RELATORIO_INSPECAO.md §6)", 0,
      len([f for f in pkg if f.startswith("bib/") and f.lower().endswith(".pdf")]),
      "README_HANDOFF.md", info=True)

# ---- text corpus ---------------------------------------------------------
docs = {}
for f in pkg:
    if f.endswith(".md"):
        with open(os.path.join(ROOT, f), encoding="utf-8") as fh:
            docs[f] = fh.read()
with open(os.path.join(ROOT, "p4_pipeline.ipynb"), encoding="utf-8") as fh:
    nb = json.load(fh)
docs["p4_pipeline.ipynb"] = "\n".join("".join(c["source"]) for c in nb["cells"])

# ---- referenced file names ----------------------------------------------
pat = re.compile(r"`([^`\s]+\.(?:md|csv|tsv|pdf|ipynb|py|tex|txt|yml))`")
refs = defaultdict(set)
for name, txt in docs.items():
    for m in pat.finditer(txt):
        refs[m.group(1)].add(name)
have = set(pkg) | {os.path.basename(f) for f in pkg}
colon = {v: k for k, v in TSV.items()}
missing = {}
for r, where in sorted(refs.items()):
    base = os.path.basename(r)
    if r in have or base in have:
        # exists, but maybe under another folder than the one cited
        if r not in pkg and "/" in r:
            actual = [f for f in pkg if os.path.basename(f) == base]
            missing[r] = ("CITED PATH DIFFERS, file is at " + ",".join(actual), where)
        continue
    if base in colon:
        continue
    in_root = os.path.isfile(os.path.join(REPO, base))
    missing[r] = ("ABSENT from package" + (" (present in repository root)" if in_root else ""),
                  where)
out.append("\n## File names cited in the documents and not found at the cited place")
for r, (st, where) in missing.items():
    out.append(f"{r}: {st}  <- cited in {', '.join(sorted(where))}")
absent = [r for r, (st, _) in missing.items() if st.startswith("ABSENT")]
check("1-07", "distinct file names cited (in backticks) and absent from the package", "",
      len(absent), "regex over all .md and the notebook", info=True)
KNOWN = ["P4_DECISION_SUPPORT_6.1.md", "COWORK_PROMPT_A9_A12.md", "P4_SOURCE_VALUES.md",
         "p4_star_catalog.csv", "audit/A7_theory.md", "audit/A8_usoskin.md"]
# audit/A7 and A8 were executed during the inspection (not absent any more); the other four stay absent
KNOWN = KNOWN[:4]
check("1-08", "files listed as missing at hand-off (minus A7/A8, executed since) confirmed absent", len(KNOWN),
      sum(1 for k in KNOWN if not os.path.exists(os.path.join(ROOT, k))),
      "README_HANDOFF.md 'O que ficou de fora'")
check("1-09", "bib/aa28479-16.pdf (Olah+2016) anywhere in the clone", "absent",
      "present" if any("aa28479" in f for d, _, fs in os.walk(REPO) for f in fs) else "absent",
      "README_HANDOFF.md; audit/A10_luhn.md §6 says 'Esta em bib/ e disponivel'")

# ---- decisions -----------------------------------------------------------
defs = defaultdict(list)
for name in ("P4_RESEARCH_NOTEBOOK.md",):
    for m in re.finditer(r"^### (D\d+b?) — (.*)$", docs[name], re.M):
        blk = docs[name][m.end(): m.end() + 600]
        st = re.search(r"\*\*Status:\*\*\s*([^·\n]+)", blk)
        defs[m.group(1)].append((name, st.group(1).strip() if st else "NO STATUS"))
allD = [f"D{i:02d}" for i in range(1, 92)]
check("2a-01", "decisions D01-D91 defined exactly once in the notebook", 91,
      sum(1 for d in allD if len(defs.get(d, [])) == 1), "notebook + DECISOES_D41_D54.md")
check("2a-02", "decisions defined more than once or missing", "none",
      ",".join(d for d in allD if len(defs.get(d, [])) != 1) or "none",
      "notebook + DECISOES_D41_D54.md")
check("2a-03", "decision headers outside D01-D91 numbering", "",
      ",".join(sorted(set(defs) - set(allD))) or "none", "DECISOES_D41_D54.md", info=True)
nostat = [d for d, v in defs.items() if any(s == "NO STATUS" for _, s in v)]
check("2a-04", "decisions without a 'Status' field", "none", ",".join(nostat) or "none",
      "notebook + DECISOES_D41_D54.md")
stat = defaultdict(list)
for d, v in defs.items():
    stat[v[0][1]].append(d)
check("2a-05", "status values in use", "", "; ".join(f"{k}: {len(v)}" for k, v in stat.items()),
      "notebook + DECISOES_D41_D54.md", info=True)
nograde = []
for name in ("P4_RESEARCH_NOTEBOOK.md",):
    for m in re.finditer(r"^### (D\d+b?) — .*\n(.*)$", docs[name], re.M):
        if "Grau" not in m.group(2):
            nograde.append(m.group(1))
check("2a-06", "decisions whose header line carries no 'Grau' field", "", len(nograde),
      "notebook + DECISOES_D41_D54.md", info=True)
out.append("\n## Decisions without a grade field: " + ",".join(nograde))
dref = defaultdict(set)
for name, txt in docs.items():
    for m in re.finditer(r"\bD(\d{2})(b?)\b", txt):
        dref["D" + m.group(1) + m.group(2)].add(name)
    for m in re.finditer(r"\bD(\d{2})[–-]D?(\d{2})\b", txt):
        for i in range(int(m.group(1)), int(m.group(2)) + 1):
            dref[f"D{i:02d}"].add(name)
orphan = sorted(d for d in dref if d not in defs)
check("2a-07", "D## referenced anywhere but not defined", "none", ",".join(orphan) or "none",
      "regex over all .md and the notebook")
if orphan:
    out.append("orphan D refs: " + "; ".join(f"{d} in {sorted(dref[d])}" for d in orphan))
unref = sorted(d for d in defs if not (dref[d] - {"P4_RESEARCH_NOTEBOOK.md"} if d <= "D40"
                                        else dref[d] - {"DECISOES_D41_D54.md"}))
check("2a-08", "decisions never cited outside the document that defines them", "",
      ",".join(unref) or "none", "regex", info=True)
nbk = docs["P4_RESEARCH_NOTEBOOK.md"]
check("2a-09", "D41-D54 present in P4_RESEARCH_NOTEBOOK.md (absent at hand-off; incorporated 2026-11-14)", 14,
      sum(1 for i in range(41, 55) if re.search(rf"^### D{i}\b", nbk, re.M)),
      "README_HANDOFF.md 'Pendencia de documentacao'")
dd = docs["DECISOES_D41_D54.md"]
same = sum(1 for i in range(41, 55)
           if (re.search(rf"^### D{i} — .*$", dd, re.M) or [None])[0] == (re.search(rf"^### D{i} — .*$", nbk, re.M) or [""])[0])
check("2a-13", "D41-D54 header lines identical in notebook and DECISOES_D41_D54.md", 14, same,
      "P4_RESEARCH_NOTEBOOK.md §4c vs DECISOES_D41_D54.md")
check("2a-10", "Q10 / Q11 present in notebook §5", "yes/yes",
      "/".join("yes" if re.search(rf"\*\*Q{i}\*\*", nbk) else "no" for i in (10, 11)),
      "README_HANDOFF.md 'Pendencia de documentacao'")
check("2a-11", "notebook log (§9) has a D41-D54 line", "yes",
      "yes" if "D41–D54" in nbk.split("## 9 ·")[1] else "no", "DECISOES_D41_D54.md §D")
check("2a-12", "rows in notebook §8 (closed questions)", "",
      len([ln for ln in nbk.split("## 8 ·")[1].split("## 9 ·")[0].splitlines()
           if ln.startswith("|") and not ln.startswith("|---") and "Questão" not in ln]),
      "P4_RESEARCH_NOTEBOOK.md §8", info=True)

# ---- findings F# ---------------------------------------------------------
fdef = defaultdict(set)
for name, txt in docs.items():
    m = re.match(r"audit/A(\d+)_", name)
    if not m:
        continue
    unit = m.group(1)
    for f in re.finditer(r"^\*\*F(\d+) —", txt, re.M):
        fdef["A" + unit].add(int(f.group(1)))
    for f in re.finditer(r"^\*\*A(\d+)([ab]?)-F(\d+) ·", txt, re.M):
        fdef["A" + f.group(1) + f.group(2)].add(int(f.group(3)))
out.append("\n## Findings defined per unit")
for u in sorted(fdef, key=lambda x: (int(re.sub(r"\D", "", x)), x)):
    out.append(f"{u}: F{min(fdef[u])}-F{max(fdef[u])} ({len(fdef[u])})")
exp_counts = {"A9": 10, "A10": 7, "A12": 7}
for i, (u, n) in enumerate(exp_counts.items()):
    check(f"2d-0{i+1}", f"findings defined in {u}", n, len(fdef[u]), "paper_state_v6.md §10")
check("2d-04", "findings defined in A11 (A11a + A11b)", 9, len(fdef["A11a"]) + len(fdef["A11b"]),
      "paper_state_v6.md §10")
for i, (u, n) in enumerate({"A1": 9, "A2": 7, "A3": 6, "A4": 8, "A5": 6, "A6": 14}.items()):
    check(f"2d-{5+i:02d}", f"findings defined in {u}", n, len(fdef[u]),
          "paper_state_v5.md §2")
fref = defaultdict(set)
rx = re.compile(r"\bA(\d+)([ab]?)[- ]F(\d+)((?:/F?\d+)*)")
for name, txt in docs.items():
    for m in rx.finditer(txt):
        nums = [int(m.group(3))] + [int(x) for x in re.findall(r"\d+", m.group(4))]
        for n in nums:
            fref[("A" + m.group(1) + m.group(2), n)].add(name)
broken = []
for (u, n), where in sorted(fref.items()):
    cands = [u] if u in fdef else [k for k in fdef if k.rstrip("ab") == u]
    if not any(n in fdef[c] for c in cands):
        broken.append(f"{u}-F{n} <- {', '.join(sorted(where))}")
check("2d-11", "A#-F# references pointing to a finding that does not exist", 0, len(broken),
      "regex over all .md")
out.append("\n## Broken finding references\n" + "\n".join(broken))
amb = [f"{u}-F{n} <- {', '.join(sorted(w))}" for (u, n), w in sorted(fref.items())
       if u == "A11" and n in fdef["A11a"] and n in fdef["A11b"]]
check("2d-12", "references written 'A11-F#' where both A11a-F# and A11b-F# exist (ambiguous)",
      0, len(amb), "regex over all .md")
out.append("\n## Ambiguous A11 references\n" + "\n".join(amb))

# audit-log tables at the end of each unit
out.append("\n## Audit-log rows found in each audit file")
logs = defaultdict(dict)
for name, txt in docs.items():
    if not name.startswith("audit/"):
        continue
    for m in re.finditer(r"^\| (A\d+) \w+ \| \**(\w+)\** \| ([\d-]*) \| (.*?) \| (.*?) \| (.*?) \|$",
                         txt, re.M):
        logs[m.group(1)][name] = (m.group(2), m.group(5).strip(), m.group(6).strip())
for u in sorted(logs, key=lambda x: int(x[1:])):
    for name, v in sorted(logs[u].items()):
        out.append(f"{u} as logged in {name}: status={v[0]} findings={v[1]} unresolved={v[2]}")
incons = [u for u in logs if len({v[1] for v in logs[u].values()}) > 1]
check("2d-13", "units whose 'Findings' cell differs between the audit-log copies", "none",
      ",".join(sorted(incons)) or "none", "audit/A*.md log tables")
check("2d-14", "audit files that carry no audit-log table", "",
      ",".join(sorted(n for n in docs if n.startswith("audit/")
                      and "Audit log" not in docs[n] and "audit log" not in docs[n].lower())),
      "P4_AUDIT_PROTOCOL.md §6 ('ends by updating the audit log')", info=True)
proto = docs["P4_AUDIT_PROTOCOL.md"].split("## 10 ·")[1].split("## 11 ·")[0]
check("2d-15", "units marked 'open' in the protocol's own audit log (§10)", "",
      len(re.findall(r"\| open \|", proto)), "P4_AUDIT_PROTOCOL.md §10", info=True)

# ---- section references A# §n -------------------------------------------
sec_broken = []
for name, txt in docs.items():
    for m in re.finditer(r"\bA(\d+) §\s?([0-9a-c]+(?:\.\d+)?)", txt):
        unit, sec = m.group(1), m.group(2)
        tgt = [f for f in docs if re.match(rf"audit/A{unit}_", f)]
        if not tgt:
            sec_broken.append(f"A{unit} §{sec}: unit file absent <- {name}")
            continue
        t = docs[tgt[0]]
        esc = re.escape(sec)
        ok = re.search(rf"^#+ +(?:\(?{esc}\)?[ .·]|{esc} ·|{esc}\b)", t, re.M) or \
            re.search(rf"^#+ .*\b{esc}\b ·", t, re.M)
        if not ok:
            sec_broken.append(f"A{unit} §{sec}: no such heading in {tgt[0]} <- {name}")
sec_broken = sorted(set(sec_broken))
check("1-10", "references 'A# §n' with no matching heading in the audit file", "",
      len(sec_broken), "regex (heading match is approximate)", info=True)
out.append("\n## Section references without a matching heading\n" + "\n".join(sec_broken))

# ---- Q# -----------------------------------------------------------------
qref = defaultdict(set)
for name, txt in docs.items():
    for m in re.finditer(r"\bQ(\d+)\b", txt):
        qref[int(m.group(1))].add(name)
check("2b-01", "Q numbers referenced anywhere", "1-11",
      f"{min(qref)}-{max(qref)}", "regex", info=True)
out.append("\n## Q# usage by document")
for q in sorted(qref):
    out.append(f"Q{q}: {', '.join(sorted(qref[q]))}")
write_out("01_inventory.txt", "\n".join(out) + "\n")
