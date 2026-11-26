"""Places the sunspot group-number file of Vaquero et al. (2016, Solar Physics 291, 3061; revised collection v1.12, 2016-05-12) in data/ after
checking its sha256 and its header. The file is not redistributed here: its terms of use (SILSO / HASO) have not been checked yet, and the
download address has not been validated, so it is not guessed. Obtain the file from the data distributors named in the paper and pass it with --from.
Usage: python -I fetch_vaquero.py --from PATH_TO_GNobservations_JV_V1-12.csv   (or no argument, if data/ already holds it)"""
import os, sys, shutil, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); DEST = os.path.join(os.path.dirname(HERE), "data", "Vaquero2016_GNobservations_JV_V1-12.csv")
SHA = "b2e8ac30b2643018490298e68ffe22f0c98a12da4921418a44b478edb49a4028"
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""): h.update(ch)
    return h.hexdigest()
src = sys.argv[sys.argv.index("--from") + 1] if "--from" in sys.argv else DEST
if not os.path.isfile(src): sys.exit(f"missing {src}: pass the file with --from (see the docstring)")
if sha(src) != SHA: sys.exit("sha256 differs from the file used in the manuscript; not accepted")
head = open(src, encoding="utf-8", errors="replace").read(400)
if "A REVISED COLLECTION OF SUNSPOT GROUP NUMBERS" not in head or "v1.12" not in head: sys.exit("unexpected header")
if os.path.abspath(src) != os.path.abspath(DEST): os.makedirs(os.path.dirname(DEST), exist_ok=True); shutil.copy2(src, DEST)
print("Vaquero 2016 v1.12 OK:", DEST)
