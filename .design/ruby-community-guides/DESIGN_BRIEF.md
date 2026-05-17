# Design Brief: Ruby Community Guides

## Problem

Ruby organizers often want to start or sustain local community work, but the available knowledge is scattered across personal experience, private conversations, conference hallways, and isolated blog posts. A potential organizer may not need a product, a checklist app, or a promotional landing page; they need a trustworthy field guide that makes organizing feel possible and grounded in real community experience.

The current site is a small Jekyll prototype with a homepage, a meetup guide outline, and interview transcripts. It needs a coherent site experience and visual identity that can support long-form guide reading while still feeling connected to RubyEvents.

## Solution

Ruby Community Guides will become a quiet, editorial subdomain of RubyEvents with two first-class guide tracks: Running Ruby Meetups and Running Ruby Conferences. The site will initially build out the meetup guide and include a lightweight conference placeholder, while designing the navigation and visual system to support both tracks equally.

The experience should feel like a durable digital book or field guide: text-led, calm, credible, and authored. The homepage explains what the project is, routes readers to the two guide tracks through prominent text links, and establishes credibility through the organizers whose interviews informed the work. Guide pages are long-form narrative pages with named chapters, a persistent desktop table of contents, mobile-friendly contents, and subtle inline interview snippets that ground recommendations in lived experience.

## Experience Principles

1. **Editorial trust over product polish** -- The design should feel authored and useful, not like startup marketing, a docs portal, a Notion wiki, or an event brand campaign.
2. **Continuity with RubyEvents over visual independence** -- The guides should match RubyEvents colors and typography closely enough to feel like a subdomain, while adapting spacing, hierarchy, and layout for long-form reading.
3. **Narrative guidance over checklist UI** -- The guide should remain prose-led and chapter-based. Practicality comes from examples, structure, and embedded voices, not checklist blocks, cards, or decision prompts.

## Aesthetic Direction

- **Philosophy**: Literary/editorial field guide with technical restraint, adapted from the RubyEvents visual language.
- **Tone**: Calm, credible, warm, community-rooted, durable.
- **Reference points**: RubyEvents visual identity; Evil Martians' meetup article for concise named sections and experience-backed prose; the Staff Engineer book for long-form technical community writing that feels book-like rather than app-like.
- **Anti-references**: Startup marketing pages, generic documentation portals, Notion-style knowledge bases, heavy conference/event branding, decorative Ruby-gem theming, card-heavy SaaS layouts.

## Existing Patterns

The current guide site is intentionally minimal and should stay simple, but its current visual foundation will be replaced or substantially reworked.

- Typography: Current site uses local Rubik and Space Mono. RubyEvents uses Inter for body text and Nunito as a serif-like display family via Tailwind config (`fontFamily.sans: Inter`, `fontFamily.serif: Nunito`) and imports Nunito in `components/typography.css`. The guides should move toward the RubyEvents type direction while tuning sizes, line length, and rhythm for long-form prose.
- Colors: Current guide site has gray/info/warning/error CSS custom properties. RubyEvents' DaisyUI theme uses primary `#DC143C`, secondary `#7A4EC2`, accent `#1DA1F2`, neutral `#261B23`, and base `#F8F9FA`. The guides should derive their token system from these colors, with a warmer page/background and quieter long-form accents where needed.
- Spacing: Current guide site has CSS custom spacing variables in `_sass/theme.scss`. RubyEvents uses Tailwind spacing, but this Jekyll site should keep plain SCSS/CSS variables. Tokens should define a prose-friendly vertical rhythm and wider layout for side navigation.
- Components: Current site has a default layout, nav, homepage hero, and basic content styling. RubyEvents has many Rails/Tailwind components, but they should be treated as visual reference rather than imported structure. This Jekyll site should keep layouts and data files minimal.

## Component Inventory

| Component | Status | Notes |
| --------- | ------ | ----- |
| Global site layout | Modify | Update `_layouts/default.html` for RubyEvents-aligned nav, primary links, and long-form content support. |
| Homepage intro | Modify | Text-led explanation of the guides with no card grid. |
| Guide track links | New | Prominent typographic links for Meetups and Conferences, equal in hierarchy. |
| Voices/credibility section | New | Homepage section listing interviewees/organizers whose experience informed the guides; not full interview navigation. |
| Guide layout | New | Single long-form guide layout with readable prose column and optional desktop side TOC. |
| Desktop table of contents | New | Persistent, quiet side navigation for guide chapters. |
| Mobile contents | New | Simple top-of-page contents; no app-like behavior required. |
| Inline interview quote | New | Subtle pull quote/excerpt with attribution, embedded inside prose. |
| Conference placeholder page | New | Lightweight page that preserves the second guide track without pretending full content exists. |
| Design tokens | Modify/New | Replace current theme variables with RubyEvents-aligned tokens adapted for reading. |
| Primary navigation | Modify | Only Meetups and Conferences as primary nav items. |

## Key Interactions

- A reader lands on the homepage, understands that these are practical Ruby community guides informed by organizer experience, and chooses between Meetups and Conferences using prominent text links.
- A reader opens the meetup guide and reads it as a long-form narrative. On desktop, the side TOC keeps them oriented and lets them jump between named chapters. On mobile, a simple contents section appears near the top.
- Interview excerpts appear inline as evidence or perspective, with restrained styling and clear attribution. They should support the reading flow rather than interrupt it as promotional cards.
- The conference link leads to a lightweight placeholder page that explains the guide is planned/developing, maintaining equal navigation presence without overpromising.

## Responsive Behavior

- Mobile: single-column reading layout, top contents list, generous line height, navigation that remains simple and non-sticky unless the implementation stays unobtrusive.
- Tablet: single or gently widened prose layout; contents may remain inline unless there is enough room for a side rail.
- Desktop: centered reading area with a persistent side TOC. The prose line length should stay comfortable; the layout may use margins/side rails for orientation and quotes rather than expanding paragraphs too wide.
- The homepage should remain text-first at all sizes; guide track links can stack on mobile and sit in a balanced typographic arrangement on wider screens.

## Accessibility Requirements

- Text contrast should meet WCAG AA for body text and links; Ruby red accents must not be the only indicator of interaction.
- Links need visible focus states and clear hover/focus affordances.
- The side TOC must be keyboard accessible and should not trap focus or obscure content.
- Heading hierarchy should remain semantic and support screen-reader navigation.
- Inline quotes should use semantic blockquote/cite patterns where possible.
- Respect reduced-motion preferences; no essential animated interactions.
- Maintain readable line length and scalable typography for long-form reading.

## Out of Scope

- Publishing full interview pages as a primary site feature.
- Building a full conference guide beyond a lightweight placeholder page.
- Adding search, filtering, user accounts, comments, CMS workflows, or JavaScript-heavy navigation.
- Importing RubyEvents' Rails/Tailwind component system into this Jekyll site.
- Creating checklist components, decision prompt widgets, or app-like task flows.
- Running the design review phase before pages are built.
