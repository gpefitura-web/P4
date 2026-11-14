# Audit A6 — Saar & Brandenburg 1999, ApJ 524, 295

**Date:** 2026-07-30
**Extraction method:** three independent passes. (1) Genuine native text layer via PyMuPDF —
page 1 carries zero embedded images, so this is real digital text, not an OCR layer. (2)
Coordinate-aware reconstruction: `get_text("words")` with x-boundaries taken from the Table 1
column headers, rows anchored on the HD column. (3) PyMuPDF render at 700 dpi + Tesseract 5
`--psm 6` over four cropped bands. Passes (2) and (3) are independent methods and are diffed
cell by cell.
**Pages read:** all 16 (journal pp. 295–310). Table 1 = pp. 297–298 (PDF pp. 3–4); §2 individual
stars = pp. 296–300; §2.1 selection rules = p. 296; Table 5 and the flat-star prediction = p. 308
(PDF p. 14); §5 summary = pp. 309–310.
**Also re-opened:** Baliunas et al. 1995 **Table 1**, p. 271 (PDF p. 3) — see §3.
**Depends on:** A1 (closed), A2 (closed), A3 (closed).

> **Glyph trap, and it is the same one A4 hit.** In this PDF's text layer the character `[`
> renders as **two different printed symbols**: a minus sign in `B[V` → `B−V` and in
> `[4.433` → `−4.433`, and a greater-than sign in `[25` → `>25` in the cycle columns. Reading the
> text layer alone would have turned every "long-term trend, >25 yr" entry into a nonsensical
> negative period. Resolved by the 700 dpi render, which prints `>25` and `−4.433` unambiguously.
> This is the second paper in the audit where a single text-layer glyph maps to two printed
> characters; it should be treated as the default expectation for 1990s ApJ PDFs.

---

## 1 · Values extracted

### 1.1 Table 1 — structure

Fourteen columns, confirmed by header word-coordinates and by the rendered image:

`Branch,Symbol` | `HD` | `B−V` | `Spectral Type` | `M_V` | `log⟨R′_HK⟩` | `τ_c,E (days)` |
`τ_c,T (days)` | `P_rot (days)` | `P_cyc (yr)` | `P_cyc(2) (yr)` | `P_cyc(L) (yr)` | `w` | `Notes`

Contents: **61 entries — 60 stars plus the Sun**, in four blocks: Active/Inactive
(split at log⟨R′_HK⟩ = −4.75) × Better-Determined/Less-Certain behaviour. Grade **A**.

> **There is no ⟨S⟩ column.** The activity measure throughout is `log⟨R′_HK⟩`. This is decisive
> for the inherited HD 10476 question — see F1.

### 1.2 The Notes key (Table 1 footnote b) — verbatim sense

| Mark | Meaning |
|---|---|
| `p` `f` `g` `e` `u` `n` | **FAP grades from Bea95**: poor, fair, good, excellent, ungraded, **new** |
| `:` | variable |
| **`V`** | **irregular variable** |
| **`F`** | **flat activity** |
| `0` | modified τ_c,T and/or luminosity class based on new π, M_V |
| `1` | P_cyc from Paper I; P_cyc(2) or L (i.e. P_cyc > 25 yr) from Bea95 added here |
| `2` | new L (i.e. P_cyc > 25 yr) added |
| `3` | as in Paper I, no additions or changes |
| `4` | P_cyc present in only part of the time series |
| `5` | old P_cyc → P_cyc + P_cyc(2) |
| `6` | Gleissberg P_cyc(2) (Wolff 1976) |
| `7` | approximate spectral type, B−V **of the secondary star** (see Paper I) |
| `8` | P_cyc modified on the basis of Radick et al. 1998 |
| `9` | tentative P_cyc (new or "poor") **rejected** |
| `10` | added L (i.e. P_cyc > 25 yr) from Bea95 |
| `11` | "fair" or better Bea95 P_cyc **rejected** (see text) |
| `12` | photometric P_cyc (Strassmeier et al. 1997), ⟨S⟩ from Rutten 1987 |
| `13` | anomalously short P_cyc, may reflect … |

Grade **A** (native text + render agree). The `w` column is a qualitative reliability weight:
"The best detections (good or excellent FAP grades, very clear photometric cycles) were given a
weight w = 4, fair grades / moderately clear w = 2, and so on", reduced by a factor of 2 per
adverse factor (§2, p. 296). Grade **A**.

### 1.3 The Sun

| B−V | SpT | M_V | log⟨R′_HK⟩ | τ_c,E | τ_c,T | P_rot | **P_cyc** | **P_cyc(2)** | **P_cyc(L)** | w | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.66 | G2 V | 4.83 | −4.901 | 11.9 | 13.0 | 26.09 d | **10.0 yr** | **84 yr** | **44 yr** | 4,4 | e, n, 6 |

