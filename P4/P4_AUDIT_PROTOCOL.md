# P4_AUDIT_PROTOCOL.md
## Source-paper audit — Paper P4, *Critical Slowing Down Near Stellar Activity Minima*

> **Status:** audit phase open. No pipeline code is to be modified until the audit
> closes and `P4_SOURCE_VALUES.md` is signed off.

---

## 1 · Why this phase exists

Two rounds of analysis were built on values recalled from memory rather than read from
the sources. The audit that followed found, among other things, a star that does not
exist in the catalogue (HD 4915), a mean activity index wrong by 62% (HD 10476), and
four stars assigned to the wrong variability group. Those errors survived because the
numbers lived inside the code with no record of where they came from.

The purpose of this phase is to establish, for every quantity P4 depends on, a written
chain of evidence from the published source — before any of it reaches the manuscript.

**A second, equally important purpose:** fixing the analysis choices from the literature
*before* the real data are examined. Window sizes, detrending rules, group definitions
and significance thresholds must all be settled from the papers now. Choosing them later,
with the data in hand, would make the result unpublishable regardless of the p-value.

---

## 2 · Scope

Nine PDFs at `github.com/gpefitura-web/P4`:

| File | Role in P4 | Text layer |
|---|---|---|
| Baliunas et al. 1995, ApJ 438, 269 | stellar catalogue, classifications | **scanned — OCR required** |
| Lockwood et al. 2007, ApJS 171, 260 | possible series extension | native |
| Egeland et al. 2017, ApJ 835, 25 | solar calibration, data location | native |
| Dakos et al. 2012, PLoS ONE 7, e41010 | EWS methodology | native |
| Peng et al. 1994, Phys. Rev. E 49, 1685 | DFA algorithm | native |
| Saar & Brandenburg 1999, ApJ 524, 295 | independent cross-check | native |
| Scheffer et al. 2009, Nature 461, 53 | CSD theory | native |
| Held & Kleinen 2004, GRL 31, L23207 | CSD precedent (climate) | native |
| Usoskin et al. 2017, LRSP 14, 3 | solar context | native |

**Not in the repository:** Eddy 1976, Science 192, 1189. Either add it or drop every
claim that would cite it (see unit A7).

---

## 3 · Rules of the audit

1. **Read, do not recall.** Every value must be traced to a page in a PDF. A number that
   cannot be located is recorded as *not found*, never as a plausible estimate.
2. **Record the location.** Paper, table or section, page. Enough for a third party to
   re-check in under a minute.
3. **Grade the confidence** of every extracted value (§4).
4. **Contradictions are findings, not obstacles.** If two papers disagree, record both
   and the disagreement. Do not silently pick one.
5. **The audit does not touch the pipeline.** Code changes come after sign-off, in one
   deliberate pass.
6. **Decisions are recorded with their basis.** "Window = 50%" is not a decision;
   "Window = 50%, per Dakos+2012 Fig. 2 caption" is.

---

## 4 · Confidence grading

Every value carries a grade:

| Grade | Meaning | Usable? |
|---|---|---|
| **A** | Read from a native text layer *and* confirmed by a second independent check (cross-paper agreement, internal checksum, or a second extraction method) | yes |
| **B** | Read cleanly from text or OCR, single source, nothing contradicts it | yes, with the source cited |
| **C** | OCR-uncertain, read off a figure, or inferred from surrounding text | **no** — must be resolved or the claim dropped |
| **X** | Not found, or sources contradict each other | **no** — escalate |

Anything graded C or X at the end of the audit either gets resolved or gets removed from
the paper. Nothing at C or X reaches the manuscript.

---

## 5 · Verification methods

**Two-pass extraction (mandatory for Baliunas+1995).** The PDF is a scan; OCR misreads
digits, and `0.198` versus `0.196` is invisible in a single pass. Extract twice with
different settings — for example PyMuPDF's text layer against Tesseract at 300 and 400
DPI, or `--psm 6` against `--psm 4` — and diff the results. Agreement raises a value to
grade B; disagreement drops it to C until resolved by visual inspection of the page
image.

