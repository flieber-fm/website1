"""Single source for /features, /agents, llms.txt, llms-full.txt and capabilities.json.

Option 2 (Collaborative AI). Copy comes verbatim from "26-10-02 Website - Content Briefing"
(Option 1, sections 4 to 6) with the changes in "26-10-02 Website - Content Briefing (Option 2)"
(sections 5 to 8).
Edit here, then run: python3 scripts/build-content.py
"""

LAST_UPDATED = "2026-10-02"
LAST_UPDATED_TEXT = "October 2, 2026"

SITE = "https://www.flieber.com"
DEV_DOCS = "https://app.flieber.com/app/developers"
TRIAL = "https://www.flieber.com/free-trial"
DEMO = "https://www.flieber.com/book-a-demo"
G2 = "https://www.g2.com/products/flieber/reviews"
PRIVACY = "https://www.flieber.com/privacy-policy"
SERVICE = "https://www.flieber.com/service-agreement"
EMAIL = "hello@flieber.com"

ACCURACY = ("36% more accurate than our previous portfolio of 16 forecasting models, tested on a random "
            "sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model.")

POSITIONING = "The inventory intelligence layer your agents run on"

# ---------------------------------------------------------------- /features
FEATURES_H1 = "Collaborative AI for every inventory decision"
FEATURES_INTRO = ("Flieber keeps a current picture of how your business works, recommends your next move and acts on it, "
                  "together with your team, your agents and your systems. Five modules cover the way from your data to a decision you can act on. Every "
                  "feature works the same whether you use it in the Flieber app, ask for it in plain language, or call it "
                  "from your own agents and systems through MCP or API.")
FEATURES_NOTE = ("Available with Flieber Self-Serve and Flieber Managed Services. During the 14-day free trial, data "
                 "comes in through native integrations; assisted integrations and simple customizations come with a paid plan. "
                 "Features marked \"on request\" are rolling out and are switched on when you ask.")

# Grouped by module (Option 2 brief, section 7). Every Option 1 feature card is kept; "Reports and dashboards"
# is new. "Connect your sales channels and inventory" is listed in the brief without a description; it uses the
# approved integrations wording from the Technical Briefing. "Data health" is not in the brief's lists but is kept,
# since the brief keeps every Option 1 card. "Sales order routing" is new and has no card copy in the brief;
# its description is the routing sentence from the data layer page lead. Each group's lead is the module page lead (access: its own lead).
# access: read | write | read_write | None ; availability: general | on_request
GROUPS = [
    {
        "id": 'data-layer', "label": 'Data layer', "h2": 'Your commerce data, consolidated, contextualized and current',
        "lead": None, "module": True,
        "features": [
            ('Connect your sales channels and inventory', "Flieber connects to pretty much any system through native and assisted integrations, plus MCP and API. Native integrations work during the free trial; assisted integrations are set up by Flieber's team on a paid plan.", 'read', 'general'),
            ('Data health', 'Checks your account for issues, gaps and anomalies, applies the fixes it can and flags the ones that need a person.', 'read_write', 'general'),
            ('Cross-channel SKU mapping', 'Links listings and SKUs across channels to one master product, so sales consolidate for planning. Automatic matching, plus bulk catalog import and export.', 'write', 'general'),
            ('Sales order routing', 'Route sales orders from any store to the regions or warehouses you choose, so one Shopify account can be planned as several regional markets.', 'write', 'general'),
            ('Kits, bundles and components', 'Turns demand for bundles into component requirements. Buy at component level and transfer inventory as finished products.', 'write', 'general'),
            ('Product configuration and classification', 'Product status, custom attributes, costs, prices and packaging units. ABCD classification ranks products by sales, units or profit using your thresholds.', 'write', 'general'),
            ('Supply chain map', 'Suppliers, warehouses, 3PLs and channels, with fulfillment and fallback locations, transfer routes, production and transit lead times and ordering cadence.', 'write', 'general'),
            ('Sales history adjusted for anomalies', 'Corrects history distorted by stockouts, spikes and promotions, and shows actual sales next to the adjusted demand used for forecasting.', 'read', 'general'),
            ('Inventory history and balances', 'Snapshots and balances across every connected location, including inbound and in-transit stock.', 'read', 'general'),
            ('Reports and dashboards', 'Report sales by product and channel, inventory history and value, projected revenue and forecast performance, and build your own dashboards with live alerts and scheduled delivery.', 'read', 'general'),
            ('Uploads and Google Sheets', 'Bulk updates to catalog, forecasts, shipments, bundles and wholesale data through CSV files or Google Sheets, with a preview before anything is saved.', 'write', 'general'),
            ('Organizations and users', 'Manage several organizations from one place, with unlimited users on every plan and Admin and Member roles.', 'write', 'general'),
        ],
    },
    {
        "id": 'demand-forecasting', "label": 'Demand forecasting', "h2": 'Forecast what would have sold, not just what did',
        "lead": None, "module": True,
        "features": [
            ('AI demand forecasts', 'Product and channel level forecasts across marketplaces, DTC and wholesale, built from adjusted history and seasonality. 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model.', 'read', 'general'),
            ('Forecast overrides and uploads', 'Import your own forecasts, or adjust at SKU, store, channel or group level, including planned promotions and events.', 'write', 'general'),
            ('Targets and new products', 'Apply growth percentages, unit targets or revenue targets across selected products. Forecast new products from similar ones or from a manual curve.', 'write', 'general'),
            ('Forecast accuracy and bias', 'Error and bias metrics, with monthly forecast versions saved so past predictions can be compared with what actually sold. Forecast value added reports on request.', 'read', 'general'),
            ('Wholesale forecast reconciliation', 'Finds wholesale demand parked on dates that passed without a sale and suggests where to move it. On request.', 'read_write', 'on_request'),
        ],
    },
    {
        "id": 'inventory-forecasting', "label": 'Inventory forecasting', "h2": 'See stockouts and overstock before they happen',
        "lead": None, "module": True,
        "features": [
            ('Inventory projections', 'Stock by product, channel and location from on-hand, inbound and forecast demand, with days of cover and consolidated warehouse needs.', 'read', 'general'),
            ('Stockouts, overstock and lost sales', 'Projected stockout dates, products below safety stock, excess inventory and the sales lost to unavailable stock or late shipments.', 'read', 'general'),
            ('Backorders and preorders', 'Counts accumulated backorder demand in inventory and replenishment calculations, with settings at the product and store level, and plans for products sold before they arrive.', 'read', 'general'),
        ],
    },
    {
        "id": 'replenishment', "label": 'Replenishment', "h2": 'Know what to buy, how much and when',
        "lead": None, "module": True,
        "features": [
            ('Purchase and transfer recommendations', 'What to order or transfer, how much and when, by product and location, including replenishment from warehouses or 3PLs to fulfillment locations such as FBA.', 'read', 'general'),
            ('Planning parameters', 'Safety stock, target days of cover, overstock thresholds, lead times and order frequency, with rules for products, categories and channels.', 'write', 'general'),
            ('Order and shipping constraints', 'Minimum order quantities and supplier constraints, container planning and rounding to case packs, cartons or pallets.', 'read', 'general'),
            ('Decision simulations', 'Test changes to order quantities, demand, arrival dates or lead times and see the effect on inventory, revenue, margin and cash before anything is committed.', 'write', 'general'),
            ('Multi-month purchase planning', 'Splits a long buying horizon into seasonally weighted purchase orders, with cartons, MOQs and lead times applied and periods already covered by stock left at zero.', 'write', 'general'),
            ('AI order-quantity adjustments', 'Rebalances planned quantities across destinations and fits orders to container capacity, budget and cash-flow limits, following notes you write in plain language.', 'write', 'general'),
            ('Saved plans and purchase orders', 'Replenishment plans by supplier and date, with costs. Create and track POs, group them under master POs and record placed-order status.', 'write', 'general'),
        ],
    },
    {
        "id": 'workflows', "label": 'Workflows', "h2": 'From approved decision to done',
        "lead": None, "module": True,
        "features": [
            ('Purchase orders to suppliers', "Sends each PO straight into the supplier's system or as an email, CSV file or Google Sheet in the supplier's own format, with products identified by SKU or product name.", 'write', 'general'),
            ('Purchase orders to ERPs', 'Pushes approved POs into NetSuite or light ERPs such as Cin7 and Brightpearl.', 'write', 'general'),
            ('Inbound shipments in Amazon and 3PLs', 'Creates inbound shipments in Amazon and in connected 3PL and warehouse systems from an approved plan.', 'write', 'general'),
            ('Inbound shipment tracking', 'Follows POs and shipments through delivery, with manual entry, Google Sheets sync and automatic import of connected inbound shipments such as Amazon FBA.', 'read', 'general'),
            ('Alerts and scheduled reports', 'Scheduled checks for stockout risk, excess inventory and orders due, delivered by email, Slack, Microsoft Teams or Google Sheets.', 'write', 'general'),
            ('Custom workflows and agents', 'Describe a recurring job in plain language and Flieber runs it on schedule, across its own data and your connected apps.', 'write', 'general'),
            ('Actions in other systems', 'Flieber is also an MCP client, so it can connect to any system with an MCP server and act where the decision lands: adjust an ad campaign, update a price, confirm with a supplier.', 'write', 'general'),
        ],
    },
    {
        "id": 'access', "label": 'Access', "h2": 'Use it your way',
        "lead": 'Collaborative AI across all five modules, wherever you work', "module": False,
        "features": [
            ('Flieber app', 'Planning screens, saved views, dashboards and exports to CSV.', None, 'general'),
            ('Ask in plain language', 'Ask questions about your data and get answers, tables, charts and dashboards. Save reports, refresh them and keep the conversation going.', None, 'general'),
            ('Slack', 'Ask questions and receive alerts in Slack.', None, 'general'),
            ('Google Sheets add-on', 'Pulls Flieber data into your own sheets and refreshes it on a schedule.', None, 'general'),
            ('MCP server', "Connect Claude, Cursor or your own agents. Requests go to Flieber's own agent (Flieber Studio), which answers questions and carries out the same actions as the app, following your approval rules. Answers typically take 30 seconds to 5 minutes. Full action list in the MCP docs (customer login required).", None, 'general'),
            ('MCP client and connected apps', 'Flieber connects out to Gmail, Outlook, Slack, Microsoft Teams, Google Sheets, OneDrive, Notion, Airtable, Meta Ads, Google Ads and NetSuite, and to any other system with an MCP server.', None, 'general'),
            ('Public API', 'Programmatic access to Flieber data for your own systems. Details in the MCP docs (customer login required).', None, 'general'),
        ],
    },
]

