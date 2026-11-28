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
NIXTLA = "Developed with Nixtla: 36% more accurate than our previous portfolio of 16 forecasting models, tested on 46,000 products."  # conservative wording (Fabricio, Nov 28)
BANNED = ("Managed Services", "managed-services", "Self-Serve", "free trial", "Free trial", "Start free", "—", "alongside",
          "run by Flieber", "take over", "Flieber Studio", "Flieber Inventory", "dashboard", "single source of truth",
          "visibility", "Essentials", "Pro tier", "Max tier", "Beyond inventory")


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


def write(rel: str, title: str, desc: str, main: str, faq=None, extra_banned=()) -> None:
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
    for bad in BANNED + tuple(extra_banned):
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


def changes_view(rows=None) -> str:
    rows = rows or [("Nov 20 · 10:42", "Maya Chen", "your team", "Holiday promotion · Dec 1–24 · +15%"),
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


# ---------- module page skeleton ----------

def hero(kicker, h1, hid, lead, video: bool, alt_href="#how-it-works", alt="See how it works") -> str:
    if video:
        right = '''<figure class="pv-video" aria-label="Module video">
          <span class="pv-play" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 22 22"><path d="M5 3l14 8-14 8z" fill="#1B1C1C"/></svg></span>
          <p><span class="pv-ph">Video placeholder</span><br><b>The approved module video goes here</b> once its closing card is re-cut for the new offer.</p>
        </figure>'''
    else:
        right = '''<figure class="pv-video" aria-label="Module video">
          <span class="pv-play" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 22 22"><path d="M5 3l14 8-14 8z" fill="#1B1C1C"/></svg></span>
          <p><span class="pv-ph">Video placeholder</span><br><b>The workflows video is in production.</b> It goes here once approved.</p>
        </figure>'''
    return f'''
    <section class="page-head pv-phead" aria-labelledby="{hid}">
      <div class="wrap pv-hero-grid">
        <div>
          <span class="kicker">{kicker}</span>
          <h1 class="h1" id="{hid}">{h1}</h1>
          <p class="lead">{lead}</p>
          <div class="pv-actions">
            <a class="btn btn-primary" href="{BOOK}">Talk to a specialist {ARROW}</a>
            <a class="pv-alt" href="{alt_href}">{alt}</a>
          </div>
        </div>
        {right}
      </div>
    </section>'''


def split(sid, kicker, h2, hid, lead, view, soft=False, extra="", flip=False) -> str:
    text = f'''<div class="reveal">
            <span class="kicker">{kicker}</span>
            <h2 class="h2" id="{hid}" style="margin-top:20px">{h2}</h2>
            <p class="lead">{lead}</p>{extra}
          </div>'''
    pic = f'''<div class="reveal">
            {view}
            <p class="pv-demo">{DEMO_NOTE}</p>
          </div>'''
    a, b = (pic, text) if flip else (text, pic)
    return f'''
    <section class="section{' section-soft' if soft else ''}" id="{sid}" aria-labelledby="{hid}">
      <div class="wrap">
        <div class="pv-build">
          {a}
          {b}
        </div>
      </div>
    </section>'''


def cards_section(sid, kicker, h2, hid, lead, items, soft=False, after="") -> str:
    cards = "\n".join(card(t, b) for t, b in items)
    return f'''
    <section class="section{' section-soft' if soft else ''}" id="{sid}" aria-labelledby="{hid}">
      <div class="wrap">
{head(kicker, h2, hid, lead)}
        <div class="pv-3 pv-row pv-span2 reveal-stagger">
{cards}
        </div>{after}
      </div>
    </section>'''


def tail(plans, features, faq, final_h2, soft_first=False) -> str:
    feats = "\n".join(f'            <div class="pv-feat"><b>{t}</b><span>{b}</span></div>' for t, b in features)
    a, b = ("section section-soft", "section") if soft_first else ("section", "section section-soft")
    return f'''{cards_section("your-specialists", "Your specialists", "What your specialists do, plan by plan", "spec-title", "", plans, soft=soft_first,
                      after='\n        <p class="pv-cite"><a href="../../pricing/#plans">Compare the plans</a></p>')}

    <section class="{b}" id="features" aria-labelledby="feat-title">
      <div class="wrap">
{head("Features", "What’s included", "feat-title")}
        <div class="pv-feats reveal">
{feats}
        </div>
      </div>
    </section>

    <section class="{a}" id="faq" aria-labelledby="faq-title">
      <div class="wrap">
{head("Questions", "Asked often", "faq-title")}
        <div class="faq reveal">
{faq_html(faq)}
        </div>
      </div>
    </section>
{final(final_h2, "final-title")}'''


def chips(items) -> str:
    return '\n            <div class="pv-integ">' + "".join(f'<span class="pv-chip">{m}</span>' for m in items) + "</div>"


# ---------- /product/inventory-forecasting ----------

def inv_sim(start, dem, inb=(), n=90):
    s, st = start, []
    for k in range(n):
        for d, q in inb:
            if k == d:
                s += q
        s = max(0, s - dem(k))
        st.append(s)
    return st


def inv_svg(st, alt=None, w=300, h=120, top=None, safety=None, target=None, mark=None, label=None) -> str:
    top = top or max(st + (alt or []) + [target or 0]) * 1.1
    n = len(st)
    x = lambda k: 8 + k * (w - 16) / (n - 1)
    y = lambda v: h - 16 - v / top * (h - 30)
    path = lambda vals: "M" + " L".join(f"{x(k):.1f} {y(v):.1f}" for k, v in enumerate(vals))
    band = (f'<rect x="8" width="{w - 16}" y="{y(target):.1f}" height="{y(safety) - y(target):.1f}" class="pv-iv-band"/>'
            f'<text x="{w - 10}" y="{y(safety) - 4:.1f}" text-anchor="end" class="df-t">safety</text>') if safety else ""
    lost = ""
    zero = [k for k, v in enumerate(st) if v == 0]
    if zero:
        lost = (f'<rect x="{x(zero[0]):.1f}" width="{x(zero[-1]) - x(zero[0]) + 2:.1f}" y="14" height="{h - 30}" class="pv-iv-lost"/>'
                f'<text x="{x(zero[0]) - 3:.1f}" y="24" text-anchor="end" class="df-t df-red">stockout</text>')
    alt_p = f'<path class="df-alt" d="{path(alt)}"/>' if alt else ""
    m = (f'<path d="M{x(mark) - 5:.1f} 4 L{x(mark) + 5:.1f} 4 L{x(mark):.1f} 12Z" class="df-mark"/>'
         f'<text x="{x(mark) + 8:.1f}" y="11" class="df-t">{label}</text>') if mark is not None else ""
    return f'''<svg viewBox="0 0 {w} {h}" fill="none" aria-hidden="true">{band}{lost}
                <path d="M8 {h - 16} H{w - 8}" class="df-base"/><path class="df-line" d="{path(st)}"/>{alt_p}{m}
              </svg>'''


IF_ROWS = [("A", "BLCK-SPRT-JRSY", "FBA US", "9 days", "sl", "Stockout likely", "Buy 1,800 by Dec 2"),
           ("A", "GREY-CHNL-MATS", "FBA CA", "0 days", "so", "Out of stock", "Transfer 400 now"),
           ("B", "BLCK-CFEE-MAKR", "3PL US", "16 days", "bs", "Below safety", "Buy 600 by Dec 6"),
           ("B", "PINK-TRVL-BKPK", "FBA EU", "48 days", "hl", "Healthy", "No action"),
           ("C", "ALMN-CRON-LUGG", "FBA UK", "74 days", "hl", "Healthy", "No action")]


def if_products_view() -> str:
    rows = "".join(f'<tr><td><span class="df-tier">{t}</span> {c}</td><td>{loc}</td><td>{d}</td><td><span class="df-st df-st-{k}">{l}</span></td><td>{a}</td></tr>'
                   for t, c, loc, d, k, l, a in IF_ROWS)
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Products</b><small>every product at every location · days of cover · next action</small></div>
              <div class="df-scroll"><table class="df-table"><tr><th>Product</th><th>Location</th><th>Cover</th><th>Status</th><th>Next</th></tr>{rows}</table></div>
            </div>'''


NET = [("Supplier", "Supplier 1", "makes to order"), ("Origin storage", "3PL China", "4,800 on hand"),
       ("Regional storage", "3PL US · 3PL EU", "3,120 · 1,640 on hand"), ("Fulfillment and channels", "FBA US · Shopify US · FBA EU · Wholesale EU", "")]
NET_LT = ["45 days", "30 to 35 days", "6 to 7 days"]


def if_network_view() -> str:
    parts = []
    for i, (r, n, s) in enumerate(NET):
        parts.append(f'<div class="df-node"><small>{r}</small><b>{n}</b>{f"<span>{s}</span>" if s else ""}</div>')
        if i < len(NET_LT):
            parts.append(f'<div class="df-edge"><span>{NET_LT[i]}</span></div>')
    params = "".join(f"<span><small>{a}</small><b>{b}</b></span>" for a, b in [("Safety stock", "21 days"), ("Target", "50 days"), ("MOQ", "500"), ("Case pack", "24")])
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Supply chain</b><small>from your supplier to every channel · lead times on each route</small></div>
              <div class="df-net">{"".join(parts)}</div>
              <div class="df-onway">On the way · PO-1042 · 2,400 units</div>
              <div class="df-params">{params}</div>
            </div>'''


def if_flags_view() -> str:
    flags = [("Lead time missing", "3PL China → 3PL EU", "Filled by rule · 35 days"),
             ("Lead time missing", "3PL EU → FBA EU", "Filled by rule · 6 days"),
             ("Safety stock not set", "04PC-PLCM-SETT · tier B", "Filled by rule · 21 days"),
             ("No demand forecast", "New listing · PINK-TRVL-BKPK · Shopify EU", "For your review")]
    rows = "".join(f'<div><b>{a}</b><small>{b}</small><em>{c}</em></div>' for a, b, c in flags)
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Flags</b><small>gaps in the data, found before they distort a plan</small></div>
              <div class="df-flags">{rows}</div>
            </div>'''


def if_scenario_view() -> str:
    base = inv_sim(1500, lambda k: 42 * (1.25 if 7 <= k <= 30 else 1), [(42, 2400)])
    alt = inv_sim(1500, lambda k: 42 * (1.25 if 7 <= k <= 30 else 1), [(24, 2400), (49, 1200)])
    acts = "".join(f'<span class="df-sc{" on" if i == 0 else ""}"><b>{a}</b><small>{b}</small></span>' for i, (a, b) in enumerate(
        [("Add a purchase", "1,200 units · Jan 12"), ("Delay a shipment", "PO-1042 · Dec 18 → Jan 5"), ("Raise demand", "+25% · Dec 1–24")]))
    return f'''<div class="df-view">
              <div class="df-view-h"><span class="df-tier">A</span><b>BLCK-SPRT-JRSY</b><small>Scenarios · projected stock, next 90 days</small></div>
              <div class="df-scs">{acts}</div>
              {inv_svg(base, alt=alt, safety=21 * 42, target=50 * 42, mark=24, label="PO-1042")}
              <div class="df-legend"><span class="l-ap">Projected stock today</span><span class="l-md">With the changes you are testing</span></div>
            </div>'''


IF_TAILOR = [
    ("Your supply chain, as it is",
     "From factory to origin storage, regional warehouses, fulfillment centers and channels, with the lead time of every route between them."),
    ("Your rules, built in",
     "Which stores get stock first, where to fall back when a location runs low and how backorders count, set once and applied every day."),
    ("Context without limits",
     "Promotions, ad campaigns, purchase timing and anything your team knows go into the projection, so risks reflect how your business works."),
]

IF_PLANS = [
    ("Lite", "Your specialists keep lead times, safety stock and settings current, fill gaps in the data and flag the products at risk before they reach you."),
    ("Core", "Everything in Lite, plus the biggest risks walked through with your team in every weekly session and in your S&amp;OP meetings."),
    ("Full", "Everything in Core, with the purchases and transfers you approve followed through to suppliers, freight and your warehouses."),
]

IF_FEATURES = [
    ("Inventory projections", "Stock by product, channel and location from on-hand, inbound and forecast demand, with days of cover and warehouse needs."),
    ("Stockouts, overstock and lost sales", "Projected stockout dates, products below safety stock, excess inventory and the sales at stake."),
    ("Backorders and preorders", "Backorder demand counted in inventory and replenishment, with settings by product and store, and plans for preorders."),
    ("Inventory history and balances", "Snapshots and balances across every connected location, including inbound and in-transit stock."),
]

IF_FAQ = [
    ("Which locations does Flieber cover?",
     "Every location in your supply chain that Flieber can see: origin and regional warehouses, 3PLs, Amazon fulfillment centers and the channels they serve, connected through native or assisted integrations."),
    ("What happens when data is missing?",
     "Flieber flags it. Missing lead times or safety stock are filled by the rules you agree with your specialists, and anything that needs a decision is left for your review."),
    ("Can we test a change before acting on it?",
     "Yes. Add a purchase, delay a shipment or raise demand for a period, and see the effect on projected stock before anything is committed."),
    ("Does it handle backorders and preorders?",
     "Yes. Backorder demand counts in inventory and replenishment calculations, with settings by product and store, and products sold before they arrive have their own plans."),
]


def if_main() -> str:
    decisions = chips(["Replenishments", "Transfers", "Advertising", "Promotions", "Cash flow"])
    return f'''  <main id="main">
{hero("Product · Inventory forecasting", "See stockouts and overstock before they happen", "if-title",
      "Flieber projects stock for every product at every location, from your supplier to every channel, using on-hand inventory, inbound shipments and forecast demand. Risks show up while there is still time to act, and your team decides what to do.", True)}
{split("how-it-works", "How it works", "Every product, at every location", "products-title",
       "Each product gets its days of cover, its status and the next action, location by location. Inventory sits at the center of every decision, from what to buy to what to promote.",
       if_products_view(), soft=True, extra=decisions)}
{split("supply-chain", "Your supply chain", "Modeled from your supplier to every channel", "net-title",
       "Every route has its lead time, every location its on-hand stock and every product its safety stock, target, MOQ and case pack, so the projection follows how stock really moves.",
       if_network_view(), flip=True)}
{split("flags", "Flags", "Gaps found before they distort a plan", "flags-title",
       "A missing lead time or safety stock quietly breaks a projection. Flieber flags each gap, fills it by the rules agreed with your team and leaves the rest for your review.",
       if_flags_view(), soft=True)}
{split("scenarios", "Scenarios", "Test a change before you commit", "sc-title",
       "Add a purchase, delay a shipment or raise demand for a promotion, and see what happens to projected stock before any money goes out. Every change is logged with who made it and why.",
       if_scenario_view(), flip=True)}
{cards_section("tailored", "Tailored to your brand", "Built around how you operate", "tailor-title",
               "You don’t adapt to the software. Your inventory forecast follows your supply chain, your rules and everything your team knows.", IF_TAILOR, soft=True)}
{tail(IF_PLANS, IF_FEATURES, IF_FAQ, "See what inventory forecasting looks like for your brand")}
  </main>'''


# ---------- /product/replenishment ----------

def rp_order_view() -> str:
    vars_ = [("MOQs", "all met"), ("Cartons", "full cartons"), ("Container", "40' HC · 96% full"), ("Price breaks", "$4.50 tier reached"),
             ("Landed cost", "$47,750"), ("Cash out", "Dec 30% · Feb 70%"), ("Approvals", "Ops ✓ · Finance ✓")]
    rows = "".join(f'<div><small>{a}</small><b>{b}</b></div>' for a, b in vars_)
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Supplier 1 · Dec 2026</b><small>14 products · one purchase order</small><span class="df-ok" style="margin-left:auto">Ready to send</span></div>
              <div class="df-vars">{rows}</div>
            </div>'''


def rp_rules_view() -> str:
    rules = [("Supplier 1", "every 4 weeks · cover 120 days · full cartons · round up to MOQ if within 10%"),
             ("Supplier 2", "every 6 weeks · cover 90 days · full containers"),
             ("3PL US → FBA US", "weekly · by the pallet")]
    toasts = [("Draft ready", "Supplier 1 · Dec 2026 · 14 products", "Flieber"), ("Draft ready", "3PL US → FBA US · 5 pallets + 1 by air", "Slack"),
              ("Draft ready", "Supplier 2 · Jan 2027 · 1 container", "Email"), ("2 items need you", "Supplier 1 · Dec 2026", "Claude")]
    r = "".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in rules)
    t = "".join(f'<div class="df-toast"><span><b>{a}</b><small>{b}</small></span><em>{c}</em></div>' for a, b, c in toasts)
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Your buying rules</b><small>in your own words</small></div>
              <div class="df-rules">{r}</div>
              <div class="df-toasts">{t}</div>
            </div>'''


def rp_exceptions_view() -> str:
    alerts = [("Order by Dec 2, 2026", "in 3 days", ""),
              ("ALMN-CRON-LUGG below MOQ 500", "no rounding rule · round up: +$1,440, +32 days of cover", "Round up"),
              ("Container 78% full · 40' HC", "top up with 3 products → 96%", "Top up"),
              ("BLCK-CFEE-MAKR · +120 units", "reaches $4.50 · saves $1,140", "Add 120")]
    rows = "".join(f'<div><span><b>{a}</b><small>{b}</small></span>{f"<em class=\"df-btn y\">{c}</em>" if c else ""}</div>' for a, b, c in alerts)
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Supplier 1 · Dec 2026</b><small>drafted by rule · only the exceptions need you</small></div>
              <div class="df-alerts">{rows}</div>
            </div>'''