**Internal checksums.** Papers usually state totals that must reconcile with their own
tables. Baliunas+1995 §5 gives roughly 52 stars with cycles, 31 flat or with linear
trends, and 29 variable without periodicity — 112 entries, against a sample of 111 stars
plus the Sun. Counting the Table 2 classifications and reproducing those totals validates
the whole extraction at once. Look for a checksum like this in every paper before
extracting individual values.

**Cross-paper checks.** Saar & Brandenburg 1999 Table 1 lists cycle periods for many of
the same stars, taken independently from the Mount Wilson database. Where both papers
cover a star, agreement raises the value to grade A; disagreement is a finding.

**Figure-derived values are provisional.** Anything read off a plot rather than a table
is grade C by definition. The `S_std` estimates currently in the catalogue are in this
category and must be flagged as such.

---

## 6 · Audit units

Each unit is one conversation, produces one deliverable, and ends by updating the audit
log. Units A1 and A2 gate the rest.

---

### A1 · Baliunas et al. 1995 — the stellar catalogue
**Priority: highest. This is the paper the sample selection rests on, and the only scan.**

Extract:
- Table 2 in full — HD, name, B−V, spectral type, ⟨S⟩, cycle period, FAP grade, secondary
  classification — for the whole sample, not only our 14 stars. The full table is what
  makes the checksum possible and what allows the sample to be revised later.
- The Table 2 note defining `Var`, `Flat`, `Flat?`, `Long`, and the σ_S/S thresholds.
- Appendix A commentary on individual stars.
- Appendix B binary flags for every candidate star.
- §5 classification totals, for the checksum.
- The observing cadence and season definition — this determines N per star, which decides
  whether DFA is admissible at all.

Checks:
- Reproduce the §5 totals by counting Table 2 classifications.
- Two-pass OCR diff on all numeric columns.
- Confirm the ⟨S⟩ column is on the HKP-2 scale and note any stated uncertainty.

Watch for:
- **Binarity.** HD 81809 is a binary (Appendix B); HD 219834B is a component of a visual
  pair. A companion contributing flux can mimic or mask variability. Decide whether
  binaries stay in the sample, and record the decision.
- Whether ⟨S⟩ is a straight mean or a seasonal-mean average.

Deliverable: `audit/A1_baliunas.md` + `audit/baliunas_table2_full.csv` with a grade
column, plus a list of every value that disagreed between OCR passes.

---

### A2 · Lockwood et al. 2007 — does the sample get longer?
**Priority: high. Runs before any decision about DFA on the stellar series.**

A preliminary scan found that only 5 of our 14 stars appear anywhere in this paper:
HD 10476, 81809, 114710, 149661 and 182572. The other nine were not found.

Determine:
- Which of the 14 have published series extending beyond 1991, and to what date.
- The resulting N per star.
- Whether the extension is on the same S scale or requires a transformation.
- Cadence of the extended data.

Why this matters: if some stars gain points and others do not, N becomes correlated with
group membership, and any difference in AR(1) between groups could be a sample-length
artefact rather than a physical signal. That would be fatal in review.

Decide and record one of:
- (a) use Baliunas only, uniform N, note the lost coverage as a limitation
- (b) use extended series only for the subset, with N as an explicit covariate
- (c) restrict the sample to stars with comparable N

Deliverable: `audit/A2_lockwood.md` with the per-star extension table and the decision.

---

### A3 · Egeland et al. 2017 — solar calibration and where the data live
Extract:
- ⟨S⟩ for cycles 15–24, cycle 23 mean, minima, amplitudes, with uncertainties.
- The K→S transformation (their Eq. 12) and its uncertainty.
- The HKP-1 → HKP-2 correction and the reason Baliunas' 0.179 is offset.
- Appendix B: exactly which instruments the machine-readable table contains, their date
  ranges, cadence and gaps.

Checks:
- Confirm the S scale used for the stars in Baliunas is the same one the solar value is
  now placed on. If not, the star–Sun comparison needs a stated caveat.

Also produce: precise, click-by-click instructions for obtaining the machine-readable
table, and a decision on which instrument series to use as the primary solar record.
NSO/SP has the longest continuous daily coverage; confirm this from the paper rather
than assuming it.

Deliverable: `audit/A3_egeland.md` + the data-acquisition instructions.

---

