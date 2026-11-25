"""Fetches Table 4 of Egeland et al. (2017, ApJ 835, 25), the calibrated solar S-index series (machine-readable table), from the
journal's public server and checks it against the sha256 recorded when the analysis was run. The table is not redistributed in this package.
Usage: python -I fetch_egeland_table4.py            download (skipped if a file with the right hash is already in data/)
       python -I fetch_egeland_table4.py --from F   use a local copy F of the table instead of downloading (offline use)"""
import os, sys, hashlib, shutil, urllib.request

URL = "https://content.cld.iop.org/journals/0004-637X/835/1/25/revision1/apjaa4e49t4_mrt.txt"
SHA256 = "6e2746d535d7d9e3e69ebc860b840494b5efca5460e613cc43fc46e060a90548"
HERE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(os.path.dirname(HERE), "data", "Egeland2017_table4_apjaa4e49t4_mrt.txt")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


if os.path.exists(DEST) and sha(DEST) == SHA256:
    print("Egeland Table 4 already present, hash OK"); sys.exit(0)
os.makedirs(os.path.dirname(DEST), exist_ok=True)
tmp = DEST + ".part"
if len(sys.argv) == 3 and sys.argv[1] == "--from":
    shutil.copyfile(sys.argv[2], tmp)
else:
    with urllib.request.urlopen(URL, timeout=60) as r, open(tmp, "wb") as fh:
        shutil.copyfileobj(r, fh)
if sha(tmp) != SHA256:
    os.remove(tmp)
    sys.exit("sha256 mismatch: the file is not the table used in the article (expected " + SHA256 + ")")
os.replace(tmp, DEST)
print("Egeland Table 4 saved to", DEST, "hash OK")
