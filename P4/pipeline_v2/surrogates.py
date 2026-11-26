"""Step 5 - ARMA(p,q) surrogates (D22) with the same gap mask and interpolation as the data (D98).

Procedure per (segment, detrending config): residual r -> ARMA(p,q) chosen by AIC over p,q in {0,1,2}
(fixed a priori) -> N surrogates of the same length from the fitted model (Gaussian innovations)
-> gap positions of the segment are blanked and linearly interpolated from the neighbouring
observed points (the D98 rule) -> rolling indicator and Kendall tau computed exactly as for the data.
p-values: p_D22 = P(tau* <= tau) (literal D22) and p_upper = P(tau* >= tau) (increasing trend, CSD direction),
both with the +1 correction."""
import warnings
import numpy as np
from scipy.signal import lfilter

ORDERS = [(p, q) for p in (0, 1, 2) for q in (0, 1, 2)]


def fit_arma(r):
    """Best ARMA(p,q) by AIC, fitted on the standardized series (mean 0, SD 1) and mapped back to the units of r (D121):
    fitting on the raw scale made the AIC choice depend on the scale of the series (see scale_sensitivity.py).
    Returns dict(const, phi[], theta[], sigma2, order, engine); const and sigma2 are in the units of r."""
    r = np.asarray(r, float)
    m, sd = float(r.mean()), float(r.std())
    if not sd > 0:
        return _fit_arma_scaled(r)
    mod = _fit_arma_scaled((r - m) / sd)
    mod["const"] = mod["const"] * sd + m
    mod["sigma2"] = mod["sigma2"] * sd ** 2
    return mod


def _fit_arma_scaled(r):
    """Best ARMA(p,q) by AIC on the series as given. statsmodels if available, else AR(p) by Yule-Walker (MA ignored)."""
    r = np.asarray(r, float)
    try:
        from statsmodels.tsa.arima.model import ARIMA
        best = None
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            for p, q in ORDERS:
                try:
                    res = ARIMA(r, order=(p, 0, q), trend="c").fit()
                except Exception:
                    continue
                if not np.isfinite(res.aic):
                    continue
                if best is None or res.aic < best[0]:
                    pr = res.params
                    best = (res.aic, dict(const=float(pr[0]), phi=list(pr[1:1 + p]), theta=list(pr[1 + p:1 + p + q]),
                                          sigma2=float(pr[-1]), order=(p, q), engine="statsmodels"))
        if best is not None:
            return best[1]
    except ImportError:
        pass
    return _fit_yw(r)


def _fit_yw(r):
    n, m = len(r), r.mean()
    x = r - m
    acf = np.array([np.sum(x[:n - k] * x[k:]) / n for k in range(4)])
    best = None
    for p in (0, 1, 2, 3):
        if p == 0:
            phi, s2 = np.array([]), acf[0]
        else:
            R = np.array([[acf[abs(i - j)] for j in range(p)] for i in range(p)])
            phi = np.linalg.solve(R, acf[1:p + 1]); s2 = acf[0] - phi @ acf[1:p + 1]
        aic = n * np.log(max(s2, 1e-300)) + 2 * (p + 1)
        if best is None or aic < best[0]:
            best = (aic, dict(const=float(m), phi=list(phi), theta=[], sigma2=float(s2), order=(p, 0), engine="yule-walker"))
    return best[1]


def simulate(model, n, nsim, rng, burn=100):
    """nsim ARMA realisations of length n -> array (nsim, n)."""
    e = rng.normal(0.0, np.sqrt(model["sigma2"]), size=(nsim, n + burn))
    y = lfilter(np.r_[1.0, model["theta"]], np.r_[1.0, -np.asarray(model["phi"])], e, axis=1)
    return y[:, burn:] + model["const"]


def apply_mask(X, filled):
    """Blank filled positions and linearly interpolate from observed neighbours (D98), row-wise."""
    X = np.array(X, float)
    if not filled.any():
        return X
    idx = np.arange(X.shape[1]); obs = idx[~filled]
    for i in range(X.shape[0]):
        X[i, filled] = np.interp(idx[filled], obs, X[i, obs])
    return X


def rolling_stat(X, w, stat):
    """Rolling-window statistic, vectorised over rows. X (nrow, L) -> (nrow, L-w+1)."""
    from numpy.lib.stride_tricks import sliding_window_view
    W = sliding_window_view(X, w, axis=1)                      # (nrow, nwin, w)
    m = W.mean(axis=2, keepdims=True); d = W - m
    if stat == "ac1":
        den = np.sum(d ** 2, axis=2)
        return np.sum(d[..., :-1] * d[..., 1:], axis=2) / den
    if stat == "var":
        return np.sum(d ** 2, axis=2) / (w - 1)
    raise ValueError(stat)


def tau_rows(R):
    """Kendall tau (no-tie form) of each row of R against its index. R (nrow, n)."""
    n = R.shape[1]
    s = np.sign(R[:, None, :] - R[:, :, None])                # s[a,i,j] = sign(R_j - R_i)
    iu = np.triu_indices(n, 1)
    return s[:, iu[0], iu[1]].sum(axis=1) / (n * (n - 1) / 2)


def surrogate_test(r, filled, frac, stat, nsurr, rng, model=None):
    """Observed tau of the rolling indicator of residual r and its surrogate p-values.
    Returns dict(tau, p_D22, p_upper, order, engine, n_windows, w)."""
    r = np.asarray(r, float); L = len(r)
    w = int(round(frac * L))
    tau = float(tau_rows(rolling_stat(r[None, :], w, stat))[0])
    model = model or fit_arma(r)
    S = apply_mask(simulate(model, L, nsurr, rng), np.asarray(filled, bool))
    ts = tau_rows(rolling_stat(S, w, stat))
    return dict(tau=tau, p_D22=float((np.sum(ts <= tau) + 1) / (nsurr + 1)),
                p_upper=float((np.sum(ts >= tau) + 1) / (nsurr + 1)),
                order=model["order"], engine=model["engine"], n_windows=L - w + 1, w=w)
