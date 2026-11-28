#!/usr/bin/env python3
"""Homepage V16: the positioning brief as written at Claude Doc revision 92 (Nov 28, 2026).

V15 (scripts/build-positioning-variant.py) is kept frozen with Claude's suggested changes; this page follows the brief verbatim.
Writes scripts/home-snapshots/2026-11-28-positioning-v16.html, which build-home-variants.py shows as V16.
Header, footer, styles and scripts come from scripts/home-option2-legacy.html (the Option 2 homepage) so the page keeps the site's design;
only the review bar, nav, main content, footer tagline and footer links change.
Placeholders (hero video, customer logos, Self-Serve page) are marked on the page, as the brief asks.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "scripts" / "home-snapshots" / "2026-11-28-positioning-v16.html"
BOOK = "https://www.flieber.com/book-a-demo"
SELF_SERVE = "pricing/#plan-ss"  # placeholder until the Self-Serve page exists (brief, open items)

ARROW = '<span class="arrow" aria-hidden="true">→</span>'
TAGLINE = "Flieber: combining AI and specialists to power your inventory decisions."
SHORT = "Flieber: where AI meets inventory experts."
# Monthly scorecard copy is an open item in the brief (section 10): shown with this marker so it is easy to drop.
PEND = '<span class="pv-pend" title="Open item in the brief: confirm before this goes live">Pending confirmation</span>'
MIT_URL = "https://www.aol.com/finance/mit-report-95-generative-ai-105412029.html"

CSS = ""  # the positioning components live in assets/css/site.css (moved Nov 28)


def card(title: str, body: str, extra: str = "", lead: str = "", side: str = "") -> str:
    if side:
        return f'''          <article class="pv-card">
            <div class="pv-card-h">{side}<h3>{title}</h3></div>
            <p>{body}</p>{extra}
          </article>'''
    return f'''          <article class="pv-card">{lead}
            <h3>{title}</h3>
            <p>{body}</p>{extra}
          </article>'''


GAP = [
    ("AI is changing how you plan",
     "Forecasts can now take in everything a business knows, not only its sales history. Routine work runs on its own, and every cycle feeds what was learned back in, so each plan is sharper than the last."),
    ("Few know how to get there",
     "AI is in every board meeting, conference and newsletter. Your team sees the potential, but between daily firefighting and the next purchase order, nobody has the time or the knowledge to bring it into how your business plans."),
    ("First movers will win",
     "While most brands are still working out where to start, the ones that take planning and operations to the next level first will move faster, react sooner and build an advantage that grows every cycle."),
]

ERA = [
    ("Data and context without limits",
     "Not just sales, inventory and purchase orders. Add marketing plans, cash flow, competitive information and the reasons behind past decisions. Flieber’s AI takes all of it into account in every forecast and plan, so your decisions reflect how your business really works, not just what your systems record."),
    ("Automations that get smarter",
     "Flieber specialists gather context from everyone involved in your business, from finance to marketing to operations, and bring what they’ve learned from more than 1,000 brands. They turn it into automations that take the routine off your team and improve with every cycle, so your people spend their time growing the brand, not running the process."),
    ("Intelligence that compounds",
     "Every exception resolved, every plan approved and every outcome observed feeds back in. Insights build on each other and alerts get sharper, so each cycle you plan with more confidence than the last, and what your team learns stays even when people change."),
]

STEPS = [
    ("We learn how you operate",
     "Our team connects your data and creates a routine of interactions with yours to continuously capture the context behind your numbers, from finance to marketing to operations. Within the first month, you already start seeing measurable value."),
    ("We tailor your platform",
     "You get your own version of Flieber, with your logo and colors, tailored to your use cases and how your team operates. Forecasting models are fine-tuned to your catalog, and new products and wholesale channels are handled by specialized tools. Views, alerts and workflows follow your preferences. When a new need comes up, it becomes part of your platform instead of a spreadsheet workaround or a long wait on the roadmap of a generic system."),
    ("We stay, and it keeps getting smarter",
     "Your Flieber specialists stay with your account, learning from the different people in your team. Each cycle, new opportunities are detected and more of the routine moves onto automations. Every plan is reviewed with your team before money goes out, and every month you get a scorecard on the measures that show your progress."),
]

MOMENTS = [
    ("A planner leaves or changes roles", "“The person who knew how all this works is gone.”",
     "What they knew is captured in your system, so the intelligence stays when people change."),
    ("A new channel, retailer or wholesale account", "“We just added Amazon, TikTok Shop, a big retailer.”",
     "We plan every channel from one picture, including wholesale and launches with no sales history."),
    ("A system dies or changes", "“Our planning tool shut down.” “We’re moving ERP or warehouse.”",
     "We set up around your new systems and keep planning running through the switch."),
    ("Fast growth", "“We’re aiming to double, and the way we plan won’t hold.”",
     "Planning scales with you: the routine runs on its own, and your team stays focused on the calls."),
    ("An inventory scare", "“We ran out of our bestseller.” “We’re sitting on months of stock.”",
     "Risks are flagged before they hit your shelves or your cash, and every plan is checked before money goes out."),
    ("A push to use AI", "“The board asked what we’re doing with AI.”",
     "A clear path into AI for your operation, with people who’ve done it for more than 1,000 brands."),
]

FAQ = [
    ("I already have a great team.",
     "Good, because Flieber works through them, not around them. Your team keeps every decision and every relationship with suppliers and partners. What changes is the work around those decisions: data checks, plan preparation and follow-ups move onto automations, new context reaches them every day, and they get specialists who have seen how more than 1,000 brands solve the same problems. Most teams are not short on talent; they are short on time."),
    ("Why not build this ourselves with AI?",
     "You can, and some brands try. The first version is usually exciting. The hard part comes after: every new use case, team change and data source adds upkeep, until maintaining the tool becomes someone’s full-time job. MIT found that partnering with specialists succeeds about three times as often as building in-house. With Flieber you start from what works across more than 1,000 brands, and the upkeep is ours."),
    ("What exactly do your specialists do?",
     "They create a routine of interactions with your team, which can go as far as joining your planning and S&amp;OP meetings if you want them there. Through it, they gather context from finance, marketing and operations and make sure your platform has it. They keep your data and setup right as your business changes, review plans with your team before money goes out, and find the opportunities for better data and automation in how you work. Behind your main contacts is a wider team with experience at the intersection of planning, operations and technology."),
    ("Do I lose control?",
     "No. Your team approves every plan and every order, and nothing moves without that approval. You also decide how much the specialists take on: some brands start with a second set of eyes on their plans, others hand over the whole planning preparation, and you can change that as trust builds."),
    ("Do your specialists leave after setup?",
     "No. Once your platform is set up, the specialists stay with your account. Their ongoing work is what makes the automations learn and the intelligence compound."),
    ("How do I know it’s working?",
     "Every month you get a scorecard on the measures you agree on with us at the start. You also see the work directly: plans reviewed, exceptions resolved and routine moved onto automations."),
    ("Why does it cost more than software?",
     "Because you’re not buying a tool your team then has to make work. You get three things software alone doesn’t give you. A platform tailored to your brand, with your products, channels, suppliers and rules built in. Specialists who keep it right as your business changes, review plans with your team and turn recurring work into automations. And what we’ve learned from more than 1,000 brands, so you start from what works instead of from scratch. Compare it with what the alternatives really cost: the time your team spends working around a generic tool, a new hire to run the process, or an in-house app someone has to maintain. Inventory shapes your advertising, promotions and cash flow, and one avoided stockout or overstock on a bestseller can pay for a year."),
    ("I just want software. I don’t want to pay for a team.",
     "We understand, and for years we sold Flieber that way. Here’s what we learned from more than 1,000 brands: software that has to fit everyone leaves gaps. Each brand used a small slice of it and filled the rest with spreadsheets and workarounds, so planning still depended on a few people’s heads. The specialists aren’t a team added on top of the software. They work with your team to make every planning cycle more streamlined and complete: they bring best practices from what works across other brands, act as a second set of eyes before money goes out, and find where better data or automation will help, building it into your platform as your business changes. They don’t replace your team or take your decisions. You decide how involved they get, from reviewing your plans to preparing the whole planning cycle for your team’s approval."),
    ("What happens in the first month?",
     "We get everything ready for you to plan on a solid foundation. Our team learns how you operate and gathers the context behind your numbers from the people involved, from finance to marketing to operations. We connect your data, map your products, channels and suppliers, and make the platform your own: views, alerts, workflows and forecasting set up around your use cases and preferences. Together we define the main gaps to close and the indicators we’ll follow. Within the first month, you already start seeing measurable value, and every cycle after that builds on it."),
]

INTEGRATIONS = ["Amazon", "Shopify", "Walmart", "NetSuite", "Flexport", "Google Sheets"]


def head(kicker: str, h2: str, hid: str, lead: str = "") -> str:
    lead_html = f'\n          <p class="lead">{lead}</p>' if lead else ""
    return f'''        <div class="section-head reveal">
          <span class="kicker">{kicker}</span>
          <h2 class="h2" id="{hid}" style="margin-top:20px">{h2}</h2>{lead_html}
        </div>'''


def live_part(start: str, end: str) -> str:
    src = (ROOT / "scripts/home-option2-legacy.html").read_text(encoding="utf-8")  # Option 2 homepage: chrome, logos, quotes
    s = src.index(start)
    return src[s:src.index(end, s) + len(end)]


RESULTS = [("↑", "38%", "more sales"), ("↓", "62%", "fewer stockouts"),
           ("↓", "17%", "less excess inventory"), ("↓", "88%", "less time on replenishment decisions")]

TEAM = [
    ("Former operators", "People who have planned and run operations at commerce brands themselves."),
    ("A senior AI team", "The engineers and data scientists behind your models and automations."),
    ("Process consultants", "Experience improving how planning teams work, not only what tools they use."),
]


GAP_ICONS = [
    '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/>',
    '<circle cx="12" cy="12" r="9"/><path d="M15.6 8.4l-2.1 5.1-5.1 2.1 2.1-5.1z"/>',
    '<path d="M6 21V4"/><path d="M6 4h12l-2.5 4.5L18 13H6"/>',
]


def icon(i: int) -> str:
    return (f'\n            <span class="pv-ico" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round">{GAP_ICONS[i]}</svg></span>')


ERA_VIZ = [
    # data and context: many streams converging into one plan
    """<svg viewBox="0 0 260 110" fill="none">
              <text x="6" y="17" class="pv-viz-t">sales</text><text x="6" y="43" class="pv-viz-t">marketing</text>
              <text x="6" y="69" class="pv-viz-t">cash</text><text x="6" y="95" class="pv-viz-t">past decisions</text>
              <path class="viz-draw" d="M104 14 C150 14 150 56 196 56"/><path class="viz-draw" d="M104 40 C150 40 150 56 196 56"/>
              <path class="viz-draw" d="M104 66 C150 66 150 56 196 56"/><path class="viz-draw" d="M104 92 C150 92 150 56 196 56"/>
              <path class="viz-draw pv-viz-y" d="M206 56 H252"/><circle cx="200" cy="56" r="9" class="pv-viz-dot"/>
            </svg>""",
    # automations: a loop that keeps turning
    """<svg viewBox="0 0 260 110" fill="none">
              <g class="pv-spin"><circle cx="130" cy="55" r="38" class="pv-viz-loop"/>
              <circle cx="130" cy="17" r="5" class="pv-viz-dot"/><circle cx="163" cy="74" r="5" class="pv-viz-dot2"/><circle cx="97" cy="74" r="5" class="pv-viz-dot2"/></g>
              <text x="130" y="59" text-anchor="middle" class="pv-viz-t">every cycle</text>
            </svg>""",
    # intelligence: a curve that compounds
    """<svg viewBox="0 0 260 110" fill="none">
              <path d="M10 100 H252" class="pv-viz-base"/>
              <path class="viz-draw pv-viz-y" d="M12 96 C70 94 110 86 150 66 S220 22 250 10"/>
              <circle cx="70" cy="92" r="3.5" class="pv-viz-dot2"/><circle cx="150" cy="66" r="3.5" class="pv-viz-dot2"/><circle cx="250" cy="10" r="5" class="pv-viz-dot"/>
            </svg>""",
]


DEMO_NOTE = "Illustration · Flieber Demo Account · fictional products and people"


def inv_chart() -> str:
    """Mini Inventory Forecast, same simulation as the videos: stock runs out, the approved plan adds a dashed on-order line."""
    n, dem, avg = 120, 30, 30
    def sim(inb):
        s, st = 1500, []
        for k in range(n):
            for d, q in inb:
                if k == d: s += q
            s = max(0, s - dem); st.append(s)
        return st
    if0, if1 = sim([]), sim([(58, 3000)])
    x = lambda k: 8 + k * 244 / (n - 1)
    y = lambda v: 100 - min(1, v / 3200) * 80
    path = lambda st, a, b: "M" + " L".join(f"{x(k):.1f} {y(v):.1f}" for k, v in enumerate(st) if a <= k <= b)
    band = f'<rect x="8" width="244" y="{y(50*avg):.1f}" height="{y(21*avg)-y(50*avg):.1f}" class="pv-iv-band"/>'
    lost = f'<rect x="{x(50):.1f}" width="{x(58)-x(50):.1f}" y="18" height="82" class="pv-iv-lost"/>'
    return f"""<svg viewBox="0 0 260 110" fill="none">{band}{lost}
              <path d="M8 100 H252" class="pv-viz-base"/>
              <path class="viz-draw pv-iv-ln" d="{path(if0, 0, 57)}"/>
              <path class="pv-iv-on" d="{path(if1, 57, n - 1)}"/>
              <path d="M{x(58)-6:.1f} 4 L{x(58)+6:.1f} 4 L{x(58):.1f} 13Z" class="pv-viz-dot"/>
              <text x="{x(61):.1f}" y="12" class="pv-viz-t">on order</text>
              <text x="250" y="{y(21*avg)-4:.1f}" text-anchor="end" class="pv-viz-t">safety</text>
              <text x="{x(49):.1f}" y="30" text-anchor="end" class="pv-viz-t pv-red">stockout</text>
            </svg>"""


TOASTS = [("Draft ready", "Supplier 1 · 14 products · $47,750", "Flieber"),
          ("Draft ready", "3PL US → FBA US · 5 pallets + 1 by air", "Slack"),
          ("2 items need you", "Supplier 1 · Dec 2026", "Claude")]


def toasts() -> str:
    rows = "".join(f'<div class="pv-toast"><span><b>{h}</b><small>{d}</small></span><em>{s}</em></div>' for h, d, s in TOASTS)
    return f'<div class="pv-toasts">{rows}</div>'


def viz(i: int) -> str:
    inner = ERA_VIZ[0] if i == 0 else toasts() if i == 1 else inv_chart()
    return f'\n            <div class="pv-viz" aria-hidden="true">{inner}</div>'


STEP_VIEWS = [
    """<div class="pv-sv pv-sv-learn"><div class="pv-sv-h">At setup · we learn how your company works</div>
              <div><b>Your team</b><span>How you plan · who approves what</span></div>
              <div><b>Your integrations</b><span>Amazon · Shopify · your ERP · your 3PL</span></div>
              <div><b>Your AI agents</b><span>Your rules · your notes · your history</span></div></div>""",
    """<div class="pv-sv pv-sv-rules"><div class="pv-sv-h">Your platform · fine-tuned to how you operate</div>
              <div><b>Supplier 1</b><span>every 4 weeks · cover 120 days · full cartons · round up to MOQ if within 10%</span></div>
              <div><b>Supplier 2</b><span>every 6 weeks · cover 90 days · full containers</span></div>
              <div><b>3PL US → FBA US</b><span>weekly · by the pallet</span></div>
              <p class="pv-sv-tags"><i>Rules in your own words</i><i>Combined MOQs</i><i>Launches</i><i>Wholesale</i><i>Your approval stages</i></p></div>""",
    """<div class="pv-sv pv-sv-stages"><div class="pv-stg"><span>Draft</span><span>In review</span><span>Ops</span><span>Finance</span><span>Approved</span></div>
              <div class="pv-sv-chip">Engine improved · your platform gets it too</div></div>""",
]


def row(cards: str, span: int) -> str:
    return f'''        <div class="pv-3 pv-row pv-span{span} reveal-stagger">
{cards}
        </div>'''


def main_html() -> str:
    gap = "\n".join(card(t, b, side=icon(i).strip()) for i, (t, b) in enumerate(GAP))
    era = "\n".join(card(t, b, lead=viz(i)) for i, (t, b) in enumerate(ERA))
    steps = "\n".join(card(t, b, side=f'<span class="pv-num" aria-hidden="true">{i}</span>').replace('<article class="pv-card">', f'<article class="pv-card">\n            <div class="pv-viz pv-viz-step" aria-hidden="true">{STEP_VIEWS[i-1]}</div>', 1) for i, (t, b) in enumerate(STEPS, 1))
    moments = "\n".join(f'''          <article class="pv-card pv-moment">
            <span class="pv-tag">{m}</span>
            <blockquote>{q}</blockquote>
            <p>{a}</p>
          </article>''' for m, q, a in MOMENTS)
    faq = "\n".join(f'''          <details>
            <summary>{q}<span class="plus" aria-hidden="true"></span></summary>
            <p>{a}</p>
          </details>''' for q, a in FAQ)
    logos = live_part('    <section class="logos-band"', "    </section>").replace(
        '<p class="logos-label" id="logos-label">Trusted by hundreds of brands</p>',
        '<p class="logos-label" id="logos-label">Brands that plan with Flieber</p>')
    results = "".join(f'<div class="pv-res-i"><span class="pv-res-n">{arrow}{n}</span><span class="pv-res-l">{l}</span></div>'
                      for arrow, n, l in RESULTS)
    quotes = live_part('        <div class="quotes reveal" id="quotes"', "            </div>\n          </div>\n        </div>")
    team = "".join(f'<div class="pv-team-i"><b>{n}</b><span>{d}</span></div>' for n, d in TEAM)
    buttons = f'''<a class="btn btn-primary" href="{BOOK}">Talk to a specialist {ARROW}</a>
              <a class="btn btn-ghost" href="{BOOK}">Book a demo</a>'''
    return f'''  <main id="main">

    <!-- Hero -->
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap">
        <div class="pv-hero-grid">
          <div>
            <h1 class="h1" id="hero-title">AI that powers decisions.<span class="pv-br"></span> Humans who shape it around your business</h1>
            <p class="lead">Planning is entering a new era: automations that learn, data and context without limits, intelligence that compounds. Flieber takes your inventory decisions there, with a platform tailored to your brand and specialists who’ve seen how more than 1,000 brands operate.</p>
            <div class="pv-actions">
              {buttons}
            </div>
          </div>
          <div class="pv-stage">
            <div class="pv-float pv-float-a" aria-hidden="true"><span class="pv-dot"></span><span><b>Draft ready</b><br>Supplier 1 · Dec 2026 · 14 products · $47,750</span></div>
          <figure class="pv-video" aria-label="Hero video placeholder">
            <span class="pv-play" aria-hidden="true"><svg width="22" height="24" viewBox="0 0 22 24"><path d="M2 2l18 10L2 22z" fill="#1B1C1C"/></svg></span>
            <p><span class="pv-ph">Placeholder</span><br><b>Hero video, about 60 to 75 seconds.</b> The shift, the gap, the bridge, smarter every cycle, then “{SHORT}” Plays with captions so it works with the sound off.</p>
          </figure>
            <div class="pv-float pv-float-b" aria-hidden="true"><span><b>ALMN-CRON-LUGG below MOQ 500</b><br>Round up: +$1,440, +32 days of cover</span><span class="pv-approve">Round up</span></div>
            <span class="pv-illus" aria-hidden="true">Illustration · Flieber Demo Account</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Customer logos, as on the live homepage -->
{logos}

    <!-- Why now? The gap -->
    <section class="section section-soft" id="why-now" aria-labelledby="gap-title">
      <div class="wrap">
{head("The gap", "Why now?", "gap-title")}
{row(gap, 2)}
      </div>
    </section>

    <!-- What changes? The new era of planning -->
    <section class="section on-dark pv-dark" id="what-changes" aria-labelledby="era-title">
      <div class="wrap">
{head("The new era of planning", "What changes?", "era-title")}
{row(era, 3)}
        <p class="pv-demo pv-demo-dark reveal">{DEMO_NOTE}</p>
      </div>
    </section>

    <!-- How do we get there? -->
    <section class="section section-soft" id="how-flieber-gets-you-there" aria-labelledby="how-title">
      <div class="wrap">
{head("How Flieber gets you there", "How do we get there?", "how-title")}
<div class="pv-steps-wrap">
{row(steps, 3)}
        </div>
        <p class="pv-demo reveal">{DEMO_NOTE}</p>
      </div>
    </section>

    <!-- Why not just buy or build software? -->
    <section class="section" id="why-not-software-alone" aria-labelledby="build-title">
      <div class="wrap">
        <div class="pv-build reveal">
          <div class="reveal">
            <span class="kicker">Why software alone isn’t enough anymore</span>
            <h2 class="h2" id="build-title" style="margin-top:20px">Why not just buy or build software?</h2>
          </div>
          <div class="reveal">
            <p class="lead">For years, software had to fit every customer the same way. Each brand used a small slice of it and filled the gaps with spreadsheets. AI changed that: a platform can now be tailored to each brand, and the value comes from shaping it around how you work. That takes people who know the work, which is why Flieber now comes with the specialists who shape it, and why we no longer sell the software on its own.</p>
            <p class="lead" style="margin-top:18px">Building it yourself is the other route, and it rarely holds: MIT’s study <i>The GenAI Divide: State of AI in Business 2025</i> found that partnering with specialists succeeds about three times as often as building in-house.</p>
            <div class="pv-bars" aria-hidden="true">
              <div class="pv-bar"><span class="pv-bar-l">Partnering with specialists</span><span class="pv-bar-t"><i style="--w:100%"></i></span><span class="pv-bar-v">about 67%</span></div>
              <div class="pv-bar"><span class="pv-bar-l">Building in-house</span><span class="pv-bar-t"><i style="--w:33%"></i></span><span class="pv-bar-v">about a third as often</span></div>
            </div>
            <p class="pv-cite">Source: MIT NANDA, <i>The GenAI Divide: State of AI in Business 2025</i>. Vendor and partnership routes succeeded about 67% of the time, and internal builds about a third as often (<a href="{MIT_URL}" rel="noopener" target="_blank">as reported by Fortune</a>). This is an outside study, not a Flieber result.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Is this for me? -->
    <section class="section section-soft" id="when-brands-bring-us-in" aria-labelledby="moments-title">
      <div class="wrap">
{head("When brands bring us in", "Is this for me?", "moments-title")}
        <div class="pv-moments pv-row pv-span3 reveal-stagger">
{moments}
        </div>
      </div>
    </section>

    <!-- Can I trust you? -->
    <section class="section" id="proof" aria-labelledby="proof-title">
      <div class="wrap">
{head("Proof", "Can I trust you?", "proof-title")}
        <div class="pv-proof reveal">
          <div class="pv-proof-l">
            <h3 class="pv-sub">Experience</h3>
            <div class="pv-exp"><span class="pv-res-n">1,000+</span><span class="pv-res-l">brands have used Flieber since 2019</span></div>
          </div>
          <div class="pv-proof-r">
            <h3 class="pv-sub">What brands see after 12 months or more</h3>
            <div class="pv-res">{results}</div>
          </div>
        </div>
        <p class="pv-cite pv-proof-note">Results are averages across customers using Flieber for 12 months or more. Not a guarantee for every brand.</p>
        <div class="pv-teamband reveal">
          <div>
            <h3 class="pv-sub" style="margin-top:0">The team behind your account</h3>
            <p class="pv-team-lead">Experience at the intersection of planning, operations and technology.</p>
          </div>
          <div class="pv-team">{team}</div>
        </div>
      </div>
    </section>

    <!-- Customer voices -->
    <section class="section pv-voices" id="customer-quotes" aria-label="What customers say">
      <div class="wrap">
{quotes}
      </div>
    </section>

    <!-- What else should I know? -->
    <section class="section section-soft" id="questions" aria-labelledby="questions-title">
      <div class="wrap">
{head("Questions", "What else should I know?", "questions-title")}
        <div class="faq">
{faq}
        </div>
      </div>
    </section>

    <!-- Final call to action -->
    <section class="section pv-final" id="talk-to-a-specialist" aria-labelledby="final-title">
      <div class="wrap">
        <h2 class="h2" id="final-title">See what your planning looks like in the new era</h2>
        <div class="pv-actions">
          {buttons}
        </div>
      </div>
    </section>
  </main>
'''


def rep(t: str, a: str, b: str) -> str:
    assert t.count(a) == 1, f"expected once: {a[:70]}"
    return t.replace(a, b)


def main() -> None:
    src = (ROOT / "scripts/home-option2-legacy.html").read_text(encoding="utf-8")  # Option 2 homepage: chrome, logos, quotes
    top = src[:src.index("  <main id=\"main\">")]
    bottom = src[src.index("  </main>") + len("  </main>\n"):]

    top = re.sub(r"<title>[^<]*</title>", f"<title>{TAGLINE[:-1]}</title>", top, count=1)
    top = re.sub(r'(<meta name="description" content=")[^"]*', r"\1" + TAGLINE + " Your team keeps every call.", top, count=1)
    top = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\1" + TAGLINE[:-1], top, count=1)
    top = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\1A planning platform tailored to your brand, with specialists who work with your team. Your team keeps every call.", top, count=1)
    top = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", top, count=1, flags=re.S)
    top = re.sub(r'<div class="review-bar"[^>]*>.*?</div>', '<div class="review-bar" role="note">Review build · <b>Positioning</b> · positioning rebuild · work in progress</div>', top, count=1, flags=re.S)
    # Nav and footer: the shared ones (scripts/site_chrome.py), so the homepage matches every other page.
    top = re.sub(r'  <header class="nav" id="nav">.*?</header>', lambda m: site_chrome.nav_html("", None), top, count=1, flags=re.S)
    bottom = re.sub(r'  <footer class="footer">.*?</footer>', lambda m: site_chrome.footer_html("", False), bottom, count=1, flags=re.S)

    page = top + main_html() + bottom
    for bad in ("Managed Services", "managed-services", "Lite", "Core,", "Full plan", "—", "Flieber Studio", "Flieber Inventory", "alongside", "run by Flieber", "Managed", "dashboard", "single source of truth", "visibility", "planning system", "Self-Serve", "Beyond inventory"):
        assert bad not in page, f"brief rule broken: {bad}"
    # The V16 snapshot (OUT) is frozen as Fabricio saw it on Nov 28; this branch only writes the homepage.
    (ROOT / "index.html").write_text(page, encoding="utf-8")
    print("wrote index.html")


if __name__ == "__main__":
    main()
