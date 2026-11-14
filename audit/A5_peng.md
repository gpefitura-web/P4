# Audit A5 — Peng et al. 1994, Phys. Rev. E 49, 1685

**Date:** 2026-07-30
**Extraction method:** two independent passes, both required. Pass 1 = the PDF's embedded text
layer via PyMuPDF. Pass 2 = PyMuPDF render at 500–700 dpi, column-cropped, Tesseract 5 under
`--psm 3`/`--psm 6`, plus whole-page passes at 400 and 600 dpi.
**Pages read:** all 5 (journal pp. 1685–1689). DFA algorithm = p. 1685 col. 2; results and
crossover discussion = pp. 1686–1687; Fig. 3 caption = p. 1687; Fig. 5 caption = p. 1688;
notes [14], [15], [16] = pp. 1688–1689.
**Depends on:** A4 (closed), which escalated findings F7 and F8 to this unit.

> **Correction to protocol §2, and it changes how this unit had to be run.** The scope table
> lists Peng+1994 as **native**. It is not. Page 1 carries exactly one embedded image and the
> "text layer" is a pre-existing OCR of a scan. Its quality is poor: author names are corrupted
> (`Havtin` for Havlin), affiliations are corrupted (`Ogg15`, `OMITS` for 02215), the method's
> own acronym appears as `DEA`, and the box-size symbol ℓ is rendered variously as `E`, `8`,
> `f`, `t'`, `@` and `I`. Every value below therefore required the two-pass treatment that the
> protocol reserves for Baliunas. No value in this unit rests on the text layer alone.

---

## 1 · Values extracted

### 1.1 The algorithm, in the paper's own terms

Peng gives the method as two numbered steps (p. 1685, col. 2), preceded by the construction of
the object it operates on.

| # | Element | As stated | Location | Grade |
|---|---|---|---|---|
| 0 | The profile | the "DNA walk": `y(n) = Σᵢ₌₁ⁿ u(i)`, the running sum of the ±1 step sequence. Integration is built into the object analysed, not a separate step of the method | p. 1685 col. 1 | A |
| 1 | Partition | "Divide the entire sequence of length N into N/ℓ **nonoverlapping** boxes, each containing ℓ nucleotides" | p. 1685 col. 2, step (1) | A |
| 1 | Local trend | "the ordinate of a **linear least-squares fit** for the DNA walk displacement in that box" | p. 1685 col. 2, step (1) | A |
| 2 | Detrended walk | `y_d(n)` = original walk minus the local trend | p. 1685 col. 2, step (2) | A |
| 2 | Fluctuation | "Calculate the variance about the detrended walk for each box, and calculate the average of these variances over all the boxes of size ℓ, denoted **F_d²(ℓ)**" | p. 1685 col. 2, step (2) | A |
| 2 | Precise definition | `F_d(ℓ) ≡ √⟨y_d²(n)⟩` — i.e. **F_d is a root-mean-square, a standard deviation, not a variance** | note [15], p. 1689 | A |
| — | Exponent | α = slope of `log₁₀ F_d(ℓ)` versus `log₁₀ ℓ` | note [16], p. 1689 | A |

**Detrending polynomial order: 1 (linear).** Peng 1994 uses a linear least-squares fit and
nothing else. Higher-order detrending does not appear in the paper in any form. Grade **A**
(both passes; the phrase "linear least-squares fit" is unambiguous in the 600 dpi render).

**Box overlap.** Non-overlapping is the definition. Overlap is offered as an *optional
generalisation* in note [14]: "instead of incrementing the box position by a distance ℓ between
each measurement, to increment the position by a distance **ℓ/S**, where S is a sliding
parameter that can be chosen to give optimal statistics." Grade **A**.

### 1.2 Box sizes — the floor is stated, the ceiling is not

| Quantity | Value | Location | Grade |
|---|---|---|---|
| Minimum box size | evaluate the slope **for ℓ > 4**, "since for very small ℓ we expect deviation (introduced by the detrending algorithm) from power-law behavior"; numerical tests show the deviation is negligible **from ℓ ≳ 4** | note [16] | A |
| Maximum box size | **no rule is stated anywhere in the paper** | — | A (negative, both passes) |

Peng's *practice* is the only guide to the ceiling, and it is conservative:

| Sequence | N | Fit range | ℓ_max as fraction of N | Boxes at ℓ_max | Decades fitted |
|---|---|---|---|---|---|
| *E. coli* K12 (Fig. 3) | 111,401 | ℓ = 4 → 861 | N/129 | 129 | 2.33 |
| Human T-cell receptor (Fig. 3) | 97,634 | ℓ = 4 → 8192 | N/12 | 11 | 3.31 |
| λ phage genome (Fig. 5) | 48,502 | ℓ = 4 → 1024 | N/47 | 47 | 2.41 |

