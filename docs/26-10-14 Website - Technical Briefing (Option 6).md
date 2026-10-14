# 26-10-14 Website - Technical Briefing (Option 6)

Oct 14, 2026 · @Fabricio Miranda

## Purpose and status

Option 6 is a new version of flieber.com, built for review next to Option 1 and Option 2. Its main direction is the 26-10-14 Flieber Website Development Brief (the "source brief", in `docs/`). Option 2 is used for structure, UI and approved claims wherever it does not conflict with the source brief. This brief is the technical companion to the Content Briefing (Option 6); the two stay in sync with each other and with the preview. Nothing in HubSpot is created, edited or published for Option 6.

| Where | What is there | State |
| --- | --- | --- |
| GitHub repo flieber-fm/website1, branch claude/option-6 | Option 6 source: the homepage, /security, CSS and JS | Current |
| Railway preview, service website-option-6 (website-option-6-production.up.railway.app) | Option 6 for review, hidden from search engines | Current |
| Branch claude/eager-bohr-ui8a03 and service website-option-2 | Option 2 | Untouched from this branch |
| Branch claude/gracious-dijkstra-qgcgls and its service | Option 1 | Untouched from this branch |
| HubSpot (portal 5767502) | Nothing for Option 6 | Untouched |

## How the two sources combine

Rule set by Fabricio on Oct 14: the source brief is the main direction; Option 2 is the structure and UI inspiration, and the main guideline wherever the two do not conflict. The documents are not merged.

| Topic | Source brief says | Option 2 has | Option 6 does |
| --- | --- | --- | --- |
| Site size | One focused homepage with anchor navigation, a contact or booking flow and privacy information; deeper pages only when real customer questions justify them | 37 pages plus llms.txt, llms-full.txt, capabilities.json and /agents | One homepage plus /security. Every other Option 2 page, the machine-readable files and the homepage variants are not part of Option 6 (they stay on the Option 2 branch) |
| Positioning | "Inventory planning built around your business"; first screen readable without AI knowledge; vibe coding secondary | "The inventory intelligence layer your agents run on", MCP-native | Source brief. Agents, MCP and AI tools appear only in "Build it with your own team", "Where AI helps" and the FAQ |
| Offers and pricing | One offer, three kinds of help; conversation-led; no packages, fixed fees or minimum commitments | Self-Serve and Managed Services (Lite and Full); 14-day free trial; "Priced to your operation" | Source brief. No plan names, no free trial, no Lite/Full. Pricing note: platform, tailoring and support priced separately, shared in the first conversation |
| Primary action | "Talk about your planning needs", the same throughout | Start free trial and Book a demo | Source brief. Book a demo stays only as the "Book a call" alternative next to the form |
| Navigation | How it works, Your options, Examples, Talk to us; keep customer sign-in accessible | Product and Solutions menus, Pricing, Who we are, /agents | Source brief, plus Log in |
| Design system, components, security wording, approved claims, logos, quotes | Use approved brand assets; only verified claims | Built and approved | Option 2 (no conflict) |
| Planners | Work alongside the team; never imply Flieber owns purchasing decisions | Sounding board, S&OP, keep data accurate, help run the planning practice; never "run it for you" | Both rules apply |

## Site map

| Page | Sections |
| --- | --- |
| / | Hero (concept planning view) · Logos · Sound familiar? (problems) · How it works (`#how-it-works`: foundation, annotated view, where AI helps, control) · Your options (`#options`) · Examples (`#examples`) · How an engagement works (`#how-we-work`) · Questions (`#questions`) · Proof (`#proof`) · Security (`#security`) · Talk to us (`#talk`, form) |
| /security | As in Option 2 (approved wording), with the Option 6 nav and footer |

Structured data on /: Organization, WebPage and FAQPage (the seven questions). No prices anywhere.

Kept live on HubSpot and linked: book-a-demo (the "Book a call" link), blog, privacy policy, service agreement. Help center and app.flieber.com (Log in) are linked as today.

## Build

