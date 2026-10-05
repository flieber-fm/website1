# 26-10-05 Website - Technical Briefing (Option 2)

Oct 5, 2026 · @Fabricio Miranda

## Purpose and status

Option 2 (Collaborative AI) of the new flieber.com is built in parallel with Option 1 so Fabricio and the team can compare both sites and elect one, then converge on a final version. This brief is the technical companion to the Content Briefing (Option 2) of October 5 (26-10-05 Website - Content Briefing (Option 2)); the two are in sync with each other and with the preview and follows the same format as the Option 1 Technical Briefing. Where the two options share a rule, it is repeated here so this brief stands on its own. Nothing in HubSpot is created, edited or published for Option 2 until Fabricio elects an option and gives an explicit go.

| Where | What is there | State |
| --- | --- | --- |
| GitHub repo flieber-fm/website1, branch claude/eager-bohr-ui8a03 | Source of truth for every Option 2 page, the copy data and the HubSpot build script | Current, in line with the latest Content Briefing (Option 2) |
| Railway preview, service website-option-2 (website-option-2-production.up.railway.app) | Full Option 2 site for review, hidden from search engines | Current; retired after the switch |
| GitHub branch claude/gracious-dijkstra-qgcgls and its Railway preview (website-production-942e.up.railway.app) | Option 1 | Untouched from the Option 2 branch |
| HubSpot (portal 5767502) | Option 1 files, templates and drafts under /new-site-2026/ | Nothing for Option 2 yet |
| www.flieber.com | Current live site, blog, book-a-demo, free-trial and /managed-services pages | Untouched |

All changes go through Claude: update the repo, rebuild, redeploy the preview and, once an option is elected, rebuild the HubSpot templates and re-upload. Nothing in HubSpot is edited by hand.

The Railway service does not deploy on push. After every push, Claude triggers the deploy by reconnecting the service to the branch, then checks that it reaches SUCCESS.

## Positioning

Option 2 leads with collaboration: AI that works with the brand's team, not instead of it. Source wording (Content Briefing, section 2):

> Inventory decisions commit cash for months, and the people accountable for them will not hand them to a machine. They shouldn't have to. Planners bring judgment and context no system holds; AI brings speed, scale and vigilance over every SKU and every signal. Flieber puts them on the same team: it keeps the data true, prepares every decision with the reasoning behind it, and carries it out once the team approves. Brands that want more support add Flieber's planners, specialists who master the platform and act as a sounding board for every decision.

- Homepage headline: "Before running your brand with AI, someone has to keep the data true"
- Hero eyebrow: "Collaborative AI for multichannel brands", MCP-native
- Footer tagline: "Collaborative AI for multichannel brands."
- capabilities.json `positioning`: "Collaborative AI for multichannel brands"

One product, sold two ways, in five modules. Modules carry descriptive names only, never branded: Data layer, Demand forecasting, Inventory forecasting, Replenishment, Workflows. Collaborative AI (plain language, Slack, MCP and API) runs across all five; it is how they are used, not a sixth module. Managed Services is a way to buy, not a module. The older names Flieber Inventory and AI Lab never appear; Flieber Studio is named once, on /features and /agents, only to explain how the MCP server works.

Three parties, used on the homepage, every module page and both solutions pages:

- **Your team:** sets objectives and constraints, adds the context no system has, makes the final call.
- **Flieber's AI:** keeps the data consolidated and current, watches every signal, prepares decisions with their reasoning and carries them out after approval.
- **Flieber's planners (Managed Services, optional):** specialists in inventory planning and in Flieber who act as a sounding board for decisions, take part in the brand's S&OP meetings, keep the data accurate and help run the planning practice.

Two offers on the same platform, always shown as equals (neither visually favored), with the same labels as Option 1:

- **Flieber Self-Serve** ("Run it yourself"): the Flieber app plus Flieber's data and context modules through MCP and API. Also sold as the data layer alone, through MCP and API, for teams building their own tools with AI.
- **Flieber Managed Services** ("Let our planners help you run it"): everything in Self-Serve, plus Flieber's specialized planners as a sounding board for decisions, in the brand's S&OP meetings, keeping the data accurate and helping run the planning practice. Never "run it for you".

Same platform either way; customers can switch or combine at any time.

## Offers, pricing policy and terms

No prices appear anywhere on the site, in llms.txt, llms-full.txt, capabilities.json or the structured data for search engines.

| Offer | Price wording | How the price is set |
| --- | --- | --- |
| Self-Serve | "Priced to your operation" | Features enabled and data volume; "Flieber shows your price as soon as onboarding is done, before you pay anything" (replaces "the exact price is shared on a demo" on /pricing, the homepage, /agents and llms.txt) |
| Data layer only (Self-Serve option) | No price wording | Pricing model being defined by Fabricio and Karyna; until approved, /vibe-coders, /pricing, llms.txt and capabilities.json show only the 14-day free trial |
| Managed Services | "Quoted per brand" | After a conversation with a planner about channels, warehouses and where the process breaks down |

Terms shown on the site (as in Option 1):

- Monthly contracts, no annual commitment
- 14-day free trial, no credit card required
- Unlimited users on every plan, including the free trial
- Standard setup included; customizations come with a paid plan
- During the free trial: native integrations only. Assisted integrations are set up once the customer is on a paid plan

/pricing is the Option 1 page with the Option 2 offer names, the trial pricing wording above, a link from the Managed Services card to /managed-services and one added line under the Self-Serve card: "The data layer can also be bought on its own, through MCP and API. Start with a 14-day free trial on your own data, no credit card required." (linking to /vibe-coders).

