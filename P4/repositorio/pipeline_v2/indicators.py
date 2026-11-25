"""Step 3 - early-warning indicators: lag-1 autocorrelation (AR(1)), variance, rolling window, Kendall tau."""
import numpy as np
from scipy.stats import kendalltau

FRACS = (0.25, 0.375, 0.5, 0.625, 0.75)   # D20: 50 % default, sweep 25-75 %


def ac1(x):
    """Lag-1 autocorrelation, mean-centred within the window (same estimator as inspecao 16/17)."""
    x = np.asarray(x, float)
    m = x.mean()
    d = np.sum((x - m) ** 2)
    return np.sum((x[:-1] - m) * (x[1:] - m)) / d if d > 0 else np.nan


def variance(x):
    return float(np.var(np.asarray(x, float), ddof=1))


def window_size(L, frac=0.5):
    return int(round(frac * L))


def rolling(x, frac=0.5, stat=ac1):
    """Statistic in a sliding window of frac*L points, step 1. Returns array of length L-w+1."""
    x = np.asarray(x, float)
    w = window_size(len(x), frac)
    return np.array([stat(x[s:s + w]) for s in range(len(x) - w + 1)])


def kendall_tau(r):
    """Kendall tau of a rolling indicator against window index (time)."""
    r = np.asarray(r, float)
    if len(r) < 3 or np.all(r == r[0]) or np.isnan(r).any():
        return np.nan
    return float(kendalltau(np.arange(len(r)), r)[0])
