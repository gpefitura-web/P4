"""Step 4 - trend removal: Gaussian-kernel smoothing residual, sigma in {1, 3, 5} years, or none (D21, R9)."""
import numpy as np
from scipy.ndimage import gaussian_filter1d

CONFIGS = (None, 1, 3, 5)      # None = no removal; sigma = 1 year is the default (R9)


def residual(x, sigma):
    """x - Gaussian smooth(x, sigma); mode 'nearest' at the edges (as in inspecao/17). sigma=None returns x."""
    x = np.asarray(x, float)
    return x.copy() if sigma is None else x - gaussian_filter1d(x, sigma, mode="nearest")


def label(sigma):
    return "none" if sigma is None else f"s{sigma}"