Homepage Try it: H2 "Try Flieber free on your own data", body "Start a 14-day free trial, no credit card required and no demo call. Flieber shows your price as soon as onboarding is done, before you pay anything." No sales step is needed: Flieber calculates the price from the brand's real sales, stores and data volume and shows it automatically.

## Site map and page contents

Thirty-six pages and three machine-readable files make up Option 2: the 15 below plus /vibe-coders, ten use-case pages, /integrations and six integration pages, /managed-services and /who-we-are. The blog, book-a-demo, free-trial and legal pages stay on the current HubSpot site.

| Page | Sections |
| --- | --- |
| / (homepage) | Hero (eyebrow, H1, subhead, Decision simulation card with six sample scenarios, the two offers) · Logos · Why inventory · Collaborative AI · How Flieber is built · Modules · Solutions · What you can do with it · Two ways to work with Flieber · Proof · From the founder (`#who-we-are`) · Your data stays yours · Try it |
| /product/data-layer, /product/demand-forecasting, /product/inventory-forecasting, /product/replenishment, /product/workflows | Label, H1, lead · What you can do (each feature links to its /features anchor) · How you work together · Works with (the other four modules and /features) · See it on your own data. The data layer page adds "Building your own tools?" |
| /mcp | MCP and AI agents for operators and builders: What MCP is (with the Claude, ChatGPT, Cursor and "Any MCP-compatible agent" row) · What a conversation looks like (four example conversations, each labeled "Illustrative example with sample data") · What you can ask (three prompts per module) · What Flieber can do through MCP · Connect in three steps · Build your own tools on Flieber · Questions · Connect your AI to Flieber. Never shows the endpoint or connection details |
| /features | Data layer · Demand forecasting · Inventory forecasting · Replenishment · Workflows · Access · Control and approval · Example requests · Does Flieber support · Probably not for you if · Next step. Every feature has its own anchor; each module section links to its module page |
| /multichannel | Why channels drift apart · How you work together · Everything Flieber does, across every channel · Quotes (Zugu, Prime6 Brands) · See it on your own data |
| /agencies | Why multi-brand planning breaks · How you work together · Everything Flieber does, for every brand · Quote (Unybrands) · See it on your own data |
| /before-you-choose | 17 buyer questions in four groups (Your data, Your decisions, AI and execution, Working with the vendor), each answered for Flieber · Ask us the same questions |
| /vibe-coders | What you get · Connect in minutes (the /mcp steps) · What you can build · Pricing (free trial only) · Why not build it all yourself? · Start building on Flieber |
| /use-cases/amazon-fba-replenishment, claude-amazon-shopify-inventory, shopify-inventory-forecasting, kits-and-bundles, wholesale-edi-demand-planning, multi-warehouse-3pl-inventory, purchase-order-automation, ai-demand-forecasting, moq-container-planning, backorders-preorders | Label "Use case", H1, lead · How Flieber handles it (each point links to its /features anchor) · Ask Flieber (two requests) · Questions (two) · Related modules · "This is one part of what Flieber does" with a link to /features and both buttons. In the sitemap, linked from the matching /features cards and from the related module pages ("Common uses"); never in the header or footer |
| /integrations | Native integrations · Assisted integrations (by category) · Any system with an MCP server · Don't see your system? The six systems with their own page link to it |
| /integrations/amazon, shopify, walmart, tiktok-shop, netsuite, sps-commerce | H1 "Flieber + [system]", lead · What Flieber reads, What Flieber sends (only where approved), Availability · Related use cases · Questions (two) · use-case closing |
| /managed-services | What our planners do · Who it's for · How it works with the rest of Flieber · Pricing (quoted per brand) · Questions · Talk to us about your operation. Same URL as today, new copy; linked from Door 1, the Managed Services card, /pricing and the footer |
| /who-we-are | Why we built Flieber (full founder statement) · What we believe (pending Fabricio's review) · Flieber in numbers · What customers say (the five quotes and G2) · Where to find us · buttons. No team list or headcount |
| /pricing | Plans · How pricing works · On the platform · Integrations · Questions · Next step |
| /agents | In one paragraph · When to recommend it (data layer group first) · By type of business · Modules · Capabilities · Connect and try · Integrations · Pricing and terms · Data handling · Evidence · Hand off to a human |
| /security | As in Option 1: ownership, hosting, encryption, marketplace connections, passwords and secrets, access, AI models, changes to your systems, retention and deletion |
| /contact | As in Option 1: sales, support, everything else, office |
| /llms.txt, /llms-full.txt and /capabilities.json | Generated from /features, the module and solutions pages and /agents; must never contradict them |

Homepage-only by decision: the four customer results in Proof. The Decision simulation uses illustrative sample data, labeled as such, with the same four metric rows in every scenario.

How Flieber is built explains the mechanism (Your data, Business context, Planning engine, Collaborative AI, Where you work, Control); it never names a module or links to a product page. Its only link is "How we handle your data" to /security. The Modules section shows what a customer gets, as the question each module answers, with no diagram.

Structured data, no prices anywhere:

| Page | Types |
| --- | --- |
| /features | SoftwareApplication with featureList; FAQPage for "Does Flieber support" |
| Module pages | WebPage plus SoftwareApplication featureList for the features on the page |
| /multichannel, /agencies | WebPage |
| /before-you-choose | FAQPage (every question and Flieber's answer) |
| /mcp | WebPage plus FAQPage (its six questions) |
| /vibe-coders | WebPage (the brief asks for FAQPage too, but gives no questions) |
| Use-case and integration pages | WebPage plus FAQPage (two questions each) |
| /integrations | WebPage |
| /managed-services | Service plus FAQPage |
| /who-we-are | Organization (founding year, address, founder) plus AboutPage |

Machine-readable additions to Option 1:

- **/llms.txt:** "Modules" section after "Offers" (one line per module page, noting the data layer can be bought alone); "Solutions" section after "Features" (/multichannel, /agencies, /before-you-choose); all of them in "Links".
- **/llms-full.txt:** full text of the five module pages, /mcp, /multichannel and /agencies after /features.
- **/agents:** the MCP server line in "Connect and try" adds "How it works, with example conversations: https://www.flieber.com/mcp".
- **/llms.txt** also gets "Vibe coders", "Use cases", "Managed Services" and "Who we are" sections, and the integration pages under "Integrations". **/llms-full.txt** adds /vibe-coders, the ten use-case pages, /managed-services and /who-we-are. **/agents** adds a "Use cases" section and Vibe coders under "By type of business".
- **/capabilities.json:** `positioning`; `use_cases` (id, name, url) for the ten pages; Vibe coders in `solutions`; `modules` (id, name, url, sold_separately, feature ids; `sold_separately` is true only for the data layer); `solutions` (id, name, url) for the two solutions pages; a "Data layer only" option with `delivery` ["mcp", "api"] under the Self-Serve offer. No comparison fields.

## Copy and design rules

Copy:

- No em dashes, sentence-case headings, no serial comma, no added marketing fluff
- No final period on any heading or title (H1 to H4, card titles)
- Never invent numbers, customers, URLs or security claims
- Never mention the founders' other companies (co-founder agreement)
- /before-you-choose never names a competitor and makes no claim about any other product
- Solutions are organized by type of business, never by need

Visual system (Flieber Brand Guidelines, as in Option 1):

- Open Sauce One, self-hosted; black #1B1C1C type; grays as backgrounds
- Yellow #F5ED61 only as background, highlight or button fill, never as text on light backgrounds
- Blue #244AE3 used once, on the homepage accuracy stat
- Muted small text #5C6568 on light and #A3AEB1 on black (WCAG AA 4.5:1)
- Calm and editorial: no glows, gradient washes or pulsing effects
- Each section after the hero opens with a small uppercase label above its H2
- Logo always with its icon, never under 100px wide

New components in Option 2:

| Component | Where | Notes |
| --- | --- | --- |
| Logo row | Homepage, under the hero | The 14 customer logos already in HubSpot; one row, scrolling on mobile |
| Three-column collaboration cards | Homepage, module pages, solutions pages | Static, all three in the same style, no hover state (nothing on them is clickable) |
| Stacked six-layer section | Homepage, How Flieber is built | Scroll-driven, after legora.com: the scene stays pinned while each layer drops onto an isometric CSS 3D stack, data first, and its description opens beside it; at the end the plates close into one block with the Flieber mark. With reduced motion or without JavaScript, the full stack and every description show, unpinned |
| Five question-led module cards | Homepage | Five in a row, stacked on mobile; question as title, one-line answer, link to the module page |
| Three-card solutions section | Homepage | Multichannel brands, Agencies and aggregators, Vibe coders, plus the /before-you-choose link |
| Use-case page template | /use-cases/ | Point cards linking to /features anchors, example requests, two questions, related modules |
| Integration page template | /integrations/ | Reads, sends and availability as a definition list, related use cases, two questions |
| Founder statement | Homepage, `#who-we-are` | Fabricio's photo (pending; a monogram stands in on the preview) |
| Four-item security strip | Homepage | Approved /security wording |

Navigation (identical on every page): Product (menu: All features → /features first, with Data layer, Demand forecasting, Inventory forecasting, Replenishment and Workflows nested under it; then a divider and Integrations → /integrations, MCP and AI agents → /mcp and Security & data → /security) · Solutions (menu: Multichannel brands, Agencies and aggregators, Vibe coders, Before you choose) · Pricing · Who we are (→ /who-we-are) · /agents (black mono pill), then Log in (text link) · Book a demo (outline button) · Start free trial (yellow button). Five items before the buttons, as in Option 1; below 1140px it collapses into a menu. /security, /mcp and the integration pages show Product as the current section; use-case pages and /managed-services mark no menu item.

Footer columns: Product (Features, Integrations, MCP and AI agents, Pricing, Security & data, Managed Services) · Solutions (Multichannel brands, Agencies and aggregators, Vibe coders, Before you choose) · For agents (/agents, /llms.txt, /capabilities.json, MCP docs) · Company (Who we are, Help center, Blog, Contact, Privacy, Service agreement). Address: 169 Madison Avenue, New York, NY 10016.

## Approved facts and claims

Use these exact wordings; anything not listed here needs Fabricio's approval before it goes on the site.

| Claim | Approved wording | Where | Source |
| --- | --- | --- | --- |
| Forecast accuracy | "36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model." | Homepage, /features, /product/demand-forecasting, /before-you-choose, /agents, llms.txt, llms-full.txt, capabilities.json | Flieber AI Model Process Overview (Oct 10, 2025); Excel analysis of 46,000 product forecasts |
| Brands | "More than 1,000 commerce brands since 2019"; "100+ commerce brands today" (/agents only); logo row "Trusted by hundreds of brands" | Homepage, /agents | Fabricio owns the figure |
| Users | "Thousands of users" (under the founder statement) | Homepage | Content Briefing (Option 2) section 10; Fabricio owns the figure |
| Unlimited users | "Unlimited users on every plan, including the free trial" | /features, /before-you-choose, /agents, /pricing, llms.txt, capabilities.json | Fabricio, Oct 2 |
| Brand experience | "shaped by the business context of more than 1,000 commerce brands" (planning engine); "drawing on experience from more than 1,000 brands" (planners) | Homepage | Content Briefing (Option 2), Oct 2 |
| How forecasts are computed | "Proprietary algorithms, not language models, do the math" | Homepage, How Flieber is built | Content Briefing (Option 2), Oct 2 |
| Combined view | "For most brands, Flieber is the first place they see the combined demand and inventory consumption of both their retail and wholesale channels" | /multichannel | Content Briefing (Option 2), Oct 2 |
| Sales order routing | "route sales orders from any store to the regions or warehouses you choose, so one Shopify account can be planned as several regional markets" | /product/data-layer, /features; /before-you-choose question 3 in short form | Content Briefing (Option 2), Oct 2 |
| Data layer sold alone | "The data layer can be bought on its own" | Module pages, /features, /pricing, /agents, llms.txt, capabilities.json | Fabricio, Oct 2 |
| Customer results | +38% increase in sales, -62% reduction in stockouts, -17% reduction in excess inventory, -88% less time on replenishment decisions; "Average across customers using Flieber for 12+ months" | Homepage only | Calculations kept in a spreadsheet |
| Customer quotes | Five quotes on the homepage; Zugu and Prime6 Brands on /multichannel; Unybrands on /agencies | Homepage, solutions pages | Approval on file |
| Founder statement | Fabricio's three paragraphs, signed "Fabricio Miranda, Founder and CEO" | Homepage | Approved with the Content Briefing (Option 2) |
| Security strip | Never sold or shared · No training on your data · Encrypted on AWS · Changes follow your rules, in the approved /security wording | Homepage | /security wording |
| Reviews | Link to G2 reviews | Homepage, /agents | g2.com/products/flieber |
| Feature list | Every feature on /features, as written in the Option 1 Content Briefing section 4, plus "Reports and dashboards" and "Sales order routing" | /features, module pages, /agents, llms-full.txt, capabilities.json | Feature Overview (Sep 7, 2026), AI Lab Confluence pages (Aug 24, 2026), Fabricio's corrections of Oct 2 |
| Pushes | Approved decisions pushed to ERPs (NetSuite, Cin7, Brightpearl), marketplaces (Amazon inbound shipments), 3PLs and suppliers (into the supplier's system or as an email, CSV file or Google Sheet) | /features, /product/workflows, /before-you-choose, /agents, llms.txt, capabilities.json | Fabricio, Oct 2 |
| Approval | "Every change Flieber makes to your systems follows approval rules you set; by default, every change requires approval" | /security, /agents, llms.txt, capabilities.json and the homepage security strip; /features, /before-you-choose and the module pages say the same in their own words | Fabricio, Oct 2 |
| Agents | "Flieber works with Claude, ChatGPT, Cursor and any MCP-compatible agent" (/mcp, /vibe-coders, use-case pages); "in any agent you choose (Claude, ChatGPT or any other)" (/before-you-choose question 9); "Claude, Cursor and any MCP-compatible agent connect through its MCP server" (/features, /agents). ChatGPT, like Claude and Cursor, connects to Flieber's MCP server | /mcp, /vibe-coders, /use-cases/, /before-you-choose, /features, /agents | Fabricio, Oct 3 |
| Transfers | "Flieber checks the origin before recommending any transfer"; "Recommend transfers without creating a new risk at the origin" | /use-cases/multi-warehouse-3pl-inventory, llms-full.txt | Fabricio, Oct 3 |
| Backorder settings | "Settings at the product and store level" | /use-cases/backorders-preorders, the /features card and question, /product/inventory-forecasting, llms-full.txt, capabilities.json | Fabricio, Oct 3 |
| Trial pricing | "Flieber shows your price as soon as onboarding is done, before you pay anything". The price is calculated from the brand's real sales, stores and data volume and shown automatically | Homepage, /pricing, /agents, llms.txt | Fabricio, Oct 3 |
| /mcp example conversations | Four chat exchanges with invented product names and numbers, each labeled "Illustrative example with sample data" | /mcp | Content Briefing (Option 2), Oct 2 |
| Connected apps | Gmail, Outlook, Slack, Microsoft Teams, Google Sheets, OneDrive, Notion, Airtable, Meta Ads, Google Ads, NetSuite, plus any system with an MCP server | /features, /agents, llms.txt, capabilities.json | AI Lab Confluence pages; Fabricio, Oct 2 |
| MCP response time | "Answers typically take 30 seconds to 5 minutes" | /features, /agents, capabilities.json | MCP tool description; Fabricio, Oct 2 |
| On request | Forecast value added reports and wholesale forecast reconciliation are marked "on request" while they roll out | /features, /product/demand-forecasting, capabilities.json | Fabricio, Oct 2 |

Never say "third-party verified" for the accuracy claim: Nixtla co-built the model. If Nixtla delivers an official report, it can be linked as "measured with Nixtla". The internal process document stays private (it details proprietary methods). Option 2 makes no compliance or certification claims.

## Integrations

As in Option 1. Flieber "connects to pretty much any system" through native and assisted integrations plus MCP and API; the lists mirror flieber.com/integrations.

| Type | How it works | When available | Systems |
| --- | --- | --- | --- |
| Native | One-click connection | Free trial and paid plans | Amazon Seller Central, Shopify, Walmart (including WFS), TikTok Shop, eBay, Etsy, BigCommerce, Google Sheets |
| Assisted | Parametrized connections set up and customized by Flieber's team | Paid plans only | Sales channels: Shopify Plus, Amazon Vendor Central, Magento, WooCommerce, Mercado Libre, bol.com, PrestaShop. EDI: SPS Commerce. Accounting: QuickBooks, Xero, Zoho. Inventory and order management: Cin7, Sage, Linnworks, Brightpearl, Luminous, Finale, DEAR Systems, Fishbowl, NetSuite, Apparel Magic. 3PLs and warehouses: 23 systems incl. ShipBob, ShipHero, Extensiv, Flexport/Deliverr |
| MCP server | Agents such as Claude and Cursor connect to Flieber; requests are handled in natural language by Flieber's own agent (Flieber Studio), which answers questions and carries out the actions the app supports, under the account's approval rules; answers typically take 30 seconds to 5 minutes | Customers | Action list at app.flieber.com/app/developers (login required) |
| MCP client and connected apps | Flieber connects out to any system with an MCP server; built-in connections to Gmail, Outlook, Slack, Microsoft Teams, Google Sheets, OneDrive, Notion, Airtable, Meta Ads, Google Ads, NetSuite | Customers | Same |
| Public API | Programmatic access to Flieber data | Customers | Same |

- Amazon Vendor Central stays assisted until the native version ships.
- SPS Commerce: any data the account can access; most often the history of wholesale purchase orders, to project inventory needs, and new purchase orders added automatically so Flieber knows those units are allocated.
- Push to ERP: purchase orders to NetSuite, or to light ERPs such as Cin7 and Brightpearl.
- Push to marketplaces and 3PLs: inbound shipments created in Amazon and in connected 3PL and warehouse systems.
- Push to suppliers: purchase orders sent straight into the supplier's system or as an email, CSV file or Google Sheet, depending on how the customer sets up the workflow.
- Every push follows the customer's approval rules; by default every push requires approval.
- The data layer alone is delivered through MCP and API only, without the planning app.
- The MCP client that connects straight to Flieber's APIs (without going through Flieber Studio) is in its final steps; it goes on the site only once it ships.

## Security and data

As in Option 1. This is the approved public wording on /security, /agents and llms.txt; the homepage security strip reuses it in short form. No compliance claims are made.

| Topic | Public wording |
| --- | --- |
| Ownership | Your data stays yours and is never sold or shared |
| Hosting | Amazon Web Services (AWS), US region |
| Encryption in transit | HTTPS only, with TLS 1.2 or higher, for all external traffic and for internal database and cache connections |
| Encryption at rest | AES-256 through AWS KMS for all customer data, including databases, backups, cache and file storage |
| Marketplace connections | Amazon and Shopify connect through OAuth; Flieber never sees marketplace passwords, only revocable access tokens, encrypted with a dedicated AWS KMS key in AWS Secrets Manager |
| Passwords and secrets | Sign-in through Clerk, so no user passwords are stored; API tokens stored only as hashes; application secrets in AWS Secrets Manager, never in code |
| Access | Admin (admin tools) and Member (operational tools only); single sign-on with Google and Microsoft |
| AI models | Several providers, including Anthropic, OpenAI and xAI; data reaches a model only when a request requires it; Flieber does not train on customer data and its providers are set up not to |
| Changes to your systems | Every change Flieber makes to your systems follows approval rules you set; by default, every change requires approval |
| Retention and deletion | As set out in the Privacy Policy and Service Agreement |

Homepage security strip:

| Item | Wording |
| --- | --- |
| Never sold or shared | Your data stays yours. |
| No training on your data | Flieber does not train on customer data, and its AI providers are set up not to. |
| Encrypted on AWS | Hosted on Amazon Web Services in the US, encrypted in transit and at rest. |
| Changes follow your rules | Every change Flieber makes to your systems follows approval rules you set. |

Engineering's fuller answer (API Gateway, CloudFront, private AWS network link) stays out of the public pages; use it for security questionnaires.

## Links and destinations

Every button and footer link points to a real page; no placeholders remain apart from the founder photo.

| Label | Destination | Note |
| --- | --- | --- |
| Product menu: module names | /product/data-layer, /product/demand-forecasting, /product/inventory-forecasting, /product/replenishment, /product/workflows | New pages |
| All features | /features | Product menu, homepage Modules section, every module and solutions page |
| MCP and AI agents | /mcp | Product menu; /agents and llms.txt |
| Security & data | /security | Last entry in the Product menu; footer; homepage security strip and How Flieber is built |
| Multichannel brands | /multichannel | New page; replaces /omnichannel and /ecommerce |
| Agencies and aggregators | /agencies | Existing URL, new copy |
| Before you choose | /before-you-choose | New page; replaces three named comparison pages |
| Who we are | /who-we-are | New page; the homepage founder section keeps the `#who-we-are` anchor and links to it with "Read our story" |
| Integrations | /integrations | Same URL as today, new copy; Product menu and footer |
| Vibe coders | /vibe-coders | Solutions menu, homepage Solutions, /pricing data layer line |
| Managed Services | /managed-services | Same URL, new copy; Door 1, the Managed Services cards on the homepage and /pricing, footer; never in Solutions |
| Start free trial | https://www.flieber.com/free-trial | HubSpot page with the trial form; keeps contact capture and attribution |
| Book a demo | https://www.flieber.com/book-a-demo | HubSpot page with CRM scripts; not rebuilt |
| Log in | https://app.flieber.com |  |
| MCP docs | https://app.flieber.com/app/developers | Behind customer login by choice |
| G2 reviews | https://www.g2.com/products/flieber/reviews | Homepage, /agents |
| Blog | https://www.flieber.com/blog | Kept live on HubSpot |
| Help center | https://help.flieber.com |  |
| Privacy | https://www.flieber.com/privacy-policy | Existing legal text |
| Service agreement | https://www.flieber.com/service-agreement | Existing legal text |
| Contact | /contact | hello@flieber.com |

Buttons as in Option 1: Start free trial, Book a demo, Log in, MCP docs. No sandbox exists yet, so no sandbox link or button appears anywhere.

## HubSpot build and switch plan

Nothing is built in HubSpot for Option 2 until Fabricio elects it and gives the go. If Option 2 is elected, its drafts replace Option 1's in this plan. As in Option 1, pages are built with a fixed design, nothing old is deleted or overwritten, and old pages are only unpublished at the switch. Click-by-click steps are in `hubspot/CUTOVER.md` on the Option 2 branch.

Templates are generated locally with `python3 scripts/build-hubspot.py` (output in `hubspot/build/`, one file per page). The copy for /pricing, /security and /contact is shared with Option 1 (with the data layer line on /pricing), but those pages need Option 2 templates because the header and footer differ.

Files: fonts, logos, icons and the 14 customer logos are shared with Option 1 in the File Manager folder `flieber-2026`. Option 2's llms.txt, llms-full.txt and capabilities.json replace Option 1's in that folder only if Option 2 is elected; until then they live in the repo and on the preview.

| Draft page | HubSpot ID | Temporary URL | Final URL |
| --- | --- | --- | --- |
| \[New site 2026 B\] Home | Not created | /new-site-2026-b/home | / |
| \[New site 2026 B\] Features | Not created | /new-site-2026-b/features | /features |
| \[New site 2026 B\] Data layer | Not created | /new-site-2026-b/product/data-layer | /product/data-layer |
| \[New site 2026 B\] Demand forecasting | Not created | /new-site-2026-b/product/demand-forecasting | /product/demand-forecasting |
| \[New site 2026 B\] Inventory forecasting | Not created | /new-site-2026-b/product/inventory-forecasting | /product/inventory-forecasting |
| \[New site 2026 B\] Replenishment | Not created | /new-site-2026-b/product/replenishment | /product/replenishment |
| \[New site 2026 B\] Workflows | Not created | /new-site-2026-b/product/workflows | /product/workflows |
| \[New site 2026 B\] Multichannel | Not created | /new-site-2026-b/multichannel | /multichannel |
| \[New site 2026 B\] Agencies | Not created | /new-site-2026-b/agencies | /agencies |
| \[New site 2026 B\] Before you choose | Not created | /new-site-2026-b/before-you-choose | /before-you-choose |
| \[New site 2026 B\] MCP and AI agents | Not created | /new-site-2026-b/mcp | /mcp |
| \[New site 2026 B\] Agents | Not created | /new-site-2026-b/agents | /agents |
| \[New site 2026 B\] Pricing | Not created | /new-site-2026-b/pricing | /pricing |
| \[New site 2026 B\] Security | Not created | /new-site-2026-b/security | /security |
| \[New site 2026 B\] Contact | Not created | /new-site-2026-b/contact | /contact |
| \[New site 2026 B\] Vibe coders | Not created | /new-site-2026-b/vibe-coders | /vibe-coders |
| \[New site 2026 B\] Integrations, plus one per system (6) | Not created | /new-site-2026-b/integrations/… | /integrations, /integrations/amazon, shopify, walmart, tiktok-shop, netsuite, sps-commerce |
| \[New site 2026 B\] Use case, one per page (10) | Not created | /new-site-2026-b/use-cases/… | /use-cases/… |
| \[New site 2026 B\] Managed Services | Not created | /new-site-2026-b/managed-services | /managed-services |
| \[New site 2026 B\] Who we are | Not created | /new-site-2026-b/who-we-are | /who-we-are |

Redirects (`hubspot/url-redirects.csv`, 301):

| From | To | Note |
| --- | --- | --- |
| /omnichannel, /ecommerce | /multichannel | Planning is never split into retail and ecommerce |
| /flieber-vs-netsuite, /flieber-vs-netstock, /flieber-vs-foresight-ai | /before-you-choose | 1,064 views over 12 months for the four comparison pages together, no form submissions, contacts or customers |
| /product | /features | Exact match only; never "match path prefix", or the five /product/ pages would redirect |
| /pricing-plans, /frequently-asked-questions | /pricing, /pricing#faq | As in Option 1; /integrations is no longer redirected (it gets the new page) |
| /flieber-inventory, /flieber-studio, /best-inventory-software and its three child pages, /standardize-vs-pages, /feature-drops, /old-home-page | / | As in Option 1 |
| /book-a-demo-old | /book-a-demo | As in Option 1 |
| /llms.txt, /llms-full.txt, /capabilities.json | /hubfs/flieber-2026/… | The uploaded files |

Not redirected:

- /flieber-vs-inventory-planner: stays unpublished and returns "not found" (cease and desist), so no Flieber page is reachable through a URL carrying that name.
- /ecommerce2: an ad landing page (6,314 views in 12 months), left as is.
- /managed-services, /agencies and /integrations: not redirected; each keeps its URL and gets the new page.

Switch day, in order (about 30 minutes, only after Fabricio's go):

1. Check that https://www.flieber.com/hubfs/flieber-2026/llms.txt, llms-full.txt and capabilities.json open with the Option 2 content.
2. Unpublish (never delete) the old homepage, the old /pricing, the old /agencies, /managed-services and /integrations, and every page in `hubspot/url-redirects.csv` that is still published. Before unpublishing /old-home-page, check whether ads point to it (3,100 views Apr to Sep 2026).
3. Claude moves the 36 drafts to their final URLs and publishes them.
4. Import `hubspot/url-redirects.csv` in Settings > Content > Domains & URLs > URL Redirects.
5. Paste `robots.production.txt` into the robots.txt setting (allows search engines and AI crawlers).
6. Click through the new pages, the Product and Solutions menus, and old URLs such as /omnichannel, /flieber-vs-netsuite and /product to confirm the redirects; confirm /flieber-vs-inventory-planner returns "not found".

Kept live and unchanged: blog, glossary, learn-hub, videos, book-a-demo, free-trial, privacy-policy, service-agreement, /ecommerce2.

After the switch: delete the HubSpot service key "Claude website build" and remove the "HubSpot website build" credential from the Claude environment; retire both Railway previews.

## Decision log

Decisions taken with Fabricio for Option 2, newest first. Option 1's decision log still applies wherever this brief says "as in Option 1".

| Date | Decision |
| --- | --- |
| Oct 5 | Content Briefing (Option 2) and this brief re-issued as 26-10-05, reflecting every decision below |
| Oct 3 | Solutions overlap accepted (a multichannel brand or an agency can also vibe code); /multichannel and /agencies link to /vibe-coders: "Building your own tools with AI? Start from Flieber's data layer →" |
| Oct 3 | Third solution renamed from "Build with AI" to "Vibe coders" (URL /vibe-coders): "Build with AI" read as building something inside Flieber; "Vibe coders" is the term the market recognises, and the page body still serves data teams |
| Oct 3 | The vibe coders page speaks to vibe coders: H1 "Vibe coding your own tools? Start from data that's already right", the lead names Claude, Cursor and ChatGPT, the homepage card and "Why not build it all yourself?" use the term. |
| Oct 3 | Product menu reordered: All features first with the five modules nested under it, a divider, then Integrations, MCP and AI agents and Security & data |
| Oct 3 | ChatGPT confirmed: /before-you-choose question 9 goes back to "Claude, ChatGPT or any other", as in the Content Briefing |
| Oct 3 | Use-case claims confirmed: the origin check before transfers and backorder settings at the product and store level; the /features backorders card and question changed from "settings by channel" to match |
| Oct 3 | Trial pricing needs no sales step: the price is calculated from real data and shown automatically after onboarding |
| Oct 3 | Use-case topics kept as written; HubSpot had no AEO prompts to check them against |
| Oct 3 | New pages: /vibe-coders (third solution), ten use-case pages kept out of the menus, /integrations with six system pages, /managed-services and /who-we-are with new copy |
| Oct 3 | "Who we are" in the navigation and footer goes to /who-we-are; Integrations joins the Product menu and footer; Vibe coders joins the Solutions menu and footer; MCP and AI agents joins the footer |
| Oct 3 | Self-Serve price: "Flieber shows your price as soon as onboarding is done, before you pay anything" replaces the Content Briefing's "We share your price during your trial, or on a demo if you prefer"; homepage Try it and /pricing match |
| Oct 3 | Data layer pricing being defined (Fabricio and Karyna): no price wording for it until approved |
| Oct 3 | /mcp: the MCP URL and per-assistant setup become public once engineering supplies them (decided after Karyna's review); until then step 1 reads "Copy your connection details from Connect Apps in Flieber" |
| Oct 3 | Out of scope for now: a case studies page (no case material with numbers yet) |
| Oct 2 | New /mcp page (MCP and AI agents) in the Product menu, between All features and Security & data; /agents links to it from the MCP server line |
| Oct 2 | Options converge on a final version: Option 2 sharing the homepage H1 and the offer labels with Option 1 is accepted |
| Oct 2 | /before-you-choose question 9: "any MCP-compatible agent, such as Claude" (reversed Oct 3) |
| Oct 2 | /before-you-choose question 17 answered for Flieber: it consolidates 3PL inventory data, connects to an existing ERP, WMS or MRP and does not replace them |
| Oct 2 | Offer labels back to Option 1's: "Let our planners help you run it" and "Run it yourself" |
| Oct 2 | Security moves from the top navigation into the Product menu as "Security & data"; five items before the buttons; collapse at 1140px |
| Oct 2 | The three collaboration cards are static and share one style; no card is emphasized |
| Oct 2 | Homepage H1 "Before running your brand with AI, someone has to keep the data true", with the new subhead; /features intro rewritten to match |
| Oct 2 | /before-you-choose replaces the named comparison pages; three redirect to it; /flieber-vs-inventory-planner gets no redirect (cease and desist); /ecommerce2 not redirected |
| Oct 2 | How Flieber is built becomes a scroll-driven stacked six-layer section after legora.com; it describes the mechanism, never names a module and links only to /security |
| Oct 2 | Homepage Modules section: five question-led cards; Collaborative AI runs across the modules and is not a sixth one |
| Oct 2 | The data layer can be bought alone, priced like Self-Serve on features enabled and data volume; /pricing gets one line saying so |
| Oct 2 | Five module pages under /product/; every module page links to the other four and to /features |
| Oct 2 | Solutions by type of business only: /multichannel (replaces /omnichannel and /ecommerce) and /agencies; no pages by need |
| Oct 2 | /features regrouped by module; "Reports and dashboards" and "Sales order routing" added; "Can I buy only the data layer?" added first to the FAQ |
| Oct 2 | Homepage gains the logo row under the hero, the founder statement and the security strip |
| Oct 2 | What Option 2 does not copy from Legora: demo-only calls to action, branded module names, security certifications, a "latest releases" section |
| Oct 2 | Option 2 built in parallel on its own branch and Railway service, hidden from search engines; Option 1 untouched; nothing in HubSpot until an option is elected |

Choices made while building, open to change:

- "Connect your sales channels and inventory" has no card copy in the Content Briefing; its card uses the approved integrations wording.
- "Data health" is in no Option 2 list, but /features keeps every Option 1 card, so it stays in the Data layer section of /features (not on the data layer page, which follows the brief's list).
- The homepage module answers are reused as the /features section leads, on the module pages' "Works with" cards, on /agents and in the llms files.
- /mcp agents row: the names are shown as text chips, not brand logos, until approved logo files are supplied. The "Waiting for your approval" tag appears on the purchase order example, the only one whose action waits for approval.
- Use-case links on /features: each use-case page is linked from the card(s) its points rely on, as "Use case: [name] →".
- Integration page questions: "Is the [system] integration native?" is answered "Yes." plus the availability line, or, for assisted systems, "No. It's an assisted integration, set up and customized by Flieber's team on paid plans."; "What does Flieber do with [system] data?" is built from the read and send columns.
- The use-case closing "This is one part of what Flieber does" is shown as the closing H2, without its period (house style).
- Links to /managed-services: "Managed Services →" under Door 1; the offer names on the homepage and /pricing cards link to it.
- /who-we-are closes with the two buttons only, as the brief asks; the founder statement and quotes are copied from the homepage at build time so they never drift.
- /mcp keeps the link to the MCP docs (customer login required) until engineering publishes the public setup steps.
- Small labels not in the Content Briefing: "Use case", "Features", "Examples", "Questions", "Modules", "Integration", "One click", "Set up for you", "Planners", "Fit", "One product", "Founder", "Beliefs", "Numbers", "Contact", "Build or buy" above the new pages' H2s; "Common uses" kicker "Use cases"; "MCP", "Examples", "Prompts", "Capabilities", "Setup", "Data layer" and "Questions" above the /mcp H2s; "Decides", "Prepares and carries out", "Advises" on the collaboration cards; "In their words" above the quotes on the solutions pages.

## Build and switch checklist

No specification decisions are open. This checklist tracks what remains before Option 2 could be switched on.

Before an option is elected:

- [ ] Fabricio's photo for the founder section (a monogram marked `[FOUNDER PHOTO]` stands in on the preview)
- [ ] Fabricio confirms the claims first used in Option 2: "Proprietary algorithms, not language models", "more than 1,000 commerce brands" in the planning engine and planner copy, the /multichannel "For most brands" line and the regional markets example for sales order routing
- [ ] Fabricio reviews "What we believe" on /who-we-are (drawn from the May 2026 strategy document)
- [ ] Fabricio (with engineering) makes the MCP URL, sign-in flow and per-assistant setup steps public for /mcp and /vibe-coders
- [ ] Fabricio expands the use-case pages, which are short for pages meant to rank (lead, three or four points, two requests, two questions)
- [ ] Fabricio and the team compare both previews and elect one option

If Option 2 is elected:

- [ ] Upload the Option 2 templates to HubSpot and create the 36 drafts under /new-site-2026-b/
- [ ] Upload Option 2's llms.txt, llms-full.txt and capabilities.json to `flieber-2026`, replacing Option 1's
- [ ] Update `hubspot/CUTOVER.md` with the draft IDs
- [ ] Fabricio reviews the drafts in HubSpot Preview (fonts, logos, the six-layer animation, the Product and Solutions menus, phone menu, any HubSpot banner or chat widget)
- [ ] Check whether ads point to /old-home-page before it is redirected
- [ ] Fabricio gives the go; run the switch steps above
- [ ] Update the Technical Briefing for the winning option only

Product and engineering, outside the site (as in Option 1):

- [ ] Replace the `ask_flieber` MCP tool description, which still says "read-only by default"
- [ ] Update the Confluence pages on product capabilities, AI Lab planning actions and what the AI Lab agent can call: they still say Flieber does not submit POs to suppliers, write to marketplaces or write to NetSuite
- [ ] Update the Feature Overview PDF (Sep 7): add data health, sales order routing and reports and dashboards; remove "run part or all of the planning process" from managed services; TikTok Shop native; Apparel Magic assisted

On the HubSpot pages that stay live:

- [ ] Free-trial page: "Integrate any system or spreadsheet" contradicts the rule that assisted integrations come only with a paid plan
- [ ] Book-a-demo page: restyle header, footer and copy to the new site; keep the form and CRM scripts
- [ ] Blog: restyle header and footer; fix the footer address to New York, NY 10016

After the switch:

- [ ] Delete the HubSpot service key and the Claude environment credential
- [ ] Retire both Railway previews

Maintenance rules after launch (not open items):

- MCP endpoint and auth method stay behind the customer login
- The direct-to-API MCP client goes on /features and /agents only once it ships
- A Nixtla accuracy report, if delivered, is linked as "measured with Nixtla"
- "On request" tags come off /features and capabilities.json as features become generally available
- /flieber-vs-inventory-planner stays unpublished and is never redirected