def rp_cash_view() -> str:
    cash = [("Dec", 14.6, 11.2), ("Jan", 38.2, 22.4), ("Feb", 61.4, 40.1), ("Mar", 22.0, 30.3), ("Apr", 18.5, 21.0)]
    w, h, top = 300, 120, 66
    bw = (w - 20) / len(cash)
    bars = ""
    for i, (m, a, b) in enumerate(cash):
        x0 = 10 + i * bw
        for j, v in enumerate((a, b)):
            y = h - 18 - v / top * (h - 30)
            bars += f'<rect class="{"df-c1" if j == 0 else "df-c2"}" x="{x0 + 8 + j * 18:.1f}" y="{y:.1f}" width="16" height="{h - 18 - y:.1f}" rx="2"/>'
        bars += f'<text x="{x0 + bw / 2:.1f}" y="{h - 4}" text-anchor="middle" class="df-t">{m}</text>'
    stages = "".join(f"<span{' class=\"on\"' if i < 4 else ''}>{s}</span>" for i, s in enumerate(["Draft", "In review", "Ops", "Finance", "Approved"]))
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Cash out by month</b><small>$ thousands · purchases planned vs budget</small></div>
              <svg viewBox="0 0 {w} {h}" fill="none" aria-hidden="true">{bars}<path d="M10 {h - 18} H{w - 10}" class="df-base"/></svg>
              <div class="df-legend"><span class="l-c1">Planned purchases</span><span class="l-c2">Budget</span></div>
              <div class="df-stg">{stages}</div>
            </div>'''


RP_TAILOR = [
    ("Buying rules in your words",
     "Buying cycles, coverage and rounding rules for each supplier and route, written the way your team already talks about them, and applied every cycle."),
    ("MOQs as they really work",
     "Minimums combined across products, case packs, cartons, pallets and containers, with price breaks and freight weighed before an order is drafted."),
    ("Your approval process",
     "Your own stages, from draft to operations and finance to approved, so every order follows the path your team already uses before money goes out."),
]

RP_PLANS = [
    ("Lite", "Your specialists keep lead times, MOQs, case packs and buying rules current, so every plan Flieber drafts starts from the right settings."),
    ("Core", "Everything in Lite, plus purchase and replenishment plans built with your team every week and approved plans turned into purchase-order files."),
    ("Full", "Everything in Core, with the orders you approve placed and followed with suppliers, forwarders and your warehouse until they arrive."),
]

RP_FEATURES = [
    ("Purchase and transfer recommendations", "What to order or transfer, how much and when, by product and location, including warehouse to FBA."),
    ("Planning parameters", "Safety stock, target days of cover, overstock thresholds, lead times and order frequency, by product, category or channel."),
    ("Order and shipping constraints", "MOQs and supplier constraints, container planning and rounding to case packs, cartons or pallets."),
    ("Decision simulations", "Test changes to quantities, demand, arrival dates or lead times and see the effect on stock, revenue, margin and cash."),
    ("Multi-month purchase planning", "A long buying horizon split into seasonally weighted orders, with cartons, MOQs and lead times applied."),
    ("AI order-quantity adjustments", "Quantities rebalanced across destinations and fitted to containers, budget and cash, following notes in plain language."),
    ("Saved plans and purchase orders", "Plans by supplier and date, with costs. Create and track purchase orders and group them under master orders."),
]

RP_FAQ = [
    ("Does Flieber send orders without us?",
     "No. Flieber drafts the plans and your team approves every order. On Full, your specialists place the orders you approve and follow them through."),
    ("Can it handle combined MOQs and containers?",
     "Yes. Minimums can be combined across products, and orders are fitted to case packs, cartons, pallets and container capacity, with price breaks and freight weighed in."),
    ("Can we plan within a cash budget?",
     "Yes. Purchases are planned against your cash by month, and quantities can be fitted to budget and cash-flow limits before anything is approved."),
    ("Does it plan transfers to Amazon too?",
     "Yes. Transfers from your warehouses or 3PLs to fulfillment locations such as FBA are planned by product and location, in the format you ship in."),
]


def rp_main() -> str:
    juggle = chips(["MOQs", "Cartons", "Containers", "Price breaks", "Freight", "Tariffs", "Cash", "Approvals"])
    return f'''  <main id="main">
{hero("Product · Replenishment", "Know what to buy, how much and when", "rp-title",
      "Flieber drafts purchase and transfer plans on every cycle, within your MOQs, cartons, containers, price breaks, lead times and cash. Your team reviews only the exceptions and approves every order.", True)}
{split("how-it-works", "How it works", "Every order weighs everything at once", "order-title",
       "One purchase order has to meet minimums, fill cartons and containers, reach price breaks, cover freight and tariffs, fit your cash and pass your approvals. Flieber weighs all of it before an order is drafted.",
       rp_order_view(), soft=True, extra=juggle)}
{split("rules", "Every cycle", "Plans drafted by your rules, on schedule", "rules-title",
       "Your buying rules are written in your own words, supplier by supplier and route by route. On every cycle, Flieber drafts the plans and lets you know in Flieber, Slack, email or Claude.",
       rp_rules_view(), flip=True)}
{split("exceptions", "Exceptions", "Your team reviews only what needs a decision", "exc-title",
       "Lines that follow your rules are ready. What doesn’t fit, a product below its MOQ, a container not yet full, a price break within reach, comes to your team with the option and its cost.",
       rp_exceptions_view(), soft=True)}
{split("cash", "Cash and approvals", "Every plan checked against your cash before money goes out", "cash-title",
       "Planned purchases are compared with your budget month by month, and each plan moves through your approval stages before an order is sent.",
       rp_cash_view(), flip=True)}
{cards_section("tailored", "Tailored to your brand", "Built around how you buy", "tailor-title",
               "You don’t adapt to the software. Your replenishment follows your suppliers, your constraints and your approval process.", RP_TAILOR, soft=True)}
{tail(RP_PLANS, RP_FEATURES, RP_FAQ, "See what replenishment looks like for your brand")}
  </main>'''


# ---------- /product/workflows ----------

WF_WHERE = [
    ("Orders sent to suppliers",
     "Approved purchase orders sent to each supplier in their own format, by email, file or Google Sheet, and pushed into NetSuite or other ERPs."),
    ("Inbound shipments created",
     "Approved transfers become inbound shipments in Amazon and in your 3PL and warehouse systems, then followed through delivery."),
    ("Alerts where your team works",
     "Scheduled checks for stockout risk, excess inventory and orders due, delivered by email, Slack, Microsoft Teams or Google Sheets."),
]


def wf_view() -> str:
    steps = [("Every Monday · 8 am", "Draft the transfers from 3PL US to FBA US"), ("Check", "Full pallets · ground unless a product runs out first"),
             ("Ask for approval", "Maya Chen, in Slack"), ("When approved", "Create the inbound shipment in Amazon"), ("Then", "Follow it to delivery and flag any delay")]
    rows = "".join(f'<div class="df-wf{" stop" if i == 2 else ""}"><small>{a}</small><b>{b}</b></div>' for i, (a, b) in enumerate(steps))
    return f'''<div class="df-view">
              <div class="df-view-h"><b>Weekly FBA transfers</b><small>a workflow described in plain language</small></div>
              <div class="df-wfs">{rows}</div>
            </div>'''


def wf_mcp_view() -> str:
    return '''<div class="df-view df-chat">
              <div class="df-view-h"><b>Flieber</b><small>connected to your other systems</small></div>
              <p class="df-u">BLCK-SPRT-JRSY will run out on FBA US before the next shipment lands. Pause its ad campaign until Dec 18?</p>
              <p class="df-a">Waiting for your approval. Once approved, the campaign is paused in your ads tool and resumes when stock is back.</p>
              <div class="df-act"><span>Nothing changes until your team approves</span><em class="df-btn">Not now</em><em class="df-btn y">Approve</em></div>
            </div>'''


WF_PLANS = [
    ("Lite", "Your specialists keep your workflows running as your systems change, and follow every failed sync or missed step until it’s fixed."),
    ("Core", "Everything in Lite, plus new workflows designed with your team every week, starting with the ones that save the most time."),
    ("Full", "Everything in Core, plus workflow automations for execution, from purchase orders and freight to logistics to your warehouse."),
]

WF_FEATURES = [
    ("Purchase orders to suppliers", "Each order sent into the supplier’s system or as an email, file or Google Sheet in their own format."),
    ("Purchase orders to ERPs", "Approved orders pushed into NetSuite, or into other ERPs through assisted integrations."),
    ("Inbound shipments in Amazon and 3PLs", "Inbound shipments created in Amazon and in connected 3PL and warehouse systems from an approved plan."),
    ("Inbound shipment tracking", "Orders and shipments followed through delivery, by manual entry, Google Sheets or automatic import."),
    ("Alerts and scheduled reports", "Checks for stockout risk, excess inventory and orders due, by email, Slack, Microsoft Teams or Google Sheets."),
    ("Custom workflows and agents", "Describe a recurring job in plain language and Flieber runs it on schedule, across its data and your apps."),
    ("Actions in other systems", "Flieber connects to systems with an MCP server, so it can act where a decision lands, with your approval."),
]

WF_FAQ = [
    ("What needs approval?",
     "You decide. Each workflow stops for approval wherever your team wants it to, and nothing it would change moves until someone approves."),
    ("Which systems can workflows reach?",
     "Your suppliers by email, file or Google Sheet, NetSuite, Amazon, your 3PL and warehouse systems, the tools your team uses for alerts, and any system with an MCP server."),
    ("Do we need to build the workflows ourselves?",
     "No. Describe the job in plain language. Your specialists help design the workflows that save your team the most time and keep them running as your systems change."),
]


def wf_main() -> str:
    where = "\n".join(card(t, b) for t, b in WF_WHERE)
    return f'''  <main id="main">
{hero("Product · Workflows", "From approved decision to done", "wf-title",
      "Once your team approves a decision, Flieber carries it into the systems where it lands: your suppliers, your ERP, Amazon, your 3PLs and the tools you already use. You decide how much runs on its own and where it stops for approval.", False,
      alt_href="#where", alt="See where decisions go")}

    <section class="section section-soft" id="where" aria-labelledby="where-title">
      <div class="wrap">
{head("Where decisions go", "Approved in Flieber, done where it lands", "where-title", "The work after a decision is where time goes: sending orders, creating shipments, chasing updates. Workflows take it on, on your terms.")}
        <div class="pv-3 pv-row pv-span2 reveal-stagger">
{where}
        </div>
      </div>
    </section>
{split("how-it-works", "In plain language", "Describe the job, set where it stops", "wf2-title",
       "Write a recurring job the way you would explain it to a colleague. Flieber runs it on schedule, across its own data and your connected apps, and stops for approval where you asked it to.",
       wf_view())}
{split("other-systems", "Other systems", "Act where the decision lands", "mcp-title",
       "Inventory shapes your ads, promotions and cash flow. Flieber connects to any system with an MCP server, so a stock risk can become a paused campaign or a supplier confirmation, always with your approval.",
       wf_mcp_view(), soft=True, flip=True)}
{tail(WF_PLANS, WF_FEATURES, WF_FAQ, "See which workflows would save your team the most time")}
  </main>'''


def main() -> None:
    write("pricing/index.html", "Pricing: one offer, three plans | Flieber",
          "One offer in three plans, Lite, Core and Full: a platform tailored to your brand and Flieber specialists who work with your team. Priced monthly by your size and plan.",
          pricing_main(), PRICING_FAQ, extra_banned=("$",))
    write("product/demand-forecasting/index.html", "Demand forecasting | Flieber",
          "Forecasts for every product on every channel, from corrected sales history, the best model for each product and the context your team adds. Your team approves every forecast.",
          df_main(), DF_FAQ)
    write("product/inventory-forecasting/index.html", "Inventory forecasting | Flieber",
          "Stock projected for every product at every location, from your supplier to every channel, so stockouts and overstock show up while there is still time to act.",
          if_main(), IF_FAQ)
    write("product/replenishment/index.html", "Replenishment | Flieber",
          "Purchase and transfer plans drafted on every cycle, within your MOQs, cartons, containers, price breaks, lead times and cash. Your team approves every order.",
          rp_main(), RP_FAQ)
    write("product/workflows/index.html", "Workflows | Flieber",
          "Approved decisions carried into your suppliers, your ERP, Amazon, your 3PLs and the tools you already use, with approval wherever your team wants it.",
          wf_main(), WF_FAQ)


if __name__ == "__main__":
    main()
