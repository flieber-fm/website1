# Flieber website

Static site for flieber.com. All copy comes from the **Flieber Website Brief (October 1, 2026)**, the source of truth for every word on the site. Logo, type and color follow the **Flieber Brand Guidelines v1.0**.

No build step. Any static host (Netlify, Vercel, Cloudflare Pages, GitHub Pages, S3) can serve it as is, or HubSpot CMS can (hosting is still an open decision; see below).

```
index.html                 Homepage (7 sections + footer)
agents/index.html          /agents: plain facts for AI agents, text-first, no animation
pricing/index.html         /pricing: the two offers, how pricing works, what's included, FAQ
llms.txt                   Generated from /agents (llms.txt convention)
capabilities.json          Generated from /agents (schema from brief §5)
sitemap.xml                /, /agents, /pricing, /llms.txt, /capabilities.json
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

1. `<meta name="robots" content="noindex, nofollow">` in `index.html`, `agents/index.html` and `pricing/index.html`
2. `robots.txt` (replace it with `robots.production.txt`, after filling in the AI crawler policy)
3. The `X-Robots-Tag` header in `Caddyfile`

## Open items before launch (brief §8)

Blocking launch:

- [ ] MCP endpoint URL, auth method and docs URL (`[MCP ENDPOINT URL]`, `[AUTH METHOD]`, `[DOCS URL]`)
- [ ] Hosting: build the pages in HubSpot CMS (Fabricio's preference, Oct 1). Needs the HubSpot connector reconnected with website-page write access; see "HubSpot changes" below

Before launch:

- [ ] Post-launch: encryption details from engineering (row removed from /security, /agents and llms.txt until then)
- [ ] Optional: official accuracy report from Nixtla. Until then the claim reads "36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model" (approved Oct 1). Never "third-party verified": Nixtla co-built the model
- [ ] Post-launch: MCP endpoint and auth method, if engineering wants them public. Until then the site points customers to https://app.flieber.com/app/developers
- [ ] Source for the four results in "Who we are" (+38% sales, -62% stockouts, -17% excess inventory, -88% time on replenishment; "average across customers using Flieber for 12+ months"): keep the method on file, since agents and buyers will quote these

## /pricing (Oct 1)

Structure follows the live flieber.com/pricing (hero, how pricing works, what you get, FAQ, closing CTA); plans, prices and terms follow the brief, because the live page publishes no prices ("we share your price on the demo call"). Pending Fabricio's confirmation:

- [ ] "From $149/month": the legacy flieber.com/pricing-plans calculator starts at $299/month (Essentials, tier 1; $209 with a 30% intro discount), with Essentials/Pro/Max tiers and an annual option
- [ ] Price drivers: the brief says sales, channels and warehouses; the live page says sales volume, channels and SKU count
- [ ] "14-day free trial, no credit card required" (from the live page; the brief only says "free trial")
- Not carried over on purpose: the live page's stats band (4.7 on G2, 3M+ SKUs, 50K+ POs/yr, "500+ brands", year-one results incl. "88% less time forecasting", "40 min to set up") and its testimonials. Results stay homepage-only, and "500+ brands" and the setup times conflict with the homepage and other live pages

Decided Oct 1 (Fabricio):

- Managed Services everywhere: planners join the team, participate in S&OP meetings to get full context, keep Flieber updated and *help* run the planning practice (not "run" it)
- Forecasting is described as AI forecasting with anomaly correction (homepage, /agents, llms.txt, capabilities.json, /pricing)
- Integrations on /pricing mirror flieber.com/integrations (native vs assisted, with data types). Native: one click, available in the free trial. Assisted: set up by Flieber's team, included on a paid plan, not during the trial. SPS Commerce added (new, assisted; covers any data the account can access, mostly wholesale PO history and new POs as allocated stock). Flieber works as an MCP client today

Decided Oct 1 (Fabricio), CTAs and links:

- Button labels: "Book a demo" (https://www.flieber.com/book-a-demo) and "Start free trial" (https://www.flieber.com/free-trial), both existing HubSpot pages with CRM forms. "Talk to a planner" and "Get started" are gone. Log in: https://app.flieber.com
- No sandbox yet: removed from the homepage, /agents, llms.txt and capabilities.json. The homepage "Try it" dark card now shows the MCP endpoint
- Blog and Privacy link to the live HubSpot pages
- Headings never end with a period

Decided Oct 1 (Fabricio), round 2:

- No prices on the site, so pricing can vary by customer: Self-Serve is "priced to your operation" (features enabled and data volume), Managed Services "quoted per brand". Terms stay: monthly contracts, free trial, standard setup included
- Canonical domain is https://www.flieber.com
- /security (AWS US; Admin and Member roles; Google and Microsoft SSO; AI providers incl. Anthropic, OpenAI, xAI, no training on customer data; deletion per Privacy Policy and Service Agreement; no compliance claims) and /contact (hello@flieber.com) added. Footer adds Service agreement
- Push to ERP: NetSuite, plus light ERPs such as Cin7 and Brightpearl
- AI crawlers are allowed (robots.production.txt)
- Customer quotes approved; Fabricio owns the "100+ brands" figure; the four results are documented in a spreadsheet

## HubSpot changes

The live site, book-a-demo, free trial and blog run on HubSpot (portal 5767502, www.flieber.com).

- [ ] Build the new pages as HubSpot website pages from this repo (/, /agents, /pricing, /security, /contact), published at cutover only
- [ ] Build the HubSpot drafts: needs api.hubapi.com allowed in the environment's network settings and a HubSpot private app or personal access key (Design Manager and File Manager write) stored as the environment variable HUBSPOT_ACCESS_KEY; then `npx @hubspot/cli` uploads hubspot/build/ templates and the assets to File Manager folder flieber-2026
- [ ] Follow `hubspot/CUTOVER.md` (unpublish, never delete, old pages; publish new ones; import `hubspot/url-redirects.csv`; upload llms.txt and capabilities.json; robots.txt)
- [ ] Restyle the book-a-demo page (header, footer, copy) to the new site; keep the form and CRM scripts
- [ ] Free-trial page: "Integrate any system or spreadsheet" contradicts the new rule (assisted integrations only on paid plans)
- [ ] Blog footer: address says NY 10017; correct is 10016
- [ ] Restyle the blog header and footer to the new site

## Analytics

Google Tag Manager (`GTM-5FS8NPG`) and HubSpot tracking (portal `5767502`, the "Flieber" HubSpot account) load only when the hostname is flieber.com, so preview traffic stays out of analytics. Confirm that 5767502 is the portal the current site uses. No forms exist yet; route any form to HubSpot.

## Brand rules applied

- **Type:** Open Sauce One. Headings Regular at 110% line height and about -4% tracking; subheads SemiBold at -3%; body Regular. Example prompts, labels and data use the system mono font.
- **Color:** Yellow `#F5ED61` is the primary color and is only used as a background, highlight or button fill, never for text on a light background. Type is Black `#1B1C1C` on white and gray backgrounds. Small muted text uses `#5C6568` (and `#A3AEB1` on black) so every text pairing meets WCAG AA 4.5:1. Blue `#244AE3` appears once, on the forecast-accuracy stat.
- **Logo:** the wordmark is always paired with the icon and never shown under 100px wide.