### A4 · Dakos et al. 2012 — the method, fixed in advance
Extract, with section and figure references:
- Rolling window size: default and the sensitivity range tested.
- Gaussian filtering: bandwidth, and precisely which indicators it applies to.
- Table 3 in full — the preprocessing, detrending, sensitivity and significance columns
  for each indicator, including all footnotes.
- The minimum series length stated for DFA.
- How significance is assessed: the surrogate/null-model procedure, how many surrogates,
  and which null model.
- Whether the trend statistic is computed on the indicator series or on the residuals.

The significance procedure is the gap in the current pipeline. Kendall τ p-values from
`scipy` assume independent observations; rolling-window indicators are strongly
autocorrelated by construction, so those p-values are optimistic. Dakos+2012 handle this
with surrogate datasets from a fitted ARMA model. **Extract that procedure in enough
detail to implement it**, because a referee will ask.

Deliverable: `audit/A4_dakos.md` — a parameter table where every row cites a section.

---

### A5 · Peng et al. 1994 — the DFA algorithm
Extract:
- The algorithm step by step, in the paper's own terms.
- The minimum box size and the stated reason.
- Whether boxes overlap.
- The detrending polynomial order used.
- How the fitting range is chosen and how crossovers are handled.
- Any statement about the shortest series the method can be applied to.

Check the native implementation in the notebook against this, line by line, and record
the comparison. Confirm the theoretical values it reproduces (0.5 for uncorrelated
noise, 1.5 for integrated noise).

Deliverable: `audit/A5_peng.md`, including a verdict on whether the implementation is
faithful.

---

### A6 · Saar & Brandenburg 1999 — independent cross-check
Extract Table 1 for every star that overlaps our sample: rotation period, cycle period(s),
branch assignment, weight, and the notes column.

Checks:
- Cycle periods against Baliunas Table 2. Agreement → grade A. Disagreement → finding.
- Their flat-activity discussion in §4.4, which predicts cycle periods for Maunder-state
  stars — directly relevant to the P4 Discussion.
- Whether any of our Irregular or Flat stars are reclassified here.

Deliverable: `audit/A6_saar.md` with a star-by-star comparison table.

---

### A7 · Scheffer et al. 2009 + Held & Kleinen 2004 — the theoretical claims
For every statement the Introduction and Theory sections will make about CSD, locate the
sentence that supports it. Specifically:
- The formal link between an approaching bifurcation and rising autocorrelation.
- The relationship between AR(1), variance and the recovery rate.
- Which systems CSD has been demonstrated in, and the stated limitations.
- Any caveat about false positives or missed alarms that P4 must acknowledge.

Also resolve the Eddy 1976 gap: either the PDF is added to the repository, or every
claim about the Maunder Minimum is re-sourced to Usoskin+2017 or Baliunas+1995 §5.

Deliverable: `audit/A7_theory.md` — a claim-to-citation map for the Introduction.

---

### A8 · Usoskin et al. 2017 — solar context
Extract:
- The quantitative characterisation of the 2008–2010 minimum in a century-long context.
  The manuscript will assert this minimum was exceptional; that assertion needs a number
  and a source, not an impression.
- Cycle 24 amplitude relative to cycles 15–23.
- The reconstructed history of grand minima: frequency, duration, and how entry into one
  is defined.
- Any statement on the predictability of grand minima — this is the closest thing in the
  literature to P4's hypothesis and must be engaged with, not ignored.

Deliverable: `audit/A8_usoskin.md`.

---

## 7 · Deliverable format

Every unit produces a file with the same structure:

```markdown
# Audit A<n> — <paper>
Date | Extraction method | Pages read

## Values extracted
| Quantity | Value | Location | Grade | Notes |

## Checks performed
- <check> -> pass / fail / finding

## Findings
1. <anything that contradicts the current pipeline or the other papers>

## Decisions taken, with basis
1. <decision> -- basis: <paper, section>

## Unresolved (grade C or X)
| Quantity | Why unresolved | Proposed resolution |
```

---

## 8 · Sequence

| Order | Unit | Depends on | Gates |
|---|---|---|---|
| 1 | A1 Baliunas | — | sample definition |
| 2 | A2 Lockwood | A1 | N per star; DFA feasibility |
| 3 | A4 Dakos | — | all method parameters |
| 4 | A3 Egeland | — | solar constants and data source |
| 5 | A5 Peng | A4 | DFA implementation |
| 6 | A6 Saar | A1 | classification cross-check |
| 7 | A8 Usoskin | — | Discussion claims |
| 8 | A7 Theory | — | Introduction claims |

