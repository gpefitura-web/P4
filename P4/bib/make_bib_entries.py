"""Prints BibTeX entries built from the Crossref record of each DOI (the ADS needs a personal API token that is not available here; REG-R4).
Usage: SSL_CERT_FILE=... python3 -I make_bib_entries.py > new_entries.bib"""
import json, re, html, urllib.request, ssl, os
ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE"))
KEYS = {"lockwood2007": "10.1086/516752", "saar1999": "10.1086/307794", "olah2016": "10.1051/0004-6361/201628479", "wright2004": "10.1086/423221",
        "metcalfe2017": "10.1007/s11207-017-1157-5", "shah2018": "10.3847/2041-8213/aad40c", "jarvinen2025": "10.1051/0004-6361/202554111",
        "isaacson2025": "10.3847/1538-3881/adf2a8", "livina2007": "10.1029/2006GL028672", "rehfeld2011": "10.5194/npg-18-389-2011",
        "boettiger2012a": "10.1098/rsif.2012.0125", "boettiger2012b": "10.1098/rspb.2012.2085", "boettiger2013": "10.1007/s12080-013-0192-6",
        "boettner2022": "10.1103/PhysRevResearch.4.013230", "lenton2012": "10.1098/rsta.2011.0304"}
ACC = {"ä": "{\\\"a}", "ö": "{\\\"o}", "ü": "{\\\"u}", "é": "{\\'e}", "á": "{\\'a}", "í": "{\\'i}", "ó": "{\\'o}", "ú": "{\\'u}", "ø": "{\\o}", "ñ": "{\\~n}", "ç": "{\\c c}", "š": "{\\v s}", "č": "{\\v c}"}
tex = lambda s: "".join(ACC.get(c, c) for c in html.unescape(re.sub(r"<[^>]+>", "", s))).replace("&", "\\&")
for key, doi in KEYS.items():
    req = urllib.request.Request(f"https://api.crossref.org/works/{doi}")
    m = json.load(urllib.request.urlopen(req, context=ctx, timeout=60))["message"]
    au = " and ".join(f"{tex(a.get('family',''))}, {tex(a.get('given',''))}" for a in m["author"])
    pages = m.get("page") or m.get("article-number", "")
    print(f"@article{{{key},\n  author  = {{{au}}},\n  title   = {{{{{tex(m['title'][0])}}}}},\n  journal = {{{tex(m['container-title'][0])}}},\n  year    = {{{m['issued']['date-parts'][0][0]}}},")
    if m.get("volume"): print(f"  volume  = {{{m['volume']}}},")
    if m.get("issue"): print(f"  number  = {{{m['issue']}}},")
    print(f"  pages   = {{{pages.replace('-', '--')}}},\n  doi     = {{{doi}}}}}\n")
