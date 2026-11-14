# Audit A2 — Lockwood et al. 2007, ApJS 171, 260

**Date:** 2026-07-29
**Extraction method:** native text layer via PyMuPDF (44 pp., ~74 kB of text; no OCR needed for
body or tables). Pages 8–29 are vector figure plates carrying no text layer — their axis
ranges and panel labels were obtained by rendering at 300 dpi and OCR'ing with `--psm 11`.
**Pages read:** all 44 (journal pp. 260–303). Table 1 = p. 262; Figure 3 (HK + photometric time
series) = pp. 266–289; Table 2 = pp. 298–299; Table 3 = p. 300; §2.6 (HK data) = p. 264.
**Depends on:** A1 (closed).

---

## 1 · The question this unit exists to answer

> Does the Mount Wilson stellar sample get *longer* — and if so, for which stars, by how much,
> and on what scale?

**Answer: no, not in any form the audit can use.** Lockwood et al. 2007 publishes no numerical
Ca II time series for any star. The extension exists, but only as ink on a figure.

---

## 2 · Values extracted

### 2.1 What the paper actually tabulates

| Table | Location | Content | Contains an S time series? |
|---|---|---|---|
| Table 1 | p. 262 | HD, V, M_V, B−V, spectral type, **mean S-index**, log R′_HK, variability flag, trend | no — a single mean per star |
| Table 2 | pp. 298–299 | comparison stars; n_L, n_F, n_lap, n_pre, n_tot; rms dispersions σ_b, σ_y, σ_by | no — **photometric only** |
| Table 3 | p. 300 | dispersions for 5 stars with one slightly variable comparison star | no — photometric only |

No machine-readable supplement is announced anywhere in the paper. Grade **A** (native text,
whole document searched).

### 2.2 Sample and observing spans

| Quantity | Value | Location | Grade |
|---|---|---|---|
| Program stars | **32** (+ the Sun in Table 1) | §2 | A |
| Selection | main sequence / near, 0.42 ≤ B−V ≤ 1.4; all but five drawn from Wilson's 91 | §2, Abstract | A |
| Lowell photometry | 1984 March – 2000 June, ~1200 nights, 0.5 m | §2.1 | A |
| Fairborn photometry | 1993 – 2003, 0.75 m | §2.2 | A |
| Total photometric span | **13–20 yr** per star | Abstract, §2 | A |
| Ca II HK source | Mount Wilson HK Project (Wilson 1978; Vaughan+1978; Duncan+1984; Baliunas+1995, 1998) | §2.6 | A |
| HK cadence | three measurements per star per night → a **nightly mean** | §2.6 | A |
| HK series as plotted | **~1985 – 2005** (Fig. 3 abscissa) | Fig. 3, pp. 266–289 | B |
| Solar HK series | 1976 – 2004, three full sunspot cycles | §4.1 | A |

### 2.3 Per-star coverage for the P4-relevant stars

`n_tot` is the total span in years of the *photometric* record from Table 2; the abstract states
the parallel HK data span the same interval.

| HD | In Lockwood? | n_L | n_F | n_tot (yr) | ⟨S⟩ Lockwood | ⟨S⟩ Baliunas (A1) | Δ |
|---|---|---|---|---|---|---|---|
| Sun | yes (Table 1 only) | — | — | 1976–2004 | 0.1783 | 0.179 | −0.4% |
| 10476 | **yes** | 16 | 10 | 19 | 0.1896 | 0.198 | **−4.2%** |
| 81809 | **yes** | 17 | 11 | 20 | 0.1713 | 0.172 | −0.4% |
| 103095 | **yes** | 17 | 11 | 20 | 0.1876 | 0.188 | −0.2% |
| 114710 | **yes** | 17 | 4 | 17 | 0.1991 | 0.201 | −0.9% |
| 143761 | **yes** | 17 | 9 | 18 | 0.1492 | 0.150 | −0.5% |
| 149661 | **yes** | 14 | 11 | 20 | 0.3327 | 0.339 | −1.9% |
| 182572 | **yes** | 16 | 11 | 20 | 0.1486 | 0.148 | +0.4% |
| 3651 | no | — | — | — | — | 0.176 | — |
| 9562 | no | — | — | — | — | 0.136 | — |
| 10700 | no | — | — | — | — | 0.171 | — |
| 32147 | no | — | — | — | — | 0.286 | — |
| 76151 | no | — | — | — | — | 0.246 | — |
| 166620 | no | — | — | — | — | 0.190 | — |
| 190406 | no | — | — | — | — | 0.194 | — |
| 219834A/B | no | — | — | — | — | 0.155 / 0.204 | — |

