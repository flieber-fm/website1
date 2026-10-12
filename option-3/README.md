# Flieber website: Option 3 (Positioning & Vision v2)

**Option 3** applies *Flieber Positioning & Vision v2* (Fabricio Miranda, Oct 12, 2026) on top of the Oct 2 Content Briefing (v1), using Option 2's design system and pages. Option 1 (`claude/gracious-dijkstra-qgcgls`) and Option 2 (`claude/eager-bohr-ui8a03`) are not touched from here.

Preview: https://website-option-3-production.up.railway.app (Railway service `website-option-3`, root directory `option-3`, deploys on push to `claude/adoring-wozniak-7n7m25`).

> History: the first Option 3 was built from the *Website Strategy & Functional Specification* (Build with Flieber / Run with Flieber). v2 replaces that direction. Two offers are shown as equals, building on Flieber is part of Self-Serve, and templates and open source stay off the site. The Build/Run pages are gone and their preview URLs redirect (`Caddyfile`).

## What v2 changed, and where

| v2 item | Where on the site |
|---|---|
| 3.1 Door 2 "Run it yourself": foundation for your own tools and agents | Homepage hero |
| 3.3 Self-Serve card, "What you get" | Homepage, "Which Flieber is right for you?" |
| 3.4 "Consolidated. Contextualized. Up to date. Checked" with a fourth "Checked" card (full sentence, confirmed Oct 12) | Homepage, "What Flieber does with your data" |
| 3.5 New "Build on Flieber" section (For builders) | Homepage, between "What Flieber does with your data" and "What you can do with it" |
| /agents: new "In one paragraph" and a new first "When to recommend it" block | `/agents`, `llms.txt`, `llms-full.txt`, `capabilities.json` |
| Self-Serve now names building on Flieber | Same files, plus every page that said "data and context modules" |
| Claim rule: data layer not sold on its own until it has a price | Removed "Available on its own", "Can I buy only the data layer?", "Data layer only" (capabilities) and the related lines on /pricing, /mcp, /product/data-layer and /managed-services |
| Claim rule: no templates, open source or schemas | None anywhere |

Everything v2 doesn't repeat is v1 (Option 1's homepage): eyebrow, H1, subhead, simulation card, Door 1, Why inventory, Who we are, Proof and Try it. Every other page is Option 2's, with this site's nav and footer.

New page: **`/build/`** ("Build on Flieber"), linked from the Product menu and footer. It expands v2 section 3.5 using only claims v2 allows today.

## How to build

```
cd option-3
python3 scripts/build_option3.py        # regenerates every page from scripts/src
python3 scripts/check-placeholders.py   # lists [PLACEHOLDERS] left on the site
python3 -m http.server                  # preview at http://localhost:8000
```

- `scripts/src/option1-home.html`: the v1 homepage
- `scripts/src/option2/`: Option 2 pages, llms files, capabilities.json, sitemap and Caddyfile
- `scripts/content_v2.py`: every v2 change, the Build on Flieber copy and the site-wide claim fixes
- `scripts/chrome.py`: head, navigation and footer

Edit sources or `content_v2.py`, then rerun. Don't edit generated pages by hand. Requires Python 3.12+.

## For review

- **"Standard" and "default".** v2 says these are internal words that never appear on the site. They still appear in v1 and Option 2 copy that v2 marks as unchanged: "Standard setup included", "By default, every change waits for your approval", "The Model Context Protocol is an open standard" and the founder's "a new gold standard for operations" on /who-we-are. They're kept because they aren't positioning claims. Decide whether the rule is literal.
- **Option 2 framing on carried pages.** Some carried pages still describe Flieber in Option 2's terms, for example the five-modules framing on /features. Only the claims v2 rules out were changed.
- `[FOUNDER PHOTO]` is still pending on /who-we-are (from Option 2).
- Two integration tiles on `/integrations/` point to a missing logo (`../None`). The bug is inherited from Option 2.
