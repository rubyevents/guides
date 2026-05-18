# Design Review — Mobile Sticky Guide Header

Reviewed against: `.design/ruby-community-guides/DESIGN_BRIEF.md`  
Date: 2026-05-18

## Screenshots captured

Saved under `.design/ruby-community-guides/screenshots/`:

- `review-meetups-desktop-1280-before.png`
- `review-meetups-tablet-768-before.png`
- `review-meetups-mobile-top-375-before.png`
- `review-meetups-mobile-sticky-closed-375-before.png`
- `review-meetups-mobile-sticky-open-375-before.png`
- `review-meetups-desktop-1280-after.png`
- `review-meetups-tablet-768-after.png`
- `review-meetups-mobile-top-375-after.png`
- `review-meetups-mobile-sticky-closed-375-after.png`
- `review-meetups-mobile-sticky-open-375-after.png`

## Result

Fixed. The sticky header/menu still works on mobile, but now uses the site’s editorial language: quiet borders, lighter radius/shadow, typographic guide links, clearer outer spacing, and a “Contents” label instead of a generic “Menu.”

## Changes made

- Replaced the duplicate semantic `<header>` with a neutral sticky container in `_layouts/default.html`.
- Renamed the toggle label from “Menu” to “Contents.”
- Restyled the sticky header in `_sass/components.scss` and `_sass/media.scss` to remove the app-like nested card/pill treatment.
- Added an expanded close-icon state and reduced-motion handling.

## Remaining notes

No must-fix issues remain for the reviewed states.
