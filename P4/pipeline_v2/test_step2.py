"""Step 2 check: MW and Keck segment lengths = inspecao/saidas/17_recommendation_support.txt s.2 and
catalogue column serie_MW_segmento_max_anos / serie_Keck_segmento_max_anos."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p4io, annual

REF = {"10700": ([29], [20]), "23249": ([29], [24]), "182572": ([35], [16, 5]), "190360": ([28], [25]),
       "10476": ([36], [24]), "152391": ([36], [4, 11]), "166620": ([30], [1, 17]), "26965": ([29], [20]),
       "4628": ([30], [14]), "101501": ([28], [9])}
ok = True
cat = p4io.load_catalog()
for _, r in cat.iterrows():
    if r.serie_fonte == "Egeland2017_T4":
        continue
    o = p4io.load_star(r.HD, r)
    res = {}
    for era in ("MW", "Keck"):
        a = annual.annual_means(o, era)
        res[era] = [len(s["years"]) for s in annual.segments(a)] if len(a) else []
    mw = max(res["MW"], default=None); kk = max(res["Keck"], default=None)
    em = int(r.serie_MW_segmento_max_anos) if r.serie_MW_segmento_max_anos else None
    ek = int(r.serie_Keck_segmento_max_anos) if r.serie_Keck_segmento_max_anos else None
    good = (mw == em) and (kk == ek or r.serie_fonte == "v2001" and ek is None)
    if r.HD in REF:
        good &= (res["MW"], res["Keck"]) == REF[r.HD]
    ok &= good
    print(r.HD, r.serie_fonte, "MW", res["MW"], "cat", em, "| Keck", res["Keck"], "cat", ek, "PASS" if good else "FAIL")
print("ALL OK" if ok else "SOME FAIL")
