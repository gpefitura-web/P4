# Audit A4 — Dakos et al. 2012, PLoS ONE 7, e41010

**Date:** 2026-07-29
**Extraction method:** native text layer via PyMuPDF (20 pp., ~85 kB). Table 3 was additionally
re-extracted by rendering p. 14 at 300 dpi and OCR'ing it, because the text layer serialises the
table column-by-column and the PDF's minus glyph extracts as the character `2`. The rendered
pass recovers true `+` / `−` and the superscript footnote markers, and the two passes agree on
every cell — that is the two-method condition of protocol §4.
**Pages read:** all 20. Table 1 = p. 2; Table 3 = p. 14; Figure 12 flowchart = p. 14;
Steps 1–5 = pp. 11–14; DFA definition = p. 4; Figs. 10–11 (sensitivity, significance) = pp. 12–13.

> **Scope note.** This unit fixes the method *before* the real data are seen, per protocol §1.
> Every parameter below carries a section citation, and the decisions in §5 are binding on the
> pipeline.

---

## 1 · Parameter table — every row cited

### 1.1 Rolling-window metrics (AR(1), variance, skewness)

| Parameter | Value | Location |
|---|---|---|
| Rolling window, default | **half the series length (50%)** — 485 points for the CSD dataset | Step 3; Fig. 2 caption |
| Rolling window, sensitivity range tested | **25% – 75%** of series length, in increments of 10 points | Step 4 |
| Window type | **sliding / overlapping**; non-overlapping "would give similar results" | Step 3 |
| Detrending method | **Gaussian kernel smoothing**, applied to autocorrelation, variance, skewness | Step 2 |
| Gaussian bandwidth, default | **10% of the time series length** | Step 3 |
| Gaussian bandwidth, sensitivity range tested | **5 to 200**, in increments of 20 | Step 4 |
| Trend statistic | **Kendall's τ** rank correlation | Step 3 |
| Trend reported on | **both the original and the residual (detrended) series** | Step 3 |
| Interpolation | necessary **only when there are too many missing values**; the methods apply to irregular series as well as regular ones | Table 3 fn 1; Step 1 |
| Sampling-interval requirement | data must be sampled at intervals **shorter than the slowest return rate** of the system | Step 1 |

Grade **A** throughout (native text confirmed against rendered OCR).

### 1.2 DFA

| Parameter | Value | Location |
|---|---|---|
| Detrending | **simple linear detrending** — *not* Gaussian smoothing | Step 2; Step 3 (DFA) |
| Table 3 qualifier | **"only polynomial detrending within rolling window"** | Table 3 fn 5 |
| Rolling window | half the size of the original record | Step 3 (DFA); Fig. 3 caption |
| **Minimum series length** | **> 100 points for robust estimation** | Methods, DFA paragraph (citing ref. 27) |
| Fitting range | "usually estimated in time ranges between 10 and 100 time units" | Methods, DFA paragraph |
| Critical value | DFA indicator reaches **1 (rescaled from 1.5)** at a critical transition | Methods, DFA paragraph (citing ref. 7) |
| Sensitivity to filtering choice | **insensitive (−)**, precisely because only in-window polynomial detrending is used | Table 3, DFA row + fn 5 |

Grade **A**.

### 1.3 Significance — the surrogate procedure

This is the part the current pipeline lacks. Extracted in full so it can be implemented.

| Element | Specification | Location |
|---|---|---|
| Problem addressed | rolling-window metrics have **no built-in null hypothesis**; trends may arise by chance | Step 5 |
| Null model | **best-fit ARMA(p, q), selected by AIC** | Step 5 |
| Fitted to | the **residuals**, i.e. after detrending/filtering — *not* the raw series | Step 5 |
| Number of surrogates | **1,000** | Step 5; Fig. 11 caption |
| Surrogate length | **same length as the residual series** | Step 5 |
| Per-surrogate computation | re-estimate the rolling-window indicator, then its **Kendall τ** | Step 5 |
| p-value definition | **P(τ\* ≤ τ)** — the fraction of surrogate τ values ≤ the observed τ | Step 5 |
| Evaluated over | **all combinations** of bandwidth × rolling-window size, as in the sensitivity analysis | Step 5; Fig. 11 |
| Which indicators were tested this way | autocorrelation at-lag-1, standard deviation, skewness | Step 5 |
| Reported outcome (CSD dataset) | AR(1) P < 0.025 for *every* combination, P ≤ 0.001 at the chosen parameters; SD P = 0.073 at chosen parameters; skewness P = 0.8 (not significant) | Step 5 |
| Stated caveat | conclusions depend on the model chosen to generate the surrogates | Step 5 |

