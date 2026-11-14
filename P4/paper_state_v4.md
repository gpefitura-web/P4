# paper_state.md — P4
# Critical Slowing Down Near Stellar Activity Minima
# Version 4.0 | Consolidation of audit units A1–A6

**Date:** 2026-07-30
**Supersedes:** `paper_state_v2.md`, which is now **superseded in its entirety** and must not be
used as a source for any number. See §5 for the list of corrections.
**Status:** audit phase, 6 of 8 units closed. Pipeline frozen. Manuscript not started.

> **Rule inherited from the protocol and still in force.** No value enters the manuscript unless
> it appears in §2, §3 or §4 of this document with a source citation and a grade of A or B.
> Nothing graded C or X reaches the paper.

---

## 1 · Where the project stands

Six audit units are closed. The methodological core of the paper is now fixed from the sources,
with every parameter carrying a section-level citation, and the stellar catalogue has been
rebuilt from a two-pass OCR of the original table and independently cross-checked against a
second paper.

Three things have changed materially since v2, and all three are consequences of reading the
sources rather than recalling them:

1. **The sample has no empirical basis in its current form.** Of the twelve stars in the v2
   catalogue, one does not exist, four are misclassified, and two more are mislabelled. A1
   established this; A6 confirmed all four reclassifications from a second, independent paper.
2. **The significance testing has to be rebuilt.** Kendall τ p-values from `scipy` are
   inadmissible for rolling-window indicators. Dakos' surrogate procedure is fully specified and
   is now the required method.
3. **The flat/Maunder group has a measurement problem that no amount of analysis will fix.**
   The class is defined at a threshold inside the catalogue's own stated precision, and
   two-thirds of its members are the calibration standard stars. This must be argued around, not
   through.

The audit has not made the paper unpublishable. It has moved the argument onto ground that can
be defended, and it has done so before the real data were examined — which is the only order in
which these choices can legitimately be made.

---

## 2 · The frozen catalogue

**Source of record:** `audit/baliunas_table2_full.csv` — 112 rows (111 stars + the Sun),
all graded A (103) or B (9), checksum-validated against Baliunas §4.3 (52 / 31 / 29).
**Cross-check:** `audit/saar_baliunas_crossmatch.csv` — 70 rows joining Saar & Brandenburg 1999
Table 1 and Table 5 onto the catalogue.

The catalogue is **frozen**. The *selection* of P4's sample from it is not made here (§6.1).

**Three defects to repair when the catalogue is rewritten as `p4_star_catalog.csv`** (A6 F14 —
found while joining Saar onto it; none changes a classification):

| | Defect | Repair |
|---|---|---|
| a | **HD 219834A's period is missing** (`P_cyc` blank, `FAP = Good`, `grade = A`). A1 §1.2 has it: **21 ± 1 yr, Good**. | restore from A1 §1.2 |
| b | HD 76572's period likewise missing; `FAP = Poor`, `grade = A`, but `n_pass = 1` | re-extract, or re-grade to B |
| c | 32 rows carry OCR debris (`wee`, `vee`, `bee`, `Snes`, …) in `secondary` where the printed cell is blank | normalise to empty |

Confirmed intact: the six CYCLE rows with neither period nor FAP grade are exactly A2 F7's
tentative set (HD 10780, 88737, 111456, 126053, 176051, 185144).

### 2.1 Classification definitions — Baliunas+1995 Table 2 note (A1 §1.3, grade A)

| Class | Definition | N in catalogue |
|---|---|---|
| cycle | graded periodicity | 52 (incl. Sun) |
| `Var` | significant variability, no pronounced periodicity, timescales > 1 yr but ≪ 25 yr; ⟨σ_S/S⟩ ≳ 2% | 29 |
| `Flat` | ⟨σ_S/S⟩ < 1%–1.5% | 11 |
| `Flat?` | ⟨σ_S/S⟩ ≈ 1.5%–2% | 4 |
| `Long` | significant variability on timescales > 25 yr | 16 |

Baliunas' own §4.3 counting groups `Flat` + `Flat?` + `Long` = 31 as "flat or linear trends".
`Long` is a secular trend, not a third stable state.

### 2.2 FAP grades — Baliunas Table 2 footnote n (A1 §1.4, grade B)

excellent: FAP < 10⁻⁹ · good: 10⁻⁹–10⁻⁵ · fair: 10⁻⁵–10⁻² · poor: 10⁻²–10⁻¹