Grade **A** (figure captions read in both passes; `861`, `8192` and `1024` each confirmed).

### 1.3 What α means — strictly what Peng says

| α | Meaning **as stated in Peng+1994** | Location | Grade |
|---|---|---|---|
| **0.5** | uncorrelated (or short-range correlated) sequence. "the detrended DNA walk must have the statistical properties of a random walk … so F_d(ℓ) ~ ℓ^(1/2)"; and "For the ideal case of a random sequence, α = 0.5" | p. 1685 col. 2; note [16] | A |
| **< 0.5** | long-range correlations "that reflect an **alternation** of different nucleotide types" (anticorrelation) | note [16] | A |
| **> 0.5** | long-range correlations that "reflect a **persistence** of the same nucleotide type" | note [16] | A |
| measured | 0.51 for the uncorrelated control and for *E. coli*; 0.61 for the correlated control and for the human intron-containing locus | p. 1686, Fig. 3 | A |
| **1.0** | appears **once, and negatively**: the *nondetrended* analysis of Karlin & Brendel crosses over "to a value close to **unity** for large ℓ", which Peng attributes to patchiness and presents as precisely the artefact DFA is designed to remove | p. 1687 | A |
| **1.5** | **the string does not occur in the paper** | — | A (negative) |

### 1.4 Negative checks — verified in both passes

The following strings occur **zero** times in Peng et al. 1994, in the text layer and in the
independent OCR of all five pages:

`1.5` · `Hurst` · `spectr` (hence no spectral exponent, no power spectrum) · `1/f` ·
`Brownian` · `minimum length` · `at least`

`rescal` occurs four times, all in the Fig. 4 histogram-collapse discussion (rescaling the
abscissa by ℓ^α so that distributions at different box sizes superpose). It has no connection to
the Dakos "DFA indicator" rescaling.

### 1.5 Series length and finite-size bias

| Question | Answer | Location | Grade |
|---|---|---|---|
| Minimum series length stated? | **No.** The only length constraint in the paper is the box-size floor ℓ ≳ 4 | — | A (negative) |
| Warning about short series? | Yes, but delegated: "since the length of the sequences is not infinite, we must take into account the statistical fluctuations for a finite size sample. A discussion of the effects of the finite length … appears in [Peng et al., Phys. Rev. E **47**, 3730 (1993)]" | note [16] | A |

Peng+1993 is **not in the repository** and APS is outside the permitted domains. Recorded as an
**action item**, not as a grade C or X value.

### 1.6 Crossovers are a first-class output, not a nuisance

This is the part of Peng that the P4 pipeline does not implement, so it is quoted at length.

- The uncorrelated patch-model control has a crossover at **ℓ_× ≈ 2500**, "a value that
  coincides with the characteristic length scale *built into*" that control (p. 1686).
- *E. coli* "also exhibit[s] a crossover at roughly the same value of ℓ_×, suggesting the
  existence of a characteristic patch size" (p. 1686).
- The correlated control and the intron-containing human sequence show **no** crossover,
  "corresponding to the existence of correlations at all scales" (p. 1687).
- Summary statement: "The DFA method, therefore, allows us to unambiguously differentiate two
  properties that were previously difficult to distinguish: **(i) the value of α**, which
  measures the degree of long-range correlation, and **(ii) the approximate value of ℓ_×, the
  crossover value**, indicating the characteristic length scale of patches" (p. 1687).

Grade **A**. Note that the *E. coli* fit (ℓ = 4 → 861) stops well below its own crossover at
≈ 2500: Peng fits **within one scaling regime**, never across a crossover.

---

## 2 · The two questions inherited from A4

### 2.1 F7 — the DFA rescaling. **Peng is not its source.**

A4 recorded Dakos' sentence: the DFA exponent "is then rescaled to give a DFA indicator, which
is usually estimated in time ranges between 10 and 100 time units, and which reaches value 1
(rescaled from 1.5) at a critical transition **[7]**".

Resolving the citation numbers in Dakos' reference list settles this:

| Dakos ref | Work | What it is cited for |
|---|---|---|
| **[26]** | **Peng C-K, Buldyrev S, Havlin S, Simons M, Stanley H, et al. (1994) Mosaic organization of DNA nucleotides. Phys Rev E 49: 1685–1689** | the definition of the fluctuation exponent α |
| **[7]** | **Livina VN, Lenton TM (2007) A modified method for detecting incipient bifurcations in a dynamical system. Geophys Res Lett 34** | **the rescaling, and the value 1 (from 1.5) at transition** |
| **[27]** | Lenton TM, Livina VN, Dakos V, van Nes EH, Scheffer M (2012) Early warning of climate tipping points from critical slowing down. Philos Trans A 370: 1185–1204 | the "> 100 points for robust estimation" floor |

So:

1. **Peng+1994 is the correct and sufficient citation for α itself**, for the algorithm, and for
   the statement that 0.5 denotes an uncorrelated series. P4 may cite it for exactly those things.
2. **Peng+1994 is not a valid citation for the rescaling, for α = 1.5 at a transition, or for
   the > 100-point floor.** None of the three appears in it. The rescaling belongs to Livina &
   Lenton 2007; the floor belongs to Lenton et al. 2012 — i.e. neither is Dakos' own result either.
3. The arithmetic that would map 0.5 → 0 and 1.5 → 1 is `indicator = α − 0.5`. **This is an
   inference from two anchor points, not a value read from a source, and it is recorded as
   grade X.** Livina & Lenton 2007 is not in the repository and GRL is outside the permitted
   domains. → **action item.**

**Consequence.** A4 F7 stands and is now fully explained. The `H = 1.235` in `paper_state_v2` is
a raw Peng α. It is not a Dakos DFA indicator and the two must not be compared numerically. Until
Livina & Lenton 2007 is in hand, P4 should report **raw α on Peng's convention and say so
explicitly**, rather than apply a rescaling it cannot cite.

### 2.2 F8 — H = (β+1)/2. **Not in Peng, and could not be.**

Peng et al. 1994 contains **no spectral analysis of any kind** — no power spectrum, no spectral
exponent, no Fourier decomposition of the fluctuation function, and the string `spectr` does not
occur (§1.4). The relation cannot be sourced here.

Tracing Dakos' spectral citations for completeness: the spectral exponent is credited to
ref **[24] Schroeder M (1991), *Fractals, Chaos, Power Laws*, Freeman** — a book, not in the
repository — and the spectral *ratio* to ref [25] Biggs, Carpenter & Brock 2009.

**Recorded as grade X.** The relation must be sourced elsewhere or the claim dropped
(→ action item). Two cautions for whoever sources it:

- The relation `H = (β+1)/2` holds for **fractional Gaussian noise**, where β = 2H − 1. For
  fractional Brownian motion the relation is β = 2H + 1. Which one applies depends on whether the
  analysed series is the noise or its integral.
- `paper_state_v2` reports `H_full = 1.235`. Under Peng's convention (integrate, then detrend) an
  α above 1 is the fBm-like regime, where `H = (β+1)/2` is **not** the applicable relation. The
  comparison the report does make — `H_from_psd = 0.863` against `H_resid = 0.864` — is at least
  in the regime where the relation could hold. The full-series comparison is not.

---

## 3 · The implementation check

> **First correction, and it redirects the whole check.** A4 F7 and the opening brief for this
> session both frame the question around `nolds.dfa`. **The pipeline does not use `nolds`.**
> `p4_pipeline.ipynb` cell 0 states "This notebook implements DFA natively (Peng et al. 1994) and
> therefore does **not** require `nolds`"; cell 4 imports it inside a `try/except` purely as an
> optional cross-check and prints a message when it is absent; cell 14 defines the DFA that is
> actually used. The object to audit is the native `dfa()`, and that is what is audited below.
> Note also that `paper_state_v2`'s reference list still cites "Schölzel 2019 — nolds" under
> Software; that entry is stale and should be removed.

### 3.1 Line by line

| Peng+1994 | `dfa()` in cell 14 | Verdict |
|---|---|---|
| profile = running sum of the series | `Y = np.cumsum(x - np.mean(x))` | **faithful** |
| N/ℓ non-overlapping boxes of length ℓ | `Y[b*n:(b+1)*n]` for `b in range(N//n)` | **faithful** |
| local trend = linear least-squares fit inside the box | `np.polyfit(idx, seg, order)` with `order=1` | **faithful** |
| F_d(ℓ) = √⟨y_d²⟩ | `sqrt(mean over boxes of (mean over points of resid²))` | **faithful** — boxes are equal length, so this equals the grand RMS exactly |
| α = slope of log F vs log ℓ | `np.polyfit(np.log10(used), np.log10(F), 1)` | **faithful** |
| ℓ ≳ 4 | `n_min = 4`, and the docstring cites Peng p. 1688 for it | **faithful, and correctly cited** |
| trailing points beyond the last whole box | discarded (`N//n` boxes) | **faithful** — Peng does the same |
| ℓ_max: no rule; practice N/12 … N/129 | `n_max = max(8, N//4)` | **divergence — F1** |
| crossover identified separately from α; fits confined to one regime | one OLS slope across all 20 scales | **divergence — F2** |