APPROVAL_H2 = "Your team decides. Flieber does the work"
APPROVAL_BODY = ("Flieber prepares the decision; you decide how much it does without asking. By default, every change "
                 "Flieber makes, in Flieber or in your other systems, waits for your approval: you see a preview and "
                 "confirm. When you ask for a change in a conversation, Flieber always shows the preview first. For "
                 "scheduled workflows you choose: let a weekly export or a data update run on its own, and keep approval "
                 "on purchase orders. Change it any time. With Managed Services, Flieber's planners review decisions "
                 "with you before they go out.")

EXAMPLES_H2 = "What customers ask Flieber to do"
EXAMPLES_LEAD = ("A few of the requests customers run every day. Each one uses the features above; the ones that reach "
                 "outside Flieber need a connection to the system involved.")
EXAMPLES = [
    "Every morning, show me the biggest inventory risks by stockout risk, sales velocity, product tier and revenue impact, and tell me what to do about each.",
    "Every Monday, recommend what to order, grouped by supplier, with MOQs, lead times and target coverage applied.",
    "Flag products where the forecast looks wrong: new products with little history, products hit by stockouts and sudden accelerations.",
    "Recommend transfers when one location is about to stock out and another has excess, without creating a new risk at the origin.",
    "Before every promotion, check whether the promoted products have enough stock for the expected lift.",
    "Compare new launches with similar past launches at 7, 14 and 30 days and tell me whether to reorder earlier.",
    "Review overstocked products and recommend for each one: keep, discount, bundle, transfer, pause replenishment or liquidate.",
    "Watch supplier emails about open POs and update the PO in Flieber when a supplier confirms a new date or quantity.",
    "Alert the marketing team in Slack when ad spend rises on a SKU projected to stock out within 30 days.",
    "When a large wholesale order comes in, check whether it puts DTC or Amazon stock at risk and recommend whether to accept, split or delay it.",
    "Track which suppliers are repeatedly late, short-shipping or changing quantities.",
    "Every Monday, send me an inventory operations memo with the top risks, what changed and the decisions I need to make.",
]
EXAMPLES_NOTE = "Some of these need a connection or a workflow set up for your account. On a demo we'll show which ones run on your setup today."

FAQ_H2 = "Does Flieber support..."
FAQ = [
    ("Can I buy only the data layer?", "Yes. Teams building their own tools with AI can use Flieber's data layer on its own through MCP and API, and add the other modules any time."),
    ("Does Flieber handle kits and bundles?", "Yes. Bundle demand is converted into component requirements, and you can buy components and transfer finished goods."),
    ("Does Flieber plan Amazon FBA replenishment?", "Yes. It recommends transfers from warehouses or 3PLs to FBA, creates the inbound shipments in Amazon and tracks them to delivery."),
    ("Can Flieber send purchase orders to my ERP?", "Yes, to NetSuite and to light ERPs such as Cin7 and Brightpearl, following your approval rules."),
    ("Can Flieber send purchase orders to my suppliers?", "Yes. Flieber sends each PO straight into the supplier's system or as an email, CSV file or Google Sheet in that supplier's format."),
    ("Does Flieber account for MOQs, case packs and containers?", "Yes. Quantities are rounded to case packs, cartons and pallets, and orders can be fitted to container capacity."),
    ("Does Flieber correct sales history for stockouts?", "Yes. History distorted by stockouts, spikes and promotions is adjusted before forecasting, and actual sales stay visible alongside."),
    ("Does Flieber handle backorders and preorders?", "Yes, with settings at the product and store level."),
    ("Does Flieber plan wholesale orders?", "Yes. Wholesale channels connect through Google Sheets, file uploads or SPS Commerce EDI, and wholesale purchase orders count as allocated units."),
    ("Can I manage several brands or organizations?", "Yes, from one place, with unlimited users on every plan."),
    ("Can my own AI agent use Flieber?", "Yes. Claude, Cursor and any MCP-compatible agent connect through Flieber's MCP server; your systems can also use the public API."),
    ("Will Flieber change anything without my approval?", "Not by default. Every change waits for your approval until you set a workflow to run on its own."),
    ("Is Flieber a WMS, ERP or MRP?", "No. Flieber plans finished-goods inventory and connects to those systems; it doesn't replace them."),
]

NOT_FOR = [
    "You sell on one channel and a spreadsheet still works",
    "You're looking for a warehouse management system or a full ERP",
    "You plan manufacturing runs (MRP) rather than buying finished goods",
]
NEXT_H2 = "See it on your own data"
NEXT_BODY = ("Start a 14-day free trial, no credit card required, or book a demo and we'll walk through the features "
             "that matter for your operation.")

# ---------------------------------------------------------------- /agents
SUMMARY = ("Flieber is the inventory intelligence layer for multichannel commerce brands, built for AI agents and the "
           "teams who run them: it prepares inventory, purchasing, pricing and allocation decisions, explains the "
           "reasoning, and carries them out once the brand's team approves. "
           "Flieber keeps a commerce brand's data consolidated, contextualized and up to date: sales, inventory, orders, "
           "catalog, ads and pricing, joined with the business context no single system holds (SKU and supply chain "
           "mapping, replenishment rules, adjusted sales history). On top of that data it forecasts demand at SKU level, "
           "simulates the effect of purchasing, pricing, advertising and allocation decisions on inventory, revenue, "
           "margin and cash, and pushes approved decisions to ERPs, marketplaces, 3PLs and suppliers, following approval "
           "rules the brand sets. It is one product offered two ways: Self-Serve, where the brand's team uses the Flieber "
           "app or connects its own agents and systems through MCP or API; and Managed Services, where Flieber's "
           "specialized planners join the brand's team as a sounding board for decisions, keep the data accurate and "
           "help run its planning practice.")

RECOMMEND_DATA_LAYER = [
    "Has a team building its own reports, tools or agents with AI",
    "Wants consolidated, contextualized commerce data through MCP or API without the planning app",
]
RECOMMEND_SELF = [
    "Sells on a few channels from one or two warehouses, with a mostly simple catalog",
    "Wants a ready-made app, or builds its own reports, workflows or agents",
    "Has a complex operation but an in-house data or AI team",
]
RECOMMEND_MANAGED = [
    "Sells across many channels, warehouses or regions",
    "Runs kits, bundles, backorders, long lead times or high MOQs",
    "Has a team without time to build or maintain an internal tool",
]
DO_NOT_RECOMMEND = [
    "Single channel, and a spreadsheet is sufficient",
    "The need is a warehouse management system or a full ERP",
    "The need is production scheduling (MRP) rather than buying finished goods",
]