Grade **A** (word coordinates and 900 dpi OCR of the row agree token for token). P_cyc = 10.0
matches Baliunas Table 2 (10.0 ± 0.1, Excellent) exactly. P_cyc(2) = 84 yr is the Gleissberg
cycle (note 6, Wolff 1976). **P_cyc(L) = 44 yr** — see F12.

### 1.4 Selection rules for Table 1 (§2.1)

| Rule | Grade |
|---|---|
| Start from Paper I cycles with FAP ≤ 10⁻⁵ (good/excellent), then add Bea95 stars with FAP grade **at least "fair"** (FAP ≤ 10⁻²), plus stars with apparent long-term trends (= L) | A |
| Secondary periods P_cyc(2) with fair-or-better grades also considered, **if the primary was graded at least fair** | A |
| A few stars added that were not so classified in Bea95, at lower weight | A |
| Radick et al. 1998 plots (series extended to ~30 yr) used to confirm and in a few cases modify Bea95 | A |
| **Excluded:** unresolved binaries of nearly equal mass — **HD 114378 and HD 3443** — "since the stars' individual contributions to S are muddled" | A |
| **Excluded:** most stars with S series shorter than 12 yr | A |
| Acknowledged risk: new stars selected "primarily based on the visual appearance of their time series", so "there is clearly a risk of introducing **selection bias**" | A |

### 1.5 Table 5 — predicted cycle periods for flat-activity stars

Header prints "(days)" over the P_cyc column; this is a typographical error — the body text
gives the predictions in years ("we primarily list only those P_cyc ≥ 4 yr"). Where two values
appear they are the two branch solutions, in the order of the `Branch` column.

| Type | HD | B−V | SpT | M_V | P_rot (d) | **P_cyc predicted (yr)** | Branch | Baliunas primary class | Bea95 Table 1 σ_S/S |
|---|---|---|---|---|---|---|---|---|---|
| F | **9562** | 0.64 | G2 IV | 3.39 | 29 | **49 (A) / 8 (I)** | A,I | **Long** | 1.4% |
| F | **10700** (τ Cet) | 0.72 | G8 Vp | 5.68 | 34 | **59 (A) / 9 (I)** | A,I | **Flat?** | — |
| F | 45067 | 0.56 | F8 IV–V | 3.28 | 8 | 10 | A | Flat | 1.1% |
| F | 89744 | 0.54 | F7 IV | 2.78 | 9 | 16 | A | Flat | 1.2% |
| F | 107213 | 0.50 | F8 IV | 2.90 | 9 | 15 | A | **Long** | 1.5% |
| F | 124570 | 0.54 | F6 IV | 2.92 | 26 | 67 / 9 | A,I | Flat | 0.9% |
| F | **143761** (ρ CrB) | 0.60 | G0 V | 4.18 | 17 | **25 / 4** | A,I | **Long** | 1.0% |
| F | 178428 | 0.70 | G4 IV–V | 4.47 | 22 | 30 / 5 | A,I | Flat | — |
| F | 207978 | 0.42 | F0 V | 3.31 | 3 | 5 | A | Flat | 1.0% |
| F | 212754 | 0.52 | F5 IV | 2.78 | 12 | 30 / 4 | A,I | **Long** | 1.3% |

Table 5 also lists 10 young cluster stars (Hyades, UMa stream, Pleiades, α Per), not relevant to P4.

Footnote a: "**F: flat activity (in Maunder-like minimum?)**". Grade **A**.

**Saar's definition of the flat group** (§4, verbatim sense): "We have estimated P_cyc for all
stars in Bea95 with measured P_rot that are classified **F** *or* have **ΔS/⟨S⟩ ≤ 1.5%** in
**Table 1 of Bea95**." Method caveat, same paragraph: the estimates "are more uncertain, since we
can use only the ω_cyc/Ω versus Ro⁻¹ relation"; use of ⟨R′_HK⟩ "is inappropriate if these stars'
HK fluxes are reduced by the temporary cessation of cycles"; results "should be within
(~0.1–0.2 dex)" for "those F stars that emerge from Maunder minimum–like states". Grade **A**.

---

## 2 · Star-by-star comparison with Baliunas

Full join in **`audit/saar_baliunas_crossmatch.csv`** (70 rows: 61 Saar Table 1 entries +
9 Table 5 flat stars not in Table 1).

Of the 61 Saar entries, 59 are in the A1 catalogue (`Sun` and `HD 98230B` are not rows of
Baliunas Table 2). **30 pairs have a numeric primary period in both papers.**

### 2.1 Agreement — 24 of 30 identical to the last digit

