# Alternative text for the figures

For the submission form (Elsevier asks for a short alternative text per figure). The wording is descriptive only: it states what is drawn, not what the numbers are; the values are in the captions and tables of `main.tex`, which are generated from `pipeline_v2/results/` and `pipeline_v2/results_calibration/`.

## Figure 1 (`cal_fig4_qq`)
**Short:** Two quantile-quantile panels of the surrogate p values of the stellar run against the uniform law, upper tail and lower tail, with points below the diagonal in the upper tail.
**Long:** Two square panels. Horizontal axis: uniform quantile from 0 to 1; vertical axis: observed p value from 0 to 1, for the 192 cells of the stellar run. A light diagonal marks perfect agreement. Left panel, upper tail (the direction of critical slowing down): the blue points lie below the diagonal over most of the range. Right panel, lower tail: the points follow the diagonal more closely, with a few small values.

## Figure 2 (`cal_fig1_controls`)
**Short:** Three rows of example series from the three positive-control models, each with its rolling autocorrelation and variance, for a series that keeps its cycle and one that loses it.
**Long:** A grid of three rows (supercritical, subcritical and multiplicative-noise oscillator) and three columns. Left: annual mean of the simulated series against year of the record, gray for the series that keeps its cycle and blue for the one that loses it; both oscillate with a period of about eleven years, and the blue one's amplitude shrinks toward the end, abruptly in the subcritical row. Centre: rolling lag-1 autocorrelation of each series, from the middle of the record to its end. Right: rolling variance; the gray line stays roughly level while the blue line falls. A shared legend is below the grid.

## Figure 3 (`cal_fig2_power_grid`)
**Short:** Four panels of AUC and lower-tail rejection against the dynamical noise for three cycle periods, for autocorrelation and variance.
**Long:** Two columns (lag-1 autocorrelation, variance) and two rows. Horizontal axis: dynamical noise at three values. Top row: AUC for separating series that lose the cycle from those that keep it, one line per period (8, 11 and 15 years, marked by circles, squares and triangles); a light line marks 0.5. Bottom row: rejection rate of the lower-tail test in percent, with a light line at 5 percent. The variance panels show higher values that decrease as the noise grows; the autocorrelation panels are lower and flatter.

## Figure 4 (`cal_fig3_design`)
**Short:** Two panels of the power of the test for a true rise of the autocorrelation against record length, with and without a cycle, for three noise levels.
**Long:** Two panels sharing the vertical axis (power in percent) with a logarithmic horizontal axis of record length from 30 to 200 years. Left: no cycle; right: with a cycle of eleven years. Six lines per panel: three noise levels in blue, orange and aqua, with solid lines for the autocorrelation and dashed lines for the variance. A light horizontal line marks 5 percent. In the left panel the lines rise with length; in the right panel they stay close to the 5 percent line.

## Figure 5 (`cal_fig6_step`)
**Short:** Dot plot of the median Kendall tau of the rolling autocorrelation and variance for seven kinds of instrumental step in null series.
**Long:** Horizontal axis: median Kendall tau of the rolling indicator; vertical axis: seven cases, from no step through steps in level of half, one and two standard deviations, to changes of the noise (halved or raised by half) and a combined case. Blue circles for the autocorrelation and orange squares for the variance. A vertical line marks zero. Level steps move both markers to negative values; halving the noise moves the variance marker far to the left and raising it moves it to the right.

## Figure 6 (`Figure_1`)
**Short:** Dot plot of the S-index standard deviation of HD 166620 in three states, with three estimates per state, and the value for the grand minimum lowest.
**Long:** Horizontal axis: the three states of HD 166620 (minimum 1, minimum 2 and the grand minimum), each labeled with its years and number of observations. Vertical axis: standard deviation of the S index. For each state three markers are drawn: squares for the raw interval, circles for the value with the instrumental noise removed (method A) and triangles for the seasonal-mean version (method B). Vertical bars give 95 % bootstrap intervals over observing seasons for the raw and method-A values (none for method B). In every point estimate the grand minimum has the lowest standard deviation.

## Figure 7 (`cal_fig5_sigma_f`)
**Short:** Two curves of the ratio of the noise-corrected variability of two cycle minima to that of the grand minimum against the assumed instrumental noise fraction.
**Long:** Horizontal axis: assumed instrumental noise fraction of the Mount Wilson states in percent of the mean S, from 0.8 to about 1.9. Vertical axis: ratio of the corrected standard deviation to that of the grand minimum. Blue line: minimum 2, high and nearly flat. Orange line: minimum 1, falling and crossing the horizontal line at one near the right of the range, then dropping steeply. Light vertical lines mark the value used in the main analysis and a larger one.

## Figure 8 (`cal_fig7_dalton`)
**Short:** Top: annual sunspot group number from 1740 to 1900 with a shaded block; bottom: Kendall tau of the rolling indicators in six blocks of 36 years.
**Long:** Top panel: annual mean group number against year as a blue line for years with enough days of data and gray dots for the years excluded; a gray band marks the block 1795 to 1830, where the cycle maxima are lower. Bottom panel: for each of six consecutive blocks of 36 years, blue circles (autocorrelation) and orange squares (variance) show Kendall tau in the four detrending configurations; a horizontal line marks zero. Values of both signs appear across blocks.

## Figure 9 (`Figure_2`)
**Short:** Annual S index of HD 166620 with its one-year Gaussian smooth, and below it the rolling lag-1 autocorrelation of the original series and of the residual.
**Long:** Top panel: annual mean S of HD 166620 against year (Mount Wilson era, no interpolated years) as a solid line, with the Gaussian smooth of width one year as a dashed line; the series shows slow, cycle-like swings. Bottom panel: rolling lag-1 autocorrelation, plotted at the end year of each window, as a solid line for the original series and a dashed line for the residual (series minus smooth).

## Figure 10 (`Figure_3`)
**Short:** Same layout as Figure 9 for the Sun: annual S index with its smooth, and the rolling lag-1 autocorrelation of the original series and of the residual.
**Long:** Top panel: annual mean S of the solar composite series (Egeland et al.) against year as a solid line with the one-year Gaussian smooth as a dashed line; open circles mark the interpolated years; the solar cycles are visible as regular oscillations. Bottom panel: rolling lag-1 autocorrelation, as in Figure 9, with the window bar. The vertical range of the top panel differs from that of Figure 9.

## Figure 11 (`Figure_4`)
**Short:** Kendall tau of the rolling lag-1 autocorrelation for each star, grouped as Flat, Cycle, Var and Long, with the Sun last; values of both signs in every group, a few marked with an asterisk.
**Long:** Horizontal axis: stars labeled by HD number, in four groups (Flat, Cycle, Var, Long) and the Sun last, sorted by HD number within a group. Vertical axis: Kendall tau of the rolling lag-1 autocorrelation. Two markers per star: circles for the original series, diamonds for the one-year residual. A gray vertical bar behind each marker spans the 5th to 95th percentile of the surrogate values and is wide for every star. An asterisk above a marker means a one-sided surrogate p below 0.05 for that configuration. In every group some values are positive and some negative.