Six of eight elements are faithful, and the two that are not are both about the *upper* end of
the scale range. The core of the implementation is correct.

### 3.2 The numbers behind the two divergences

For the solar series as described in `paper_state_v2` (N ≈ 20,000 daily points, 1966–2021), the
implementation's own rule produces:

- `n_min = 4`, `n_max = N//4 = 5000` days = **13.7 yr**; 20 log-spaced scales:
  `4, 5, 8, 12, 17, 26, 38, 55, 80, 117, 170, 248, 361, 526, 765, 1114, 1621, 2360, 3435, 4999`
- At `n_max` exactly **4 boxes** contribute, so F at the largest scale is the RMS of four numbers.
- The 11-yr cycle is 4018 days. **Three of the twenty fitted scales sit at or above half the
  cycle length**, and the top scale exceeds a full cycle.
- The ~27-day rotation period lands almost exactly on the scale `n = 26`.

---

## 4 · Findings

**F1 — `n_max = N/4` is between 3× and 32× more aggressive than any fitting range Peng used.**
Peng's most aggressive published fit reached N/11.9, and even there 11 boxes contributed at the
largest scale. `N/4` leaves four. Peng states no ceiling, so this is not a violation of a written
rule — but it is far outside the practice of the paper being cited, it is the regime where F(ℓ)
is noisiest, and an OLS slope weights those points equally with the well-determined small scales.
A ceiling of `N/10` with a stated minimum box count, and a reported sensitivity to it, would cost
nothing.

**F2 — the pipeline fits a single slope across 3.1 decades with no crossover check, and the
solar series is guaranteed to have a crossover.** Peng treats ℓ_× as a *second output of the
method*, of equal standing to α, and never fits across one. Track A applies DFA to the raw solar
series with only a linear detrend — the deterministic 11-yr cycle is fully present — and the
fitting range straddles it. A strong periodic component produces a pronounced knee in F(ℓ) near
its period. Reporting one α over that range is not a parameter choice; it is the specific error
the DFA paper was written to expose.

**F3 — the justification recorded for Track A in `paper_state_v2` is factually wrong.**
The document states that DFA is *"insensível ao ciclo de ~11 anos porque nvals cobre escalas
menores que ~5 anos"*. The implementation's largest scale is `N//4 = 5000` days = **13.7 yr** —
**2.7× the claimed bound**, and longer than the cycle it is said to avoid. This sentence cannot be
repaired by rewording, because the code does the opposite of what it claims. It must be struck,
and either the code changed to match the claim (`n_max ≈ 1800` days would put every scale below
5 yr) or the claim dropped.

**F4 — `H = 1.235` is not defensible as currently reported, for three independent reasons.**
(i) it is a raw Peng α, not a Dakos DFA indicator (A4 F7, now confirmed at the source);
(ii) it is fitted across a crossover the method's own paper requires to be identified separately
(F2); (iii) it is fitted out to 13.7 yr with four boxes at the top scale (F1). Each is
individually sufficient to draw a referee's fire. The number should not appear in the manuscript
until all three are addressed.

**F5 — the stellar DFA floor is confirmed from the algorithm side, but Peng is not its source.**
Peng states no minimum series length. What Peng does impose is ℓ ≳ 4 plus the implicit
requirement of a scaling range wide enough to fit a slope over (his own fits span 2.3–3.3
decades). With N = 26 and the pipeline's own ceiling, the admissible range is 4 ≤ n ≤ 6: under
half a decade, two or three distinct scales. DFA is inadmissible for the Mount Wilson series, and
this now follows from the algorithm as well as from the data. The pipeline's `dfa_hurst` gate
(NaN below N = 100) is correct in effect, but its stated basis — "exactly the threshold
Dakos+2012 state" — should cite **Lenton et al. 2012** (Dakos ref [27]), which is where that
number actually comes from. Protocol open question 1 is now closed from all four directions.

**F6 — protocol §2 misclassifies the Peng PDF as native.** See the note at the head of this
unit. The scope table should be corrected, and the correction matters: had this unit trusted the
text layer, it would have reported the fit ranges and the ℓ ≳ 4 floor from a source that renders
ℓ as `E`, `8` and `f` interchangeably.

---

