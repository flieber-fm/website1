# 26-10-14 Website - Content Briefing (Option 6)

Copy for Option 6 of the new flieber.com, written October 14, 2026 to match the built preview. Option 6 follows the 26-10-14 Flieber Website Development Brief (the "source brief", in this folder) as its main direction. Option 2 (26-10-05 briefings, also in this folder) supplies structure, UI and approved claims wherever the two do not conflict.

## 0. How to use this brief

- The repo (flieber-fm/website1, branch claude/option-6) is the source of truth for the built page. This brief and the Technical Briefing (Option 6) stay in sync with it and with each other.
- The source brief calls its copy "a starting point for review". Where this brief changes that copy, the change is listed in section 3.
- House style (as in Option 2): no em dashes; sentence-case headings; no final period on any heading or title; no serial comma; no added marketing fluff; never mention the founders' other companies.
- Never invent numbers, customers, URLs, integrations or security claims. Every claim on the page is either in Option 2's "Approved facts and claims" or listed as open in the Technical Briefing (Option 6).
- Never say "run it for you" about the planners. The source brief adds: avoid implying that Flieber owns purchasing decisions or executes every supply-chain task.

## 1. Positioning (context, do not publish verbatim)

From the source brief: Flieber helps brands create an inventory planning system that works the way their business operates, backed by an established planning foundation and specialists who can help build and run it.

One offer, three ways to get help, on one foundation:

- **The foundation:** Flieber's data connections, business context and forecasting and replenishment logic, plus the Flieber app as a ready-made starting point.
- **Tailor it with our team:** Flieber learns how the customer plans and builds the views, workflows and reports it needs.
- **Build it with your own team:** the customer's developers or AI tools build on the foundation through the API and MCP server.
- **Add ongoing planning support (optional):** Flieber's planners work alongside the customer's team. Decisions stay with the customer.

Audience: commerce brands whose inventory complexity has outgrown their current team. The page lets visitors pick their level of help without assuming size decides it. AI is explained through what it enables; "vibe coding", "agents" and "MCP-native" are not used in the first screen.

## 2. Homepage copy

One page, top to bottom. Each section after the hero opens with a small uppercase label above its H2.

**Page title:** Flieber: inventory planning built around your business

**Meta description:** Build the views and workflows your team needs on Flieber’s data and planning foundation. Get help tailoring your system, and add ongoing planning support when you need it.

### 2.1 Navigation

**Review banner (preview only, above the nav on every page):** Review build · Option 6 · Oct 14 development brief on Option 2’s design

