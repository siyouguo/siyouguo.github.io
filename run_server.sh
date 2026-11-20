#!/bin/sh
# Jekyll 3.x has no --livereload; `serve` watches sources and rebuilds on change
# (refresh the browser manually).
export LANG=en_US.UTF-8
export RUBYOPT=-EUTF-8

# Prefer Homebrew Ruby 3.3 when available (versioned formulas are keg-only).
[ -x /opt/homebrew/opt/ruby@3.3/bin/ruby ] && export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"

# jekyll-github-metadata calls the GitHub API at build time; use the system
# certificate chain so the request works behind a local TLS proxy.
[ -f /etc/ssl/cert.pem ] && export SSL_CERT_FILE="${SSL_CERT_FILE:-/etc/ssl/cert.pem}"

# Prefer the project-local gem install when present (macOS system Ruby can't
# write to /Library/Ruby/Gems, so `BUNDLE_PATH=.bundle/vendor bundle install`
# is the reliable setup here).
[ -d .bundle/vendor ] && export BUNDLE_PATH=.bundle/vendor

exec bundle exec jekyll serve "$@"
