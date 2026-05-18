# Build Tasks: Ruby Community Guides

Generated from: `.design/ruby-community-guides/DESIGN_BRIEF.md`  
Architecture: `.design/ruby-community-guides/DESIGN_ARCHITECTURE.md`  
Tokens: `_sass/theme.scss`  
Date: 2026-05-17

---

## Foundation

- [x] **Rewrite `_sass/base.scss`**: Global element styles using new tokens. Set `font-family` to `--font-body` on `body`, `--font-display` on headings. Apply `--color-bg`, `--color-text`, `--line-height-relaxed` for prose. Set `--max-width-prose` on the default reading column. Remove all Rubik references. _Replaces existing file. Depends on: `theme.scss` tokens._

- [x] **Rewrite `_sass/components.scss`**: Start fresh. Add only the nav component to begin — site title styled with `--color-accent`, nav links using `--color-link` / `--color-link-hover`, clean horizontal layout, no decoration. Establish the BEM or flat naming convention that all future components will follow. _Replaces existing file. New component: `.nav`._

- [x] **Update `_layouts/default.html`**: Rewrite the base layout. Nav should show site title + Meetups + Conferences links. Wrap content in a semantically correct `<main>`. Remove Rubik preload, keep Inter/Nunito Google Fonts link already added. Add a minimal `<footer>` placeholder. _Modifies existing file._

- [x] **Rewrite `_sass/utilities.scss`**: Minimal set of utility classes derived from tokens — text sizes, spacing helpers, visually-hidden class for accessibility. Nothing that duplicates component styles. _Replaces existing file._

---

## Core UI

- [x] **Build `_layouts/guide.html`**: New layout extending `default.html`. On desktop (≥1024px), renders a two-column CSS grid: side TOC column (`--toc-width`) + prose column (`--max-width-prose`). On mobile/tablet, single column with TOC column hidden. The layout shell only — TOC content and styling come in the next task. _New file. Depends on: `default.html`, `base.scss`._

- [x] **Build `_includes/toc.html` + `.toc` styles in `components.scss`**: Side table of contents include. Renders an `<nav aria-label="Guide contents">` with a list of chapter links passed in via Jekyll front matter or generated from page headings. Styles: `--color-toc-text`, `--color-toc-text-active`, `--color-toc-marker` for the active indicator, `position: sticky` on desktop. Keyboard accessible. _New include + new component. Depends on: `guide.html`._

- [x] **Build `_includes/quote.html` + `.quote` styles in `components.scss`**: Reusable inline interview excerpt. Accepts `quote` and `attribution` parameters via Jekyll include syntax. Renders as a `<blockquote>` with `<cite>`. Styled with `--color-quote-border` (left bar), `--color-quote-bg`, `--color-quote-text`, `--color-quote-cite`. Should read quietly within prose flow — not a callout box. _New include + new component._

- [x] **Rebuild `index.md` + homepage styles in `components.scss`**: Homepage content and layout. Sections in order: (1) purpose statement prose, (2) guide track links (Meetups / Conferences as prominent typographic links, equal weight, no cards), (3) Voices/credibility section listing organizer names and communities. Text-led, warm, no hero imagery. Add `.home`, `.guide-links`, `.voices` component styles. _Modifies existing file. New components._

- [x] **Build `conferences/index.md`**: Conference guide placeholder page using `default` layout. Contains: guide title, honest status note, brief scope paragraph, quiet link home. Establishes the `/conferences/` URL so the nav link works. _New file._

- [x] **Rebuild `meetups/index.md`**: Meetup guide page using `guide` layout. Includes front matter for TOC chapters. Prose content with named chapter headings (Place, Platform, Talks, Food & Sponsors, Promotion, Keeping It Going, etc.). Embed at least two `{% include quote.html %}` instances in appropriate chapters to validate quote component in context. _Modifies existing file. Depends on: `guide.html`, `toc.html`, `quote.html`._

---

## Responsive & Polish

- [ ] **Responsive pass on `media.scss`**: Add breakpoint rules for the guide layout (TOC column collapse at tablet/mobile), nav wrapping, homepage guide-links stacking on mobile. No tokens here — only layout behaviour changes at breakpoints. _New content in `media.scss`._

- [ ] **Typography polish pass on `base.scss`**: Review heading hierarchy, paragraph spacing, blockquote styling, and link underline behaviour across all three pages in a browser. Tune `--space-*` values between chapters, tighten or loosen where reading rhythm feels off. _Modifies `base.scss`._

- [ ] **Accessibility pass**: Verify focus styles on all interactive elements using `--color-border-focus` / `--shadow-focus`. Check heading hierarchy on all three pages. Confirm TOC is keyboard-navigable. Add `aria-current="page"` to active nav link. Verify `prefers-reduced-motion` is respected for any transitions. _Touches `base.scss`, `components.scss`, layout files._

---

## Review

- [ ] **Design review**: Run `/design-review` once all pages are built and the site is running locally. Check against the brief: editorial tone, RubyEvents visual continuity, reading experience, quote integration, TOC behaviour, mobile layout, dark mode.
