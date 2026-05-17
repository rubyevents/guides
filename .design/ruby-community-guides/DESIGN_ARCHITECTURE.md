# Design Architecture: Ruby Community Guides

## Site Map

- Home `/`
- Meetup Guide `/meetups/`
- Conference Guide `/conferences/`

That is the complete public surface of the site. Interview transcripts remain under `interviews/` in the repository but are excluded from the Jekyll build via `_config.yml`; they are source material, not pages.

## Navigation Model

- **Primary navigation**: Site title (links home) + two guide links: **Meetups** and **Conferences**. No other primary nav items.
- **Secondary navigation**: Within guide pages only. Desktop: a persistent side table of contents listing named chapter headings, anchored to the active section. Mobile: a simple inline contents list near the top of the page, not floating or app-like.
- **Utility navigation**: None. No account, settings, search, or footer mega-nav.
- **Mobile navigation**: The primary nav collapses gracefully to a minimal bar. The guide side TOC is not shown on mobile; the inline top-of-page contents serves that purpose instead.

## Content Hierarchy

### Home `/`

1. **Site identity and purpose statement** — a compact, clearly written explanation of what these guides are and who they are for. Not a tagline, not a manifesto. Two to four sentences.
2. **Guide track links** — prominent typographic links to Meetups and Conferences, equal in visual weight. Text-led, not cards.
3. **Voices and credibility** — a named list of the organizers whose experience informed the guides. Names, roles, and communities. Establishes trust without making interviews the product.
4. **Secondary framing** — brief "how to use these guides" note or similar, if needed. Below the fold.

### Meetup Guide `/meetups/`

1. **Guide title and lead paragraph** — orients the reader and sets the narrative tone.
2. **Mobile contents** — visible only on small screens; a simple in-page list of chapter names with anchor links.
3. **Named chapters in order** — long-form narrative prose, broken into named sections matching the pillar structure (Place, Platform, Talks, etc. or adapted equivalents).
4. **Inline interview excerpts** — appear as pull quotes within chapters where organizer experience grounds a recommendation.
5. **Desktop side TOC** — persistent on wide screens; quiet typographic list of chapter names, tracks scroll position.

### Conference Guide `/conferences/` (placeholder)

1. **Guide title** — "Running Ruby Conferences"
2. **Status statement** — a short honest note that this guide is being developed from organizer interviews and community experience.
3. **Brief scope preview** — one short paragraph describing what the guide will cover when ready.
4. **Link back** — quiet link back to the meetup guide or home.

## User Flows

### Reading the meetup guide (primary flow)

1. User lands on `/` via a link from rubyevents.org, search, or a community share.
2. User reads the purpose statement and understands this is a practical guide for Ruby organizers.
3. User clicks the Meetups link (nav or homepage link).
4. User arrives at `/meetups/`. On desktop, they see the guide text and the side TOC. On mobile, they see the inline contents.
5. User reads through the guide, possibly jumping to a specific chapter via the TOC.
6. Inline interview excerpts appear in the flow; user reads them as grounding voices, not as interruptions.
7. User finishes the guide. No required next step; the site does not push a conversion.

### Discovering the conference guide

1. User arrives on `/` or is in the nav and sees Conferences.
2. User clicks; arrives at `/conferences/`.
3. User reads the status note and scope preview, understands the guide is coming.
4. User optionally follows the link back to the meetup guide or home.

### Arriving directly on a guide page

1. User lands directly on `/meetups/` via a shared link or search result.
2. User orients themselves via the guide title and intro paragraph.
3. On desktop, the side TOC is immediately visible. On mobile, the inline contents is near the top.
4. User jumps to the chapter they need or reads from the start.

## Naming Conventions

| Concept                      | Label in UI                            | Notes                                                            |
| ---------------------------- | -------------------------------------- | ---------------------------------------------------------------- |
| The whole site               | Ruby Community Guides                  | Used in site title and nav title                                 |
| A guide track                | Guide (Meetup Guide, Conference Guide) | Not "handbook", "resource", or "track"                           |
| Homepage guide links         | Meetups / Conferences                  | Short, consistent with nav labels                                |
| Organizer interview snippets | Not labelled in UI                     | Appear as attributed quotes inline                               |
| People who gave interviews   | Organizers / Voices                    | Credibility section on homepage                                  |
| In-page navigation           | Contents (mobile) / side TOC (desktop) | No "Table of Contents" heading needed; chapters are self-evident |
| Named guide sections         | Chapters                               | Called chapters internally; displayed as plain headings in HTML  |

## Component Reuse Map

| Component               | Used on                                               | Behavior differences                                                                                           |
| ----------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `_layouts/default.html` | All pages                                             | Base layout: nav, main content, minimal footer. Used directly on homepage and conference placeholder.          |
| `_layouts/guide.html`   | Guide pages (`/meetups/`, `/conferences/` when ready) | Extends default; adds two-column structure for side TOC on desktop. Mobile collapses to single column.         |
| `_includes/quote.html`  | Inside guide content                                  | Reusable inline interview excerpt component. Takes quote text and attribution as parameters.                   |
| Primary nav             | All pages                                             | Same on every page. No active-state suppression needed given the small nav.                                    |
| Side TOC                | Desktop guide pages only                              | Either JS scroll-driven or CSS `position: sticky` column. Content is a duplicate of the guide's `h2` headings. |

## Content Growth Plan

The site is intentionally small and stable. Growth areas:

- **Meetup guide depth**: Individual chapters may grow in prose over time. Single-page format accommodates this without structural change.
- **Conference guide**: When the conference guide is ready, the placeholder page becomes a full guide page following the same layout as `/meetups/`. No new layouts or routing patterns needed.
- **Voices section**: Additional organizer names can be added to the homepage section as more interviews are conducted.
- **Additional guides**: If a third guide is ever added (e.g., Running Ruby Camps), it follows the same pattern — a new top-level directory, a guide layout, and a primary nav addition. The design system should not need to change.

No pagination, search, filtering, or archive patterns are needed at this scale.

## URL Strategy

- Pattern: `/<guide-name>/` — flat, one level deep for all guides.
- Dynamic segments: none. This is a static Jekyll site.
- Query parameters: none.
- Anchor links: guide chapters are reachable via `#chapter-slug` anchor, generated from heading IDs in Markdown. TOC links use these anchors.
- The conference guide placeholder lives at `/conferences/index.md`, matching the meetup pattern at `/meetups/index.md`.

## Jekyll File Structure

```
index.md                   ← Homepage
meetups/
  index.md                 ← Meetup guide (single long page)
conferences/
  index.md                 ← Conference guide placeholder
_layouts/
  default.html             ← Base layout (nav, content, footer)
  guide.html               ← Guide layout extending default (adds side TOC column)
_includes/
  quote.html               ← Reusable interview excerpt component
_sass/
  theme.scss               ← Design tokens (colors, type, spacing)
  base.scss                ← Global HTML element styles
  components.scss          ← Nav, quote, TOC, voices section
  media.scss               ← Dark mode and responsive overrides
  utilities.scss           ← Helper classes
interviews/                ← Source material only, excluded from Jekyll build
```