Grade **A**.

### 1.4 Table 3 in full, as printed

Legend: `+` sensitive to; `−` insensitive to; `n/a` not applicable.
Column groups: Preprocessing (interpolation, transformations) | Filtering/Detrending |
Sensitivity (rolling window size, filtering) | Significance.

| Method/Indicator | interpolation | transformations | Filt./Detr. | window size | filtering | Significance |
|---|---|---|---|---|---|---|
| Autocorrelation at-lag-1 | necessary¹ | depends on data | + | + | + | null model³ |
| Detrended Fluctuation Analysis | necessary¹ | no | + | + | **−⁵** | null model³ |
| Standard deviation | no | depends on data | + | + | + | null model³ |
| Skewness | no | depends on data | + | + | + | null model³ |
| Kurtosis | no | depends on data | + | + | + | null model⁴ |
| Conditional Heteroskedasticity | no | depends on data | − | + | − | built-in |
| BDS test | no | no | + | −² | + | bootstrapping |
| Time-varying AR(p) models | no | log-transform | + | − | − | built-in |
| Nonparametric DDJ models | no | log-transform | − | − | −⁴ | MC error estimates |
| Threshold AR(p) models | no | log-transform | − | − | − | built-in |
| Potential Analysis | no | no | n/a | + | − | null model³ |

**Footnotes, verbatim sense:**
1. only when there are too many missing values
2. to be applied only for rolling windows of > 500 points
3. choice of null model contingent on system
4. depends on bandwidth of Gaussian kernel smoother
5. **only polynomial detrending within rolling window**

### 1.5 Other indicators P4 references

| Indicator | Definition given | Location |
|---|---|---|
| Spectral exponent | slope of a linear fit to **log spectral density vs log frequency** | Methods, spectral paragraph (citing ref. 24) |
| Spectral ratio | density at low frequency (e.g. 0.05) ÷ density at high frequency (e.g. 0.5) | Methods (citing ref. 25) |
| AR(1) coefficient | listed as a distinct "rising memory" indicator from autocorrelation-at-lag-1 | Table 1 |

The spectral exponent is credited to "[this paper]" in Table 1 but is developed only in
Figure S3 of the Supporting Information, which is **not in the repository PDF**.

---

## 2 · Checks performed

- **Two-method extraction of Table 3** (text layer vs 300 dpi render + OCR): agree on all
  11 rows × 6 columns, including the `−⁵` on the DFA filtering cell. pass.
- **Does the paper state a minimum length for DFA?** Yes — > 100 points. pass.
- **Is the trend statistic computed on the indicator series or the residuals?** Both are reported;
  Kendall's τ is computed on the *rolling-window indicator series*, which may itself be derived
  from either the original or the detrended record. Dakos reports both side by side
  (AR(1): τ = 0.911 original, τ = 0.944 residual). pass.
- **Are the surrogates fitted to raw data or residuals?** Residuals, explicitly. pass.
- **Internal consistency of the CSD example:** grazing rate increased over 1,000 time steps,
  transition at ~step 970, window = 485 = half of 970. pass.

---

## 3 · Findings

