"""Fetch Google Scholar citation count via a single ScraperAPI request + regex parse.

This avoids the scholarly library's multi-request scraping which is slow and unreliable
from GitHub Actions datacenter IPs. Instead we make ONE HTTP request through ScraperAPI
and extract the total citation count from the profile page's HTML table.
"""
import json
import os
import re
import sys
import requests

GOOGLE_SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "ZKXXk4IAAAAJ")
SCRAPER_API_KEY = os.environ.get("SCRAPER_API_KEY")
REPO = "siyouguo/siyouguo.github.io"

PROFILE_URL = f"https://scholar.google.com/citations?user={GOOGLE_SCHOLAR_ID}&hl=en"
RAW_DATA_URL = (
    f"https://raw.githubusercontent.com/{REPO}/google-scholar-stats/gs_data.json"
)


def fetch_via_scraperapi(url: str, timeout: int = 120) -> str:
    """Fetch a URL through ScraperAPI proxy."""
    api_url = f"http://api.scraperapi.com?api_key={SCRAPER_API_KEY}&url={url}"
    resp = requests.get(api_url, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def parse_citation_count(html: str) -> int:
    """Extract the total citation count from Google Scholar profile HTML.

    The stats table (<table id="gsc_rsb_st">) lists Citations, h-index, i10-index.
    The first <td class="gsc_rsb_std"> contains the all-time citation count.
    """
    matches = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)
    if not matches:
        print("ERROR: Could not find citation count in page HTML", file=sys.stderr)
        sys.exit(1)
    return int(matches[0])


def fetch_existing_data() -> dict:
    """Download existing gs_data.json to preserve per-publication citation data."""
    try:
        resp = requests.get(RAW_DATA_URL, timeout=30)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return {}


def main() -> None:
    if not SCRAPER_API_KEY:
        print("ERROR: SCRAPER_API_KEY is not set", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching Google Scholar profile via ScraperAPI...", file=sys.stderr)
    html = fetch_via_scraperapi(PROFILE_URL)

    citedby = parse_citation_count(html)
    print(f"Total citations: {citedby}", file=sys.stderr)

    # Preserve existing per-publication data, update citedby
    existing = fetch_existing_data()
    existing['citedby'] = citedby

    os.makedirs("results", exist_ok=True)

    with open("results/gs_data.json", "w") as f:
        json.dump(existing, f, ensure_ascii=False)

    with open("results/gs_data_shieldsio.json", "w") as f:
        json.dump({
            "schemaVersion": 1,
            "label": "citations",
            "message": str(citedby),
        }, f)

    print(f"Done: gs_data.json, gs_data_shieldsio.json (citedby={citedby})",
          file=sys.stderr)


if __name__ == "__main__":
    main()