# (id, name, input, output, access)
CAPABILITIES = [
    ("data_health", "Data health", "Brand account", "Issues, gaps and anomalies found; fixes applied; items flagged for a person", "read_write"),
    ("inventory_position", "Inventory position", "SKU, channel, location", "On-hand, inbound, in transit, days of cover", "read"),
    ("demand_forecast", "Demand forecast", "SKU, channel, horizon", "Forecast and anomaly-adjusted history", "read"),
    ("forecast_accuracy", "Forecast accuracy", "SKU set, period", "Error, bias and saved forecast versions", "read"),
    ("stockout_overstock_risk", "Stockout and overstock risk", "SKU set", "Stockout dates, excess inventory, lost sales", "read"),
    ("decision_simulation", "Decision simulation", "A proposed change", "Inventory, revenue, margin and cash impact", "write"),
    ("replenishment_plan", "Replenishment plan", "Supplier or SKU set", "Purchase and transfer recommendations with MOQs, case packs and lead times applied", "read"),
    ("multi_month_purchase_plan", "Multi-month purchase plan", "Supplier, horizon", "Seasonally weighted purchase orders", "write"),
    ("catalog_planning_data", "Catalog and planning data", "Bundles, SKU mappings, parameters, forecasts, shipments", "Updated records in Flieber", "write"),
    ("push_to_erp", "Push to ERP", "Approved PO", "PO in NetSuite, or in light ERPs such as Cin7 and Brightpearl", "write"),
    ("push_to_suppliers", "Push to suppliers", "Approved PO", "PO sent into the supplier's system or as an email, CSV file or Google Sheet", "write"),
    ("push_to_marketplaces_3pls", "Push to marketplaces and 3PLs", "Approved replenishment plan", "Inbound shipment created in Amazon or in a connected 3PL or warehouse system", "write"),
    ("scheduled_agents", "Scheduled agents", "Plain-language rule", "Recurring report, alert, export or action", "write"),
    ("actions_connected_systems", "Actions in connected systems", "Plain-language request", "Action in any system with an MCP server", "write"),
]
APPROVAL_AGENTS = ("Every write follows approval rules the brand sets. By default every write requires approval: Flieber "
                   "shows a preview and waits for confirmation. Writes requested in a conversation always show a preview "
                   "first. The brand can let specific scheduled workflows run without confirmation.")

CONNECTED_APPS = ["Gmail", "Outlook", "Slack", "Microsoft Teams", "Google Sheets", "OneDrive", "Notion", "Airtable",
                  "Meta Ads", "Google Ads", "NetSuite"]

CONNECT = [
    ("Free trial", "14 days, no credit card required, on the brand's own data. Native integrations only during the trial; standard setup included. Assisted integrations and simple customizations require a paid plan.", TRIAL),
    ("MCP server", "Claude, Cursor and other MCP-compatible agents connect to Flieber's MCP server. Requests are handled in natural language by Flieber's own agent (Flieber Studio), which answers questions and carries out the actions the Flieber app supports, under the account's approval rules. Answers typically take 30 seconds to 5 minutes; a conversation can continue across calls. How it works, with example conversations: https://www.flieber.com/mcp. Full action list (customer login required):", DEV_DOCS),
    ("MCP client", "Flieber connects to any system with an MCP server. Built-in connections: " + ", ".join(CONNECTED_APPS) + ".", None),
    ("Public API", "Programmatic access to Flieber data. Details (customer login required):", DEV_DOCS),
    ("Demo", "", DEMO),
]

NATIVE = ["Amazon Seller Central", "Shopify", "Walmart (including WFS)", "TikTok Shop", "eBay", "Etsy", "BigCommerce", "Google Sheets"]
ASSISTED = [
    ("Sales channels and marketplaces", ["Shopify Plus", "Amazon Vendor Central", "Magento", "WooCommerce", "Mercado Libre", "bol.com", "PrestaShop"]),
    ("EDI", ["SPS Commerce"]),
    ("Accounting and finance", ["QuickBooks", "Xero", "Zoho"]),
    ("Inventory and order management", ["Cin7", "Sage", "Linnworks", "Brightpearl", "Luminous", "Finale", "DEAR Systems", "Fishbowl", "NetSuite", "Apparel Magic"]),
    ("3PLs and warehouses", ["SkuVault", "ShipStation", "Anvyl", "Flexport/Deliverr", "ShipBob", "ShipHero", "Extensiv", "Stord", "Veeqo", "Flowspace", "Everstox", "GoFlow", "Fulfil", "AMZ Prep", "Logiwa", "Unleashed", "ShipMonk", "3PLGuys", "Shipout", "EasyFulfillment", "CEVA Logistics", "World Depot Inc.", "ZhenHub"]),
]

PRICING_TERMS = [
    "**Flieber Self-Serve:** priced to your operation, based on features enabled and data volume; Flieber shows the price as soon as onboarding is done, before the brand pays anything.",
    "**Flieber Managed Services:** quoted per brand, after a conversation with a planner about channels, warehouses and where the process breaks down.",
    "Monthly contracts, no annual commitment.",
    "14-day free trial, no credit card required.",
    "Unlimited users on every plan, including the free trial.",
    "Standard setup included; customizations come with a paid plan.",
    "**Flieber's engineers (custom builds):** app customizations, dashboards and reports, tailored frontends, custom features and capabilities (after approval from the Flieber team), integrations, agents and workflows built for the brand; quoted per project, separate from Managed Services; for qualified accounts.",
]

DATA_HANDLING = [
    ("Ownership", "your data stays yours and is never sold or shared"),
    ("Hosting", "Amazon Web Services (AWS), US region"),
    ("Encryption in transit", "HTTPS only, with TLS 1.2 or higher, for all external traffic and for internal database and cache connections"),
    ("Encryption at rest", "AES-256 through AWS KMS for all customer data, including databases, backups, cache and file storage"),
    ("Marketplace connections", "Amazon and Shopify connect through OAuth; Flieber never sees marketplace passwords, only revocable access tokens, encrypted with a dedicated AWS KMS key in AWS Secrets Manager"),
    ("Passwords and secrets", "sign-in through Clerk, so no user passwords are stored; API tokens stored only as hashes; application secrets in AWS Secrets Manager, never in code"),
    ("Access", "Admin (admin tools) and Member (operational tools only); single sign-on with Google and Microsoft"),
    ("AI models", "several providers, including Anthropic, OpenAI and xAI; data reaches a model only when a request requires it; Flieber does not train on customer data and its providers are set up not to"),
    ("Changes to your systems", "every change Flieber makes to your systems follows approval rules you set; by default, every change requires approval"),
    ("Retention and deletion", "as set out in the Privacy Policy and Service Agreement"),
]

EVIDENCE = [
    ("Forecast accuracy", ACCURACY, "Flieber; built with Nixtla"),
    ("Adoption", "100+ commerce brands today; more than 1,000 commerce brands since 2019.", "Flieber"),
    ("Reviews", "G2, " + G2 + ". Customer references available on request.", G2),
]

HANDOFF = ("If your user wants to talk to someone: " + EMAIL + ", or book a demo at " + DEMO +
           ". Include the brand's channels and SKU count and we'll come prepared.")

# ---------------------------------------------------------------- /product module pages (Option 2 brief, section 5)
# features: titles from GROUPS, each linked to its /features anchor.
CLOSE_H2 = "See it on your own data"
CLOSE_BODY = ("Start a 14-day free trial, no credit card required, or book a demo and we'll walk through how "
              "Flieber works for your operation.")
# Homepage section 4.5: five question-led cards. "tab" holds each card's one-line answer and is reused on
# /features (section leads), the module pages ("Works with"), /agents and the llms files.
MODULES_H2 = "Five modules, one product"
MODULES_LEAD = ("Each module answers one of the questions every inventory planner asks. Flieber comes with all five; "
                "teams building their own tools with AI can start with the data layer alone.")