**F1 — the pipeline's significance testing is wrong, and the correct procedure is now specified.**
Kendall τ p-values from `scipy` assume independent observations. Rolling-window indicators are
autocorrelated by construction — successive windows share most of their data — so those p-values
are anticonservative. The audit protocol suspected this; it is now confirmed and the replacement
is fully specified in §1.3. Every τ p-value currently in `paper_state_v2` (the solar subwindow
"+0.636, p < 0.0001" in particular) is not admissible and must be recomputed against 1,000
ARMA surrogates.

**F2 — P4's Gaussian bandwidth is far outside Dakos' tested range, and in the direction Dakos
warns about.** Dakos' default is a bandwidth of **10% of series length**; the sensitivity analysis
spans bandwidths 5–200 on series of ~1,000 points, i.e. roughly 0.5%–20%. P4 currently uses
σ = 1 yr on a 1966–2021 solar series (~55 yr) — about **1.8%**, at the very bottom of that range.
Dakos observed directly that "small bandwidths over-fit the data and removed most of the
variability, which the standard deviation was expected to capture", and reported *negative* SD
trends at small bandwidths. P4's variance track is therefore running at exactly the setting known
to suppress the variance signal.

There is a genuine tension here rather than a simple error, and it should be stated as such: P4
is removing a **deterministic ~11 yr cycle**, which is not the monotonic trend Dakos' detrending
step was designed for. A bandwidth of 10% of a 55 yr series (5.5 yr) would not track an 11 yr
cycle and would leave most of it in the residuals. So the narrow bandwidth is *motivated* — but
it is a departure from the cited source, not an application of it, and cannot be presented as
"following Dakos et al. (2012)" without qualification.

**F3 — the DFA detrending rule is confirmed, and is narrower than "linear detrending".**
Table 3 footnote 5 reads "only polynomial detrending within rolling window". Combined with Step 2
("simple linear detrending (DFA)") and Step 3 ("after removing a simple linear trend"), the rule
is: detrend **inside each rolling window**, polynomially. Gaussian pre-filtering is for the
AR(1)/variance/skewness track only and must not be applied ahead of DFA. P4's Track A / Track B
split is correct on this point and is now sourced to a specific footnote.

**F4 — DFA needs > 100 points; the Mount Wilson series have ~26.** This is the algorithmic floor
to set against A1's N ≈ 25–26 and A2's finding that no extension is obtainable. The three units
agree: **DFA is inadmissible for the stellar series**, by a factor of ~4 in N. It remains
comfortably admissible for the solar series. Protocol open question 1 is now closed from all
three directions (data, extension, algorithm), with A5 remaining only to verify the implementation.

**F5 — the rolling-window default (50%) is confirmed, but P4's sensitivity range is too narrow.**
`paper_state_v2` Appendix A plans w = 40%, 50%, 60%. Dakos tests **25%–75%**. Adopting the
published range costs nothing and forestalls the obvious referee question.

**F6 — reporting τ on both the original and the residual series has precedent.** Dakos reports
both (AR(1): 0.911 vs 0.944). P4's two-track presentation is therefore standard practice, not a
post-hoc rescue of a negative result — provided **both** are reported, including the negative
full-series τ. Reporting only the residual track would misrepresent the source's own practice.

**F7 — the DFA indicator is rescaled, and P4's H values are not on that scale.** Dakos states the
DFA exponent is "rescaled to give a DFA indicator … which reaches value 1 (rescaled from 1.5) at a
critical transition". `nolds.dfa` returns the raw exponent α, where 1.5 corresponds to the
transition and 0.5 to uncorrelated noise. The synthetic solar value of H = 1.235 in
`paper_state_v2` is a raw α, **not** a Dakos DFA indicator, and the two must not be compared
numerically. Either state the convention explicitly or apply the rescaling. Carried to **A5**.

**F8 — the spectral-exponent relation H = (β+1)/2 is not sourced from this paper.** Dakos defines
the spectral exponent as the log-log slope of spectral density against frequency, which is what
P4 computes — that much is sourced. The conversion to a Hurst exponent is not stated here, and
Figure S3, where the spectral treatment lives, is not in the repository. The relation must be
sourced elsewhere (**A5**, Peng+1994) or the claim dropped.

---

## 4 · Decisions taken, with basis

