#!/usr/bin/env python3
"""Homepage built on the Nov 27, 2026 positioning brief (Flieber Positioning: Website & Video Brief).

Writes scripts/home-snapshots/2026-11-27-positioning.html, which build-home-variants.py shows as a variant.
Header, footer, styles and scripts come from the current index.html so the page keeps the site's design;
only the review bar, nav, main content, footer tagline and footer links change.
Placeholders (hero video, customer logos, Self-Serve page) are marked on the page, as the brief asks.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "scripts" / "home-snapshots" / "2026-11-27-positioning.html"
BOOK = "https://www.flieber.com/book-a-demo"
SELF_SERVE = "pricing/#plan-ss"  # placeholder until the Self-Serve page exists (brief, open items)

ARROW = '<span class="arrow" aria-hidden="true">→</span>'
TAGLINE = "Flieber: combining AI and specialists to power your inventory decisions."
SHORT = "Flieber: where AI meets inventory experts."
# Monthly scorecard copy is an open item in the brief (section 10): shown with this marker so it is easy to drop.
PEND = '<span class="pv-pend" title="Open item in the brief: confirm before this goes live">Pending confirmation</span>'
MIT_URL = "https://www.aol.com/finance/mit-report-95-generative-ai-105412029.html"

CSS = """<style>
/* Positioning variant (Nov 27 brief): page-scoped components */
.pv-hero-grid{display:grid;grid-template-columns:1fr;gap:clamp(28px,4vw,56px);align-items:center}
@media(min-width:980px){.pv-hero-grid{grid-template-columns:1.05fr 1fr}}
.pv-hero-grid .lead{max-width:560px;margin-top:22px}
.pv-actions{display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px;margin-top:28px}
.pv-alt{font-size:15px;color:var(--charcoal);text-decoration:underline;text-underline-offset:3px}
.pv-alt:hover{color:var(--black)}
.pv-video{margin:0;position:relative;aspect-ratio:16/9;border-radius:20px;background:var(--black);color:#fff;display:flex;flex-direction:column;justify-content:flex-end;padding:22px 24px;overflow:hidden}
.pv-video::before{content:"";position:absolute;inset:0;background:radial-gradient(120% 90% at 85% 10%,rgba(245,237,97,.28),transparent 60%)}
.pv-play{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:72px;height:72px;border-radius:50%;background:var(--yellow);display:grid;place-items:center}
.pv-play svg{margin-left:4px}
@media(max-width:600px){.pv-video{aspect-ratio:auto;min-height:300px;padding:18px}.pv-play{top:30%;width:56px;height:56px}}
.pv-video p{position:relative;margin:0;font-size:14px;line-height:1.45;color:rgba(255,255,255,.82)}
.pv-video b{color:#fff;font-weight:600}
.pv-ph{display:inline-block;margin-bottom:8px;padding:3px 8px;border:1px dashed rgba(255,255,255,.55);border-radius:6px;font:600 11px/1.2 ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--yellow)}
.pv-ph.dark{border-color:var(--gray-dark);color:var(--charcoal)}
.pv-3{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:820px){.pv-3{grid-template-columns:repeat(3,1fr)}}
.pv-2{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:820px){.pv-2{grid-template-columns:repeat(2,1fr)}}
.pv-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 26px 28px}
.section-soft .pv-card{background:#fff}
.pv-card h3{margin:0 0 10px;font-size:20px;line-height:1.25;letter-spacing:-.02em;font-weight:600}
.pv-card p{margin:0;color:var(--charcoal);font-size:16px;line-height:1.55}
.pv-num{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--yellow);font:600 15px/1 ui-monospace,monospace;margin-bottom:18px}
.pv-proof-pt{margin-top:16px!important;padding-top:14px;border-top:1px solid var(--line);font-size:14px!important;color:var(--black)!important}
.pv-proof-pt b{font-weight:600}
.pv-moments{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:700px){.pv-moments{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1040px){.pv-moments{grid-template-columns:repeat(3,1fr)}}
.pv-moment{display:flex;flex-direction:column;gap:14px}
.pv-moment .pv-tag{font:600 12px/1.2 ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--gray-dark)}
.pv-moment blockquote{margin:0;font-size:19px;line-height:1.35;letter-spacing:-.01em}
.pv-moment p{margin-top:auto!important;padding-top:14px;border-top:1px solid var(--line)}
.pv-beyond{max-width:860px;margin:0 auto;text-align:center;font-size:clamp(24px,3vw,34px);line-height:1.25;letter-spacing:-.025em}
.pv-stats{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:820px){.pv-stats{grid-template-columns:repeat(3,1fr)}}
.pv-stat{border-top:2px solid var(--black);padding-top:18px}
.pv-stat strong{display:block;font-size:clamp(34px,4vw,48px);line-height:1;letter-spacing:-.04em;font-weight:500}
.pv-stat span{display:block;margin-top:12px;color:var(--charcoal);font-size:15px;line-height:1.5}
.pv-integ{margin-top:36px;display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.pv-integ-l{font-size:14px;color:var(--gray-dark);margin-right:6px}
.pv-chip{padding:8px 14px;border:1px solid var(--line);border-radius:999px;background:#fff;font-size:15px}
.pv-logos{margin-top:28px;padding:18px 20px;border:1px dashed var(--gray-medium);border-radius:14px;color:var(--charcoal);font-size:14px}
.pv-ss{display:grid;grid-template-columns:1fr;gap:20px;align-items:center;background:var(--gray-light);border-radius:22px;padding:clamp(26px,4vw,44px)}
@media(min-width:820px){.pv-ss{grid-template-columns:1fr auto}}
.pv-ss h2{margin:0 0 8px}
.pv-ss p{margin:0;color:var(--charcoal);max-width:620px}
.pv-pend{display:inline-block;margin-left:6px;padding:1px 7px;border:1px dashed var(--gray-dark);border-radius:6px;font:600 10px/1.5 ui-monospace,monospace;letter-spacing:.05em;text-transform:uppercase;color:var(--charcoal);vertical-align:2px;white-space:nowrap}
.pv-build{display:grid;grid-template-columns:1fr;gap:clamp(24px,4vw,56px);align-items:start}
@media(min-width:900px){.pv-build{grid-template-columns:1fr 1fr}}
.pv-big{font-size:clamp(56px,7vw,88px);line-height:1;letter-spacing:-.05em;font-weight:500}
.pv-big-l{margin-top:12px;color:var(--charcoal);font-size:16px;line-height:1.5;max-width:420px}
.pv-build .lead{margin-top:0}
.pv-cite{margin-top:18px;font-size:13px;line-height:1.5;color:var(--gray-dark)}
.pv-cite a{color:inherit;text-decoration:underline;text-underline-offset:2px}
.pv-final{text-align:center}
.pv-final .h2{max-width:760px;margin:20px auto 0}
.pv-final .pv-actions{justify-content:center}
</style>"""


def card(title: str, body: str, extra: str = "", lead: str = "") -> str:
    return f'''          <article class="pv-card">{lead}
            <h3>{title}</h3>
            <p>{body}</p>{extra}
          </article>'''


PROBLEM = [
    ("Your team is buried in the work around decisions",
     "Gathering and fixing data, rebuilding spreadsheets, chasing suppliers. The decisions themselves get what time is left."),
    ("What your company knows is spread across many people",
     "Finance, marketing and operations each work from their own picture, and the context behind the numbers lives in people’s heads."),
    ("Nobody has time to work out what AI could take off their plate",
     "Everyone agrees AI should help. Nobody has the time to step back and decide where."),
]

STEPS = [
    ("We learn how you run",
     "We connect your data, join your planning meetings and capture the context behind your numbers. Setup takes about the first month, and we add value before it ends."),
    ("We tailor your system",
     "Your channels, suppliers, rules and views, in a planning system tailored to how you run."),
    ("We stay and keep improving",
     f"Your specialists stay after setup, your team approves every plan and every recurring task becomes an automation or an alert. Every month you get a scorecard on the measures we agree on together. {PEND}"),
]

PILLARS = [
    ("Built around how you run",
     "Each brand gets its own system, tailored to its channels, suppliers and way of planning. What it needs becomes part of its system, not a spreadsheet workaround or a wait for a roadmap.",
     "Your logo, your views, your use cases. Tailored, not one-size-fits-all."),
    ("A team that sees the whole picture",
     "What your company knows is spread across many people. Our team’s experience spans planning, operations and technology, so it connects what your team knows and spots what can be automated.",
     "Experience from more than 1,000 brands since 2019."),
    ("Better every month",
     f"Your specialists stay after setup. Every recurring task they handle is turned into an automation or an alert, and every month you get a scorecard on the measures you agreed on. {PEND} Context is captured once and kept, so it isn’t lost when people change.",
     "More of the work around each decision is automated every month."),
    ("Your decisions stay yours",
     "Your team approves every plan and every order. Our specialists work with your people, never over them.",
     "Nothing moves without your approval."),
]

MOMENTS = [
    ("A planner leaves or changes roles", "“The person who knew how all this works is gone.”",
     "What they knew gets built into your system, so it stays when people change."),
    ("A new channel, retailer or wholesale account", "“We just added Amazon, TikTok Shop, a big retailer.”",
     "We plan every channel from one picture, including wholesale and launches with no sales history."),
    ("A system dies or changes", "“Our planning tool shut down.” “We’re moving ERP or warehouse.”",
     "We set up around your new systems and keep planning running through the switch."),
    ("Fast growth", "“We’re aiming to double, and the spreadsheets won’t hold.”",
     "Planning keeps up with your growth, and your team stays focused on the decisions."),
    ("An inventory scare", "“We ran out of our bestseller.” “We’re sitting on months of stock.”",
     "A second set of eyes on every plan before money goes out."),
    ("A push to use AI", "“The board asked what we’re doing with AI.”",
     "A practical way to bring AI into operations, run by people who know this work."),
]

FAQ = [
    ("I already have a great team.",
     "Good: we work with them, not instead of them. We take the work they never get to and turn it into automations, so they spend their time on decisions."),
    ("Why not build this ourselves with AI?",
     "You can, but most in-house AI projects stall. Partnering with specialists succeeds about three times as often, and you get what we’ve learned from more than 1,000 brands from day one."),
    ("Do I lose control?", "No. Your team approves every plan and every order."),
    ("Do your specialists leave after setup?",
     "No. They stay with your account, and your system keeps getting better every month."),
    (f"How do I know it’s working? {PEND}",
     "Every month you get a scorecard on the measures we agree on together."),
    ("Why does it cost more than software?",
     "Because it’s more than software: a system tailored to your operation and specialists who work with your team. Inventory shapes your most important decisions, and one avoided stockout or overstock on a bestseller can pay for a year."),
    ("What happens in the first month?",
     "We connect your data, set up your system and learn how you plan. You see value before the month ends."),
    ("Can I just use the tool?",
     f'Yes. <a href="{SELF_SERVE}">Flieber Self-Serve</a> gives you the app, CLI and API.'),
]

INTEGRATIONS = ["Amazon", "Shopify", "Walmart", "NetSuite", "Flexport", "Google Sheets"]


def head(kicker: str, h2: str, hid: str, lead: str = "") -> str:
    lead_html = f'\n          <p class="lead">{lead}</p>' if lead else ""
    return f'''        <div class="section-head reveal">
          <span class="kicker">{kicker}</span>
          <h2 class="h2" id="{hid}" style="margin-top:20px">{h2}</h2>{lead_html}
        </div>'''


def main_html() -> str:
    problem = "\n".join(card(t, b) for t, b in PROBLEM)
    steps = "\n".join(card(t, b, lead=f'\n            <span class="pv-num" aria-hidden="true">{i}</span>') for i, (t, b) in enumerate(STEPS, 1))
    pillars = "\n".join(card(t, b, f'\n            <p class="pv-proof-pt"><b>Proof:</b> {p}</p>') for t, b, p in PILLARS)
    moments = "\n".join(f'''          <article class="pv-card pv-moment">
            <span class="pv-tag">{m}</span>
            <blockquote>{q}</blockquote>
            <p>{a}</p>
          </article>''' for m, q, a in MOMENTS)
    faq = "\n".join(f'''          <details>
            <summary>{q}<span class="plus" aria-hidden="true"></span></summary>
            <p>{a}</p>
          </details>''' for q, a in FAQ)
    chips = "".join(f'<span class="pv-chip">{n}</span>' for n in INTEGRATIONS)
    return f'''  <main id="main">

    <!-- 1. Hero -->
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap">
        <div class="pv-hero-grid">
          <div>
            <h1 class="h1" id="hero-title">If your team is buried in spreadsheets, who’s planning what’s next?</h1>
            <p class="lead">Flieber combines AI and specialists to power your inventory decisions. Your team keeps every call.</p>
            <div class="pv-actions">
              <a class="btn btn-primary" href="{BOOK}">Book a review of your operation {ARROW}</a>
              <a class="pv-alt" href="{SELF_SERVE}">Prefer to run it yourself? See Flieber Self-Serve</a>
            </div>
          </div>
          <figure class="pv-video" aria-label="Hero video placeholder">
            <span class="pv-play" aria-hidden="true"><svg width="22" height="24" viewBox="0 0 22 24"><path d="M2 2l18 10L2 22z" fill="#1B1C1C"/></svg></span>
            <p><span class="pv-ph">Placeholder</span><br><b>Hero video, about 60 to 75 seconds.</b> The problem, the gap, the answer, better every month, then “{SHORT}” Plays with captions so it works with the sound off.</p>
          </figure>
        </div>
      </div>
    </section>

    <!-- 2. The problem -->
    <section class="section section-soft" id="the-problem" aria-labelledby="problem-title">
      <div class="wrap">
{head("The problem", "Your team makes the decisions that move your business. Most of their time goes elsewhere", "problem-title")}
        <div class="pv-3 reveal-stagger">
{problem}
        </div>
      </div>
    </section>

    <!-- 3. How it works -->
    <section class="section" id="how-it-works" aria-labelledby="how-title">
      <div class="wrap">
{head("How it works", "A planning system tailored to how you run, with specialists who work with your team", "how-title")}
        <div class="pv-3 reveal-stagger">
{steps}
        </div>
      </div>
    </section>

    <!-- 4. Pillars -->
    <section class="section section-soft" id="why-it-works" aria-labelledby="pillars-title">
      <div class="wrap">
{head("Why it works", "AI in your operation, without rebuilding your team", "pillars-title")}
        <div class="pv-2 reveal-stagger">
{pillars}
        </div>
      </div>
    </section>

    <!-- 5. When brands bring us in -->
    <section class="section" id="when-brands-bring-us-in" aria-labelledby="moments-title">
      <div class="wrap">
{head("When brands bring us in", "Something changes, and the current setup stops being enough", "moments-title", "Brands rarely bring us in during a quiet month. These are the moments we hear about most.")}
        <div class="pv-moments reveal-stagger">
{moments}
        </div>
      </div>
    </section>

    <!-- 6. Why not build it yourself -->
    <section class="section section-soft" id="why-not-build-it-yourself" aria-labelledby="build-title">
      <div class="wrap">
        <div class="pv-build">
          <div class="reveal">
            <span class="kicker">Build or partner</span>
            <h2 class="h2" id="build-title" style="margin-top:20px">Why not build it yourself?</h2>
          </div>
          <div class="reveal">
            <p class="lead">Brands that partner on AI succeed about three times as often as those that build it alone, according to MIT’s 2025 study of enterprise AI. We bring the platform, the specialists and what we’ve learned from more than 1,000 brands, so you don’t start from zero.</p>
            <p class="pv-cite">Source: MIT NANDA, <i>The GenAI Divide: State of AI in Business 2025</i>. Vendor and partnership routes succeeded about 67% of the time, and internal builds about a third as often (<a href="{MIT_URL}" rel="noopener" target="_blank">as reported by Fortune</a>). This is an outside study, not a Flieber result.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. Beyond inventory -->
    <section class="section" id="beyond-inventory" aria-label="Beyond inventory">
      <div class="wrap">
        <p class="pv-beyond reveal">Inventory shapes your advertising, promotions and cash flow, so planning connects finance, marketing and operations.</p>
      </div>
    </section>

    <!-- 8. Proof -->
    <section class="section section-soft" id="proof" aria-labelledby="proof-title">
      <div class="wrap">
{head("Proof", "Experience your team can lean on", "proof-title")}
        <div class="pv-stats reveal-stagger">
          <div class="pv-stat"><strong>1,000+</strong><span>More than 1,000 brands have used Flieber since 2019.</span></div>
          <div class="pv-stat"><strong>100+</strong><span>Brands planning with Flieber today.</span></div>
          <div class="pv-stat"><strong>36%</strong><span>More accurate, verified by Nixtla against 16 statistical and machine-learning models on 46,000 products.</span></div>
        </div>
        <div class="pv-integ reveal"><span class="pv-integ-l">Native integrations</span>{chips}<span class="pv-integ-l">Other sources connect through Google Sheets or custom scripts.</span></div>
        <div class="pv-logos reveal"><span class="pv-ph dark">Placeholder</span> Customer logos, quotes and results appear here once each customer approves them in writing.</div>
      </div>
    </section>

    <!-- 9. Self-Serve -->
    <section class="section" id="self-serve" aria-labelledby="ss-title">
      <div class="wrap">
        <div class="pv-ss reveal">
          <div>
            <h2 class="h3" id="ss-title">Flieber Self-Serve</h2>
            <p>Want to run Flieber yourself, or build your own tools on our data? Use the app, CLI and API directly.</p>
          </div>
          <a class="btn btn-ghost" href="{SELF_SERVE}">See Flieber Self-Serve {ARROW}</a>
        </div>
      </div>
    </section>

    <!-- 10. FAQ -->
    <section class="section section-soft" id="questions" aria-labelledby="questions-title">
      <div class="wrap">
{head("Questions", "What brands ask before they bring us in", "questions-title")}
        <div class="faq">
{faq}
        </div>
      </div>
    </section>

    <!-- 11. Final call to action -->
    <section class="section pv-final" id="book-a-review" aria-labelledby="final-title">
      <div class="wrap">
        <span class="kicker">Next step</span>
        <h2 class="h2" id="final-title">See what your operation looks like with Flieber</h2>
        <div class="pv-actions">
          <a class="btn btn-primary" href="{BOOK}">Book a review {ARROW}</a>
        </div>
      </div>
    </section>
  </main>
'''


def rep(t: str, a: str, b: str) -> str:
    assert t.count(a) == 1, f"expected once: {a[:70]}"
    return t.replace(a, b)


def main() -> None:
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    top = src[:src.index("  <main id=\"main\">")]
    bottom = src[src.index("  </main>") + len("  </main>\n"):]

    top = re.sub(r"<title>[^<]*</title>", f"<title>{TAGLINE[:-1]}</title>", top, count=1)
    top = re.sub(r'(<meta name="description" content=")[^"]*', r"\1" + TAGLINE + " Your team keeps every call.", top, count=1)
    top = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\1" + TAGLINE[:-1], top, count=1)
    top = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\1A planning system tailored to how you run, with specialists who work with your team. Your team keeps every call.", top, count=1)
    top = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", top, count=1, flags=re.S)
    top = re.sub(r'<div class="review-bar"[^>]*>.*?</div>', '<div class="review-bar" role="note">Review build · <b>Positioning</b> · Nov&nbsp;27 brief (revised), proposal</div>', top, count=1, flags=re.S)
    top = top.replace("</head>", CSS + "\n</head>", 1)
    # Nav: one product, the team inside the copy, Self-Serve as the secondary path.
    nav = re.search(r'<nav class="nav-links" aria-label="Primary">.*?</nav>', top, flags=re.S).group(0)
    top = top.replace(nav, f'''<nav class="nav-links" aria-label="Primary">
        <a href="#how-it-works">How it works</a>
        <a href="#when-brands-bring-us-in">When brands bring us in</a>
        <a href="who-we-are/">Who we are</a>
        <a href="{SELF_SERVE}">Self-Serve</a>
        <a class="menu-only" href="https://app.flieber.com">Log in</a>
        <a class="menu-only" href="{BOOK}">Book a review</a>
      </nav>''')
    cta = re.search(r'<div class="nav-cta">.*?<button class="nav-toggle"', top, flags=re.S).group(0)
    top = top.replace(cta, f'''<div class="nav-cta">
        <a class="nav-login" href="https://app.flieber.com">Log in</a>
        <a class="btn btn-primary btn-sm" href="{BOOK}">Book a review</a>
        <button class="nav-toggle"''')

    bottom = rep(bottom, '<p class="tagline">The inventory intelligence layer <em>your agents run on.</em></p>',
                 '<p class="tagline">Flieber: where AI meets <em>inventory experts.</em></p>')
    bottom = rep(bottom, '            <li><a href="managed-services/">Managed Services</a></li>\n', f'            <li><a href="{SELF_SERVE}">Flieber Self-Serve</a></li>\n')

    page = top + main_html() + bottom
    for bad in ("Managed Services", "managed-services", "Lite", "Core,", "Full plan", "—", "Flieber Studio", "Flieber Inventory", "alongside", "run by Flieber", "Managed"):
        assert bad not in page, f"brief rule broken: {bad}"
    OUT.write_text(page, encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
