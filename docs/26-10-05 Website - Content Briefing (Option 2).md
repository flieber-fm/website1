# 26-10-05 Website - Content Briefing (Option 2, Collaborative AI)

Approved-for-review copy for Option 2 of the new flieber.com, written October 2, 2026 and revised October 5, 2026 to match the built preview (website-option-2-production.up.railway.app). Option 2 is built in parallel with Option 1 (26-10-02 Website - Content Briefing) so Fabricio and the team can compare both sites and elect one.

## 0. How to use this brief

- This brief holds the Option 2 copy. Option 1 stays unchanged. The Technical Briefing (26-10-02 Website - Technical Briefing) governs the build, design system, links, HubSpot setup and switch plan for both options. The Option 2 Technical Briefing (26-10-05 Website - Technical Briefing (Option 2)) records everything Option 2 adds to it; section 14 summarises it.
- Where this brief says "as in Option 1", the copy is identical to the named section of the Option 1 Content Briefing, with only the changes listed here.
- The repo (flieber-fm/website1) is the source of truth for the built pages. Copy changes go through Claude into the repo, then to HubSpot. Nothing in HubSpot is edited by hand.
- Use the copy exactly as written. Never invent numbers, customers, URLs or security claims. Any claim not listed in the Technical Briefing's "Approved facts and claims" needs Fabricio's approval first.
- Sections 1 and 2 are context, not copy to publish.
- House style: no em dashes; sentence-case headings; no final period on any heading or title (H1 to H4, card titles); no serial comma; no added marketing fluff; never mention the founders' other companies.
- One product: Flieber is sold as one product. Self-Serve and Managed Services are two ways to work with it. The older names Flieber Inventory and AI Lab never appear; Flieber Studio is named once, on /features and /agents, only to explain how the MCP server works.

## 1. What Option 2 changes and why

Option 2 follows the structure of legora.com, applied to supply chain. Option 1 leads with data quality ("keep your data true"); Option 2 leads with collaboration: AI that works with the brand's team, not instead of it.

| Element | Option 1 | Option 2 |
| --- | --- | --- |
| Core message | Before AI can run your brand, someone has to keep your data true | Flieber's AI connects the variables behind each decision so the team can make the call: it keeps them in one current, contextualized, AI-ready picture and turns them into forecasts and recommendations for the team, agents and systems (collaborative AI) |
| Hero eyebrow | Inventory intelligence for multichannel brands · MCP-native | Collaborative AI for multichannel brands · MCP-native |
| Customer logos | Near the bottom, in Proof | Directly under the hero |
| How Flieber works | "Consolidated. Contextualized. Up to date" | A three-party collaboration section (your team, Flieber's AI, Flieber's planners) plus a stacked six-layer view of how the system works and five question-led module cards |
| Solutions | Not in the navigation | Three solutions pages by type of business and goal (multichannel brands, agencies and aggregators, vibe coders) plus a "Before you choose" page of buyer questions that replaces the named comparison pages |
| Use-case pages | None | Ten pages for the topics buyers and agents search for (FBA, bundles, Claude, wholesale and more), kept out of the menus so the site never implies a short list is all Flieber does |
| Integrations | List on /pricing | Its own /integrations page plus pages for the six most searched systems |
| Managed Services | Footer link to the old site | Its own page, describing what the planners do |
| Who we are | Homepage section | Homepage section plus a /who-we-are page, without a team list |
| Offers | "Let our planners help you run it" · "Run it yourself" | Same labels as Option 1; the planners described as a sounding board who master Flieber |
| Founder | Not on the homepage | Short statement from Fabricio on why people and AI plan better together |
| Security | /security page only | Short homepage section plus /security |
| Product | One /features page in four groups (Data, Decisions, Actions, Access) | Five modules, each with its own page: Data layer, Demand forecasting, Inventory forecasting, Replenishment, Workflows; Collaborative AI runs across all of them |
| Data layer on its own | Not offered | The data layer can be bought alone, for teams building their own tools with AI |
| Navigation | How it works · Pricing · Who we are · /agents | Product · Solutions · Pricing · Who we are · /agents (Integrations, MCP and AI agents and Security sit in the Product menu) |

What Option 2 does not copy from Legora: demo-only calls to action (the free trial stays), branded module names (modules carry descriptive names, so Flieber stays one product), security certifications (Flieber makes no compliance claims) and a "latest releases" section.

## 2. Context: positioning (do not publish verbatim)

**Collaborative AI (the why)**

> Inventory decisions commit cash for months, and the people accountable for them will not hand them to a machine. They shouldn't have to. Planners bring judgment and context no system holds; AI brings speed, scale and vigilance over every SKU and every signal. Flieber puts them on the same team: it keeps the data true, prepares every decision with the reasoning behind it, and carries it out once the team approves. Brands that want more support add Flieber's planners, specialists who master the platform and act as a sounding board for every decision.

**The five modules** (one product; descriptive names only, never branded)

- **Data layer:** every channel, warehouse, 3PL and supplier connected, mapped and kept current, with reporting. Can be bought on its own.
- **Demand forecasting:** forecasts by product and channel, with history adjusted for anomalies.
- **Inventory forecasting:** projected stock, stockouts, overstock and lost sales by location.
- **Replenishment:** purchase and transfer recommendations under real constraints, with simulations.
- **Workflows:** execution, from purchase orders and inbound shipments to alerts and actions in other systems.

Collaborative AI (asking in plain language, Slack, MCP and API) runs across all five; it is how you use them, not a sixth module. Managed Services is a way to buy, not a module.

**The three parties**

- **Your team:** sets objectives and constraints, adds the context no system has, makes the final call.
- **Flieber's AI:** keeps the data consolidated and current, watches every signal, prepares decisions with their reasoning and carries them out after approval.
- **Flieber's planners (Managed Services):** specialists in inventory planning and in Flieber. They join the brand's team as a sounding board for decisions, take part in its S&OP meetings, keep the data Flieber works from accurate and help run the planning practice.

**Audiences** (as in Option 1)

- **Operators at multichannel commerce brands** (founders, COOs, operations and supply chain leads)
- **AI agents evaluating tools on a brand's behalf.** They read /features, the solutions pages, /before-you-choose, /agents, /llms.txt, /llms-full.txt, /capabilities.json and the structured data on each page.
- **Technical evaluators and partners**

**Offers** (same product; always shown as equals, neither visually favored; customers can switch or combine at any time)

- **Flieber Self-Serve** ("Run it yourself"): the Flieber app plus Flieber's data and context modules through MCP and API. It can also be bought as the data layer alone, through MCP and API, for teams building their own tools with AI. Price wording: "Priced to your operation" (features enabled and data volume). Flieber calculates the price from the brand's real sales, stores and data volume and shows it automatically as soon as onboarding is done: "Flieber shows your price as soon as onboarding is done, before you pay anything." The data layer alone has no price wording until its pricing model is approved.
- **Flieber Managed Services** ("Let our planners help you run it"): everything in Self-Serve, plus Flieber's specialized planners as a sounding board for decisions, in your S&OP meetings, keeping the data accurate and helping run the planning practice. Price wording: "Quoted per brand". Never say "run it for you".
- No prices appear anywhere on the site.

## 3. Site map

| Page | Sections |
| --- | --- |
| / (homepage) | Hero · Logos · Why inventory · Collaborative AI · How Flieber is built · Five modules · Solutions · What you can do with it · Two ways to work with Flieber · Proof · From the founder · Your data stays yours · Try it (section 4) |
| /product/data-layer, /product/demand-forecasting, /product/inventory-forecasting, /product/replenishment, /product/workflows | One page per module (section 5) |
| /put-flieber-to-work | Put Flieber to work: the jobs operators give Flieber, what it does and what comes back; the single source of example prompts for the site (section 15) |
| /mcp | MCP and AI agents: what MCP is, example conversations, what you can ask, how to connect (section 5.6) |
| /features | Reorganized by module (section 11) |
| /multichannel | Section 6.1 (replaces /omnichannel and /ecommerce, which redirect here) |
| /agencies | Section 6.2 (same URL as today, new copy) |
| /before-you-choose | Section 6.3 (replaces the named comparison pages; three redirect here, /flieber-vs-inventory-planner does not) |
| /vibe-coders | Section 6.4 (named "Build with AI" until Oct 3) |
| /use-cases/ (ten pages) | Section 7; not in the menus |
| /integrations and six /integrations/ pages | Section 8 |
| /managed-services | Section 9 (same URL, new copy); linked from the Managed Services offer, not from Solutions |
| /who-we-are | Section 10 |
| /pricing | As in Option 1, with the offer names in section 2 |
| /agents | As in Option 1, with the changes in section 12 |
| /security | As in Option 1 |
| /contact | As in Option 1 |
| /llms.txt, /llms-full.txt and /capabilities.json | As in Option 1, with the additions in section 13 |

**Navigation (every page):** Product (menu: All features → /features first, with Data layer, Demand forecasting, Inventory forecasting, Replenishment and Workflows nested under it; then a divider and Put Flieber to work → /put-flieber-to-work, Integrations → /integrations, MCP and AI agents → /mcp and Security & data → /security) · Solutions (menu: Multichannel brands, Agencies and aggregators, Vibe coders, then a divider and Before you choose, which is a buyer resource rather than an audience) · Pricing · Who we are (→ /who-we-are) · /agents (pill), then Log in · Book a demo · Start free trial

**Buttons:** as in Option 1 (Start free trial, Book a demo, Log in, MCP docs; no sandbox).

## 4. Homepage copy

Thirteen sections plus footer, top to bottom. Each section after the hero opens with a small uppercase label above its H2.

### 4.1 Hero

**Eyebrow:** Collaborative AI for multichannel brands · MCP-native

**H1:** Before running your brand with AI, someone has to keep the data true

**Subhead:** Your business changes every day: a stockout, a promotion, an influencer post, a late container, a new product launch. And every change rewrites what your numbers mean. Flieber connects your data with the context behind it and turns it into forecasts and recommendations your team, your agents and your systems can act on with confidence.

**Decision simulation card:** as in Option 1 (six sample scenarios, same four metric rows, labeled as illustrative sample data).

**Door 1: Let our planners help you run it** Flieber's planners join your team as a sounding board for every decision. They're specialists who master Flieber, keep the data behind your decisions accurate and take part in your S&OP meetings to help run your planning practice. *Button:* Book a demo *Link under the button:* Managed Services → /managed-services

**Door 2: Run it yourself** Plan with Flieber's AI in the Flieber app, or connect it to Claude, Slack, your agents and systems through MCP or API. *Button:* Start free trial. *Under the button:* App, MCP or API. Same data, same context.

