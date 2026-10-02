# Switching www.flieber.com to the new site (HubSpot)

> **Option 2 branch.** Nothing below has been done for Option 2: no files, templates or drafts exist in HubSpot for it. If Option 2 is elected, its 15 drafts go under `/new-site-2026-b/` and the lists below apply (see `docs/26-10-02 Website - Technical Briefing (Option 2).md`). The "Current state" section describes Option 1's drafts.

Nothing is deleted or overwritten. The new site is built as **new** pages, templates and modules in HubSpot. Old pages are only **unpublished**: they stay in the account as drafts, with their full revision history, and can be republished at any time.

## Before the switch (Claude)

1. Build the new pages in HubSpot as unpublished drafts: Home, /agents, /pricing, /security, /contact, under temporary URLs starting with `/new-site-2026/`. Existing pages, templates and modules are not touched. Templates are generated with `python3 scripts/build-hubspot.py` (output in `hubspot/build/`).
2. Send you the HubSpot preview link for each draft to review.

## Current state (Oct 1, 2026)

- Files uploaded to File Manager folder `flieber-2026` (fonts, images, customer logos, llms.txt, capabilities.json), served at `https://www.flieber.com/hubfs/flieber-2026/...`
- Templates in Design Manager folder `flieber-2026/templates` (home, agents, pricing, security, contact). Regenerate with `python3 scripts/build-hubspot.py` and upload with the CMS source-code API after any change
- Draft pages (unpublished):
  - [New site 2026] Home: 223386154416, `/new-site-2026/home`, final URL `/`
  - [New site 2026] Agents: 223390302985, `/new-site-2026/agents`, final URL `/agents`
  - [New site 2026] Pricing: 223390303022, `/new-site-2026/pricing`, final URL `/pricing`
  - [New site 2026] Security: 223386154542, `/new-site-2026/security`, final URL `/security`
  - [New site 2026] Contact: 223386154546, `/new-site-2026/contact`, final URL `/contact`

## On the day of the switch (Fabricio, about 30 minutes)

Do the steps in this order. Steps 2 and 3 should happen within a few minutes of each other, because between them those URLs show a 404.

### 1. Check the uploaded files

Fonts, images, `llms.txt` and `capabilities.json` are uploaded ahead of time to the File Manager folder `flieber-2026` (by Claude through the HubSpot CLI, or by hand: **Content > Files**, folder `flieber-2026`, upload every file from `assets/fonts`, `assets/img`, `assets/logos` plus `llms.txt` and `capabilities.json`). Check that `https://www.flieber.com/hubfs/flieber-2026/llms.txt` opens. If the URL is different, tell Claude so the templates and the redirect file can be updated.

### 2. Unpublish the old pages (do not delete)

In **Content > Website Pages**, for each page below: hover over it, click **More**, then **Unpublish**. If you also see **Archive**, you can use it: archived pages stay in the account and can be restored. Never use **Delete**.

- Flieber Home 2026 (`/`)
- Pricing New (`/pricing`)
- The old /agencies page (the new /agencies replaces it on the same URL)
- Every page in `url-redirects.csv` that is still published: /pricing-plans, /integrations, /frequently-asked-questions, /product, /flieber-inventory, /flieber-studio, /omnichannel, /ecommerce, /flieber-vs-netsuite, /flieber-vs-netstock, /flieber-vs-foresight-ai, /best-inventory-software and its three child pages, /standardize-vs-pages, /feature-drops, /old-home-page, /book-a-demo-old
- /flieber-vs-inventory-planner stays unpublished and is never redirected

Before unpublishing **/old-home-page**: check whether any ad campaign sends traffic to it (3,100 views from April to September 2026). If one does, update the ad first.

Keep these published: /book-a-demo, /free-trial, /blog (and every post), /privacy-policy, /service-agreement, /glossary, /learn-hub, /videos, /ecommerce2, /managed-services (with the new header and footer).

### 3. Publish the new pages

Tell Claude, who changes each draft's URL from `/new-site-2026-b/...` to its final URL (`/`, `/features`, the five `/product/...` pages, `/multichannel`, `/agencies`, `/before-you-choose`, `/mcp`, `/agents`, `/pricing`, `/security`, `/contact`) and publishes it.

If HubSpot says a URL is already in use, the old page still holds it: open the old page, change its URL to `/archive/<old-slug>` and keep it unpublished, then publish the new page.

### 4. Import the redirects

1. Go to **Settings (gear icon) > Content > Domains & URLs > URL Redirects**.
2. Click **Import** and upload `hubspot/url-redirects.csv`. Map the columns: Original URL and Redirect to. Use permanent (301) redirects.
3. Check that /llms.txt, /llms-full.txt and /capabilities.json open the files you uploaded in step 1.
4. Do not tick "match path prefix" on the /product redirect, or the five /product/ pages would redirect too.

### 5. Set robots.txt

1. Go to **Settings > Content > Pages**, select the www.flieber.com domain, then the **SEO & Crawlers** tab.
2. Replace the robots.txt contents with `robots.production.txt` from the repository.

### 6. Click through

Open each new page, the Product and Solutions menus, `/llms.txt`, `/llms-full.txt` and `/capabilities.json`, and old URLs such as `/omnichannel`, `/flieber-vs-netsuite`, `/product` and `/pricing-plans` to confirm they redirect. Confirm `/flieber-vs-inventory-planner` returns "not found".

## Undo

Unpublish the new page and republish the old one. Redirects can be removed from the same URL Redirects screen.
