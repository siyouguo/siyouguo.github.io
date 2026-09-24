# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

- **Start dev server**: `./run_server.sh` (runs `bundle exec jekyll serve`; Jekyll 3.9 has no `--livereload`, the server rebuilds on change and you refresh manually)
- **Install dependencies**: `bundle install`
- **Fetch Google Scholar stats locally**: `cd google_scholar_crawler && python3 main.py` (stdlib only; then push `results/*.json` to the orphan `google-scholar-stats` branch, see README)

## Architecture

This is a **Jekyll static site** hosted on GitHub Pages at `siyouguo.github.io`. It serves as Siyou Guo's academic personal website — a single-page profile with publications, news, education, and honors sections.

**Page structure**: The single page lives at `_pages/about.md` (permalink: `/`). It contains the profile introduction and delegates the News and Publications sections to `_includes/news-list.html` and `_includes/publication-list.html`. Their content is maintained as structured data in `_data/news.yml` and `_data/publications.yml`. The `default` layout (`_layouts/default.html`) composes: `head.html` → `masthead.html` → `sidebar.html` (with `author-profile.html`) → page content → `footer.html` → `scripts.html`. SCSS partials in `_sass/` are compiled into `assets/css/main.css` by Jekyll's Sass pipeline.

**Google Scholar integration**: A Python script (`google_scholar_crawler/main.py`) fetches the citation count directly from the profile page using stdlib `urllib` + regex (no external deps). It must run from a local/residential IP — Google Scholar blocks datacenter IPs (GitHub Actions runners), and the ScraperAPI free tier no longer covers Scholar's protected domain, so there is no scheduled CI job anymore; stats are refreshed manually and pushed to the orphan `google-scholar-stats` branch. The Scholar ID `-6apF3oAAAAJ` is hardcoded in `main.py`. The site displays the citation badge via shields.io reading `gs_data_shieldsio.json` from that branch (raw GitHub or jsDelivr CDN per the `google_scholar_stats_use_cdn` config flag).

**Navigation**: Defined in `_data/navigation.yml`. The masthead renders anchor links pointing to sections on the single about page (`/#about-me`, `/#-news`, `/#-publications`, etc.).

**Theme foundation**: The site is built on a modified version of the Minimal Mistakes Jekyll theme, customized with research paper box components, badge styling, and a Chinese/English bilingual author profile.

**Image organization**: Images are grouped by purpose under `images/profile/`, `images/affiliations/`, `images/publications/`, and `images/icons/`. Keep new assets in the matching directory and update all references when moving files.
