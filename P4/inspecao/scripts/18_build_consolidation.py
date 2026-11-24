"""Build the DRAFT consolidated catalogue consolidacao/p4_star_catalog.csv for the researcher's signature.
Inputs (read-only): frozen baliunas_table2_full.csv, consolidacao/rascunho_reparos_catalogo.csv, baum2022_59stars.csv,
data/J_AJ_163_183_table1.tsv, data/HK_Project_v2001_NSO/*.mgd, data/J_ApJS_274_35_table2.tsv, audit/saar_baliunas_crossmatch.csv.
Rules applied are ONLY those decided in D13, D68-D102 (D95 option v, D98 gaps, D100 minimum segment, R1 binarity rule, R11).
Nothing is selected by looking at stellar values. Run with `python -I`; output is deterministic."""
import csv
import hashlib
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, check, write_out

REPO = ROOT
FROZEN = os.path.join(REPO, "baliunas_table2_full.csv")
frozen = list(csv.DictReader(open(FROZEN, encoding="utf-8")))
sha_frozen = hashlib.sha256(open(FROZEN, "rb").read()).hexdigest()

# ---- repairs (side file, D64) -------------------------------------------------------------------
rep = list(csv.DictReader(open(os.path.join(REPO, "consolidacao", "rascunho_reparos_catalogo.csv"), encoding="utf-8")))
patch = defaultdict(dict)
note = defaultdict(list)
grade_rep = {}
for r in rep:
    patch[r["HD"]][r["campo"]] = r["valor_proposto"]
    note[r["HD"]].append(f"{r['campo']}: '{r['valor_atual']}' -> '{r['valor_proposto']}'")
    grade_rep[r["HD"]] = r["grau"]

# ---- auxiliary sources ----------------------------------------------------------------------------
baum = {r["HD"]: r for r in csv.DictReader(open(os.path.join(REPO, "baum2022_59stars.csv"), encoding="utf-8"))}
t1_years = defaultdict(lambda: defaultdict(set))
for ln in open(os.path.join(REPO, "data", "J_AJ_163_183_table1.tsv"), encoding="utf-8"):
    if ln.startswith("#") or ";" not in ln:
        continue
    p = [x.strip() for x in ln.rstrip("\n").split(";")]
    if p[0].isdigit() and p[4] != "sigma":
        t1_years[p[0]]["MW" if p[3].startswith("HKP") else "Keck"].add(int(float(p[2])))
v2001 = {}
D2001 = os.path.join(REPO, "data", "HK_Project_v2001_NSO")
for fn in sorted(os.listdir(D2001)):
    if fn.endswith(".mgd"):
        hd = fn[2:-4].lstrip("0").upper()
        ys = set()
        for ln in open(os.path.join(D2001, fn), encoding="latin-1"):
            f = ln.split()
            if len(f) >= 10:
                jd = 2444000.0 + float(f[2])
                ys.add(int(2000.0 + (jd - 2451544.5) / 365.25))
        v2001[hd] = ys
clsv = {}
for ln in open(os.path.join(REPO, "data", "J_ApJS_274_35_table2.tsv"), encoding="utf-8"):
    if ln.startswith("#") or ";" not in ln:
        continue
    p = [x.strip() for x in ln.rstrip("\n").split(";")]
    m = re.match(r"HD (\w+)$", p[0])
    if m:
        clsv[m.group(1)] = {"bv": p[6], "nobs": p[5]}
saar = {r["HD"]: r for r in csv.DictReader(open(os.path.join(REPO, "audit", "saar_baliunas_crossmatch.csv"), encoding="utf-8"))}

STD17 = set("9562 13421 29645 45067 76572 89744 107213 124570 136202 142373 143761 159332 187013 187691 207978 212754 216385".split())
APPB = set("3443 39587 76572 81809 88355 114378 124570 137107 141004 156026 158614 178428".split())
R11_EXCLUDE = {"81809", "219834A"}
SEVEN = [r["HD"] for r in frozen if r["primary_class"] in ("Flat", "Flat?") and r["HD"] not in STD17]
FIVE = sorted(set(SEVEN) - APPB, key=int)           # R1


