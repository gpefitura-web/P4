"""Step 2 - annual series (D08 calendar-year mean), per instrument era, gap rule D98, segments."""
import numpy as np
import pandas as pd


def annual_means(obs, era=None):
    """Mean S per calendar year; optionally restricted to one era ('MW' or 'Keck').
    Returns DataFrame [year, S, n]."""
    d = obs if era is None else obs[obs.era == era]
    y = np.floor(d.t.values).astype(int)
    g = pd.DataFrame({"year": y, "S": d.S.values}).groupby("year").S.agg(["mean", "size"])
    return g.rename(columns={"mean": "S", "size": "n"}).reset_index()


def segments(ann, max_fill=2):
    """D98: split at gaps of >= 3 missing years; fill gaps of 1-2 missing years linearly.
    Returns list of dicts: year0, years (array), S (array), filled (bool array)."""
    ann = ann.sort_values("year")
    yrs, S = ann.year.values, ann.S.values
    out, start = [], 0
    for i in range(1, len(yrs) + 1):
        if i == len(yrs) or yrs[i] - yrs[i - 1] - 1 > max_fill:
            sy, ss = yrs[start:i], S[start:i]
            full = np.arange(sy[0], sy[-1] + 1)
            filled = ~np.isin(full, sy)
            out.append({"year0": int(sy[0]), "years": full,
                        "S": np.interp(full, sy, ss), "filled": filled})
            start = i
    return out
