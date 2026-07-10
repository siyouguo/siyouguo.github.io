# Sidebar Card Design — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add card styling (shadow, border, radius, padding) to the sidebar at desktop breakpoints.

**Architecture:** Single SCSS partial edit — add five CSS properties inside the existing `$large` breakpoint block of `.sidebar` in `_sass/_sidebar.scss`.

**Tech Stack:** Jekyll, SCSS (Sass), Susy grid, Minimal Mistakes theme

## Global Constraints

- Desktop-only: changes apply inside `@include breakpoint($large)` (≥925px)
- Use existing SCSS variables where applicable (`$border-color`)
- Preserve existing grid placement, sticky behavior, and opacity transition
- No HTML changes

---

### Task 1: Add card styles to sidebar

**Files:**
- Modify: `_sass/_sidebar.scss:16-25`

**Interfaces:**
- Consumes: `$border-color` from `_variables.scss` (already imported)
- Produces: `.sidebar` card appearance at `$large` breakpoint

- [ ] **Step 1: Add card properties inside the $large breakpoint**

Open `_sass/_sidebar.scss`. Replace lines 16-25:

```scss
  @include breakpoint($large) {
    @include span(2 of 12);
    opacity: 1;
    -webkit-transition: opacity 0.2s ease-in-out;
            transition: opacity 0.2s ease-in-out;

    &:hover {
      opacity: 1;
    }
  }
```

with:

```scss
  @include breakpoint($large) {
    @include span(2 of 12);
    opacity: 1;
    background-color: #fff;
    border: 1px solid $border-color;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    padding: 1.25em;
    -webkit-transition: opacity 0.2s ease-in-out;
            transition: opacity 0.2s ease-in-out;

    &:hover {
      opacity: 1;
    }
  }
```

- [ ] **Step 2: Build the site to verify SCSS compiles**

```
bundle exec jekyll build
```
Expected: Build succeeds with no SCSS errors.

- [ ] **Step 3: Start dev server and visually verify**

```
bundle exec jekyll liveserve
```
Open browser at http://localhost:4000. Resize window to ≥925px width.

Verify:
- [ ] Sidebar has visible card appearance (shadow + border + rounded corners)
- [ ] Sidebar content has breathing room (padding)
- [ ] Sidebar remains sticky on scroll
- [ ] At <925px width (mobile), sidebar looks unchanged (no card)
- [ ] Content area layout is unaffected

- [ ] **Step 4: Commit**

```bash
git add _sass/_sidebar.scss
git commit -m "feat: card-style sidebar with shadow and rounded corners"
```