HD 1835, 18256, 20630, 76151, 78366, 114710, 152391, 156026, 10476, 16160, 26965, 32147, 103095,
115404, 160346, 166620, 190406, 201091, 219834B, 155885, 194012, 206860, and the Sun, plus
HD 100180 (3.60 vs 3.56, inside Baliunas' stated ±0.04).

Saar drew these from the Mount Wilson database independently of A1's OCR of the printed table.
Under protocol §5 ("Where both papers cover a star, agreement raises the value to grade A"),
this **independently validates A1's extraction** and raises the agreeing periods to grade A on a
cross-paper basis rather than on OCR consensus alone.

### 2.2 Divergence — 6 of 30

| HD | Baliunas | Saar | Δ | Saar note | Reading |
|---|---|---|---|---|---|
| **165341A** | 5.1 ± 0.1, Fair | **15.5** primary, 5.1 secondary | +204% | `n,f,5` — note 5 = "old P_cyc → P_cyc + P_cyc(2)" | **Documented reclassification.** Saar promotes a *new* 15.5 yr period to primary and demotes Baliunas' 5.1 yr (retaining its "fair" grade) to secondary. |
| **201092** | 11.7 ± 0.4, Good | **10.5** | −10.3% | `g,1,8` — note 8 = "P_cyc modified based on Radick+1998" | **Documented revision** using a later dataset not available to Baliunas. |
| **149661** | 17.4 ± 0.7, Good | **16.2** | −6.9% | `g,g,1` — note 1 = "P_cyc from Paper I" | **Unexplained.** Both graded "good". Saar's value comes from Paper I, whose derivation is not reproduced here. Outside Baliunas' quoted ΔP. |
| **3651** | 13.8 ± 0.4, Good | **14.6** | +5.8% | `g,1` — note 1 = "P_cyc from Paper I" | **Unexplained.** 2σ beyond Baliunas' quoted ΔP, on the star A1 F5 identifies as the clearest Maunder-transition candidate. |
| **4628** | 8.37 ± 0.08, Excellent | **8.6** | +2.7% | `e,3` — note 3 = "as in Paper I, **no additions/changes**" | **Unexplained, and the note makes it worse:** Saar asserts no change, yet the value differs by ~3× Baliunas' quoted ΔP. |
| 100180 | 3.56 ± 0.04, Fair | 3.60 | +1.1% | `f,f` | Rounding; within ΔP. Not a divergence. |

Per protocol rule 4, **both values are recorded in the cross-match CSV; neither is chosen.**

### 2.3 Classification-level divergence — 5 stars

| HD | Baliunas primary class | Saar treatment | Saar note |
|---|---|---|---|
| 136202 | **Long** | cycle, 23 yr | `n,0` (new) |
| 187013 | **Long** | cycle, 25? — then **rejected** | `n,9,10` (note 9 = tentative, rejected) |
| 75332 | **Var** | cycle, 3.5? | `n` (new) |
| 224930 | **cycle, 10.2 ± 0.4, Poor** | cycle dropped; > 25 yr trend only, P_cyc(L) = 57 | — |
| **219834A** | **cycle, 21 ± 1, Good** | cycle **rejected**; > 25 yr trend, P_cyc(L) = 70: | `0,2,11` (note 11 = "'fair' or better Bea95 P_cyc rejected") |

### 2.4 The V and F flags

| HD | Saar flag | Baliunas primary class | Agreement? |
|---|---|---|---|
| 39587, 101501, 22049, 30495, 115383, 155886 | `V` (irregular variable) | **Var** (all six) | **yes** |
| 176095 | `V` | **Long** | no — but Saar's text says explicitly "HD 176095 (b) could be classified V instead" |
| 82885 | `V?` | **cycle, 7.9 ± 0.2, Fair** | no — Saar downgrades a graded cycle to a query |
| **10700** | **`F`** (flat activity) | **Flat?** | **yes** |

Saar's Table 1 contains **exactly one** F star and **no** Baliunas `Flat` star at all.

### 2.5 Baliunas classes of Saar's 59 matched stars

| Baliunas class | Count in Saar Table 1 |
|---|---|
| cycle | 42 |
| Long | 9 |
| Var | 7 |
| Flat? | 1 |
| **Flat** | **0** |

---

## 3 · Baliunas Table 1 — the σ_S/S question, resolved

A1 escalated "σ_S/S per star — not tabulated; only defined as class thresholds" to **A2/A6**.
Saar's flat-star criterion cites "ΔS/⟨S⟩ ≤ 1.5% in **Table 1 of Bea95**", which contradicts A1's
finding that no such column exists. Re-opening Baliunas+1995 settles it.

**Baliunas Table 1 (p. 271) is titled "STANDARD STARS".** It is not the catalogue — the catalogue
is Table 2, as A1 correctly established. It lists the **17 stars used as photometric standards**,
with columns `HD Number`, `B−V`, `⟨σ_S/S⟩`.

Extracted at 600, 900 and 1200 dpi under `--psm 6` and `--psm 4` — **six configurations, all in
exact agreement**:

| HD | B−V | ⟨σ_S/S⟩ | | HD | B−V | ⟨σ_S/S⟩ |
|---|---|---|---|---|---|---|
| 9562 | 0.64 | 1.4% | | 142373 | 0.56 | 0.8% |
| 13421 | 0.56 | 1.4% | | **143761** | 0.60 | **1.0%** |
| 29645 | 0.57 | 1.4% | | 159332 | 0.48 | 1.6% |
| 45067 | 0.56 | 1.1% | | 187013ᵃ | 0.47 | 2.2% |
| 76572ᵃ | 0.43 | 2.0% | | 187691ᵃ | 0.55 | 1.5% |
| 89744 | 0.54 | 1.2% | | 207978 | 0.42 | 1.0% |
| 107213 | 0.50 | 1.5% | | 212754 | 0.52 | 1.3% |
| 124570 | 0.54 | 0.9% | | 216385 | 0.48 | 0.8% |
| 136202ᵃ | 0.54 | 2.2% | | | | |

ᵃ the four standards that "appear to have low amplitude but significant variations" (§2.3).

**Two arithmetic checksums, both exact:**

| Stated in table | Recomputed from the 17 rows | Result |
|---|---|---|
| Mean ⟨σ_S/S⟩ (17 stars) = **1.4%** | 23.3 / 17 = 1.3706 → 1.4% | **PASS** |
| Mean ⟨σ_S/S⟩ (13 stars) = **1.2%** | (23.3 − 7.9) / 13 = 1.1846 → 1.2% | **PASS** |

The second checksum simultaneously confirms *which* four stars carry the footnote marker
(76572, 136202, 187013, 187691 — the four largest σ after 159332). Grade **A** by checksum.

Table 1 note, verbatim sense: *"The mean ⟨σ_S/S⟩ should represent the **upper limit of long-term
precision**. The least variable stars in this table have ⟨σ_S/S⟩ ~ 0.8%–1.0%. **Not all stars
with low variability are standards.**"* And §2.3: the combined calibration "yields a long-term
(25 yr) precision of stellar records of **~1.4% s.d.**, based on the average standard deviation
of the 17 standard stars … Eliminating those four stars yields a slightly improved estimate of
long-term precision, **1.2%**."

---

## 4 · Checks performed

- Text-layer glyph `[` disambiguated against a 700 dpi render → **finding**, resolved (see head note).
- Table 1 column assignment from header word-coordinates, cross-checked against OCR row order → **pass**.
- Coordinate parse vs 700 dpi OCR, cell by cell, on every P4-relevant row → **pass**, no disagreement.
- Sun row re-extracted at 900 dpi and compared to word coordinates token by token → **pass**.
- 30 cycle periods against Baliunas Table 2 → 24 exact, 1 rounding, **5 findings** (§2.2).
- Baliunas Table 1 at six OCR configurations → **pass**, unanimous.
- Baliunas Table 1 arithmetic checksums, 17-star and 13-star means → **both PASS**.
- Does Saar tabulate ⟨S⟩ anywhere? All five tables inspected column by column → **no** (F1).
- Saar Table 5 F-list against the A1 catalogue classes → **finding** (F4).
- Saar Table 5 F-list against the Baliunas standard-star list → **finding** (F7).

---

## 5 · Findings

**F1 — Saar provides no third ⟨S⟩ for HD 10476; the contradiction stands, two-way and open.**
The unit was asked to record three measures. There are only two. Saar & Brandenburg tabulate
`log⟨R′_HK⟩`, not ⟨S⟩, and for HD 10476 give **−4.912**. That number is not a usable third
measurement for two reasons: R′_HK is obtained from S through a colour-dependent photospheric
and basal correction, so it is not invertible without adopting a specific transformation; and
Saar's activity values derive from Bea95 and Paper I in the first place, so they would not be
independent even if they were invertible. The record therefore stands as:

| Source | ⟨S⟩ for HD 10476 | Grade in its own source |
|---|---|---|
| Baliunas+1995 Table 2 | **0.198** | A |
| Lockwood+2007 Table 1 | **0.1896** | A |
| Saar & Brandenburg 1999 | **not tabulated** (log⟨R′_HK⟩ = −4.912) | — |

The −4.2% discrepancy, against Lockwood's own stated 1–2% tolerance, is **unresolved and
escalated to consolidation**. A6 was the last unit with stellar values, so no further audit unit
can resolve it; it needs either a paper that tabulates S on both scales, or an explicit statement
in Methods that P4 uses Baliunas values throughout and inherits a few-percent systematic if ever
mixed. Note that P4's current position — Baliunas only (A2 decision (a)) — means the exposure is
nil in practice.

**F2 — Saar independently confirms A1's four reclassifications.** This is the single most useful
result of the unit. All four stars that A1 F3 found misclassified in `paper_state_v2` appear in
Saar's Table 1 as cycling stars, with periods identical to Baliunas' and with Saar's note
carrying Bea95's FAP grade:

| HD | `paper_state_v2` | Baliunas (A1) | **Saar** |
|---|---|---|---|
| 32147 | Variable | cycle 11.1, Excellent | **11.1**, note `e` |
| 103095 | Maunder/Flat | cycle 7.30, Excellent | **7.3**, note `e` |
| 166620 | Maunder/Flat | cycle 15.8, Excellent | **15.8**, note `e` |
| 219834B | Irregular | cycle 10.0, Excellent | **10.0**, note `e` |

Protocol open question 6 is answered for the cycling stars: **Baliunas and Saar agree, and agree
exactly.** A1 F3 is no longer a single-source finding.

**F3 — but they disagree on three periods with no stated reason, and one of them matters.**
§2.2: HD 3651 (+5.8%), HD 149661 (−6.9%), HD 4628 (+2.7%), all outside Baliunas' quoted ΔP, all
graded good-or-better in both papers, none carrying a note that explains the change — HD 4628
carries note 3, which positively asserts *no* change. Two further differences (HD 165341A,
HD 201092) are documented reclassifications rather than disagreements. HD 3651 is the star A1
singled out as Baliunas' clearest "caught in transition" Maunder candidate, and HD 149661 is in
P4's current Cycling group, so neither divergence is academic. Both values recorded; neither
chosen. The likely explanation for the first two — Paper I (Brandenburg, Saar & Turpin 1998),
which is where Saar says those periods come from — is not in the repository → **action item**.

**F4 — Saar's flat/Maunder group is broader than Baliunas' Flat class and crosses its
boundaries.** Saar's criterion is "classified F **or** ΔS/⟨S⟩ ≤ 1.5%". Against Baliunas' own
thresholds (A1 §1.3: Flat < 1–1.5%; Flat? ≈ 1.5–2%; Long = variability on > 25 yr timescales),
the ≤ 1.5% cut swallows the whole Flat class and the bottom of Flat?. In practice the resulting
Table 5 list crosses three Baliunas classes:

| Baliunas class of Saar's 10 F stars | Count | Which |
|---|---|---|
| Flat | 5 | 45067, 89744, 124570, 178428, 207978 |
| **Long** | **4** | **9562, 107213, 143761, 212754** |
| Flat? | 1 | 10700 |

**HD 143761 (ρ CrB) is in Saar's Maunder-candidate list.** A1 F4 argued the opposite — that
ρ CrB is "Long", not "Flat", and that treating it as post-transition flat is "a different claim
from the one the data support". Both readings are grade A in their own source, and Baliunas'
own Table 1 gives ρ CrB σ_S/S = **1.0%**, squarely inside the Flat definition, while Table 2
gives it the primary class Long. **The two Baliunas tables point in different directions for this
star.** Recorded, not resolved — this is a consolidation decision.

**F5 — σ_S/S does exist in Baliunas+1995, in Table 1, for 17 standard stars.** A1's escalated
item is closed, with a qualification in each direction. A1 F1 is correct: Table 2 has no σ_S
column, and there is no per-star σ_S/S for the 111-star catalogue. But the stronger reading — that
the quantity is nowhere tabulated — is too strong. For 17 stars it is, at grade A with two
arithmetic checksums (§3). Only **one** of them, HD 143761, is in P4's current sample. This does
not restore σ_S/S as a usable per-star quantity for P4, and A1 decision 6 stands; but it does
supply the calibration numbers that F6 rests on, and it explains what Saar was citing.

**F6 — the Flat class is defined at or below Baliunas' own stated measurement precision.**
This sharpens A2 F6, and now from the catalogue paper itself rather than from Lockwood:

| Quantity | Value | Source |
|---|---|---|
| Baliunas long-term (25 yr) precision, 17 standards | **1.4%** | Bea95 §2.3, Table 1 |
| same, excluding the 4 variable standards | **1.2%** | Bea95 Table 1 |
| least variable standards | **0.8%–1.0%** | Bea95 Table 1 note |
| Lockwood instrumental floor | 0.8% | Lockwood §2.6 (A2 F6) |
| **Baliunas `Flat` definition** | **⟨σ_S/S⟩ < 1%–1.5%** | Bea95 Table 2 note (A1 §1.3) |
| Baliunas `Flat?` definition | ≈ 1.5%–2% | same |

The Flat threshold sits *inside* the stated precision band, and Baliunas says as much: the mean
σ_S/S "should represent the **upper limit of long-term precision**". A star classified Flat is a
star whose variability could not be distinguished from the calibration noise over 25 years. Any
P4 claim that Flat stars exhibit *low variance* is therefore close to unfalsifiable at this
precision. As A2 already concluded, the comparison that survives is between **φ₁ — an
autocorrelation, not an amplitude** — and that argument must be made in those terms explicitly.

**F7 — selection circularity in the flat group, and it is severe.** Cross-matching Saar's
Table 5 against Baliunas' standard-star list:

- **8 of Saar's 10 flat/Maunder candidates are Baliunas standard stars** (9562, 45067, 89744,
  107213, 124570, 143761, 207978, 212754). Only 10700 and 178428 are not.