## Notes

- **Copy rules (brief §0):** no em dashes in site copy, sentence-case headings, no serial comma. Short section labels above some H2s use the brief's own section names.
- **Hero card:** a dark "Decision simulation" card that rotates through six sample scenarios (wholesale order, promotion, influencer campaign, ad campaign, purchase order, warehouse transfer), about 8 seconds each. It pauses on hover, keyboard focus or when off screen, has a pause button, and does not autoplay for visitors who prefer reduced motion. All numbers are illustrative sample data, no customer data. Edit the scenarios in `index.html` (`.sim-panel`); keep every panel to four metric rows so the card height stays fixed.
- **Logo strip:** 14 logos matching the live homepage (white PNGs, rendered black with a CSS filter). Near-square logos use `logo-square` and very wide ones `logo-thin`.
- **Docs in the top nav:** removed until the MCP/API documentation exists (decided Oct 1). It stays reachable as "MCP docs" in the footer. When the docs go live, add it back to the nav, ideally labeled "Developers" or "API docs".
- **Keep /agents, llms.txt and capabilities.json in sync.** The two files are generated by hand from /agents and must never contradict it. Update `last_updated` and the /agents date together.
- **Cache busting:** CSS and JS are linked with `?v=N`. Bump it when you change either file.
- **Lighthouse (mobile, Oct 1):** Performance 98, Accessibility 100, Best practices 100 on both pages. SEO scores 69 only because of the preview no-index; it clears at launch.