def segments(ys):
    s = sorted(ys)
    segs, start = [], s[0]
    for a, b in zip(s, s[1:]):
        if b - a - 1 >= 3:                           # D98: gaps of 1-2 years are filled, gaps >= 3 years split
            segs.append(a - start + 1)
            start = b
    segs.append(s[-1] - start + 1)
    return segs


COLS = ["HD", "star", "bv_B95", "bv_CLSV", "sptype", "S_B95", "classe_B95", "P_cyc", "dP", "FAP", "P_cyc_tentativo",
        "secondary", "grau_catalogo", "reparo_aplicado", "grau_reparo", "classe_Baum", "P_Saar", "P_Baum_ou_classe",
        "padrao_D13", "apendiceB_binaria", "subgigante_catalogo", "logg_Baum", "vsini_Baum", "FeH_Baum",
        "grupo_P4", "serie_fonte", "serie_MW_segmento_max_anos", "serie_Keck_segmento_max_anos", "indicador_elegivel_D100",
        "status_amostra", "motivo", "confirmar_na_assinatura"]
out_rows = []
for r in frozen:
    hd = r["HD"]
    pt = patch.get(hd, {})
    P = pt.get("P_cyc", r["P_cyc"])
    dP = pt.get("dP", r["dP"])
    sec = r["secondary"]
    if "secondary" in pt:
        sec = pt["secondary"]
    # group (R1, v5/v6 groups)
    if hd in FIVE:
        grupo = "Flat_limpa"
    elif r["primary_class"] == "CYCLE" and r["FAP"] == "Excellent":
        grupo = "CYCLE_Excellent"
    elif r["primary_class"] == "Var":
        grupo = "Var"
    elif r["primary_class"] == "Long":
        grupo = "Long"
    else:
        grupo = "fora_dos_grupos"
    # series source (D95 option v: Baum + v2001 layer; Sun from Egeland)
    if hd in t1_years:
        fonte = "Baum"
        mw = segments(t1_years[hd]["MW"]) if t1_years[hd]["MW"] else []
        kk = segments(t1_years[hd]["Keck"]) if t1_years[hd]["Keck"] else []
    elif hd in v2001:
        fonte = "v2001"
        mw, kk = segments(v2001[hd]), []
    elif hd == "(Sun)":
        fonte, mw, kk = "Egeland2017_T4", [], []
    else:
        fonte, mw, kk = "nenhuma", [], []
    mwmax = max(mw) if mw else ""
    kmax = max(kk) if kk else ""
    elig = "sim" if (mw and max(mw) >= 24) else ("ver_P4_SOURCE_VALUES" if fonte == "Egeland2017_T4" else "nao")
    # status
    if hd in STD17:
        status, motivo = "excluida", "D13: estrela-padrao de calibracao"
    elif hd in R11_EXCLUDE:
        status, motivo = "excluida", "R11 (D102): binaria composta/resolvida nos controles"
    elif grupo == "fora_dos_grupos":
        status, motivo = "fora_dos_grupos", "classe sem grupo definido em v5/v6"
    elif fonte == "nenhuma":
        status, motivo = "sem_serie", "sem serie em Baum nem em v2001"
    else:
        status, motivo = "incluida", "grupo + serie disponivel"
    confirm = "sim" if (status == "incluida" and grupo in ("Var", "Long")) else ""
    b = baum.get(hd, {})
    sp = r["sptype"]
    sub = "sim" if re.search(r"\bI[Vv]\b|IV|Iv|Vp", sp) else "nao"
    out_rows.append({
        "HD": hd, "star": r["star"], "bv_B95": r["bv"], "bv_CLSV": clsv.get(hd, {}).get("bv", ""), "sptype": sp,
        "S_B95": r["S"], "classe_B95": r["primary_class"], "P_cyc": P, "dP": dP, "FAP": r["FAP"],
        "P_cyc_tentativo": pt.get("P_cyc_tentativo", ""), "secondary": sec, "grau_catalogo": r["grade"],
        "reparo_aplicado": "; ".join(note.get(hd, [])), "grau_reparo": grade_rep.get(hd, ""),
        "classe_Baum": b.get("class_Baum", ""), "P_Saar": saar.get(hd, {}).get("saar_Pcyc", ""),
        "P_Baum_ou_classe": b.get("class_Baum", ""), "padrao_D13": "sim" if hd in STD17 else "nao",
        "apendiceB_binaria": "sim" if hd in APPB else "nao", "subgigante_catalogo": sub,
        "logg_Baum": b.get("logg", ""), "vsini_Baum": b.get("vsini", ""), "FeH_Baum": b.get("FeH", ""),
        "grupo_P4": grupo, "serie_fonte": fonte, "serie_MW_segmento_max_anos": mwmax,
        "serie_Keck_segmento_max_anos": kmax, "indicador_elegivel_D100": elig, "status_amostra": status,
        "motivo": motivo, "confirmar_na_assinatura": confirm})