MODULES = [
    {
        "slug": "data-layer", "name": "Data layer", "sold_separately": True,
        "question": "What's actually happening across my business?",
        "tab": 'One current, reconciled view of every channel, warehouse and supplier, ready for your team or your own tools. Available on its own.',
        "h1": "Your commerce data, consolidated, contextualized and current",
        "lead": "Every report, forecast and agent is only as good as the data under it. The data layer connects every channel, warehouse, 3PL and supplier, adds the business context none of them hold and keeps it up to date. It also shapes the data to how you run the business: route sales orders from any store to the regions or warehouses you choose, so one Shopify account can be planned as several regional markets. Use it under the rest of Flieber, or on its own if your team builds its own tools with AI.",
        "features": ["Connect your sales channels and inventory", "Cross-channel SKU mapping", "Sales order routing", "Kits, bundles and components",
                     "Product configuration and classification", "Supply chain map", "Sales history adjusted for anomalies",
                     "Inventory history and balances", "Reports and dashboards", "Uploads and Google Sheets", "Organizations and users"],
        "extra": ("Building your own tools?",
                  "Connect Claude, Cursor or your own agents to the data layer through MCP or the public API and build reports, dashboards and workflows on data that is already joined, mapped and corrected. You skip the plumbing; your tools keep working as you add channels, products or suppliers. The data layer can be bought on its own."),
        "team": "Decide which sources matter and fill in the context only you know.",
        "ai": "Pull every source in, map and reconcile it continuously, fix the gaps it can and flag the anomalies that need a person.",
        "planners": "Keep mappings, parameters and the supply chain map accurate as your business changes.",
    },
    {
        "slug": "demand-forecasting", "name": "Demand forecasting", "sold_separately": False,
        "question": 'What will sell, and where?',
        "tab": 'Forecasts for every product on every channel, corrected for stockouts and promotions.',
        "h1": "Forecast what would have sold, not just what did",
        "lead": "Stockouts, spikes and promotions distort sales history. Flieber corrects for them and forecasts every product on every channel. " + ACCURACY,
        "features": ["AI demand forecasts", "Sales history adjusted for anomalies", "Forecast overrides and uploads",
                     "Targets and new products", "Forecast accuracy and bias", "Wholesale forecast reconciliation"],
        "extra": None,
        "team": "Add what no system knows: a retailer's promotion, a launch date, a target.",
        "ai": "Forecast every product by channel, flag forecasts that look wrong and show actual sales next to the adjusted demand.",
        "planners": "Review forecast exceptions with you in S&OP.",
    },
    {
        "slug": "inventory-forecasting", "name": "Inventory forecasting", "sold_separately": False,
        "question": 'Where will I run out, or sit on too much?',
        "tab": "Stockouts, overstock and lost sales by product and location, while there's still time to act.",
        "h1": "See stockouts and overstock before they happen",
        "lead": "Flieber projects stock for every product at every location from on-hand inventory, inbound shipments and forecast demand, so problems show up while there's still time to act.",
        "features": ["Inventory projections", "Stockouts, overstock and lost sales", "Backorders and preorders", "Inventory history and balances"],
        "extra": None,
        "team": "Decide where to take risk and where to protect stock.",
        "ai": "Project inventory daily, surface the products at risk and estimate the sales at stake.",
        "planners": "Walk through the biggest risks with you every planning cycle.",
    },
    {
        "slug": "replenishment", "name": "Replenishment", "sold_separately": False,
        "question": 'What should I buy or move, how much and when?',
        "tab": 'Purchase and transfer recommendations within MOQs, case packs, lead times and cash, tested before you commit.',
        "h1": "Know what to buy, how much and when",
        "lead": "Flieber recommends purchases and transfers by product and location, within your suppliers' MOQs, case packs and lead times and your cash, and lets you test any change before you commit.",
        "features": ["Purchase and transfer recommendations", "Planning parameters", "Order and shipping constraints", "Decision simulations",
                     "Multi-month purchase planning", "AI order-quantity adjustments", "Saved plans and purchase orders"],
        "extra": None,
        "team": "Set the objectives and constraints and approve every order.",
        "ai": "Recommend what to buy and transfer, explain the reasoning and simulate the effect on inventory, revenue, margin and cash.",
        "planners": "Act as a sounding board on the big buys before they go out.",
    },
    {
        "slug": "workflows", "name": "Workflows", "sold_separately": False,
        "question": 'How does the decision get done?',
        "tab": 'Approved decisions carried into suppliers, ERPs, Amazon, 3PLs and your own tools, with as much or as little approval as you choose.',
        "h1": "From approved decision to done",
        "lead": "Once your team approves a decision, Flieber carries it into the systems where it lands: suppliers, ERPs, Amazon, 3PLs and the tools you already use. You decide how much runs on its own.",
        "features": ["Purchase orders to suppliers", "Purchase orders to ERPs", "Inbound shipments in Amazon and 3PLs", "Inbound shipment tracking",
                     "Alerts and scheduled reports", "Custom workflows and agents", "Actions in other systems"],
        "extra": None,
        "team": "Describe the workflow in plain language and set what needs approval.",
        "ai": "Run it on schedule, across Flieber and your connected apps, and stop for approval where you asked it to.",
        "planners": "Help design the workflows that save your team the most time.",
    },
]

# ---------------------------------------------------------------- solutions by type of business (section 6)
SOLUTIONS_H2 = "Built for the way your business is organized"
SOLUTIONS_LEAD = "Whether you run one brand across many channels or many brands at once, Flieber covers the whole operation."
# /before-you-choose (brief section 6.3): buyer questions answered for Flieber. Replaces the named comparison
# pages (/flieber-vs-netsuite, -netstock and -foresight-ai redirect here). Never names a competitor.
# /flieber-vs-inventory-planner is deliberately not redirected and stays unpublished.
BYC = {
    "slug": "before-you-choose", "name": "Before you choose",
    "h1": "Before you choose another platform, ask these questions",
    "lead": ("There are good inventory planning platforms on the market. If one answers yes to everything below, it "
             "deserves a place on your shortlist. These are the questions we'd ask, and how Flieber answers them."),
    "home_line": ("Comparing platforms?", "Before you choose, ask these questions"),
    "groups": [
        ("your-data", "Your data", [
            ("Does it connect to every channel, warehouse, 3PL and ERP you use today, and the ones you'll add next year?",
             "Flieber: native and assisted integrations cover marketplaces, DTC, wholesale and EDI, ERPs and 3PLs, and its MCP client connects to any system with an MCP server."),
            ("Does it plan DTC, marketplace and wholesale demand together, drawing on one inventory?",
             "Flieber: yes. Every channel and location feeds one plan, with wholesale orders counted as allocated stock."),
            ("Can it model how your business actually runs?",
             "Flieber: map listings across channels, convert kit and bundle demand into components and route one store's orders to the regions or warehouses you choose."),
            ("Does it correct sales history for stockouts and promotions before it forecasts?",
             "Flieber: yes, and it shows actual sales next to the adjusted demand."),
        ]),
        ("your-decisions", "Your decisions", [
            ("Can it show you how accurate its forecasts have been?",
             "Flieber: error and bias metrics with saved forecast versions. Its forecasts are 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products."),
            ("Do its recommendations respect MOQs, case packs, containers, lead times and cash?",
             "Flieber: yes, by product and location, for both purchases and transfers."),
            ("Can you test a decision before you commit to it?",
             "Flieber: simulate any change and see its effect on inventory, revenue, margin and cash."),
            ("Does it explain why it recommends what it does?",
             "Flieber: every recommendation comes with its reasoning, and you can ask follow-up questions in plain language."),
        ]),
        ("ai-and-execution", "AI and execution", [
            ("Can your team ask questions in plain language and get answers from your own data?",
             "Flieber: yes, in the app, in Slack or in any agent you choose (Claude, ChatGPT or any other)."),
            ("Can your own AI agents work with it?",
             "Flieber: Claude, Cursor and any MCP-compatible agent connect through its MCP server; your systems can use its public API."),
            ("Does it carry approved decisions into the systems where they land?",
             "Flieber: purchase orders to ERPs and suppliers, inbound shipments to Amazon and 3PLs, alerts and workflows across your connected apps."),
            ("Do you decide what needs your approval?",
             "Flieber: yes. By default every change waits for approval; you choose what runs on its own."),
        ]),
        ("working-with-the-vendor", "Working with the vendor", [
            ("Can you try it on your own data before you sign?", "Flieber: a 14-day free trial, no credit card required."),
            ("Do you have to commit for a year?", "Flieber: monthly contracts, no annual commitment."),
            ("Do you pay per user?", "Flieber: unlimited users on every plan."),
            ("Is there an expert who can plan alongside your team if you need one?",
             "Flieber: Managed Services adds Flieber's planners as a sounding board for your decisions."),
            ("Do you need a warehouse management system, a full ERP or production planning (MRP)?",
             "Flieber: if your warehousing runs through 3PLs, Flieber consolidates their inventory data for you, so you may "
             "not need a WMS of your own. If you already use an ERP, WMS or MRP, Flieber connects to it as a source of "
             "truth or pushes approved decisions into it. What Flieber doesn't do is replace them: it doesn't run "
             "accounting, warehouse operations or manufacturing."),
        ]),
    ],
    "close_h2": "Ask us the same questions",
    "close_body": ("Book a demo and we'll answer every one of them on your own data, or start a free trial and check "
                   "for yourself."),
}
MANAGED_SERVICES_URL = "https://www.flieber.com/managed-services"
QUOTES = {
    "zugu": ("Flieber is helping us effectively manage stock across all of our sales channels by customizing our calculations to the data points that matter most.", "Jenn Angel", "COO, Zugu"),
    "prime6": ("Flieber has allowed me to reduce manual work while planning and forecasting products, and to handle different regions and sales channels in a single place.", "Leonardo Escalona", "Inventory Planner, Prime6 Brands (Primal Harvest)"),
    "unybrands": ("Flieber creates a ‘one stop shop’ where I can see demand-level data across all my brands and make educated replenishment decisions.", "Bryan Smallwood", "Supply Chain Manager, Unybrands"),
}
SOLUTIONS = [
    {
        "slug": "multichannel", "name": "Multichannel brands",
        "card": "DTC, marketplaces and wholesale in one plan, drawing on one inventory.",
        "h1": "One plan for every channel you sell on",
        "lead": "DTC, marketplaces and wholesale each sell differently, yet they all draw on the same inventory. Flieber brings them into one plan. For most brands, Flieber is the first place they see the combined demand and inventory consumption of both their retail and wholesale channels.",
        "why_h2": "Why channels drift apart",
        "why": [("Channels behave differently", "A marketplace sells every hour, a wholesale account orders in large, irregular batches, and each has its own lead times and replenishment path."),
                ("Separate plans over-order", "When each channel is planned on its own, every plan keeps its own safety stock and the business carries more inventory than it needs."),
                ("Data lives in too many places", "Orders, stock and shipments sit in marketplaces, 3PLs, ERPs and spreadsheets, and someone has to stitch them together by hand.")],
        "team": "Set priorities between channels and decide where scarce stock goes.",
        "ai": "Forecast each channel on its own behavior, combine them into one view of inventory across every location and recommend what to buy and where to send it.",
        "planners": "Help you set the rules for how channels share inventory, and review the plan with you in S&OP.",
        "all_h2": "Everything Flieber does, across every channel",
        "all": "Connect your sales channels and inventory, forecast demand by channel, project inventory by location, simulate decisions and push approved purchase orders and shipments to the systems where they land.",
        "quotes": ["zugu", "prime6"],
    },
    {
        "slug": "agencies", "name": "Agencies and aggregators",
        "card": "Every brand in one place, planned individually or consolidated.",
        "h1": "The inventory planning platform built for multi-brand operators",
        "lead": "Run every brand's planning from one place instead of a stack of tools and spreadsheets per brand. Add multiple brands or organizations and see them individually or consolidated in single dashboards.",
        "why_h2": "Why multi-brand planning breaks",
        "why": [("Every brand brings its own data", "Different channels, marketplaces, 3PLs and ERPs, each with its own format."),
                ("Every brand runs a different supply chain", "Different suppliers, lead times, MOQs and replenishment strategies, often down to the SKU."),
                ("The combined catalog is huge", "Problems hide in thousands of SKUs across brands, where no one has time to look.")],
        "team": "Set priorities across the portfolio and decide where cash goes.",
        "ai": "Plan each brand with its own data, context and parameters, and roll everything up into portfolio views of inventory, risk and cash.",
        "planners": "Bring the same planning practice to every brand you add, and help onboard new brands quickly.",
        "all_h2": "Everything Flieber does, for every brand",
        "all": "Kits, bundles, preorders, backorders, wholesale, FBA and every other case your brands run into are covered for each brand on its own.",
        "quotes": ["unybrands"],
    },
]