- **7 of Baliunas' 11 `Flat` stars are standard stars** (13421, 45067, 89744, 124570, 142373,
  207978, 216385), plus 1 of the 4 `Flat?` (159332).

The standard stars were selected *because* they were expected to be constant, and were then used
to define the calibration against which every other star's variability is measured. A group
defined by low variability, and populated mainly by the objects used to set the zero point,
cannot then serve as evidence that the low variability is astrophysical rather than instrumental.
Baliunas anticipates part of the objection — "Not all stars with low variability are standards" —
but that addresses the converse. P4 has two honest options: exclude standard stars from any Flat
group, or state the circularity and argue in terms of φ₁ rather than σ (per F6). A referee who
knows this literature will raise it.

**F8 — Saar does predict cycle periods for Maunder-state stars, and two of A1's three named
candidates are on the list.** This is the protocol's §4.4 item, delivered in Table 5 (§1.5):

- **HD 9562** → 49 yr (active branch) or 8 yr (inactive branch)
- **HD 10700** (τ Cet) → 59 yr or 9 yr
- **HD 143761** (ρ CrB) → 25 yr or 4 yr

with the stated accuracy "within ~0.1–0.2 dex", a floor of P_cyc ≥ 4 yr ("there is little
evidence for shorter periods"), and an unresolved two-branch ambiguity that spans a factor of ~6
for the A,I stars. These are model extrapolations from ω_cyc/Ω versus Ro⁻¹, **not measurements**,
and Saar flags them as the most uncertain in the paper. They are usable in P4's Discussion as a
published prediction to compare against, and for nothing else.

**A1's third candidate, HD 3651, is absent from Table 5** — Saar gives it a real cycle (14.6 yr,
grade g) plus a > 25 yr secondary and an 83 yr long trend. So the two papers differ in emphasis
on the one star A1 called "the paper's clearest star caught in transition": Baliunas Appendix A
and footnote q flag it as possibly entering a Maunder minimum after 1980; Saar treats it as an
ordinary cycling star on the inactive branch. Recorded, not resolved.

