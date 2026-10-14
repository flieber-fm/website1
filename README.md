# Flieber website: Option 7

**This branch (`claude/option-7`) is Option 7**, the service-led positioning from the memo "Flieber Website: Path to the Final Version" (Oct 14). It starts from Option 6 (`claude/option-6`, f74517f) and adds Option 4's hero demo and role cards and Option 2's agent page and files, rewritten to the new lead. Options 1, 2, 4, 5 and 6 are never touched from here.

- Lead: "Your inventory planning, done with you" (Flieber's planners and planning engine, Managed Services).
- Supporting: customization (how the help fits the team) and the agent platform (MCP, API, /agents, llms.txt, capabilities.json).
- `/review` is a preview-only reviewer's guide: which positioning leads, where each appears, open decisions and new wording. Remove before launch.
- `scripts/build_agents.py` generates `agents/index.html`, `llms.txt` and `capabilities.json` from one source. Run it, then `python3 scripts/site_chrome.py`.
- `assets/css/demo.css` and `assets/js/demo.js` are Option 4's `v1.css` / `v1.js` (hero tool demo), loaded on the homepage only.
- Free trial: still out, as in Option 6. Open decision.

The notes below are Option 6's and still describe the shared build.

---

# Flieber website: Option 6

**This branch (`claude/option-6`) is Option 6.** It starts from Option 2 (`claude/eager-bohr-ui8a03`, commit f4408ac). Option 2 and Option 1 (`claude/gracious-dijkstra-qgcgls`) are never touched from here.

Direction: `docs/26-10-14 Flieber Website Development Brief (Option 6 source).md` is the main direction. Option 2 is the guideline for structure, UI and approved claims wherever the two don't conflict.

- Copy, section by section: `docs/26-10-14 Website - Content Briefing (Option 6).md`
- Build, claims, open items and decision log: `docs/26-10-14 Website - Technical Briefing (Option 6).md`
- The Option 2 briefings stay in `docs/` as reference

## What's in the site

```
index.html              The homepage, edited by hand (one focused page with anchor navigation)
security/index.html     /security (approved wording from Option 2)
assets/css/site.css     All styles; Option 6 styles are in the "Option 6" block at the end
assets/js/site.js       Nav, reveals, quotes carousel, the "Talk to us" form and analytics events
assets/fonts, img, logos
scripts/site_chrome.py  Nav and footer for both pages
scripts/check-placeholders.py   Lists placeholders and the preview no-index layers
Dockerfile, Caddyfile   Static preview server (Railway)
robots.txt              PREVIEW: blocks all crawlers
robots.production.txt   Launch version
```

## Build and check

1. Edit `index.html` (copy) or `scripts/site_chrome.py` (nav, footer), then run `python3 scripts/site_chrome.py`.
2. After any CSS or JS change, bump `site.css?v=` or `site.js?v=` in both HTML files.
3. Serve locally with `python3 -m http.server 8765`, then check 1440, 1024, 768 and 390px with Playwright (`PW=$(npm root -g)/playwright`) for horizontal overflow, JS errors and broken links and anchors.

The FAQ is in `index.html` twice: the visible list and the FAQPage JSON-LD. Change both.

## Preview rules

- Search engines are blocked by meta robots, `robots.txt` and the `X-Robots-Tag` header in `Caddyfile`. Keep it that way until launch.
- The form sends nothing yet. Connecting it is a HubSpot change and needs Fabricio's go.
- Analytics (GTM `GTM-5FS8NPG`, HubSpot portal 5767502) load only on flieber.com.
- Railway does not auto-deploy. Option 6 gets its own service; never deploy it to website-option-2 or Option 1's service.
