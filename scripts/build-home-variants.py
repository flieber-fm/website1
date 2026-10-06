#!/usr/bin/env python3
"""Homepage variants for side-by-side review (preview only, never indexed, not in the sitemap).

Each variant is the main index.html plus the agent-first follow-ons (hero card, doors, roles
section, How Flieber is built lead) and its own eyebrow, H1 and subhead. Output:
home-variants/index.html (the comparison hub) and home-variants/<n>/index.html.
Run after build-content.py, so the variants pick up every change to the main page.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "home-variants"

VARIANTS = [
    {"name": "Layer",
     "eyebrow": "Built for AI agents and the teams who run them",
     "h1": "The inventory layer your agents run on",
     "sub": ("Live data from every channel, the business context that connects it, a planning engine that does the math, "
             "and workflows that carry out what you approve, all under the rules you set. Connect Claude, ChatGPT or your "
             "own agents through MCP or API. Your team works from the same data layer, whether in the Flieber app, in Slack "
             "or with the help of our planners.")},
    {"name": "What agents know",
     "eyebrow": "Inventory intelligence for AI agents",
     "h1": "Your agents are only as good as what they know. Flieber is what they know about inventory",
     "sub": ("Flieber gives Claude, ChatGPT, your own agents and your automations live data from every channel, the context "
             "behind it and a planning engine that does the math. They forecast, plan purchases and move inventory within "
             "the approval rules you set, and your team works from the same source in the Flieber app, in Slack or with our planners.")},
    {"name": "The right purchase order",
     "eyebrow": "Works with Claude, ChatGPT and your own agents",
     "h1": "Your AI can write a purchase order. Flieber makes sure it’s the right one",
     "sub": ("Claude, ChatGPT, your vibe-coded apps and your automations are only as good as the data and context behind "
             "them. Flieber gives them, and your team, one live view of sales, inventory and supply chain across every "
             "channel, with the forecasts and recommendations to act on. Connect through MCP, API, Slack or the Flieber app.")},
    {"name": "Bring your own AI",
     "eyebrow": "Inventory AI for multichannel brands",
     "h1": "Bring your own AI. Flieber brings the inventory intelligence",
     "sub": ("Flieber’s AI forecasts every product on every channel, recommends what to buy and where to move it, and "
             "carries out what you approve. Your agents, automations and vibe-coded apps work from the same data and "
             "context through MCP and API, and your team works the same way in the Flieber app or in Slack.")},
    {"name": "Ask, automate, build",
     "eyebrow": "Inventory planning, built for how you work now",
     "h1": "Ask it. Automate it. Build on it",
     "sub": ("Ask Flieber anything about your inventory from Claude or Slack, turn the answer into an automation that runs "
             "every Monday, or vibe code your own dashboards and agents on top. Flieber does the data and the math "
             "underneath, so none of it breaks when your business changes.")},
    {"name": "Intelligence layer",
     "eyebrow": "Built for AI agents and the teams who run them",
     "h1": "The inventory intelligence layer your agents run on",
     "sub": ("Live data from every channel, the business context that connects it, a planning engine that does the math, "
             "and workflows that carry out what you approve, all under the rules you set. Connect Claude, ChatGPT or your "
             "own agents through MCP or API. Your team works from the same data layer, whether in the Flieber app, in Slack "
             "or with the help of our planners.")},
]

# Hero card: the six sample scenarios, shown as requests from agents and people.
# (The last field, a status line, is kept for reference but not shown: it cluttered the card.)
SCENES = [
    ("A wholesale buyer wants <b>1,800 units</b>.", "Claude",
     "A wholesale buyer wants <b>1,800 units</b> of the travel kit. Can we take the order?", "Split order ready for your ERP. Waiting for your approval."),
    ("Marketing wants <b>25% off</b> the travel kit next week.", "Slack · #marketing",
     "Can we run <b>25% off</b> the travel kit next week?", "Answer posted in the thread. Marketing makes the call."),
    ("An influencer post could <b>double demand</b> for a hero SKU.", "ChatGPT",
     "An influencer post could <b>double demand</b> for our hero SKU. When should it go live?", "Launch date goes into the forecast once you confirm."),
    ("A hero SKU will <b>sell out 3 weeks</b> before its next PO lands.", "Your agent · daily check",
     "Flagged: a hero SKU will <b>sell out 3 weeks</b> before its next PO lands.", "Recommendation sent to the ads team."),
    ("A supplier offers <b>8% off</b> for six months of stock.", "Claude",
     "A supplier offers <b>8% off</b> for six months of stock. Is it worth it?", "Three-month PO drafted. Waiting for your approval."),
    ("Ops wants to send <b>2,000 units</b> from the 3PL to Amazon FBA.", "Slack · scheduled",
     "Ops wants to send <b>2,000 units</b> from the 3PL to Amazon FBA. Should we?", "Transfer plan ready. Waiting for your approval."),
]

# Follow-ons shared by every variant, so the comparison isolates the hero copy.
SHARED = [
    ('<span class="sim-title" id="sim-title">Decision simulation</span>', '<span class="sim-title" id="sim-title">Agents at work on Flieber</span>'),
    ("<h2>Run it yourself</h2>", "<h2>Connect your agents, or use the app</h2>"),
    ("<p>Plan with Flieber’s AI in the Flieber app, or connect it to Claude, Slack, your agents and systems through MCP or API. Every way in works from the same data and context.</p>",
     "<p>Plug Claude, ChatGPT and your own agents into Flieber through MCP or API, or plan with Flieber’s AI in the app and in Slack. Every way in works from the same data and context.</p>"),
    ("<h2>Let our planners help you run it</h2>", "<h2>Add planners who work alongside your agents</h2>"),
    ("<p>Flieber’s planners join your team as a sounding board for every decision.", "<p>Flieber’s planners join your team as a sounding board for every decision, whether it comes from a person or an agent."),
    ('id="collab-title" style="margin-top:20px">AI that plans with your team, not instead of it</h2>', 'id="collab-title" style="margin-top:20px">Your team decides. Agents do the work around it</h2>'),
    ('<p class="lead">Inventory decisions commit cash for months. Flieber keeps people in charge of them and takes on everything around them.</p>',
     '<p class="lead">Inventory decisions commit cash for months. With Flieber, your team stays in charge of them, while Flieber’s AI and your own agents take on everything around them.</p>'),
    ('<span class="collab-step">Prepares and carries out</span>', '<span class="collab-step">Prepare and carry out</span>'),
    ('<h3 class="h3">Flieber’s AI</h3>\n            <p>Keeps your data consolidated and current, watches every SKU and every signal, prepares each decision with the reasoning behind it and carries it out once you approve.</p>',
     '<h3 class="h3">Flieber’s AI and your agents</h3>\n            <p>Keep your data consolidated and current, watch every SKU and every signal, prepare each decision with the reasoning behind it and carry it out once you approve. Your own agents work from the same data, context and engine through MCP and API.</p>'),
    ("act as a sounding board for your decisions and keep the data they rely on accurate.</p>", "act as a sounding board for your decisions and keep the data your team and your agents rely on accurate.</p>"),
    ('id="stack-title" style="margin-top:20px">From raw data to a decision you can trust</h2>', 'id="stack-title" style="margin-top:20px">What your agents run on</h2>'),
    ('<p class="lead">A language model on a spreadsheet can sound confident. Getting the answer right takes everything underneath it. Each layer adds something the one below it doesn’t have.</p>',
     '<p class="lead">An agent on a spreadsheet can sound confident and still get inventory wrong. It doesn’t know which listings are the same product, what’s inside a bundle or that last month’s dip was a stockout. Before running your brand with agents, someone has to keep the data true. Each layer adds something the one below it doesn’t have.</p>'),
    ("<p>The AI layer translates between your team and the engine.", "<p>The AI layer translates between the engine and whoever is asking, your team or your agents."),
]

BAR_CSS = """<style>
.vbar{position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:999;display:flex;flex-wrap:wrap;align-items:center;gap:6px;max-width:calc(100% - 24px);padding:8px 10px;border-radius:12px;background:#1B1C1C;color:#fff;font:500 13px/1.2 system-ui,sans-serif;box-shadow:0 8px 30px rgba(0,0,0,.25)}
.vbar b{font-weight:600;margin-right:4px}.vbar a{color:#fff;text-decoration:none;padding:5px 9px;border-radius:8px;border:1px solid rgba(255,255,255,.25)}
.vbar a[aria-current]{background:#F3EC65;color:#1B1C1C;border-color:#F3EC65}
@media print{.vbar{display:none}}
</style>"""


def rep(t: str, a: str, b: str) -> str:
    assert t.count(a) == 1, f"expected once: {a[:70]}"
    return t.replace(a, b)


def prefix_paths(t: str, up: str) -> str:
    return re.sub(r'(href|src)="(?!https?:|#|/|mailto:|tel:|data:)([^"]*)"', lambda m: f'{m.group(1)}="{up}{m.group(2)}"', t)


def bar(current: int, up: str) -> str:
    cur = ' aria-current="page"'
    links = [f'<a href="{up}"{cur if current == -1 else ""}>Main</a>']
    links += [f'<a href="{up}home-variants/{i}/"{cur if current == i else ""}>V{i}</a>' for i in range(1, len(VARIANTS) + 1)]
    return f'<nav class="vbar" aria-label="Homepage variants"><b>Compare</b>{"".join(links)}<a href="{up}home-variants/">All</a></nav>'


def variant(base: str, i: int, v: dict) -> str:
    t = base
    for a, b in SHARED:
        t = rep(t, a, b)
    for old_q, src, ask, status in SCENES:
        a = f'<p class="sim-q">{old_q}</p>'
        k = t.index(a)
        new = (f'<p class="sim-src"><span class="sim-src-dot" aria-hidden="true"></span>{src} <span class="sim-src-arrow" aria-hidden="true">→</span> Flieber</p>\n'
               f'                <p class="sim-q">“{ask}”</p>')
        t = t[:k] + new + t[k + len(a):]
    t = rep(t, '<figure class="sim" id="sim"', '<figure class="sim sim-compact" id="sim"')
    t = re.sub(r'(<span class="eyebrow"><span class="pulse" aria-hidden="true"></span><span>)[^<]*(</span>)', lambda m: m.group(1) + v["eyebrow"] + m.group(2), t, count=1)
    t = re.sub(r'(<h1 class="h1" id="hero-title">)[^<]*(</h1>)', lambda m: m.group(1) + v["h1"] + m.group(2), t, count=1)
    s = t.index('<p class="lead">', t.index('id="hero-title"'))
    t = t[:s] + f'<p class="lead">{v["sub"]}</p>' + t[t.index("</p>", s) + 4:]
    t = re.sub(r"<title>[^<]*</title>", f"<title>V{i} {html.escape(v['name'])}: {v['h1']} | Flieber</title>", t, count=1)
    t = re.sub(r'\s*<link rel="canonical"[^>]*>', "", t, count=1)
    up = "../../"
    t = prefix_paths(t, up)
    return t.replace("</head>", BAR_CSS + "\n</head>", 1).replace("</body>", bar(i, up) + "\n</body>", 1)


def hub(base: str) -> str:
    rows = "\n".join(f'''        <a class="vh-card" href="{i}/"><span class="vh-n">V{i} · {html.escape(v["name"])}</span>
          <span class="vh-eb">{html.escape(v["eyebrow"])} · MCP-native</span>
          <span class="vh-h1">{v["h1"]}</span><span class="vh-sub">{v["sub"]}</span></a>''' for i, v in enumerate(VARIANTS, 1))
    main_h1 = re.search(r'<h1 class="h1" id="hero-title">([^<]*)</h1>', base).group(1)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Homepage variants | Flieber preview</title>
<style>
:root{{--bg:#F7F7F5;--ink:#1B1C1C;--muted:#5E6262;--line:#DADBD6;--yellow:#F3EC65}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,-apple-system,sans-serif}}
main{{max-width:980px;margin:0 auto;padding:48px 16px 80px}} h1{{font-size:clamp(28px,4vw,40px);letter-spacing:-.03em;margin:0 0 8px;font-weight:500}}
p.lead{{color:var(--muted);margin:0 0 32px;max-width:680px}}
.vh-card{{display:block;background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 24px;margin-bottom:14px;color:inherit;text-decoration:none}}
.vh-card:hover{{border-color:var(--ink)}} .vh-card.main{{background:var(--yellow);border-color:var(--ink)}}
.vh-n{{display:block;font:600 12px/1.2 ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}}
.vh-eb{{display:block;margin-top:12px;font-size:13px;color:var(--muted)}}
.vh-h1{{display:block;margin-top:6px;font-size:clamp(22px,2.6vw,30px);line-height:1.15;letter-spacing:-.03em}}
.vh-sub{{display:block;margin-top:10px;color:var(--muted);font-size:15px}}
</style></head><body><main>
<h1>Homepage variants</h1>
<p class="lead">The main homepage and the agent-first variants. Every variant shares the same agent follow-ons (hero card, doors, roles section and the How Flieber is built lead), so the difference between them is the eyebrow, H1 and subhead. Each page has a compare bar at the bottom to jump between versions.</p>
        <a class="vh-card main" href="../"><span class="vh-n">Main · live preview today</span><span class="vh-h1">{main_h1}</span></a>
{rows}
</main></body></html>
'''


def main() -> None:
    base = (ROOT / "index.html").read_text(encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    (OUT / "index.html").write_text(hub(base), encoding="utf-8")
    for i, v in enumerate(VARIANTS, 1):
        d = OUT / str(i)
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(variant(base, i, v), encoding="utf-8")
    print(f"home-variants: hub + {len(VARIANTS)} variants")


if __name__ == "__main__":
    main()
