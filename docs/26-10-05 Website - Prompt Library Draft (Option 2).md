# 26-10-05 Website - Prompt Library Draft (Option 2)

Draft for Fabricio's approval, October 5, 2026. Once approved, it becomes section 15 of the Content Briefing (Option 2) and is built on the preview. Nothing here is on the site yet.

Sources: the "Prompt Examples" section of 26-05-29 AI Lab - Product Strategy (27 prompts), the example requests already approved on /features (drawn from the same document) and the prompts already on the homepage, /mcp and the use-case pages. Every "What Flieber does" line uses only capabilities listed on /features; entries that depend on anything else are marked **Confirm**.

## 15.1 Why the page exists

Operators are not used to what AI can do with their own data. The library shows it in their words: what to type, what Flieber does with it and what comes back. It is also the single source of example prompts for the whole site (decided Oct 5): the homepage, /features, /mcp and the use-case pages show a few entries each, pulled from the library, and link to it. One update refreshes every page.

AI Lab usage can later tell us which prompts customers actually run, to decide what to add or rewrite. Prompts are never copied from customer accounts; every entry is written in generic form (decided Oct 5; no live feed for now).

## 15.2 Page

- **URL:** /prompts
- **Name:** Prompt library
- **Navigation:** Product menu, first item after the divider: Prompt library · Integrations · MCP and AI agents · Security & data. Footer, Product column, after Features.
- **Label:** Product · Prompt library
- **H1:** Ask Flieber anything your operation depends on
- **Lead:** Type a question or describe a job in plain language, in the Flieber app, in Slack or in Claude, ChatGPT or any MCP-compatible agent. These are prompts operators use today, what Flieber does with each one and what you get back.
- **Filters:** by goal (the nine groups below) and by module (Data layer, Demand forecasting, Inventory forecasting, Replenishment, Workflows). Without JavaScript, all entries show, grouped by goal.
- **Note under the filters:** "Some prompts need a connection or a workflow set up for your account. On a demo we'll show which ones run on your setup today." (the approved /features note)
- **Closing:** H2 "Try these on your own data" · Body "Start a 14-day free trial, connect your channels and ask your first question in minutes." · *Buttons:* Start free trial · Book a demo
- **Structured data:** WebPage plus ItemList (one item per prompt). No prices.

## 15.3 Entry format

Each entry is a card:

- **Prompt** in the monospace font, with a copy button
- **What Flieber does:** two to four steps
- **What you get:** one line
- **Tags:** goal · modules · *Runs once* or *Runs on schedule* · approval (*Read only*, *Asks before changing anything* or *Changes after your approval*) · connection needed, if any

Everything works in the Flieber app, in Slack and in any MCP-compatible agent, so the card doesn't repeat it. Scheduled prompts use Workflows (custom workflows and agents).

## 15.4 Entries

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

## 15.5 Where the library feeds other pages

| Page | Today | With the library |
| --- | --- | --- |
| Homepage, "What you can do with it" | Six hand-written prompts | Six entries (P4, P14, P22, P6, P32, P23), each linking to its card; "See all prompts →" /prompts |
| /features, "Example requests" | Twelve prompts | The same twelve, now library entries (P1, P5, P11, P16, P20, P13, P30, P24, P21, P32, P26, P2), plus "See all prompts →" |
| /mcp, "What you can ask" | Three prompts per module | Three entries per module from the library |
| Use-case pages, "Ask Flieber" | Two prompts each | Two matching entries each |
| /vibe-coders, "What you can build" | Four build ideas | Unchanged (they describe tools to build, not prompts) |

The /mcp example conversations stay as they are: they show answers with sample numbers, which the library does not.

## 15.6 Machine-readable files

- **/llms.txt:** a "Prompt library" line with the URL.
- **/llms-full.txt:** every entry in full.
- **/capabilities.json:** `"prompts": [ { "id": "P1", "title": "string", "prompt": "string", "modules": ["string"], "schedule": "once | scheduled", "approval": "read_only | asks_first | after_approval", "connections": ["string"] } ]`, excluding entries still marked Confirm.
- **/agents:** one line under "Capabilities" pointing to /prompts.

## 15.7 For Fabricio to decide

1. Approve the page (URL, name, menu position, H1, lead, closing).
2. Confirm or drop the five entries marked **Confirm**: P19 cross-system reconciliation, P27 freight ETA updates, P28 3PL receiving reports, P29 invoices and landed cost, P36 Amazon availability issues. Until confirmed they stay off the site.
3. Any prompts AI Lab users run often that are missing here.
