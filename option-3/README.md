# Flieber website: Option 3 (Build with Flieber / Run with Flieber)

**Option 3** puts the positioning from *Flieber Website Strategy & Functional Specification* (working draft 1.0, Oct 12, 2026) on top of Option 2's design system, facts and copy. Option 2 is on branch `claude/eager-bohr-ui8a03` and Option 1 on `claude/gracious-dijkstra-qgcgls`. Neither branch is touched from here.

Core promise: **Inventory software that works the way you do.** Two journeys share one foundation:

- **Build with Flieber**: data foundation, inventory intelligence, app templates and reliability tools, each selectable on its own, through MCP and API.
- **Run with Flieber**: ready-to-use apps for demand forecasting, inventory forecasting, replenishment and workflows, tailored by Flieber's team when needed.

## What's new and what's carried over

| Route | Source |
|---|---|
| `/` | New: vision-first homepage (spec section 7). Both paths are visible in the first viewport at 1366×768 |
| `/build/` | New: Build overview (spec 8.1–8.6), with anchors `#data`, `#intelligence`, `#templates`, `#reliability` and `#services` |
| `/build/data/` | Option 2's `/product/data-layer/` page, moved under Build |
| `/run/` | New: Run overview (spec 9.1), with Option 2's decision-simulation card in the hero |
| `/run/forecasting/`, `/run/inventory/`, `/run/replenishment/`, `/run/workflows/` | Option 2's module pages plus the spec's application template (9.2): audience, three jobs, inputs and outputs, accuracy, customization and FAQ |
| Every other page | Option 2 pages with the new navigation, footer and links (features, pricing, MCP, customize, integrations, solutions, use cases, managed services, who we are, security, contact, /agents) |

Navigation: Build ▾ · Run ▾ · Solutions ▾ · Pricing · Who we are · `/agents`, then Log in · Book a demo · Start free trial. Build and Run pages carry a sticky journey bar with breadcrumbs and a one-click Build/Run switch (spec section 12). Build is marked with a black dot and Run with a yellow one, in the nav and the switch.

The old `/product/*` URLs redirect to their new homes (`Caddyfile`).

## How to build

```
cd option-3
python3 scripts/build_option3.py        # regenerates new pages, rewrites nav/footer/links on carried pages
python3 scripts/check-placeholders.py   # lists every [PLACEHOLDER] still on the site
python3 -m http.server                  # preview at http://localhost:8000
```

- `scripts/chrome.py`: head, navigation, journey bar and footer
- `scripts/content_option3.py`: copy for the homepage, `/build/`, `/run/` and the additions to the Run app pages
- `scripts/src/`: Option 2's homepage and module pages, kept as source material
- `assets/css/site.css`: Option 2 styles, plus an "Option 3" block at the end

The generator needs Python 3.12 or later. Railway preview: the same `Dockerfile` and `Caddyfile` setup as Option 2, with `option-3/` as the service root directory.

## Placeholders before launch (visible as dashed `[BRACKETS]`)

All of these are on `/build/`:

- `[CONFIRM BRING-YOUR-OWN-WAREHOUSE SUPPORT]`: CSV and Google Sheets uploads and forecast imports are confirmed. A direct connection to a customer's own data warehouse is not (spec 8.2, acceptance criteria)
- `[IN PREPARATION]` ×4 and `[LICENSE, REPOSITORIES AND RELEASE DATES]`: no app templates are published yet (spec 2 and 19, P0/P1)
- `[CONFIRM OWNERSHIP AND SUPPORT TERMS]`: code ownership and maintenance for self-serve vs engineer-built work (spec 5.1)
- `[CONFIRM EXPORT AND PORTABILITY TERMS]`: the "Am I locked in?" answer

Everything else comes from Option 2's approved copy: 1,000+ brands since 2019, the four customer results, the 36% accuracy claim with Nixtla, customer logos and quotes, integrations, pricing terms and security facts.

## Known gaps

- `/agents`, `llms.txt`, `llms-full.txt` and `capabilities.json` still carry Option 2's positioning ("the inventory intelligence layer your agents run on"). Only their URLs were updated. Rewrite them once Option 3 is chosen (spec section 11).
- Pages carried from Option 2 keep their own headlines and copy, so the "agents run on" framing still shows in places such as `/features` and `/mcp`.
- Two integration tiles (SPS Commerce, Apparel Magic) on `/integrations/` link to a missing logo image (`../None`). The bug is inherited from Option 2.
- No `/solutions` gallery or `/developers` hub yet (spec Phase 2). The Solutions menu and `/mcp/` cover them for now.
