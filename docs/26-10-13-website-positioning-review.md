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
| Hero doors (Let our planners help you run it / Run it yourself) | Replace | "Run it yourself" collides with "Run with Flieber". Replaced by one offer with Run as the default and Build as a secondary path; services leave the hero (see A5) |
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
| 18 | Homepage priority | One audience (operators), agents secondary | Builders strategic priority, Run buyers current revenue | Medium | Run is the default in the hero and Build a visible secondary path (revised after the Comp benchmark, A5), because Run is who pays today. Build first in /agents and llms.txt, because that is who the agent channel brings |
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

## A5. Benchmark check: Comp (added Oct 13)

Source: Comp Benchmark for Flieber Positioning (Fabricio, Oct 13). Each of the five moves it recommends borrowing is checked against the first version of this review. The benchmark's other points (where the analogy breaks, open questions) were checked too.

| Comp move | Already in this review? | What changed |
| --- | --- | --- |
| 1. Name the category and say what you are not | **Partly.** B1 had a category frame (off-the-shelf vs build from scratch) but no "not X, not Y, not Z" sentence | Added a category sentence to B1 and used it as the H2 of the problem section (B4.3). No "AI-native inventory" label: the benchmark itself warns a borrowed label won't differentiate in US commerce, and it would reverse the "AI is not the headline" decision |
| 2. Enemy = the buyer's failed alternatives | **Partly.** Two of the three were there (shelf software, DIY with AI). "Adding planners or consultants" was missing | Added the third alternative, framed as "more hands on spreadsheets", not "planners". Flieber sells planners, so the enemy is headcount doing clerical work around a weak system, not expertise. Did not use "only 10% used": it's not an approved number |
| 3. Lead with one offer; configure after the call | **No, the opposite.** The first version had two equal hero doors (Run, Build) with services inside each: exactly the "two routes times two service options" the benchmark calls Flieber's clarity gap | Hero now leads with one offer and one entry (the free inventory health check). Build stays visible above the fold as a secondary path, so the agreed "both journeys visible" decision holds. Routes and modules live below the fold and on /run and /build. "Configure after the call" is adopted only for the services: Flieber's self-serve buyer gets a price after onboarding, with no sales step (Fabricio, Oct 3), and that shouldn't be lost |
| 4. A diagnosis as the low-stakes entry | **No.** Entry was the 14-day free trial | Added a "Free inventory health check" (B4.9), built from features that already exist (data health checks, stockouts before the next PO, cost of stockouts, overstock). It is the trial with a defined result, not a new product. A planner-reviewed version is the entry for Managed Services. Avoided "AI readiness check": AI isn't the headline |
| 5. Show the people if services are an equal option | **No**, and only partly applicable | Services are add-ons in this positioning, not equal to the product, so the people are not the hero (the benchmark agrees: Flieber's moat is maintained data plus cross-brand context, not pedigree). Added named planners to /managed-services only (B7), pending consent and a reversal of the "no team list" rule for that page (D11) |
| Free tools as top of funnel (Comp: AI diagnosis, Claude Skills for CHROs, benchmark data) | **No** | Added a free tools block to /build (B6.1): Claude Skills for inventory planners and a stockout cost calculator. It is the same move as the agent channel, so it costs little extra **[Confirm]** |
| One-line pricing logic | Flagged as a decision (D5) | Proposed the line in D5 |
| Canonical proof number | Not flagged | Added to B8. "Trusted by hundreds of brands" (logo label) and "more than 1,000 brands since 2019" need one definition. The benchmark's churn figure (53 to 46) shows why: if a reader takes "hundreds" as current paying customers, it may not hold |
| Who owns custom builds; does reuse become product | Not covered | Added D10. It matters for Build: a build by Flieber's engineers that becomes a template is how the template library grows without a separate team |
| Hero of the story | Implicit | Made explicit in B1: the hero is the foundation that stays right (data and logic), shown through the software that fits. Not the AI, not the planners |

**What not to borrow, agreeing with the benchmark:** a services-led homepage (reads as the product being deprioritized to remaining self-serve accounts), people as the proof (undersells the data moat) and an "AI-native" category label.

---

# Part B. Recommended positioning and content

## B1. Positioning

**Category sentence (after Comp).** Flieber is not inventory software you work around, not a tool you rebuild from scratch every time the business changes and not more hands on spreadsheets. It's inventory software that works the way you do, on data and logic that stay right as you grow.

**The three failed alternatives (the enemy, never a named competitor)**

1. **Off-the-shelf software:** built for the average brand. Teams bend their process around it, use a fraction of it and drift back to spreadsheets.
2. **Building it yourself with AI:** fast to start, but it covers today's cases. Every new channel, bundle or supplier means rebuilding the data and logic under it.
3. **More hands on spreadsheets:** more planners, analysts or consultants add hours, not a system. The work stays manual and the knowledge leaves when they do.

Flieber's planners are not alternative 3: they work on Flieber, not on spreadsheets. Say so wherever planners appear.

**Hero of the story.** The foundation that stays right (connected data and inventory logic), shown through the software that fits. Not the AI and not the people.

**Positioning statement (internal, do not publish verbatim).** For multichannel commerce brands, and the teams and agents that build tools for them, Flieber is inventory software that works the way they do. Run it ready-made, or build your own on it. Either way it starts from connected data and inventory logic shaped by more than 1,000 brands since 2019, so the software fits the operation without giving up speed or reliability.

**Headline (revised again Oct 13, supersedes the two versions before it):** AI just raised the bar for inventory planning

AI now leads the message. This reverses the October discussion's "AI is an enabler, not the headline" and the "Code is cheap" version. The emotion is FOMO: brands that plan with AI weigh far more variables per decision and hand off the work around it, and the rest fall behind. The rule that keeps it from being wallpaper: every AI claim names the variables it weighs (sales, stockouts, promotions, ad spend, supplier delays, cash) or the work it takes on, and the hero carries approved result numbers, not a promise of "getting inventory right". "Software" is still never used for Flieber. A/B variant: "Your competitors are planning inventory with AI. Are you?". Full homepage copy: Claude Doc "Flieber homepage: structure and copy".

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

**One offer, one entry (revised Oct 13 after the Comp benchmark).** The hero sells Flieber, not a menu. Run is the default route, because it is what most buyers want on day one and what current customers pay for. Build is visible above the fold as a secondary path, not as an equal door. Services don't appear in the hero.

**Primary button:** Get your free inventory health check (→ trial signup; see B4.9)

**Secondary button:** Book a demo

**Line under the buttons:** 14-day free trial · No credit card · Monthly contracts · Setup included

**Build path, directly under it** (a single line with a link, visible without scrolling): Building your own tools or agents? Start from Flieber's data and inventory logic → /build

### B4.2 Logos

**Label:** Trusted by hundreds of brands. As today.

### B4.3 The problem

**Label:** Why Flieber

**H2:** Not a tool you work around. Not a build from scratch. Not more spreadsheets

**Lead:** Most brands try one of three fixes for inventory planning. Each one breaks in the same place: the data and the logic under the decisions.

Three cards:

1. **Off-the-shelf software** Built for the average brand. Your team bends its process around it, uses a fraction of it and drifts back to spreadsheets.
2. **Building it yourself with AI** Fast to start, but it covers today's cases. Every new channel, bundle or supplier means rebuilding the data and logic under it.
3. **More hands on spreadsheets** More planners, analysts or consultants add hours, not a system. The work stays manual, and the knowledge leaves when they do.

**Under the cards:** Flieber is inventory software that works the way you do, on data and planning logic that stay right as you add channels, products or suppliers.

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

*Under:* Our planners work on Flieber, not on spreadsheets, so what they set up keeps working after every meeting. Same platform either way. Switch or combine any time.

**Entry offer (added after the Comp benchmark):** the free inventory health check. It is the 14-day free trial packaged with a defined result, so the buyer signs up to learn something about their business, not to learn a tool. Every item comes from a feature that exists today. Comp's diagnosis takes two weeks and a senior expert. Flieber's runs on connected data, which shows off the data edge Comp doesn't have.

**Label:** Free inventory health check

**H2:** See what your inventory data is hiding

**Lead:** Connect your channels and Flieber checks your inventory on your own data, free for 14 days. No credit card, no demo call.

What you get:

- **Data issues** Listings not mapped to a product, bundles without components, discontinued products still forecast and inbound shipments that never reached the balance.
- **Stockouts ahead** The products that run out before their next purchase order lands, and by how many days.
- **What stockouts cost you** Lost sales last month, in units and revenue, by product and channel.
- **Cash tied up** Overstocked products and the inventory value at stake.

**Under the list:** Flieber shows your price as soon as onboarding is done, before you pay anything. **[Confirm: the four results are produced automatically during the trial without setup by Flieber's team; native integrations only]**

*Buttons:* Get your free health check · Book a demo

**For complex brands:** "Many channels, warehouses or bundles? Book a demo and one of our planners will walk through your health check with you." This is the entry to Managed Services, the equivalent of Comp's diagnosis. **[Confirm: planner time per review call]**

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

**Section "Free tools" (added after the Comp benchmark; all [Confirm]):** H2 "Start with free tools" · Comp uses free tools (an AI maturity diagnosis, Claude Skills for CHROs, a benchmark) as its top of funnel. Flieber's version doubles as agent discoverability:

- **Claude Skills for inventory planners** Ready-made skills for stockout checks, reorder points and bundle demand that run in Claude, and work better connected to Flieber.
- **Stockout cost calculator** Estimate what stockouts cost you, then connect your store to see the real number in the free health check.
- **Working app templates** As in "What you build on", once one ships.

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
| /managed-services | Linked from Run and from the health check, not from the hero. Add a "Meet the planners" section after "How our planners work with you": name, role, background, and the categories and number of brands each has planned (after Comp, which makes its experts the proof). Add the line "Our planners work on Flieber, not on spreadsheets, so what they set up keeps working." **[Confirm: consent from each planner; D11]** |
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
| Health check results are produced automatically during the trial | B4.1, B4.9 | Each item maps to an existing feature (P34, P4, P31, P30); confirm they run without setup by Flieber's team |
| Claude Skills for inventory planners, stockout cost calculator | /build free tools | Do not exist yet |
| "Trusted by hundreds of brands" and "more than 1,000 brands since 2019" | Logo label, founder block, /who-we-are | Both approved, but define them: cumulative brands since 2019 vs current customers. If current paying customers are well below "hundreds", change the logo label to "More than 1,000 brands have planned on Flieber since 2019" |
| Named planners and their track record | /managed-services | Needs consent and Fabricio's approval |

## B9. Decisions needed from Fabricio

1. **Template at launch.** Will one working template (recommend replenishment) ship before the site goes live? If not, Build launches with three blocks.
2. **What is open and what is hosted.** Recommendation: app code open, inventory logic and connected data hosted. That keeps the moat where AI can't reproduce it.
3. **Layer-by-layer purchase.** Beyond the data layer alone (approved), which layers can be bought without the others today?
4. **Run packaging.** Individual tools, or all four with the price driven by what's turned on and data volume? Recommendation: keep one account and one metric ("Priced to your operation") and avoid credits until usage data shows a need.
5. **Pricing in one line.** Proposed, for /pricing, /agents and llms.txt: "Software priced by your data volume and the tools you turn on, shown as soon as onboarding is done. Planners quoted per brand, engineers per project." Volume-based for the software and scope-based for services: that answers the benchmark's "retainer or volume" question with both, each where it fits.
6. **Public MCP URL date.** Gates the Build launch.
7. **Cross-brand patterns.** Is anonymized, aggregated insight from 1,000+ brands a product, and is it compatible with "never sold or shared"? Legal review before any mention.
8. **Founder statement.** Approve or rewrite B4.8.
9. **Headline test.** Approve running "Ready-made inventory planning you can change to fit" as the A/B variant.
10. **Custom build ownership.** Who owns what Flieber's engineers build: the customer or Flieber? Recommendation: the customer owns its configuration and data, and Flieber keeps the right to turn the generic parts into templates. That is how the template library grows (Comp's reusable modules point the same way).
11. **Named planners.** Reverse the "no team list" rule for /managed-services only? Recommended if services stay a paid option sold through a demo, because the buyer of a planner wants to see the planner.
12. **Hero entry.** Approve the free inventory health check as the primary call to action, replacing "Start free trial" in the hero only. "Start free trial" stays everywhere else until the health check is confirmed to run automatically.