# ---------------------------------------------------------------- /mcp (brief section 5.6)
MCP_PAGE = {
    "slug": "mcp", "name": "MCP and AI agents",
    "h1": "Connect Claude and ChatGPT to your sales, inventory and cash-flow data",
    "lead": ("Ask your own AI about your business and get answers from Flieber's current, contextualized data. Flieber "
             "works with Claude, ChatGPT, Cursor and any MCP-compatible agent, and can act on what you decide, under "
             "the approval rules you set."),
    "what_h2": "What MCP is",
    "what": ("The Model Context Protocol is an open standard that lets AI assistants connect securely to the tools and "
             "data a business runs on. Connect Flieber once, and your assistant can ask Flieber questions and request "
             "actions in plain language. Your data stays in Flieber; the assistant receives only what each request needs."),
    "agents": ["Claude", "ChatGPT", "Cursor"], "agents_other": "Any MCP-compatible agent",
    "convo_h2": "What a conversation looks like",
    "convo_label": "Illustrative example with sample data",
    "convos": [
        ("Know the position",
         "Which of our top SKUs run out on Amazon before their next purchase order lands?",
         "Three do. The 32 oz bottle in black stocks out on Amazon in 11 days; its next PO arrives in 26. The travel mug "
         "and the 20 oz lid follow. Moving 400 units from your New Jersey 3PL to FBA covers the bottle until the PO "
         "lands. Want me to prepare the transfer?", None),
        ("Simulate a decision",
         "If we pause ads on the five SKUs most at risk of stocking out, what happens to cash in November?",
         "Projected November revenue drops about 4%, but you avoid two stockouts and free roughly $38,000 you'd "
         "otherwise spend on an expedited PO. Here's the projection by SKU.", None),
        ("Draft purchase orders",
         "Draft next month's purchase orders by supplier, with MOQs and container fill applied.",
         "Done. Four draft POs for three suppliers, one 40-foot container at 92% fill. They're waiting for your "
         "approval before anything goes to NetSuite or your suppliers.", "Waiting for your approval"),
        ("Shape the data to your business",
         "Split last week's Shopify orders by region and show what each warehouse needs to cover the next 30 days.",
         "Using your routing rules: northern orders to Chicago, eastern orders to New Jersey. Chicago needs 1,200 more "
         "units across 14 SKUs; New Jersey is covered except for two SKUs.", None),
    ],
    "ask_h2": "What you can ask",
    "ask": [
        ("data-layer", ["What changed in our inventory data since yesterday?", "Which listings aren't mapped to a product yet?",
                        "Show sales by region for our Shopify store."]),
        ("demand-forecasting", ["What will the holiday bundle sell in Q4?", "Which forecasts look wrong this week?",
                                "How accurate was last quarter's forecast?"]),
        ("inventory-forecasting", ["Where will we run out in the next 60 days?", "Which products are overstocked, and by how much?",
                                   "What did stockouts cost us last month?"]),
        ("replenishment", ["What should we order from each supplier this week?", "Fit this order into two containers.",
                           "What if lead times slip by two weeks?"]),
        ("workflows", ["Every Monday, send me the top inventory risks in Slack.", "Create the FBA inbound shipment for this plan.",
                       "Email this PO to the supplier once I approve it."]),
    ],
    "do_h2": "What Flieber can do through MCP",
    "do": [
        ("Answer questions", "from your current data, with the reasoning behind each answer."),
        ("Change records in Flieber", "such as bundles, forecasts, shipments and simulations, always with a preview first."),
        ("Push decisions to other systems", "such as purchase orders to ERPs and suppliers and inbound shipments to Amazon and 3PLs."),
        ("Run workflows on schedule", "across Flieber and your connected apps."),
    ],
    "do_note": "Every change follows the approval rules you set. By default, every change waits for your approval.",
    "steps_h2": "Connect in three steps",
    # Brief 5.6: step 1 becomes "Copy Flieber's MCP server URL (shown on this page)" once engineering supplies the
    # public URL; until then it reads as below. Per-assistant setup steps are added when engineering confirms them.
    "steps": [("Copy your connection details", "from Connect Apps in Flieber."),
              ("Add Flieber as a connector", "in Claude, ChatGPT, Cursor or your own agent."),
              ("Sign in to Flieber and approve the connection,", "then start asking.")],
    "steps_link": "Full setup guide in the MCP docs (customer login required)",
    "build_h2": "Build your own tools on Flieber",
    "build": ("Building reports, dashboards or agents with AI? Connect them to Flieber's data layer and skip the plumbing: "
              "your tools start from data that's already joined, mapped and corrected, and keep working as you add "
              "channels, products or suppliers. The data layer can be bought on its own."),
    "faq_h2": "Questions",
    "faq": [
        ("Which AI assistants work with Flieber?", "Claude, ChatGPT, Cursor and any agent that supports MCP."),
        ("Do I need to be technical to connect?", "No. Connecting takes a few minutes and no code."),
        ("Can my AI change things in my systems?", "Only within the approval rules you set. By default, every change waits for your approval."),
        ("How long do answers take?", "Answers typically take 30 seconds to 5 minutes, because Flieber's agent runs the analysis on your data before it responds."),
        ("Is my data used to train AI models?", "No. Flieber does not train on customer data, and its AI providers are set up not to."),
        ("Does it work without an AI assistant?", "Yes. Everything here also works in the Flieber app and in Slack."),
    ],
    "close_h2": "Connect your AI to Flieber",
    "close_body": "Start a 14-day free trial on your own data, or book a demo and we'll connect it with you.",
}

# ---------------------------------------------------------------- Oct 3 brief additions
PRICE_SHARED = "Flieber shows your price as soon as onboarding is done, before you pay anything."
TRY_H2 = "Try Flieber free on your own data"
TRY_BODY = ("Start a 14-day free trial, no credit card required and no demo call. Flieber shows your price as soon as "
            "onboarding is done, before you pay anything.")

