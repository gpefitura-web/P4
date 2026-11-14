# Audit A1 — Baliunas et al. 1995, ApJ 438, 269

**Date:** 2026-07-28
**Extraction method:** PyMuPDF render → Tesseract 5.3.4. Document is a pure 1-bit scan
(5120 × 6600 px, ~600 dpi native); the only text layer is the ADS bibcode
`1995ApJ...438..269B`. Two-pass rule applied and extended: page-level OCR at 300/400/500/600 dpi
× `--psm 6`/`--psm 4` (8 passes), then column-aware extraction via Tesseract TSV word
coordinates, then cell-level OCR at 900–2000 dpi under 5–8 independent configurations for every
disputed or P4-critical value.
**Pages read:** all 19 (journal pp. 269–287). Table 2 = pp. 280–281 (PDF pp. 12–13);
Figure 1 panels = pp. 273–279; §4.3/§5 = p. 284; Appendix A = p. 285; Appendix B = p. 286.

---

## 1 · Values extracted

Full catalogue: **`audit/baliunas_table2_full.csv`** — all 112 rows (111 stars + the Sun),
9 columns plus grade, cross-check and disagreement fields.

### 1.1 Table 2 column structure (as printed)

| # | Column | Note |
|---|---|---|
| 1 | HD Number | |
| 2 | Star | common name, blank for many |
| 3 | Figure 1 Reference | panel id, e.g. `1f` |
| 4 | B−V | |
| 5 | Spectral Type | footnote a–l on source |
| 6 | ⟨S⟩ | footnote m |
| 7 | P_cyc ± ΔP (yr) | *or* the words Var / Flat / Flat? / Long |
| 8 | FAP Grade | footnote n |
| 9 | Secondary Classification | footnote o |

> **Finding F1 — there is no σ_S or σ_S/S column in Table 2.** Columns 7–8 are headed
> "Primary Classification"; the variability class and the cycle period share one column.
> Grade **A** (header read at 400 dpi, confirmed by TSV word positions and by the
> reproduced column count).

### 1.2 P4 sample stars — verified values

All rows below are confirmed in **two independent locations within the paper**: Table 2
and the Figure 1 panel annotation (which prints HD, B−V, and period/class for each panel).
That is the grade-A condition of §4 of the protocol.

| HD | Star | B−V | ⟨S⟩ | Primary class | P_cyc ± ΔP (yr) | FAP | Secondary | Grade |
|---|---|---|---|---|---|---|---|---|
| — | **Sun** | 0.66 | 0.179 | cycle | 10.0 ± 0.1 | Excellent | … | A |
| 3651 | 54 Psc | 0.85 | 0.176 | cycle | 13.8 ± 0.4 ^p,q^ | Good | Long | A |
| 9562 | — | 0.64 | 0.136 | **Long** | — | — | … | A |
| 10476 | 107 Psc | 0.84 | **0.198** | cycle | 9.6 ± 0.1 | Excellent | … | A |
| 10700 | τ Cet | 0.72 | 0.171 | **Flat?** ^r^ | — | — | … | B |
| 32147 | — | 1.06 | **0.286** | **cycle** | 11.1 ± 0.2 | **Excellent** | Long | A |
| 76151 | — | 0.67 | **0.246** | **cycle** | 2.52 ± 0.02 ^p^ | Fair | Long | B |
| 81809 | — | 0.64 | 0.172 | cycle | 8.17 ± 0.08 | Excellent | … | A |
| 103095 | Gmb 1830 | 0.75 | **0.188** | **cycle** | 7.30 ± 0.08 | **Excellent** | … | A |
| 114710 | β Com | 0.57 | **0.201** | cycle | 16.6 ± 0.6 | Good | 9.6 ± 0.3, fair | A |
| 143761 | ρ CrB | 0.60 | **0.150** | **Long** | — | — | … | A |
| 149661 | 12 Oph | 0.82 | **0.339** | cycle | 17.4 ± 0.7 | Good | 4.00 ± 0.04, Good | A |
| 166620 | — | 0.87 | **0.190** | **cycle** | 15.8 ± 0.3 | **Excellent** | … | A |
| 182572 | 31 Aql | 0.77 | 0.148 | **Flat** | — | — | … | A |
| 190406 | 15 Sge | 0.61 | **0.194** | cycle | **2.60 ± 0.02** | Fair | 16.9 ± 0.8, good | A |
| 219834A | 94 Aqr A | 0.80 | 0.155 | cycle | 21 ± 1 | Good | … | A |
| 219834B | 94 Aqr B | 0.91 | **0.204** | **cycle** | 10.0 ± 0.2 | **Excellent** | … | A |