Six of the 52 "cycles" carry a query and **no FAP grade** (HD 10780, 88737, 111456, 126053,
176051, 185144). A cycling control group should require a graded FAP, which excludes these
(A2 F7).

### 2.3 Stars named in the sources as Maunder-minimum candidates

| HD | Named by | Basis | Saar's treatment |
|---|---|---|---|
| **3651** (54 Psc) | Baliunas App. A + Table 2 footnote q | steady decline since 1966; "entering a period of low-amplitude variation, similar to the solar Maunder Minimum" | **cycle, 14.6 yr, grade g** — *not* treated as flat |
| **9562** | Baliunas App. A | flat record, ⟨S⟩ ~20% below solar, but v sin i implies it is *younger* than the Sun | Table 5 flat star; predicted P_cyc **49 or 8 yr** |
| **10700** (τ Cet) | Baliunas App. A | σ_S/S = 1.2%, among the smallest in the survey | Table 1 flag **F**, tentative P_cyc 11? **rejected**, w = 0; Table 5 predicted **59 or 9 yr** |

Saar's flat list adds seven more (45067, 89744, 107213, 124570, **143761**, 178428, 207978,
212754 — of which 107213, 143761, 212754 and 9562 are Baliunas `Long`, not `Flat`). See §6.2.

### 2.4 Binarity — recorded, not decided

| Star | Status | Sources |
|---|---|---|
| **HD 81809** | Composite record. Baliunas App. A/B: 40-day P_rot inconsistent with ⟨S⟩ and colour; activity likely from the lower-mass (~K0 V) component. Saar note 7: tabulated spectral type and B−V are **the secondary's**; B−V listed 0.80: vs Baliunas 0.64. | A1 F7, A6 F11 |
| **HD 219834A/B** | Resolved visual pair. Saar keeps B (10.0 yr, grade e, w = 4) and **rejects** A's Baliunas cycle (21 ± 1, Good) under note 11, leaving only a > 25 yr trend. | A1 §2.5, A6 F10 |

Saar excludes near-equal-mass unresolved binaries on principle (HD 114378, HD 3443).

---

## 3 · Verified constants

| Constant | Value | Source and location | Grade |
|---|---|---|---|
| `S_SUN_MEAN` | **0.1694 ± 0.0005** | Egeland+2017 abstract and Table 2; arithmetic checksum on the 10 cycle means | **A** |
| ⟨S⟩_min (solar) | 0.1621 ± 0.0008 | Egeland Table 2 | A |
| ⟨S⟩_max (solar) | 0.177 ± 0.001 | Egeland Table 2 | A |
| ⟨ΔS⟩_cyc (solar) | 0.0145 ± 0.0012 | Egeland Table 2 | A |
| cycle-to-cycle scatter of ⟨S⟩_cyc | 0.002 | Egeland Table 2 | A |
| Cycle 22 → 24 amplitude decline | 0.0178 → 0.0089 = **−50.0%** | Egeland Table 2 | A |
| S scale | **HKP-2 by definition**; there is no scale-free S. Baliunas Table 2 ⟨S⟩ is on the same scale, so star–Sun comparison is direct | Egeland §2, §3.1 | A |
| Baliunas solar ⟨S⟩ = 0.179 | **proxy, not a measurement** — 5% high, amplitude inflated 76%. **Discard.** | A3 | A |
| Mount Wilson record end | 1991 March 31 | Baliunas §2 | A |
| ⟨S⟩ in Baliunas Table 2 | **annual mean over all years** ⇒ **N ≈ 25–26 per star** | Baliunas Table 2 note m, §2 | A |
| Lockwood instrumental floor | 0.8% in S | Lockwood §2.6 | A |
| **Baliunas long-term precision, 17 standards** | **1.4%** (1.2% excluding 4 variable standards; best stars 0.8–1.0%) | Baliunas Table 1, p. 271; **two arithmetic checksums** | **A** |
| Solar P_cyc / P_cyc(2) / P_cyc(L) | 10.0 yr / 84 yr (Gleissberg) / **44 yr** | Saar Table 1, Sun row | A |

**σ_S/S per star:** exists in Baliunas **Table 1** for the **17 standard stars only** (A6 §3,
grade A by two checksums). It does **not** exist for the 111-star catalogue. Not used as a
per-star quantity for P4. Only HD 143761 (ρ CrB, 1.0%) is both a standard star and in the current
sample.