## 5 · Decisions taken, with basis

1. **Peng+1994 is cited for the DFA algorithm and for α, and for nothing else.** Specifically it
   is *not* cited for the rescaled DFA indicator, for α = 1.5 at a transition, for
   H = (β+1)/2, or for any minimum series length. Basis: §1.4 negative checks and §2.
2. **DFA parameters are fixed as: profile = cumulative sum of the mean-centred series;
   non-overlapping boxes; detrending polynomial order 1; n_min = 4.** Basis: steps (1)–(2),
   note [16]. The current implementation already conforms and does not change.
3. **`n_max` is reduced from N/4, and the fitting range, the number of scales and the box count
   at the largest scale are reported alongside every α.** Basis: Peng's published practice,
   N/12 – N/129 (§1.2), and F1.
4. **A crossover check is mandatory before any α is reported, and α is fitted within a single
   scaling regime.** Basis: p. 1687, "(i) the value of α … and (ii) the approximate value of
   ℓ_×"; and the *E. coli* fit stopping below its own crossover.
5. **The Track A justification sentence in `paper_state_v2` is struck.** Basis: F3.
6. **α is reported on Peng's raw convention, with the convention stated explicitly in Methods,
   until Livina & Lenton 2007 is obtained.** Basis: §2.1. This is the honest option: it cites
   what can be cited and defers what cannot.
7. **DFA remains reserved for the solar series.** Basis: F5, confirming A4 decision 5.
8. **The `nolds` entry is removed from the reference list.** Basis: the pipeline does not use it.

---

## 6 · Unresolved (grade C or X)

| Quantity | Grade | Why unresolved | Proposed resolution |
|---|---|---|---|
| DFA-indicator rescaling (α → indicator) | **X** | stated by Dakos, attributed to Livina & Lenton 2007, GRL 34; that paper is not in the repository and AGU/Wiley is outside the permitted domains | **action item** — obtain the PDF. Until then, report raw α (decision 6) |
| `H = (β+1)/2` | **X** | absent from Peng; Dakos attributes the spectral exponent to Schroeder 1991 (a book), also absent | **action item** — source it, or drop the claim. Note the fGn/fBm caveat in §2.2 |
| Finite-length bias in DFA | **X** | Peng note [16] delegates it to Peng et al. 1993, PRE 47, 3730; not in the repository, APS blocked | **action item**. Not blocking: DFA is not applied to the short series anyway |

No parameter that P4 currently depends on is graded C.

---

## 7 · Open questions from protocol §11 — status after A5

| # | Question | Status |
|---|---|---|
| 1 | Is DFA admissible for the stellar series? | **Closed: no**, now from the algorithm side as well. N = 26 admits 4 ≤ n ≤ 6 — two or three scales, under half a decade. |

---

## 8 · Consequence for P4

Nothing about the DFA *implementation* is broken in a way that invalidates work already done: six
of the eight algorithmic elements are faithful to the source, and the two divergences are both at
the long-scale end. What has to change is the treatment of the largest scales and the reporting
of α.

The substantive casualty is `H = 1.235`. It cannot survive in its current form, and the sentence
in `paper_state_v2` that justifies producing it is demonstrably false against the code (F3). The
per-decade H values are on much safer ground — each decade is ~4000 daily points, so `n_max` is
about 1000 days ≈ 2.7 yr, comfortably below the cycle, with 4 boxes only at the very top. Those
five numbers, recomputed with a crossover check and a stated ceiling, are the defensible part of
Track A.

The citation situation is cleaner than A4 feared in one respect and worse in another. Peng is a
perfectly good citation for what P4 actually computes — a raw α on the original convention. But
two claims currently attached to that citation belong to papers nobody in this audit has read,
one of which (Livina & Lenton 2007) is the actual origin of the "DFA indicator" framing that
`paper_state_v2` leans on. Getting that PDF should be near the top of the action list.

---

## 9 · Audit log entry

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | closed | 2026-07-28 | `audit/A1_baliunas.md`, `audit/baliunas_table2_full.csv` | F1–F9 | none (2 → A3) |
| A2 Lockwood | closed | 2026-07-29 | `audit/A2_lockwood.md` | F1–F7 | none (2 → A3) |
| A3 Egeland | closed | 2026-07-29 | `audit/A3_egeland.md` | — | none (1 action item) |
| A4 Dakos | closed | 2026-07-29 | `audit/A4_dakos.md` | F1–F8 | none (2 → A5) |
| A5 Peng | **closed** | 2026-07-30 | `audit/A5_peng.md` | F1–F6 | 3 grade X, all → action items |
