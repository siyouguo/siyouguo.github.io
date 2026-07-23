"""Fetch Google Scholar citation count via a single ScraperAPI request + regex parse.

Zero external dependencies — uses only Python stdlib (urllib).
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

GOOGLE_SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "ZKXXk4IAAAAJ")
SCRAPER_API_KEY = os.environ.get("SCRAPER_API_KEY")
REPO = "siyouguo/siyouguo.github.io"

PROFILE_URL = f"https://scholar.google.com/citations?user={GOOGLE_SCHOLAR_ID}&hl=en"
RAW_DATA_URL = (
    f"https://raw.githubusercontent.com/{REPO}/google-scholar-stats/gs_data.json"
)


def http_get(url: str, timeout: int = 120) -> str:
    """Fetch a URL and return the response body as a string."""
    req = urllib.request.Request(url, headers={"User-Agent": "curl/7.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:500]
        print(f"HTTP {e.code}: {body}", file=sys.stderr)
        raise


def fetch_via_scraperapi(url: str, timeout: int = 120) -> str:
    """Fetch a URL through ScraperAPI proxy."""
    api_url = (
        f"http://api.scraperapi.com"
        f"?api_key={SCRAPER_API_KEY}"
        f"&url={urllib.parse.quote(url, safe='')}"
    )
    return http_get(api_url, timeout=timeout)


def parse_citation_count(html: str) -> int:
    """Extract the total citation count from Google Scholar profile HTML.

    The stats table (<table id="gsc_rsb_st">) lists Citations, h-index, i10-index.
    The first <td class="gsc_rsb_std"> contains the all-time citation count.
    """
    matches = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)
    if not matches:
        print("DEBUG: HTML snippet (first 2000 chars):", file=sys.stderr)
        print(html[:2000], file=sys.stderr)
        print("ERROR: Could not find citation count in page HTML", file=sys.stderr)
        sys.exit(1)
    return int(matches[0])


def fetch_existing_data() -> dict:
    """Download existing gs_data.json to preserve per-publication citation data."""
    try:
        text = http_get(RAW_DATA_URL, timeout=30)
        return json.loads(text)
    except Exception as e:
        print(f"Note: Could not fetch existing gs_data.json: {e}", file=sys.stderr)
        return {}


def main() -> None:
    if not SCRAPER_API_KEY:
        print("ERROR: SCRAPER_API_KEY is not set", file=sys.stderr)
        sys.exit(1)

    try:
        print("Fetching Google Scholar profile via ScraperAPI...", file=sys.stderr)
        html = fetch_via_scraperapi(PROFILE_URL)

        citedby = parse_citation_count(html)
        print(f"Total citations: {citedby}", file=sys.stderr)

        existing = fetch_existing_data()
        existing["citedby"] = citedby

        os.makedirs("results", exist_ok=True)

        with open("results/gs_data.json", "w") as f:
            json.dump(existing, f, ensure_ascii=False)

        with open("results/gs_data_shieldsio.json", "w") as f:
            json.dump(
                {"schemaVersion": 1, "label": "citations", "message": str(citedby)}, f
            )

        print(
            f"Done: gs_data.json, gs_data_shieldsio.json (citedby={citedby})",
            file=sys.stderr,
        )

    except Exception as e:
        print(f"FATAL: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
