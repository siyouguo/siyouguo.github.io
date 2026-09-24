# Siyou Guo · Personal Academic Website

A personal academic website built with **Jekyll** and hosted on **GitHub Pages** at [siyouguo.github.io](https://siyouguo.github.io).

## About

This site serves as my academic homepage — a single-page profile featuring:

- **Publications** with citation counts
- **News & updates**
- **Education** timeline
- **Honors & awards**
- **Bilingual profile** (Chinese / English)

Built on a customized version of the [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) Jekyll theme, with custom research paper box components, badge styling, and responsive design.

## Project Structure

```
├── _config.yml          # Site configuration
├── _data/               # Navigation and structured content data
│   ├── navigation.yml   # Main navigation links
│   ├── news.yml         # Homepage news entries
│   └── publications.yml # Publication metadata
├── _includes/           # Reusable HTML components
├── _layouts/            # Page layout templates
├── _pages/              # Main page content (about.md → /)
├── _sass/               # SCSS partials
├── assets/              # Static assets (CSS, JS, fonts)
├── images/              # Organized image resources
│   ├── profile/         # Personal profile images
│   ├── affiliations/    # University and organization logos
│   ├── publications/    # Paper thumbnails and figures
│    └── icons/           # Favicon and web manifest
└── google_scholar_crawler/  # Google Scholar citation scraper
```

## Features

- **Responsive design** — mobile-friendly layout
- **Citation badge** — Google Scholar stats refreshed by running the local crawler script (see below)
- **Structured content** — News and publication metadata are maintained in `_data/` and rendered through reusable includes
- **Shields.io badges** — citation counts served from the `google-scholar-stats` branch
- **Image performance** — publication figures use lazy loading; profile and affiliation images use descriptive alt text

## Getting Started

### Prerequisites

- Ruby (with Bundler)
- Python 3 (for the Google Scholar crawler)

### Local Development

```bash
# Install Ruby dependencies. On macOS with the system Ruby, a project-local
# path avoids sudo (run_server.sh picks it up automatically):
BUNDLE_PATH=.bundle/vendor bundle install

# Start the dev server. Jekyll 3.9 has no live reload: the server rebuilds on
# file changes, refresh the browser to see them.
./run_server.sh
```

### Google Scholar Stats

Google Scholar blocks datacenter IPs, so stats are refreshed manually from a
local machine (no CI job, no third-party proxy needed):

```bash
cd google_scholar_crawler
python3 main.py   # stdlib only; writes results/*.json with the citation count

# Publish to the orphan branch the shields.io badge reads from:
tmp=$(mktemp -d) && cp results/*.json "$tmp/" && cd "$tmp"
git init && git add *.json && git commit -m "Updated Citation Data"
git push git@github.com:siyouguo/siyouguo.github.io.git HEAD:google-scholar-stats --force
```

## Deployment

Automatically deployed via GitHub Pages on every push to `main`.
