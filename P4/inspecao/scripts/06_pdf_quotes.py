"""Stage 3.11 - literal passages of the PDFs that the inspection report relies on.

Each row of checks.csv says whether a regular expression is found in the text that
pdftotext extracts from the PDF (ligatures normalised, whitespace collapsed). PDFs in
repository root are read from the parent of the package. Requires poppler-utils.
Image-only PDFs (Baliunas+1995) are not covered.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # -I drops the script dir
import re
import subprocess
import unicodedata

from common import ROOT, check, write_out

REPO = os.path.dirname(ROOT)


def text(path):
    raw = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True,
                         check=True).stdout
    raw = unicodedata.normalize("NFKC", raw)
    return re.sub(r"\s+", " ", raw)


PDF = {
    "luhn": os.path.join(ROOT, "bib", "Luhn_2022_ApJL_936_L23.pdf"),
    "baum": os.path.join(ROOT, "bib", "Baum_2022_AJ_163_183.pdf"),
    "cls5": os.path.join(ROOT, "bib", "Isaacson_2024_ApJS_274_35.pdf"),
    "cls6": os.path.join(ROOT, "bib", "Isaacson_2025_AJ_170_181.pdf"),
    "jarv": os.path.join(ROOT, "bib", "Jarvinen_2025_AA_698_A93_arXiv2504.19670.pdf"),
    "luhn_ax": os.path.join(ROOT, "bib", "Luhn_2022_arXiv2207.00612.pdf"),
    "baum_ax": os.path.join(ROOT, "bib", "Baum_2022_arXiv2203.13376.pdf"),
    "noyes": os.path.join(ROOT, "bib", "Noyes1984.pdf"),
    "scheffer": os.path.join(REPO, "Scheffer et al. 2009, Nature 461, 53.pdf"),
    "hk": os.path.join(REPO, "Held & Kleinen 2004, GRL 31, L23207.pdf"),
    "usoskin": os.path.join(REPO, "Usoskin et al. 2017, Living Rev. Sol. Phys. 14, 3.pdf"),
    "egeland": os.path.join(REPO, "Egeland_2017_ApJ_835_25.pdf"),
    "dakos": os.path.join(REPO, "Dakos et al. 2012, PLoS ONE 7, e41010.pdf"),
}
T = {k: text(v) for k, v in PDF.items()}

# (id, description, pdf, regex, expected presence)
Q = [
    ("3.11-01", "Luhn §3.1: noise subtracted 'from the observed values'", "luhn",
     r"subtract these estimates of the random noise on S\s?HK in quadrature from the observed values", True),
    ("3.11-02", "Luhn §3.1: F-test sentence introduced by 'Even when corrected for intrinsic noise differences'",
     "luhn", r"Even when corrected for intrinsic noise differences.{0,160}F-test gives 8\.78", True),
    ("3.11-03", "Luhn §3.1: the words 'within each' season are NOT used for the sigma_S of the minima",
     "luhn", r"in quadrature from the observed values.{0,200}within each", False),
    ("3.11-04", "Luhn §2.2: 'contain 158 observations'", "luhn", r"contain 158 observations", True),
    ("3.11-05", "Luhn §3.1: second minimum 'from 1986 to 1990'", "luhn", r"from 1986 to 1990", True),
    ("3.11-06", "Luhn §3.1: second minimum '(1987.0.1991.0)'", "luhn", r"1987\.0\S{1,3}1991\.0", True),
    ("3.11-07", "Luhn §3.1: 'less than this in six of the nine seasons' follows the 1.2 % value",
     "luhn", r"give .{1,3}S\s?.{0,3}\s?.{0,2}1\.2%.{0,400}less than this in six of the nine seasons", True),
    ("3.11-08", "Baum Abstract: 'analyzed 29 stars with periodic cycles'", "baum",
     r"analyzed 29 stars with periodic cycles", True),
    ("3.11-09", "Baum §2.1.3: 'Fourteen stars in the post-2010 CPS data showed a clear offset'",
     "baum", r"Fourteen stars in the post-2010 CPS data showed a clear offset", True),
    ("3.11-10", "Baum §4.1: HD 101501 'dropped to a low S-value with little variation'", "baum",
     r"dropped to a low S-value with little variation", True),
    ("3.11-11", "Baum §4.1: HD 101501 'possibly still exhibiting a low-amplitude cycle'", "baum",
     r"possibly still exhibiting a low.?amplitude cycle", True),
    ("3.11-12", "Baum §4.2: '14 stars were given new classifications'", "baum",
     r"14 stars were given new classifications", True),
    ("3.11-13", "CLS V §5.6: 'least active star with more than 45 observations is HD 55575'",
     "cls5", r"least active star with more than 45 observations is HD 55575 with a relative dispersion of 0\.0007/0\.1562 = 0\.45%", True),
    ("3.11-14", "CLS V §5.6: 'Fifty stars have a smaller S-value standard deviation than HD 10700'",
     "cls5", r"Fifty stars have a smaller S-value standard deviation than HD 10700", True),
    ("3.11-15", "CLS V §3: B-V is derived from Teff and [Fe/H] (Ramirez & Melendez 2005)", "cls5",
     r"we derive.{0,200}B . V using the Ram.rez & Mel.ndez \(2005\) method, which uses both Teff and \[Fe/H\]", True),
    ("3.11-16", "CLS V Fig. 10 caption: '256 stars that have more than 45 observations'", "cls5",
     r"256 stars that have more than 45", True),
    ("3.11-17", "CLS V §5: '138/284 stars have cycles'", "cls5", r"138/284 stars have cycles", True),
    ("3.11-18", "CLS V §4.3: 'Out of 70 solar-like stars, we find 29 stars with cycles'", "cls5",
     r"Out of 70 solar-like stars, we find 29 stars with cycles", True),
    ("3.11-19", "CLS VI Abstract: sample of 91 solar-type dwarfs", "cls6",
     r"spectra of 91 solar-type G- and K-type main-sequence dwarfs", True),
    ("3.11-20", "CLS VI §3.1: mass division 'reduces the need for a spectral-type indifferent metric'",
     "cls6", r"reduces the need for a spectral-type indifferent metric", True),
    ("3.11-21", "CLS VI §3.3: 'suggestive of a rapid (on stellar timescales) transition'", "cls6",
     r"suggestive of a rapid \(on stellar timescales\) transition", True),
    ("3.11-22", "CLS VI §3.3.1: 'requires a stochastic process that is poorly understood'", "cls6",
     r"requires a stochastic process that is poorly understood", True),
    ("3.11-23", "CLS VI §3.2: tau Ceti 'pole-on inclination'", "cls6",
     r"known to have a pole-on inclination", True),
    ("3.11-24", "CLS VI §5: 'the S-value itself best correlates with S-value variability'", "cls6",
     r"the S-value itself best correlates with S-value variability", True),
    ("3.11-25", "Jarvinen: '13 RAVE stars out of 13 326 (0.1%)'", "jarv",
     r"13 RAVE stars out of 13 326 \(0\.1%\)", True),
    ("3.11-26", "Jarvinen: snapshot observations 'in the presence of undetected rotational modulation and cycles'",
     "jarv", r"snapshot observations in the presence of undetected rotational modulation and cycles", True),
    ("3.11-27", "Noyes §II: the paper concerns 'the mean level of activity'", "noyes",
     r"concerned in this paper with the mean level of activity", True),
    ("3.11-28", "Noyes Appendix b: 'a very significant correction for the chromospherically less active stars'",
     "noyes", r"can be a very significant correction for the chromospherically less active stars", True),
    ("3.11-29", "Noyes §II: 'calibration for B.V > 1.0 may be uncertain by as much as 20%'", "noyes",
     r"may be uncertain by as much as 20%", True),
    ("3.11-30", "Noyes Appendix a: Linsky et al. calibration falls below by 0.3 dex at B-V = 1.25", "noyes",
     r"falls below ours by an amount 0\.3 dex at B.{1,3}V = 1\.25", True),
    ("3.11-31", "Scheffer 2009: Hopf = 'transition from a stable system to an oscillatory system'",
     "scheffer", r"transition from a stable system to an oscillatory system", True),
    ("3.11-32", "Scheffer 2009: critical transitions in cyclic systems 'are less well studied'",
     "scheffer", r"cyclic and chaotic systems are less well studied", True),
    ("3.11-33", "Scheffer 2009: 'We know of no explicit work on early-warning signals for such transitions'",
     "scheffer", r"We know of no explicit work on early-warning signals for such transitions", True),
    ("3.11-34", "File 'Held & Kleinen 2004' is Boulton, Allison & Lenton 2014 (Nature Commun. 5:5752)",
     "hk", r"Early warning signals of Atlantic Meridional Overturning Circulation collapse in a fully coupled climate model Chris A\. Boulton.{0,40}Lenton", True),
    ("3.11-35", "File 'Held & Kleinen 2004' does not carry the Held & Kleinen title in its first page",
     "hk", r"^.{0,3000}Detection of climate system bifurcations by degenerate fingerprinting", False),
    ("3.11-36", "Usoskin 2017: 'hardly able to predict its occurrence'", "usoskin",
     r"a grand minimum should appear soon or later, but presently we are hardly able to predict its occurrence", True),
    ("3.11-37", "Usoskin 2017: 'contrary to some predictions, a Grand minimum of activity has no started'",
     "usoskin", r"contrary to some predictions, a Grand minimum of activity has no started", True),
    ("3.11-38", "Usoskin 2017: start of the Maunder minimum 'not very sudden but via a regular cycle of reduced height'",
     "usoskin", r"might had been not very sudden but via a regular cycle of reduced height", True),
    ("3.11-39", "Egeland 2017: abstract <S_cyc> = 0.1694 +- 0.0005", "egeland",
     r"0\.1694 .{0,3}0\.0005", True),
    ("3.11-40", "Egeland 2017 text: cycle amplitude '0.0145+-0.0014' (abstract/Table 2 give 0.0012)",
     "egeland", r"0\.0145[^0-9]{1,6}0\.0014 in S", True),
    ("3.11-41", "Dakos 2012: rolling windows '25% to 75%' and bandwidths '5 to 200'", "dakos",
     r"25% to 75% of the time series length.{0,80}bandwidths ranging from 5 to 200", True),
    ("3.11-42", "Luhn arXiv draft §2.2: 1995-2002 data scraped from Figure 2 of Olah+2016", "luhn_ax",
     r"scrape the data from Figure 2 of Ol.h et al\. \(2016\) for HD 166620", True),
    ("3.11-43", "Luhn arXiv draft: 'the scraped data is reliable, but not exact'", "luhn_ax",
     r"the scraped data is reliable, but not exact", True),
    ("3.11-44", "Luhn arXiv draft: 'contains 119 (scraped) observations'", "luhn_ax",
     r"contains 119 \(scraped\) observations", True),
    ("3.11-45", "Luhn published: data 'acquired ... courtesy of K. Ol.h and W. Soon' and 158 observations",
     "luhn", r"acquired this data courtesy of K\. Ol.h and W\. Soon", True),
    ("3.11-46", "Luhn arXiv draft: same F-test sentence ('Even corrected for intrinsic noise differences')",
     "luhn_ax", r"Even corrected for intrinsic noise differences.{0,160}F-test gives 8\.78", True),
    ("3.11-47", "Luhn arXiv draft: second minimum S_HK = 0.1724 +- 0.0058 (published rounds to 0.172 +- 0.006)",
     "luhn_ax", r"0\.1724 .{0,3}0\.0058", True),
    ("3.11-48", "Baum arXiv draft: same '29 stars with periodic cycles'", "baum_ax",
     r"analyzed 29 stars with periodic cycles", True),
    ("3.11-49", "Baum arXiv draft: same '14 stars were given new classifications'", "baum_ax",
     r"14 stars were given new classifications", True),
]
for cid, desc, k, rx, want in Q:
    got = bool(re.search(rx, T[k], re.I | re.S))
    check(cid, desc, "yes" if want else "no", "yes" if got else "no",
          os.path.basename(PDF[k]))


# page numbers of each passage (PDF page index; journal page is given in the audit text)
def page_texts(path):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", path], capture_output=True,
                                                        text=True).stdout).group(1))
    out = []
    for pg in range(1, n + 1):
        r = subprocess.run(["pdftotext", "-f", str(pg), "-l", str(pg), path, "-"],
                           capture_output=True, text=True).stdout
        out.append(re.sub(r"\s+", " ", unicodedata.normalize("NFKC", r)))
    return out


PT = {}
lines = ["id | pdf | PDF pages where the pattern is found (page 1 = first page of the file)"]
for cid, desc, k, rx, want in Q:
    if not want:
        continue
    if k not in PT:
        PT[k] = page_texts(PDF[k])
    pgs = [i + 1 for i, t in enumerate(PT[k]) if re.search(rx, t, re.I | re.S)]
    lines.append(f"{cid} | {os.path.basename(PDF[k])} | {pgs or 'spans a page break or not found page-wise'}")
write_out("06_pdf_pages.txt", "\n".join(lines) + "\n")