Bold = differs from the value currently in `paper_state_v2.md`.

### 1.3 Table 2 note — the classification definitions (verbatim sense, footnote to Table 2)

| Class | Definition |
|---|---|
| **Var** | significant variability without pronounced periodicity, on timescales longer than 1 yr but much shorter than 25 yr; ⟨σ_S/S⟩ ≳ 2% |
| **Flat** | ⟨σ_S/S⟩ < 1%–1.5% |
| **Flat?** | ⟨σ_S/S⟩ ≈ 1.5%–2% |
| **Long** | significant variability on timescales longer than 25 yr |

Grade **A** (read cleanly at 400 and 1000 dpi, multiple configurations agree).
The note adds that some records show secular change over 25 yr implying, if a cycle is
present, a period > 50 yr.

### 1.4 FAP grade definition (Table 2, footnote n) — FAP quoted *in percent*

| Grade | Range |
|---|---|
| excellent | FAP < 10⁻⁹ |
| good | 10⁻⁹ < FAP < 10⁻⁵ |
| fair | 10⁻⁵ < FAP < 10⁻² |
| poor | 10⁻² < FAP < 10⁻¹ |

Grade **B**. The two `10⁻⁹` exponents required isolation at 2000 dpi before four
configurations agreed; the chain is additionally self-consistent (each grade's upper bound is
the next one's lower bound). Recorded as B rather than A because only one location in the
paper states it.

### 1.5 Other Table 2 footnotes relevant to P4

| Mark | Meaning |
|---|---|
| m | ⟨S⟩ is an **annually averaged mean over all years** |
| n | primary classification / FAP grade definition (§1.4) |
| o | secondary period after the primary frequency was filtered out, or behaviour on timescales > 25 yr |
| p | **linear trend removed prior to period identification** — carried by HD 3651, 76151, and others |
| q | **Maunder-minimum activity beginning after 1980?** — carried by HD 3651 |
| r | possible increasing activity after 1988 — carried by HD 10700 |

### 1.6 Observing cadence and season definition

| Quantity | Value | Location | Grade |
|---|---|---|---|
| Wilson-era cadence | monthly, 1966–1977, 100-inch telescope | §2 | A |
| later cadence | near-nightly, 60-inch telescope | §2 | B |
| record end | 1991 March 31 | §2 | A |
| total individual observations | 171,300 | §2 | A |
| binning of the published record | means in **30-day intervals** | §2 | A |
| ⟨S⟩ in Table 2 | **annual** mean over all years | Table 2 note m | A |
| sample size | **111 stars** (Wilson's 91 previously published + 7 + others) | §2.5/§3 | A |

**Implication for N.** The published per-star series that P4 can reconstruct from this paper is
the annual mean: 1966–1991 → **N ≈ 25–26 points per star**. The 30-day means exist but are not
tabulated in this paper; only Figure 1 plots them.

---

## 2 · Checks performed

### 2.1 §5 classification checksum — **PASS**

The paper states (p. 284, §4.3, immediately before §5): roughly 52 stars including the Sun show
cycles, 31 are flat or have linear trends over the observing interval, and 29 show variability
with no periodicity.

| Category | Counted from Table 2 | Paper | Result |
|---|---|---|---|
| cycles (incl. Sun) | **52** | 52 | PASS |
| flat or linear trends (Flat 11 + Flat? 4 + Long 16) | **31** | 31 | PASS |
| variable, no periodicity (Var) | **29** | 29 | PASS |
| total | **112** | 111 stars + Sun = 112 | PASS |

This validates the extraction as a whole, not merely row by row. Note that the paper's
"flat or have linear trends" category **groups Flat, Flat? and Long together** — Long is a
linear/secular trend, not a separate third state.

### 2.2 Two-pass OCR diff — pass, with 20 values escalated and resolved

Page-level passes at 400/500/600 dpi agreed on every row. The 300 dpi × `--psm 4` pass degraded
badly (27 of 66 rows recovered) and was retained only as a negative control. Disagreements were
concentrated in the period column, where the parser could confuse the primary period with the
secondary-classification period; all 20 affected rows were resolved by cell-level OCR at
1200 dpi under 4–8 configurations. Zero values remain unresolved.

### 2.3 Independent in-paper cross-check against Figure 1 — pass

Each Figure 1 panel is annotated with HD number, B−V, and either the cycle period + FAP grade or
the class word. This is an independent typesetting of the same information, so agreement is a
genuine second check rather than a re-read. 103 of 112 rows were confirmed on both B−V and
class; **no mismatch was found**. Examples: HD 143761 `0.60 Long`; HD 103095 `0.75 7.3, excl`;
HD 166620 `0.87 15.8, excl`; HD 32147 `1.06 11.1, excl`; HD 219834B `0.91 10.0, excl`;
HD 207978 `0.42 Flat`.

### 2.4 ⟨S⟩ scale — **not stated in this paper**

Table 2 gives no instrument scale for ⟨S⟩ and the word "HKP-2" does not appear. The paper
describes the photometers and the calibration procedure (§2) and gives the Sun as ⟨S⟩ = 0.179,
but does not label the scale. **Escalated to A3 (Egeland+2017)**, which is where the
HKP-1 → HKP-2 offset and the reason Baliunas' solar value is offset must be established.
Recorded here as a gap, not resolved.

### 2.5 Binarity — Appendix B read in full

Appendix B lists 12 stars with binary information: HD 3443, 39587, 76572, 81809, 88355, 114378,
124570, 137107, 141004, 156026, 158614, 178428. §5 separately names the resolved visual pairs:
HD 26913/23, 131156A/B, 155885/6, 165341A/B, 201091/2, **219834A/B**.

| Star | Status | Grade |
|---|---|---|
| **HD 81809** | Binary. Orbital period ~35 yr; masses 1.5 ± 0.5 and 0.8 ± 0.2 M☉ → ~G0 V + K0 V; ΔV ≈ 0.8 mag; separation ~0″.4. | A |
| **HD 219834B** | Component of a **resolved visual pair**, measured separately from 219834A; not in the Appendix B blended-flux list. | A |

---

## 3 · Findings

**F1 — Table 2 contains no σ_S column.** The `S_std` values in the current pipeline cannot have
come from this table. Under §5 of the protocol any σ_S read off Figure 1 is grade C by
definition and cannot reach the manuscript. Either the quantity is dropped, or it is taken from
a source that tabulates it.

**F2 — HD 4915 does not exist in this paper.** A full-text search of all 19 pages returns no
occurrence. Table 2 runs 4628 → 6920. Confirms the earlier audit finding; the star must be
removed from the catalogue and cannot be a "Flat/Maunder" member.

**F3 — Four stars in the current P4 catalogue are cycling stars with graded periods.**
Each is contradicted by Table 2 *and* by its Figure 1 panel label:

| HD | `paper_state_v2` | Baliunas 1995 |
|---|---|---|
| 32147 | Variable, ⟨S⟩ 0.396 | **cycle 11.1 ± 0.2 yr, Excellent**, ⟨S⟩ 0.286, secondary Long |
| 103095 | Maunder/Flat, ⟨S⟩ 0.165 | **cycle 7.30 ± 0.08 yr, Excellent**, ⟨S⟩ 0.188 |
| 166620 | Maunder/Flat, ⟨S⟩ 0.215 | **cycle 15.8 ± 0.3 yr, Excellent**, ⟨S⟩ 0.190 |
| 219834B | Irregular, ⟨S⟩ 0.159 | **cycle 10.0 ± 0.2 yr, Excellent**, ⟨S⟩ 0.204 |

Appendix A is explicit about HD 103095: it is the sole Population II star in the survey,
older than 10 Gyr with [Fe/H] < −1.0, and it still shows a 7.3 yr cycle — the paper uses it as
evidence that old metal-poor stars *can* sustain vigorous cycles. Using it as a Maunder-analogue
inverts the source's own argument. §5 likewise states that HD 219834A and B both show cyclic
activity.

**F4 — HD 143761 (ρ CrB) is "Long", not "Flat".** ⟨S⟩ = 0.150. "Long" means significant
variability on timescales > 25 yr. It belongs to the paper's *flat-or-linear-trend* group of 31
for counting purposes, but it is not a low-variability Flat star, and treating it as
"post-transition, flat" is a different claim from the one the data support.

**F5 — the paper's own Maunder-minimum candidates are not the ones in the P4 catalogue.**
Appendix A names three, none currently used as such:

- **HD 3651** (54 Psc) — activity has declined steadily since 1966; the ~1989 maximum is
  extraordinarily low relative to 1978; Baliunas concludes it "is entering a period of
  low-amplitude variation, similar to the solar Maunder Minimum". It carries Table 2 footnote q,
  *Maunder-minimum activity beginning after 1980?* This is the paper's clearest **star caught in
  transition** — precisely the object class P4's CSD hypothesis is about.
- **HD 9562** — flat record, ⟨S⟩ about 20% below the Sun, but v sin i of 2–3 km s⁻¹ implies it is
  *younger* than the Sun; the inactivity is therefore not age, and "implies a Maunder minimum
  phase".
- **HD 10700** (τ Cet) — σ_S/S = 1.2%, among the smallest in the survey; "may be in a Maunder
  minimum state", with a slight rise after 1989 possibly signalling a return to cyclic activity.

**F6 — HD 190406's primary period is 2.60 ± 0.02 yr, not 16.9 yr.** The 16.9 ± 0.8 yr value is
the *secondary* period, recovered only after the 2.6 yr cycle is filtered out (Appendix A;
Table 2 footnote o). `paper_state_v2` lists 16.9 as P_cyc. The same primary/secondary inversion
affects HD 114710 (primary 16.6, secondary 9.6 — as listed) and HD 149661 (primary 17.4,
secondary 4.00).

**F7 — HD 81809 is a binary whose activity may not originate in the catalogued star.**
Appendix A: the 40-day rotation period is inconsistent with both its ⟨S⟩ and its colour; the
resolution offered is that the observed activity arises from the *lower-mass component*
(estimated K0 V), with the primary being much less active. The smooth 8.17 yr cycle is therefore
a cycle of an unresolved companion in a composite record. As a "clean cycling control" this star
is compromised.

**F8 — HD 76151's period rests on a removed linear trend.** 2.52 ± 0.02 yr, FAP grade Fair,
carrying footnote p (linear trend removed prior to period identification) and a secondary
classification of Long. It is a cycling star, not "Variable, episodes of decline".

**F9 — ⟨S⟩ is an annual mean, so N ≈ 25–26 per star.** Confirms that DFA is not admissible for
the Mount Wilson series on the strength of this paper alone. Carried to A2 and A5.

---

## 4 · Decisions taken, with basis

1. **The catalogue is rebuilt from `audit/baliunas_table2_full.csv`, not amended in place.**
   Basis: four of twelve stars are misclassified and one does not exist; patching preserves the
   provenance problem the audit exists to remove.
2. **HD 4915 is removed permanently.** Basis: absent from all 19 pages.
3. **⟨S⟩ for every star is taken from Table 2 column 6, understood as an annual mean over all
   years.** Basis: Table 2 footnote m.
4. **Group membership is defined by the Table 2 primary classification, using the paper's own
   three-way split.** Basis: §4.3 totals (52 / 31 / 29), which the extraction reproduces exactly.
   "Long" is grouped with flat/linear-trend, per the paper's own counting, and is *labelled*
   distinctly so P4 can decide whether to keep the distinction.
5. **Where a star has two periods, the Table 2 column-7 value is the primary and the
   column-9 value is the secondary.** Basis: Table 2 footnote o and Appendix A on HD 190406.
6. **No σ_S/S value is admitted from this paper.** Basis: F1 and protocol §5 on figure-derived
   values.
7. **The ⟨S⟩ scale question is deferred to A3, not assumed.** Basis: §2.4 above.
8. **The binarity decision is deferred to the consolidation pass, and flagged.** HD 81809 is a
   composite record (Appendix A/B); HD 219834B is a resolved component. Both are currently
   sample members. Recording rather than resolving, per protocol rule 4.

---

## 5 · Unresolved (grade C or X)

**None.** All 112 rows are graded A (103) or B (9). The 20 values that disagreed between passes
were resolved by cell-level OCR; the one row that remained (HD 82885) was resolved to
primary 7.9 ± 0.2, Fair, secondary 12.6 ± 0.7, poor.

Two items are *out of scope* rather than unresolved, and are escalated:

| Item | Why not resolved here | Goes to |
|---|---|---|
| ⟨S⟩ instrument scale (HKP-2?) | Not stated anywhere in Baliunas+1995 | **A3 (Egeland+2017)** |
| σ_S/S per star | Not tabulated; only defined as class thresholds | **A2/A6**, or drop the quantity |

---

## 6 · Open questions from protocol §11 — status after A1

| # | Question | Status |
|---|---|---|
| 1 | Is DFA admissible for the stellar series? | **Provisionally no.** ⟨S⟩ is annual, 1966–1991 → N ≈ 25–26. Revisit at A2. |
| 2 | Do binaries stay in the sample? | **Recorded, not decided.** HD 81809 composite (F7); HD 219834B a resolved component. |
| 6 | Do Baliunas and Saar agree on classifications? | Baliunas side now fixed and graded; **A6** can proceed. |

---

## 7 · Consequence for the P4 sample

The audit removes the paper's empirical basis for the current three-group design. Of the four
stars used as Flat/Maunder-analogues, three (103095, 166620, and by extension 219834B) have
Excellent-grade cycles, one (4915) does not exist, and ρ CrB is a long-trend star. Of the three
Irregular/pre-Maunder CSD candidates, two (32147, 76151) are cycling.

Baliunas+1995 does contain genuine members for both groups — the Flat class has 11 members and
Flat? has 4, and Appendix A names three explicit Maunder-minimum candidates (HD 3651, 9562,
10700), with HD 3651 documented as *entering* such a state during the observing window. But
selecting them is a sample-definition decision, and under protocol §1 it must be made from the
frozen catalogue before the real data are examined — not here, and not with results in hand.
That decision belongs to the consolidation pass, after A2 fixes N per star.

---

## 8 · Audit log entry

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | **closed** | 2026-07-28 | `audit/A1_baliunas.md`, `audit/baliunas_table2_full.csv` | F1–F9 | none (2 escalated to A3) |

---

## 9 · Reproducibility

Scripts used, in order: `extract_tsv.py` (TSV column-aware extraction),
`merge_table2.py` (multi-pass consensus + disagreement flags), `cell_verify.py` (cell-level
multi-configuration verification), `finalize.py` (Figure 1 cross-check, grading, checksum).
The checksum in §2.1 re-runs from `finalize.py` and is the single fastest way for a third party
to confirm the whole extraction.
