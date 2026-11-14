"""Stage 3.1 - frozen catalogue baliunas_table2_full.csv."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import re

from common import check, read_csv, write_out

SRC_V4 = "paper_state_v4.md §2"
b = read_csv("baliunas_table2_full.csv")
cls = b.primary_class.value_counts().to_dict()

check("3.1-01", "catalogue rows", 112, len(b), SRC_V4)
check("3.1-02", "CYCLE rows", 52, cls.get("CYCLE", 0), "P4_RESEARCH_NOTEBOOK.md D09")
check("3.1-03", "Flat rows", 11, cls.get("Flat", 0), "paper_state_v4.md §2.1")
check("3.1-04", "Flat? rows", 4, cls.get("Flat?", 0), "paper_state_v4.md §2.1")
check("3.1-05", "Long rows", 16, cls.get("Long", 0), "paper_state_v4.md §2.1")
check("3.1-06", "Flat+Flat?+Long", 31,
      cls.get("Flat", 0) + cls.get("Flat?", 0) + cls.get("Long", 0),
      "P4_RESEARCH_NOTEBOOK.md D09")
check("3.1-07", "Var rows", 29, cls.get("Var", 0), "P4_RESEARCH_NOTEBOOK.md D09")
g = b.grade.value_counts().to_dict()
check("3.1-08", "rows graded C or X", 0, g.get("C", 0) + g.get("X", 0), SRC_V4)
check("3.1-09", "rows graded A", 103, g.get("A", 0), SRC_V4)
check("3.1-10", "rows graded B", 9, g.get("B", 0), SRC_V4)
check("3.1-11", "duplicated HD identifiers", 0, int(b.HD.duplicated().sum()),
      "implicit (one row per star)")

# Defect a: HD 219834A period missing, FAP Good, grade A
r = b[b.HD == "219834A"].iloc[0]
check("3.1-12", "HD 219834A (P_cyc|FAP|grade)", "|Good|A",
      f"{r.P_cyc}|{r.FAP}|{r.grade}", SRC_V4 + " defect a")
# Defect b: HD 76572 period missing, FAP Poor, grade A, n_pass 1
r = b[b.HD == "76572"].iloc[0]
check("3.1-13", "HD 76572 (P_cyc|FAP|grade|n_pass)", "|Poor|A|1",
      f"{r.P_cyc}|{r.FAP}|{r.grade}|{r.n_pass}", SRC_V4 + " defect b")
# Six CYCLE rows with neither period nor FAP
six = sorted(b[(b.primary_class == "CYCLE") & (b.P_cyc == "") & (b.FAP == "")].HD,
             key=int)
check("3.1-14", "CYCLE rows with neither period nor FAP",
      "10780,88737,111456,126053,176051,185144", ",".join(six), SRC_V4)

# Defect c: OCR debris in 'secondary'. A cell is legitimate if empty, 'Long',
# or a 'period + error, grade' secondary cycle.
legit = re.compile(r"^(Long|\d+(\.\d+)?\s*\+\s*\d+(\.\d+)?,\s*(excellent|good|fair|poor))$",
                   re.I)
nonempty = b[b.secondary != ""]
debris = nonempty[~nonempty.secondary.map(lambda s: bool(legit.match(s)))]
check("3.1-15", "rows with OCR debris in 'secondary'", 32, len(debris),
      SRC_V4 + " defect c")
check("3.1-16", "rows with legitimate non-empty 'secondary' (Long or 2nd period)",
      "", len(nonempty) - len(debris), "not stated in the documents", info=True)

# Other residue visible in text columns (not listed in v4 §2)
odd_sp = b[b.sptype.str.contains(r"[°?]|KO|FO|Iv|\bv\b", regex=True)]
odd_star = b[b.star.isin([":", "a"])]
check("3.1-17", "rows with OCR residue in 'sptype' (deg sign, '?', 'KO', 'FO', lowercase class)",
      "", len(odd_sp), "not stated in the documents", info=True)
check("3.1-18", "rows with single-character residue in 'star'", "", len(odd_star),
      "not stated in the documents", info=True)
dis = b[b.disagree != ""]
check("3.1-19", "rows with non-empty 'disagree' (OCR passes disagreed)", "",
      len(dis), "not stated in v4/v6", info=True)
check("3.1-20", "of those, rows graded A", "", int((dis.grade == "A").sum()),
      "P4_AUDIT_PROTOCOL.md §5 (disagreement drops to C until resolved)", info=True)

out = ["# OCR debris rows in 'secondary'", debris[["HD", "secondary"]].to_string(),
       "", "# residue in sptype", odd_sp[["HD", "sptype"]].to_string(),
       "", "# residue in star", odd_star[["HD", "star"]].to_string(),
       "", "# rows with 'disagree' set",
       dis[["HD", "disagree", "n_pass", "grade", "P_cyc", "dP", "primary_class"]].to_string()]
write_out("03a_baliunas.txt", "\n".join(out) + "\n")
