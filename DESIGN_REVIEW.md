# Design Review — Mobile Sticky Guide Header

## Screenshots captured

- `screenshots/review-meetups-mobile-top-375.png`
- `screenshots/review-meetups-mobile-sticky-closed-375.png`
- `screenshots/review-meetups-mobile-sticky-open-375.png`
- `screenshots/review-meetups-tablet-768.png`
- `screenshots/review-meetups-desktop-1280.png`

## Result

Pass. The sticky header appears only on mobile after scrolling, preserves the editorial style, and the burger menu exposes both guide-switching links and the page TOC.

## Checks

- Visual hierarchy: header is compact and visible without overpowering the article.
- Responsive behavior: hidden at 768px/tablet and desktop; active at 375px mobile.
- Interaction states: menu opens/closes, link clicks close it, Escape/outside click close it.
- Accessibility: uses a real button with `aria-expanded`/`aria-controls`; menu links remain semantic navigation.
- Motion: respects `prefers-reduced-motion`.

## Notes

No must-fix issues found in the captured states.