- `index.html` is edited by hand. Its nav and footer come from `scripts/site_chrome.py`; run `python3 scripts/site_chrome.py` after changing either (it rewrites `index.html` and `security/index.html`).
- The FAQ appears twice in `index.html`: the visible `<details>` list and the FAQPage JSON-LD in the head. Change both together.
- Review banner: a dark bar above the nav on every page, "Review build · Option 6 · Oct 14 development brief on Option 2’s design" ("Option 6" in yellow), written by `scripts/site_chrome.py`. Preview only; remove before launch.
- Styles: `assets/css/site.css` (Option 2's file; Option 6 styles are appended in the "Option 6" block). Scripts: `assets/js/site.js` (Option 6 adds the form and analytics events). Cache busting: `site.css?v=50`, `site.js?v=18`; bump with sed across .html files on every CSS or JS change.
- Serving: Caddy (Dockerfile copies `index.html`, `robots.txt`, `sitemap.xml`, `security/` and `assets/`). No redirects yet.
- Search engines stay blocked: meta robots on both pages, `robots.txt` and the `X-Robots-Tag` header. `python3 scripts/check-placeholders.py` lists them.
- Removed from this branch (still on the Option 2 branch): every other page, llms.txt, llms-full.txt, capabilities.json, /home-variants, `assets/integrations/`, `hubspot/` and the Option 2 generators (`build-content.py`, `build-home-variants.py`, `build-hubspot.py`, `site_content.py`, `work_content.py`, `integ_content.py`).
- Checks before every push: serve with `python3 -m http.server 8765`; Playwright (`PW=$(npm root -g)/playwright`) at 1440, 1024, 800, 768 and 390px for horizontal overflow, JS errors and broken links and anchors; screenshot what changed.

## Lead capture and analytics

Form fields follow the source brief: name, work email, company, a short description of the planning problem, and an optional choice (tailoring a system, building with our own team, ongoing support, not sure yet). Visible validation with messages tied to each field (`aria-describedby`, `aria-invalid`), focus on the first error, a confirmation state that takes focus, a honeypot field against bots and a note asking not to send passwords or data files.

**Preview only:** the form sends nothing. A visible note says so on the form and on the confirmation. Connecting it (for example to a HubSpot form) is a HubSpot change and waits for Fabricio's go.

Analytics events are pushed to the GTM `dataLayer` (GTM loads only on flieber.com, so the preview sends nothing):

| Event | When | Fields |
| --- | --- | --- |
| `cta_click` | Any "Talk about your planning needs", "Talk to us" or "Book a call" click | `cta_location`: nav, hero, options, book |
| `form_start` | First input in the form | |
| `form_error` | Submit with missing or invalid fields | `fields` |
| `form_submit` | Valid submit | `service_interest`: tailor, build, support, unsure, none |

Scheduling completions are not tracked: the book-a-demo page lives on HubSpot.

## Claims used

Every claim comes from Option 2's "Approved facts and claims" table unless marked open.

| Claim on the page | Source |
| --- | --- |
| 14 customer logos, "Trusted by hundreds of brands" | Option 2, approved |
| "More than 1,000 commerce brands have planned with Flieber since 2019"; "Planning with commerce brands since 2019" | Option 2: "More than 1,000 commerce brands since 2019". The source brief asks to verify the count and wording; open item 3 |
| Customer results (+38%, -62%, -17%, -88%, 12+ months) | Option 2, homepage only, spreadsheet on file. The source brief asks for customer evidence; open item 3 |
| Accuracy stat (36%, 16 models, 46,000 products, Nixtla) | Option 2, approved |
| Five quotes and the G2 link | Option 2, approved |
| Native integrations (Amazon, Shopify, Walmart, TikTok Shop, eBay, Etsy, BigCommerce, Google Sheets); NetSuite, SPS Commerce, accounting systems, "more than 20" 3PL and warehouse systems set up by the team | Option 2 integrations table (23 3PL and warehouse systems) |
| "Proprietary algorithms, not language models, do the math" | Option 2 (still on its checklist for Fabricio's confirmation) |
| Approval rules; by default every change requires approval | Option 2, approved |
| API and MCP server; Claude, ChatGPT and Cursor connect | Option 2, approved |
| Planners: keep data accurate, S&OP, sounding board, carry out what is approved | Option 2 Managed Services (Full plan executes after approval) |
| "with dashboards that keep the work visible" | Source brief, Fabricio's direction; open item 2 |
| Security strip | Option 2, approved /security wording |
| The Flieber app as a ready-made starting point | Sold today as Self-Serve; open item 1 |
| What happens after the form (reply by email, first conversation, scope and pricing proposal) | Written for Option 6; open item 4 |

All product views (hero card, annotated view, three examples) are labeled "Concept · sample data" or "Illustration with sample data, not a product screenshot". No real screenshot is used yet.

## Open items

Raised in the source brief ("Resolve before public launch") or created by Option 6:

1. Confirm what is available today: the Flieber app as a ready-made starting point, how customers build on the API and MCP server, and how far tailoring goes (the source brief's "recommended boundary for customization").
2. Confirm the ongoing support scope as written on the card, including "dashboards that keep the work visible" and "our planners carry out what you approve".
3. Confirm the evidence: the 1,000+ brands wording and the four customer results under the source brief's stricter rule.
4. Confirm the process after the form (who replies, how, what the customer gets after the first conversation) and where leads go. Then connect the form (HubSpot change, needs the go) and add consent handling for analytics.
5. A real, annotated product screenshot for "How it works" (the source brief asks for a "verified product view"); the current view is an illustration.
6. Free trial: Option 2's 14-day free trial is not on Option 6 because the source brief is conversation-led. Decide whether it comes back as a secondary path.
7. Redirects: if Option 6 replaces the live site, decide where the live site's other URLs (/pricing, /features, /managed-services, /agencies and others) should go.
8. Editing copy without a rebuild (source brief): today copy is edited in `index.html`. HubSpot modules would solve it at the switch.

## Decision log

Newest first.

| Date | Decision |
| --- | --- |
| Oct 14 | Review banner on top of every page names the version under review: "Review build · Option 6 · Oct 14 development brief on Option 2’s design" (Fabricio: always add it). Preview only |
| Oct 14 | Railway service website-option-6 (2bd8097d-0023-4982-8d60-ffb12ad7ee8f) created for the preview at Fabricio's request, connected to claude/option-6 |
| Oct 14 | Option 6 built on branch claude/option-6 from Option 2 (commit f4408ac). The source brief is the main direction and Option 2 is the structure and UI guideline where they don't conflict (Fabricio). Built as one focused homepage plus /security, following the source brief's recommended first release; the other Option 2 pages, machine-readable files and homepage variants are not part of Option 6 |
| Oct 14 | Primary action "Talk about your planning needs" everywhere on the page, nav button "Talk to us", with "Book a call" (existing book-a-demo page) as the only alternative; no free trial and no plan names or prices (source brief, conversation-led pricing) |
| Oct 14 | The source brief's proposed copy is used with house-style fixes only where possible (no serial comma, no final period on headings); every change is listed in the Content Briefing (Option 6), section 3 |
| Oct 14 | Option 2's approved claims, logos, quotes, results, accuracy stat and security wording are reused; items the source brief asks to re-verify are listed as open, not removed |