How it works · Your options · Examples, then Log in (text link to app.flieber.com) and a yellow "Talk to us" button (to #talk). On phones the three links and Log in collapse into the menu; "Talk to us" stays visible.

### 2.2 Hero

**Eyebrow:** Inventory planning for commerce brands

**H1:** Inventory planning built around your business

**Subhead:** Build the views and workflows your team needs on Flieber’s data and planning foundation. Get help tailoring your system, and add ongoing planning support when you need it.

**Buttons:** Talk about your planning needs (primary, to #talk) · See how it works (secondary, to #how-it-works)

**Under the buttons:** Your team keeps the final say · Ongoing support is optional · Planning with commerce brands since 2019

**Hero card** (static, dark, no animation): "Monday purchasing review", badge "Concept · sample data", line "Grouped by supplier, the way your buyers order, with your rules applied." Supplier A (MOQ 500 · lead time 45 days) with four rows:

| Product | Days of cover | Suggested order | Status |
| --- | --- | --- | --- |
| Travel kit | 9 | 1,800 | Order now |
| Gift bundle | 14 | 600 | Review |
| Hero serum | 41 | 0 | On track |
| Refill pack | 112 | 0 | Excess |

**Your rule:** Keep 30 days of cover on Amazon. The travel kit order covers it until the next PO, and waits for your approval.

**Caption:** Illustration with sample data, not a product screenshot.

### 2.3 Logos

**Label:** Trusted by hundreds of brands. The 14 approved customer logos, as in Option 2.

### 2.4 Recognizable planning problems

**Label:** Sound familiar?

**H2:** Your team knows the business. It’s running out of hours

**Lead:** Most planning teams don’t lack judgment. They lack time, because the work around each decision keeps growing faster than the team.

1. **The spreadsheet gets rebuilt every week** Someone exports sales, pastes in stock levels and fixes the formulas again before anyone can start planning.
2. **Information is scattered across systems** Marketplaces, your store, the ERP, the 3PL and supplier emails each hold part of the picture.
3. **Standard software doesn’t fit how you plan** Your bundles, suppliers and approval steps don’t match the tool, so the real plan stays in spreadsheets.
4. **Firefighting leaves no time to improve** Stockouts and surprise overstock take up the week, so the planning process never gets better.

### 2.5 How it works (`#how-it-works`)

**Label:** How it works

**H2:** What sits underneath your system

**Lead:** Every view and workflow your team uses runs on the same foundation, so the team stops assembling data and starts from numbers it can trust.

1. **Connected data** Sales, orders, inventory and shipments from your channels, warehouses, 3PLs and suppliers, reconciled into one record and kept current. *Note:* Amazon, Shopify, Walmart, TikTok Shop, eBay, Etsy, BigCommerce and Google Sheets connect in one click. ERPs such as NetSuite, EDI through SPS Commerce, accounting systems and more than 20 3PL and warehouse systems are set up by our team.
2. **Business context** Which listings are the same product, which components make a bundle, which supplier ships to which warehouse and what a stockout did to last month’s sales.
3. **Forecasting and replenishment logic** Forecasts by product and channel, corrected for stockouts and promotions, and purchase and transfer recommendations within your MOQs, case packs, lead times and cash. Proprietary algorithms, not language models, do the math.

**Annotated view** (light card, sample data, markers 1 to 3 matching the list): "Travel kit · all channels". (1) Sales, last 30 days: Amazon 1,240, Shopify 610, Wholesale 400. (2) Context applied: Sold alone and in 3 bundles · 6 stockout days adjusted · Ships from Supplier A to the 3PL. (3) Next 90 days: Forecast demand 7,050 · On hand and inbound 3,900 · Suggested order 3,000; "Rounded to the MOQ of 500 and timed for a 45-day lead time." Caption: Illustration with sample data, not a product screenshot.

**Where AI helps** AI lets us tailor views and workflows to your team quickly, takes repetitive work off your planners and makes our support faster. It explains results in plain language; the math stays in the planning engine.

**You stay in control** Nothing changes in your systems without passing the approval rules you set. By default, every change requires approval. *Link:* How we handle your data → /security

### 2.6 Your options (`#options`)

A decision tree in three steps (Fabricio, Oct 14), then a summary of the chosen path. Every choice is readable without JavaScript; with it, picking a path fills the summary.

**Label:** Your options

**H2:** Choose how much help you need

**Lead:** Three decisions shape your system, and every path runs on the same foundation. Ongoing services are always optional, and you can change any decision later.

**Step 1 · How do you want to start?**

- **Use it as it is** Plan with Flieber’s ready-made templates for planning views, reports and workflows, in the Flieber app. *Good fit if a standard planning routine works for your team.*
- **Customize it** Adapt the views, workflows and reports to how your team plans, your products and your rules, on the same foundation. *Good fit if standard software has never matched how you plan.*

**Step 2 · only if you customize · Who builds it?** (dimmed, with "Skipped: you’re using Flieber as it is.", when step 1 is "Use it as it is")

- **Our team** We learn how you plan, agree the scope with you and build the views, workflows and reports your team needs. Your team explains how it plans and reviews what we build.
- **Your team** Your developers, or the AI tools your team already uses, build on Flieber’s data and planning logic through our API and MCP server. Claude, ChatGPT and Cursor connect directly.

**Step 3 · in every case · Do you want ongoing planning support?**

- **Add Managed Services** (tag: Optional) Flieber’s planners work alongside your team on day-to-day planning, with dashboards that keep the work visible. They keep the data accurate, prepare the analysis, join your S&OP meetings and act as a sounding board. Your team makes every decision.
- **Run it with your own team** Your team plans in Flieber on its own. You can add Managed Services later if you need more capacity.

**Your path** (dark summary): before a full path is chosen, "Choose an option in step N to see what your path includes." Then the path name ("Use it as it is" / "Customized by our team" / "Customized by your team", followed by "with Managed Services" or "run by your own team") and three lists:

| Choice | Flieber | Your team | You pay for |
| --- | --- | --- | --- |
| Every path | | | The Flieber platform |
| Use it as it is | Connects your data and sets up the ready-made templates | Plans with the templates in the Flieber app | |
| Customized by our team | Learns how you plan, agrees the scope with you and builds what was agreed | Explains how it plans today and reviews what we build | Customization by our team, quoted once the scope is agreed |
| Customized by your team | Keeps the data connected, mapped and current, and supplies the planning logic through the API and MCP server | Builds and maintains its own views, workflows and tools | |
| With Managed Services | Planners keep the data accurate, prepare the analysis, join your S&OP meetings and act as a sounding board | Makes every decision; if you choose, our planners carry out what you approve | Managed Services |
| Run by your own team | | Runs planning day to day, and can add Managed Services later | |

*Button:* Talk about your planning needs (goes to the form and ticks the matching interests).

**How pricing works:** Every path includes the Flieber platform. Customization by our team and Managed Services are priced separately, so you only pay for what you choose. We share pricing in the first conversation, once we understand your operation. *Button:* Talk about your planning needs

### 2.7 Examples (`#examples`)

**Label:** Examples

**H2:** What a tailored system can look like

**Lead:** Three concepts built from what planning teams ask for. Each one shows what changes for the people using it.

Each card has a small dark mock, the label "Concept · sample data", a title and "What changes":

1. **A replenishment view built around your purchasing routine** (mock: Supplier A, ships every 6 weeks; Travel kit 1,800, Gift bundle 600, Hero serum 0; container fill 82%). What changes: your buyer opens one view each Monday, grouped the way they order, instead of rebuilding a spreadsheet.
2. **A dashboard of the products that need attention** (mock: 4 of 312 products; Travel kit stockout in 12 days, Refill pack 180 days of cover, Hero serum sales 40% above forecast, Gift bundle inbound 9 days late). What changes: the team starts the day with the few products that need a decision, not every row in the catalog.
3. **A workflow that applies your own rules** (mock: wholesale order received, 1,800 units → your rule: keep 30 days on Amazon → recommendation: 1,100 now, 700 after the next PO → waiting for your approval). What changes: your rules are applied the same way every time, and nothing is ordered or shipped until someone on your team approves it.

### 2.8 How an engagement works

**Label:** Working together

**H2:** How an engagement works

**Lead:** No two teams plan the same way, so we agree on the scope before anything is built.

1. **Talk through your planning.** How you plan today, where it breaks down and what you want to improve.
2. **Agree on scope and responsibilities.** What we build, what your team builds or runs and how each part is priced.
3. **Configure or build the agreed system.** We set up the views and workflows on your data, and your team reviews them.
4. **Decide on ongoing support.** Run the system with your own team, or add our planners. You can change this later.

No timelines (source brief, section 6).

### 2.9 Questions

**Label:** Questions

**H2:** What teams ask us first

Collapsible, as the Option 2 /pricing FAQ. Also published as FAQPage structured data.

- **What can Flieber help me do, and what will my team still handle?** Flieber connects and reconciles your data, forecasts demand, projects inventory and recommends what to buy or move, in views and workflows that fit how you plan. Your team sets the objectives, adds what no system knows and makes every decision that commits cash. If you add ongoing support, our planners help with the analysis and the planning routine; the decisions stay with you.
- **Can I use Flieber without ongoing services?** Yes. Ongoing planning support (Managed Services) is a separate, optional engagement. Your team can use Flieber as it is, or any system you customize, on its own.
- **What can be tailored, and how do we agree on scope?** Views, reports, dashboards and workflows, built around your process and rules on top of Flieber’s shared data connections and planning logic. Before any work starts, we agree on what will be built, who maintains it and how it’s priced.
- **If my own team builds or runs the tools, what do I keep paying Flieber for?** Ongoing use of the Flieber platform: the data connections, business context and planning logic your tools run on. Customization by our team and Managed Services are charged separately, and only if you choose them.
- **How much does it cost?** It depends on your operation and on the help you choose. We share pricing in the first conversation, once we understand how you plan.
- **Does my team need to know AI to use Flieber?** No. Your team works in views built for how it plans. AI works in the background: it speeds up tailoring, takes repetitive work off your team and explains results in plain language.
- **Can Flieber change anything in our systems on its own?** Only within the approval rules you set. By default, every change Flieber makes to your systems requires approval.

### 2.10 Proof

**Label:** Proof

**H2:** What brands get from planning with Flieber

**Lead:** More than 1,000 commerce brands have planned with Flieber since 2019.

Then, as in Option 2: the four customer results (+38% increase in sales, -62% reduction in stockouts, -17% reduction in excess inventory, -88% less time on replenishment decisions; "Average across customers using Flieber for 12+ months"), the accuracy stat (36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products; built with Nixtla, the team behind the TimeGPT forecasting model), the five approved quotes and "Read more reviews on G2".

### 2.11 Security

As in Option 2: label "Security", H2 "Your data stays yours", the four items (Never sold or shared · No training on your data · Encrypted on AWS · Changes follow your rules) and "How we handle your data →" to /security.

### 2.12 Talk to us (`#talk`)

**Label:** Talk to us

**H2:** Tell us how you plan today and what you want to improve

**What happens next:**

1. We read your note and reply by email to arrange a first conversation.
2. In that conversation we go through how you plan today and what you want to change. No preparation needed.
3. If there’s a fit, we propose a scope and pricing for the help you chose. Nothing is agreed until you say so.

**Alternative:** Prefer to pick a time now? Book a call → https://www.flieber.com/book-a-demo

**Form:** Name · Work email · Company · "How do you plan today, and what do you want to improve?" (hint: "A few sentences is enough. Please don’t include passwords or data files.") · "What are you interested in? (optional, choose any)", checkboxes matching the tree: Using Flieber as it is / Customizing it with Flieber’s team / Customizing it with our own team / Ongoing planning support (Managed Services) / Not sure yet. Button: Talk about your planning needs. Under it: "By sending this form you agree to our Privacy Policy." Preview only: "Preview: this form doesn’t send anything yet. Its destination is set before launch."

**Errors:** Please enter your name. · Please enter a valid work email, like name@yourbrand.com. · Please enter your company. · Please tell us a little about how you plan today.

**Confirmation:** Thanks, [first name]. Your note is in · We’ll reply by email at [email] to arrange a first conversation.

### 2.13 Footer

**Tagline:** Inventory planning built around your business.

**Columns:** On this page (How it works, Your options, Examples, Talk to us) · Company (Security & data, Blog, hello@flieber.com, Privacy, Service agreement) · Customers (Log in, Help center). 169 Madison Avenue, New York, NY 10016.

## 3. Changes to the source brief's proposed copy

| Source brief | Option 6 | Why |
| --- | --- | --- |
| "Flieber's data, integrations, and planning logic" (and other lists with a comma before "and") | No serial comma | House style |
| Section 4 options "tailor with our specialists; build with your own resources where supported; add ongoing planning help" | "Tailor it with our team", "Build it with your own team", "Add ongoing planning support", each with what Flieber does and what your team does | Answers "what will my team still handle?" on the card itself; "where supported" is made concrete (API and MCP server, Claude, ChatGPT and Cursor, all approved in Option 2) |
| Section 4 options and "a ready-made starting experience can be added if its availability is confirmed" | A three-step decision tree: use the templates as they are or customize; if customizing, our team or yours; in every case, Managed Services or not | Fabricio's direction, Oct 14. "Ready-made templates" is his wording and still needs confirming as an available product |
| Section 7 "Close with: Tell us how you plan today and what you want to improve" | Used as the H2 of the closing section | Heading, so no final period |
| Nav "Talk to us" | Yellow button; the in-page buttons say "Talk about your planning needs" | The long label does not fit the nav |
| Questions the website must answer | A "Questions" section with seven answers, plus FAQPage structured data | The four required questions, plus price, AI and control |