---

## 4 · Method parameters — every row cited

### 4.1 Rolling-window indicators (AR(1), variance, skewness)

| Parameter | Value | Source |
|---|---|---|
| Rolling window, default | **50%** of series length | Dakos Step 3, Fig. 2 caption |
| Rolling window, sensitivity range | **25% – 75%** | Dakos Step 4 |
| Window type | sliding / overlapping | Dakos Step 3 |
| Detrending | Gaussian kernel smoothing (AR(1), variance, skewness **only**) | Dakos Step 2 |
| Gaussian bandwidth, Dakos default | **10% of series length** | Dakos Step 3 |
| Trend statistic | Kendall's τ | Dakos Step 3 |
| Trend reported on | **both** original and residual series | Dakos Step 3; A4 F6 |

### 4.2 Significance — the required procedure

| Element | Specification | Source |
|---|---|---|
| Null model | best-fit **ARMA(p,q)**, selected by AIC | Dakos Step 5 |
| Fitted to | the **residuals**, after detrending — not the raw series | Dakos Step 5 |
| Surrogates | **1,000**, same length as the residual series | Dakos Step 5, Fig. 11 |
| Per surrogate | re-estimate the rolling indicator, then its Kendall τ | Dakos Step 5 |
| p-value | **P(τ\* ≤ τ)** | Dakos Step 5 |
| Evaluated over | the full bandwidth × window grid | Dakos Step 5 |

**This replaces every `scipy` Kendall p-value in the pipeline.** All τ p-values in v2, including
the headline "+0.636, p < 0.0001", are inadmissible until recomputed.

### 4.3 DFA

| Parameter | Value | Source |
|---|---|---|
| Profile | cumulative sum of the mean-centred series | Peng p. 1685 col. 1 |
| Boxes | **non-overlapping**, length ℓ (overlap is an optional generalisation, note [14]) | Peng step (1) |
| Detrending | **linear least-squares fit within each box**; polynomial order **1** | Peng step (1); Dakos Table 3 fn 5 |
| Fluctuation | `F(ℓ) = √⟨y_d²⟩` — an RMS, not a variance | Peng note [15] |
| Exponent | α = slope of log F(ℓ) vs log ℓ | Peng note [16] |
| **n_min** | **4** | Peng note [16] |
| **n_max** | **no rule in Peng.** Peng's practice: N/12 … N/129 | Peng Figs. 3, 5 |
| Crossover | ℓ_× is a **second output** of the method; α is fitted **within one scaling regime** | Peng p. 1687 |
| Gaussian pre-filtering | **never** applied ahead of DFA | Dakos Table 3 fn 5 |
| Rolling window (solar DFA) | half the record | Dakos Step 3, Fig. 3 caption |
| Minimum series length | **> 100 points** | Dakos Methods, citing ref [27] = **Lenton et al. 2012** (not Dakos, not Peng) |

**α convention.** Peng's α is raw: **0.5 = uncorrelated**, > 0.5 = persistent, < 0.5 =
anticorrelated. Peng never mentions 1.5, "Hurst", any spectral quantity, or any rescaling. The
"DFA indicator rescaled to reach 1 (from 1.5)" belongs to **Livina & Lenton 2007** (Dakos ref
[7]), which the audit has not read. **P4 reports raw α on Peng's convention and states the
convention explicitly** until that paper is obtained.

### 4.4 Fixed decisions

| # | Decision | Basis |
|---|---|---|
| 1 | Use **Baliunas only**; uniform N ≈ 25–26 annual means. N is therefore uniform across groups **by construction**, so N cannot be confounded with group — state this in Methods. | A2 §5, decision (a) |
| 2 | **DFA is not applied to the stellar series.** N = 26 admits 4 ≤ n ≤ 6: two or three scales, under half a decade. | A4 F4, A5 F5 |
| 3 | DFA is reserved for the solar series, with a crossover check and a stated n_max and box count. | A5 F1, F2 |
| 4 | Significance by 1,000 ARMA surrogates (§4.2). | A4 decision 6 |
| 5 | Report τ on both the original and the residual series, including negative results. | A4 F6 |
| 6 | The Gaussian bandwidth is a **departure** from Dakos requiring its own justification and its own sweep (≥ 0.5%–20% of series length), stated as a percentage of series length alongside the value in years. | A4 F2, decision 8 |
| 7 | The Flat-group argument rests on **φ₁ (an autocorrelation), not on variance**. | A2 §8, A6 F6 |
| 8 | Every Flat-group member is flagged for whether it is a Baliunas standard star. | A6 F7, decision 6 |

