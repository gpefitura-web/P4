# Alternative text for the figures

For the submission form (Elsevier asks for a short alternative text per figure). The wording is descriptive only: it states what is drawn, not what the numbers are; the values are in the captions and tables of `main.tex`, which are generated from `pipeline_v2/results/`.

## Figure 1 (`Figure_1`)
**Short:** Dot plot of the S-index standard deviation of HD 166620 in three states, with three estimates per state, and the value for the grand minimum lowest.
**Long:** Horizontal axis: the three states of HD 166620 (minimum 1, minimum 2 and the grand minimum), each labeled with its years and number of observations. Vertical axis: standard deviation of the S index. For each state three markers are drawn: squares for the raw interval, circles for the value with the instrumental noise removed (method A) and triangles for the seasonal-mean version (method B). Vertical bars give 95 % bootstrap intervals over observing seasons for the raw and method-A values (none for method B). In every point estimate the grand minimum has the lowest standard deviation.

## Figure 2 (`Figure_2`)
**Short:** Annual S index of HD 166620 with its one-year Gaussian smooth, and below it the rolling lag-1 autocorrelation of the original series and of the residual.
**Long:** Top panel: annual mean S of HD 166620 against year (Mount Wilson era, no interpolated years) as a solid line, with the Gaussian smooth of width one year as a dashed line; the series shows slow, cycle-like swings. Bottom panel: rolling lag-1 autocorrelation, plotted at the end year of each window, as a solid line for the original series and a dashed line for the residual (series minus smooth).

## Figure 3 (`Figure_3`)
**Short:** Same layout as Figure 2 for the Sun: annual S index with its smooth, and the rolling lag-1 autocorrelation of the original series and of the residual.
**Long:** Top panel: annual mean S of the solar composite series (Egeland et al.) against year as a solid line with the one-year Gaussian smooth as a dashed line; open circles mark the interpolated years; the solar cycles are visible as regular oscillations. Bottom panel: rolling lag-1 autocorrelation, as in Figure 2, with the window bar. The vertical range of the top panel differs from that of Figure 2.

## Figure 4 (`Figure_4`)
**Short:** Kendall tau of the rolling lag-1 autocorrelation for each star, grouped as Flat, Cycle, Var and Long, with the Sun last; values of both signs in every group, a few marked with an asterisk.
**Long:** Horizontal axis: stars labeled by HD number, in four groups (Flat, Cycle, Var, Long) and the Sun last, sorted by HD number within a group. Vertical axis: Kendall tau of the rolling lag-1 autocorrelation. Two markers per star: circles for the original series, diamonds for the one-year residual. A gray vertical bar behind each marker spans the 5th to 95th percentile of the surrogate values and is wide for every star. An asterisk above a marker means a one-sided surrogate p below 0.05 for that configuration. In every group some values are positive and some negative.
