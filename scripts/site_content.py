"""Single source for /features, /agents, llms.txt, llms-full.txt and capabilities.json.

Copy comes verbatim from "26-10-02 Website - Content Briefing" (sections 4 to 6).
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

# ---------------------------------------------------------------- /features
FEATURES_INTRO = ("Flieber is one product. Every feature on this page works the same whether you use it in the "
                  "Flieber app, ask for it in plain language, or call it from your own agents and systems through "
                  "MCP or API. It's grouped the way Flieber works: keep your data true, turn it into decisions and act on them.")
FEATURES_NOTE = ("Available with Flieber Self-Serve and Flieber Managed Services. During the 14-day free trial, data "
                 "comes in through native integrations; assisted integrations and customizations come with a paid plan. "
                 "Features marked \"on request\" are rolling out and are switched on when you ask.")

# access: read | write | read_write | None ; availability: general | on_request
GROUPS = [
    {
        "id": "data", "label": "Data", "h2": "Keep your data true",
        "lead": "Flieber connects every channel, warehouse and supplier, then adds the business context none of them hold.",
        "features": [
            ("Data health", "Checks your account for issues, gaps and anomalies, applies the fixes it can and flags the ones that need a person.", "read_write", "general"),
            ("Cross-channel SKU mapping", "Links listings and SKUs across channels to one master product, so sales consolidate for planning. Automatic matching, plus bulk catalog import and export.", "write", "general"),
            ("Kits, bundles and components", "Turns demand for bundles into component requirements. Buy at component level and transfer inventory as finished products.", "write", "general"),
            ("Product configuration and classification", "Product status, custom attributes, costs, prices and packaging units. ABCD classification ranks products by sales, units or profit using your thresholds.", "write", "general"),
            ("Supply chain map", "Suppliers, warehouses, 3PLs and channels, with fulfillment and fallback locations, transfer routes, production and transit lead times and ordering cadence.", "write", "general"),
            ("Sales history adjusted for anomalies", "Corrects history distorted by stockouts, spikes and promotions, and shows actual sales next to the adjusted demand used for forecasting.", "read", "general"),
            ("Inventory history and balances", "Snapshots and balances across every connected location, including inbound and in-transit stock.", "read", "general"),
            ("Uploads and Google Sheets", "Bulk updates to catalog, forecasts, shipments, bundles and wholesale data through CSV files or Google Sheets, with a preview before anything is saved.", "write", "general"),
            ("Organizations and users", "Manage several organizations from one place, with unlimited users on every plan and Admin and Member roles.", "write", "general"),
        ],
    },
    {
        "id": "decisions", "label": "Decisions", "h2": "Turn it into decisions",
        "lead": "Forecasts, projections and simulations built on the same data, so every recommendation comes with reasoning you can check.",
        "features": [
            ("AI demand forecasts", "Product and channel level forecasts across marketplaces, DTC and wholesale, built from adjusted history and seasonality. " + ACCURACY, "read", "general"),
            ("Forecast overrides and uploads", "Import your own forecasts, or adjust at SKU, store, channel or group level, including planned promotions and events.", "write", "general"),
            ("Targets and new products", "Apply growth percentages, unit targets or revenue targets across selected products. Forecast new products from similar ones or from a manual curve.", "write", "general"),
            ("Forecast accuracy and bias", "Error and bias metrics, with monthly forecast versions saved so past predictions can be compared with what actually sold. Forecast value added reports on request.", "read", "general"),
            ("Wholesale forecast reconciliation", "Finds wholesale demand parked on dates that passed without a sale and suggests where to move it. On request.", "read_write", "on_request"),
            ("Inventory projections", "Stock by product, channel and location from on-hand, inbound and forecast demand, with days of cover and consolidated warehouse needs.", "read", "general"),
            ("Stockouts, overstock and lost sales", "Projected stockout dates, products below safety stock, excess inventory and the sales lost to unavailable stock or late shipments.", "read", "general"),
            ("Backorders and preorders", "Counts accumulated backorder demand in inventory and replenishment calculations, with settings by channel, and plans for products sold before they arrive.", "read", "general"),
            ("Purchase and transfer recommendations", "What to order or transfer, how much and when, by product and location, including replenishment from warehouses or 3PLs to fulfillment locations such as FBA.", "read", "general"),
            ("Planning parameters", "Safety stock, target days of cover, overstock thresholds, lead times and order frequency, with rules for products, categories and channels.", "write", "general"),
            ("Order and shipping constraints", "Minimum order quantities and supplier constraints, container planning and rounding to case packs, cartons or pallets.", "read", "general"),
            ("Decision simulations", "Test changes to order quantities, demand, arrival dates or lead times and see the effect on inventory, revenue, margin and cash before anything is committed.", "write", "general"),
            ("Multi-month purchase planning", "Splits a long buying horizon into seasonally weighted purchase orders, with cartons, MOQs and lead times applied and periods already covered by stock left at zero.", "write", "general"),
            ("AI order-quantity adjustments", "Rebalances planned quantities across destinations and fits orders to container capacity, budget and cash-flow limits, following notes you write in plain language.", "write", "general"),
        ],
    },
    {
        "id": "actions", "label": "Actions", "h2": "Act on it",
        "lead": "Once a decision is approved, Flieber carries it into the systems where it lands.",
        "features": [
            ("Saved plans and purchase orders", "Replenishment plans by supplier and date, with costs. Create and track POs, group them under master POs and record placed-order status.", "write", "general"),
            ("Purchase orders to suppliers", "Sends each PO straight into the supplier's system or as an email, CSV file or Google Sheet in the supplier's own format, with products identified by SKU or product name.", "write", "general"),
            ("Purchase orders to ERPs", "Pushes approved POs into NetSuite or light ERPs such as Cin7 and Brightpearl.", "write", "general"),
            ("Inbound shipments in Amazon and 3PLs", "Creates inbound shipments in Amazon and in connected 3PL and warehouse systems from an approved plan.", "write", "general"),
            ("Inbound shipment tracking", "Follows POs and shipments through delivery, with manual entry, Google Sheets sync and automatic import of connected inbound shipments such as Amazon FBA.", "read", "general"),
            ("Alerts and scheduled reports", "Scheduled checks for stockout risk, excess inventory and orders due, delivered by email, Slack, Microsoft Teams or Google Sheets.", "write", "general"),
            ("Custom workflows and agents", "Describe a recurring job in plain language and Flieber runs it on schedule, across its own data and your connected apps.", "write", "general"),
            ("Actions in other systems", "Flieber is also an MCP client, so it can connect to any system with an MCP server and act where the decision lands: adjust an ad campaign, update a price, confirm with a supplier.", "write", "general"),
        ],
    },
    {
        "id": "access", "label": "Access", "h2": "Use it your way",
        "lead": "The same data and the same context, wherever you work.",
        "features": [
            ("Flieber app", "Planning screens, saved views, dashboards and exports to CSV.", None, "general"),
            ("Ask in plain language", "Ask questions about your data and get answers, tables, charts and dashboards. Save reports, refresh them and keep the conversation going.", None, "general"),
            ("Slack", "Ask questions and receive alerts in Slack.", None, "general"),
            ("Google Sheets add-on", "Pulls Flieber data into your own sheets and refreshes it on a schedule.", None, "general"),
            ("MCP server", "Connect Claude, Cursor or your own agents. Requests go to Flieber's own agent (Flieber Studio), which answers questions and carries out the same actions as the app, following your approval rules. Answers typically take 30 seconds to 5 minutes. Full action list in the MCP docs (customer login required).", None, "general"),
            ("MCP client and connected apps", "Flieber connects out to Gmail, Outlook, Slack, Microsoft Teams, Google Sheets, OneDrive, Notion, Airtable, Meta Ads, Google Ads and NetSuite, and to any other system with an MCP server.", None, "general"),
            ("Public API", "Programmatic access to Flieber data for your own systems. Details in the MCP docs (customer login required).", None, "general"),
        ],
    },
]

APPROVAL_H2 = "You decide what runs on its own"
APPROVAL_BODY = ("Flieber prepares the decision; you decide how much it does without asking. By default, every change "
                 "Flieber makes, in Flieber or in your other systems, waits for your approval: you see a preview and "
                 "confirm. When you ask for a change in a conversation, Flieber always shows the preview first. For "
                 "scheduled workflows you choose: let a weekly export or a data update run on its own, and keep approval "
                 "on purchase orders. Change it any time.")

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
    ("Does Flieber handle kits and bundles?", "Yes. Bundle demand is converted into component requirements, and you can buy components and transfer finished goods."),
    ("Does Flieber plan Amazon FBA replenishment?", "Yes. It recommends transfers from warehouses or 3PLs to FBA, creates the inbound shipments in Amazon and tracks them to delivery."),
    ("Can Flieber send purchase orders to my ERP?", "Yes, to NetSuite and to light ERPs such as Cin7 and Brightpearl, following your approval rules."),
    ("Can Flieber send purchase orders to my suppliers?", "Yes. Flieber sends each PO straight into the supplier's system or as an email, CSV file or Google Sheet in that supplier's format."),
    ("Does Flieber account for MOQs, case packs and containers?", "Yes. Quantities are rounded to case packs, cartons and pallets, and orders can be fitted to container capacity."),
    ("Does Flieber correct sales history for stockouts?", "Yes. History distorted by stockouts, spikes and promotions is adjusted before forecasting, and actual sales stay visible alongside."),
    ("Does Flieber handle backorders and preorders?", "Yes, with settings by channel."),
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
SUMMARY = ("Flieber keeps a commerce brand's data consolidated, contextualized and up to date: sales, inventory, orders, "
           "catalog, ads and pricing, joined with the business context no single system holds (SKU and supply chain "
           "mapping, replenishment rules, adjusted sales history). On top of that data it forecasts demand at SKU level, "
           "simulates the effect of purchasing, pricing, advertising and allocation decisions on inventory, revenue, "
           "margin and cash, and pushes approved decisions to ERPs, marketplaces, 3PLs and suppliers, following approval "
           "rules the brand sets. It is one product offered two ways: Self-Serve, where the brand's team uses the Flieber "
           "app or connects its own agents and systems through MCP or API; and Managed Services, where Flieber's "
           "specialized planners join the brand's team and help run its planning practice.")

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
    ("Free trial", "14 days, no credit card required, on the brand's own data. Native integrations only during the trial; standard setup included. Assisted integrations and customizations require a paid plan.", TRIAL),
    ("MCP server", "Claude, Cursor and other MCP-compatible agents connect to Flieber's MCP server. Requests are handled in natural language by Flieber's own agent (Flieber Studio), which answers questions and carries out the actions the Flieber app supports, under the account's approval rules. Answers typically take 30 seconds to 5 minutes; a conversation can continue across calls. Full action list (customer login required):", DEV_DOCS),
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
    "**Flieber Self-Serve:** priced to your operation, based on features enabled and data volume. The exact price is shared on a demo.",
    "**Flieber Managed Services:** quoted per brand, after a conversation with a planner about channels, warehouses and where the process breaks down.",
    "Monthly contracts, no annual commitment.",
    "14-day free trial, no credit card required.",
    "Unlimited users on every plan, including the free trial.",
    "Standard setup included; customizations come with a paid plan.",
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
