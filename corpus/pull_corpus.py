"""Pull the full SLR corpus from Scopus (query = system of record, proposal.tex).

Run with WU VPN connected:  python corpus/pull_corpus.py
Saves raw JSON pages to corpus/raw/ and a flat CSV to corpus/.
The run date is stamped into the filenames; the saved export is the frozen corpus.
"""
import csv
import json
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY = (ROOT / ".scopus_api_key").read_text().strip()
RUN_DATE = date.today().isoformat()
RAW_DIR = ROOT / "corpus" / "raw" / RUN_DATE
RAW_DIR.mkdir(parents=True, exist_ok=True)

QUERY = (
    'TITLE(("artificial intelligence" OR "machine learning" OR "deep learning" OR "AI")) '
    'AND TITLE-ABS-KEY(("invest" OR "invests" OR "invested" OR "investing" OR "investment" '
    'OR "investments" OR "investor" OR "investors" OR adopt* OR implement*) '
    'AND ("competitive advantage" OR "firm performance" OR "financial performance" '
    'OR "firm productivity" OR "firm value" OR "market value" OR "firm growth")) '
    'AND SUBJAREA(BUSI OR ECON OR DECI) AND PUBYEAR > 2014 AND PUBYEAR < 2027 '
    'AND DOCTYPE(ar) AND LANGUAGE(english) AND SRCTYPE(j)'
)

PAGE = 25  # max for view=COMPLETE


def fetch(start):
    params = urllib.parse.urlencode(
        {"query": QUERY, "count": PAGE, "start": start, "view": "COMPLETE"}
    )
    req = urllib.request.Request(
        f"https://api.elsevier.com/content/search/scopus?{params}",
        headers={"X-ELS-APIKey": KEY, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def authors(entry):
    a = entry.get("author") or []
    return "; ".join(x.get("authname", "") for x in a)


entries = []
start, total = 0, None
while total is None or start < total:
    data = fetch(start)
    sr = data["search-results"]
    total = int(sr["opensearch:totalResults"])
    page_no = start // PAGE
    (RAW_DIR / f"page_{page_no:02d}.json").write_text(
        json.dumps(data, indent=1), encoding="utf-8"
    )
    entries.extend(sr.get("entry", []))
    print(f"page {page_no:02d}: {len(entries)}/{total}")
    start += PAGE
    time.sleep(0.5)  # stay well under the API rate limit

csv_path = ROOT / "corpus" / f"corpus_{RUN_DATE}.csv"
cols = [
    "eid", "doi", "year", "authors", "first_author", "title", "journal",
    "issn", "eissn", "volume", "pages", "citedby", "openaccess",
    "authkeywords", "abstract",
]
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for e in entries:
        w.writerow([
            e.get("eid", ""),
            e.get("prism:doi", ""),
            (e.get("prism:coverDate") or "")[:4],
            authors(e),
            e.get("dc:creator", ""),
            e.get("dc:title", ""),
            e.get("prism:publicationName", ""),
            e.get("prism:issn", ""),
            e.get("prism:eIssn", ""),
            e.get("prism:volume", ""),
            e.get("prism:pageRange", ""),
            e.get("citedby-count", ""),
            e.get("openaccess", ""),
            e.get("authkeywords", ""),
            e.get("dc:description", ""),
        ])

print(f"\nrun date : {RUN_DATE}")
print(f"records  : {len(entries)} (Scopus total: {total})")
print(f"raw JSON : {RAW_DIR}")
print(f"csv      : {csv_path}")
assert len(entries) == total, "record count mismatch - do not use this export"