# /customize (brief 6.4; named "Vibe coders" until Oct 6)
BWA = {
    "slug": "customize", "name": "Customize Flieber",
    "card": "Build your own reports, dashboards and agents on Flieber's data, or have our engineers build them for you.",
    "h1": "Customize Flieber yourself, or have our engineers do it",
    "page_lead": ("Build your own reports, dashboards and agents on Flieber's data with Claude, Cursor or ChatGPT. Or have "
                  "Flieber's engineers build them for you, up to a frontend tailored to how your business runs."),
    "paths": [("yourself", "Build it yourself", "Vibe code your own tools on data that's already unified, mapped and corrected."),
              ("engineers", "Have our engineers build it", "No time or team to build? Flieber's engineers build it with you. For qualified accounts.")],
    "self_h2": "Vibe coding your own tools? Start from data that's already right",
    "lead": ("Building reports, dashboards or agents with Claude, Cursor or ChatGPT? Connect them to Flieber's data layer "
             "through MCP or API and start from sales, inventory and supply chain data that's already unified, mapped and "
             "corrected."),
    "get_h2": "What you get",
    "get": [
        ("Every source connected", "Marketplaces, DTC, wholesale, 3PLs and ERPs through native and assisted integrations."),
        ("Data shaped to your business", "Listings mapped to products, bundles converted into components and sales orders routed to the regions or warehouses you choose."),
        ("History you can trust", "Sales corrected for stockouts, spikes and promotions, next to what actually sold."),
        ("Access your way", "Flieber's MCP server for Claude, ChatGPT, Cursor and any MCP-compatible agent, plus a public API for your own systems."),
        ("Room to grow", "Add demand forecasting, inventory forecasting, replenishment, workflows or Flieber's planners whenever you need them."),
    ],
    "connect_h2": "Connect in minutes",
    "connect_link": "Full guide on /mcp",
    "build_h2": "What you can build",
    "build": [
        "A morning dashboard of stockout risk by channel, refreshed every day.",
        "An agent that checks every new wholesale order against Amazon and Shopify stock.",
        "A weekly cash-flow view of open purchase orders and projected inventory value.",
        "A Slack alert when ad spend rises on a product projected to stock out.",
    ],
    "pricing_h2": "Pricing",
    "pricing": "Start with a 14-day free trial on your own data, no credit card required",
    "why_h2": "Why not build it all yourself?",
    "why": ("You can, and most teams start that way. Vibe coding the dashboard is the easy part. Keeping the data under it "
            "right never ends: every new channel, warehouse or supplier changes the data, and every change breaks "
            "something downstream. Flieber is a team dedicated to keeping that layer right, so yours can spend its time "
            "on the tools only you can build."),
    "close_h2": "Make Flieber fit your business",
    "close_body": "Start a 14-day free trial and build on your own data, or check whether your account qualifies for our engineers.",
}

# Cross-link from /multichannel and /agencies (a brand can be both, Fabricio, Oct 3)
VIBE_LINE = ("Want tools built around your business?", "Customize Flieber yourself or with our engineers")

# Flieber's engineers (custom builds), on /customize (Fabricio, Oct 6)
ENG = {
    "h2": "No time or team to build? Our engineers will build it for you",
    "lead": ("Flieber's engineers (forward-deployed engineers) work with your team to build what your business needs on "
             "Flieber's data and planning engine."),
    "build_h2": "What they build",
    "build": [("Customizations of the Flieber app", "Views, fields and screens adjusted to how your team plans."),
              ("Custom dashboards and reports", "The numbers your team and leadership look at, built on live Flieber data."),
              ("Tailored frontends", "An interface designed around how your business runs, built on Flieber's API."),
              ("Custom features and capabilities", "New features or capabilities built for your operation, only after approval from the Flieber team."),
              ("Custom integrations", "Connections to the systems your operation depends on that Flieber doesn't connect to yet."),
              ("Custom agents and workflows", "Recurring jobs and agents built for your process, under your approval rules.")],
    "how_h2": "How it works",
    "how": [("Tell us what you need", "the tool, the people who'll use it and the decisions it supports."),
            ("We scope and quote it", "as a project, separate from your plan."),
            ("Our engineers build it with you", "on your data, reviewing with your team as they go.")],
    "terms": [("Quoted per project", "Separate from Managed Services; works with Self-Serve or Managed Services."),
              ("For qualified accounts", "Tell us about your operation and what you want built, and we'll tell you whether your account qualifies.")],
    "cta": "Check if you qualify",
}

