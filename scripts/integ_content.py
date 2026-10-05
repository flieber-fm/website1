"""Integrations page data (/integrations), restructured after the live flieber.com/integrations (Oct 5).

Logos and data types (Sales, Inventory, Shipments) come from the live page; names follow the approved lists in
site_content (NATIVE, ASSISTED). SPS Commerce and Apparel Magic were not on the live page: no logo, no data types.
"""

LOGOS = {  # name: (logo path, data types)
    'Amazon Seller Central': ('assets/integrations/amazon-seller-central.png', ['Sales', 'Inventory', 'Shipments']),
    'Shopify': ('assets/integrations/shopify.png', ['Sales', 'Inventory']),
    'Walmart (including WFS)': ('assets/integrations/walmart-including-wfs.png', ['Sales', 'Inventory']),
    'eBay': ('assets/integrations/ebay.png', ['Sales']),
    'Etsy': ('assets/integrations/etsy.png', ['Sales']),
    'BigCommerce': ('assets/integrations/bigcommerce.png', ['Sales', 'Inventory']),
    'Google Sheets': (None, ['Sales', 'Inventory', 'Shipments']),
    'Shopify Plus': ('assets/integrations/shopify-plus.png', ['Sales', 'Inventory']),
    'Amazon Vendor Central': ('assets/integrations/amazon-vendor-central.jpg', ['Sales']),
    'TikTok Shop': ('assets/integrations/tiktok-shop.png', ['Sales', 'Inventory']),
    'Magento': ('assets/integrations/magento.png', ['Sales', 'Inventory']),
    'WooCommerce': ('assets/integrations/woocommerce.png', ['Sales', 'Inventory']),
    'Mercado Libre': ('assets/integrations/mercado-libre.png', ['Sales', 'Inventory']),
    'bol.com': ('assets/integrations/bol-com.png', ['Sales', 'Inventory']),
    'PrestaShop': ('assets/integrations/prestashop.png', ['Sales', 'Inventory']),
    'QuickBooks': (None, ['Shipments', 'Inventory']),
    'Xero': ('assets/integrations/xero.png', ['Inventory', 'Shipments']),
    'Zoho': (None, ['Inventory', 'Shipments']),
    'Cin7': ('assets/integrations/cin7.png', ['Sales', 'Inventory', 'Shipments']),
    'Sage': ('assets/integrations/sage.png', ['Sales', 'Inventory', 'Shipments']),
    'Linnworks': (None, ['Sales', 'Inventory', 'Shipments']),
    'Brightpearl': ('assets/integrations/brightpearl.png', ['Sales', 'Inventory', 'Shipments']),
    'Luminous': ('assets/integrations/luminous.png', ['Sales', 'Inventory', 'Shipments']),
    'Finale': ('assets/integrations/finale.png', ['Sales', 'Inventory', 'Shipments']),
    'DEAR Systems': (None, ['Sales', 'Inventory', 'Shipments']),
    'Fishbowl': ('assets/integrations/fishbowl.png', ['Sales', 'Inventory', 'Shipments']),
    'SkuVault': ('assets/integrations/skuvault.png', ['Inventory', 'Shipments']),
    'ShipStation': ('assets/integrations/shipstation.png', ['Sales', 'Inventory']),
    'Anvyl': ('assets/integrations/anvyl.png', ['Shipments']),
    'Flexport/Deliverr': ('assets/integrations/flexport-deliverr.png', ['Inventory', 'Shipments']),
    'ShipBob': ('assets/integrations/shipbob.png', ['Inventory', 'Shipments']),
    'ShipHero': ('assets/integrations/shiphero.png', ['Inventory', 'Shipments']),
    'Extensiv': ('assets/integrations/extensiv.png', ['Inventory', 'Shipments']),
    'Stord': ('assets/integrations/stord.png', ['Inventory', 'Shipments']),
    'Veeqo': ('assets/integrations/veeqo.png', ['Inventory', 'Shipments']),
    'Flowspace': ('assets/integrations/flowspace.png', ['Inventory', 'Shipments']),
    'Everstox': ('assets/integrations/everstox.png', ['Inventory', 'Shipments']),
    'GoFlow': (None, ['Inventory', 'Shipments']),
    'Fulfil': ('assets/integrations/fulfil.png', ['Inventory', 'Shipments']),
    'AMZ Prep': (None, ['Inventory', 'Shipments']),
    'Logiwa': ('assets/integrations/logiwa.png', ['Inventory', 'Shipments']),
    'Unleashed': ('assets/integrations/unleashed.png', ['Inventory', 'Shipments']),
    'ShipMonk': ('assets/integrations/shipmonk.png', ['Inventory', 'Shipments']),
    '3PLGuys': ('assets/integrations/3plguys.png', ['Inventory', 'Shipments']),
    'Shipout': ('assets/integrations/shipout.png', ['Inventory', 'Shipments']),
    'EasyFulfillment': ('assets/integrations/easyfulfillment.png', ['Inventory', 'Shipments']),
    'CEVA Logistics': ('assets/integrations/ceva-logistics.png', ['Inventory', 'Shipments']),
    'World Depot Inc.': ('assets/integrations/world-depot-inc.png', ['Inventory', 'Shipments']),
    'ZhenHub': ('assets/integrations/zhenhub.png', ['Inventory', 'Shipments']),
    'NetSuite': (None, ['Sales', 'Inventory']),
}

NATIVE_DESC = {
    'Amazon Seller Central': "Connect one or more Amazon stores from any marketplace to one Flieber account and get recommendations for purchases from suppliers and transfers to FBA.",
    'Shopify': "Connect one or more Shopify stores to one Flieber account, set up kits and bundles, backorders and wholesale channels, and get purchase recommendations for every product at every inventory location.",
    'Walmart (including WFS)': "Connect one or more Walmart stores to one Flieber account and get recommendations for purchases from suppliers and transfers to WFS.",
    'TikTok Shop': "Connect one or more TikTok Shop stores to one Flieber account and get purchase recommendations for every product at every inventory location.",
    'eBay': "Connect one or more eBay stores to one Flieber account and get purchase recommendations for every product at every inventory location.",
    'Etsy': "Connect one or more Etsy stores to one Flieber account and get purchase recommendations for every product at every inventory location.",
    'BigCommerce': "Connect one or more BigCommerce stores to one Flieber account and get purchase recommendations for every product at every inventory location.",
    'Google Sheets': "Keep using your spreadsheets: connect any sales, inventory or shipment data and sync it with Flieber. We can help you automate the flow so nothing needs updating by hand.",
}

DATA_TYPES = [
    ('Sales', 'Orders and sales by product, channel and location.'),
    ('Inventory', 'On-hand, inbound and in-transit stock at every location.'),
    ('Shipments', 'Purchase orders, inbound shipments and transfers.'),
]
DATA_H2 = 'Inventory forecasts need three types of data'
DATA_BODY = ("Flieber pulls all three from the systems you already use, so it can forecast sales and inventory across every "
             "channel and location, plan replenishment and keep the right amount of stock on hand.")
ASSISTED_BODY = ("For systems without a native integration, Flieber's team sets up the connection using data modeling and "
                 "AI-based mapping.")
SEARCH_PLACEHOLDER = 'Search for your channel, ERP, 3PL or app'
API_BODY = ("Agents such as Claude, ChatGPT and Cursor connect to Flieber through its MCP server, and your own systems can use "
            "the public API.")

# Logos drawn for a dark background on the old site; shown by name only here.
NO_LOGO = {"QuickBooks", "Zoho", "Linnworks", "DEAR Systems", "NetSuite", "AMZ Prep", "GoFlow", "Google Sheets"}