### 2.4 Lockwood's 32 stars classified by the A1 Baliunas classes

| Baliunas class | N in Lockwood |
|---|---|
| cycle | 19 |
| Flat | 5 — HD 13421, 124570, 158614, 182572, 216385 |
| Long | 3 — HD 25998, 35296, 143761 |
| Var | 5 — HD 39587, 75332, 115383, 129333, 131156A |
| Flat? | **0** |

Grade **A** (join of two graded tables).

---

## 3 · Checks performed

- **Is any HK series tabulated?** All three tables inspected column by column → **no**. pass.
- **Do the figure panels extend the Baliunas window backwards?** Axis ranges OCR'd on four
  independent figure pages (pp. 8, 9, 15, 22, 29): all read ~1985–2005, none earlier →
  **finding F2**.
- **Is the S scale the same as Baliunas 1995?** §2.6 states the data were reprocessed by
  Donahue; differences from the 1995 compilation are "usually less than 1%–2%". Measured against
  the A1 values for the seven overlapping stars: six agree within 2%, **HD 10476 differs by
  −4.2%** → **finding F3**.
- **Machine-readable supplement?** Searched for "machine-readable", "electronic edition",
  "online only", "supplement" → none. pass.
- **Sample count reconciles?** 34 stars in Paper II, minus HD 203387 (luminosity class III) and
  HD 176095 (no reliable comparison star) = 32. Table 1 rows counted = 32 + Sun. pass.

---

## 4 · Findings

**F1 — Lockwood et al. 2007 cannot extend the P4 stellar series.** The paper's own Ca II data are
published only as Figure 3 light curves. Under protocol §5, "anything read off a plot rather than
a table is grade C by definition", and grade C cannot reach the manuscript. Digitising Figure 3
would additionally sit close to the program's standing prohibition on deriving one's own
photometry (UNIVERSAL_PAPER_CONTEXT §2.1), and would produce a series whose per-point
uncertainty is unknown. There is no admissible route from this paper to a longer series.

**F2 — even graphically, the extension does not overlap most of the Baliunas window.**
Figure 3 spans ~1985–2005. Baliunas spans 1966–1991 March. The overlap is only ~1985–1991; the
genuinely new coverage is ~1991–2004. So Lockwood is not a continuation of a 1966-based record
in the plots either — it is a partially overlapping second window.

**F3 — the two papers are not on the same S scale, and one star exceeds the stated tolerance.**
§2.6 records that the HK data have been reprocessed several times, most recently by Donahue, with
differences from the 1995 compilation "usually less than 1%–2%". HD 10476 differs by 4.2%
(0.198 → 0.1896). Both values are grade A in their own source. This is recorded as a
contradiction, not resolved (protocol rule 4). Any future work that mixes the two compilations
inherits a few-percent systematic; P4 currently plans to use Baliunas values only, so the
exposure is nil as long as that holds.

**F4 — the sample coverage is worse than the preliminary scan suggested, and also different.**
The protocol's preliminary scan reported that 5 of the 14 stars appear (HD 10476, 81809, 114710,
149661, 182572). Two more are present: **HD 103095 and HD 143761**, both in Table 1 and both with
a Figure 3 panel. The correct count is 7 of the P4-relevant stars plus the Sun. The scan was
incomplete; the protocol's §A2 preamble should be corrected.

**F5 — Lockwood contains no Flat? stars and only 5 Flat stars.** If P4 ever wanted post-1991
coverage for its low-activity group, only HD 13421, 124570, 158614, 182572 and 216385 would have
any, and only as figures. None of the paper's three named Maunder-minimum candidates
(HD 3651, 9562, 10700 — A1 finding F5) is in Lockwood's sample at all.

**F6 — the instrumental noise floor is 0.8% in S.** §2.6: an iterative standardisation procedure
"yields an average standard deviation relative to S of 0.8% in the flattest stellar records".
This is a hard floor and it sits directly beneath Baliunas' Flat threshold of ⟨σ_S/S⟩ < 1%–1.5%
(A1 §1.3). The Flat class is therefore defined barely above the measurement noise — at most a
factor ~1.9 in σ, and for the flattest stars essentially at it. Any P4 claim that Flat stars show
*low variance* must reckon with the possibility that it is measuring the instrument. This is a
Discussion-section obligation, and a referee will raise it.