**F9 — τ Cet is not cleanly flat in either paper.** Saar Table 1 lists HD 10700 with
P_cyc = **11?**, w = **0**, notes `n,F,9` — simultaneously flagging it flat (F) and recording a
tentative 11 yr period which note 9 then **rejects**. Baliunas has it as `Flat?` with no period
and a note of possible increasing activity after 1988 (A1 §1.5, footnote r). If P4 uses τ Cet as
a settled Maunder analogue, both papers have to be quoted with their hedges intact.

**F10 — Saar rejects HD 219834A's cycle while keeping HD 219834B's.** Baliunas gives A a
21 ± 1 yr cycle at Good FAP; Saar rejects it explicitly (note 11, "'fair' or better Bea95 P_cyc
rejected") and records only a > 25 yr trend with P_cyc(L) = 70:. Component B keeps 10.0 yr at
grade e and w = 4. The pair is P4's second binary question; this does not settle it, but it means
the two components are treated asymmetrically in the more recent source.

**F11 — Saar independently corroborates A1 F7 on HD 81809.** Table 1 gives HD 81809 note **7**:
"approximate spectral type, **B−V of the secondary star** (see Paper I)", and lists B−V = 0.80:
(colon = uncertain) against Baliunas' 0.64. Saar is therefore also treating the tabulated
parameters as belonging to the companion rather than to the catalogued primary. Two papers now
independently indicate that HD 81809's catalogued properties do not describe the object producing
the signal. As a "clean cycling control" the star is compromised from both directions. The
binarity decision remains for consolidation (A1 decision 8), but the evidence is now stronger.

**F12 — Saar assigns the Sun a 44 yr long-trend period, and P4's solar record is 55 yr long.**
The Sun's row (§1.3) carries P_cyc = 10.0 yr, P_cyc(2) = 84 yr (Gleissberg) and
**P_cyc(L) = 44 yr**. P4's solar series runs 1966–2021, i.e. **55 yr**. A 44 yr component is
longer than half the record and would be very nearly degenerate with any monotone trend in a
rolling-window statistic — which is exactly what the Kendall τ on φ₁ measures. Worse, the Track B
filter (Gaussian, σ = 1 yr) is tuned to remove the 11 yr cycle and leaves a 44 yr component
completely intact, as does the linear detrend in Track A. This is a genuine confound for the
headline CSD result and it must be stated in Methods; whether it can be controlled for at all in
a 55 yr record is doubtful, and saying so is the honest course.

**F13 — the answer to protocol question 6 is asymmetric, and the asymmetry is the point.**
Saar's Table 1 contains 42 Baliunas cycling stars, 9 Long, 7 Var, 1 Flat? and **zero Flat**.
On cycling stars the two papers agree almost perfectly (F2). On flat stars Saar has **no
independent measurement at all** — flat stars enter only in Table 5, as model predictions
(F8). So "do Baliunas and Saar agree on the classifications?" resolves to: *yes for the cycling
stars, and for the flat stars the question does not arise, because there is only one measurement
in the literature.* Every claim P4 makes about the flat group rests on Baliunas alone — measured
at a precision that barely resolves the class (F6), on a sample largely composed of the
calibration standards (F7). That is the real finding of this unit.

**F14 — three defects in `baliunas_table2_full.csv`, found while joining Saar onto it.** The CSV
is the declared source of record for every stellar value in P4, so these matter even though none
is large. A1 closed with "unresolved: none"; that referred to OCR disagreements, and these are a
different class of problem — data that survived extraction but was lost or corrupted in assembly.

| # | Defect | Detail |
|---|---|---|
| a | **HD 219834A's cycle period is missing from the CSV** | The row has `P_cyc` and `dP` empty but `FAP = Good` and `grade = A`. A1's own §1.2 table gives **21 ± 1 yr, Good**. The value was extracted and verified, then lost in assembly. It is also one of the two stars in P4's binary question (§2.4 of `paper_state_v4`), and Saar's rejection of exactly this period (F10) cannot be assessed against a blank cell. |
| b | **HD 76572's period is likewise missing**, `FAP = Poor`, `grade = A`, and `n_pass = 1` — the lowest pass count in the file | Low impact (Poor grade, and Saar excludes it), but `grade = A` on a row built from a single pass is not defensible under protocol §4. |
| c | **32 rows carry OCR debris in the `secondary` column** where the printed cell is blank | Tokens observed: `wee` (18), `vee` (5), `a` (2), `bee`, `Lee`, `nee`, `Snes`, `see ;`, `_`, `...`. All are Tesseract renderings of the ellipsis used for an empty cell. Meaning is unaffected, but anything that joins or filters on `secondary` will treat them as content. |

One thing this check *confirms*: the six CYCLE rows with neither a period nor a FAP grade are
exactly A2 F7's tentative set — HD 10780, 88737, 111456, 126053, 176051, 185144. That finding
reproduces cleanly from the file.

**Disposition:** all three are repaired at consolidation, when the catalogue is rewritten as
`p4_star_catalog.csv`. (a) is restored from A1 §1.2; (b) is either re-extracted or re-graded to B;
(c) is normalised to empty strings. The audit does not edit A1's deliverable in place.

---

## 6 · Decisions taken, with basis

1. **The HD 10476 ⟨S⟩ contradiction is recorded with two entries, not three, and escalated to
   consolidation.** Basis: F1 — Saar tabulates no ⟨S⟩, so the expected third measure does not
   exist. No remaining audit unit can resolve it.
2. **Baliunas Table 1 σ_S/S is admitted at grade A for the 17 standard stars only.** Basis: §3,
   six-configuration agreement plus two arithmetic checksums.
3. **A1 decision 6 stands: no per-star σ_S/S is used for the P4 sample.** Basis: F5 — the
   quantity exists for 17 stars, only one of which (HD 143761) is in the current sample.
4. **Saar's cycle periods are recorded alongside Baliunas', not merged into the catalogue.**
   Where they agree, the Baliunas value is promoted to grade A on cross-paper grounds
   (protocol §5); where they differ, both are recorded and neither is chosen (rule 4).
   Basis: §2.1, §2.2.
5. **The flat-group definition is escalated, not settled.** Baliunas Table 2 primary class and
   Saar Table 5 disagree on four stars (9562, 107213, 143761, 212754 — all Baliunas `Long`), and
   Baliunas' own two tables disagree on ρ CrB. Basis: F4. Consolidation decides.
6. **Any P4 Flat group must record, for each member, whether it is a Baliunas standard star.**
   Basis: F7. This is a data-hygiene requirement, not a selection decision — the flag has been
   added to `audit/saar_baliunas_crossmatch.csv`.
7. **The 44 yr solar component is added to the Methods obligations for the solar analysis.**
   Basis: F12.
8. **No sample re-selection is performed here.** Basis: protocol §1. A5 and A6 feed the
   consolidation decision; they do not pre-empt it.

---

## 7 · Unresolved (grade C or X)

| Item | Grade | Why unresolved | Disposition |
|---|---|---|---|
| HD 10476 ⟨S⟩: 0.198 vs 0.1896 | **X** | two grade-A values; no third measurement exists in the audited literature | **consolidation.** Exposure is nil while P4 uses Baliunas only (A2 decision (a)) |
| P_cyc for HD 3651, 4628, 149661 | **X** | grade A in both sources, differing beyond quoted ΔP, no stated reason | both recorded in the cross-match CSV; **action item** — Paper I (Brandenburg, Saar & Turpin 1998) would likely explain 3651 and 149661 |
| ρ CrB: `Long` (Bea95 Table 2) vs flat/Maunder (Saar Table 5, Bea95 Table 1 σ = 1.0%) | **X** | the two Baliunas tables point different ways; Saar follows Table 1 | **consolidation** |

No value that P4 currently depends on is graded C.

---

## 8 · Action items — blocked domains

Per the session's network constraints these are recorded as action items, **not** as grade C or X
values. None can be fetched from inside the sandbox.

| Item | Needed for | Where |
|---|---|---|
| Egeland+2017 Table 4 (machine-readable solar S, cycles 15–24) | the solar series itself | IOP (inherited from A3) |
| **Livina & Lenton 2007, GRL 34** | the DFA-indicator rescaling (A5 §2.1) | AGU/Wiley |
| A source for `H = (β+1)/2`; Dakos cites Schroeder 1991 (book) | A5 §2.2, or drop the claim | — |
| Peng et al. 1993, PRE 47, 3730 | DFA finite-length bias (A5 §1.5) | APS |
| **Brandenburg, Saar & Turpin 1998 (Paper I)** | explains Saar's P_cyc for HD 3651, 149661 (F3) | IOP |
| Radick et al. 1998 | Saar's revision of HD 201092 (F3) | IOP |
| Baliunas & Jastrow 1990 | the original "Maunder-minimum stars" claim both papers lean on | Nature |

---

## 9 · Open questions from protocol §11 — status after A6

| # | Question | Status |
|---|---|---|
| 2 | Do binaries stay in the sample? | **Still open — for consolidation.** Evidence strengthened: Saar corroborates HD 81809's parameters as the secondary's (F11) and rejects HD 219834A's cycle while keeping B's (F10). Saar also excludes near-equal-mass unresolved binaries on principle (§1.4). |
| 5 | Are star and Sun S-indices on the same scale? | Closed at A3 (S_SUN_MEAN = 0.1694). A6 adds nothing — Saar uses R′_HK. |
| **6** | **Do Baliunas and Saar agree on classifications?** | **Closed, asymmetrically.** Cycling stars: yes, 24 of 30 periods identical, including all four of A1's reclassifications (F2). Five classification-level changes (§2.3), three unexplained period divergences (F3). Flat stars: the question does not arise — Saar has no flat-star measurements, only predictions (F13). |

---

## 10 · Consequence for P4

The cycling side of the catalogue is now on solid ground. Two papers, working from the same
database but independently, produce the same periods for the same stars, and A1's four
corrections to `paper_state_v2` are confirmed from outside A1. That part of the sample can be
frozen with confidence.

The flat side is in worse shape than the audit had assumed, and F6, F7 and F13 compound rather
than merely accumulate. The Flat class is defined at a threshold inside the stated measurement
precision; two-thirds of its members are the calibration standard stars; and no second
measurement of any of them exists anywhere in the audited literature. P4's central comparison —
that stars near a cycle collapse show rising autocorrelation relative to stars that have already
collapsed — is being made against a group whose defining property is partly an artefact of how it
was selected and measured. This does not sink the paper. It does mean the Flat group cannot carry
a *variance* argument, and the whole weight has to fall on φ₁, with the circularity stated
outright rather than left for a referee to find. A2 reached the same conclusion from Lockwood's
noise floor; A6 confirms it from Baliunas' own calibration table, which is the harder version to
argue with.

The 44 yr solar component (F12) is the unexpected item. It is a single table cell in a paper
nobody read for that purpose, and it sits directly underneath P4's headline result.

---

## 11 · Audit log entry

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | closed | 2026-07-28 | `audit/A1_baliunas.md`, `audit/baliunas_table2_full.csv` | F1–F9 | none (2 → A3) |
| A2 Lockwood | closed | 2026-07-29 | `audit/A2_lockwood.md` | F1–F7 | none (2 → A3) |
| A3 Egeland | closed | 2026-07-29 | `audit/A3_egeland.md` | — | none (1 action item) |
| A4 Dakos | closed | 2026-07-29 | `audit/A4_dakos.md` | F1–F8 | none (2 → A5) |
| A5 Peng | closed | 2026-07-30 | `audit/A5_peng.md` | F1–F6 | 3 grade X → action items |
| A6 Saar | **closed** | 2026-07-30 | `audit/A6_saar.md`, `audit/saar_baliunas_crossmatch.csv` | F1–F13 | 3 grade X → consolidation |

**Remaining units:** A7 (Scheffer + Held & Kleinen, theory claims) and A8 (Usoskin, solar
context). Neither gates code. See `paper_state_v4.md` §7 for the sequenced plan.
