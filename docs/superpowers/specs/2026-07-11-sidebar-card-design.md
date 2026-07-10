# Sidebar Card Design

**Date:** 2026-07-11
**Status:** approved

## Problem

The homepage has a two-column layout (sidebar + content) on desktop, but both columns share the same white background with no visual separation. The sidebar blends into the content area, lacking hierarchy.

## Design Decision

**Card-style sidebar** — wrap the entire sidebar in a card with subtle shadow, border, and rounded corners at desktop breakpoints. On mobile (stacked layout), the sidebar sits above content so no card treatment needed.

## Visual Spec

Applied to `.sidebar` at `$large` breakpoint (≥925px):

| Property | Value | Rationale |
|----------|-------|-----------|
| `background-color` | `#fff` | Ensures card stands out |
| `border` | `1px solid $border-color` | Subtle boundary definition |
| `border-radius` | `8px` | Soft, not cartoonish |
| `box-shadow` | `0 2px 8px rgba(0, 0, 0, 0.08)` | Moderate elevation, like Material elevation-2 |
| `padding` | `1.25em` | Breathing room between card edge and content |

- **No background color on sidebar region** — the card itself provides separation via shadow + border against the page's white background. Adding a tinted background to the sidebar column would be redundant.
- **Single unified card** — the sidebar content (avatar, name, bio, links) reads as one "business card." Splitting into multiple sub-cards would fragment the identity.

## Implementation

Single file change in `_sass/_sidebar.scss`:

1. Inside the existing `@include breakpoint($large)` block for `.sidebar`, add the card properties.
2. The existing `span(2 of 12)` grid placement, sticky positioning, and opacity transition are preserved.
3. No HTML changes needed.

### Before (current)
```scss
.sidebar {
  @include breakpoint($large) {
    @include span(2 of 12);
    opacity: 1;
    ...
  }
}
```

### After
```scss
.sidebar {
  @include breakpoint($large) {
    @include span(2 of 12);
    opacity: 1;
    background-color: #fff;
    border: 1px solid $border-color;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    padding: 1.25em;
    ...
  }
}
```

## Scope

- **In scope:** One SCSS file (`_sass/_sidebar.scss`), ~5 new CSS properties
- **Out of scope:** Mobile behavior (unchanged), content changes, other page elements
