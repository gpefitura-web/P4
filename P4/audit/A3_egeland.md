# Audit A3 — Egeland et al. 2017, ApJ 835, 25

**Date:** 2026-07-29
**Extraction method:** native text layer via PyMuPDF (16 pp., ~79 kB). No OCR required.
Table 2 was verified by an **arithmetic checksum**: the ten per-cycle means I extracted average
to 0.16936 against the printed 0.1694, and the ten amplitudes to 0.01455 against 0.0145. That is
an independent confirmation of the row-level extraction, not a re-read.
**Pages read:** all 16. Abstract = p. 1; instrument definitions §1–2 = pp. 1–2; Table 1 (prior
S(K) transformations) = p. 3; §3.1 HKP-1/HKP-2 = p. 4; §4.6 composite = p. 9; Table 2 = p. 10;
Table 4 (machine-readable solar S series) = p. 15.
**Inherited questions:** three, from A1 §2.4 and A2 §6.

---

## 1 · The headline value

**S_SUN_MEAN = 0.1694 ± 0.0005**, the mean of the cycle means over cycles 15–24.

Grade **A** — stated in the abstract and again in Table 2, and reproduced by the arithmetic
checksum above. The value currently in the P4 pipeline is correct.

Companion values, same grade:

| Quantity | Value | Meaning |
|---|---|---|
| ⟨S⟩_cyc | **0.1694 ± 0.0005** | mean over cycles 15–24 |
| ⟨S⟩_min | 0.1621 ± 0.0008 | mean cycle minimum |
| ⟨S⟩_max | 0.177 ± 0.001 | mean cycle maximum |
| ⟨ΔS⟩_cyc | 0.0145 ± 0.0012 | mean cycle amplitude (max − min) |
| σ_scatter on ⟨S⟩_cyc | **0.002** | cycle-to-cycle scatter of the cycle mean |

---

## 2 · Table 2 — per-cycle solar S, cycles 15–24

| Cycle | S_min | S_max | ΔS_cyc | ⟨S⟩_cyc |
|---|---|---|---|---|
| 15 | 0.1615 | 0.172 | 0.0108 | 0.1671 |
| 16 | 0.1614 | 0.175 | 0.0135 | 0.1678 |
| 17 | 0.1610 | 0.177 | 0.0160 | 0.1690 |
| 18 | 0.1619 | 0.177 | 0.0146 | 0.1696 |
| 19 | 0.1610 | 0.182 | **0.0208** | 0.1716 |
| 20 | 0.1621 | 0.174 | 0.0124 | 0.1684 |
| 21 | 0.1629 | 0.179 | 0.0164 | 0.1717 |
| 22 | 0.1631 | 0.181 | 0.0178 | 0.1713 |
| 23 | 0.1634 | 0.178 | 0.0143 | 0.1701 |
| 24 | 0.1626 | 0.172 | **0.0089** | 0.1670 |
| **⟨15–24⟩** | **0.1621** | **0.177** | **0.0145** | **0.1694** |
| σ_measure | 0.0008 | 0.001 | 0.0012 | 0.0005 |
| σ_scatter | 0.0008 | 0.003 | 0.003 | 0.002 |

Grade **A** (native text + arithmetic checksum).

---

## 3 · Inherited questions — all three resolved

### 3.1 What scale is S on? (from A1 §2.4)

**Resolved.** Egeland states it directly and emphatically: *S is an instrumental flux scale of the
HKP-2 spectrophotometer that cannot be independently measured without cross-calibration using
overlapping Mount Wilson targets* (§2). So:

