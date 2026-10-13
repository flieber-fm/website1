# 26-10-13 Website - Positioning Review and Content Briefing (Build and Run)

Cross-check of the live Option 2 brief (26-10-05 Website - Content Briefing, Option 2) against the October 2026 strategy discussion (Flieber Discussion Context Summary). Part A is the analysis. Part B is the recommended positioning and site content. Copy in Part B follows the house style (no em dashes, sentence-case headings, no final period on headings, no serial comma). Every claim that is not in the approved facts list is tagged **[Confirm]** and must not ship until Fabricio approves it.

---

# Part A. Analysis

## A1. Bottom line

1. **The two documents disagree at the top, not at the edges.** Option 2 sells Flieber as AI infrastructure ("The inventory intelligence layer your agents run on", "Collaborative AI for multichannel brands"). The discussion says AI is an enabler, not the headline, and that the promise is software that fits how the customer works. The hero, footer tagline, `positioning` field in capabilities.json, the first sentence of /agents, the Collaborative AI section, the six-layer stack and the founder statement all lead with AI. All of them have to change.
2. **Most of the depth survives.** Integrations, use-case pages, Put Flieber to work, /before-you-choose, /managed-services, /security, the module pages and the trust wording carry over with renaming. Roughly two thirds of the written content is reusable. The rewrite is concentrated on the homepage, the framing pages and the naming.
3. **The site currently has three overlapping product taxonomies, and the new strategy would add a fourth.** Five modules, a six-layer stack, three solutions and two offers already compete. The discussion adds four Build layers plus Run tools. Without consolidation, a visitor meets four different ways of slicing the same product before scrolling past the fold. Part B collapses them into one: four layers, sold two ways.
4. **The biggest risk is not copy, it's that the Build path is mostly unshipped.** Working templates, open source, purchasing layers separately, bring-your-own data and reliability tools as a product are not in the approved facts. Data-layer pricing is undefined. A vision-led homepage that splits traffic 50/50 and sends half of it to a path with no artifact and no price will underperform the current site with the buyers who pay today. Recommendation: build Run fully, and launch Build with only what exists (data layer, MCP, API, engineers) plus whatever template ships before launch.
5. **The founder's lean on the "agent moment" (domain logic alone) is the weakest of the candidate moats, by the discussion's own reasoning.** Logic is what AI reproduces most cheaply. What an agent cannot reproduce is logic running on the customer's data, already joined, mapped, stockout-corrected and kept current. The first callable should combine layers 1 and 2. See A4.

## A2. What survives, what changes, what goes

