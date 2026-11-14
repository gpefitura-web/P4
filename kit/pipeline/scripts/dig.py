"""Ajudantes de leitura para os textos extraídos (ver extract_texts.py).

Uso em Python: import sys; sys.path.insert(0, 'scripts'); from dig import *
Defina TXT_DIR com o diretório usado em extract_texts.py.
"""
import re

TXT_DIR = "/tmp/txt/"


def load(k):
    t = open(TXT_DIR + k + ".txt").read()
    pages = {int(m.group(1)): m.start() for m in re.finditer(r"=====PAGE (\d+)=====", t)}
    pg = lambda pos: max(p for p, s in pages.items() if s <= pos)
    return t, pages, pg


def head(k, n=2500):
    t, _, _ = load(k)
    print(t[:n].replace("\n", " "))


def hits(k, pats, w=450, b=150, n=2):
    t, pages, pg = load(k)
    for pat in pats:
        ms = list(re.finditer(pat, t))
        print(f"## {pat}: {len(ms)} hits, pages {sorted({pg(m.start()) for m in ms})[:12]}")
        for m in ms[:n]:
            print(f"[{k} p{pg(m.start())}] ...{t[max(0, m.start()-b):m.start()+w]}...".replace("\n", " "))
            print()


def page(k, p, a=0, b=3500):
    t, pages, _ = load(k)
    print(t[pages[p]:pages.get(p + 1, len(t))][a:b])
