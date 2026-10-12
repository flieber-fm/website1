# Flieber website (Phase 1)

Static site implementing Phase 1 of *Flieber Website Strategy & Functional Specification* (working draft 1.0, 12 Oct 2026). Plain HTML/CSS/JS with no build step. Host the `flieber/` folder on any static host.

| Route | Page |
|---|---|
| `/` | Homepage: vision-first, with Build and Run path cards above the fold |
| `/build/` | Build overview (the four layers, templates, validation and services are anchors on this page) |
| `/run/` | Run overview |
| `/run/forecasting/`, `/run/inventory/`, `/run/replenishment/`, `/run/workflows/` | Run application pages (§9.2 template) |
| `/about/` | About / proof |
| `/contact/` | Contact / demo intake |

Shared files: `assets/site.css` and `assets/site.js`. The visual language matches the root `index.html` (dark, DM Sans + Instrument Serif). Build uses a periwinkle accent, Run uses green, and a path bar on Build/Run pages shows the current journey with a one-click switch (§12).

## Before publishing: claims to verify

Add `?verify` to any URL (e.g. `/run/?verify`) to outline every unverified claim on the page.

| Claim | Where | Spec ref |
|---|---|---|
| "7 years of inventory planning experience" | Home, Run, About proof strips | §4, §19 P0 |
| "1,000+ brands served" | Home, Run, About proof strips | §4, §19 P0 |
| Template names, "In preparation" status, "open source (license to be confirmed)" | `/build/#templates` | §2, §19 P0/P1 |
| Illustrative inventory record schema | `/build/` bring-your-own-data | §8.2 |
| Self-serve / assisted / Flieber-led service descriptions | `/build/#services` | §5.1, §19 P1 |
| API / docs / MCP FAQ answer | `/build/` FAQ | §11, §18 |

All product UI on the site is HTML/CSS mockups labeled "Illustrative". §12 asks for genuine product imagery, so replace them with verified screenshots when available.

## Lead capture

All forms (`form[data-lead]`) POST JSON to the same Google Apps Script endpoint as the root `index.html` (`LEAD_ENDPOINT` in `assets/site.js`). Fields sent:

`email, company, role, path (run|build|unsure), intent (demo|expert|customization), requested (original CTA intent, e.g. walkthrough/templates), useCase, channels, systems, timeframe, message, originPage, submittedAt, source`

**The Apps Script must be updated to store these fields.** The existing script may only save `email`. Requests use `no-cors`, so the page cannot detect server-side failures.

CTAs deep-link into the contact form with `?intent=…&path=…&app=…`, which pre-selects the matching options.

## Analytics

Clicks on elements with `data-track` push events to `window.dataLayer` (journey selection, path switches, cross-journey links, app cards, CTAs, lead submits). This does nothing until a tag manager is added (§15, §16).

## Deliberate deviations from the spec

- **Nav omits Solutions, Developers and Pricing.** Those are Phase 2/3 pages, and §14 says not to publish pricing until it is approved. Add them back when the pages exist.
- **Build hero secondary CTA is "Talk to an expert", not "View developer docs".** No docs exist yet (§18: describe agent/API features only at their actual release status).
- **Build sub-pages (`/build/data`, etc.) are anchors on `/build/`** until Phase 2 content exists.
- No canonical URLs or sitemap yet, because the production domain is not known.
