"""Fetch full-text PDFs for included studies via the Elsevier Article Retrieval API.

Works for Elsevier DOIs (10.1016/...) under the WU entitlement (VPN required).
Non-Elsevier titles are written to corpus/fulltext_missing.csv for manual
download via the WU library. PDFs land in literature/ as Author_Year_<doisuffix>.pdf.
"""
import csv
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = (ROOT / ".scopus_api_key").read_text().strip()
LIT = ROOT / "literature"
LIT.mkdir(exist_ok=True)

rows = [r for r in csv.DictReader(open(ROOT / "corpus" / "screening_2026-07-17.csv", encoding="utf-8-sig"))
        if r["screen_decision"] == "include"]

def fname(r):
    author = re.sub(r"[^A-Za-z]", "", r["first_author"].split()[0]) or "Unknown"
    suffix = re.sub(r"[^A-Za-z0-9]+", "-", r["doi"].split("/", 1)[-1])[:40] if r["doi"] else r["eid"][-10:]
    return f"{author}_{r['year']}_{suffix}.pdf"

ok, skipped, failed, missing = 0, 0, [], []
for r in rows:
    doi = r["doi"]
    if not doi or not doi.startswith("10.1016/"):
        missing.append(r)
        continue
    out = LIT / fname(r)
    if out.exists() and out.stat().st_size > 10_000:
        skipped += 1
        continue
    req = urllib.request.Request(
        f"https://api.elsevier.com/content/article/doi/{doi}?httpAccept=application%2Fpdf",
        headers={"X-ELS-APIKey": KEY},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        if data[:4] == b"%PDF":
            out.write_bytes(data)
            ok += 1
            print(f"OK   {out.name} ({len(data)//1024} KB)")
        else:
            failed.append((r, "not a PDF response"))
            print(f"FAIL {r['first_author']} ({r['year']}): non-PDF response")
    except Exception as e:
        failed.append((r, str(e)))
        print(f"FAIL {r['first_author']} ({r['year']}): {e}")
    time.sleep(1)  # gentle on the API quota

with open(ROOT / "corpus" / "fulltext_missing.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["first_author", "year", "journal", "title", "doi", "reason"])
    for r in missing:
        w.writerow([r["first_author"], r["year"], r["journal"], r["title"], r["doi"], "non-Elsevier - fetch via WU library"])
    for r, err in failed:
        w.writerow([r["first_author"], r["year"], r["journal"], r["title"], r["doi"], f"API failed: {err}"])

print(f"\ndownloaded: {ok} | already present: {skipped} | failed: {len(failed)} | manual (non-Elsevier): {len(missing)}")
print("manual-download list: corpus/fulltext_missing.csv")
