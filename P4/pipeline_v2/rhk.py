"""Step 7 - R'_HK from S (Noyes+1984 recipe, D52 / V35) with the B-V validity band of D53 / V36."""
import numpy as np


def ccf_log(bv):
    return 1.13 * bv ** 3 - 3.91 * bv ** 2 + 2.84 * bv - 0.47


def delta_logc(bv):
    if bv > 0.63:
        return 0.0
    x = 0.63 - bv
    return 0.135 * x - 0.814 * x ** 2 + 6.03 * x ** 3


def rphot(bv):
    return 10 ** (-4.898 + 1.918 * bv ** 2 - 2.893 * bv ** 3)


def rhk_prime(S, bv):
    """R'_HK = R_HK - R_phot with R_HK = 1.340e-4 * C_cf * S. S may be an array; bv scalar."""
    S = np.asarray(S, float)
    rhk = 1.340e-4 * 10 ** (ccf_log(bv) + delta_logc(bv)) * S
    return rhk - rphot(bv), rhk


def band(bv):
    """D53 validity band of R_phot (B-V open interval 0.44 < B-V < 0.82)."""
    if bv < 0.44:
        return "FORA (abaixo de 0.44)"
    if bv < 0.82:
        return "DENTRO"
    if bv <= 1.0:
        return "EXTRAPOLADO (0.82-1.0)"
    return "EXTRAPOLADO (>1.0, incerteza ate 20 %)"


def bv_for_star(row):
    """D52: B-V from the CLS V when it exists, else B95; the source is returned for declaration."""
    if str(row["bv_CLSV"]).strip():
        return float(row["bv_CLSV"]), "CLS V"
    return float(row["bv_B95"]), "B95"