| Current element (Option 2) | Verdict | Why |
| --- | --- | --- |
| Hero eyebrow, H1, subhead ("intelligence layer your agents run on") | Replace | Leads with AI and agents; directly contradicts the agreed headline |
| Hero card (six agent requests) | Replace | Shows AI conversations, not fit. The new visual must prove "works the way you do" |
| Hero doors (Let our planners help you run it / Run it yourself) | Replace | "Run it yourself" collides with "Run with Flieber". Doors become Run and Build; services move inside each path |
| Logos under hero | Keep | Neutral, strong |
| Why inventory (every decision is an inventory decision) | Move to /run | Good argument for Run buyers, not the homepage's job anymore |
| Collaborative AI (three columns) | Demote | Becomes the approval and control point inside "Built to trust" and on /run |
| How Flieber is built (six layers) | Replace | Six layers mix mechanism (data, context, engine) with channels (where you work) and AI. Replaced by four layers |
| Its lead ("An agent on a spreadsheet can sound confident and still get inventory wrong...") | Keep, move to /build | The single best piece of Build copy already written |
| Five modules, one product | Restructure | Data layer is infrastructure, not an outcome. The discussion says Run "modules" must be outcomes. Data layer moves to Build; four Run tools remain |
| Solutions (multichannel, agencies, customize) | Restructure | Multichannel and agencies become "by business" links under Run. Customize becomes Build |
| What you can do with it (prompts) | Move to /run | Keeps the homepage short |
| Two ways to work with Flieber (Self-Serve vs Managed) | Restructure | Becomes "Do it yourself, or with us": planners for Run, engineers for Build |
| Proof (results, accuracy, quotes) | Keep | Approved, strong |
| From the founder (planners plus AI) | Rewrite | Its thesis is the old positioning |
| Your data stays yours | Keep, merge into "Built to trust" | Approved wording |
| Try it | Keep | |
| Module pages (/product/*) | Keep four, move one | /product/data-layer becomes /build/data |
| /customize | Becomes /build | Already has both paths (yourself, our engineers) and the "Why not build it all yourself?" argument |
| /mcp, /agents, llms.txt, capabilities.json | Keep, reframe | Agent channel assets are the right bet; first sentences and positioning fields change |
| /put-flieber-to-work, use-case pages, integrations, /before-you-choose, /managed-services, /security, /who-we-are | Keep | Minor edits listed in B7 |

## A3. Conflict register

Severity: **High** blocks launch or contradicts the strategy at the top. **Medium** confuses the buyer. **Low** wording.

| # | Conflict | Current (Option 2) | New direction | Severity | Resolution |
| --- | --- | --- | --- | --- | --- |
| 1 | Lead message | "The inventory intelligence layer your agents run on"; eyebrow "Built for AI agents and the teams who run them · MCP-native" | "Inventory software that works the way you do"; AI is not the headline | High | New hero (B4.1). MCP stays as a proof point under Build, not in the eyebrow |
| 2 | Core thesis | Collaborative AI: people decide, AI prepares and executes | Tailored fit without losing speed or reliability | High | Fit is the promise. Collaboration becomes one of the trust mechanisms (approval rules, planners) |
| 3 | Machine-readable positioning | capabilities.json `"positioning": "Collaborative AI for multichannel brands"`; /agents first sentence "Flieber is collaborative AI..." | Same as #1 | High | New wording in B6. Agents read this first, so it must change with the homepage, not after |
| 4 | "Run" naming collision | Self-Serve door is "Run it yourself" | "Run with Flieber" means buying finished tools | High | Retire "Run it yourself" and "Let our planners help you run it" as door labels |
| 5 | Number of taxonomies | 5 modules + 6 layers + 3 solutions + 2 offers | + 4 Build layers + Run tools | High | One structure: four layers, sold as Run (vertical slices) or Build (horizontal layers). B2 |
| 6 | One product vs composable | "Flieber is sold as one product"; "Flieber comes with all five" | Buy only the layers or tools you need | Medium | "One platform, one account; turn on what you need." Remove "comes with all five". Packaging still needs a decision (D4) |
| 7 | What a "module" is | Data layer is module 1 of 5 | For non-builders, modules mean business outcomes, not infrastructure | Medium | Data layer leaves the Run list and becomes a Build layer. Run keeps it inside, invisibly |
| 8 | Customize vs Build | "Customize Flieber" is one of three solutions, aimed at vibe coders | Build is one of two primary journeys and the strategic priority | Medium | /customize becomes /build (301). Promoted to the main navigation |
| 9 | Layer names | Data layer · Business context · Planning engine · Collaborative AI · Where you work · Control | Data integration · Domain logic / data contextualization · Templates · Reliability | Medium | Connected data · Inventory logic · Apps · Checks (B3). "Contextualization" never appears in copy |
| 10 | Where business context sits | Its own layer between data and engine | Split across layer 1 (map, connect) and layer 2 (relationships, calculations) | Low | Mapping, bundles and routing sit in Connected data. Relationships and calculations sit in Inventory logic |
| 11 | Templates | Not mentioned anywhere | Working, open-source app templates are one of four foundations | High | Not an approved claim. Ship at least one before saying it **[Confirm]** |
| 12 | Open source vs "proprietary algorithms" | "Proprietary algorithms, not language models, do the math" | Templates open source; what stays proprietary is an open question | Medium | Coherent if the split is: app code open, inventory logic hosted. Recommend stating that split once decided (D2) |
| 13 | Reliability as a product | Only as features (accuracy and bias, data checks P34/P35, simulations) | A layer: output correctness, forecast accuracy, decision accuracy vs outcomes | Medium | Present "Checks" with only the features that exist. No claim about validating modified code |
| 14 | Bring your own data | Not offered; Flieber's integrations are the only input | Customers with a data lake can bring their own | Medium | Only say it if ingest exists **[Confirm]** |
| 15 | Two offers vs two journeys | Self-Serve and Managed Services are the two ways to buy | Build and Run are the two journeys; services are optional on both | Medium | Services become help options: planners (Run), engineers (Build) |
| 16 | Founder statement | "Why we built Flieber to work with planners, not around them" | Software that fits; the hard part is keeping data and logic right | Medium | Draft in B4.8 for Fabricio's approval |
| 17 | Pricing | No prices; "Priced to your operation"; data layer has no price wording | Packaging unresolved; avoid credit complexity | Medium | Keep "Priced to your operation" as the single metric across Run and Build. Build needs at least a pricing sentence before launch, because agents rank vendors with visible pricing higher |
| 18 | Homepage priority | One audience (operators), agents secondary | Builders strategic priority, Run buyers current revenue | Medium | Doors equal in size; Run first in reading order, because that is who pays today. Build first in /agents and llms.txt, because that is who the agent channel brings |
| 19 | Who-we-are "What we believe" | Decisions stay with people · Execution should be automatic · Context is the hard part | Fit, speed, trust | Low | Keep 1 and 3, replace 2 with "Software should fit the operation" (B7) |
| 20 | "Inventory intelligence" phrase | Homepage H1 and footer tagline | Long-term ambition: the inventory intelligence foundation agents choose | Low | Use on /build, /agents and llms.txt; never as the homepage headline |
| 21 | "Seven years" | Approved fact is "since 2019" | Discussion uses "roughly seven years" | Low | Say "since 2019". Never say templates were "used by 1,000 brands" |
| 22 | Prompt library as Run content only | Put Flieber to work is framed for operators | Builders also need recipes | Low | Keep the page. Add a Build filter later with code-level examples in the docs |

## A4. Stress-testing the new direction

The discussion is directionally right, but five assumptions are weaker than they sound.

**1. "Inventory software that works the way you do" is a promise every vendor makes.** Asana, Monday.com and Airtable all run variations of "work the way you want". On its own it reads as flexibility marketing. It only becomes credible with the mechanism next to it: you can change the software itself, yourself, with AI or with Flieber's engineers. The subhead and the hero visual have to carry that proof, or the headline is noise. I would keep it (it is agreed and it is clear about the category) but test one variant that states the mechanism in the H1 itself (B4.1).

**2. A vision-led homepage serves the future buyer at the expense of the current one.** The mainstream buyer wants a finished tool and may not be AI-ready. "Build" and "code" are a reason for that buyer to leave. Mitigation: on every Run surface, say "make it yours" or "change it to fit", never "code" or "build". The word "build" lives on the Build side.

**3. The Build journey has the least product behind it.** Today Build can honestly offer: the data layer alone (approved, unpriced), MCP and the public API (approved; public MCP URL still pending engineering) and custom builds by Flieber's engineers (approved, quoted per project). It cannot yet offer: templates, open source, layer-by-layer purchase, bring-your-own data or validation of modified logic. Launching the Build page with "four foundations" when two of them don't exist breaks the brief's own rule ("never invent claims"). Ship one working template (replenishment is the strongest candidate: it touches every layer and is the most-used decision) before launch, or launch Build with three blocks and add templates when they exist.

**4. The agent recommendation moment should not be "domain logic".** The discussion itself concedes that formulas are what AI reproduces cheaply. An agent asked "build me a reorder tool for my Shopify and Amazon store" can write a reorder-point formula in seconds. What it cannot do is know that two listings are the same product, that a bundle drains three components, that last month's dip was a stockout or that a PO is due in 26 days. The Keepa analogy points the same way: agents recommend Keepa for data they cannot get anywhere else, not for its formulas. So the first callable Flieber capability should be **an answer that requires both layers**: "for this store, when does each SKU run out and what should be ordered, with the reasoning". The input is a store connection; the output is a projection and a recommendation. The customer pays because the expensive part (connected, corrected, current data) is maintained, not because the math is secret. The current site already says this better than the discussion does: "An agent on a spreadsheet can sound confident and still get inventory wrong." Make that the Build argument.

A second, stronger Keepa analog may exist: patterns across more than 1,000 brands (launch curves, supplier lead-time behavior, seasonality by category) are data no agent can reproduce. It conflicts with "Your data is never sold or shared" unless it is anonymized and aggregated, and it needs legal review. Treat it as a hypothesis, not copy (D7).

**5. Customization and trust pull against each other, and the site must not paper over it.** If a customer changes the replenishment logic with Claude Code, Flieber cannot promise the result is correct. What Flieber can honestly offer: accuracy tracked against what actually sold, data health checks, simulations before committing and approval rules on every change. Say exactly that. Do not write "validated", "certified" or "guaranteed" anywhere until there is a retesting process for modified logic.

**What the discussion gets right and the current site gets wrong:** the current site describes how Flieber works (layers, engine, AI) far more than what the buyer gets. Six layers, three parties and five modules on one homepage is an explanation, not a pitch. The new direction forces the site to answer one question first: do you want it ready, or do you want it yours? That is a better first question than anything on the current homepage.

---

# Part B. Recommended positioning and content

## B1. Positioning

**Category frame (the enemy).** Off-the-shelf inventory tools make teams work their way. Building your own starts from zero, and the hard part is not the screen, it's the data and the logic under it. Flieber is the third option: software that fits, on a foundation that's already right.

**Positioning statement (internal, do not publish verbatim).** For multichannel commerce brands, and the teams and agents that build tools for them, Flieber is inventory software that works the way they do. Run it ready-made, or build your own on it. Either way it starts from connected data and inventory logic shaped by more than 1,000 brands since 2019, so the software fits the operation without giving up speed or reliability.

**Headline:** Inventory software that works the way you do

**Three pillars** (each with the proof that already exists)

| Pillar | Promise | Proof available today |
| --- | --- | --- |
| Your way | The software fits the operation: views, columns, rules, approvals, workflows | Sales order routing, kits and bundles, planning parameters, custom workflows and agents, engineers' custom builds |
| Faster value | Start ahead with logic and apps that already work | 14-day trial on your own data, one-click integrations, setup included, more than 1,000 brands since 2019 |
| Built to trust | Connected data, checked results, your rules | 36% accuracy claim, accuracy and bias tracking, approval rules, security wording, results footnoted to 12+ months |

**Words to use:** works the way you do · ready-made · make it yours · change it to fit · inventory logic · connected data · checked against what actually sold · nothing changes without your approval · keeps working as you add channels, products or suppliers

**Words to avoid:** collaborative AI (as a headline) · intelligence layer (on the homepage) · AI-native · data contextualization · validated or certified · maintenance (sell the outcome: "keeps working as you grow") · open source (until a repo exists)

## B2. Product structure: one platform, two ways to buy it

The four Build layers and the Run tools are the same product cut two ways. Run sells vertical slices (an outcome, all layers included). Build sells horizontal layers (take the ones you need). This replaces the five modules, the six-layer stack and the three solutions.

```
                 Run with Flieber (ready-made tools)
              Demand      Inventory     Replenish-    Workflows
              forecasting forecasting   ment
            +-----------+-------------+-------------+-----------+
  Apps      |           |             |             |           |  <- Build: start from working apps [Confirm]
  Inventory |           |             |             |           |  <- Build: call it through API and MCP
  logic     |           |             |             |           |
  Connected |           |             |             |           |  <- Build: the data layer, alone (approved)
  data      |           |             |             |           |
            +-----------+-------------+-------------+-----------+
  Checks: accuracy, data health, simulations, approval rules (across everything)
```

| Layer | Plain name | What's in it (from approved features) | Old names |
| --- | --- | --- | --- |
| 1 | Connected data | Integrations, cross-channel SKU mapping, kits and bundles, sales order routing, supply chain map, sales history adjusted for anomalies, inventory history, uploads and Google Sheets | Data layer; Your data; part of Business context |
| 2 | Inventory logic | Stockout-corrected demand, forecasts, inventory projections, lost sales, purchase and transfer recommendations under MOQs, case packs, lead times and cash | Business context (relationships); Planning engine |
| 3 | Apps | The Flieber app's forecasting, planning, replenishment and workflow screens, plus templates **[Confirm]** | Where you work; module pages |
| 4 | Checks | Forecast accuracy and bias, data health checks, decision simulations, approval rules | Control; parts of Collaborative AI |

Collaborative AI (plain-language questions, Slack, MCP, API) is how you use every layer, as today. It is not a layer and not a headline.

## B3. Site map and navigation

**Navigation:** Run · Build · Pricing · Customers · Company · /agents (pill) · Log in · Book a demo · Start free trial

- **Run** (menu): Overview → /run · Demand forecasting · Inventory forecasting · Replenishment · Workflows · divider · By business: Multichannel brands · Agencies and aggregators · divider · Put Flieber to work · Our planners (Managed Services)
- **Build** (menu): Overview → /build · Connected data → /build/data · MCP and AI agents → /mcp · API and docs · Templates **[Confirm]** · divider · Our engineers → /build#engineers
- **Customers:** proof, quotes, G2 (can start as a homepage anchor until a case studies page exists)
- **Company:** Who we are · Security & data · Integrations · Before you choose · Contact

| Page | Status |
| --- | --- |
| / | Rewritten (B4) |
| /run | New (B5) |
| /build | New, replaces /customize (301) (B6) |
| /build/data | Moved from /product/data-layer (301) |
| /product/demand-forecasting, /product/inventory-forecasting, /product/replenishment, /product/workflows | Kept, moved under Run; consider /run/... URLs later, not at launch |
| /mcp, /agents, /llms.txt, /llms-full.txt, /capabilities.json | Kept, reframed (B6.3) |
| /put-flieber-to-work, /use-cases/*, /integrations/*, /before-you-choose, /managed-services, /security, /who-we-are, /pricing, /contact | Kept with the edits in B7 |

## B4. Homepage copy

Eight sections plus footer.

### B4.1 Hero

**Eyebrow:** Inventory planning software for multichannel brands

**H1:** Inventory software that works the way you do

*Variant to test:* Ready-made inventory planning you can change to fit

**Subhead:** Ready-made forecasting, inventory planning and replenishment, on data and inventory logic that are already right. Use it as it is, change it to fit, or build your own on top: yourself, with AI or with our team.

**Hero visual:** the same replenishment screen in two states with a toggle, "Ready-made" and "Yours". "Yours" shows a brand's own columns, a supplier-specific rule, its own approval step and a "Send to NetSuite" button. Footer label: "Sample data. Illustrative only." This is the proof of the headline; an AI chat window is not.

**Door 1: Run with Flieber**
*Ready to use from day one*
Forecasting, inventory planning and replenishment shaped by more than 1,000 commerce brands since 2019. Connect your channels and start planning, no code needed. Add our planners whenever you want a second pair of eyes.
*Button:* Start free trial · *Link:* See the tools → /run

**Door 2: Build with Flieber**
*Your own inventory software, without starting from zero*
Build your own tools on Flieber's connected data and inventory logic, through MCP and API, with Claude, Cursor or your own agents. Or have our engineers build it with you.
*Button:* Start building → /build

**Under the doors:** 14-day free trial · No credit card · Monthly contracts · Setup included

### B4.2 Logos

**Label:** Trusted by hundreds of brands. As today.

### B4.3 The problem

**Label:** Why Flieber

**H2:** Off-the-shelf tools make you work their way. Building your own starts from zero

**Body:** Most inventory software is built for the average brand, so your team bends its process around it or goes back to spreadsheets. Building your own with AI is now fast, until you reach the hard part: data from every channel joined, mapped and corrected, and planning logic that knows a stockout from a slow month. Flieber gives you both halves: software that fits, on a foundation that's already right.

### B4.4 How Flieber works

**Label:** How Flieber works

**H2:** One foundation. Ready-made tools or your own

**Lead:** Every Flieber tool runs on the same four layers. Run customers get all of them, ready to use. Builders take the layers they need.

1. **Connected data** Every channel, warehouse, 3PL, ERP and supplier, joined into one record: listings mapped to products, bundles to their components, orders routed to the warehouses you choose. Kept current as you add channels, products or suppliers.
2. **Inventory logic** How inventory actually works: demand corrected for stockouts and promotions, projections by product and location, and purchase and transfer recommendations within MOQs, case packs, lead times and cash. Proprietary algorithms, not language models, do the math.
3. **Apps** Forecasting, inventory planning, replenishment and workflows, ready to use in the Flieber app, Slack and Google Sheets, or through your own agents.
4. **Checks** Forecast accuracy and bias against what actually sold, data health checks, simulations before you commit and approval rules on every change.

*Link:* How we handle your data → /security

### B4.5 Run and Build

**Label:** Two ways to use Flieber

**H2:** Run it as it is, or build it your way

Two columns, equal width.

**Run with Flieber**
- **Demand forecasting** What will sell, and where? Forecasts for every product on every channel, corrected for stockouts and promotions. → /product/demand-forecasting
- **Inventory forecasting** Where will I run out, or sit on too much? Stockouts, overstock and lost sales by product and location, while there's still time to act. → /product/inventory-forecasting
- **Replenishment** What should I buy or move, how much and when? Recommendations within MOQs, case packs, lead times and cash, tested before you commit. → /product/replenishment
- **Workflows** How does the decision get done? Approved decisions carried into suppliers, ERPs, Amazon and 3PLs. → /product/workflows

*Under:* Each tool's output feeds the next, so you can start with what you need. **[Confirm: depends on D4]** → /run

**Build with Flieber**
- **Connected data** Sales, inventory and supply chain data that's already joined, mapped and corrected, through MCP and API. Available on its own. → /build/data
- **Inventory logic** Forecasts, projections and recommendations your own tools and agents can call. → /build#logic
- **Working apps to start from** Start from a working replenishment app and change anything. **[Confirm: ship a template first]**
- **Our engineers** No time or team to build? Our engineers build it with you, from views and reports to a tailored frontend. → /build#engineers

*Under:* → /build

### B4.6 Make it yours

**Label:** Make it yours

**H2:** Start ready-made. Make it yours as you go

**Lead:** You don't have to choose on day one. Every Flieber tool has a path to fit your operation more closely.

1. **Use it as it is** Connect your channels and plan in the Flieber app.
2. **Set it up your way** Your parameters, views, approval rules and scheduled reports.
3. **Change how it works** Custom workflows and agents, built by your team with AI or by our engineers.
4. **Build your own** Your own tools on the same data and logic, with nothing thrown away.

### B4.7 Built to trust

**Label:** Built to trust

**H2:** Software that fits, numbers you can check

- **Checked against reality** Forecast accuracy and bias tracked against what actually sold. Forecasts 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products.
- **Nothing changes without your approval** By default, every change waits for your approval. You decide what runs on its own.
- **Never sold or shared** Your data stays yours, and Flieber does not train on it. Its AI providers are set up not to.
- **Encrypted on AWS** Hosted on Amazon Web Services in the US, encrypted in transit and at rest.

*Link:* How we handle your data → /security

### B4.8 Proof and founder

**Label:** Proof

**H2:** What brands get from planning on Flieber

Customer results, footnote, accuracy stat, quotes carousel and G2 link as today.

**From the founder** (draft for Fabricio's approval; replaces the current statement)

> Every brand we've worked with plans a little differently: its own channels, suppliers and rules, and the columns its team checks first. For years, software made them choose between a tool built for the average brand and a spreadsheet built for them.
>
> AI is changing that. Building software is getting easy. Getting inventory right isn't: the data has to be joined and corrected, the logic has to know a stockout from a slow month, and both have to keep up as the business changes. That's what we've spent since 2019 getting right with more than 1,000 brands.
>
> Now we're opening it up, so every team can run Flieber as it is or build the software that fits exactly how it works.

Fabricio Miranda, Founder and CEO

**Under:** More than 1,000 commerce brands since 2019. Thousands of users. 169 Madison Avenue, New York. → /who-we-are

### B4.9 Help and try it

**Label:** Do it yourself, or with us

**H2:** Help when you want it

- **Our planners** Specialists in inventory planning and in Flieber who join your S&OP meetings, act as a sounding board for your decisions and keep your data accurate. Quoted per brand. → /managed-services
- **Our engineers** Customizations, dashboards, tailored frontends, integrations and agents built for your operation. Quoted per project, for qualified accounts. → /build#engineers

*Under:* Same platform either way. Switch or combine any time.

**H2:** Try Flieber free on your own data

**Body:** Start a 14-day free trial, no credit card required and no demo call. Flieber shows your price as soon as onboarding is done, before you pay anything.

*Buttons:* Start free trial · Book a demo

### Footer

**Tagline:** Inventory software that works the way you do.

**Columns:** Run (Overview, the four tools, Multichannel brands, Agencies and aggregators, Put Flieber to work, Managed Services) · Build (Overview, Connected data, MCP and AI agents, API and docs, Our engineers) · For agents (/agents, /llms.txt, /capabilities.json, MCP docs) · Company (Who we are, Integrations, Before you choose, Security & data, Pricing, Help center, Blog, Contact, Privacy, Service agreement)

## B5. /run

**Label:** Run with Flieber

**H1:** Inventory planning that works from day one

**Lead:** Forecasting, inventory planning, replenishment and workflows, ready to use on your own data, shaped by more than 1,000 commerce brands since 2019. No code, no project. Connect your channels and start planning, then make it yours as you go.

**Section 1, "Why inventory":** the current homepage section 4.3 (H2 "Purchases, promotions, ads, financing: every one is ultimately an inventory decision"), unchanged.

**Section 2, the four tools:** the four Run cards from B4.5, each linking to its module page.

**Section 3, "Your team decides":** the current Collaborative AI three columns (Your team · Flieber's AI and your agents · Flieber's planners), with H2 "Your team decides. Flieber does the work around it".

**Section 4, "Ask anything your operation depends on":** the six Put Flieber to work entries now on the homepage (P4, P14, P22, P6, P32, P23).

**Section 5, "By business":** Multichannel brands → /multichannel · Agencies and aggregators → /agencies.

**Section 6, "Make it yours":** H2 "When the ready-made version isn't enough" · Body "Set it up your way, add custom workflows or have our engineers change it to fit. It's the same platform, so nothing you've set up is lost." → /build

**Section 7, fit:** the current "You're probably here if" and "Probably not for you if" lists.

**Closing:** H2 "See it on your own data" · *Buttons:* Start free trial · Book a demo

## B6. /build

### B6.1 Page

**Label:** Build with Flieber

**H1:** Build your own inventory software. We'll handle the hard parts

**Lead:** Building the screen is the easy part. Flieber gives your tools and agents what's hard to build and harder to keep right: sales, inventory and supply chain data already joined, mapped and corrected, and inventory logic that does the math. Build it yourself with Claude, Cursor or your own agents, or have our engineers build it with you.

**Two path cards:** **Build it yourself** → #yourself · **Have our engineers build it** → #engineers

**Section "Why your agent needs Flieber":** H2 "An agent on a spreadsheet can sound confident and still get inventory wrong" · Body "It doesn't know which listings are the same product, what's inside a bundle or that last month's dip was a stockout. Flieber does, for every channel you sell on, and keeps it current as your business changes."

**Section "What you build on"** (anchor #yourself):

1. **Connected data** Every channel, warehouse, 3PL and ERP through native and assisted integrations, with listings mapped to products, bundles converted into components and sales history corrected for stockouts. Available on its own. → /build/data
2. **Inventory logic** (anchor #logic) Ask for forecasts, inventory projections, stockout dates and purchase or transfer recommendations from your own tools and agents, through MCP and API.
3. **Working apps to start from** **[Confirm; omit until one ships]** A working replenishment app to use as it is, copy or change with Claude Code or Codex.
4. **Checks** See how accurate forecasts have been against what actually sold, run data health checks and simulate a decision before your tool acts on it.

**Section "What you can build":** the four ideas on today's /customize (morning stockout dashboard, wholesale order checker, weekly cash-flow view, Slack ad-spend alert).

**Section "Connect in minutes":** the three MCP steps from /mcp.

**Section "Why not build it all yourself?":** today's /customize copy, unchanged. It is the clearest statement of the moat in customer terms.

**Section "Our engineers"** (anchor #engineers): today's /customize engineers section (what they build, how it works, terms), unchanged.

**Section "Pricing":** "Start with a 14-day free trial on your own data, no credit card required." Add price wording as soon as D5 is decided.

**Closing:** H2 "Start building on data that's already right" · *Buttons:* Start free trial · Read the MCP docs

### B6.2 /build/data

Today's /product/data-layer, with the label "Build · Connected data" and the H1 kept ("Your commerce data, consolidated, contextualized and current" becomes "Your commerce data, connected, corrected and current", to drop "contextualized").

### B6.3 Agent channel (/agents, llms.txt, capabilities.json)

- **/agents first sentence:** "Flieber is inventory software for multichannel commerce brands, available two ways: ready-made forecasting, inventory planning, replenishment and workflow tools, or connected commerce data and inventory logic that a brand's own tools and agents use through MCP and API."
- **When to recommend it, first group:** "Recommend Flieber when the user or agent needs to know, for a real store, when each product will run out and what to order, and the answer depends on data an agent can't reconstruct from raw exports: listings that are the same product, bundle components, stockout-corrected history, open POs and lead times."
- **capabilities.json:** `"positioning": "Inventory software that works the way you do"`; replace `modules` with `"run_tools"` (four) and `"build_layers"` (connected data `sold_separately: true`; others false until D3).
- **Public MCP URL:** the single highest-leverage item for the agent channel, ahead of any copy. Already in engineering's queue; it should gate the Build launch.

## B7. Edits to pages that otherwise stay

| Page | Edit |
| --- | --- |
| Module pages | Remove "Five modules" language and the Data layer from "Works with"; add a "Make it yours" line linking to /build |
| /features | H1 "Everything Flieber does, ready-made or through MCP and API". Group by the four Run tools plus Connected data. Keep anchors |
| /multichannel, /agencies | Change "Customize Flieber yourself or with our engineers → /customize" to "Want tools built around your business? Build with Flieber →/build" |
| /agencies H1 | "The inventory intelligence layer for every brand you run" becomes "One plan for every brand you run" |
| /before-you-choose | Add three questions under a new H2 "Fit": "Can you change how it works to fit your operation?" · "Can your own tools and agents use its data and logic?" · "Can you start with only what you need?" Answer only with approved facts |
| /pricing | Remove "Run it yourself" and "Let our planners help you run it" as labels. Show Run and Build, then planners and engineers as add-ons. Keep "Priced to your operation" |
| /managed-services | No copy change; it is now linked from Run, not from the hero |
| /who-we-are | Founder statement from B4.8. "What we believe": 1 Decisions stay with people · 2 Software should fit the operation, not the other way round · 3 Context is the hard part |
| /mcp | Keep. Change "Build your own tools on Flieber" link from /product/data-layer to /build |
| /put-flieber-to-work | Keep. Lead adds "in the app or from your own tools" |

## B8. Claims to confirm before publishing

| Claim | Where | Status |
| --- | --- | --- |
| Working app templates exist | Hero door 2 (omitted until true), /build, B4.5 | Not approved |
| Templates are open source, and under which license | Nowhere until decided | Not approved |
| Claude Code and Codex as build tools | /build | Claude, Cursor and ChatGPT are approved; Claude Code and Codex are not named in approved facts |
| Inventory logic callable on its own through MCP and API | /build #logic | MCP and API exist; confirm the specific calls (forecast, projection, recommendation) are exposed |
| Run tools can be bought individually | B4.5 "start with what you need" | Not approved; contradicts "Flieber comes with all five" |
| Bring your own data | Not used in copy | Not approved |
| Validation of modified logic | Not used in copy | Not approved; do not imply |
| Competitive analysis tool | Not used in copy | Mentioned in discussion only |

## B9. Decisions needed from Fabricio

1. **Template at launch.** Will one working template (recommend replenishment) ship before the site goes live? If not, Build launches with three blocks.
2. **What is open and what is hosted.** Recommendation: app code open, inventory logic and connected data hosted. That keeps the moat where AI can't reproduce it.
3. **Layer-by-layer purchase.** Beyond the data layer alone (approved), which layers can be bought without the others today?
4. **Run packaging.** Individual tools, or all four with the price driven by what's turned on and data volume? Recommendation: keep one account and one metric ("Priced to your operation") and avoid credits until usage data shows a need.
5. **Build pricing sentence.** Even one line ("Priced by data volume, shown after onboarding") helps agents recommend Flieber.
6. **Public MCP URL date.** Gates the Build launch.
7. **Cross-brand patterns.** Is anonymized, aggregated insight from 1,000+ brands a product, and is it compatible with "never sold or shared"? Legal review before any mention.
8. **Founder statement.** Approve or rewrite B4.8.
9. **Headline test.** Approve running "Ready-made inventory planning you can change to fit" as the A/B variant.
