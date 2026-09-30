# Flieber website

Static site for flieber.com. Built from the approved **Flieber Website Copy (Sep 29, 2026)** as the source of truth for all copy, and the **Flieber Brand Guidelines v1.0** for logo, type and color.

No build step. Any static host (Netlify, Vercel, Cloudflare Pages, GitHub Pages, S3) serves it as is.

```
index.html            Homepage (8 sections + footer)
agents/index.html     /agents: plain facts for AI agents
llms.txt              Same content as /agents, plain text
capabilities.json     Same content as /agents, machine-readable
assets/css/site.css   All styles; brand tokens at the top
assets/js/site.js     Nav, scroll reveals, hero agent demo, quote carousel, copy button
assets/fonts/         Open Sauce One 400/500/600 (SIL OFL, self-hosted)
assets/img/           Logo (dark + light), icon, favicon: vectors traced from the brand manual
assets/logos/         Customer logos from the shared Drive logo folder
```

Local preview: `python3 -m http.server` from the repo root, then open http://localhost:8000.

## Private preview (current state)

The site is deployed as a **hidden, non-indexed preview** on Railway (project `flieber-website-preview`), built from this branch with the `Dockerfile` (Caddy static server).

Three layers keep it out of search engines. **All three must be removed before the public launch:**

1. `<meta name="robots" content="noindex, nofollow">` in `index.html` and `agents/index.html`
2. `robots.txt` with `Disallow: /`
3. The `X-Robots-Tag` header in `Caddyfile`

The preview is unlisted, not password-protected: anyone with the URL can open it.

## Brand rules applied

- **Type:** Open Sauce One. Headings Regular at 110% line height and about -4% tracking; subheads SemiBold at -3%; body Regular.
- **Color:** Yellow `#F5ED61` is the primary color and is only used as a background, highlight or button fill. It is never used for text on a light background. Type is Black `#1B1C1C` on white and gray backgrounds. Dark sections use Black or Charcoal with Light Gray, White or Yellow text. Blue `#244AE3` appears once, on the forecast-accuracy stat, as an occasional bold accent.
- **Logo:** the wordmark is always paired with the icon and is never shown under 100px wide. The favicon uses the icon alone.

## Open items before launch

Every unconfirmed value is marked in the HTML with a `data-todo="KEY"` attribute, so `grep -rn data-todo` lists them all. Visible placeholders keep the bracket text from the copy doc and get a dashed outline (class `todo`). Until a URL is filled in, placeholder links on the homepage point to the **Try it** section instead of a dead `#`.

| Key | Where | What's needed |
| --- | --- | --- |
| `MCP_ENDPOINT_URL` | Home §9, /agents, llms.txt, capabilities.json | MCP endpoint URL (**blocks launch**) |
| `MCP_AUTH` | /agents, llms.txt, capabilities.json | Auth method (copy says "OAuth, confirm") |
| `MCP_DOCS_URL` | Footer, /agents, llms.txt, capabilities.json | MCP docs URL |
| `SANDBOX_URL` | Home §9, /agents | Sandbox link (sandbox still to be built, **blocks launch**) |
| `SIGNUP_URL` | Nav, hero, §5, §9 | Free trial / Get started destination |
| `PLANNER_URL` | Nav, hero, §5, §9, /agents | Booking link for "Talk to a planner" / 30-minute call |
| `NIXTLA_REPORT_URL` | Home §7, /agents | Link to the Nixtla report ("Read the method") |
| `SEC_*` (6 keys) | /agents Data handling, llms.txt, capabilities.json | Hosting, encryption, compliance, AI models, access, deletion |
| `ERP_LIST` | /agents Capabilities | ERPs besides NetSuite for "Push to ERP" |
| `CONTACT_EMAIL` | /agents Hand off, llms.txt, capabilities.json | Contact email |
| `HELP_CENTER_URL`, `BLOG_URL`, `CONTACT_URL`, `PRIVACY_URL` | Footer | Existing flieber.com URLs |

Also listed in the copy doc: someone needs to own the **"100+ brands today, 1,000+ since 2019"** figures (homepage §4 closing line and §7, /agents, llms.txt, capabilities.json).

## Notes

- **Hero adds a line to the approved copy.** The approved H1 ("Before AI can run your brand, someone has to keep your data true.") stays as the H1. Directly under it is "Make better [word] decisions." with a rotating word (inventory, purchasing, pricing, promo, ad spend, allocation, transfer, cash-flow). Edit the words in the `data-words` attribute in `index.html`; screen readers and crawlers get the full list as one sentence. The rotation runs once, settles on "inventory", pauses on hover, and is off for visitors who prefer reduced motion.
- **Cache busting:** CSS and JS are linked with `?v=N`. Bump it when you change either file.

- The hero "agent console" is an illustration and uses **made-up sample SKUs**; it is labeled "Sample brand · illustrative data". Replace it with real sandbox output once the sandbox exists.
- The logo strip uses the six logos (white PNGs, rendered black with a CSS filter) in the shared Drive logo folder (Lifepro, Zugu, Primal Harvest, Unybrands, Waterglider, Qualico). Modloft appears in a quote but has no logo in that folder. Check the strip against the live homepage before launch.
- Keep `/agents`, `llms.txt` and `capabilities.json` in sync. They are three renderings of the same content.
- Before launch, add an OG share image (`og:image`) and analytics.