OUT = os.path.join(REPO, "consolidacao", "p4_star_catalog.csv")
with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, lineterminator="\n")
    w.writeheader()
    w.writerows(out_rows)
sha_out = hashlib.sha256(open(OUT, "rb").read()).hexdigest()

# ---- summary ----------------------------------------------------------------------------------------
from collections import Counter
cnt = Counter((r["grupo_P4"], r["status_amostra"]) for r in out_rows)
lines = ["grupo_P4 | status_amostra | n"] + [f"{g} | {s} | {n}" for (g, s), n in sorted(cnt.items())]
lines += ["", f"sha256 frozen baliunas_table2_full.csv: {sha_frozen}", f"sha256 p4_star_catalog.csv: {sha_out}"]
write_out("18_catalog_summary.txt", "\n".join(lines) + "\n")

check("3.20-01", "rows of p4_star_catalog.csv", 112, len(out_rows), "baliunas_table2_full.csv (frozen, D36)")
check("3.20-02", "frozen catalogue unchanged (sha256 first 16)", "recorded", sha_frozen[:16], "baliunas_table2_full.csv", info=True)
check("3.20-03", "five clean Flat by R1 (D13 + B95 Appendix B)", "10700,23249,43587,182572,190360", ",".join(FIVE), "D102 R1")
check("3.20-04", "catalogue rows carrying a repair note (6 tentative periods, 219834A, 76572 and 33 secondary normalisations; some overlap)", "", sum(1 for r in out_rows if r["reparo_aplicado"]),
      "consolidacao/rascunho_reparos_catalogo.csv; 6 tentative periods + 219834A + 76572 are 8 stars; 33 secondary normalisations are separate", info=True)
check("3.20-05", "secondary normalisations applied", 33, sum(1 for r in out_rows if "secondary" in r["reparo_aplicado"]), "rascunho_reparos 3.13-02")
incl = [r for r in out_rows if r["status_amostra"] == "incluida"]
check("3.20-06", "included stars without any series source", 0, sum(1 for r in incl if r["serie_fonte"] == "nenhuma"), "catalogue")
check("3.20-07", "included stars | with an indicator-eligible MW segment >= 24 yr (D100)", "",
      f"{len(incl)} | {sum(1 for r in incl if r['indicador_elegivel_D100'] == 'sim')}", "saidas/18_catalog_summary.txt", info=True)
check("3.20-08", "excluded: D13 standards | R11 binaries", "17 | 2", f"{sum(1 for r in out_rows if r['padrao_D13'] == 'sim')} | "
      f"{sum(1 for r in out_rows if r['status_amostra'] == 'excluida' and r['motivo'].startswith('R11'))}", "D13, D102 R11")

# ---- sign-off condition: nothing graded C or X in P4_SOURCE_VALUES.md (sections 1-6 only) -------------------
sv = open(os.path.join(REPO, "consolidacao", "P4_SOURCE_VALUES.md"), encoding="utf-8").read().split("## Apêndice")[0]
grades = [ln.rstrip().rstrip("|").rsplit("|", 1)[-1].strip() for ln in sv.splitlines() if re.match(r"\| V\d\d ", ln)]
check("3.20-09", "entries of P4_SOURCE_VALUES.md (sections 1-6) graded C or X", 0, sum(1 for g in grades if g[:1] in ("C", "X")),
      "consolidacao/P4_SOURCE_VALUES.md §7")
check("3.20-10", "entries of P4_SOURCE_VALUES.md (sections 1-6)", "", len(grades), "consolidacao/P4_SOURCE_VALUES.md", info=True)

