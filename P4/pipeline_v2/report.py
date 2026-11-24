"""Step 9 - facts report from results/*.csv and h1.json. No interpretation. Group tests copy mw_test of cell 20 of p4_pipeline.ipynb."""
import os, json, sys
import numpy as np, pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, "results")


def md(df, floatfmt="{:.3f}"):
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(floatfmt.format(v) if isinstance(v, (float, np.floating)) else str(v) for v in r) + " |")
    return "\n".join(out)


def mw_test(df, g1, g2, metric, alt="greater"):      # copied from cell 20 (Group -> grupo)
    a = df[df.grupo == g1][metric].dropna().values
    b = df[df.grupo == g2][metric].dropna().values
    if len(a) < 2 or len(b) < 2:
        return dict(g1=g1, g2=g2, metric=metric, U=np.nan, p=np.nan, med1=np.nan, med2=np.nan, sig="--", n1=len(a), n2=len(b))
    U, p = stats.mannwhitneyu(a, b, alternative=alt)
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "n.s."
    return dict(g1=g1, g2=g2, metric=metric, U=float(U), p=float(p), med1=float(np.median(a)), med2=float(np.median(b)),
                sig=sig, n1=len(a), n2=len(b))


res = pd.read_csv(os.path.join(R, "star_results.csv"), dtype={"HD": str})
seg = pd.read_csv(os.path.join(R, "segments.csv"), dtype={"HD": str})
met = pd.read_csv(os.path.join(R, "star_metrics.csv"), dtype={"HD": str})
h1 = json.load(open(os.path.join(R, "h1.json")))
L = ["# REPORT — fatos do pipeline_v2 (execução única, sem interpretação)", "",
     "Cada tabela cita o arquivo de origem em `pipeline_v2/results/`. Sementes fixas (base 20261124), 1 000 surrogates ARMA(p,q), "
     "p, q ∈ {0,1,2} por AIC. `p_upper` = P(τ* ≥ τ) (direção CSD); `p_D22` = P(τ* ≤ τ) (D22 literal). "
     "Configurações de tendência: none, s1, s3, s5 (σ em anos). Concordância = nº de configurações com τ > 0 e p_upper < 0.05.", ""]
L += ["## 1. Segmentos e amostra (`segments.csv`)", "", md(seg.fillna("")), ""]

L += ["## 2. H1 — HD 166620, σ_S por estado (`h1.json`; fonte: Luhn+2022 Tabela 2)", ""]
st = pd.DataFrame(h1["states"]).T.reset_index().rename(columns={"index": "estado"})
L += [md(st, "{:.5g}"), ""]
frows = []
for k, v in h1.items():
    if k.startswith("F_"):
        for kind, f in v.items():
            frows.append(dict(comparacao=k[2:], variancias=kind, F=f["F"], p_unilateral=f["p_one"], p_bilateral=f["p_two"]))
L += [md(pd.DataFrame(frows), "{:.4g}"), ""]

main = res[(res.series == "S")]
L += ["## 3. Indicador temporal por segmento, série S, janela 50 % (`star_results.csv`)", "",
      "H2 (exploratório, n = 1): linhas de HD 166620. Sol: exploratório (série composta de Egeland).", ""]
for stat, name in (("ac1", "AR(1) lag-1"), ("var", "variância")):
    d = main[(main.frac == 0.5) & (main["stat"] == stat)]
    piv = d.pivot_table(index=["HD", "grupo", "seg_year0", "L"], columns="config", values=["tau", "p_upper", "p_D22"], aggfunc="first")
    flat = pd.DataFrame({f"{a}_{b}": piv[(a, b)] for a in ("tau", "p_upper", "p_D22") for b in ("none", "s1", "s3", "s5")}).reset_index()
    sig = d.assign(c=((d.tau > 0) & (d.p_upper < 0.05))).groupby(["HD", "seg_year0"]).c.sum().rename("concordantes_de_4").reset_index()
    flat = flat.merge(sig, on=["HD", "seg_year0"]); flat["HD"] = flat["HD"].astype(str)
    L += [f"### 3.{1 if stat == 'ac1' else 2} {name}", "", md(flat, "{:.3f}"), ""]

L += ["## 4. Varredura de janela 25–75 % (`star_results.csv`): configurações concordantes (de 20 = 4 tendências × 5 janelas)", ""]
sw = main.assign(c=((main.tau > 0) & (main.p_upper < 0.05))).groupby(["HD", "seg_year0", "stat"]).c.sum().unstack("stat").reset_index()
sw.columns = ["HD", "seg_year0", "var_de_20", "ac1_de_20"]
L += [md(sw[["HD", "seg_year0", "ac1_de_20", "var_de_20"]]), ""]

rr = res.pivot_table(index=["HD", "seg_year0", "config", "frac", "stat"], columns="series", values="tau")
L += ["## 5. R′_HK contra S (`star_results.csv`)", "",
      f"Linhas comparadas: {len(rr)}; |τ(R′_HK) − τ(S)| máximo = {np.abs(rr.RHK - rr.S).max():.3g}. "
      "Segmentos com banda de R_phot e fonte de B−V: ver seção 1 (`banda_Rphot`, `bv_fonte`).", ""]

L += ["## 6. Testes entre grupos (lógica da célula 20 do pipeline antigo; `star_metrics.csv`)", "",
      "Uma linha por estrela (segmento MW mais longo; Sol excluído por ser exploratório). Mann–Whitney unilateral (greater).", ""]
best = met.sort_values("L", ascending=False).drop_duplicates(["HD", "config"])
best = best[best.HD != "(Sun)"]
tests = []
for cfg in ("none", "s1", "s3", "s5"):
    d = best[best.config == cfg]
    for metric in (("ac1", "var_norm") if cfg in ("none", "s1") else ("ac1",)):
        for g1, g2 in (("Var", "Flat_limpa"), ("Long", "Flat_limpa"), ("CYCLE_Excellent", "Flat_limpa"),
                       ("Var", "CYCLE_Excellent"), ("Long", "CYCLE_Excellent")):
            t = mw_test(d, g1, g2, metric); t["config"] = cfg; tests.append(t)
L += [md(pd.DataFrame(tests)[["config", "metric", "g1", "g2", "U", "p", "med1", "med2", "sig", "n1", "n2"]], "{:.4g}"), ""]
open(os.path.join(R, "REPORT.md"), "w").write("\n".join(L) + "\n")
print("report written")