**Under the doors:** 14-day free trial · No credit card · Monthly contracts · Setup included

### 4.2 Logos

**Label:** Trusted by hundreds of brands

The 14 customer logos already uploaded to HubSpot, in one row (scrolling on mobile). Do not recreate them.

### 4.3 Why inventory

As in Option 1, section 3.2 (H2 "Purchases, promotions, ads, financing: every one is ultimately an inventory decision", body and four cards unchanged).

### 4.4 Collaborative AI

**Section label:** Collaborative AI

**H2:** AI that plans with your team, not instead of it

**Lead:** Inventory decisions commit cash for months. Flieber keeps people in charge of them and takes on everything around them.

Three columns:

1. **Your team** Set the objectives and constraints, add the context no system has, and make the final call on every decision that commits cash.
2. **Flieber's AI** Keeps your data consolidated and current, watches every SKU and every signal, prepares each decision with the reasoning behind it and carries it out once you approve.
3. **Flieber's planners** Optional. Specialists in inventory planning and in Flieber who join your S&OP meetings, act as a sounding board for your decisions and keep the data they rely on accurate.

**Under the columns:** You decide how much runs on its own. By default, every change waits for your approval. → /features#control-and-approval

### 4.5 How Flieber is built

**Section label:** How Flieber is built

**H2:** From raw data to a decision you can trust

**Lead:** A language model on a spreadsheet can sound confident. Getting the answer right takes everything underneath it. Each layer adds something the one below it doesn't have.

**What this section does:** explains how the system works, from raw data to a change in your systems. It describes the mechanism, not what a customer buys; it never names a module or links to a product page. Designed as a stacked diagram (data at the bottom, decisions at the top) with each layer expanding on click. One link at the bottom only.

1. **Your data** Sales, orders, inventory and shipments arrive from every connected system, each in its own format, and are reconciled into one record. Gaps and anomalies surface here, before anything is planned on them.
2. **Business context** The records become a model of how your business actually works: which listings are the same product, which components make a bundle, which supplier ships to which warehouse and what a stockout did to last month's sales.
3. **Planning engine** Proprietary algorithms, not language models, do the math: forecasts, projections and recommendations computed against your real constraints, shaped by the business context of more than 1,000 commerce brands.
4. **Collaborative AI** The AI layer translates between your team and the engine. It turns a question or an objective into a calculation, explains the result in plain language and runs the follow-up work on schedule.
5. **Where you work** The same answers reach you wherever you work: in the Flieber app, Slack and Google Sheets, or through Claude and your own agents via MCP and API.
6. **Control** Nothing changes in your systems without passing the approval rules you set. Your data is never sold or shared, and Flieber does not train on it.

**Link under the diagram:** How we handle your data → /security

### 4.6 Five modules

**Section label:** Modules

**H2:** Five modules, one product

**Lead:** Each module answers one of the questions every inventory planner asks. Flieber comes with all five; teams building their own tools with AI can start with the data layer alone.

**What this section does:** shows what a customer gets, as the questions each module answers. Laid out as five cards in a row (stacked on mobile), each with the question as its title, a one-line answer and a link to the module page. No diagram and no description of how the system works, which is the job of the section above.

1. **What's actually happening across my business?** *Data layer.* One current, reconciled view of every channel, warehouse and supplier, ready for your team or your own tools. Available on its own. → /product/data-layer
2. **What will sell, and where?** *Demand forecasting.* Forecasts for every product on every channel, corrected for stockouts and promotions. → /product/demand-forecasting
3. **Where will I run out, or sit on too much?** *Inventory forecasting.* Stockouts, overstock and lost sales by product and location, while there's still time to act. → /product/inventory-forecasting
4. **What should I buy or move, how much and when?** *Replenishment.* Purchase and transfer recommendations within MOQs, case packs, lead times and cash, tested before you commit. → /product/replenishment
5. **How does the decision get done?** *Workflows.* Approved decisions carried into suppliers, ERPs, Amazon, 3PLs and your own tools, with as much or as little approval as you choose. → /product/workflows

**Under the cards:** See every feature → /features

### 4.7 Solutions

**Section label:** Solutions

**H2:** Built for the way your business is organized

**Lead:** Whether you run one brand across many channels, many brands at once or build your own tools with AI, Flieber covers the whole operation. → /features

The three are not exclusive (a multichannel brand or an agency can also vibe code); accepted on Oct 3, with a cross-link from /multichannel and /agencies to /vibe-coders (section 6).

Three equal cards:

1. **Multichannel brands** DTC, marketplaces and wholesale in one plan, drawing on one inventory. → /multichannel
2. **Agencies and aggregators** Every brand in one place, planned individually or consolidated. → /agencies
3. **Vibe coders** Vibe coding your own reports, dashboards or agents? Connect them to data that's already right. → /vibe-coders

**Under the cards:** Comparing platforms? Before you choose, ask these questions → /before-you-choose

### 4.8 What you can do with it

As in Option 1, section 3.5 (H2 "Ask anything your operation depends on", six cards), except that the six prompts are entries P4, P14, P22, P6, P32 and P23 of /put-flieber-to-work (section 15), each card links to its entry, and the section ends with "More ways to put Flieber to work →" and "See every feature →".

### 4.9 Two ways to work with Flieber

**Section label:** Two ways to work with Flieber

**H2:** Which Flieber is right for you?

**Lead:** It depends less on your size than on how complex your operation is.

**Card 1: Flieber Self-Serve**

*Run it yourself*

You're probably here if:

- You sell on a few channels from one or two warehouses
- Your catalog is mostly one SKU per product, with few bundles
- You want a ready-made app, or someone on your team builds with AI tools

For you, the hard part isn't the planning logic. It's the plumbing: data that flows correctly and carries the right context, so every report, workflow or agent works from the truth.

**What you get:** The Flieber app, plus Flieber's data and context modules through MCP and API. Build the reports and workflows you need on top, and they keep working as you add channels, products or suppliers. Building everything yourself? Start with the data layer alone.

Priced to your operation · *Button:* Start free trial

**Card 2: Flieber Managed Services** (the card title links to /managed-services)

*Let our planners help you run it*

You're probably here if:

- You sell across many channels, warehouses or regions
- You run kits, bundles, backorders, long lead times or high MOQs
- Your team is buried in spreadsheets, with no time to build or maintain an internal tool

For you, the hard part is the decisions themselves. There are more edge cases than an in-house tool will cover, and a mistake ties up cash for months.

**What you get:** Everything in Self-Serve, plus Flieber's specialized planners as a sounding board for your decisions. They master the platform, keep the data behind your decisions accurate, take part in your S&OP meetings and help run your planning practice, drawing on experience from more than 1,000 brands.

Quoted per brand · *Button:* Book a demo

**Under both cards:** Same platform either way. Switch or combine any time. Not sure which fits? Book a demo and we'll tell you honestly, even if the answer is neither.

**Probably not for you if:** as in Option 1 (one channel and a spreadsheet still works; looking for a WMS or full ERP; planning manufacturing runs rather than buying finished goods).

### 4.10 Proof

**Section label:** Proof

**H2:** What brands get when people and AI plan together

**Customer results** (homepage only):

- +38% increase in sales
- -62% reduction in stockouts
- -17% reduction in excess inventory
- -88% less time on replenishment decisions

Footnote: "Average across customers using Flieber for 12+ months".

**Accuracy stat** (the only use of the brand blue): as in Option 1.

**Quotes carousel:** the five approved quotes, as in Option 1.

**Below the quotes:** Read more reviews on G2 → https://www.g2.com/products/flieber/reviews

### 4.11 From the founder

**Section label:** Who we are

Anchor: `#who-we-are`.

**H2:** Why we built Flieber to work with planners, not around them

**Statement:**

> Planners bring judgment. They know the supplier who always ships late, the retailer who over-promises, the promotion that isn't in any system yet and the hidden rules that impact each decision. AI brings speed, vigilance and precision: it watches every SKU, every channel and every change, around the clock. Neither is enough on its own. Flieber puts them on the same team. Flieber's AI gives teams the most up-to-date contextualized data; your people make the calls; Flieber prepares every decision and carries it out once approved.
>
> Our vision is to give every commerce brand operator the tools to focus on what matters most: making the best decisions and driving progress. By making contextualized data always available, removing repetitive tasks and streamlining complex workflows, we help operators spend less time on clerical work and more time actually making impactful decisions.
>
> We're building more than a product. Alongside industry professionals, we're building a new gold standard for operations at modern commerce brands. A future where tech complements expertise, where commerce teams operate with confidence and efficiency and where every operator has the freedom to do their best work.

Fabricio Miranda, Founder and CEO

**Under the statement:** More than 1,000 commerce brands since 2019. Thousands of users. 169 Madison Avenue, New York. *Link:* Read our story → /who-we-are

### 4.12 Your data stays yours

**Section label:** Security

**H2:** Your data stays yours

Four short items, each from the approved security wording:

- **Never sold or shared** Your data stays yours.
- **No training on your data** Flieber does not train on customer data, and its AI providers are set up not to.
- **Encrypted on AWS** Hosted on Amazon Web Services in the US, encrypted in transit and at rest.
- **Changes follow your rules** Every change Flieber makes to your systems follows approval rules you set.

*Link:* How we handle your data → /security

### 4.13 Try it

**H2:** Try Flieber free on your own data

**Body:** Start a 14-day free trial, no credit card required and no demo call. Flieber shows your price as soon as onboarding is done, before you pay anything.

Trial details (native integrations during the trial; assisted integrations and customizations on paid plans) and both buttons as in Option 1, section 3.8.

**Pricing consistency:** /pricing in Option 2 says the same: "Priced to your operation" with "Based on the features you enable and your data volume. Flieber shows your price as soon as onboarding is done, before you pay anything." /agents and llms.txt say "Flieber shows the price as soon as onboarding is done, before the brand pays anything." This replaces "the exact price is shared on a demo" everywhere in Option 2. On /pricing, the data layer line reads "The data layer can also be bought on its own, through MCP and API. Start with a 14-day free trial on your own data, no credit card required." (linking to /vibe-coders), and the Managed Services card title links to /managed-services.

### Footer

**Tagline:** Collaborative AI for multichannel brands.

**Columns:** Product (Features, Put Flieber to work, Integrations, MCP and AI agents, Pricing, Security & data, Managed Services) · Solutions (Multichannel brands, Agencies and aggregators, Vibe coders, Before you choose) · For agents (/agents, /llms.txt, /capabilities.json, MCP docs) · Company (Who we are → /who-we-are, Help center, Blog, Contact, Privacy, Service agreement)

