# Flieber website

Static site for flieber.com. All copy comes from the **Flieber Website Brief (October 1, 2026)**, the source of truth for every word on the site. Logo, type and color follow the **Flieber Brand Guidelines v1.0**.

No build step. Any static host (Netlify, Vercel, Cloudflare Pages, GitHub Pages, S3) can serve it as is, or HubSpot CMS can (hosting is still an open decision; see below).

```
index.html                 Homepage (7 sections + footer)
agents/index.html          /agents: plain facts for AI agents, text-first, no animation
llms.txt                   Generated from /agents (llms.txt convention)
capabilities.json          Generated from /agents (schema from brief §5)
sitemap.xml                /, /agents, /llms.txt, /capabilities.json
robots.txt                 PREVIEW: blocks all crawlers
robots.production.txt      Launch version: allows search engines, AI crawler policy pending
scripts/check-placeholders.py   Lists every placeholder still on the site
assets/css/site.css        All styles; brand tokens at the top
assets/js/site.js          Nav, scroll reveals, quote carousel, copy button, logo fallback
assets/fonts/              Open Sauce One 400/500/600 (SIL OFL, self-hosted)
assets/img/                Flieber logo (dark + light), icon, favicon
assets/logos/              Customer logos from the shared Drive logo folder
Dockerfile, Caddyfile      Static server for the Railway preview
```

Local preview: `python3 -m http.server` from the repo root, then open http://localhost:8000.

## Homepage structure (brief §3, plus "Who we are")

1. Hero, with a decision-simulation card on sample data (clearly labeled "Sample data")
2. Why inventory
3. Which Flieber is right for you? (`#which-flieber`): two equal cards, neither visually favored, then "Probably not for you if"
4. What Flieber does with your data (`#how-it-works`)
5. What you can do with it (example prompts in the mono font)
6. Who we are (`#who-we-are`, added Oct 1 at Fabricio's request; not in the brief): since 2019, 1,000+ brands, operators first, and the four customer results. Founders' other companies are deliberately not mentioned (agreement between the co-founders). The four results are homepage-only by decision (Oct 1): they are intentionally not on /agents, llms.txt or capabilities.json
7. Proof
8. Try it

## Decisions that differ from the brief

Confirmed with Fabricio on October 1, 2026:

- **Visual system:** the site stays on the Flieber Brand Guidelines (Open Sauce One, yellow and black) instead of the brief's §6 palette and fonts. The brief's "editorial and calm" direction is applied: no gradient washes, glows or pulsing effects.
- **Proof stat:** "tested on **a sample of** 46,000 products" (homepage, /agents, llms.txt, capabilities.json).
- **Logo strip label:** "Trusted by hundreds of brands" (the brief's "100+ brands run on Flieber today…" line is not used on the homepage; /agents keeps "100+ commerce brands today; more than 1,000 since 2019").

## Placeholders and launch checks

Every `[BRACKET]` from the brief is rendered visibly (dashed outline, class `todo`). Links whose destination is still a placeholder carry `data-placeholder="[...]"`: they stay on the page when clicked and show the pending placeholder on hover.

List everything that remains:

```
python3 scripts/check-placeholders.py           # list
python3 scripts/check-placeholders.py --strict  # exit 1 if anything remains (use before launch)
```

The check also reports the three preview-only no-index layers, which **must be removed at launch**:

1. `<meta name="robots" content="noindex, nofollow">` in `index.html` and `agents/index.html`
2. `robots.txt` (replace it with `robots.production.txt`, after filling in the AI crawler policy)
3. The `X-Robots-Tag` header in `Caddyfile`

## Open items before launch (brief §8)

Blocking launch:

- [ ] MCP endpoint URL, auth method and docs URL (`[MCP ENDPOINT URL]`, `[AUTH METHOD]`, `[DOCS URL]`)
- [ ] Build the sandbox (`[SANDBOX URL]`)
- [ ] Button destinations: `[BOOKING URL]`, `[SIGNUP URL]`, `[TRIAL URL]`, `[SANDBOX URL]`
- [ ] Hosting and CMS decision: HubSpot CMS or separate hosting, keeping HubSpot forms and tracking either way

Before launch:

- [ ] Nixtla report link (`[NIXTLA REPORT URL]`)
- [ ] Six security and hosting placeholders in /agents Data handling
- [ ] AI crawler policy for robots.txt (`[AI CRAWLER POLICY]` in `robots.production.txt`)
- [ ] Quoted customers: confirm all five are active and approve use of their quotes
- [ ] Contact email for the /agents hand-off (`[EMAIL]`)
- [ ] Owner for the "100+ brands" figure
- [ ] Blog, Contact and Privacy URLs for the footer (`[PLACEHOLDER: …]`), and check that `/pricing` and `/security` exist on the live site
- [ ] "Push to ERP" ERPs besides NetSuite (`[others]`)
- [ ] Source for the four results in "Who we are" (+38% sales, -62% stockouts, -17% excess inventory, -88% time on replenishment; "average across customers using Flieber for 12+ months"): keep the method on file, since agents and buyers will quote these

## Analytics

Google Tag Manager (`GTM-5FS8NPG`) and HubSpot tracking (portal `5767502`, the "Flieber" HubSpot account) load only when the hostname is flieber.com, so preview traffic stays out of analytics. Confirm that 5767502 is the portal the current site uses. No forms exist yet; route any form to HubSpot.

## Brand rules applied

- **Type:** Open Sauce One. Headings Regular at 110% line height and about -4% tracking; subheads SemiBold at -3%; body Regular. Example prompts, labels and data use the system mono font.
- **Color:** Yellow `#F5ED61` is the primary color and is only used as a background, highlight or button fill, never for text on a light background. Type is Black `#1B1C1C` on white and gray backgrounds. Small muted text uses `#5C6568` (and `#A3AEB1` on black) so every text pairing meets WCAG AA 4.5:1. Blue `#244AE3` appears once, on the forecast-accuracy stat.
- **Logo:** the wordmark is always paired with the icon and never shown under 100px wide.

## Notes

- **Copy rules (brief §0):** no em dashes in site copy, sentence-case headings, no serial comma. Short section labels above some H2s use the brief's own section names.
- **Hero card:** a dark "Decision simulation" card that rotates through four sample scenarios (wholesale order, promotion, influencer campaign, purchase order), about 8 seconds each. It pauses on hover, keyboard focus or when off screen, has a pause button, and does not autoplay for visitors who prefer reduced motion. All numbers are illustrative sample data, no customer data. Edit the scenarios in `index.html` (`.sim-panel`); keep every panel to four metric rows so the card height stays fixed.
- **Logo strip:** 14 logos matching the live homepage (white PNGs, rendered black with a CSS filter). Near-square logos use `logo-square` and very wide ones `logo-thin`.
- **Docs in the top nav:** removed until the MCP/API documentation exists (decided Oct 1). It stays reachable as "MCP docs" in the footer. When the docs go live, add it back to the nav, ideally labeled "Developers" or "API docs".
- **Keep /agents, llms.txt and capabilities.json in sync.** The two files are generated by hand from /agents and must never contradict it. Update `last_updated` and the /agents date together.
- **Cache busting:** CSS and JS are linked with `?v=N`. Bump it when you change either file.
- **Lighthouse (mobile, Oct 1):** Performance 98, Accessibility 100, Best practices 100 on both pages. SEO scores 69 only because of the preview no-index; it clears at launch.