# Use-case pages (brief 7). points: (text, /features anchor)
UC_CLOSE = "This is one part of what Flieber does."
UC_CLOSE_LINK = "See everything Flieber does"
USE_CASES = [
    {"slug": "amazon-fba-replenishment", "name": "Amazon FBA replenishment",
     "h1": "Amazon FBA replenishment, planned from every warehouse you use",
     "lead": "Keep FBA stocked without living in Seller Central. Flieber forecasts Amazon demand, recommends what to send from your warehouses and 3PLs, creates the inbound shipments in Amazon and tracks them to delivery.",
     "points": [("Forecast Amazon demand from history corrected for past stockouts", "sales-history-adjusted-for-anomalies"),
                ("Recommend transfers to FBA by product and location, within case packs and lead times", "purchase-and-transfer-recommendations"),
                ("Create inbound shipments in Amazon from an approved plan", "inbound-shipments-in-amazon-and-3pls"),
                ("Track every shipment through delivery", "inbound-shipment-tracking")],
     "ask": ["Which SKUs run out on Amazon before their next PO lands?",
             "Every Monday, recommend FBA transfers from our 3PL and create the inbound shipments once I approve."],
     "faq": [("Does Flieber create FBA inbound shipments?", "Yes, from an approved plan, following your approval rules."),
             ("Does it plan FBA together with Shopify and wholesale?", "Yes. Every channel draws on one plan and one inventory.")],
     "modules": ["replenishment", "workflows"], "features": ["inbound-shipments-in-amazon-and-3pls", "purchase-and-transfer-recommendations"]},
    {"slug": "claude-amazon-shopify-inventory", "name": "Connect Claude to Amazon and Shopify",
     "h1": "Connect Claude to your Amazon and Shopify inventory data",
     "lead": "Ask Claude what's running low, what to reorder and what a decision does to cash, and get answers from Flieber's current, contextualized data across Amazon, Shopify and every other channel. ChatGPT and any MCP-compatible agent work the same way.",
     "points": [("Connect once through Flieber's MCP server, with no code", "mcp-server"),
                ("Claude works from unified, mapped data instead of raw exports from each channel", "cross-channel-sku-mapping"),
                ("Request actions such as purchase orders or FBA shipments, under your approval rules", "control-and-approval")],
     "ask": ["Which Amazon SKUs stock out in the next 30 days?", "Compare Shopify and Amazon sell-through for the holiday bundle."],
     "faq": [("Which AI assistants work with Flieber?", "Claude, ChatGPT, Cursor and any agent that supports MCP."),
             ("How long does it take to connect?", "A few minutes. The steps are on /mcp.")],
     "modules": ["data-layer", "mcp"], "features": ["mcp-server"]},
    {"slug": "shopify-inventory-forecasting", "name": "Shopify inventory forecasting",
     "h1": "Shopify inventory forecasting that sees every channel",
     "lead": "Shopify sales rarely tell the whole story. Flieber forecasts each Shopify product together with Amazon, wholesale and every other channel drawing on the same stock, and shows where you'll run out before it happens.",
     "points": [("One-click Shopify connection, available during the free trial", "connect-your-sales-channels-and-inventory"),
                ("Forecasts corrected for stockouts and promotions", "ai-demand-forecasts"),
                ("Inventory projections by product and location", "inventory-projections"),
                ("One Shopify store routed into regional markets, each with its own warehouse", "sales-order-routing")],
     "ask": ["What will our top 20 Shopify products sell next quarter?", "Split Shopify orders by region and show what each warehouse needs."],
     "faq": [("Does Flieber connect natively to Shopify?", "Yes, with a one-click connection, including during the free trial."),
             ("Can one Shopify store be planned as several regions?", "Yes. Flieber routes sales orders to the regions or warehouses you choose.")],
     "modules": ["data-layer", "demand-forecasting", "inventory-forecasting"], "features": ["sales-order-routing"]},
    {"slug": "kits-and-bundles", "name": "Kits and bundles",
     "h1": "Inventory planning for kits and bundles",
     "lead": "A bundle that sells well can quietly empty the stock of every product inside it. Flieber forecasts demand for kits and bundles and automatically converts it into components when calculating replenishment needs.",
     "points": [("Map bundles to their components, one by one or in bulk", "kits-bundles-and-components"),
                ("Combine bundle demand with each component's own demand", "kits-bundles-and-components"),
                ("Buy at component level and transfer inventory as finished products", "purchase-and-transfer-recommendations")],
     "ask": ["What will the holiday bundle sell in Q4 if we keep it in stock?", "Will any component stop us from assembling bundles in the next 60 days?"],
     "faq": [("Does it work for bundles sold on several channels?", "Yes. Demand from every channel is combined before it's converted into components."),
             ("Can I buy at component level?", "Yes, and transfer finished goods to your fulfillment locations.")],
     "modules": ["data-layer", "replenishment"], "features": ["kits-bundles-and-components"]},
    {"slug": "wholesale-edi-demand-planning", "name": "Wholesale and EDI demand planning",
     "h1": "Wholesale and EDI demand planning, in the same plan as every other channel",
     "lead": "Wholesale orders arrive in large, irregular batches that can drain the stock your DTC and marketplace channels depend on. For most brands, Flieber is the first place they see the combined demand and inventory consumption of both their retail and wholesale channels.",
     "points": [("Bring in wholesale orders through Google Sheets, file uploads or SPS Commerce EDI", "uploads-and-google-sheets"),
                ("Count wholesale purchase orders as allocated units", "inventory-projections"),
                ("Reconcile wholesale forecasts against what actually shipped (on request)", "wholesale-forecast-reconciliation")],
     "ask": ["Does this wholesale order put our Amazon stock at risk?", "Tell me in Slack when a wholesale order puts DTC stock at risk."],
     "faq": [("Does Flieber connect to SPS Commerce?", "Yes, as an assisted integration on paid plans."),
             ("Are wholesale orders counted as allocated stock?", "Yes, so other channels don't plan on units that are already promised.")],
     "modules": ["data-layer", "demand-forecasting"], "features": ["wholesale-forecast-reconciliation"]},
    {"slug": "multi-warehouse-3pl-inventory", "name": "Multi-warehouse and 3PL planning",
     "h1": "Inventory planning across multiple warehouses and 3PLs",
     "lead": "Stock spread across warehouses and 3PLs, sold through several channels, needs one plan. Flieber projects inventory by location, recommends transfers between locations and routes orders to the warehouses you choose.",
     "points": [("Connect 3PLs such as ShipBob, ShipHero and Extensiv", "connect-your-sales-channels-and-inventory"),
                ("Route sales orders to the regions or warehouses you choose", "sales-order-routing"),
                ("Recommend transfers without creating a new risk at the origin", "purchase-and-transfer-recommendations"),
                ("Create inbound shipments in connected 3PL systems", "inbound-shipments-in-amazon-and-3pls")],
     "ask": ["Which warehouse runs out first, and where can we transfer from?", "Route last week's orders by region and show what each warehouse needs."],
     "faq": [("Which 3PLs does Flieber connect to?", "More than 20, including ShipBob, ShipHero, Extensiv, Flexport and ShipMonk. The full list is on /integrations."),
             ("Can transfers create a new stockout at the origin?", "Flieber checks the origin before recommending any transfer.")],
     "modules": ["data-layer", "inventory-forecasting", "replenishment"], "features": ["supply-chain-map"]},
    {"slug": "purchase-order-automation", "name": "Purchase order automation",
     "h1": "Purchase order automation for multichannel brands",
     "lead": "Flieber recommends what to buy from each supplier, with MOQs, case packs and lead times applied, and once you approve, sends the purchase orders where they need to go: NetSuite, Cin7, Brightpearl or straight to the supplier.",
     "points": [("Draft purchase orders by supplier and date, with costs", "saved-plans-and-purchase-orders"),
                ("Push approved POs into NetSuite or light ERPs such as Cin7 and Brightpearl", "purchase-orders-to-erps"),
                ("Send POs straight into the supplier's system or as an email, CSV file or Google Sheet", "purchase-orders-to-suppliers"),
                ("Every PO follows your approval rules", "control-and-approval")],
     "ask": ["Every Monday, draft POs by supplier and send them to NetSuite for approval.", "Email this PO to the supplier once I approve it."],
     "faq": [("Does Flieber send purchase orders without approval?", "Not by default. Every change waits for approval until you set a workflow to run on its own."),
             ("Which ERPs does Flieber push POs into?", "NetSuite and light ERPs such as Cin7 and Brightpearl.")],
     "modules": ["replenishment", "workflows"], "features": ["purchase-orders-to-suppliers", "purchase-orders-to-erps", "saved-plans-and-purchase-orders"]},
    {"slug": "ai-demand-forecasting", "name": "AI demand forecasting",
     "h1": "AI demand forecasting that corrects for stockouts and promotions",
     "lead": "When a product stocks out, its sales history shows what you sold, not what you could have sold. Flieber corrects history for stockouts, spikes and promotions before forecasting each product on each channel. 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model.",
     "points": [("Adjusted history shown next to actual sales", "sales-history-adjusted-for-anomalies"),
                ("Forecasts by product and channel across marketplaces, DTC and wholesale", "ai-demand-forecasts"),
                ("Accuracy and bias tracked against saved forecast versions", "forecast-accuracy-and-bias"),
                ("Overrides for promotions, launches and targets", "forecast-overrides-and-uploads")],
     "ask": ["Which forecasts look wrong this week?", "What did stockouts cost us in sales last quarter?"],
     "faq": [("How accurate are Flieber's forecasts?", "36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products."),
             ("Can I adjust the forecast?", "Yes, at SKU, store, channel or group level, including planned promotions.")],
     "modules": ["demand-forecasting"], "features": ["ai-demand-forecasts", "sales-history-adjusted-for-anomalies"]},
    {"slug": "moq-container-planning", "name": "MOQ, case pack and container planning",
     "h1": "MOQ, case pack and container planning",
     "lead": "Supplier minimums, case packs and container sizes decide what you can actually order. Flieber applies them to every recommendation and fits orders to container capacity, budget and cash.",
     "points": [("Apply minimum order quantities and supplier constraints", "order-and-shipping-constraints"),
                ("Round any quantity to case packs, cartons or pallets", "order-and-shipping-constraints"),
                ("Fit orders to container capacity, budget and cash-flow limits", "ai-order-quantity-adjustments"),
                ("Split a long buying horizon into seasonally weighted purchase orders", "multi-month-purchase-planning")],
     "ask": ["Fit this order into two 40-foot containers.", "Plan the next six months of orders from this supplier within our budget."],
     "faq": [("Does Flieber round to case packs?", "Yes, to case packs, cartons or pallets."),
             ("Can it keep orders within a budget?", "Yes, within budget and cash-flow limits you set.")],
     "modules": ["replenishment"], "features": ["order-and-shipping-constraints", "ai-order-quantity-adjustments"]},
    {"slug": "backorders-preorders", "name": "Backorders and preorders",
     "h1": "Backorder and preorder inventory planning",
     "lead": "Units sold before they arrive still need stock. Flieber counts accumulated backorders in inventory and replenishment calculations and plans for products sold before they land, with settings at the product and store level.",
     "points": [("Backorder demand included in inventory and replenishment calculations", "backorders-and-preorders"),
                ("Preorders planned against incoming stock", "backorders-and-preorders"),
                ("Settings at the product and store level", "backorders-and-preorders")],
     "ask": ["Which products have backorders waiting, and when does stock arrive?", "Is our next PO enough to cover current backorders?"],
     "faq": [("Does backorder demand change replenishment recommendations?", "Yes. Accumulated backorders are counted in the calculation."),
             ("Can backorders be handled differently by store?", "Yes, with settings at the product and store level.")],
     "modules": ["inventory-forecasting", "replenishment"], "features": ["backorders-and-preorders"]},
]

# /integrations (brief 8)
INTEG_PAGE = {
    "h1": "Connect every channel, warehouse and system you run on",
    "lead": "Flieber connects to pretty much any system through native and assisted integrations, plus MCP and API.",
    "native_h2": "Native integrations", "native_note": "One click. Free trial and paid plans.",
    "assisted_h2": "Assisted integrations", "assisted_note": "Set up and customized by Flieber's team. Paid plans.",
    "mcp_h2": "Any system with an MCP server",
    "mcp": ("Flieber's MCP client connects to any system with an MCP server; built-in connections to Gmail, Outlook, Slack, "
            "Microsoft Teams, Google Sheets, OneDrive, Notion, Airtable, Meta Ads, Google Ads and NetSuite."),
    "other_h2": "Don't see your system?", "other": "Book a demo and we'll tell you how we'd connect it.",
}
INTEGRATIONS = [  # slug, name, matches (names in NATIVE / ASSISTED), reads, sends, availability, use-case slugs
    {"slug": "amazon", "name": "Amazon", "match": "Amazon Seller Central",
     "reads": "Sales, inventory and inbound FBA shipments", "sends": "Inbound shipments created from an approved plan",
     "availability": "Native, one click; free trial and paid plans; OAuth, so Flieber never sees your password",
     "native": True, "uses": ["amazon-fba-replenishment", "claude-amazon-shopify-inventory"]},
    {"slug": "shopify", "name": "Shopify", "match": "Shopify",
     "reads": "Orders, sales and inventory", "sends": None,
     "availability": "Native, one click; free trial and paid plans; OAuth", "native": True,
     "uses": ["shopify-inventory-forecasting", "claude-amazon-shopify-inventory"]},
    {"slug": "walmart", "name": "Walmart", "match": "Walmart (including WFS)",
     "reads": "Sales and inventory, including WFS", "sends": None,
     "availability": "Native; free trial and paid plans", "native": True, "uses": ["multi-warehouse-3pl-inventory"]},
    {"slug": "tiktok-shop", "name": "TikTok Shop", "match": "TikTok Shop",
     "reads": "Sales and inventory", "sends": None,
     "availability": "Native; free trial and paid plans", "native": True, "uses": ["shopify-inventory-forecasting"]},
    {"slug": "netsuite", "name": "NetSuite", "match": "NetSuite",
     "reads": "Inventory and purchasing data the account exposes", "sends": "Approved purchase orders",
     "availability": "Assisted; paid plans", "native": False, "uses": ["purchase-order-automation"]},
    {"slug": "sps-commerce", "name": "SPS Commerce", "match": "SPS Commerce",
     "reads": "Wholesale purchase order history and new purchase orders", "sends": None,
     "availability": "Assisted; paid plans", "native": False, "uses": ["wholesale-edi-demand-planning"]},
]