A1, A2, A3 and A4 are the ones that gate code changes. A5–A8 can proceed in parallel and
mainly serve the manuscript text.

**Closing the audit.** After A1–A8, one consolidation pass produces the final
`P4_SOURCE_VALUES.md` and `p4_star_catalog.csv`, and only then does the pipeline get
updated — in a single pass, against a frozen reference.

---

## 9 · Standard opening for an audit conversation

```
Paper P4 -- audit phase. See P4_AUDIT_PROTOCOL.md in Project Knowledge.
Unit: A<n> -- <paper>
Previous units completed: <list, or "none">

Fetch the PDF from github.com/gpefitura-web/P4 and extract per the protocol.
Apply the two-pass rule if the document is scanned.
Grade every value. Report contradictions rather than resolving them silently.
Produce audit/A<n>_<name>.md in the protocol format.
```

Fetching the PDFs inside the sandbox (VizieR and ADS are blocked, GitHub raw is not):

```bash
BASE="https://raw.githubusercontent.com/gpefitura-web/P4/main"
curl -s -o baliunas1995.pdf "$BASE/Baliunas%20et%20al.%201995%2C%20ApJ%20438%2C%20269.pdf"
curl -s -o dakos2012.pdf    "$BASE/Dakos%20et%20al.%202012%2C%20PLoS%20ONE%207%2C%20e41010.pdf"
curl -s -o egeland2017.pdf  "$BASE/Egeland_2017_ApJ_835_25.pdf"
curl -s -o held2004.pdf     "$BASE/Held%20%26%20Kleinen%202004%2C%20GRL%2031%2C%20L23207.pdf"
curl -s -o lockwood2007.pdf "$BASE/Lockwood_2007_ApJS_171_260.pdf"
curl -s -o peng1994.pdf     "$BASE/Peng%20et%20al.%201994%2C%20Phys.%20Rev.%20E%2049%2C%201685.pdf"
curl -s -o saar1999.pdf     "$BASE/Saar_1999_ApJ_524_295.pdf"
curl -s -o scheffer2009.pdf "$BASE/Scheffer%20et%20al.%202009%2C%20Nature%20461%2C%2053.pdf"
curl -s -o usoskin2017.pdf  "$BASE/Usoskin%20et%20al.%202017%2C%20Living%20Rev.%20Sol.%20Phys.%2014%2C%203.pdf"
```

---

## 10 · Audit log

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | open | | | | |
| A2 Lockwood | open | | | | |
| A3 Egeland | open | | | | |
| A4 Dakos | open | | | | |
| A5 Peng | open | | | | |
| A6 Saar | open | | | | |
| A7 Theory | open | | | | |
| A8 Usoskin | open | | | | |

**Sign-off condition:** all units closed, no value in `P4_SOURCE_VALUES.md` graded C or X,
and every methodological parameter carrying a section-level citation.

---

## 11 · Open questions the audit must answer

These are known unknowns. Each should be resolved by the unit named.

1. **Is DFA admissible for the stellar series at all?** (A1 for N, A2 for extensions,
   A5 for the algorithmic floor.) Current position: no, N ≈ 26 is too short. If Lockwood
   extends some stars, revisit.
2. **Do binaries stay in the sample?** (A1.) HD 81809 and HD 219834B are affected.
3. **How is significance established for rolling-window trends?** (A4.) The current
   Kendall τ p-values do not account for the autocorrelation the method induces.
4. **Is N confounded with group?** (A2.) If extensions are uneven, this must be handled.
5. **Are the star and Sun S-indices on the same scale?** (A3.)
6. **Do Baliunas and Saar agree on our stars' classifications?** (A6.)
7. **Has anyone already claimed grand minima are unpredictable?** (A8.) If so, P4 must
   engage with that claim directly.
8. **Is the Eddy 1976 citation replaceable?** (A7.)

---

*Companion documents: `P4_SOURCE_VALUES.md` (the audit's product), `paper_state.md`
(project status), `p4_pipeline.ipynb` (frozen until sign-off).*