# ---- final star list for signature (R2: written and dated before any temporal indicator is computed) -----------
DATE = "2026-11-24"
L = [f"# Lista final de estrelas — RASCUNHO PARA ASSINATURA ({DATE})", "",
     "**Estado:** preparada por Claude a pedido do pesquisador; **não assinada**. Cumpre R2 (D102): a lista é escrita e datada **antes de calcular qualquer indicador temporal**; até esta data **nenhum AR(1), variância em janela ou τ de Kendall foi calculado em estrela real** (o que existe são estatísticas descritivas e testes sintéticos sem valores de S).",
     "", f"**Catálogo:** `consolidacao/p4_star_catalog.csv`, sha256 `{sha_out}`; catálogo congelado `baliunas_table2_full.csv`, sha256 `{sha_frozen}` (inalterado).",
     "**Regras aplicadas (só as decididas):** D13 (padrões excluídas); R1 (cinco `Flat`); R11 (HD 81809 e 219834A fora); D95 opção (v) (Baum e v2001, Sol por Egeland); D98 (lacunas); D100 (segmento ≥ 24 anos). Nada foi escolhido olhando valores de S.", "",
     "## Contagem por grupo e situação", "", "| Grupo | Situação | n |", "|---|---|---|"]
for (g, s_), n in sorted(cnt.items()):
    L.append(f"| {g} | {s_} | {n} |")
L += ["", "## Estrelas incluídas, por grupo", "", "| HD | Grupo | Série | Segmento Mount Wilson (anos) | Segmento Keck (anos) | Indicador (D100) | Confirmar |", "|---|---|---|---|---|---|---|"]
order = {"Flat_limpa": 0, "CYCLE_Excellent": 1, "Var": 2, "Long": 3}
for r in sorted((r for r in out_rows if r["status_amostra"] == "incluida"), key=lambda r: (order[r["grupo_P4"]], r["HD"].zfill(8))):
    L.append(f"| {r['HD']} | {r['grupo_P4']} | {r['serie_fonte']} | {r['serie_MW_segmento_max_anos']} | {r['serie_Keck_segmento_max_anos']} | {r['indicador_elegivel_D100']} | {r['confirmar_na_assinatura']} |")
L += ["", "## Fora da amostra e por quê", "", "| HD | Grupo | Motivo |", "|---|---|---|"]
for r in sorted((r for r in out_rows if r["status_amostra"] in ("excluida", "sem_serie") and r["grupo_P4"] != "fora_dos_grupos"), key=lambda r: (order.get(r["grupo_P4"], 9), r["HD"].zfill(8))):
    L.append(f"| {r['HD']} | {r['grupo_P4']} | {r['status_amostra']}: {r['motivo']} |")
L += ["", f"(As {sum(1 for r in out_rows if r['grupo_P4'] == 'fora_dos_grupos')} estrelas do catálogo sem grupo definido em v5/v6 ficam no CSV com `status_amostra = fora_dos_grupos` ou `excluida`.)", "",
      "## Pontos a confirmar na assinatura (não decididos por Claude)",
      "1. **Var e Long entram como grupos de referência?** D102 não o diz; v5/v6 usam os quatro grupos (Flat, CYCLE+Excellent, Var, Long). Marcadas com `Confirmar = sim` na tabela. [ ] sim  [ ] não  [ ] só alguns",
      "2. **HD 219834B** consta em Baum mas não tem linhas na Tabela 1: fica `sem_serie`. [ ] de acordo",
      "3. **Sol:** entra por Egeland (Tabela 4, 1966–2016), série exploratória (R10); o critério de segmento de D100 não se aplica à série composta. [ ] de acordo",
      "4. **O indicador temporal só roda nas estrelas com segmento Mount Wilson ≥ 24 anos** (coluna \"Indicador\"). [ ] de acordo", "",
      "## Assinatura (REG-01)",
      "Aprovo esta lista e o `p4_star_catalog.csv` e o `P4_SOURCE_VALUES.md` correspondentes como a consolidação do P4, e autorizo a etapa seguinte (reconstrução do pipeline em passada única, contra esta referência congelada).", "",
      "Nome: ____________________   Data: ____/____/______   Assinatura: ____________________", ""]
with open(os.path.join(REPO, "consolidacao", f"LISTA_FINAL_ESTRELAS_{DATE}.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(L))
