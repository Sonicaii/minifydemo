# lightningcss Property Order Bug

This repository demonstrates a bug in **lightningcss** where vendor-prefixed CSS properties are incorrectly removed if they appear after the standard property.

**Bug Report:** https://github.com/parcel-bundler/lightningcss/issues/695

## Issue

When lightningcss processes CSS with both a standard property and its vendor-prefixed equivalent, it removes the unprefixed version if it appears first:

```css
/* This gets broken by lightningcss */
backdrop-filter: blur(8px);
-webkit-backdrop-filter: blur(8px);
```

## Fix

Put the vendor-prefixed property **before** the standard property:

```css
/* This works correctly */
-webkit-backdrop-filter: blur(8px);
backdrop-filter: blur(8px);
```

## Demo
Using https://github.com/adamchainz/django-minify-html which uses lightningcss

Live demo: https://sonicaii.pythonanywhere.com/
- `/` - Minified version (using lightningcss via django-minify-html)
- `/unminified/` - Unminified version

This is intentionally broken on non-webkit browsers.
Both should work identically since the CSS is in the correct order.
