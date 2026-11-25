"""Step 8 - single official run on the included stars (D04: no tuning after seeing the output).
Usage: python -I run_all.py   (writes results/*.csv, results/h1.json, results/run_log.txt)"""
import os, sys, json, time
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p4io, annual, indicators as ind, detrend as dt, surrogates as sg, rhk, state_comparison as sc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
BASE_SEED, NSURR, MIN_SEG = 20261124, 1000, 24
FRACS, STATS = ind.FRACS, ("ac1", "var")


def precision(L):
    return "baixa" if L < 40 else "adequada"


def main():
    t0 = time.time()
    cat = p4io.load_catalog()
    log = []
    rows, metrics, segrows = [], [], []
    for ci, r in cat.iterrows():
        sun = r.serie_fonte == "Egeland2017_T4"
        if not sun and r.indicador_elegivel_D100 != "sim":
            segrows.append(dict(HD=r.HD, grupo=r.grupo_P4, fonte=r.serie_fonte, seg_year0="", L="", rodou="nao",
                                motivo="indicador_elegivel_D100 = nao (segmento MW < 24 anos): so descricao"))
            continue
        obs = p4io.load_star(r.HD, r)
        ann = annual.annual_means(obs, None if sun else "MW")
        bv, bvsrc = (float(r.bv_CLSV), "CLS V") if str(r.bv_CLSV).strip() else (float(r.bv_B95), "B95")
        for si, seg in enumerate(annual.segments(ann)):
            L = len(seg["years"])
            if L < MIN_SEG:
                segrows.append(dict(HD=r.HD, grupo=r.grupo_P4, fonte=r.serie_fonte, seg_year0=seg["year0"], L=L,
                                    rodou="nao", motivo="segmento < 24 anos: so descricao"))
                continue
            segrows.append(dict(HD=r.HD, grupo=r.grupo_P4, fonte=r.serie_fonte, seg_year0=seg["year0"], L=L,
                                n_filled=int(seg["filled"].sum()), precisao=precision(L), rodou="sim", motivo="",
                                bv=bv, bv_fonte=bvsrc, banda_Rphot=rhk.band(bv),
                                exploratorio="sim" if sun or L < 40 else "nao"))
            series = {"S": seg["S"], "RHK": rhk.rhk_prime(seg["S"], bv)[0]}
            for ki, (sname, x) in enumerate(series.items()):
                for gi, sigma in enumerate(dt.CONFIGS):
                    res = dt.residual(x, sigma)
                    rng = np.random.default_rng([BASE_SEED, ci, si, ki, gi])
                    model = sg.fit_arma(res)
                    Ssur = sg.apply_mask(sg.simulate(model, L, NSURR, rng), seg["filled"])
                    for frac in FRACS:
                        w = ind.window_size(L, frac)
                        for stat in STATS:
                            tau = float(sg.tau_rows(sg.rolling_stat(res[None, :], w, stat))[0])
                            ts = sg.tau_rows(sg.rolling_stat(Ssur, w, stat))
                            rows.append(dict(HD=r.HD, grupo=r.grupo_P4, fonte=r.serie_fonte, seg_year0=seg["year0"], L=L,
                                             series=sname, config=dt.label(sigma), frac=frac, w=w, n_windows=L - w + 1,
                                             stat=stat, tau=tau,
                                             p_D22=(np.sum(ts <= tau) + 1) / (NSURR + 1),
                                             p_upper=(np.sum(ts >= tau) + 1) / (NSURR + 1),
                                             arma=f"{model['order']}", engine=model["engine"]))
                    if sname == "S":
                        metrics.append(dict(HD=r.HD, grupo=r.grupo_P4, seg_year0=seg["year0"], L=L, config=dt.label(sigma),
                                            ac1=ind.ac1(res), var_norm=float(np.var(res, ddof=1) / np.mean(x) ** 2)))
            log.append(f"{r.HD} seg {seg['year0']} L={L} done {time.time() - t0:.0f}s")
    df = pd.DataFrame(rows); df.to_csv(os.path.join(OUT, "star_results.csv"), index=False)
    pd.DataFrame(segrows).to_csv(os.path.join(OUT, "segments.csv"), index=False)
    pd.DataFrame(metrics).to_csv(os.path.join(OUT, "star_metrics.csv"), index=False)
    with open(os.path.join(OUT, "h1.json"), "w") as fh:
        json.dump(sc.run_h1(), fh, indent=1)
    with open(os.path.join(OUT, "run_log.txt"), "w") as fh:
        fh.write("\n".join(log) + f"\nseed base {BASE_SEED}, {NSURR} surrogates, total {time.time() - t0:.0f}s\n")
    print("rows", len(df), "time", round(time.time() - t0))


if __name__ == "__main__":
    main()
