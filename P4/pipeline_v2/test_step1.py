"""Step 1 check: counts must equal checks 3.2-01, 3.2-22 (Baum), 3.15-01 (v2001), 3.12-01 (Egeland)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p4io

ok = True
def chk(name, exp, got):
    global ok
    r = "PASS" if exp == got else "FAIL"
    ok &= exp == got
    print(f"{name}: expected {exp}, got {got} -> {r}")

chk("3.2-01 Baum rows (all)", 62135, len(p4io.load_baum(drop_sigma=False)))
chk("3.2-22 Baum rows (no sigma flag)", 61662, len(p4io.load_baum()))
chk("3.2-02 Baum stars", 59, p4io.load_baum(False).HD.nunique())
v = p4io.load_v2001()
chk("3.15-01 v2001 stars", 35, v.HD.nunique())
chk("3.12-01 Egeland rows", 6349, len(p4io.load_egeland()))
cat = p4io.load_catalog(only_included=False)
chk("catalog rows (manuscript: stars of Baliunas Table 2)", 112, len(cat))
chk("clean Flat stars", 5, int((cat.grupo_P4 == "Flat_limpa").sum()))
chk("clean Flat stars with a series", 4, int(((cat.grupo_P4 == "Flat_limpa") & (cat.status_amostra == "incluida")).sum()))
chk("calibration stars excluded (D13)", 17, int(cat.motivo.str.startswith("D13").sum()))
chk("binaries excluded (R11)", 2, int(cat.motivo.str.startswith("R11").sum()))
c = p4io.load_catalog()
print("catalog included:", len(c), c.serie_fonte.value_counts().to_dict())
for _, r in c.iterrows():
    n = len(p4io.load_star(r.HD, r))
    if n == 0:
        ok = False; print("EMPTY series", r.HD)
print("ALL OK" if ok else "SOME FAIL")
