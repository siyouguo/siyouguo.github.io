"""Fetch Google Scholar citation count via ScraperAPI proxy + regex parse.

Google Scholar blocks requests from datacenter IPs (including GitHub Actions
runners), so the profile page is fetched through ScraperAPI's residential proxy.
Zero external dependencies — uses only the Python standard library (urllib + regex).
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

# Hardcoded on purpose: the previous env-var lookup let a stale GitHub secret
# (still pointing at the deleted profile) silently override this value. The ID is
# already public in _config.yml and _pages/about.md, so it is not a secret.
GOOGLE_SCHOLAR_ID = "-6apF3oAAAAJ"
SCRAPER_API_KEY = os.environ.get("SCRAPER_API_KEY")
REPO = "siyouguo/siyouguo.github.io"

PROFILE_URL = f"https://scholar.google.com/citations?hl=en&user={GOOGLE_SCHOLAR_ID}"
RAW_DATA_URL = (
    f"https://raw.githubusercontent.com/{REPO}/google-scholar-stats/gs_data.json"
)

# Browser-like User-Agent — ScraperAPI forwards it to Google Scholar.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.36"
)


def http_get(url: str, timeout: int = 120) -> str:
    """Fetch a URL and return the response body as a string."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:500]
        print(f"HTTP {e.code}: {body}", file=sys.stderr)
        raise


def fetch_via_scraperapi(url: str, timeout: int = 120) -> str:
    """Fetch a URL through the ScraperAPI proxy."""
    api_url = (
        "http://api.scraperapi.com"
        f"?api_key={SCRAPER_API_KEY}"
        f"&url={urllib.parse.quote(url, safe='')}"
    )
    return http_get(api_url, timeout=timeout)


def parse_citation_count(html: str) -> int:
    """Extract the total citation count from the profile HTML.

    The stats table (<table id="gsc_rsb_st">) lists Citations, h-index, i10-index.
    The first numeric <td class="gsc_rsb_std"> cell holds the all-time count.
    """
    matches = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)
    if not matches:
        print("DEBUG: HTML snippet (first 2000 chars):", file=sys.stderr)
        print(html[:2000], file=sys.stderr)
        print("ERROR: Could not find citation count in page HTML", file=sys.stderr)
        sys.exit(1)
    return int(matches[0])


def fetch_existing_data() -> dict:
    """Download the existing gs_data.json to preserve per-publication data."""
    try:
        return json.loads(http_get(RAW_DATA_URL, timeout=30))
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

        data = fetch_existing_data()
        data["citedby"] = citedby

        os.makedirs("results", exist_ok=True)

        with open("results/gs_data.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)

        with open("results/gs_data_shieldsio.json", "w") as f:
            json.dump(
                {"schemaVersion": 1, "label": "citations", "message": str(citedby)},
                f,
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
