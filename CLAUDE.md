# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- **Start dev server**: `bundle exec jekyll liveserve` (or `./run_server.sh`) — uses the `hawkins` gem for live reload
- **Install dependencies**: `bundle install`
- **Fetch Google Scholar stats locally**: `cd google_scholar_crawler && pip3 install -r requirements.txt && python3 main.py`

## Architecture

This is a **Jekyll static site** hosted on GitHub Pages at `siyouguo.github.io`. It serves as Siyou Guo's academic personal website — a single-page profile with publications, news, education, and honors sections.

**Page structure**: The single page lives at `_pages/about.md` (permalink: `/`). It uses the `default` layout (`_layouts/default.html`) which composes: `head.html` → `masthead.html` → `sidebar.html` (with `author-profile.html`) → page content → `footer.html` → `scripts.html`. SCSS partials in `_sass/` are compiled into `assets/css/main.css` by Jekyll's Sass pipeline.

**Google Scholar integration**: A Python script (`google_scholar_crawler/main.py`) uses the `scholarly` library to fetch citation counts from Google Scholar. A GitHub Actions workflow (`.github/workflows/google_scholar_crawler.yaml`) runs this daily at 8:00 UTC, committing the resulting JSON to the orphan `google-scholar-stats` branch. The site displays the citation badge via shields.io, pulling data from jsDelivr CDN (or raw GitHub) based on the `google_scholar_stats_use_cdn` config flag.

**Navigation**: Defined in `_data/navigation.yml`. The masthead renders anchor links pointing to sections on the single about page (`/#about-me`, `/#-news`, `/#-publications`, etc.).

**Theme foundation**: The site is built on a modified version of the Minimal Mistakes Jekyll theme, customized with research paper box components, badge styling, and a Chinese/English bilingual author profile.