---

## 5 · Corrections to `paper_state_v2` — do not reuse it

| v2 statement | Status |
|---|---|
| HD 4915 in the Maunder group | **Star does not exist.** Absent from all 19 pages of Baliunas. Removed permanently. |
| HD 32147 "Variable", ⟨S⟩ 0.396 | **cycle 11.1 ± 0.2 yr, Excellent**, ⟨S⟩ 0.286. Confirmed by Saar (11.1, grade e). |
| HD 103095 "Maunder/Flat", ⟨S⟩ 0.165 | **cycle 7.30 ± 0.08 yr, Excellent**, ⟨S⟩ 0.188. Confirmed by Saar (7.3, grade e). Baliunas uses it as evidence that old metal-poor stars *can* sustain vigorous cycles — the opposite of the v2 usage. |
| HD 166620 "Maunder/Flat", ⟨S⟩ 0.215 | **cycle 15.8 ± 0.3 yr, Excellent**, ⟨S⟩ 0.190. Confirmed by Saar (15.8, grade e). |
| HD 219834B "Irregular", ⟨S⟩ 0.159 | **cycle 10.0 ± 0.2 yr, Excellent**, ⟨S⟩ 0.204. Confirmed by Saar (10.0, grade e). |
| HD 143761 "Flat", ⟨S⟩ 0.144 | ⟨S⟩ **0.150**; Baliunas Table 2 class is **`Long`**. Contested — see §6.2. |
| HD 76151 "Variable, episodes of decline" | **cycle 2.52 ± 0.02 yr**, Fair, on a removed linear trend; secondary `Long`. |
| HD 190406 P_cyc = 16.9 | **Primary is 2.60 ± 0.02 yr.** 16.9 is the *secondary*. Confirmed independently by Saar (2.6 / 16.9). |
| ⟨S⟩ values for 10476, 81809, 149661, 114710, 190406 | all differ from Table 2; use the catalogue CSV |
| Stellar H column (1.677, 1.495, …) | **Stale and indefensible.** Produced by an older code path; current `dfa_hurst` returns NaN below N = 100. Delete. |
| `H = 1.235` (solar, full series) | **Not defensible.** Raw α, fitted across a crossover, out to 13.7 yr with 4 boxes at the top scale. |
| "DFA insensitive to the 11-yr cycle because nvals covers scales below ~5 yr" | **False against the code.** `n_max = N//4 = 5000 d = 13.7 yr`, 2.7× the claimed bound and longer than the cycle. Strike the sentence. |
| `H = (β+1)/2` | **Not sourced.** Absent from Dakos and from Peng. Grade X. |
| Kendall τ p-values, incl. "+0.636, p < 0.0001" | **Inadmissible.** Recompute per §4.2. |
| Methods sentence "Following Dakos et al. (2012), we removed the deterministic 11-yr cycle … σ = 1 yr" | **Overstates the warrant.** σ = 1 yr ≈ 1.8% of the record, at the bottom of Dakos' tested range and in the direction Dakos warns suppresses the variance signal. |
| Reference: "Schölzel 2019 — nolds" | **Remove.** The pipeline implements DFA natively; nolds is an unused optional import. |
| Data plan: VizieR / ADS downloads | Both blocked in the sandbox. Egeland Table 4 is an action item (§8). |

---

## 6 · Decisions left for human consolidation

These are **not** audit questions. Each requires a judgement the audit deliberately did not make.

### 6.1 Sample selection — the largest one
A1 removed the empirical basis for the three-group design. Baliunas does contain genuine members
for both groups (11 `Flat`, 4 `Flat?`, plus three named Maunder candidates), but selecting them
is a sample-definition decision. Under protocol §1 it must be made **from the frozen catalogue,
before the real data are examined**. Inputs now available: §2.1 class definitions and counts,
§2.2 FAP requirement, §2.3 named candidates, §2.4 binarity, §6.2 flat-group ambiguity, and the
standard-star flag in the cross-match CSV.

