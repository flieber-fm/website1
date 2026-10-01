# Switching www.flieber.com to the new site (HubSpot)

Nothing is deleted or overwritten. The new site is built as **new** pages, templates and modules in HubSpot. Old pages are only **unpublished**: they stay in the account as drafts, with their full revision history, and can be republished at any time.

## Before the switch (Claude)

1. Build the new pages in HubSpot as unpublished drafts: Home, /agents, /pricing, /security, /contact, under temporary URLs starting with `/new-site-2026/`. Existing pages, templates and modules are not touched. Templates are generated with `python3 scripts/build-hubspot.py` (output in `hubspot/build/`).
2. Send you the HubSpot preview link for each draft to review.

## On the day of the switch (Fabricio, about 30 minutes)

Do the steps in this order. Steps 2 and 3 should happen within a few minutes of each other, because between them those URLs show a 404.

### 1. Check the uploaded files

Fonts, images, `llms.txt` and `capabilities.json` are uploaded ahead of time to the File Manager folder `flieber-2026` (by Claude through the HubSpot CLI, or by hand: **Content > Files**, folder `flieber-2026`, upload every file from `assets/fonts`, `assets/img`, `assets/logos` plus `llms.txt` and `capabilities.json`). Check that `https://www.flieber.com/hubfs/flieber-2026/llms.txt` opens. If the URL is different, tell Claude so the templates and the redirect file can be updated.

### 2. Unpublish the old pages (do not delete)

In **Content > Website Pages**, for each page below: hover over it, click **More**, then **Unpublish**. If you also see **Archive**, you can use it: archived pages stay in the account and can be restored. Never use **Delete**.

- Flieber Home 2026 (`/`)
- Pricing New (`/pricing`)
- Every page in `url-redirects.csv` that is still published: /pricing-plans, /integrations, /frequently-asked-questions, /managed-services, /product, /flieber-inventory, /flieber-studio, /omnichannel, /ecommerce, /agencies, the three /flieber-vs-… pages, /best-inventory-software and its three child pages, /standardize-vs-pages, /feature-drops, /old-home-page, /book-a-demo-old

Before unpublishing **/old-home-page**: check whether any ad campaign sends traffic to it (3,100 views from April to September 2026). If one does, update the ad first.

Keep these published: /book-a-demo, /free-trial, /blog (and every post), /privacy-policy, /service-agreement, /glossary, /learn-hub, /videos.

### 3. Publish the new pages

Tell Claude, who changes each draft's URL from `/new-site-2026/...` to its final URL (`/`, `/agents`, `/pricing`, `/security`, `/contact`) and publishes it.

If HubSpot says a URL is already in use, the old page still holds it: open the old page, change its URL to `/archive/<old-slug>` and keep it unpublished, then publish the new page.

### 4. Import the redirects

1. Go to **Settings (gear icon) > Content > Domains & URLs > URL Redirects**.
2. Click **Import** and upload `hubspot/url-redirects.csv`. Map the columns: Original URL and Redirect to. Use permanent (301) redirects.
3. Check that /llms.txt and /capabilities.json open the two files you uploaded in step 1.

### 5. Set robots.txt

1. Go to **Settings > Content > Pages**, select the www.flieber.com domain, then the **SEO & Crawlers** tab.
2. Replace the robots.txt contents with `robots.production.txt` from the repository.

### 6. Click through

Open each of these and check they load the new design: `/`, `/agents`, `/pricing`, `/security`, `/contact`, `/llms.txt`, `/capabilities.json`, and three old URLs (for example `/pricing-plans`, `/product`, `/integrations`) to confirm they redirect.

## Undo

Unpublish the new page and republish the old one. Redirects can be removed from the same URL Redirects screen.
