"""Integration check of a rendered chapter opening (requires pdfplumber/pypdf).

Usage: python tests/check_pdf_opening.py FILE --chapter 13 --title "Chapter title"
Visual inspection and testing in the reader itself remain separate.
"""
import argparse
import re

import pdfplumber
from pypdf import PdfReader


def check(path, chapter, title):
    text = PdfReader(path).pages[0].extract_text()
    assert re.match(rf"Chapter {chapter}\s", text), "chapter label is not ordinary untracked text"
    with pdfplumber.open(path) as pdf:
        words = pdf.pages[0].extract_words(extra_attrs=["fontname", "size"])
    expected = title.split()
    start = next(i for i in range(len(words))
                 if [w["text"] for w in words[i:i + len(expected)]] == expected)
    heading = words[start:start + len(expected)]
    opening = words[start + len(expected)]
    assert all("bold" in w["fontname"].lower() for w in heading), "title lacks a bold font"
    assert min(w["size"] for w in heading) > opening["size"], "title is not larger than body"
    assert opening["top"] - max(w["bottom"] for w in heading) >= 12, "title runs into opening"
    assert abs(heading[0]["x0"] - opening["x0"]) < 1, "chapter opening is indented"
    return "PASS: normal chapter label; bold distinct title; separated, flush-left opening"


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pdf")
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--title", required=True)
    args = ap.parse_args()
    print(check(args.pdf, args.chapter, args.title))