### 6.2 What counts as "flat" — Baliunas and Saar disagree, and so do Baliunas' own two tables
Saar's criterion is "classified F **or** ΔS/⟨S⟩ ≤ 1.5%", which merges `Flat`, `Flat?` and part of
`Long`. Four of his ten Maunder candidates (9562, 107213, 143761, 212754) are Baliunas `Long`.
**HD 143761 (ρ CrB)** is the sharp case: Baliunas Table 2 primary class = `Long`; Baliunas
Table 1 σ_S/S = **1.0%**, inside the `Flat` definition; Saar lists it as flat/Maunder. All three
statements are grade A. Pick a definition and state it, or drop the star.

### 6.3 Binaries
HD 81809 (composite; both papers indicate the tabulated parameters are the secondary's) and
HD 219834A/B (resolved pair; Saar rejects A's cycle, keeps B's). See §2.4.

### 6.4 Gaussian bandwidth (A4 F2)
Genuine methodological tension, not an error. σ = 1 yr removes a **deterministic 11-yr cycle**,
which is not the monotonic detrending Dakos' step was designed for; Dakos' own 10%-of-length
default (5.5 yr here) would leave most of the cycle in the residuals. Defensible, but it is a
departure from the cited source, not an application of it. Requires human judgement.

### 6.5 The flat group's measurement problem (A6 F6, F7, F13)
The `Flat` threshold (< 1–1.5%) sits inside Baliunas' own stated long-term precision (1.4%,
1.2% excluding four variable standards). Seven of the 11 `Flat` stars, and 8 of Saar's 10
Maunder candidates, **are the calibration standard stars** — selected for constancy and used to
define the zero point. And no second measurement of any flat star exists in the audited
literature: Saar has zero Baliunas `Flat` stars in Table 1, only Table 5 predictions. Decide how
to present this. Decisions 7 and 8 in §4.4 are the minimum response.

### 6.6 The 44-yr solar component (A6 F12)
Saar assigns the Sun P_cyc(L) = 44 yr. P4's record is 55 yr. A 44-yr component is nearly
degenerate with a monotone trend in a rolling-window statistic, and neither the σ = 1 yr Gaussian
filter nor a linear detrend removes it. Decide whether this can be addressed at all in a 55-yr
record, and say so either way.

---

## 7 · Sequenced plan for the remaining work

| # | Conversation | Depends on | Product |
|---|---|---|---|
| 1 | **A8 — Usoskin+2017** | — | `audit/A8_usoskin.md`: quantitative characterisation of the 2008–2010 minimum in a century-long context; cycle 24 vs 15–23; grand-minima frequency, duration, entry definition; **any published claim that grand minima are unpredictable** (protocol Q7 — P4 must engage with it, not ignore it) |
| 2 | **A7 — Scheffer+2009 & Held & Kleinen 2004** | — | `audit/A7_theory.md`: claim-to-citation map for the Introduction; formal bifurcation↔autocorrelation link; AR(1)/variance/recovery-rate relations; stated limitations and false-positive caveats; **resolve the Eddy 1976 gap** (add the PDF or re-source every Maunder claim to Usoskin+2017 / Baliunas §5) |
| 3 | **Consolidation (human-led)** | A1–A8 | `P4_SOURCE_VALUES.md` + `p4_star_catalog.csv`. Settles §6.1–§6.6. **The sample is selected here, from the frozen catalogue, before any real data are seen.** |
| 4 | **Pipeline rebuild, single pass** | consolidation signed off | Implement §4 against the frozen reference: ARMA surrogate significance (§4.2), DFA n_max + crossover check (§4.3), bandwidth sweep, catalogue swap. No exploratory changes. |
| 5 | **Real data acquisition** | action items §8 | Egeland Table 4 for the solar series. Must happen outside the sandbox. |
| 6 | **Analysis on real data** | 4 + 5 | Re-run; expect the solar CSD signal to weaken substantially under surrogate testing |
| 7 | **Figures** | 6 | 4 figures, Super Mongo style per `UNIVERSAL_PAPER_CONTEXT.md` |
| 8 | **Manuscript** | 6, 7 | Introduction/Theory from A7; Discussion from A8 + §6.5 + §6.6 |

**Sign-off condition (protocol §7) unchanged:** all units closed, nothing graded C or X in
`P4_SOURCE_VALUES.md`, every methodological parameter carrying a section-level citation.

---

## 8 · Action items — all blocked inside the sandbox

