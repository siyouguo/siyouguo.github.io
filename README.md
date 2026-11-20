# Siyou Guo — Academic Homepage

[![Website](https://img.shields.io/badge/site-siyouguo.github.io-2ea44f)](https://siyouguo.github.io)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Jekyll](https://img.shields.io/badge/Jekyll-3.10-orange.svg)](https://jekyllrb.com/)

A single-page academic profile at [siyouguo.github.io](https://siyouguo.github.io), built with Jekyll and hosted on GitHub Pages.

## Architecture

```mermaid
flowchart LR
    D[_data] --> I[_includes]
    P[_pages] --> L[_layouts]
    I --> L
    S[assets + _sass] --> O[_site]
    L --> O
    O --> GH[GitHub Pages]
```

## Layout

| Path | Purpose |
| --- | --- |
| `_data/` | News, publications, navigation |
| `_pages/about.md` | Homepage content |
| `_includes/`, `_layouts/` | Components and page composition |
| `_sass/`, `assets/css/main.scss` | Styling |
| `assets/js/main.min.js` | Deployed script bundle |
| `google_scholar_crawler/` | Citation scraper |

## Develop

Ruby 3.3+, Bundler, Python 3.

```bash
BUNDLE_PATH=.bundle/vendor bundle install
./run_server.sh
```

`assets/js/_main.js` and `assets/js/plugins/` are reference sources; only `main.min.js` is deployed.

## Maintain

- Profile and links: `_config.yml`, `_pages/about.md`
- News: `_data/news.yml`
- Publications: `_data/publications.yml`
- Citation count: run `cd google_scholar_crawler && python3 main.py`, then push the generated JSON to the orphan `google-scholar-stats` branch
- Deployment: push to `main`; GitHub Pages builds automatically

MIT license. See [LICENSE](LICENSE).