# /managed-services (brief 9)
MS = {
    "slug": "managed-services", "name": "Managed Services",
    "h1": "Flieber's planners, on your team",
    "lead": ("Running demand and inventory planning in-house takes time, focus and expertise. Managed Services pairs the "
             "Flieber platform with a dedicated team of planners who co-lead your planning process with you. Your team "
             "keeps the final say on every decision."),
    "what_h2": "What Managed Services is",
    "what": ("Flieber forecasts every product on every channel, recommends what to buy and where to move it, and keeps "
             "your reports current. Our planners make sure every detail behind it is right, from setup to data quality, "
             "partner with you to bring into Flieber all the context your data doesn't carry, and help you execute and "
             "automate your operations. Think of them as an extension of your team, so yours can focus on what really "
             "matters: growing the brand."),
    "do_h2": "How our planners work with you",
    "do": [("Take part in your S&OP meetings", "Get the full context on everything that affects your decisions, from new channels to supplier changes."),
           ("Keep Flieber accurate", "Maintain mappings, parameters and the supply chain map as your business changes, so every forecast and recommendation starts from the truth."),
           ("Act as a sounding board", "Review the big decisions with you before they go out: purchase orders, transfers, promotions and launches."),
           ("Help run your planning practice", "Bring a proven way of working, drawing on experience from more than 1,000 brands.")],
    "plans_h2": "Two plans, two scopes",
    "plans_lead": "Lite covers the planning. Full adds the execution that follows your approval.",
    "plans": [
        {"id": "lite", "name": "Lite", "tag": "Planning, co-led with your team", "sub": "What's included",
         "items": [("Configuration and parameters", "New products, discontinued products, new channels, warehouse changes. Our planners keep your configuration and parameters up to date."),
                   ("Data loading", "Flieber connects natively to most of your systems. Where you still rely on spreadsheets or disconnected systems, our planners keep sales, inventory and purchase order data in sync."),
                   ("Forecast management", "Flieber's AI forecasting models give a strong baseline. Our planners review the forecasts and add what the data can't see yet, such as promotions."),
                   ("Anomaly detection", "We flag risks early, such as stockouts, overstock and sudden shifts in demand, and help you act fast."),
                   ("Replenishment recommendations", "Purchase and transfer recommendations on your schedule and in your preferred format, ready for your approval."),
                   ("Reporting", "Recurring reports tailored to each team, in the format and frequency they need.")]},
        {"id": "full", "name": "Full", "tag": "Planning and execution", "sub": "Everything in Lite, plus",
         "items": [("Purchase and transfer orders", "Once you approve, our team extracts, adjusts and sends your purchase and transfer orders."),
                   ("Production management", "Supplier follow-up at the cadence you choose, so you act early instead of reacting late."),
                   ("Freight management", "From engaging freight forwarders to checking customs documents and coordinating trucking."),
                   ("Inbound shipments", "Creating and managing FBA and 3PL inbound shipments, as part of our daily routine."),
                   ("Other specific needs", "Special projects and needs specific to your operation. Tell us about your use case.")]},
    ],
    "plans_note": "This offering doesn't include building customized software for your business, which is a separate project by Flieber's engineers.",
    "why_h2": "What it changes for your business",
    "why": [("Sell more", "Meet demand without losing revenue to stockouts."),
            ("Free up cash", "Avoid tying capital up in inventory you don't need."),
            ("Protect your margins", "Fewer mistakes, lower storage costs and a more efficient operation."),
            ("Give your team time back", "No more spreadsheets or firefighting. Our planners take on the heavy lifting.")],
    "for_h2": "Who it's for",
    "for": ["You sell across many channels, warehouses or regions", "You run kits, bundles, backorders, long lead times or high MOQs",
            "Your team is buried in spreadsheets, with no time to build or maintain an internal tool",
            "You're growing fast but don't want to hire more people",
            "You want to draw on the experience of more than 1,000 other brands to grow your business"],
    "with_h2": "How it works with the rest of Flieber",
    "with": ("Managed Services adds to any way you use Flieber: the app, your own agents through MCP or API, or the data "
             "layer on its own. Your planners and your team see the same data and context in real time. Switch or "
             "combine any time. Custom builds by Flieber's engineers are a separate project, quoted on their own."),
    "price_h2": "Pricing", "price": ("Quoted per brand on a monthly contract, after a conversation with a planner about your channels, warehouses, "
                                     "the plan that fits and where the process breaks down."),
    "price_cta": "Talk to a planner",
    "faq": [("Do your planners make decisions for us?", "No. Your team makes the calls; our planners help you make them with the best data and context. On the Full plan, our team carries out the orders and follow-ups you approve."),
            ("What's the difference between Lite and Full?", "Lite covers planning: keeping Flieber accurate, forecasts, anomalies, replenishment recommendations and reports. Full adds execution after your approval: purchase and transfer orders, supplier follow-up, freight and inbound shipments."),
            ("Can we switch between Lite and Full?", "Yes, at the end of any billing cycle."),
            ("Who are Flieber's planners?", "Specialists in demand and inventory planning who master the Flieber platform and draw on experience from more than 1,000 brands."),
            ("Do we get a dedicated planner?", "Yes. A dedicated planner works with your team, backed by a wider team at Flieber that helps with most of the tasks behind the scenes."),
            ("What hours and time zones do your planners work in?", "As a rule, 8am to 6pm Eastern Time. We can adjust for customers in very different time zones, such as Europe and Australia."),
            ("Which languages do your planners speak?", "English is the team's main language, and the team includes native speakers of other languages, such as Spanish and Portuguese."),
            ("How do we work with our planners day to day?", "They take part in your S&OP meetings, send replenishment recommendations on your schedule and in your format, flag risks as they appear and keep your recurring reports coming."),
            ("Do we still have access to the Flieber app?", "Yes. Managed Services includes everything in Self-Serve, so your team plans in the same app, with the same data, as your planners."),
            ("What access do your planners have to our data and systems?", "The access you choose to give them. At a minimum, they have full access to the data in your Flieber account. The more context you share from outside Flieber, the better their work."),
            ("Can we use our own AI agents with Managed Services?", "Yes. Your agents connect to Flieber through MCP or API and work from the same data and context as your team and your planners."),
            ("Our data lives partly in spreadsheets. Is that a problem?", "No. Flieber connects natively to most systems, and where you rely on spreadsheets or disconnected systems, our planners keep sales, inventory and purchase order data in sync."),
            ("How do promotions and launches get into the forecast?", "Your planners bring them in. They review the forecasts with you and add what the data can't see yet, such as promotions, launches and channel changes."),
            ("Do your planners talk to our suppliers and freight forwarders?", "On the Full plan, yes: supplier follow-up at the cadence you choose, freight forwarders, customs documents and trucking. On the Lite plan, your team keeps those relationships."),
            ("Do you build custom software as part of Managed Services?", "No. Custom features, dashboards, frontends and integrations are a separate project by Flieber's engineers, quoted on its own."),
            ("Is it a monthly contract?", "Yes, Managed Services runs on a monthly contract, like Self-Serve."),
            ("Is there a free trial of Managed Services?", "No. Managed Services is tailored to your operation from day one and takes real work from our team, so it starts as a paid plan. You can try the platform itself with a 14-day Self-Serve trial on your own data."),
            ("Can we start with Self-Serve and add planners later?", "Yes, at any time.")],
    "close_h2": "Talk to us about your operation",
}

# /who-we-are (brief 10)
WHO = {
    "slug": "who-we-are", "name": "Who we are",
    "h1": "Built for the operators behind modern commerce brands",
    "lead": ("Since 2019, Flieber has helped more than 1,000 commerce brands make better purchasing, sales and cash-flow "
             "decisions, with thousands of users planning on the platform."),
    "why_h2": "Why we built Flieber",
    "believe_h2": "What we believe",
    "believe": [("Decisions stay with people", "The people accountable for a decision should make it, with the best data and reasoning in front of them."),
                ("Execution should be automatic", "Once a decision is made, everything downstream should happen without manual work."),
                ("Context is the hard part", "Data is easy to collect. Keeping it current and connected to how a business actually works is what makes AI useful.")],
    "numbers_h2": "Flieber in numbers",
    "numbers": ["More than 1,000 commerce brands since 2019", "Thousands of users",
                "Forecasts 36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products, built with Nixtla"],
    "quotes_h2": "What customers say",
    "find_h2": "Where to find us",
}
