"""Positioning rebuild (Nov 28 brief, rev 133): pages rebuilt on the brief, page by page.

So far: /pricing (the three plans as levels of one offer, no prices) and /product/demand-forecasting.
Copy, structure and design follow homepage V16 (scripts/build-positioning-v16.py); the components live in assets/css/site.css.
Head, nav and footer are kept from each page's current file, so run this after build-content.py:
  python3 scripts/build-content.py && python3 scripts/build-positioning-pages.py && python3 scripts/build-positioning-v16.py \
    && python3 scripts/build-hubspot.py && python3 scripts/build-home-variants.py
The previous versions are kept in scripts/page-archive/.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = "https://www.flieber.com/book-a-demo"
ARROW = '<span class="arrow" aria-hidden="true">→</span>'
DEMO_NOTE = "Illustration · Flieber Demo Account · fictional products and people"
NIXTLA = "36% more accurate, verified by Nixtla against 16 statistical and machine-learning models on 46,000 products."
BANNED = ("Managed Services", "managed-services", "Self-Serve", "free trial", "Free trial", "Start free", "—", "alongside",
          "run by Flieber", "take over", "Flieber Studio", "Flieber Inventory", "dashboard", "single source of truth",
          "visibility", "Essentials", "Pro tier", "Max tier", "$")


# ---------- shared pieces ----------

def head(kicker: str, h2: str, hid: str, lead: str = "") -> str:
    lead_html = f'\n          <p class="lead">{lead}</p>' if lead else ""
    return f'''        <div class="section-head reveal">
          <span class="kicker">{kicker}</span>
          <h2 class="h2" id="{hid}" style="margin-top:20px">{h2}</h2>{lead_html}
        </div>'''


def card(title: str, body: str, side: str = "", lead: str = "") -> str:
    if side:
        return f'''          <article class="pv-card">
            <div class="pv-card-h">{side}<h3>{title}</h3></div>
            <p>{body}</p>
          </article>'''
    return f'''          <article class="pv-card">{lead}
            <h3>{title}</h3>
            <p>{body}</p>
          </article>'''


def faq_html(items) -> str:
    return "\n".join(f'''          <details>
            <summary>{q}<span class="plus" aria-hidden="true"></span></summary>
            <p>{a}</p>
          </details>''' for q, a in items)


def final(h2: str, hid: str) -> str:
    return f'''
    <section class="section pv-final" id="talk-to-a-specialist" aria-labelledby="{hid}">
      <div class="wrap">
        <span class="kicker">Next step</span>
        <h2 class="h2" id="{hid}">{h2}</h2>
        <div class="pv-actions">
          <a class="btn btn-primary" href="{BOOK}">Talk to a specialist {ARROW}</a>
        </div>
      </div>
    </section>'''


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


def write(rel: str, title: str, desc: str, main: str, faq=None) -> None:
    f = ROOT / rel
    src = f.read_text(encoding="utf-8")
    top = src[:src.index('  <main id="main">')]
    bottom = src[src.index("  </main>") + len("  </main>"):]
    top = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", top, count=1)
    top = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + desc, top, count=1)
    top = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + title, top, count=1)
    top = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + desc, top, count=1)
    url = "https://www.flieber.com/" + rel.replace("index.html", "").rstrip("/")
    graph = [{"@type": "WebPage", "@id": url, "url": url, "name": title, "description": desc,
              "isPartOf": {"@id": "https://www.flieber.com/#website"}, "publisher": {"@id": "https://www.flieber.com/#organization"}}]
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": strip_tags(q),
                      "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq]})
    ld = '<script type="application/ld+json">\n' + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False) + "\n  </script>"
    top = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: ld, top, count=1, flags=re.S)
    page = top + main + bottom
    body = main
    for bad in BANNED:
        assert bad not in body, f"{rel}: brief rule broken: {bad}"
    f.write_text(page, encoding="utf-8")
    print("wrote", rel)


# ---------- /pricing ----------

INCLUDED = [
    ("A platform tailored to you",
     "Demand forecasting, inventory forecasting and replenishment, with your logo and colors, set up around your products, channels, suppliers and rules."),
    ("Your requests, built in",
     "When your team needs something new, it becomes part of your platform instead of a spreadsheet workaround or a long wait on someone else’s roadmap."),
    ("Smarter every cycle",
     "Each new case becomes an automation, an alert or a simpler step, and the context gathered over time makes every forecast and plan sharper."),
    ("A monthly scorecard",
     "Every month, a scorecard on the measures you agree with us for your needs, from how your brand is doing to what your specialists did."),
]

PLANS = [
    ("lite", "Lite", "A second set of eyes on your data and plans",
     "Your team plans, decides and runs operations, in Flieber or by asking it from Claude. Your specialists watch everything so nothing slips.",
     ["Flieber kept current: data, SKU mappings, new products, stores, lead times and MOQs",
      "Integration issues followed until they’re fixed, not only flagged",
      "Early flags on what needs your attention and the decisions only you can make",
      "Forecast drift reviewed closely once you approve",
      "Context from your team, your documents and the web added to Flieber",
      "Reviews every two weeks, plus a monthly management meeting"]),
    ("core", "Core", "Planning, together with your team",
     "Everything in Lite, plus your specialists plan with your team every week.",
     ["A weekly working session to plan together",
      "Thorough forecast reviews",
      "Purchase and replenishment plans built with you, and approved plans turned into purchase-order files",
      "Your specialists in your S&amp;OP",
      "You approve every plan and order, send the orders and run operations"]),
    ("full", "Full", "Planning and operations, followed through",
     "Everything in Core, plus your specialists follow execution all the way to your warehouse.",
     ["Purchase orders placed on your approval, with supplier follow-up until production is done",
      "Freight quotes and bookings, with shipments and customs followed with your forwarder and broker",
      "Logistics followed to the warehouse, and received quantities reconciled",
      "Workflow automations for execution",
      "You still approve every plan and order and keep supplier terms, payments and budget"]),
]

HOW_PRICED = [
    ("Your size",
     "Your price follows your annual sales, sales orders and number of products, reviewed every month from the last 12 months."),
    ("Your plan",
     "Lite, Core or Full, set by how much your specialists take on. You can move up or down as your needs change."),
    ("Your proposal",
     "After a first conversation about your operation, you get a proposal with your plan, your price and your first 90 days."),
]

SCORE_BRAND = ["Stockouts and estimated lost sales", "Excess inventory", "Forecast accuracy and bias",
               "Whether our reviews improved the forecast", "Cash in inventory"]
SCORE_WORK = ["Data kept current", "Risks flagged and acted on", "Reviews held on schedule",
              "Automations shipped", "Context added to your platform"]

PRICING_FAQ = [
    ("Can I buy just the software?",
     "Not anymore. For years we sold Flieber that way, and we learned from more than 1,000 brands that software built to fit everyone leaves gaps, which teams fill with spreadsheets and workarounds. The value now comes from shaping the platform around each business, and that takes people who know the work. On Lite, your team still plans in Flieber itself, with specialists making sure nothing slips."),
    ("Why don’t you publish prices?",
     "Because your price depends on your size and your plan, and we would rather show you the right number than a range that doesn’t apply. A first conversation is enough to prepare your proposal."),
    ("Can I change plans later?",
     "Yes. Start with the plan that fits your operation today and move up or down as your needs change."),
    ("Do I lose control?",
     "No. In every plan, your team approves every plan and every order, and nothing moves without that approval."),
    ("Can my team still work in Flieber directly?",
     "Yes, in every plan. Your team works in Flieber or asks it in plain language from Claude or another AI tool connected to it. <a href=\"../prompt-ideas/\">See prompt ideas</a> for what that looks like."),
    ("How do I know it’s working?",
     "Every month you get a scorecard on the measures we agree on with you at the start, chosen for your needs. You also see the work directly: plans reviewed, risks flagged and routine moved onto automations."),
]

CHECK = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M3 8.3l3.2 3.2L13 4.7" stroke="currentColor" stroke-width="1.7"/></svg>')


def plan_card(key, name, tag, intro, items) -> str:
    lis = "\n".join(f"              <li>{CHECK}<span>{x}</span></li>" for x in items)
    return f'''          <article class="pv-card pv-plan" id="plan-{key}">
            <div class="pv-plan-top"><h3>{name}</h3><p class="pv-plan-tag">{tag}</p></div>
            <p class="pv-plan-intro">{intro}</p>
            <ul class="pv-plan-list">
{lis}
            </ul>
            <p class="pv-plan-foot">Your team approves every plan and order</p>
          </article>'''


def pricing_main() -> str:
    incl = "\n".join(card(t, b) for t, b in INCLUDED)
    plans = "\n".join(plan_card(*p) for p in PLANS)
    priced = "\n".join(card(t, b, side=f'<span class="pv-num" aria-hidden="true">{i}</span>') for i, (t, b) in enumerate(HOW_PRICED, 1))
    brand = "".join(f"<li>{x}</li>" for x in SCORE_BRAND)
    work = "".join(f"<li>{x}</li>" for x in SCORE_WORK)
    return f'''  <main id="main">

    <section class="page-head" aria-labelledby="pricing-title">
      <div class="wrap">
        <div class="section-head" style="margin-bottom:0">
          <span class="kicker">Pricing</span>
          <h1 class="h1" id="pricing-title">One offer, three levels of involvement</h1>
          <p class="lead">Every plan gives you a Flieber platform tailored to your brand and specialists who work with your team. The plans differ in how much your specialists take on. In all three, your team keeps every call.</p>
          <div class="pv-actions">
            <a class="btn btn-primary" href="{BOOK}">Talk to a specialist {ARROW}</a>
            <a class="pv-alt" href="#plans">Compare the plans</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="included" aria-labelledby="incl-title">
      <div class="wrap">
{head("Every plan", "What every plan includes", "incl-title")}
        <div class="pv-2 pv-4c pv-row pv-span2 reveal-stagger">
{incl}
        </div>
      </div>
    </section>

    <section class="section" id="plans" aria-labelledby="plans-title">
      <div class="wrap">
{head("Plans", "Choose how much your specialists take on", "plans-title", "Start with the plan that fits your operation today, and move up or down as your needs change.")}
        <div class="pv-3 pv-plans reveal-stagger">
{plans}
        </div>
      </div>
    </section>

    <section class="section section-soft" id="how-pricing-works" aria-labelledby="priced-title">
      <div class="wrap">
{head("How pricing works", "Priced monthly by your size and your plan", "priced-title")}
        <div class="pv-3 pv-row pv-span2 reveal-stagger">
{priced}
        </div>
      </div>
    </section>

    <section class="section" id="scorecard" aria-labelledby="score-title">
      <div class="wrap">
{head("Monthly scorecard", "Measures you agree on with us", "score-title", "Every month you see how your brand is doing and what your specialists did. We choose the measures with you at the start, for your needs. Some examples:")}
        <div class="pv-2 reveal-stagger">
          <article class="pv-card pv-score"><h3>How your brand is doing</h3><ul>{brand}</ul></article>
          <article class="pv-card pv-score"><h3>What your specialists did</h3><ul>{work}</ul></article>
        </div>
        <p class="pv-cite">On Full, inbound timing against plan is added. Examples, not a fixed list: your scorecard follows what matters to your brand.</p>
      </div>
    </section>

    <section class="section section-soft" id="faq" aria-labelledby="faq-title">
      <div class="wrap">
{head("Questions", "The usual ones, answered plainly", "faq-title")}
        <div class="faq reveal">
{faq_html(PRICING_FAQ)}
        </div>
      </div>
    </section>
{final("See which plan fits your operation", "final-title")}
  </main>'''


# ---------- /product/demand-forecasting ----------

STEPS5 = [
    ("Bring your data together", "Sales, inventory, purchase and transfer orders, ads and promotions, from every channel and system, through native or assisted integrations."),
    ("Correct anomalies", "Stockouts and one-off spikes are corrected, so the forecast reflects real demand. The original stays visible for your review."),
    ("Compare models", "Every model in the library is tested on your own sales, and each product and store gets the one with the lowest error."),
    ("Add events", "Promotions, ad campaigns, launches and targets your team knows about go into the forecast, for the period they cover."),
    ("Measure performance", "Accuracy and bias are tracked against what really sold, every month, so each cycle starts from what was learned."),
]

MODELS = ["Flieber AI · Blend", "Amazon Chronos 2", "Google TimesFM", "Meta Prophet", "ARIMA", "Croston", "Naive + seasonality"]

TAILOR = [
    ("Your products, your structure",
     "Forecasts follow how your catalog really works, such as style, color and size in apparel. New products are forecast from similar ones until they have their own history."),
    ("Every channel in one forecast",
     "Amazon, Shopify, Walmart and wholesale are forecast product by product and store by store, with wholesale demand reconciled when orders land on dates that passed."),
    ("Context without limits",
     "Marketing plans, cash, past decisions and what the web says about your brand and market go in with your data, so the forecast reflects how your business works."),
]

DF_PLANS = [
    ("Lite", "Your specialists keep products, stores and settings current, flag forecasts that look wrong and review drift closely once you approve."),
    ("Core", "Everything in Lite, plus thorough forecast reviews with your team every cycle and your forecast reviewed in your S&amp;OP meetings."),
    ("Full", "Everything in Core, with your approved forecast carried through to purchase orders, suppliers and freight, always on your approval."),
]

FEATURES = [
    ("AI demand forecasts", "Product and channel forecasts across marketplaces, DTC and wholesale, built from corrected history and seasonality."),
    ("Sales history corrected for anomalies", "Stockouts, spikes and promotions corrected, with actual sales shown next to the demand used for forecasting."),
    ("Your forecasts and adjustments", "Import your own forecasts or adjust by product, store, channel or group, including planned promotions and events."),
    ("Targets and new products", "Growth percentages, unit or revenue targets across selected products, and new products forecast from similar ones."),
    ("Forecast accuracy and bias", "Error and bias by month, with past forecast versions kept so predictions can be compared with what sold."),
    ("Wholesale forecast reconciliation", "Finds wholesale demand parked on dates that passed without a sale and suggests where to move it. On request."),
]

WK = [52, 55, 50, 58, 61, 57, 63, 60, 0, 0, 0, 62, 66, 64, 128, 63, 67, 65, 70, 68]
GAPS, SPIKE = (8, 9, 10), 14


def psr_view() -> str:
    """Past sales review, as in the Demand Forecast video: a stockout filled in, a one-off spike corrected."""
    w, h, n = 300, 120, len(WK)
    bw = w / n
    bars = []
    for k, v in enumerate(WK):
        val = 62 if v == 0 else (64 if k == SPIKE else v)
        y = h - 18 - val * 0.7
        cls = "df-gap" if k in GAPS else "df-fix" if k == SPIKE else "df-bar"
        bars.append(f'<rect class="{cls}" x="{k * bw + 2:.1f}" y="{y:.1f}" width="{bw - 4:.1f}" height="{h - 18 - y:.1f}" rx="2"/>')
        if k == SPIKE:
            y0 = h - 18 - v * 0.7
            bars.append(f'<rect class="df-orig" x="{k * bw + 2:.1f}" y="{y0:.1f}" width="{bw - 4:.1f}" height="{y - y0:.1f}" rx="2"/>')
    return f'''<div class="df-view">
              <div class="df-view-h"><span class="df-tier">A</span><b>BLCK-SPRT-JRSY</b><small>Past sales review · last 20 weeks · Amazon US</small></div>
              <svg viewBox="0 0 {w} {h}" fill="none" aria-hidden="true">{"".join(bars)}
                <text x="{9 * bw + bw / 2:.1f}" y="{h - 4}" text-anchor="middle" class="df-t">stockout · 3 weeks</text>
                <text x="{SPIKE * bw + bw / 2:.1f}" y="12" text-anchor="middle" class="df-t">one-off spike</text>
              </svg>
              <div class="df-rows">
                <div><span class="df-ok">Corrected</span><b>Stockout</b><small>filled to the level before and after</small><em>For your review</em></div>
                <div><span class="df-ok">Corrected</span><b>One-off spike</b><small>2× normal, outside any retail event</small><em>For your review</em></div>
              </div>
            </div>'''


def model_view() -> str:
    rows = [("Flieber AI · Blend", 24, 31, 38), ("Amazon Chronos 2", 26, 33, 37), ("Google TimesFM", 27, 30, 39),
            ("Meta Prophet", 31, 34, 35), ("Seasonal ARIMA", 28, 29, 34), ("Naive + seasonality", 29, 26, 41)]
    best = [min(r[j] for r in rows) for j in (1, 2, 3)]
    tr = "".join(f'<tr><td>{r[0]}</td>' + "".join(f'<td{" class=\"df-best\"" if r[j] == best[j - 1] else ""}>{r[j]}%</td>' for j in (1, 2, 3)) + "</tr>" for r in rows)
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Model</b><small>every model tested on your sales · error a month ahead</small></div>
              <table class="df-table"><tr><th>Model</th><th>Amazon US</th><th>Shopify US</th><th>Wholesale US</th></tr>{tr}</table>
              <p class="df-note">Each product uses the model with the lowest error, store by store.</p>
            </div>'''


def changes_view() -> str:
    rows = [("Nov 20 · 10:42", "Maya Chen", "your team", "Holiday promotion · Dec 1–24 · +15%"),
            ("Nov 18 · 16:05", "Rafael Lima", "Flieber team", "Took out a one-off week · Amazon US"),
            ("Nov 12 · 09:30", "Rafael Lima", "Flieber team", "Shopify US → Naive + seasonality")]
    tr = "".join(f'<div class="df-log-r"><small>{w}</small><span><b>{n}</b><i>{r}</i></span><span>{c}</span><em>↶ Undo</em></div>' for w, n, r, c in rows)
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Changes</b><small>every change, by whom and why · each can be undone</small></div>
              <div class="df-log">{tr}</div>
            </div>'''


def claude_view() -> str:
    return '''<div class="df-view df-chat">
              <div class="df-view-h"><b>Claude</b><small>connected to Flieber</small></div>
              <p class="df-u">Add 15% to December for BLCK-SPRT-JRSY, for our holiday promotion.</p>
              <p class="df-a">Done: December 2026 is now 10,706 units (+15%) in your demand forecast, logged as a change by Maya Chen.</p>
              <p class="df-u">Why did GREY-CHNL-MATS drop?</p>
              <p class="df-a">Two stockout weeks in October. They are filled in the history, so the forecast is not pulled down.</p>
            </div>'''


def drift_view() -> str:
    import math
    n, w, h = 20, 300, 120
    x = lambda k: 10 + k * (w - 20) / (n - 1)
    y = lambda v: h - 16 - (v - 50) * 1.6
    appr = [92 + 6 * math.sin(k / 3) for k in range(n)]
    act = [appr[k] * (0.97 - k * 0.03) for k in range(8)]
    mdl = [appr[k] * 0.8 for k in range(6, n)]
    path = lambda pts: "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts)
    bars = "".join(f'<rect class="df-bar" x="{x(k) - 5:.1f}" y="{y(v):.1f}" width="10" height="{h - 16 - y(v):.1f}" rx="2"/>' for k, v in enumerate(act))
    return f'''<div class="df-view">
              <div class="df-view-h"><span class="df-tier">A</span><b>BLCK-SPRT-JRSY</b><span class="df-warn">Drifted −17% since approval</span></div>
              <svg viewBox="0 0 {w} {h}" fill="none" aria-hidden="true">{bars}
                <path class="df-appr" d="{path([(x(k), y(v)) for k, v in enumerate(appr)])}"/>
                <path class="df-mdl" d="{path([(x(k), y(v)) for k, v in zip(range(6, n), mdl)])}"/>
                <line class="df-now" x1="{x(7.5):.1f}" x2="{x(7.5):.1f}" y1="4" y2="{h - 16}"/><text x="{x(7.5) + 4:.1f}" y="12" class="df-t">today</text>
              </svg>
              <div class="df-legend"><span class="l-ap">The forecast you approved</span><span class="l-ac">What is really happening</span><span class="l-md">What the models now say</span></div>
              <div class="df-act"><span>Sales and the models both run below what was approved</span><em class="df-btn">Keep it</em><em class="df-btn y">Review the forecast</em></div>
            </div>'''


DF_FAQ = [
    ("Which models does Flieber use?",
     "A library that includes Flieber’s own AI blend, Amazon Chronos 2, Google TimesFM, Meta Prophet, ARIMA, Croston and simpler baselines such as naive with seasonality. Each is tested on your own sales, and each product and store uses the one with the lowest error."),
    ("Can we use our own forecasts?",
     "Yes. Import your own forecasts or adjust any product, store, channel or group, and every change is logged with who made it and why."),
    ("What about products with no sales history?",
     "New products are forecast from similar products or from a curve you set, until they have enough history of their own."),
    ("Do I have to approve every forecast?",
     "Your team approves the forecast before it drives purchase plans. After that, Flieber watches it and flags drift, so you decide whether to keep it or update it."),
]


def df_main() -> str:
    steps = "\n".join(f'''            <li><span class="pv-num" aria-hidden="true">{i}</span><div><b>{t}</b><p>{b}</p></div></li>''' for i, (t, b) in enumerate(STEPS5, 1))
    tailor = "\n".join(card(t, b) for t, b in TAILOR)
    plans = "\n".join(card(n, b) for n, b in DF_PLANS)
    feats = "\n".join(f'            <div class="pv-feat"><b>{t}</b><span>{b}</span></div>' for t, b in FEATURES)
    chips = "".join(f'<span class="pv-chip">{m}</span>' for m in MODELS)
    return f'''  <main id="main">

    <section class="page-head pv-phead" aria-labelledby="df-title">
      <div class="wrap pv-hero-grid">
        <div>
          <span class="kicker">Product · Demand forecasting</span>
          <h1 class="h1" id="df-title">Forecast what would have sold, not just what did</h1>
          <p class="lead">Stockouts, one-off spikes and promotions distort sales history. Flieber corrects them, tests every model in its library on your own sales and adds the context your team knows. Your Flieber specialists keep it right as your business changes, and your team approves every forecast.</p>
          <div class="pv-actions">
            <a class="btn btn-primary" href="{BOOK}">Talk to a specialist {ARROW}</a>
            <a class="pv-alt" href="#how-it-works">See how it works</a>
          </div>
        </div>
        <figure class="pv-video" aria-label="Demand forecasting video">
          <span class="pv-play" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 22 22"><path d="M5 3l14 8-14 8z" fill="#1B1C1C"/></svg></span>
          <p><span class="pv-ph">Video placeholder</span><br><b>Demand forecasting, in about four minutes.</b> The approved module video goes here once its closing card is re-cut for the new offer.</p>
        </figure>
      </div>
    </section>

    <section class="section section-soft" id="how-it-works" aria-labelledby="steps-title">
      <div class="wrap">
{head("How it works", "A process, not a number", "steps-title", "A forecast is only as good as the process behind it. Flieber follows the same five steps for every product, on every channel.")}
        <div class="pv-build">
          <ol class="pv-steps5 reveal">
{steps}
          </ol>
          <div class="reveal">
            {psr_view()}
            <p class="pv-demo">{DEMO_NOTE}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="models" aria-labelledby="models-title">
      <div class="wrap">
        <div class="pv-build">
          <div class="reveal">
            <span class="kicker">Models</span>
            <h2 class="h2" id="models-title" style="margin-top:20px">The best model for each product, store by store</h2>
            <p class="lead">No single model wins everywhere. Flieber tests every model in its library on your own sales and picks the one with the lowest error for each product and store, then checks again as your sales change.</p>
            <div class="pv-integ">{chips}</div>
            <p class="pv-cite">{NIXTLA}</p>
          </div>
          <div class="reveal">
            {model_view()}
            <p class="pv-demo">{DEMO_NOTE}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="tailored" aria-labelledby="tailor-title">
      <div class="wrap">
{head("Tailored to your brand", "Built around how you operate", "tailor-title", "You don’t adapt to the software. Your demand forecasting is set up around your catalog, your channels and everything your team knows.")}
        <div class="pv-3 pv-row pv-span2 reveal-stagger">
{tailor}
        </div>
      </div>
    </section>

    <section class="section" id="your-call" aria-labelledby="call-title">
      <div class="wrap">
{head("Your team keeps every call", "Every change visible, every change yours", "call-title", "Your team and your specialists work on the same forecast. Change it on screen or ask from Claude, and every change shows who made it, when and why.")}
        <div class="pv-2 reveal-stagger">
          <div>{changes_view()}<p class="pv-demo">{DEMO_NOTE}</p></div>
          <div>{claude_view()}<p class="pv-demo">{DEMO_NOTE}</p></div>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="after-approval" aria-labelledby="drift-title">
      <div class="wrap">
        <div class="pv-build">
          <div class="reveal">
            <span class="kicker">After approval</span>
            <h2 class="h2" id="drift-title" style="margin-top:20px">Watched week by week, not set and forgotten</h2>
            <p class="lead">Once your team approves a forecast, Flieber keeps comparing it with what really sells and with what the models now say. When they drift apart, it flags the product so you can keep the forecast or review it before it reaches a purchase order.</p>
          </div>
          <div class="reveal">
            {drift_view()}
            <p class="pv-demo">{DEMO_NOTE}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="your-specialists" aria-labelledby="spec-title">
      <div class="wrap">
{head("Your specialists", "What your specialists do, plan by plan", "spec-title")}
        <div class="pv-3 pv-row pv-span2 reveal-stagger">
{plans}
        </div>
        <p class="pv-cite"><a href="../../pricing/#plans">Compare the plans</a></p>
      </div>
    </section>

    <section class="section section-soft" id="features" aria-labelledby="feat-title">
      <div class="wrap">
{head("Features", "What’s included", "feat-title")}
        <div class="pv-feats reveal">
{feats}
        </div>
      </div>
    </section>

    <section class="section" id="faq" aria-labelledby="faq-title">
      <div class="wrap">
{head("Questions", "About demand forecasting", "faq-title")}
        <div class="faq reveal">
{faq_html(DF_FAQ)}
        </div>
      </div>
    </section>
{final("See what demand forecasting looks like for your brand", "final-title")}
  </main>'''


def main() -> None:
    write("pricing/index.html", "Pricing: one offer, three plans | Flieber",
          "One offer in three plans, Lite, Core and Full: a platform tailored to your brand and Flieber specialists who work with your team. Priced monthly by your size and plan.",
          pricing_main(), PRICING_FAQ)
    write("product/demand-forecasting/index.html", "Demand forecasting | Flieber",
          "Forecasts for every product on every channel, from corrected sales history, the best model for each product and the context your team adds. Your team approves every forecast.",
          df_main(), DF_FAQ)


if __name__ == "__main__":
    main()