Permitted: `github.com`, `raw.githubusercontent.com`, `api.github.com`, PyPI, npm.
Blocked: IOP, VizieR, NASA ADS, Zenodo, Harvard Dataverse, AGU/Wiley, APS, Nature.

| # | Item | Needed for | Blocking? |
|---|---|---|---|
| 1 | **Egeland+2017 Table 4** — machine-readable solar S, cycles 15–24 | the solar series itself | **yes, blocks step 5** |
| 2 | **Livina & Lenton 2007, GRL 34** | the DFA-indicator rescaling; also the origin of the "DFA indicator" framing v2 leans on | no — report raw α meanwhile |
| 3 | A source for **H = (β+1)/2** (Dakos cites Schroeder 1991, a book) | the spectral track | no — drop the claim if unsourced |
| 4 | **Peng et al. 1993, PRE 47, 3730** | DFA finite-length bias | no |
| 5 | **Brandenburg, Saar & Turpin 1998 (Paper I)** | explains Saar's P_cyc for HD 3651 and 149661 | no |
| 6 | **Radick et al. 1998** | Saar's revision of HD 201092 | no |
| 7 | **Baliunas & Jastrow 1990** | the original "Maunder-minimum stars" claim both papers rely on | no |
| 8 | **Eddy 1976, Science 192, 1189** | Introduction citations — or re-source them (A7) | no |

---

## 9 · Audit log

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | closed | 2026-07-28 | `audit/A1_baliunas.md`, `audit/baliunas_table2_full.csv` | F1–F9 | none (2 → A3) |
| A2 Lockwood | closed | 2026-07-29 | `audit/A2_lockwood.md` | F1–F7 | none (2 → A3) |
| A3 Egeland | closed | 2026-07-29 | `audit/A3_egeland.md` | — | none (1 action item) |
| A4 Dakos | closed | 2026-07-29 | `audit/A4_dakos.md` | F1–F8 | none (2 → A5) |
| **A5 Peng** | **closed** | 2026-07-30 | `audit/A5_peng.md` | F1–F6 | 3 grade X → action items |
| **A6 Saar** | **closed** | 2026-07-30 | `audit/A6_saar.md`, `audit/saar_baliunas_crossmatch.csv` | F1–F13 | 3 grade X → consolidation |
| A7 Theory | open | | | | |
| A8 Usoskin | open | | | | |

### Protocol §11 open questions

| # | Question | Status |
|---|---|---|
| 1 | Is DFA admissible for the stellar series? | **Closed: no.** Data (A1), extension (A2), method floor (A4), algorithm (A5) all agree. |
| 2 | Do binaries stay in the sample? | **Open — consolidation.** Evidence recorded, A1 F7 / A6 F10, F11. |
| 3 | How is significance established? | **Closed.** §4.2. |
| 4 | Is N confounded with group? | **Closed: no.** Uniform by construction (A2 §5). |
| 5 | Are star and Sun S on the same scale? | **Closed: yes**, HKP-2 (A3 §3.1). |
| 6 | Do Baliunas and Saar agree on classifications? | **Closed, asymmetrically.** Cycling: yes, 24/30 periods identical. Flat: the question does not arise — Saar has no flat-star measurements (A6 F13). |
| 7 | Has anyone claimed grand minima are unpredictable? | **Open → A8.** |
| 8 | Is Eddy 1976 replaceable? | **Open → A7.** |

### Two corrections to the protocol itself

1. **§2 scope table misclassifies Peng+1994 as "native".** It is a scan carrying a poor
   pre-existing OCR layer (A5 head note). Two-pass treatment was required.
2. **§A2 preamble undercounts the Lockwood overlap.** Seven of the P4-relevant stars appear, not
   five: HD 103095 and HD 143761 were missed by the preliminary scan (A2 F4).

---

## 10 · Files

| File | Role |
|---|---|
| `P4_AUDIT_PROTOCOL.md` | the audit's terms of reference |
| `audit/A1_baliunas.md` … `audit/A6_saar.md` | closed unit deliverables |
| **`audit/baliunas_table2_full.csv`** | **the frozen catalogue — source of record for all stellar values** |
| **`audit/saar_baliunas_crossmatch.csv`** | Saar × Baliunas join; period diffs, standard-star flag, Table 5 predictions |
| `paper_state_v4.md` | **this file** — supersedes v2 |
| `p4_pipeline.ipynb` | **frozen** until consolidation is signed off |
| `bib/` | the nine source PDFs |