1. **Rolling window = 50% of series length; sensitivity reported over 25%–75%.**
   Basis: Step 3 (default), Step 4 (range).
2. **Windows are sliding/overlapping.** Basis: Step 3.
3. **Gaussian smoothing applies to the AR(1) and variance tracks only; never ahead of DFA.**
   Basis: Step 2; Table 3 fn 5.
4. **DFA uses polynomial detrending within each rolling window.** Basis: Table 3 fn 5.
5. **DFA is not applied to the Mount Wilson stellar series.** Basis: > 100-point floor
   (Methods, DFA paragraph) against N ≈ 26 (A1 F9, A2 §5).
6. **Significance for every rolling-window trend is established by 1,000 ARMA(p,q) surrogates
   fitted by AIC to the residuals, with p = P(τ\* ≤ τ), evaluated across the bandwidth × window
   grid.** Basis: Step 5. This replaces all `scipy` Kendall p-values in the pipeline.
7. **Both original-series and residual-series τ are reported.** Basis: Step 3, and F6.
8. **The Gaussian bandwidth is treated as a departure requiring its own justification and its own
   sensitivity sweep**, not as an application of Dakos' default. Basis: F2. The sweep must span
   at least 0.5%–20% of series length and the paper must state the bandwidth as a *percentage of
   series length*, which is the form Dakos uses, alongside the value in years.

---

## 5 · Unresolved (grade C or X)

**None** for any parameter P4 depends on.

Two items are out of scope and escalated rather than unresolved:

| Item | Why not resolved here | Goes to |
|---|---|---|
| DFA indicator rescaling (α vs rescaled indicator) | Dakos states the convention but not the algorithm | **A5 (Peng+1994)** |
| H = (β+1)/2 | not stated in this paper; Fig. S3 absent from repository | **A5**, or drop the claim |

---

## 6 · Open questions from protocol §11 — status after A4

| # | Question | Status |
|---|---|---|
| 1 | Is DFA admissible for the stellar series? | **Closed: no.** > 100-point floor vs N ≈ 26. Confirmed from the algorithm side. |
| 3 | How is significance established for rolling-window trends? | **Closed.** Full procedure in §1.3; decision 6. |

---

## 7 · Consequence for P4

The methodological core of the paper is now fixed from the source, and two things must change in
the pipeline.

The significance testing has to be rebuilt (decision 6). This is the single largest piece of work
the audit has generated, and it will change reported p-values — plausibly a great deal, since
surrogate testing on autocorrelated indicators is typically far more conservative than `scipy`'s.
The honest expectation is that the solar CSD signal comes out weaker than the current
"p < 0.0001". Better to discover that now than in review.

The bandwidth question (F2) is the one that needs a judgement rather than a lookup. P4's σ = 1 yr
is defensible for removing a deterministic cycle but is not what Dakos did, and the manuscript
sentence currently drafted in `paper_state_v2` — "Following Dakos et al. (2012), we removed the
deterministic 11-yr cycle prior to computing EWS metrics, using a Gaussian kernel smoother with
σ = 1 yr" — overstates the warrant. It should say that Dakos' framework is followed and that the
bandwidth is chosen for cycle removal rather than trend removal, with the sensitivity sweep
reported.

---

## 8 · Audit log entry

| Unit | Status | Date | Deliverable | Findings | Unresolved |
|---|---|---|---|---|---|
| A1 Baliunas | closed | 2026-07-28 | `audit/A1_baliunas.md`, `audit/baliunas_table2_full.csv` | F1–F9 | none (2 → A3) |
| A2 Lockwood | closed | 2026-07-29 | `audit/A2_lockwood.md` | F1–F7 | none (2 → A3) |
| A4 Dakos | **closed** | 2026-07-29 | `audit/A4_dakos.md` | F1–F8 | none (2 → A5) |

**Next in sequence:** A3 (Egeland+2017) — now carrying three inherited scale questions — then
A5 (Peng+1994), which inherits the DFA rescaling and the H–β relation.
