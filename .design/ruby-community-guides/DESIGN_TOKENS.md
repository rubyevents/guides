# Design Tokens: Ruby Community Guides

**Philosophy**: Literary/editorial field guide with technical restraint  
**Stack**: Jekyll + plain SCSS, CSS custom properties  
**Source file**: `_sass/theme.scss` (light mode), `_sass/media.scss` (dark mode)

## Typography

| Token                   | Value                       | Use                                 |
| ----------------------- | --------------------------- | ----------------------------------- |
| `--font-display`        | Nunito                      | Headings — matches RubyEvents h1/h2 |
| `--font-body`           | InterVariable / Inter       | Body text — matches RubyEvents base |
| `--font-mono`           | Space Mono                  | Code — self-hosted asset            |
| `--font-size-md`        | clamp(1rem → 1.125rem)      | Prose body                          |
| `--font-size-lg`        | clamp(1.125rem → 1.3125rem) | Lead/intro paragraphs               |
| `--font-size-2xl`       | clamp(1.5rem → 1.875rem)    | Chapter headings (h2)               |
| `--font-size-3xl`       | clamp(1.875rem → 2.5rem)    | Page title (h1)                     |
| `--line-height-relaxed` | 1.75                        | Prose — long-form reading           |
| `--max-width-prose`     | 70ch                        | Reading line length                 |

## Colors

| Token                     | Light                      | Dark                     | Use                         |
| ------------------------- | -------------------------- | ------------------------ | --------------------------- |
| `--color-bg`              | warm-50 (linen near-white) | warm-900 (warm charcoal) | Page background             |
| `--color-text`            | warm-900                   | warm-50                  | Body text                   |
| `--color-text-secondary`  | warm-600                   | warm-300                 | Captions, secondary prose   |
| `--color-link`            | warm-850                   | warm-200                 | Default link — near-black   |
| `--color-link-hover`      | ruby-500 (#DC143C)         | ruby-300                 | Hover — crimson appears     |
| `--color-accent`          | ruby-500                   | ruby-300                 | Nav title, strong emphasis  |
| `--color-quote-border`    | ruby-500                   | ruby-400                 | Interview quote left border |
| `--color-quote-bg`        | warm-100                   | warm-850                 | Interview quote background  |
| `--color-toc-text`        | warm-500                   | warm-400                 | TOC chapter links           |
| `--color-toc-text-active` | warm-900                   | warm-50                  | Active/current chapter      |
| `--color-toc-marker`      | ruby-500                   | ruby-400                 | Active chapter indicator    |

Tip callouts ("field notes") carry no dedicated colour tokens. They are
unfilled, ruled asides led by an uppercase rubric, reusing the warm + ruby
system: the `Ideas` rubric uses `--color-accent` (ruby); the `Tools` rubric
uses `--color-text-secondary` (neutral). Body copy is `--color-text`. This
keeps them in the page's two-temperature palette instead of introducing a cold
admonition box.

## Spacing

8px base, editorial scale. Key values:

| Token       | Value         | Typical use                          |
| ----------- | ------------- | ------------------------------------ |
| `--space-4` | 1rem / 16px   | Base unit, inline gaps               |
| `--space-5` | 1.5rem / 24px | Paragraph spacing, component padding |
| `--space-6` | 2rem / 32px   | Section gaps, nav padding            |
| `--space-7` | 3rem / 48px   | Between chapters                     |
| `--space-8` | 4rem / 64px   | Major section breaks, TOC gap        |
| `--space-9` | 6rem / 96px   | Top-of-page breathing room           |

## Layout

| Token                 | Value | Use                            |
| --------------------- | ----- | ------------------------------ |
| `--max-width-prose`   | 70ch  | Comfortable reading column     |
| `--max-width-content` | 72rem | Full layout including side TOC |
| `--toc-width`         | 14rem | Desktop side TOC column        |
| `--toc-gap`           | 4rem  | Space between TOC and prose    |

## Font loading

Inter and Nunito are loaded from Google Fonts in `_layouts/default.html`. For production, consider self-hosting both files alongside the existing `SpaceMono.woff2`.

```html
<link
  href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Nunito:wght@600;700;800&display=swap"
  rel="stylesheet"
/>
```