**F7 — six of Baliunas' 52 "cycles" carry tentative periods with no FAP grade.**
Noticed while joining the two samples: HD 10780 (">7"), 88737 ("24?"), 111456 ("7?"),
126053 ("22?"), 176051 ("10?") and 185144 = σ Dra ("7?") appear in the cycle column with a
question mark and **no FAP grade**. They are counted among the 52 (the A1 checksum requires it),
but their periods are not formally significant. A cycling *control* group for P4 should require
a graded FAP, which excludes these six.

---

## 5 · Decision required by the protocol

The protocol asks A2 to choose one of:

> (a) use Baliunas only, uniform N, note the lost coverage as a limitation
> (b) use extended series only for the subset, with N as an explicit covariate
> (c) restrict the sample to stars with comparable N

**Decision: (a) — use Baliunas et al. 1995 only, uniform N ≈ 25–26 annual means per star.**

Basis: F1. Option (b) presupposes an extended series exists in usable form; it does not, for any
star. Option (c) is vacuous for the same reason — every star already has comparable N precisely
*because* no extension is available. The lost 1991–2004 coverage is recorded as a stated
limitation of the stellar analysis.

**Consequence, and it is a favourable one.** Protocol open question 4 asked whether N is
confounded with group membership. Because no star gains points, **N is uniform across all groups
by construction, and the confound cannot arise.** The risk the protocol flagged as "fatal in
review" — a between-group AR(1) difference that is really a series-length artefact — is closed,
not by handling it but by the absence of the thing that would have caused it. This should be
stated explicitly in Methods rather than left implicit.

---

## 6 · Unresolved (grade C or X)

**None.** No value in this unit is graded C or X. Two items are recorded as contradictions rather
than resolved, per protocol rule 4:

| Item | Status | Disposition |
|---|---|---|
| HD 10476 ⟨S⟩: 0.198 (Baliunas) vs 0.1896 (Lockwood), −4.2% | both grade A in their own source | recorded; no impact while P4 uses Baliunas only. Revisit at **A3** if the solar and stellar scales must be reconciled. |
| Whether the Donahue reprocessing supersedes Baliunas 1995 | not stated in either paper | **A3 (Egeland+2017)**, which addresses HKP-1 → HKP-2 |

---

## 7 · Open questions from protocol §11 — status after A2

| # | Question | Status |
|---|---|---|
| 1 | Is DFA admissible for the stellar series? | **Closed: no.** N ≈ 25–26 annual means, and A2 establishes no extension is obtainable. Final algorithmic confirmation at A5, but the data question is settled. |
| 2 | Do binaries stay in the sample? | Still open (A1 F7 recorded; decide at consolidation). |
| 4 | Is N confounded with group? | **Closed: no.** N is uniform by construction — see §5. |
| 5 | Are star and Sun S-indices on the same scale? | Still open; A2 adds that a *third* scale (Donahue reprocessing) exists. → **A3**. |

---

## 8 · Consequence for P4

Two things change.

The stellar analysis is now firmly fixed as **AR(1) and variance on ~25–26 annual means per
star**, with DFA reserved for the solar series. That was already the working position; it is now
sourced rather than assumed, and the uniform-N argument in §5 turns what looked like a weakness
into a clean statement about the design.

The harder consequence is F6. The Flat class is defined at ⟨σ_S/S⟩ < 1%–1.5% against an
instrumental floor of 0.8%. P4's expected result — low φ₁ and low σ² in the Flat group — is
partly a statement about a group *defined* by having small σ, measured close to the noise. The
comparison that survives this objection is between **φ₁ (an autocorrelation, not an amplitude)**
across groups, not between variances; and the argument should be made in those terms. Worth
settling at A4, where the Dakos indicator definitions are fixed.

---

## 9 · Audit log entry

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | closed | 2026-07-28 | `audit/A1_baliunas.md`, `audit/baliunas_table2_full.csv` | F1–F9 | none (2 escalated to A3) |
| A2 Lockwood | **closed** | 2026-07-29 | `audit/A2_lockwood.md` | F1–F7 | none (2 contradictions recorded, escalated to A3) |

**Next unit in sequence:** A4 (Dakos et al. 2012) — all method parameters, and the surrogate
significance procedure the current pipeline lacks. A3 (Egeland) now carries three inherited
questions rather than one.