- **The S-index is HKP-2 by definition.** There is no scale-free S.
- HKP-1 (Wilson's coudé scanner, 100-inch) measured a different quantity, F. The α calibration
  constant was set nightly so that on average S = F, but the instruments are not identical.
- Vaughan et al. (1978), from 13 coincident nights in 1977, give the conversion
  **F = 0.033 + 0.9978·S − 0.2019·S²** (Egeland Eq. 3) — a *quadratic*, not a unit transformation.

Baliunas et al. 1995's stellar Table 2 ⟨S⟩ values are on this HKP-2 S scale, which is why they are
directly comparable to Egeland's solar value. Grade **A**.

### 3.2 Does the Donahue reprocessing supersede Baliunas 1995? (from A2)

**Not addressed by this paper, and therefore still formally open** — but the practical answer is
that it does not matter for P4. Egeland is a solar calibration paper; it does not revisit stellar
S values. A2 established the reprocessing exists and shifts values by typically 1–2%. Since
decision A2-(a) fixes P4 on Baliunas values throughout, no mixing occurs. Recorded, not resolved.

### 3.3 HD 10476: 0.198 vs 0.1896 (from A2)

**Not addressed.** Egeland does not mention HD 10476 or any individual star. The 4.2%
discrepancy stands as recorded in A2 §6. It has no bearing on P4 as long as Baliunas values are
used uniformly. Escalated to **A6** (Saar & Brandenburg), the only remaining unit with stellar
S values.

---

## 4 · Findings

**F1 — S_SUN_MEAN = 0.1694 is confirmed, and the earlier correction was right.** The pipeline's
current constant is sourced, grade A, from two locations in the paper plus an arithmetic
checksum. Nothing to change.

**F2 — Baliunas et al. 1995's own solar value of 0.179 is not a measurement, and is biased high
by 5%.** This is the substantive finding of the unit. Egeland §2 establishes that:

- Baliunas' solar S came from an **unpublished S(K) proxy transformation**, not from observing the
  Sun with HKP-2. Egeland had to reconstruct it from mean values Donahue & Keil (1995) published
  for several intervals.
- The transformation was constructed to smooth the cycle 20–21 minima transition and to preserve
  the relative cycle amplitudes seen in F10.7 and sunspot records — i.e. it was tuned to other
  proxies, not derived from calcium measurements of the Sun.
- Baliunas reported ⟨S⟩ = 0.179 for cycles 20–22. Egeland's Table 2 gives 0.1684, 0.1717 and
  0.1713 for those cycles, a mean of **0.1705**. Baliunas is high by **5.0%**, consistent with
  Egeland's own statement that later SSS re-reductions were "∼5% lower".

**F3 — the Baliunas solar cycle *amplitude* is inflated by ~76%, which matters more than the
mean.** For cycle 23 the Baliunas S(K) relation gives ΔS = 0.0251; Egeland's direct HKP-2
measurement gives 0.0143. Egeland notes the Baliunas estimate is "more than double" the Hall &
Lockwood measurement, and quantifies the spread across all published transformations as ≈10% in
minima, ≈11% in cycle means, but **≈81% in amplitude**. His conclusion is blunt: *the solar
S-index has so far not been well understood.*

For P4 this is the more dangerous of the two biases. A CSD analysis compares *variance* and
*autocorrelation*, not absolute level. A solar series calibrated through the Baliunas S(K)
relation would carry a cycle amplitude nearly double the truth, inflating solar variance relative
to the stellar sample by a factor of ~3 in σ². Any solar-versus-stellar variance comparison built
on that calibration would be an artefact of the transformation.

**F4 — solar cycle amplitude has halved over the last three cycles.** From Table 2:
ΔS = 0.0178 (cycle 22) → 0.0143 (cycle 23) → **0.0089 (cycle 24)**, a 50% decline. Cycle 24 has
the lowest amplitude and the lowest cycle mean of all ten cycles measured, and cycle 19 the
highest amplitude (0.0208). This is a directly relevant empirical datum for P4's central
hypothesis and, as far as this audit is concerned, the strongest quantitative support in the
source material for treating the modern Sun as a system whose cycle is weakening. It is also a
sourced, grade-A number, which the current `paper_state_v2` narrative does not cite.

**F5 — a calibrated solar S-index time series exists and P4 is not using it.** Egeland Table 4,
*Calibrated Solar S-index Time Series*, gives columns Date (JD − 2,400,000), original S or K,
**calibrated S**, and instrument, with rows drawn from MWO/HKP-1, NSO/SP, MWO/HKP-2, SSS/CCD-1 and
SSS/CCD-2. It is published in full as a machine-readable table. This is a homogenised,
HKP-2-calibrated solar series spanning cycles 15–24 — precisely the quantity P4's solar track
needs, and strictly better than calibrating raw NSO K values in-house, which is the current plan
and which would reintroduce exactly the transformation problem F3 describes.

**F6 — the cycle-to-cycle scatter of the solar cycle mean is 0.002 in S (≈1.2%).** From Table 2,
σ_scatter on ⟨S⟩_cyc. This sets the natural scale against which "the Sun is variable" claims should
be judged, and it sits just above the 0.8% instrumental floor established in A2 F6. Worth stating
in the paper: the Sun's *cycle-mean* activity is stable at the ~1% level even while its cycle
*amplitude* halves. Those are different quantities and P4 should not conflate them.

---

## 5 · Decisions taken, with basis

1. **S_SUN_MEAN = 0.1694 is retained** as the solar mean on the HKP-2 S scale. Basis: F1.
2. **Baliunas' solar ⟨S⟩ = 0.179 is not used anywhere in P4**, including as a cross-check or in
   figures. Basis: F2, F3. Where the Baliunas Table 2 solar row is reproduced (it is a legitimate
   part of the catalogue), it must be footnoted as a proxy estimate superseded by Egeland.
3. **The solar series is placed on the HKP-2 scale using Egeland, not by an in-house K→S
   transformation.** Basis: F3, F5.
4. **Egeland Table 4 is adopted as the preferred solar S source**, subject to obtaining it —
   see §6. Basis: F5.
5. **Cycle-mean stability and cycle-amplitude decline are reported as separate quantities.**
   Basis: F6.
6. **The HKP-1 → HKP-2 quadratic (Eq. 3) is recorded but not applied by P4.** Basis: §3.1. P4
   does not reduce raw HKP-1 data; the conversion matters only for understanding why Baliunas'
   1966–1977 segment and its post-1977 segment are commensurable at all.

---

## 6 · Unresolved (grade C or X), and one action item

**No value in this unit is graded C or X.**

| Item | Status | Disposition |
|---|---|---|
| Egeland Table 4 machine-readable file | **not obtained** — published at the journal (IOP); the sandbox network allows only the domains listed in the environment configuration, and neither IOP nor the CDS mirror is among them | **Action item**, not a grade-C value. Retrieve outside the sandbox. The in-paper sample rows and column definitions are extracted above, so the file's structure is known in advance. |
| Donahue reprocessing vs Baliunas 1995 | not addressed by this paper | recorded; moot under A2 decision (a) |
| HD 10476 ⟨S⟩ 0.198 vs 0.1896 | not addressed by this paper | escalated to **A6** |

The related Harvard Dataverse deposit for the underlying composite Ca II K index
(Pevtsov 2016, doi:10.7910/DVN/VF5BMO) is cited in the references and is also outside the
permitted domains.

---

## 7 · Open questions from protocol §11 — status after A3

| # | Question | Status |
|---|---|---|
| 5 | Are the star and Sun S-indices on the same scale? | **Closed: yes, provided Egeland's solar value is used.** Both are HKP-2 S. Baliunas' *stellar* values are direct HKP-2 measurements; Baliunas' *solar* value is a proxy estimate and must be discarded (F2, F3). |

Remaining open across the audit: question 2 (binaries — decide at consolidation) and question 6
(Baliunas vs Saar classification agreement — **A6**).

---

## 8 · Consequence for P4

The solar calibration constant survives the audit unchanged, which is the least interesting
outcome and also a genuine relief — it was corrected before this audit began and the correction
was right.

The two things that change are both about *amplitude*. First, the Baliunas solar amplitude is
inflated ~76%, so any solar-versus-stellar variance comparison must be built on Egeland's
calibration or not made at all. Second, and more usefully, Table 2 hands P4 a sourced,
grade-A statement that solar cycle amplitude fell by half from cycle 22 to cycle 24, with cycle 24
the weakest of ten. That is a stronger and more defensible empirical hook for the paper's
motivation than anything currently in `paper_state_v2`, and it is measured on exactly the index
the stellar comparison uses.

The action item in §6 is the one thing that needs doing outside this environment. If Egeland
Table 4 can be retrieved, P4's solar track should be rebuilt on it: it is already homogenised
across five instruments, already on HKP-2, and already spans ten cycles — which would also extend
the solar series well beyond the 1966–2021 window currently planned, and correspondingly improve
the DFA statistics that A2 and A4 confirmed are viable only for the Sun.

---

## 9 · Audit log entry

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | closed | 2026-07-28 | `audit/A1_baliunas.md`, `audit/baliunas_table2_full.csv` | F1–F9 | none |
| A2 Lockwood | closed | 2026-07-29 | `audit/A2_lockwood.md` | F1–F7 | none |
| A4 Dakos | closed | 2026-07-29 | `audit/A4_dakos.md` | F1–F8 | none (2 → A5) |
| A3 Egeland | **closed** | 2026-07-29 | `audit/A3_egeland.md` | F1–F6 | none (1 action item; 1 → A6) |

**Next in sequence:** A5 (Peng et al. 1994) — inherits the DFA rescaling convention and the
H = (β+1)/2 relation from A4 F7 and F8.