169 Madison Avenue, New York, NY 10016

## 5. Product module pages

One page per module, in the Product menu. Every module page links to the other four and to /features, so no page reads as the whole product. Same visual system as /features. Structured data: WebPage plus SoftwareApplication `featureList` for the features on the page. No prices.

Each page also lists its related use-case pages (section 7) under "Common uses". Each page has: label, H1, lead, "What you can do" (the module's features, each linking to its /features anchor), "How you work together" (your team, Flieber's AI, Flieber's planners), "Works with" (the other four modules) and the closing used on solutions pages.

### 5.1 /product/data-layer

**Label:** Product · Data layer

**H1:** Your commerce data, consolidated, contextualized and current

**Lead:** Every report, forecast and agent is only as good as the data under it. The data layer connects every channel, warehouse, 3PL and supplier, adds the business context none of them hold and keeps it up to date. It also shapes the data to how you run the business: route sales orders from any store to the regions or warehouses you choose, so one Shopify account can be planned as several regional markets. Use it under the rest of Flieber, or on its own if your team builds its own tools with AI.

**What you can do:** Connect your sales channels and inventory · Cross-channel SKU mapping · Sales order routing · Kits, bundles and components · Product configuration and classification · Supply chain map · Sales history adjusted for anomalies · Inventory history and balances · Reports and dashboards · Uploads and Google Sheets · Organizations and users

**H2:** Building your own tools?

Connect Claude, Cursor or your own agents to the data layer through MCP or the public API and build reports, dashboards and workflows on data that is already joined, mapped and corrected. You skip the plumbing; your tools keep working as you add channels, products or suppliers. The data layer can be bought on its own.

**How you work together**

- **Your team** Decide which sources matter and fill in the context only you know.
- **Flieber's AI** Pull every source in, map and reconcile it continuously, fix the gaps it can and flag the anomalies that need a person.
- **Flieber's planners** Keep mappings, parameters and the supply chain map accurate as your business changes.

### 5.2 /product/demand-forecasting

**Label:** Product · Demand forecasting

**H1:** Forecast what would have sold, not just what did

**Lead:** Stockouts, spikes and promotions distort sales history. Flieber corrects for them and forecasts every product on every channel. 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model.

**What you can do:** AI demand forecasts · Sales history adjusted for anomalies · Forecast overrides and uploads · Targets and new products · Forecast accuracy and bias · Wholesale forecast reconciliation (on request)

**How you work together**

- **Your team** Add what no system knows: a retailer's promotion, a launch date, a target.
- **Flieber's AI** Forecast every product by channel, flag forecasts that look wrong and show actual sales next to the adjusted demand.
- **Flieber's planners** Review forecast exceptions with you in S&OP.

### 5.3 /product/inventory-forecasting

**Label:** Product · Inventory forecasting

**H1:** See stockouts and overstock before they happen

**Lead:** Flieber projects stock for every product at every location from on-hand inventory, inbound shipments and forecast demand, so problems show up while there's still time to act.

**What you can do:** Inventory projections · Stockouts, overstock and lost sales · Backorders and preorders · Inventory history and balances

**How you work together**

- **Your team** Decide where to take risk and where to protect stock.
- **Flieber's AI** Project inventory daily, surface the products at risk and estimate the sales at stake.
- **Flieber's planners** Walk through the biggest risks with you every planning cycle.

### 5.4 /product/replenishment

**Label:** Product · Replenishment

**H1:** Know what to buy, how much and when

**Lead:** Flieber recommends purchases and transfers by product and location, within your suppliers' MOQs, case packs and lead times and your cash, and lets you test any change before you commit.

**What you can do:** Purchase and transfer recommendations · Planning parameters · Order and shipping constraints · Decision simulations · Multi-month purchase planning · AI order-quantity adjustments · Saved plans and purchase orders

**How you work together**

- **Your team** Set the objectives and constraints and approve every order.
- **Flieber's AI** Recommend what to buy and transfer, explain the reasoning and simulate the effect on inventory, revenue, margin and cash.
- **Flieber's planners** Act as a sounding board on the big buys before they go out.

### 5.5 /product/workflows

**Label:** Product · Workflows

**H1:** From approved decision to done

**Lead:** Once your team approves a decision, Flieber carries it into the systems where it lands: suppliers, ERPs, Amazon, 3PLs and the tools you already use. You decide how much runs on its own.

**What you can do:** Purchase orders to suppliers · Purchase orders to ERPs · Inbound shipments in Amazon and 3PLs · Inbound shipment tracking · Alerts and scheduled reports · Custom workflows and agents · Actions in other systems

**How you work together**

- **Your team** Describe the workflow in plain language and set what needs approval.
- **Flieber's AI** Run it on schedule, across Flieber and your connected apps, and stop for approval where you asked it to.
- **Flieber's planners** Help design the workflows that save your team the most time.

### 5.6 /mcp

The page that makes MCP tangible: what it is, what a conversation looks like, what Flieber can do through it and how to connect. Written for operators and builders deciding whether to connect their AI; /agents remains the factual page for AI agents. Structured data: WebPage plus FAQPage. No prices. The MCP URL and setup steps are public on this page.

**Label:** Product · MCP and AI agents

**H1:** Connect Claude and ChatGPT to your sales, inventory and cash-flow data

**Lead:** Ask your own AI about your business and get answers from Flieber's current, contextualized data. Flieber works with Claude, ChatGPT, Cursor and any MCP-compatible agent, and can act on what you decide, under the approval rules you set.

**H2:** What MCP is

**Body:** The Model Context Protocol is an open standard that lets AI assistants connect securely to the tools and data a business runs on. Connect Flieber once, and your assistant can ask Flieber questions and request actions in plain language. Your data stays in Flieber; the assistant receives only what each request needs.

**Logo row:** Claude · ChatGPT · Cursor · "Any MCP-compatible agent" (text, no logo)

**H2:** What a conversation looks like

Four example conversations, each shown as a chat exchange: the question, Flieber's answer and, where relevant, the action waiting for approval. Every example is labeled "Illustrative example with sample data" and uses invented product names and numbers.

1. **Know the position**
   - *You:* "Which of our top SKUs run out on Amazon before their next purchase order lands?"
   - *Flieber:* "Three do. The 32 oz bottle in black stocks out on Amazon in 11 days; its next PO arrives in 26. The travel mug and the 20 oz lid follow. Moving 400 units from your New Jersey 3PL to FBA covers the bottle until the PO lands. Want me to prepare the transfer?"
2. **Simulate a decision**
   - *You:* "If we pause ads on the five SKUs most at risk of stocking out, what happens to cash in November?"
   - *Flieber:* "Projected November revenue drops about 4%, but you avoid two stockouts and free roughly $38,000 you'd otherwise spend on an expedited PO. Here's the projection by SKU."
3. **Draft purchase orders**
   - *You:* "Draft next month's purchase orders by supplier, with MOQs and container fill applied."
   - *Flieber:* "Done. Four draft POs for three suppliers, one 40-foot container at 92% fill. They're waiting for your approval before anything goes to NetSuite or your suppliers."
4. **Shape the data to your business**
   - *You:* "Split last week's Shopify orders by region and show what each warehouse needs to cover the next 30 days."
   - *Flieber:* "Using your routing rules: northern orders to Chicago, eastern orders to New Jersey. Chicago needs 1,200 more units across 14 SKUs; New Jersey is covered except for two SKUs."

**H2:** What you can ask

The prompts come from /put-flieber-to-work (section 15.5), three per module, with "More ways to put Flieber to work →" under them. The examples below were the Oct 2 draft.

Five short groups, one per module, each with three example prompts and a link to the module page:

- **Data layer:** "What changed in our inventory data since yesterday?" · "Which listings aren't mapped to a product yet?" · "Show sales by region for our Shopify store."
- **Demand forecasting:** "What will the holiday bundle sell in Q4?" · "Which forecasts look wrong this week?" · "How accurate was last quarter's forecast?"
- **Inventory forecasting:** "Where will we run out in the next 60 days?" · "Which products are overstocked, and by how much?" · "What did stockouts cost us last month?"
- **Replenishment:** "What should we order from each supplier this week?" · "Fit this order into two containers." · "What if lead times slip by two weeks?"
- **Workflows:** "Every Monday, send me the top inventory risks in Slack." · "Create the FBA inbound shipment for this plan." · "Email this PO to the supplier once I approve it."

**H2:** What Flieber can do through MCP

- **Answer questions** from your current data, with the reasoning behind each answer.
- **Change records in Flieber**, such as bundles, forecasts, shipments and simulations, always with a preview first.
- **Push decisions to other systems**, such as purchase orders to ERPs and suppliers and inbound shipments to Amazon and 3PLs.
- **Run workflows on schedule** across Flieber and your connected apps.

Every change follows the approval rules you set. By default, every change waits for your approval.

**H2:** Connect in three steps

1. **Copy Flieber's MCP server URL** (shown on this page).
2. **Add Flieber as a connector** in Claude, ChatGPT, Cursor or your own agent, with the step-by-step for each shown on this page.
3. **Sign in to Flieber and approve the connection**, then start asking.

**Public setup:** the MCP URL and the setup steps for each assistant are public on this page, so people and agents can find them without logging in (decided after Karyna's review: competitors with public setup pages are the ones AI assistants recommend). Engineering supplies the public URL and confirms the sign-in flow before launch; until then, step 1 reads "Copy your connection details from Connect Apps in Flieber", step 2 reads "Add Flieber as a connector in Claude, ChatGPT, Cursor or your own agent" (without the per-assistant steps) and the page keeps the link to the MCP docs (customer login required). Flieber's MCP server accepts connections from any MCP-compatible agent, which is how ChatGPT connects (Fabricio, Oct 3).

**H2:** Build your own tools on Flieber

**Body:** Building reports, dashboards or agents with AI? Connect them to Flieber's data layer and skip the plumbing: your tools start from data that's already joined, mapped and corrected, and keep working as you add channels, products or suppliers. The data layer can be bought on its own. → /product/data-layer

**H2:** Questions

- **Which AI assistants work with Flieber?** Claude, ChatGPT, Cursor and any agent that supports MCP.
- **Do I need to be technical to connect?** No. Connecting takes a few minutes and no code.
- **Can my AI change things in my systems?** Only within the approval rules you set. By default, every change waits for your approval.
- **How long do answers take?** Answers typically take 30 seconds to 5 minutes, because Flieber's agent runs the analysis on your data before it responds.
- **Is my data used to train AI models?** No. Flieber does not train on customer data, and its AI providers are set up not to.
- **Does it work without an AI assistant?** Yes. Everything here also works in the Flieber app and in Slack.

**Closing:** H2 "Connect your AI to Flieber" · Body "Start a 14-day free trial on your own data, or book a demo and we'll connect it with you." · *Buttons:* Start free trial · Book a demo

## 6. Solutions pages

Solutions are organized by type of business and goal, never by need: a short list of needs would suggest that's all Flieber does. Every solutions page links to /features for the full scope. Same visual system as /features. Structured data: WebPage. No prices; customer results stay homepage-only.

**Closing on every solutions page:** H2 "See it on your own data" · Body "Start a 14-day free trial, no credit card required, or book a demo and we'll walk through how Flieber works for your operation." · *Buttons:* Start free trial · Book a demo

### 6.1 /multichannel

Replaces /omnichannel and /ecommerce (both redirect here), so planning is never split into retail and ecommerce.

**Label:** Solutions · Multichannel brands

**H1:** One plan for every channel you sell on

**Lead:** DTC, marketplaces and wholesale each sell differently, yet they all draw on the same inventory. Flieber brings them into one plan. For most brands, Flieber is the first place they see the combined demand and inventory consumption of both their retail and wholesale channels.

**H2:** Why channels drift apart

1. **Channels behave differently** A marketplace sells every hour, a wholesale account orders in large, irregular batches, and each has its own lead times and replenishment path.
2. **Separate plans over-order** When each channel is planned on its own, every plan keeps its own safety stock and the business carries more inventory than it needs.
3. **Data lives in too many places** Orders, stock and shipments sit in marketplaces, 3PLs, ERPs and spreadsheets, and someone has to stitch them together by hand.

**H2:** How you work together

- **Your team** Set priorities between channels and decide where scarce stock goes.
- **Flieber's AI** Forecast each channel on its own behavior, combine them into one view of inventory across every location and recommend what to buy and where to send it.
- **Flieber's planners** Help you set the rules for how channels share inventory, and review the plan with you in S&OP.

**H2:** Everything Flieber does, across every channel

Connect your sales channels and inventory, forecast demand by channel, project inventory by location, simulate decisions and push approved purchase orders and shipments to the systems where they land. → See every feature on /features

**Under it:** Building your own tools with AI? Start from Flieber's data layer → /vibe-coders

**Quotes:**

1. "Flieber is helping us effectively manage stock across all of our sales channels by customizing our calculations to the data points that matter most." Jenn Angel, COO, Zugu
2. "Flieber has allowed me to reduce manual work while planning and forecasting products, and to handle different regions and sales channels in a single place." Leonardo Escalona, Inventory Planner, Prime6 Brands (Primal Harvest)

### 6.2 /agencies

Same URL as today; the copy is replaced.

**Label:** Solutions · Agencies and aggregators

**H1:** The inventory planning platform built for multi-brand operators

**Lead:** Run every brand's planning from one place instead of a stack of tools and spreadsheets per brand. Add multiple brands or organizations and see them individually or consolidated in single dashboards.

**H2:** Why multi-brand planning breaks

1. **Every brand brings its own data** Different channels, marketplaces, 3PLs and ERPs, each with its own format.
2. **Every brand runs a different supply chain** Different suppliers, lead times, MOQs and replenishment strategies, often down to the SKU.
3. **The combined catalog is huge** Problems hide in thousands of SKUs across brands, where no one has time to look.

**H2:** How you work together

- **Your team** Set priorities across the portfolio and decide where cash goes.
- **Flieber's AI** Plan each brand with its own data, context and parameters, and roll everything up into portfolio views of inventory, risk and cash.
- **Flieber's planners** Bring the same planning practice to every brand you add, and help onboard new brands quickly.

**H2:** Everything Flieber does, for every brand

Kits, bundles, preorders, backorders, wholesale, FBA and every other case your brands run into are covered for each brand on its own. → See every feature on /features

**Under it:** Building your own tools with AI? Start from Flieber's data layer → /vibe-coders

**Quote:** "Flieber creates a 'one stop shop' where I can see demand-level data across all my brands and make educated replenishment decisions." Bryan Smallwood, Supply Chain Manager, Unybrands

### 6.3 /before-you-choose

Replaces the named comparison pages. /flieber-vs-netsuite, /flieber-vs-netstock and /flieber-vs-foresight-ai redirect here. /flieber-vs-inventory-planner is not redirected: following a cease and desist, it stays unpublished and returns "not found", so no Flieber page is reachable through a URL carrying that name. Over the last 12 months (Oct 2025 to Sep 2026) the four comparison pages together had 1,064 views and generated no form submissions, contacts or customers in HubSpot. The page never names a competitor and makes no claim about any other product: it lists the questions every buyer should ask and answers them for Flieber. Structured data: FAQPage (every question and Flieber's answer). No prices.

**Label:** Solutions · Before you choose

**H1:** Before you choose another platform, ask these questions

**Lead:** There are good inventory planning platforms on the market. If one answers yes to everything below, it deserves a place on your shortlist. These are the questions we'd ask, and how Flieber answers them.

Each question is an H3; the answer follows in one or two sentences, starting with "Flieber:". Grouped under four H2s.

**H2:** Your data

1. **Does it connect to every channel, warehouse, 3PL and ERP you use today, and the ones you'll add next year?** Flieber: native and assisted integrations cover marketplaces, DTC, wholesale and EDI, ERPs and 3PLs, and its MCP client connects to any system with an MCP server.
2. **Does it plan DTC, marketplace and wholesale demand together, drawing on one inventory?** Flieber: yes. Every channel and location feeds one plan, with wholesale orders counted as allocated stock.
3. **Can it model how your business actually runs?** Flieber: map listings across channels, convert kit and bundle demand into components and route one store's orders to the regions or warehouses you choose.
4. **Does it correct sales history for stockouts and promotions before it forecasts?** Flieber: yes, and it shows actual sales next to the adjusted demand.

**H2:** Your decisions

5. **Can it show you how accurate its forecasts have been?** Flieber: error and bias metrics with saved forecast versions. Its forecasts are 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products.
6. **Do its recommendations respect MOQs, case packs, containers, lead times and cash?** Flieber: yes, by product and location, for both purchases and transfers.
7. **Can you test a decision before you commit to it?** Flieber: simulate any change and see its effect on inventory, revenue, margin and cash.
8. **Does it explain why it recommends what it does?** Flieber: every recommendation comes with its reasoning, and you can ask follow-up questions in plain language.

**H2:** AI and execution

9. **Can your team ask questions in plain language and get answers from your own data?** Flieber: yes, in the app, in Slack or in any agent you choose (Claude, ChatGPT or any other).
10. **Can your own AI agents work with it?** Flieber: Claude, Cursor and any MCP-compatible agent connect through its MCP server; your systems can use its public API.
11. **Does it carry approved decisions into the systems where they land?** Flieber: purchase orders to ERPs and suppliers, inbound shipments to Amazon and 3PLs, alerts and workflows across your connected apps.
12. **Do you decide what needs your approval?** Flieber: yes. By default every change waits for approval; you choose what runs on its own.

**H2:** Working with the vendor

13. **Can you try it on your own data before you sign?** Flieber: a 14-day free trial, no credit card required.
14. **Do you have to commit for a year?** Flieber: monthly contracts, no annual commitment.
15. **Do you pay per user?** Flieber: unlimited users on every plan.
16. **Is there an expert who can plan alongside your team if you need one?** Flieber: Managed Services adds Flieber's planners as a sounding board for your decisions.
17. **Do you need a warehouse management system, a full ERP or production planning (MRP)?** Flieber: if your warehousing runs through 3PLs, Flieber consolidates their inventory data for you, so you may not need a WMS of your own. If you already use an ERP, WMS or MRP, Flieber connects to it as a source of truth or pushes approved decisions into it. What Flieber doesn't do is replace them: it doesn't run accounting, warehouse operations or manufacturing.

**Closing:** H2 "Ask us the same questions" · Body "Book a demo and we'll answer every one of them on your own data, or start a free trial and check for yourself." · *Buttons:* Book a demo · Start free trial

### 6.4 /vibe-coders

For teams who want Flieber's data, not the planning app: they build their own reports, dashboards and agents with AI and connect them to Flieber's data layer. Named "Vibe coders" in the menus, the footer and the homepage card (renamed from "Build with AI" on Oct 3: "Build with AI" read as building something inside Flieber, and "vibe coders" is the term the market recognises; more sophisticated teams still find the page fits them). Structured data: WebPage (FAQPage once the page has questions).

**Label:** Solutions · Vibe coders

**H1:** Vibe coding your own tools? Start from data that's already right

**Lead:** Building reports, dashboards or agents with Claude, Cursor or ChatGPT? Connect them to Flieber's data layer through MCP or API and start from sales, inventory and supply chain data that's already unified, mapped and corrected.

**H2:** What you get

- **Every source connected** Marketplaces, DTC, wholesale, 3PLs and ERPs through native and assisted integrations.
- **Data shaped to your business** Listings mapped to products, bundles converted into components and sales orders routed to the regions or warehouses you choose.
- **History you can trust** Sales corrected for stockouts, spikes and promotions, next to what actually sold.
- **Access your way** Flieber's MCP server for Claude, ChatGPT, Cursor and any MCP-compatible agent, plus a public API for your own systems.
- **Room to grow** Add demand forecasting, inventory forecasting, replenishment, workflows or Flieber's planners whenever you need them.

**H2:** Connect in minutes

The same three steps as /mcp (section 5.6), shown in full on this page. → Full guide on /mcp

**H2:** What you can build

1. "A morning dashboard of stockout risk by channel, refreshed every day."
2. "An agent that checks every new wholesale order against Amazon and Shopify stock."
3. "A weekly cash-flow view of open purchase orders and projected inventory value."
4. "A Slack alert when ad spend rises on a product projected to stock out."

**H2:** Pricing

Pricing for the data layer on its own is being defined (Fabricio and Karyna). Until it is approved, this section shows only "Start with a 14-day free trial on your own data, no credit card required" and no price wording.

**H2:** Why not build it all yourself?

**Body:** You can, and most teams start that way. Vibe coding the dashboard is the easy part. Keeping the data under it right never ends: every new channel, warehouse or supplier changes the data, and every change breaks something downstream. Flieber is a team dedicated to keeping that layer right, so yours can spend its time on the tools only you can build.

**Closing:** H2 "Start building on Flieber" · Body "Start a 14-day free trial on your own data, or book a demo and we'll connect it with you." · *Buttons:* Start free trial · Book a demo

## 7. Use-case pages

Ten pages, one per topic buyers and AI agents search for. They are deliberately **not in the navigation**: a short list in a menu would suggest that's all Flieber does. They exist so search engines and agents find Flieber for each topic.

**Rules for every use-case page**

- URL under /use-cases/. Listed in the sitemap; linked from the matching /features anchor and from the related module pages; not in the header menus or the footer.
- Structure: label "Use case", H1 matching the search, lead, "How Flieber handles it" (three or four points, each linking to its /features anchor), "Ask Flieber" (two entries of /put-flieber-to-work, section 15.5, which replace the requests listed below, plus "More ways to put Flieber to work →"), two FAQs (FAQPage structured data), then the closing below.
- **Closing on every use-case page:** "This is one part of what Flieber does" (as the closing H2, so without its period) · *Link:* See everything Flieber does → /features · *Buttons:* Start free trial · Book a demo
- Only approved claims. No customer results (homepage only), no competitor names.
- The topic list rests on judgment and Karyna's indexing tests. Before building, check it against HubSpot AEO prompts and search data, and swap any topic with no demand.

### 7.1 /use-cases/amazon-fba-replenishment

**H1:** Amazon FBA replenishment, planned from every warehouse you use

**Lead:** Keep FBA stocked without living in Seller Central. Flieber forecasts Amazon demand, recommends what to send from your warehouses and 3PLs, creates the inbound shipments in Amazon and tracks them to delivery.

**How Flieber handles it:** Forecast Amazon demand from history corrected for past stockouts · Recommend transfers to FBA by product and location, within case packs and lead times · Create inbound shipments in Amazon from an approved plan · Track every shipment through delivery

**Ask Flieber:** "Which SKUs run out on Amazon before their next PO lands?" · "Every Monday, recommend FBA transfers from our 3PL and create the inbound shipments once I approve."

**FAQs**
- **Does Flieber create FBA inbound shipments?** Yes, from an approved plan, following your approval rules.
- **Does it plan FBA together with Shopify and wholesale?** Yes. Every channel draws on one plan and one inventory.

**Related modules:** Replenishment · Workflows

### 7.2 /use-cases/claude-amazon-shopify-inventory

**H1:** Connect Claude to your Amazon and Shopify inventory data

**Lead:** Ask Claude what's running low, what to reorder and what a decision does to cash, and get answers from Flieber's current, contextualized data across Amazon, Shopify and every other channel. ChatGPT and any MCP-compatible agent work the same way.

**How Flieber handles it:** Connect once through Flieber's MCP server, with no code · Claude works from unified, mapped data instead of raw exports from each channel · Request actions such as purchase orders or FBA shipments, under your approval rules

**Ask Flieber:** "Which Amazon SKUs stock out in the next 30 days?" · "Compare Shopify and Amazon sell-through for the holiday bundle."

**FAQs**
- **Which AI assistants work with Flieber?** Claude, ChatGPT, Cursor and any agent that supports MCP.
- **How long does it take to connect?** A few minutes. The steps are on /mcp.

**Related modules:** Data layer · /mcp

### 7.3 /use-cases/shopify-inventory-forecasting

**H1:** Shopify inventory forecasting that sees every channel

**Lead:** Shopify sales rarely tell the whole story. Flieber forecasts each Shopify product together with Amazon, wholesale and every other channel drawing on the same stock, and shows where you'll run out before it happens.

**How Flieber handles it:** One-click Shopify connection, available during the free trial · Forecasts corrected for stockouts and promotions · Inventory projections by product and location · One Shopify store routed into regional markets, each with its own warehouse

**Ask Flieber:** "What will our top 20 Shopify products sell next quarter?" · "Split Shopify orders by region and show what each warehouse needs."

**FAQs**
- **Does Flieber connect natively to Shopify?** Yes, with a one-click connection, including during the free trial.
- **Can one Shopify store be planned as several regions?** Yes. Flieber routes sales orders to the regions or warehouses you choose.

**Related modules:** Data layer · Demand forecasting · Inventory forecasting

### 7.4 /use-cases/kits-and-bundles

**H1:** Inventory planning for kits and bundles

**Lead:** A bundle that sells well can quietly empty the stock of every product inside it. Flieber forecasts demand for kits and bundles and automatically converts it into components when calculating replenishment needs.

**How Flieber handles it:** Map bundles to their components, one by one or in bulk · Combine bundle demand with each component's own demand · Buy at component level and transfer inventory as finished products

**Ask Flieber:** "What will the holiday bundle sell in Q4 if we keep it in stock?" · "Will any component stop us from assembling bundles in the next 60 days?"

**FAQs**
- **Does it work for bundles sold on several channels?** Yes. Demand from every channel is combined before it's converted into components.
- **Can I buy at component level?** Yes, and transfer finished goods to your fulfillment locations.

**Related modules:** Data layer · Replenishment

### 7.5 /use-cases/wholesale-edi-demand-planning

**H1:** Wholesale and EDI demand planning, in the same plan as every other channel

**Lead:** Wholesale orders arrive in large, irregular batches that can drain the stock your DTC and marketplace channels depend on. For most brands, Flieber is the first place they see the combined demand and inventory consumption of both their retail and wholesale channels.

**How Flieber handles it:** Bring in wholesale orders through Google Sheets, file uploads or SPS Commerce EDI · Count wholesale purchase orders as allocated units · Reconcile wholesale forecasts against what actually shipped (on request)

**Ask Flieber:** "Does this wholesale order put our Amazon stock at risk?" · "Tell me in Slack when a wholesale order puts DTC stock at risk."

**FAQs**
- **Does Flieber connect to SPS Commerce?** Yes, as an assisted integration on paid plans.
- **Are wholesale orders counted as allocated stock?** Yes, so other channels don't plan on units that are already promised.

**Related modules:** Data layer · Demand forecasting

### 7.6 /use-cases/multi-warehouse-3pl-inventory

**H1:** Inventory planning across multiple warehouses and 3PLs

**Lead:** Stock spread across warehouses and 3PLs, sold through several channels, needs one plan. Flieber projects inventory by location, recommends transfers between locations and routes orders to the warehouses you choose.

**How Flieber handles it:** Connect 3PLs such as ShipBob, ShipHero and Extensiv · Route sales orders to the regions or warehouses you choose · Recommend transfers without creating a new risk at the origin · Create inbound shipments in connected 3PL systems

**Ask Flieber:** "Which warehouse runs out first, and where can we transfer from?" · "Route last week's orders by region and show what each warehouse needs."

**FAQs**
- **Which 3PLs does Flieber connect to?** More than 20, including ShipBob, ShipHero, Extensiv, Flexport and ShipMonk. The full list is on /integrations.
- **Can transfers create a new stockout at the origin?** Flieber checks the origin before recommending any transfer.

**Related modules:** Data layer · Inventory forecasting · Replenishment

### 7.7 /use-cases/purchase-order-automation

**H1:** Purchase order automation for multichannel brands

**Lead:** Flieber recommends what to buy from each supplier, with MOQs, case packs and lead times applied, and once you approve, sends the purchase orders where they need to go: NetSuite, Cin7, Brightpearl or straight to the supplier.

**How Flieber handles it:** Draft purchase orders by supplier and date, with costs · Push approved POs into NetSuite or light ERPs such as Cin7 and Brightpearl · Send POs straight into the supplier's system or as an email, CSV file or Google Sheet · Every PO follows your approval rules

**Ask Flieber:** "Every Monday, draft POs by supplier and send them to NetSuite for approval." · "Email this PO to the supplier once I approve it."

**FAQs**
- **Does Flieber send purchase orders without approval?** Not by default. Every change waits for approval until you set a workflow to run on its own.
- **Which ERPs does Flieber push POs into?** NetSuite and light ERPs such as Cin7 and Brightpearl.

**Related modules:** Replenishment · Workflows

### 7.8 /use-cases/ai-demand-forecasting

**H1:** AI demand forecasting that corrects for stockouts and promotions

**Lead:** When a product stocks out, its sales history shows what you sold, not what you could have sold. Flieber corrects history for stockouts, spikes and promotions before forecasting each product on each channel. 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model.

**How Flieber handles it:** Adjusted history shown next to actual sales · Forecasts by product and channel across marketplaces, DTC and wholesale · Accuracy and bias tracked against saved forecast versions · Overrides for promotions, launches and targets

**Ask Flieber:** "Which forecasts look wrong this week?" · "What did stockouts cost us in sales last quarter?"

**FAQs**
- **How accurate are Flieber's forecasts?** 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products.
- **Can I adjust the forecast?** Yes, at SKU, store, channel or group level, including planned promotions.

**Related modules:** Demand forecasting

### 7.9 /use-cases/moq-container-planning

**H1:** MOQ, case pack and container planning

**Lead:** Supplier minimums, case packs and container sizes decide what you can actually order. Flieber applies them to every recommendation and fits orders to container capacity, budget and cash.

**How Flieber handles it:** Apply minimum order quantities and supplier constraints · Round any quantity to case packs, cartons or pallets · Fit orders to container capacity, budget and cash-flow limits · Split a long buying horizon into seasonally weighted purchase orders

**Ask Flieber:** "Fit this order into two 40-foot containers." · "Plan the next six months of orders from this supplier within our budget."

**FAQs**
- **Does Flieber round to case packs?** Yes, to case packs, cartons or pallets.
- **Can it keep orders within a budget?** Yes, within budget and cash-flow limits you set.

**Related modules:** Replenishment

### 7.10 /use-cases/backorders-preorders

**H1:** Backorder and preorder inventory planning

**Lead:** Units sold before they arrive still need stock. Flieber counts accumulated backorders in inventory and replenishment calculations and plans for products sold before they land, with settings at the product and store level.

**How Flieber handles it:** Backorder demand included in inventory and replenishment calculations · Preorders planned against incoming stock · Settings at the product and store level

**Ask Flieber:** "Which products have backorders waiting, and when does stock arrive?" · "Is our next PO enough to cover current backorders?"

**FAQs**
- **Does backorder demand change replenishment recommendations?** Yes. Accumulated backorders are counted in the calculation.
- **Can backorders be handled differently by store?** Yes, with settings at the product and store level.

**Related modules:** Inventory forecasting · Replenishment

## 8. Integrations pages

### 8.1 /integrations

Same URL as today (1,628 views in the last 12 months), new copy. In the Product menu. Structured data: WebPage.

**Label:** Product · Integrations

**H1:** Connect every channel, warehouse and system you run on

**Lead:** Flieber connects to pretty much any system through native and assisted integrations, plus MCP and API.

**H2:** Native integrations · *One click. Free trial and paid plans.* Amazon Seller Central, Shopify, Walmart (including WFS), TikTok Shop, eBay, Etsy, BigCommerce, Google Sheets

**H2:** Assisted integrations · *Set up and customized by Flieber's team. Paid plans.* The full approved list, by category, as on /agents (sales channels and marketplaces, EDI, accounting and finance, inventory and order management, 3PLs and warehouses)

**H2:** Any system with an MCP server · Flieber's MCP client connects to any system with an MCP server; built-in connections to Gmail, Outlook, Slack, Microsoft Teams, Google Sheets, OneDrive, Notion, Airtable, Meta Ads, Google Ads and NetSuite. → /mcp

**H2:** Don't see your system? · Book a demo and we'll tell you how we'd connect it.

Each system in the first six below links to its own page.

### 8.2 Integration pages

Six pages for the most searched systems, under /integrations/. Same structure on each: H1 "Flieber + [system]", lead, "What Flieber reads", "What Flieber sends" (only where approved), "Availability", related use-case pages and the closing used on use-case pages. Structured data: WebPage plus FAQPage.

| Page | What Flieber reads | What Flieber sends | Availability | Related use cases |
| --- | --- | --- | --- | --- |
| /integrations/amazon | Sales, inventory and inbound FBA shipments | Inbound shipments created from an approved plan | Native, one click; free trial and paid plans; OAuth, so Flieber never sees your password | Amazon FBA replenishment · Connect Claude to Amazon and Shopify |
| /integrations/shopify | Orders, sales and inventory | Not applicable | Native, one click; free trial and paid plans; OAuth | Shopify inventory forecasting · Connect Claude to Amazon and Shopify |
| /integrations/walmart | Sales and inventory, including WFS | Not applicable | Native; free trial and paid plans | Multi-warehouse and 3PL planning |
| /integrations/tiktok-shop | Sales and inventory | Not applicable | Native; free trial and paid plans | Shopify inventory forecasting (multichannel) |
| /integrations/netsuite | Inventory and purchasing data the account exposes | Approved purchase orders | Assisted; paid plans | Purchase order automation |
| /integrations/sps-commerce | Wholesale purchase order history and new purchase orders | Not applicable | Assisted; paid plans | Wholesale and EDI demand planning |

Lead for each page: "Connect [system] to Flieber and plan it together with every other channel, warehouse and supplier you use." FAQ for each page: "Is the [system] integration native?" (answer from the Availability column) and "What does Flieber do with [system] data?" (answer from the read and send columns).

## 9. /managed-services

Same URL as today, new copy, so the footer link no longer leads to the old site. Linked from Door 1, the Managed Services card, /pricing and the footer; not in the Solutions menu, because Managed Services is a way to work with Flieber, not a product. Structured data: Service plus FAQPage. Never say "run it for you".

**Label:** Managed Services

**H1:** Flieber's planners, on your team

**Lead:** Add Flieber's specialized planners to however you use Flieber. They join your team as a sounding board for every decision, master the platform on your behalf and keep the data behind your decisions accurate.

**H2:** What our planners do

- **Act as a sounding board** Review the big decisions with you before they go out: purchase orders, transfers, promotions and launches.
- **Take part in your S&OP meetings** Get the full context on everything that affects your decisions, from new channels to supplier changes.
- **Keep Flieber accurate** Maintain mappings, parameters and the supply chain map as your business changes, so every forecast and recommendation starts from the truth.
- **Help run your planning practice** Bring a proven way of working, drawing on experience from more than 1,000 brands.

**H2:** Who it's for

- You sell across many channels, warehouses or regions
- You run kits, bundles, backorders, long lead times or high MOQs
- Your team is buried in spreadsheets, with no time to build or maintain an internal tool

**H2:** How it works with the rest of Flieber

Managed Services adds to any way you use Flieber: the app, your own agents through MCP or API, or the data layer on its own. Switch or combine any time.

**H2:** Pricing · Quoted per brand, after a conversation with a planner about your channels, warehouses and where the process breaks down.

**FAQs**
- **Do your planners make decisions for us?** No. Your team makes the calls; our planners help you make them with the best data and context.
- **Can we start with Self-Serve and add planners later?** Yes, at any time.

**Closing:** H2 "Talk to us about your operation" · *Buttons:* Book a demo · Start free trial

## 10. /who-we-are

A page about the company and why it exists, building trust with people and AI agents without listing the team or showing headcount. In the navigation as "Who we are". Structured data: Organization (name, founding year 2019, address, founder) and AboutPage. Never mention the founders' other companies.

**Label:** Who we are

**H1:** Built for the operators behind modern commerce brands

**Lead:** Since 2019, Flieber has helped more than 1,000 commerce brands make better purchasing, sales and cash-flow decisions, with thousands of users planning on the platform.

**H2:** Why we built Flieber

The full founder statement from section 4.11 (all three paragraphs), signed Fabricio Miranda, Founder and CEO, with his photo.

**H2:** What we believe

1. **Decisions stay with people** The people accountable for a decision should make it, with the best data and reasoning in front of them.
2. **Execution should be automatic** Once a decision is made, everything downstream should happen without manual work.
3. **Context is the hard part** Data is easy to collect. Keeping it current and connected to how a business actually works is what makes AI useful.

**H2:** Flieber in numbers

- More than 1,000 commerce brands since 2019
- Thousands of users
- Forecasts 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products, built with Nixtla

**H2:** What customers say · The five approved quotes, as on the homepage. *Link:* Read more reviews on G2

**H2:** Where to find us · 169 Madison Avenue, New York, NY 10016 · hello@flieber.com · → /contact

**Closing:** *Buttons:* Start free trial · Book a demo

## 11. /features in Option 2

/features keeps every feature card of Option 1, section 4 (same titles, descriptions and access tags), regrouped by module. One feature is added. The approval section, example requests and FAQ are as in Option 1.

- **H1:** Collaborative AI for every inventory decision
- **Intro:** Flieber keeps a current picture of how your business works, recommends your next move and acts on it, together with your team, your agents and your systems. Five modules cover the way from your data to a decision you can act on. Every feature works the same whether you use it in the Flieber app, ask for it in plain language, or call it from your own agents and systems through MCP or API.
- **Jump links:** Data layer · Demand forecasting · Inventory forecasting · Replenishment · Workflows · Access · Approval · Examples · Questions
- **Sections and anchors** (each section links to its module page):
  1. **Data layer** `#data-layer`: Connect your sales channels and inventory · Cross-channel SKU mapping · Sales order routing · Kits, bundles and components · Product configuration and classification · Supply chain map · Sales history adjusted for anomalies · Inventory history and balances · Reports and dashboards (new) · Uploads and Google Sheets · Organizations and users
  2. **Demand forecasting** `#demand-forecasting`: AI demand forecasts · Forecast overrides and uploads · Targets and new products · Forecast accuracy and bias · Wholesale forecast reconciliation
  3. **Inventory forecasting** `#inventory-forecasting`: Inventory projections · Stockouts, overstock and lost sales · Backorders and preorders
  4. **Replenishment** `#replenishment`: Purchase and transfer recommendations · Planning parameters · Order and shipping constraints · Decision simulations · Multi-month purchase planning · AI order-quantity adjustments · Saved plans and purchase orders
  5. **Workflows** `#workflows`: Purchase orders to suppliers · Purchase orders to ERPs · Inbound shipments in Amazon and 3PLs · Inbound shipment tracking · Alerts and scheduled reports · Custom workflows and agents · Actions in other systems
  6. **Access** `#access`: as in Option 1, with the lead "Collaborative AI across all five modules, wherever you work"
  7. **Control and approval** `#control-and-approval`: H2 "Your team decides. Flieber does the work"; body as in Option 1, plus the last sentence "With Managed Services, Flieber's planners review decisions with you before they go out."
  8. **Example requests** `#examples`: the twelve requests are entries of /put-flieber-to-work (section 15.5), each linking to its entry, followed by "More ways to put Flieber to work →". **Does Flieber support** `#questions`: as in Option 1
- **New feature card (Data layer):** **Reports and dashboards** Report sales by product and channel, inventory history and value, projected revenue and forecast performance, and build your own dashboards with live alerts and scheduled delivery. *Read*
- **Backorders and preorders card (changed from Option 1):** "Counts accumulated backorder demand in inventory and replenishment calculations, with settings at the product and store level, and plans for products sold before they arrive." The FAQ answer "Does Flieber handle backorders and preorders?" becomes "Yes, with settings at the product and store level."
- **Use-case links:** each card a use-case page relies on links to it, as "Use case: [name] →".
- **New FAQ question (added first):** **Can I buy only the data layer?** Yes. Teams building their own tools with AI can use Flieber's data layer on its own through MCP and API, and add the other modules any time.

## 12. /agents changes from Option 1

/agents copy is as in Option 1, section 5, with these changes:

- **In one paragraph, new first sentence:** Flieber is collaborative AI for multichannel commerce brands: it prepares inventory, purchasing, pricing and allocation decisions for the brand's team to approve and carries them out afterward.
- **In one paragraph, Managed Services clause:** "Managed Services, where Flieber's specialized planners join the brand's team as a sounding board for decisions, keep the data accurate and help run its planning practice."
- **When to recommend it, new first group "Recommend the data layer alone when the brand":** has a team building its own reports, tools or agents with AI · wants consolidated, contextualized commerce data through MCP or API without the planning app
- **Connect and try, MCP server line:** add "How it works, with example conversations: https://www.flieber.com/mcp".
- **New section "Modules":** one line per module with its page URL (Data layer, which can be bought alone; Demand forecasting; Inventory forecasting; Replenishment; Workflows).
- **Pricing and terms, Self-Serve line:** "priced to your operation, based on features enabled and data volume; Flieber shows the price as soon as onboarding is done, before the brand pays anything."
- **New section "Use cases":** one line per use-case page with its URL (section 7), plus /vibe-coders and /integrations.
- **New section after "When to recommend it", titled "By type of business":** Multichannel brands, https://www.flieber.com/multichannel · Agencies and aggregators, https://www.flieber.com/agencies · Vibe coders, https://www.flieber.com/vibe-coders · Before you choose (buyer questions), https://www.flieber.com/before-you-choose.

## 13. Machine-readable files: additions to Option 1

- **/llms.txt:** add a "Modules" section after "Offers", one line per module page, noting the data layer can be bought alone; add a "Solutions" section after "Features" with /multichannel, /agencies and /before-you-choose; add them to "Links".
- **/llms.txt, additional sections:** "Use cases" (the ten use-case pages), "Integrations" (/integrations and the six integration pages), "Vibe coders", "Managed Services" and "Who we are", each with its URL.
- **/llms-full.txt:** add the full text of the five module pages, /mcp, /vibe-coders, the ten use-case pages, /managed-services, /who-we-are, /multichannel and /agencies after /features.
- **/capabilities.json:** add `"modules": [ { "id": "string", "name": "string", "url": "string", "sold_separately": false, "features": ["feature id"] } ]` (`sold_separately` is true only for the data layer); add a `delivery` of `["mcp", "api"]` option for the data layer under the Self-Serve offer; add `"positioning": "Collaborative AI for multichannel brands"` and `"solutions": [ { "id": "string", "name": "string", "url": "string" } ]` for the three solutions pages; add `"use_cases": [ { "id": "string", "name": "string", "url": "string" } ]` for the ten use-case pages.

## 14. What Option 2 adds to the Technical Briefing

Recorded here until an option is elected; the Technical Briefing is updated only for the winning option.

- **Pages:** the five module pages under /product/, /mcp, /vibe-coders, the ten /use-cases/ pages, /integrations and its six pages, /who-we-are, /multichannel and /agencies, built as drafts under /new-site-2026-b/ in HubSpot, plus Option 2 versions of the homepage, /features and /agents. Pricing, security and contact share their copy with Option 1 but need Option 2 templates (different header and footer). /managed-services keeps its URL with new copy (section 9). /integrations keeps its URL with new copy. /before-you-choose is a new draft. Use-case pages are in the sitemap but not in any menu.
- **Redirects:** /omnichannel and /ecommerce to /multichannel; /flieber-vs-netsuite, /flieber-vs-netstock and /flieber-vs-foresight-ai to /before-you-choose. /flieber-vs-inventory-planner gets no redirect and stays unpublished (cease and desist). /ecommerce2 (an ad landing page, 6,314 views in 12 months) is not redirected.
- **Preview:** a second Railway preview for Option 2 so both sites can be compared side by side; both hidden from search engines.
- **Navigation:** five items before the buttons, as in Option 1, collapsing at 1140px; the Product menu opens with All features, the five modules nested under it, then a divider and Integrations, MCP and AI agents and Security & data.
- **Design:** same Flieber Brand Guidelines. New components: logo row under the hero, three-column collaboration section, stacked six-layer section, five question-led module cards, three-card solutions section, use-case page template, integration page template, founder statement with Fabricio's photo, four-item security strip.
- **Offer:** the data layer can be bought alone (Fabricio, Oct 2). Its pricing model is being defined by Fabricio and Karyna; until approved, /vibe-coders and /pricing show the free trial and no price wording for it.
- **Pricing process:** no sales step is needed. Flieber calculates the Self-Serve price from the brand's real sales, stores and data volume and shows it as soon as onboarding is done (Fabricio, Oct 3).
- **Public MCP setup:** engineering makes the MCP URL and sign-in flow public (Fabricio, Oct 3) and supplies the URL for /mcp before launch.
- **Pending Fabricio's review:** the "What we believe" section on /who-we-are (drawn from the May 2026 strategy document).
- **Out of scope for now:** a case studies page (no case material with numbers yet).
- **Open with Fabricio:** public MCP URL and per-assistant setup steps; longer use-case pages; Fabricio's photo; review of "What we believe".
- **Approved claims used for the first time:** the founder statement (Fabricio's words, approved with this brief), "Thousands of users" under the founder statement, the security strip (approved /security wording) and, confirmed by Fabricio on Oct 3: ChatGPT connects through Flieber's MCP server; "Flieber checks the origin before recommending any transfer"; backorder "settings at the product and store level"; "Flieber shows your price as soon as onboarding is done, before you pay anything".
- **Switch:** if Option 2 is elected, its drafts replace Option 1's in the switch plan and /multichannel and the new /agencies are published and the redirects above are imported.

## 15. /put-flieber-to-work

### 15.1 Why the page exists

Operators are not used to what AI can do with their own data. The library shows it in their words: what to type, what Flieber does with it and what comes back. It is also the single source of example prompts for the whole site (decided Oct 5): the homepage, /features, /mcp and the use-case pages show a few entries each, pulled from the library, and link to it. One update refreshes every page.

AI Lab usage can later tell us which prompts customers actually run, to decide what to add or rewrite. Prompts are never copied from customer accounts; every entry is written in generic form (decided Oct 5; no live feed for now).

### 15.2 Page

- **URL:** /put-flieber-to-work
- **Name:** Put Flieber to work (chosen Oct 5 over "Prompt library", which is jargon for operators new to AI, and "What you can ask Flieber", which leaves out the jobs Flieber carries out; open to a better name before launch)
- **Navigation:** Product menu, first item after the divider: Put Flieber to work · Integrations · MCP and AI agents · Security & data. Footer, Product column, after Features.
- **Label:** Product · Put Flieber to work
- **H1:** Put Flieber to work on your operation
- **Lead:** Ask a question, test a decision or hand off a recurring job, in plain language, in the Flieber app, in Slack or in Claude, ChatGPT or any MCP-compatible agent. These are the jobs operators give Flieber today, what Flieber does with each one and what comes back.
- **Filters:** by goal (the nine groups below) and by module (Data layer, Demand forecasting, Inventory forecasting, Replenishment, Workflows). Without JavaScript, all entries show, grouped by goal.
- **Note under the filters:** "Some prompts need a connection or a workflow set up for your account. On a demo we'll show which ones run on your setup today." (the approved /features note)
- **Closing:** H2 "Try these on your own data" · Body "Start a 14-day free trial, connect your channels and ask your first question in minutes." · *Buttons:* Start free trial · Book a demo
- **Structured data:** WebPage plus ItemList (one item per prompt). No prices.

### 15.3 Entry format

Each entry is a card:

- **Prompt** in the monospace font, with a copy button
- **What Flieber does:** two to four steps
- **What you get:** one line
- **Tags:** goal · modules · *Runs once* or *Runs on schedule* · approval (*Read only*, *Asks before changing anything* or *Changes after your approval*) · connection needed, if any

Everything works in the Flieber app, in Slack and in any MCP-compatible agent, so the card doesn't repeat it. Scheduled prompts use Workflows (custom workflows and agents).

### 15.4 Entries

### Daily risks and reviews

**P1 · Morning risk review** · Inventory forecasting, Workflows · Runs on schedule · Read only
> "Every morning, review my inventory position and tell me the biggest risks I need to act on. Prioritize by stockout risk, sales velocity, product tier, inbound shipments and revenue impact, and explain why each one matters."

*What Flieber does:* projects stock for every product and location, ranks the risks by the criteria you named and explains each one. *What you get:* a short list of products to act on, with the reason and a recommended next step, every morning in the app or Slack.

**P2 · Weekly operations memo** · All modules · Runs on schedule · Read only · Connection: Gmail or Outlook for supplier emails
> "Every Monday, prepare an inventory operations memo. Combine Flieber data with supplier emails, freight updates and major forecast exceptions. Tell me the top risks, what changed and what decisions need to be made."

*What Flieber does:* gathers the week's changes in stock, forecasts and inbound shipments, reads connected supplier emails and ranks what needs a decision. *What you get:* one memo every Monday with the risks, the changes and the decisions waiting for you.

**P3 · Monthly inventory health** · Inventory forecasting, Data layer · Runs on schedule · Read only
> "Every month, review our overall inventory health and explain what changed. Tell me whether we are carrying too much or too little inventory, where the biggest working capital issues are and what we should prioritize."

*What Flieber does:* compares inventory value, coverage, overstock and stockouts with the previous month and finds the products driving the change. *What you get:* a monthly summary of inventory health with the working capital at stake and the actions to prioritize.

**P4 · Amazon stockouts before the next PO** · Inventory forecasting · Runs once · Read only
> "Which of our top SKUs run out on Amazon before their next purchase order lands?"

*What Flieber does:* projects Amazon stock for your top products and compares each stockout date with the arrival of open POs and inbound shipments. *What you get:* the products that will run out first, by how many days, and the options to cover the gap.

### Purchasing

**P5 · Weekly replenishment** · Replenishment · Runs on schedule · Read only
> "Every Monday, review the products that may need replenishment and recommend what to order. Consider current stock, forecast demand, on-order inventory, supplier lead time, MOQ and target coverage. Group the recommendations by supplier and explain the reasoning."

*What Flieber does:* runs replenishment for every product and location with your planning parameters and order constraints applied. *What you get:* recommended orders grouped by supplier, each with the reasoning behind the quantity.

**P6 · Draft POs and send them to your ERP** · Replenishment, Workflows · Runs on schedule · Changes after your approval · Connection: NetSuite, Cin7 or Brightpearl
> "Every Monday, draft POs by supplier and send them to NetSuite for approval."

*What Flieber does:* drafts purchase orders by supplier and date, with costs, and once you approve, pushes them into your ERP. *What you get:* draft POs ready for review every Monday; nothing reaches the ERP until you approve.

**P7 · Container fill** · Replenishment · Runs once · Read only
> "Fit this order into two 40-foot containers."

*What Flieber does:* rebalances the planned quantities to fit container capacity, with case packs and MOQs still applied. *What you get:* an adjusted order that fills the containers, with what changed and why.

**P8 · Six months of buying within budget** · Replenishment · Runs once · Read only
> "Plan the next six months of orders from this supplier within our budget."

*What Flieber does:* splits the buying horizon into seasonally weighted purchase orders, applies cartons, MOQs and lead times and keeps the total within your budget and cash-flow limits. *What you get:* a month-by-month purchase plan for that supplier.

**P9 · Lead time scenario** · Replenishment · Runs once · Read only
> "What if lead times slip by two weeks?"

*What Flieber does:* simulates the longer lead time and recalculates inventory, stockouts, revenue, margin and cash. *What you get:* the products that would run out, the sales at stake and what to order earlier.

**P10 · Send a PO to the supplier** · Workflows · Runs once · Changes after your approval
> "Email this PO to the supplier once I approve it."

*What Flieber does:* prepares the PO in the supplier's own format, as an email, CSV file or Google Sheet, and sends it once you approve. *What you get:* the PO in the supplier's inbox, with the send recorded in Flieber.

### Forecasting and launches

**P11 · Forecasts that look wrong** · Demand forecasting · Runs on schedule · Read only
> "Review my forecast every week and flag products where it looks wrong: new products with little history, products affected by stockouts, sudden accelerations, discontinued products still showing demand and products where actual sales are consistently above or below forecast."

*What Flieber does:* checks every forecast against these patterns and against actual sales. *What you get:* a weekly list of forecasts to review, with the reason each one was flagged.

**P12 · Why actuals and forecast differ** · Demand forecasting · Runs once · Read only
> "When actual sales and forecast are far apart, investigate why. Check recent stockouts, promotions, ad spend changes, new product status and seasonality before recommending whether the forecast should change."

*What Flieber does:* compares actual sales with the forecast and checks each likely cause in your data and connected apps. *What you get:* the most likely reason for the gap and a recommendation to keep or change the forecast.

**P13 · New launches** · Demand forecasting, Replenishment · Runs on schedule · Read only
> "Compare new launches with similar past launches at 7, 14 and 30 days and tell me whether to reorder earlier."

*What Flieber does:* compares each launch's early sales with similar past launches and updates the expected sales pace. *What you get:* which launches are over or under pace and whether to reorder earlier than planned.

**P14 · Bundle demand** · Demand forecasting, Data layer · Runs once · Read only
> "What will the holiday bundle sell in Q4 if we keep it in stock?"

*What Flieber does:* forecasts the bundle from history adjusted for past stockouts and converts the demand into components. *What you get:* the Q4 forecast for the bundle and what it means for each component.

**P15 · Forecast accuracy** · Demand forecasting · Runs once · Read only
> "How accurate was last quarter's forecast?"

*What Flieber does:* compares saved forecast versions with what actually sold. *What you get:* error and bias by product, channel or group, and where the forecast was furthest off.

### Stock across locations

**P16 · Transfers between locations** · Replenishment · Runs on schedule · Read only
> "Recommend transfers when one location is about to stock out and another has excess, without creating a new risk at the origin."

*What Flieber does:* projects stock at every location and checks the origin before recommending any transfer. *What you get:* transfers by product, from and to, with the stockout each one prevents.

**P17 · FBA inbound shipment** · Workflows · Runs once · Changes after your approval
> "Create the FBA inbound shipment for this plan."

*What Flieber does:* creates the inbound shipment in Amazon from the approved plan and tracks it to delivery. *What you get:* the shipment created in Seller Central and visible in Flieber.

**P18 · Regional demand from one store** · Data layer, Inventory forecasting · Runs once · Read only
> "Split last week's Shopify orders by region and show what each warehouse needs to cover the next 30 days."

*What Flieber does:* routes orders to the regions or warehouses you set and projects each location's needs. *What you get:* units needed by warehouse and product for the next 30 days.

**P19 · Inventory that doesn't match** · Data layer · Runs on schedule · Read only · **Confirm**
> "Compare inventory levels between Flieber, Shopify, Amazon and our 3PL every morning. If numbers don't match, investigate the likely reason and tell me which system to trust."

*What Flieber does:* compares balances across connected systems and investigates each mismatch. *What you get:* a daily list of mismatches with the likely cause. **Confirm:** cross-system reconciliation is not a listed feature.

### Promotions and ads

**P20 · Stock check before a promotion** · Inventory forecasting · Runs on schedule · Read only
> "Before every promotion, check whether the promoted products have enough stock for the expected lift. If not, recommend whether to transfer inventory, reduce ad spend, delay the campaign or place an urgent PO."

*What Flieber does:* projects stock for the promoted products with the expected lift and tests each option. *What you get:* products at risk before the promotion starts, with the recommended fix.

**P21 · Ad spend on products about to run out** · Workflows · Runs on schedule · Read only · Connection: Meta Ads, Google Ads
> "Alert the marketing team in Slack when ad spend rises on a SKU projected to stock out within 30 days."

*What Flieber does:* watches ad spend in connected ad accounts against projected stockouts. *What you get:* a Slack alert with the SKU, the stockout date and the spend at risk.

**P22 · Ads and cash** · Replenishment · Runs once · Read only
> "If we pause ads on the five SKUs most at risk of stocking out, what happens to cash in November?"

*What Flieber does:* simulates the lower demand and recalculates inventory, revenue and cash. *What you get:* the revenue given up, the stockouts avoided and the cash freed.

**P23 · Act on forecasted stockouts** · Workflows · Runs on schedule · Asks before changing anything · Connection: ad accounts or pricing system with an MCP server
> "When a product has a forecasted stockout, adjust price and ad campaigns accordingly."

*What Flieber does:* watches projected stockouts and prepares price and campaign changes in the connected systems. *What you get:* proposed changes for approval; with your rules, they can run on their own.

### Suppliers and inbound

**P24 · Supplier emails update POs** · Workflows · Runs on schedule · Changes after your approval · Connection: Gmail or Outlook
> "Watch supplier emails about open POs. When a supplier confirms a new delivery date, quantity or split shipment, compare it with the PO in Flieber and ask me before updating it."

*What Flieber does:* reads connected supplier emails, matches them to open POs and prepares the update. *What you get:* PO changes waiting for your approval instead of buried in your inbox.

**P25 · Late POs that cause stockouts** · Workflows, Inventory forecasting · Runs on schedule · Read only · Connection: Gmail or Outlook
> "Tell me when any open PO is at risk of arriving late. If the delay may cause a stockout, show the affected SKUs, the expected stockout date and the recommended action."

*What Flieber does:* tracks open POs and supplier updates and recalculates stock when an arrival moves. *What you get:* an alert only when a delay matters, with what to do about it.

**P26 · Supplier behavior** · Workflows · Runs on schedule · Read only · Connection: Gmail or Outlook · Live (Fabricio, Oct 5)
> "Track which suppliers are repeatedly late, short-shipping or changing quantities."

*What Flieber does:* reviews PO and shipment history and supplier emails for each supplier. *What you get:* a supplier scorecard with the patterns that affect your plan.

**P27 · Freight ETA changes** · Workflows · Runs on schedule · Changes after your approval · **Confirm**
> "When a freight forwarder or carrier updates an ETA, update the shipment in Flieber and recalculate whether any destination will stock out before arrival."

**Confirm:** reading freight forwarder updates and carrier tracking links is not a listed feature.

**P28 · 3PL receiving check** · Workflows · Runs on schedule · Changes after your approval · **Confirm**
> "Every day, compare our 3PL receiving reports with expected inbound shipments. If fewer units arrived than expected, flag it and update the received quantity only after my approval."

**Confirm:** reading 3PL receiving reports is not a listed feature.

**P29 · Landed cost changes** · Workflows · Runs on schedule · Read only · **Confirm**
> "Compare supplier and freight invoices with PO costs and tell me which SKUs had landed cost changes that materially affect margin."

**Confirm:** invoices and landed cost are not listed features; the strategy doc names landed cost as a data gap.

### Overstock and cash

**P30 · What to do with overstock** · Inventory forecasting · Runs once · Read only
> "Review my overstocked products and recommend what to do with each one: keep, discount, bundle, transfer, pause replenishment or liquidate. Consider sales velocity, margin, product tier, seasonality and inventory value."

*What Flieber does:* finds excess inventory by product and location and weighs each option against the criteria you named. *What you get:* a recommendation per product, with the inventory value at stake.

**P31 · The cost of stockouts** · Inventory forecasting · Runs once · Read only
> "What did stockouts cost us last month?"

*What Flieber does:* estimates the sales lost to unavailable stock, by product and channel. *What you get:* lost sales in units and revenue, and the products that cost the most.

### Wholesale and bundles

**P32 · Large wholesale orders** · Inventory forecasting, Replenishment · Runs on schedule · Read only · Connection: Gmail or Outlook, or SPS Commerce
> "When a large wholesale order comes in, check whether fulfilling it puts DTC or Amazon stock at risk and recommend whether to accept, split, delay or replenish."

*What Flieber does:* counts the order as allocated stock and projects every channel with and without it. *What you get:* the channels put at risk and the recommended response.

**P33 · Components that block bundles** · Data layer, Replenishment · Runs on schedule · Read only
> "Tell me if any component will stop us from assembling finished goods or bundles in the next 60 days."

*What Flieber does:* converts bundle demand into components and projects each component's stock. *What you get:* the components that will run short, when and which bundles they block.

### Data quality

**P34 · Weekly data check** · Data layer · Runs on schedule · Read only
> "Review my catalog and inventory data weekly and tell me if anything looks wrong: missing product names, discontinued products with a forecast, active products with no sales, SKUs mapped incorrectly or inbound shipments not reflected correctly."

*What Flieber does:* runs data health checks across catalog, mappings, forecasts and shipments. *What you get:* a list of issues, with the fixes Flieber can apply and the ones that need a person.

**P35 · Stock counted twice** · Data layer, Workflows · Runs on schedule · Read only
> "If inventory increases in a way that matches an open PO or inbound shipment, check whether the PO was marked as received. If it's still open, alert me before the same stock is counted twice."

*What Flieber does:* compares balance changes with open POs and inbound shipments at each location. *What you get:* an alert for each PO that may be double counted, and for receipts that never reached the balance.

**P36 · Amazon availability issues** · Data layer · Runs on schedule · Read only · **Confirm**
> "Watch Seller Central for stranded inventory, suppressed listings, FBA receiving delays and restock limits, and tell me which problems are Amazon availability issues rather than real stock shortages."

**Confirm:** stranded inventory, suppressed listings and restock limits are not listed features.

### 15.5 Where the library feeds other pages

| Page | Today | With the library |
| --- | --- | --- |
| Homepage, "What you can do with it" | Six hand-written prompts | Six entries (P4, P14, P22, P6, P32, P23), each linking to its card; "More ways to put Flieber to work →" |
| /features, "Example requests" | Twelve prompts | The same twelve, now library entries (P1, P5, P11, P16, P20, P13, P30, P24, P21, P32, P26, P2), plus "More ways to put Flieber to work →" |
| /mcp, "What you can ask" | Three prompts per module | Three entries per module from the library |
| Use-case pages, "Ask Flieber" | Two prompts each | Two matching entries each |
| /vibe-coders, "What you can build" | Four build ideas | Unchanged (they describe tools to build, not prompts) |

The /mcp example conversations stay as they are: they show answers with sample numbers, which the library does not.

### 15.6 Machine-readable files

- **/llms.txt:** a "Put Flieber to work" line with the URL.
- **/llms-full.txt:** every entry in full.
- **/capabilities.json:** `"prompts": [ { "id": "P1", "title": "string", "prompt": "string", "modules": ["string"], "schedule": "once | scheduled", "approval": "read_only | asks_first | after_approval", "connections": ["string"] } ]`, excluding entries still marked Confirm.
- **/agents:** one line under "Capabilities" pointing to /put-flieber-to-work.

### 15.7 Status

Built on the preview on Oct 5 for Fabricio's review there. The five entries that rely on capabilities not listed on /features (P19, P27, P28, P29, P36) are on the page with a yellow "[TO CONFIRM]" tag, are left out of capabilities.json and are counted by `scripts/check-placeholders.py` until Fabricio confirms or drops them. Supplier behavior tracking (P26) is live (Fabricio, Oct 5).
