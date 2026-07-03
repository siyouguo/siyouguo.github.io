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
├── _data/               # Navigation & data files
├── _includes/           # Reusable HTML components
├── _layouts/            # Page layout templates
├── _pages/              # Main page content (about.md → /)
├── _sass/               # SCSS partials
├── assets/              # Static assets (CSS, JS, fonts)
├── images/              # Image resources
└── google_scholar_crawler/  # Google Scholar citation scraper
```

## Features

- **Responsive design** — mobile-friendly layout
- **Auto-updating citations** — Google Scholar stats fetched daily via GitHub Actions
- **Live reload** — Hawkins gem for instant dev feedback
- **Shields.io badges** — citation counts served via jsDelivr CDN

## Getting Started

### Prerequisites

- Ruby (with Bundler)
- Python 3 (for the Google Scholar crawler)

### Local Development

```bash
# Install Ruby dependencies
bundle install

# Start the dev server with live reload
bundle exec jekyll liveserve
# or
./run_server.sh
```

### Google Scholar Crawler

```bash
cd google_scholar_crawler
pip3 install -r requirements.txt
python3 main.py
```

A GitHub Actions workflow runs the crawler daily at 8:00 UTC and commits results to the `google-scholar-stats` branch.

## Deployment

Automatically deployed via GitHub Pages on every push to `main`.
