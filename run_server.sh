#!/bin/sh
# Jekyll 3.9 has no --livereload; `serve` watches sources and rebuilds on change
# (refresh the browser manually).
export LANG=en_US.UTF-8
export RUBYOPT=-EUTF-8

# Prefer the project-local gem install when present (macOS system Ruby can't
# write to /Library/Ruby/Gems, so `BUNDLE_PATH=.bundle/vendor bundle install`
# is the reliable setup here).
[ -d .bundle/vendor ] && export BUNDLE_PATH=.bundle/vendor

exec bundle exec jekyll serve "$@"
