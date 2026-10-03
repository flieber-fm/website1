#!/usr/bin/env python3
"""Generate /features, the five /product module pages, /multichannel, /agencies, the /agents body, llms.txt, llms-full.txt and
capabilities.json, then write the shared nav and footer into every page (scripts/site_chrome.py).

All of them come from scripts/site_content.py so they can never contradict each other.
The /features page reuses the header and footer of /pricing; /agents keeps its own
head, header and footer and only its <main> is regenerated.

    python3 scripts/build-content.py
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import site_content as C  # noqa: E402
import site_chrome  # noqa: E402

ACCESS_LABEL = {"read": "Read", "write": "Write", "read_write": "Read and write", None: None}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def esc(text: str) -> str:
    """HTML-escape, then use typographic apostrophes like the rest of the site."""
    return html.escape(text, quote=False).replace("'", "’")


def md_bold(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


MODULE_BY_SLUG = {m["slug"]: m for m in C.MODULES}


# ------------------------------------------------------------------ /features
def features_main() -> str:
    jump = [(g["id"], g["label"]) for g in C.GROUPS] + [("control-and-approval", "Approval"), ("examples", "Examples"), ("questions", "Questions")]
    out = []
    out.append(f'''
    <section class="page-head feat-head" aria-labelledby="features-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Features</span>
          <h1 class="h1" id="features-title">{esc(C.FEATURES_H1)}</h1>
          <p class="lead">{esc(C.FEATURES_INTRO)}</p>
          <p class="feat-note">{esc(C.FEATURES_NOTE)}</p>
        </div>
      </div>
    </section>

    <nav class="feat-jump" aria-label="On this page">
      <div class="wrap">
        {"".join(f'<a href="#{i}">{esc(l)}</a>' for i, l in jump)}
      </div>
    </nav>
''')
    for n, g in enumerate(C.GROUPS):
        soft = " section-soft" if n % 2 == 0 else ""
        mod = MODULE_BY_SLUG.get(g["id"])
        lead = mod["tab"] if mod else g["lead"]
        more = (f'\n        <p class="link-row"><a class="link-arrow" href="../product/{mod["slug"]}/">{esc(mod["name"])} <span class="arrow" aria-hidden="true">→</span></a></p>'
                if mod else "")
        cards = []
        for title, desc, access, avail in g["features"]:
            tags = []
            if ACCESS_LABEL[access]:
                tags.append(ACCESS_LABEL[access])
            if avail == "on_request":
                tags.append("On request")
            tag_html = f'\n              <p class="feat-tag">{" · ".join(tags)}</p>' if tags else ""
            ucs = [u for u in C.USE_CASES if slug(title) in u["features"]]
            uc_html = "".join(f'\n              <p class="feat-uc"><a href="../use-cases/{u["slug"]}/">Use case: {esc(u["name"])} {ARROW}</a></p>' for u in ucs)
            cards.append(f'''            <article class="feat-card" id="{slug(title)}">
              <h3 class="h3">{esc(title)}</h3>
              <p>{esc(desc)}</p>{tag_html}{uc_html}
            </article>''')
        out.append(f'''
    <section class="section{soft} feat-group" id="{g["id"]}" aria-labelledby="{g["id"]}-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">{esc(g["label"])}</span>
          <h2 class="h2" id="{g["id"]}-title" style="margin-top:20px">{esc(g["h2"])}</h2>
          <p class="lead">{esc(lead)}</p>
        </div>
        <div class="feat-grid">
{chr(10).join(cards)}
        </div>{more}
      </div>
    </section>
''')
    examples = "\n".join(f'          <li><span class="feat-q">“{esc(e)}”</span></li>' for e in C.EXAMPLES)
    faq = "\n".join(f'''          <div class="feat-faq-item">
            <h3 class="h3" id="{slug(q)}">{esc(q)}</h3>
            <p>{esc(a)}</p>
          </div>''' for q, a in C.FAQ)
    notfor = "\n".join(f'''            <li><span class="ico" aria-hidden="true"><svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M2 2l6 6M8 2L2 8" stroke="#757F82" stroke-width="1.5"/></svg></span>{esc(x)}</li>''' for x in C.NOT_FOR)
    out.append(f'''
    <section class="section" id="control-and-approval" aria-labelledby="approval-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Approval</span>
          <h2 class="h2" id="approval-title" style="margin-top:20px">{esc(C.APPROVAL_H2)}</h2>
        </div>
        <p class="feat-approval">{esc(C.APPROVAL_BODY)}</p>
      </div>
    </section>

    <section class="section section-soft" id="examples" aria-labelledby="examples-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Examples</span>
          <h2 class="h2" id="examples-title" style="margin-top:20px">{esc(C.EXAMPLES_H2)}</h2>
          <p class="lead">{esc(C.EXAMPLES_LEAD)}</p>
        </div>
        <ol class="feat-examples">
{examples}
        </ol>
        <p class="feat-note">{esc(C.EXAMPLES_NOTE)}</p>
      </div>
    </section>

    <section class="section" id="questions" aria-labelledby="questions-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Questions</span>
          <h2 class="h2" id="questions-title" style="margin-top:20px">{esc(C.FAQ_H2)}</h2>
        </div>
        <div class="feat-faq">
{faq}
        </div>
        <div class="fit-col fit-no feat-notfor">
          <h2 class="h3" id="not-built-for">Probably not for you if</h2>
          <ul>
{notfor}
          </ul>
        </div>
      </div>
    </section>

    <section class="section try" id="next" aria-labelledby="next-title">
      <div class="wrap" style="position:relative">
        <div class="section-head">
          <span class="kicker">Next step</span>
          <h2 class="h2" id="next-title" style="margin-top:20px">{esc(C.NEXT_H2)}</h2>
          <p class="lead">{esc(C.NEXT_BODY)}</p>
        </div>
        <div class="try-actions">
          <a class="btn btn-primary" href="{C.TRIAL}">Start free trial <span class="arrow" aria-hidden="true">→</span></a>
          <a class="btn btn-ghost" href="{C.DEMO}">Book a demo</a>
        </div>
      </div>
    </section>
''')
    return "".join(out)


def features_jsonld() -> str:
    feature_list = [t for g in C.GROUPS for t, *_ in g["features"]]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": "https://www.flieber.com/#organization", "name": "Flieber",
             "url": "https://www.flieber.com", "logo": "https://www.flieber.com/assets/img/flieber-logo.svg",
             "foundingDate": "2019",
             "address": {"@type": "PostalAddress", "streetAddress": "169 Madison Avenue", "addressLocality": "New York",
                         "addressRegion": "NY", "postalCode": "10016", "addressCountry": "US"}},
            {"@type": "SoftwareApplication", "name": "Flieber", "applicationCategory": "BusinessApplication",
             "operatingSystem": "Web", "url": "https://www.flieber.com/features",
             "publisher": {"@id": "https://www.flieber.com/#organization"}, "featureList": feature_list},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in C.FAQ]},
        ],
    }
    return '<script type="application/ld+json">\n' + json.dumps(graph, indent=2, ensure_ascii=False) + "\n  </script>"


def build_features() -> None:
    src = (ROOT / "pricing/index.html").read_text(encoding="utf-8")
    top = src[: src.index('<main id="main">') + len('<main id="main">')]
    bottom = src[src.index("  </main>"):]
    top = top.replace('<a href="/pricing" aria-current="page">Pricing</a>', '<a href="/pricing">Pricing</a>')
    bottom = bottom.replace('<a href="/pricing" aria-current="page">Pricing</a>', '<a href="/pricing">Pricing</a>')
    top = top.replace('<a href="../features/">How it works</a>', '<a href="../features/" aria-current="page">How it works</a>')
    bottom = bottom.replace('<a href="../features/">How it works</a>', '<a href="../features/" aria-current="page">How it works</a>')
    title = "Features: collaborative AI for every inventory decision"
    desc = ("Every Flieber feature: a current picture of how your business works, your next move recommended and "
            "carried out with your team, agents and systems. Forecasts, purchase orders, inbound shipments, MCP and API.")
    top = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", top)
    top = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', top)
    top = top.replace('https://www.flieber.com/pricing"', 'https://www.flieber.com/features"')
    top = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', top)
    top = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', top)
    top = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: features_jsonld(), top, flags=re.S)
    out = ROOT / "features/index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(top + "\n" + features_main() + "\n" + bottom, encoding="utf-8")


# ------------------------------------------------------------------ /product module pages, /multichannel, /agencies
FEATURES_BY_TITLE = {t: (g, d, a, av) for g in C.GROUPS for t, d, a, av in g["features"]}
ICON_TEAM = '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true"><circle cx="5.5" cy="5.5" r="2.2"/><circle cx="11" cy="6" r="1.8"/><path d="M1.6 13.5c.5-2.3 2-3.6 3.9-3.6s3.4 1.3 3.9 3.6M10 9.6c1.9 0 3.3 1.2 3.8 3.4"/></svg>'
ICON_AI = '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true"><path d="M8 1.8l1.5 3.7 3.7 1.5-3.7 1.5L8 12.2 6.5 8.5 2.8 7l3.7-1.5z"/><path d="M12.6 11.2l.6 1.5 1.5.6-1.5.6-.6 1.5-.6-1.5-1.5-.6 1.5-.6z"/></svg>'
ICON_PLANNER = '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true"><circle cx="8" cy="5" r="2.6"/><path d="M2.8 14c.6-2.7 2.7-4.3 5.2-4.3s4.6 1.6 5.2 4.3"/></svg>'
ARROW = '<span class="arrow" aria-hidden="true">→</span>'


def collab_cards(x) -> str:
    """Three-party collaboration cards (your team, Flieber's AI, Flieber's planners)."""
    cols = [("Your team", ICON_TEAM, x["team"], None, ""), ("Flieber’s AI", ICON_AI, x["ai"], None, ""),
            ("Flieber’s planners", ICON_PLANNER, x["planners"], "With Managed Services", "")]
    out = []
    for name, icon, body, tag, cls in cols:
        tag_html = f'<span class="collab-tag">{esc(tag)}</span>' if tag else ""
        out.append(f'''          <article class="collab-card{cls}">
            <div class="collab-top"><span class="collab-ic">{icon}</span>{tag_html}</div>
            <h3 class="h3">{name}</h3>
            <p>{esc(body)}</p>
          </article>''')
    return '        <div class="collab">\n' + "\n".join(out) + "\n        </div>"


def feature_cards(titles, p: str) -> str:
    cards = []
    for f in titles:
        g, d, a, av = FEATURES_BY_TITLE[f]
        tags = [ACCESS_LABEL[a]] if ACCESS_LABEL[a] else []
        if av == "on_request":
            tags.append("On request")
        tag_html = f'\n              <p class="feat-tag">{" · ".join(tags)}</p>' if tags else ""
        cards.append(f'''            <a class="feat-card sol-feat" href="{p}features/#{slug(f)}">
              <h3 class="h3">{esc(f)} {ARROW}</h3>
              <p>{esc(d)}</p>{tag_html}
            </a>''')
    return "\n".join(cards)


def section(sid: str, kicker: str, h2: str, body: str, soft: bool, lead: str = "") -> str:
    lead_html = f'\n          <p class="lead">{esc(lead)}</p>' if lead else ""
    return f'''
    <section class="section{" section-soft" if soft else ""}" id="{sid}" aria-labelledby="{sid}-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">{esc(kicker)}</span>
          <h2 class="h2" id="{sid}-title" style="margin-top:20px">{esc(h2)}</h2>{lead_html}
        </div>
{body}
      </div>
    </section>
'''


def page_head(kicker: str, h1: str, lead: str, demo_first: bool = False) -> str:
    if demo_first:
        btns = (f'<a class="btn btn-primary" href="{C.DEMO}">Book a demo {ARROW}</a>\n          '
                f'<a class="btn btn-ghost" href="{C.TRIAL}">Start free trial</a>')
    else:
        btns = (f'<a class="btn btn-primary" href="{C.TRIAL}">Start free trial {ARROW}</a>\n          '
                f'<a class="btn btn-ghost" href="{C.DEMO}">Book a demo</a>')
    return f'''
    <section class="page-head sol-head" aria-labelledby="page-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">{esc(kicker)}</span>
          <h1 class="h1" id="page-title">{esc(h1)}</h1>
          <p class="lead">{esc(lead)}</p>
        </div>
        <div class="sol-actions">
          {btns}
        </div>
      </div>
    </section>
'''


def closing(extra: str = "", h2: str = None, body: str = None, demo_first: bool = False) -> str:
    trial = f'<a class="btn btn-{{}}" href="{C.TRIAL}">Start free trial{{}}</a>'
    demo = f'<a class="btn btn-{{}}" href="{C.DEMO}">Book a demo{{}}</a>'
    if demo_first:
        buttons = demo.format("primary", " " + ARROW) + "\n          " + trial.format("ghost", "")
    else:
        buttons = trial.format("primary", " " + ARROW) + "\n          " + demo.format("ghost", "")
    h2 = C.CLOSE_H2 if h2 is None else h2
    body = C.CLOSE_BODY if body is None else body
    head = ""
    if h2:
        head = f'''
        <div class="section-head">
          <span class="kicker">Next step</span>
          <h2 class="h2" id="next-title" style="margin-top:20px">{esc(h2)}</h2>{f"""
          <p class="lead">{esc(body)}</p>""" if body else ""}
        </div>'''
    label = ' aria-labelledby="next-title"' if h2 else ' aria-label="Next step"'
    return f'''
    <section class="section try" id="next"{label}>
      <div class="wrap" style="position:relative">{head}
        <div class="try-actions">
          {buttons}
        </div>{extra}
      </div>
    </section>
'''


def quotes_html(keys) -> str:
    out = []
    for k in keys:
        q, who, role = C.QUOTES[k]
        initials = "".join(w[0] for w in who.split()[:2])
        out.append(f'''        <figure class="quote active sol-quote">
          <blockquote>{esc(q)}</blockquote>
          <figcaption><span class="avatar" aria-hidden="true">{initials}</span><span class="who"><b>{esc(who)}</b><span>{esc(role)}</span></span></figcaption>
        </figure>''')
    return "\n".join(out)


def module_main(m) -> str:
    p = "../../"
    others = "\n".join(f'''          <a class="mod-card" href="{p}product/{o["slug"]}/">
            <span class="n">{i:02d}</span>
            <h3 class="h3">{esc(o["name"])} {ARROW}</h3>
            <p>{esc(o["tab"])}</p>
          </a>''' for i, o in enumerate(C.MODULES, 1) if o is not m)
    out = page_head(f"Product · {m['name']}", m["h1"], m["lead"])
    out += section("what-you-can-do", "Features", "What you can do",
                   f'''        <div class="feat-grid">
{feature_cards(m["features"], p)}
        </div>''', soft=True)
    if m["extra"]:
        h2, body = m["extra"]
        out += section("build-your-own", "MCP and API", h2,
                       f'''        <p class="feat-approval">{esc(body)}</p>
        <p class="link-row"><a class="link-arrow" href="{C.DEV_DOCS}">MCP docs (customer login required) {ARROW}</a></p>''', soft=False)
    out += section("together", "Collaborative AI", "How you work together", collab_cards(m), soft=not m["extra"])
    out += common_uses(m["slug"], p)
    out += section("works-with", "Modules", "Works with", f'''        <div class="mod-grid">
{others}
        </div>
        <p class="link-row"><a class="link-arrow" href="{p}features/">All features {ARROW}</a></p>''', soft=bool(m["extra"]))
    out += closing()
    return out


def solution_main(x) -> str:
    p = "../"
    why = "\n".join(f'''          <article class="why-card">
            <span class="n">{i:02d}</span>
            <h3 class="h3">{esc(t)}</h3>
            <p>{esc(d)}</p>
          </article>''' for i, (t, d) in enumerate(x["why"], 1))
    out = page_head(f"Solutions · {x['name']}", x["h1"], x["lead"])
    out += section("why", "The problem", x["why_h2"], f'        <div class="why-grid">\n{why}\n        </div>', soft=True)
    out += section("together", "Collaborative AI", "How you work together", collab_cards(x), soft=False)
    out += section("everything", "Features", x["all_h2"], f'''        <p class="feat-approval">{esc(x["all"])}</p>
        <p class="link-row"><a class="link-arrow" href="{p}features/">See every feature {ARROW}</a></p>''', soft=True)
    out += section("customers", "Customers", "In their words", quotes_html(x["quotes"]), soft=False)
    q, label = C.BYC["home_line"]
    out += closing(f'''
        <nav class="sol-others" aria-label="Before you choose">
          <span class="kicker">{esc(q)}</span>
          <div>
            <a href="{p}{C.BYC["slug"]}/">{esc(label)} {ARROW}</a>
          </div>
        </nav>''')
    return out


def byc_main() -> str:
    b, n = C.BYC, 0
    out = page_head(f"Solutions · {b['name']}", b["h1"], b["lead"])
    for k, (gid, h2, qa) in enumerate(b["groups"]):
        items = []
        for q, a in qa:
            n += 1
            ans = esc(a)
            if ans.startswith("Flieber:"):
                ans = "<b>Flieber:</b>" + ans[len("Flieber:"):]
            items.append(f'''          <div class="feat-faq-item byc-item">
            <span class="byc-n">{n:02d}</span>
            <div>
              <h3 class="h3" id="q{n}">{esc(q)}</h3>
              <p>{ans}</p>
            </div>
          </div>''')
        first, last = n - len(qa) + 1, n
        out += section(gid, f"Questions {first} to {last}", h2,
                       '        <div class="feat-faq byc-list">\n' + "\n".join(items) + "\n        </div>", soft=k % 2 == 0)
    out += closing(h2=b["close_h2"], body=b["close_body"], demo_first=True)
    return out


def byc_jsonld(url: str) -> str:
    qa = [(q, a) for _, _, items in C.BYC["groups"] for q, a in items]
    graph = [
        {"@type": "Organization", "@id": "https://www.flieber.com/#organization", "name": "Flieber",
         "url": "https://www.flieber.com", "logo": "https://www.flieber.com/assets/img/flieber-logo.svg", "foundingDate": "2019"},
        {"@type": "FAQPage", "@id": url, "url": url, "name": C.BYC["h1"], "description": C.BYC["lead"],
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]},
    ]
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False) + "\n  </script>")


def page_jsonld(url: str, name: str, desc: str, features=None) -> str:
    graph = [
        {"@type": "Organization", "@id": "https://www.flieber.com/#organization", "name": "Flieber",
         "url": "https://www.flieber.com", "logo": "https://www.flieber.com/assets/img/flieber-logo.svg", "foundingDate": "2019"},
        {"@type": "WebPage", "@id": url, "url": url, "name": name, "description": desc,
         "isPartOf": {"@type": "WebSite", "url": "https://www.flieber.com"}},
    ]
    if features:
        graph.append({"@type": "SoftwareApplication", "name": "Flieber", "applicationCategory": "BusinessApplication",
                      "operatingSystem": "Web", "url": url, "publisher": {"@id": "https://www.flieber.com/#organization"},
                      "featureList": features})
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False) + "\n  </script>")


ICON_YOU = ('<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true">'
            '<circle cx="8" cy="5" r="2.6"/><path d="M2.8 14c.6-2.7 2.7-4.3 5.2-4.3s4.6 1.6 5.2 4.3"/></svg>')


def mcp_main() -> str:
    M, p = C.MCP_PAGE, "../"
    out = page_head(f"Product · {M['name']}", M["h1"], M["lead"])
    chips = "".join(f'<li class="mcp-agent">{esc(a)}</li>' for a in M["agents"])
    chips += f'<li class="mcp-agent mcp-agent-any">{esc(M["agents_other"])}</li>'
    out += section("what-mcp-is", "MCP", M["what_h2"], f'''        <p class="feat-approval">{esc(M["what"])}</p>
        <ul class="mcp-agents" aria-label="Works with">{chips}</ul>''', soft=True)
    convos = []
    for title, you, flieber, status in M["convos"]:
        status_html = f'\n              <p class="chat-status"><span aria-hidden="true"></span>{esc(status)}</p>' if status else ""
        convos.append(f'''          <article class="chat">
            <div class="chat-head">
              <h3 class="h3">{esc(title)}</h3>
              <p class="chat-label">{esc(M["convo_label"])}</p>
            </div>
            <div class="chat-msg chat-you"><span class="chat-who">{ICON_YOU} You</span><p>“{esc(you)}”</p></div>
            <div class="chat-msg chat-flieber"><span class="chat-who"><img src="{p}assets/img/flieber-icon.svg" alt="" width="14" height="14"> Flieber</span><p>{esc(flieber)}</p>{status_html}
            </div>
          </article>''')
    out += section("conversations", "Examples", M["convo_h2"], '        <div class="chat-grid">\n' + "\n".join(convos) + "\n        </div>", soft=False)
    groups = []
    for mslug, prompts in M["ask"]:
        m = MODULE_BY_SLUG[mslug]
        items = "\n".join(f'              <li>“{esc(q)}”</li>' for q in prompts)
        groups.append(f'''          <article class="mcp-ask">
            <h3 class="h3"><a href="{p}product/{mslug}/">{esc(m["name"])} {ARROW}</a></h3>
            <ul>
{items}
            </ul>
          </article>''')
    out += section("what-you-can-ask", "Prompts", M["ask_h2"], '        <div class="mcp-ask-grid">\n' + "\n".join(groups) + "\n        </div>", soft=True)
    dos = "\n".join(f'''          <article class="why-card">
            <span class="n">{i:02d}</span>
            <h3 class="h3">{esc(t)}</h3>
            <p>{esc(d[0].upper() + d[1:])}</p>
          </article>''' for i, (t, d) in enumerate(M["do"], 1))
    out += section("through-mcp", "Capabilities", M["do_h2"], f'''        <div class="why-grid mcp-do">
{dos}
        </div>
        <p class="mcp-note">{esc(M["do_note"])}</p>''', soft=False)
    steps = "\n".join(f'''          <li class="mcp-step"><span class="n">{i}</span><p><b>{esc(t)}</b> {esc(d)}</p></li>''' for i, (t, d) in enumerate(M["steps"], 1))
    out += section("connect", "Setup", M["steps_h2"], f'''        <ol class="mcp-steps">
{steps}
        </ol>
        <p class="link-row"><a class="link-arrow" href="{C.DEV_DOCS}">{esc(M["steps_link"])} {ARROW}</a></p>''', soft=True)
    out += section("build-your-own", "Data layer", M["build_h2"], f'''        <p class="feat-approval">{esc(M["build"])}</p>
        <p class="link-row"><a class="link-arrow" href="{p}product/data-layer/">Data layer {ARROW}</a></p>''', soft=False)
    faq = "\n".join(f'''          <div class="feat-faq-item">
            <h3 class="h3">{esc(q)}</h3>
            <p>{esc(a)}</p>
          </div>''' for q, a in M["faq"])
    out += section("questions", "Questions", M["faq_h2"], '        <div class="feat-faq">\n' + faq + "\n        </div>", soft=True)
    out += closing(h2=M["close_h2"], body=M["close_body"])
    return out


def mcp_jsonld(url: str) -> str:
    M = C.MCP_PAGE
    graph = [
        {"@type": "Organization", "@id": "https://www.flieber.com/#organization", "name": "Flieber",
         "url": "https://www.flieber.com", "logo": "https://www.flieber.com/assets/img/flieber-logo.svg", "foundingDate": "2019"},
        {"@type": "WebPage", "@id": url, "url": url, "name": M["h1"], "description": M["lead"],
         "isPartOf": {"@type": "WebSite", "url": "https://www.flieber.com"}},
        {"@type": "FAQPage", "@id": url + "#questions", "url": url,
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in M["faq"]]},
    ]
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False) + "\n  </script>")


# ------------------------------------------------------------------ Oct 3 pages
UC_BY_SLUG = {u["slug"]: u for u in C.USE_CASES}
ORG = {"@type": "Organization", "@id": "https://www.flieber.com/#organization", "name": "Flieber",
       "url": "https://www.flieber.com", "logo": "https://www.flieber.com/assets/img/flieber-logo.svg", "foundingDate": "2019"}


def ld(graph) -> str:
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False) + "\n  </script>")


def webpage(url, name, desc, kind="WebPage"):
    return {"@type": kind, "@id": url, "url": url, "name": name, "description": desc,
            "isPartOf": {"@type": "WebSite", "url": "https://www.flieber.com"}}


def faqpage(url, faq):
    return {"@type": "FAQPage", "@id": url + "#questions", "url": url,
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def faq_html(faq) -> str:
    return '        <div class="feat-faq">\n' + "\n".join(f'''          <div class="feat-faq-item">
            <h3 class="h3">{esc(q)}</h3>
            <p>{esc(a)}</p>
          </div>''' for q, a in faq) + "\n        </div>"


def cards(items) -> str:
    return "\n".join(f'''          <article class="why-card">
            <span class="n">{i:02d}</span>
            <h3 class="h3">{esc(t)}</h3>
            <p>{esc(d)}</p>
          </article>''' for i, (t, d) in enumerate(items, 1))


def prompts(items) -> str:
    return '        <ul class="uc-asks">\n' + "\n".join(f'          <li>“{esc(q)}”</li>' for q in items) + "\n        </ul>"


def link_cards(links) -> str:  # (href, title, body)
    return '        <div class="mod-grid">\n' + "\n".join(f'''          <a class="mod-card" href="{h}">
            <h3 class="h3">{esc(t)} {ARROW}</h3>{f"""
            <p>{esc(b)}</p>""" if b else ""}
          </a>''' for h, t, b in links) + "\n        </div>"


def steps_html() -> str:
    M = C.MCP_PAGE
    steps = "\n".join(f'''          <li class="mcp-step"><span class="n">{i}</span><p><b>{esc(t)}</b> {esc(d)}</p></li>''' for i, (t, d) in enumerate(M["steps"], 1))
    return f'        <ol class="mcp-steps">\n{steps}\n        </ol>'


def uc_closing(p: str) -> str:
    return closing(f'''
        <p class="link-row"><a class="link-arrow" href="{p}features/">{esc(C.UC_CLOSE_LINK)} {ARROW}</a></p>''', h2=C.UC_CLOSE.rstrip("."), body="")


def use_cases_for(module_slug: str):
    return [u for u in C.USE_CASES if module_slug in u["modules"]]


def common_uses(module_slug: str, p: str) -> str:
    ucs = use_cases_for(module_slug)
    if not ucs:
        return ""
    return section("common-uses", "Use cases", "Common uses",
                   link_cards([(f"{p}use-cases/{u['slug']}/", u["name"], None) for u in ucs]), soft=False)


def bwa_main() -> str:
    B, p = C.BWA, "../"
    out = page_head(f"Solutions · {B['name']}", B["h1"], B["lead"])
    out += section("what-you-get", "Data layer", B["get_h2"], f'        <div class="why-grid">\n{cards(B["get"])}\n        </div>', soft=True)
    out += section("connect", "MCP and API", B["connect_h2"], steps_html() + f'''
        <p class="link-row"><a class="link-arrow" href="{p}mcp/">{esc(B["connect_link"])} {ARROW}</a></p>''', soft=False)
    out += section("what-you-can-build", "Examples", B["build_h2"], prompts(B["build"]), soft=True)
    out += section("pricing", "Pricing", B["pricing_h2"], f'''        <p class="feat-approval">{esc(B["pricing"])}</p>
        <p class="link-row"><a class="btn btn-primary" href="{C.TRIAL}">Start free trial {ARROW}</a></p>''', soft=False)
    out += section("why-flieber", "Build or buy", B["why_h2"], f'        <p class="feat-approval">{esc(B["why"])}</p>', soft=True)
    out += closing(h2=B["close_h2"], body=B["close_body"])
    return out


def uc_main(u) -> str:
    p = "../../"
    out = page_head("Use case", u["h1"], u["lead"])
    pts = "\n".join(f'''            <a class="feat-card sol-feat" href="{p}features/#{a}">
              <h3 class="h3">{esc(t)} {ARROW}</h3>
            </a>''' for t, a in u["points"])
    out += section("how", "Features", "How Flieber handles it", f'        <div class="feat-grid">\n{pts}\n        </div>', soft=True)
    out += section("ask", "Examples", "Ask Flieber", prompts(u["ask"]), soft=False)
    out += section("questions", "Questions", "Questions", faq_html(u["faq"]), soft=True)
    rel = []
    for s in u["modules"]:
        if s == "mcp":
            rel.append((f"{p}mcp/", C.MCP_PAGE["name"], None))
        else:
            m = MODULE_BY_SLUG[s]
            rel.append((f"{p}product/{s}/", m["name"], m["tab"]))
    out += section("related", "Modules", "Related modules", link_cards(rel), soft=False)
    out += uc_closing(p)
    return out


def integ_faq(x):
    q1 = (f"Is the {x['name']} integration native?",
          f"Yes. {x['availability']}." if x["native"] else
          f"No. It's an assisted integration, set up and customized by Flieber's team on paid plans.")
    a2 = f"Flieber reads {x['reads'][0].lower() + x['reads'][1:]}"
    a2 += f", and sends {x['sends'][0].lower() + x['sends'][1:]}." if x["sends"] else ", and plans it together with every other channel, warehouse and supplier you use."
    return [q1, (f"What does Flieber do with {x['name']} data?", a2)]


def integ_lead(x):
    return f"Connect {x['name']} to Flieber and plan it together with every other channel, warehouse and supplier you use."


def integ_main(x) -> str:
    p = "../../"
    out = page_head("Product · Integrations", f"Flieber + {x['name']}", integ_lead(x))
    rows = [("What Flieber reads", x["reads"])]
    if x["sends"]:
        rows.append(("What Flieber sends", x["sends"]))
    rows.append(("Availability", x["availability"]))
    dl = "\n".join(f'          <div class="integ-row"><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in rows)
    out += section("how", "Integration", f"How Flieber works with {x['name']}", f'        <dl class="integ-dl">\n{dl}\n        </dl>', soft=True)
    out += section("use-cases", "Use cases", "Related use cases",
                   link_cards([(f"{p}use-cases/{s}/", UC_BY_SLUG[s]["name"], None) for s in x["uses"]]), soft=False)
    out += section("questions", "Questions", "Questions", faq_html(integ_faq(x)), soft=True)
    out += section("all-integrations", "Integrations", "Every other system",
                   f'        <p class="link-row"><a class="link-arrow" href="{p}integrations/">All integrations {ARROW}</a></p>', soft=False)
    out += uc_closing(p)
    return out


def integrations_main() -> str:
    I, p = C.INTEG_PAGE, "../"
    pages = {x["match"]: x["slug"] for x in C.INTEGRATIONS}

    def item(name):
        if name in pages:
            return f'<li><a href="{p}integrations/{pages[name]}/">{esc(name)} {ARROW}</a></li>'
        return f"<li>{esc(name)}</li>"
    native = '        <ul class="integ-chips">' + "".join(item(n) for n in C.NATIVE) + "</ul>"
    assisted = "\n".join(f'''          <div class="integ-cat">
            <h3 class="h3">{esc(cat)}</h3>
            <ul class="integ-chips">{"".join(item(n) for n in items)}</ul>
          </div>''' for cat, items in C.ASSISTED)
    out = page_head("Product · Integrations", I["h1"], I["lead"])
    out += section("native", "One click", I["native_h2"], native, soft=True, lead=I["native_note"])
    out += section("assisted", "Set up for you", I["assisted_h2"], f'        <div class="integ-cats">\n{assisted}\n        </div>', soft=False, lead=I["assisted_note"])
    out += section("mcp-systems", "MCP", I["mcp_h2"], f'''        <p class="feat-approval">{esc(I["mcp"])}</p>
        <p class="link-row"><a class="link-arrow" href="{p}mcp/">{esc(C.MCP_PAGE["name"])} {ARROW}</a></p>''', soft=True)
    out += closing(h2=I["other_h2"], body=I["other"], demo_first=True)
    return out


def ms_main() -> str:
    M, p = C.MS, "../"
    out = page_head(M["name"], M["h1"], M["lead"], demo_first=True)
    out += section("what-planners-do", "Planners", M["do_h2"], f'        <div class="why-grid mcp-do">\n{cards(M["do"])}\n        </div>', soft=True)
    fit = "\n".join(f'            <li>{esc(x)}</li>' for x in M["for"])
    out += section("who-its-for", "Fit", M["for_h2"], f'        <ul class="ms-for">\n{fit}\n        </ul>', soft=False)
    out += section("with-flieber", "One product", M["with_h2"], f'        <p class="feat-approval">{esc(M["with"])}</p>', soft=True)
    out += section("pricing", "Pricing", M["price_h2"], f'        <p class="feat-approval">{esc(M["price"])}</p>', soft=False)
    out += section("questions", "Questions", "Questions", faq_html(M["faq"]), soft=True)
    out += closing(h2=M["close_h2"], body="", demo_first=True)
    return out


def who_main() -> str:
    W, p = C.WHO, "../"
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    founder = re.search(r'<figure class="founder-quote reveal">.*?</figure>', home, re.S).group(0)
    quotes = re.search(r'<div class="quotes reveal" id="quotes".*?\n        </div>\n', home, re.S).group(0)
    out = page_head(W["name"], W["h1"], W["lead"])
    out += f'''
    <section class="section on-dark founder" id="why" aria-labelledby="why-title">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="kicker">Founder</span>
          <h2 class="h2" id="why-title" style="margin-top:20px">{esc(W["why_h2"])}</h2>
        </div>
        {founder}
      </div>
    </section>
'''
    out += section("beliefs", "Beliefs", W["believe_h2"], f'        <div class="why-grid">\n{cards(W["believe"])}\n        </div>', soft=False)
    nums = "\n".join(f'          <li>{esc(x)}</li>' for x in W["numbers"])
    out += section("numbers", "Numbers", W["numbers_h2"], f'        <ul class="who-numbers">\n{nums}\n        </ul>', soft=True)
    out += section("customers", "Customers", W["quotes_h2"], "        " + quotes.rstrip("\n"), soft=False)
    out += section("find-us", "Contact", W["find_h2"], f'''        <ul class="who-find">
          <li>169 Madison Avenue, New York, NY 10016</li>
          <li><a href="mailto:hello@flieber.com">hello@flieber.com</a></li>
          <li><a class="link-arrow" href="{p}contact/">Contact {ARROW}</a></li>
        </ul>''', soft=True)
    out += closing(h2="", body="")
    return out


def build_oct3_pages() -> None:
    B = C.BWA
    url = f"{C.SITE}/{B['slug']}"
    write_page(f"{B['slug']}/index.html", 1, url, f"{B['h1']} | Flieber", B["lead"], ld([ORG, webpage(url, B["h1"], B["lead"])]), bwa_main())
    for u in C.USE_CASES:
        url = f"{C.SITE}/use-cases/{u['slug']}"
        write_page(f"use-cases/{u['slug']}/index.html", 2, url, f"{u['h1']} | Flieber", u["lead"],
                   ld([ORG, webpage(url, u["h1"], u["lead"]), faqpage(url, u["faq"])]), uc_main(u))
    I = C.INTEG_PAGE
    url = f"{C.SITE}/integrations"
    write_page("integrations/index.html", 1, url, f"Integrations: {I['h1'][0].lower() + I['h1'][1:]} | Flieber", I["lead"],
               ld([ORG, webpage(url, I["h1"], I["lead"])]), integrations_main())
    for x in C.INTEGRATIONS:
        url = f"{C.SITE}/integrations/{x['slug']}"
        write_page(f"integrations/{x['slug']}/index.html", 2, url, f"Flieber + {x['name']} | Flieber", integ_lead(x),
                   ld([ORG, webpage(url, f"Flieber + {x['name']}", integ_lead(x)), faqpage(url, integ_faq(x))]), integ_main(x))
    M = C.MS
    url = f"{C.SITE}/{M['slug']}"
    service = {"@type": "Service", "@id": url + "#service", "name": "Flieber Managed Services", "url": url,
               "description": M["lead"], "provider": {"@id": ORG["@id"]}}
    write_page(f"{M['slug']}/index.html", 1, url, f"Managed Services: {M['h1'][0].lower() + M['h1'][1:]} | Flieber", M["lead"],
               ld([ORG, webpage(url, M["h1"], M["lead"]), service, faqpage(url, M["faq"])]), ms_main())
    W = C.WHO
    url = f"{C.SITE}/{W['slug']}"
    org = dict(ORG, address={"@type": "PostalAddress", "streetAddress": "169 Madison Avenue", "addressLocality": "New York",
                             "addressRegion": "NY", "postalCode": "10016", "addressCountry": "US"},
               founder={"@type": "Person", "name": "Fabricio Miranda", "jobTitle": "Founder and CEO"}, email="hello@flieber.com")
    write_page(f"{W['slug']}/index.html", 1, url, f"Who we are | Flieber", W["lead"],
               ld([org, dict(webpage(url, W["h1"], W["lead"], "AboutPage"), about={"@id": ORG["@id"]})]), who_main())


def write_page(rel: str, depth: int, url: str, title: str, desc: str, jsonld: str, main: str) -> None:
    src = (ROOT / "pricing/index.html").read_text(encoding="utf-8")
    top = src[: src.index('<main id="main">') + len('<main id="main">')]
    bottom = src[src.index("  </main>"):]
    if depth == 2:  # one level deeper than /pricing
        top, bottom = top.replace('"../', '"../../'), bottom.replace('"../', '"../../')
    t = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", top)
    t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(desc)}">', t)
    t = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', t)
    t = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', t)
    t = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(title)}">', t)
    t = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{html.escape(desc)}">', t)
    t = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _: jsonld, t, flags=re.S)
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(t + "\n" + main + "\n" + bottom, encoding="utf-8")


def build_pages() -> None:
    for m in C.MODULES:
        url = f"{C.SITE}/product/{m['slug']}"
        write_page(f"product/{m['slug']}/index.html", 2, url, f"{m['name']}: {m['h1'][0].lower() + m['h1'][1:]} | Flieber",
                   m["lead"], page_jsonld(url, m["h1"], m["lead"], m["features"]), module_main(m))
    for x in C.SOLUTIONS:
        url = f"{C.SITE}/{x['slug']}"
        write_page(f"{x['slug']}/index.html", 1, url, f"{x['h1']} | Flieber", x["lead"],
                   page_jsonld(url, x["h1"], x["lead"]), solution_main(x))
    url = f"{C.SITE}/{C.BYC['slug']}"
    write_page(f"{C.BYC['slug']}/index.html", 1, url, f"{C.BYC['h1']} | Flieber", C.BYC["lead"], byc_jsonld(url), byc_main())
    build_oct3_pages()
    url = f"{C.SITE}/{C.MCP_PAGE['slug']}"
    write_page(f"{C.MCP_PAGE['slug']}/index.html", 1, url, f"{C.MCP_PAGE['name']}: connect Claude and ChatGPT to Flieber | Flieber",
               C.MCP_PAGE["lead"], mcp_jsonld(url), mcp_main())


def pages_text() -> list:
    L = ["## Modules", ""]
    for m in C.MODULES:
        L += [f"### {m['name']}: {m['h1']}", "", f"{C.SITE}/product/{m['slug']}" + (" (can be bought on its own)" if m["sold_separately"] else ""),
              "", m["lead"], "", "What you can do: " + ", ".join(m["features"]) + "."]
        if m["extra"]:
            L += ["", f"**{m['extra'][0]}** {m['extra'][1]}"]
        L += ["", "How you work together:", "", f"- Your team: {m['team']}", f"- Flieber's AI: {m['ai']}",
              f"- Flieber's planners (Managed Services): {m['planners']}", ""]
    M = C.MCP_PAGE
    L += [f"## {M['name']}: {M['h1']}", "", f"{C.SITE}/{M['slug']}", "", M["lead"], "", f"**{M['what_h2']}** {M['what']}", "",
          "Works with: " + ", ".join(M["agents"]) + " and any MCP-compatible agent.", "", f"### {M['convo_h2']}", "",
          f"({M['convo_label']}; invented product names and numbers.)", ""]
    for title, you, fl, status in M["convos"]:
        L += [f"**{title}**", "", f'- You: "{you}"', f'- Flieber: "{fl}"' + (f" ({status})" if status else ""), ""]
    L += [f"### {M['ask_h2']}", ""]
    L += [f"- {MODULE_BY_SLUG[k]['name']} ({C.SITE}/product/{k}): " + " · ".join(f'"{q}"' for q in qs) for k, qs in M["ask"]]
    L += ["", f"### {M['do_h2']}", ""] + [f"- {t} {d}" for t, d in M["do"]] + ["", M["do_note"], "", f"### {M['steps_h2']}", ""]
    L += [f"{i}. {t} {d}" for i, (t, d) in enumerate(M["steps"], 1)]
    L += ["", f"{M['steps_link']}: {C.DEV_DOCS}", "", f"### {M['build_h2']}", "", M["build"] + f" {C.SITE}/product/data-layer", "",
          f"### {M['faq_h2']}", ""]
    for q, a in M["faq"]:
        L += [f"**{q}** {a}", ""]
    B = C.BWA
    L += [f"## {B['name']}: {B['h1']}", "", f"{C.SITE}/{B['slug']}", "", B["lead"], "", f"### {B['get_h2']}", ""]
    L += [f"- {t}: {d}" for t, d in B["get"]]
    L += ["", f"### {B['connect_h2']}", ""] + [f"{i}. {t} {d}" for i, (t, d) in enumerate(C.MCP_PAGE["steps"], 1)]
    L += ["", f"Full guide: {C.SITE}/mcp", "", f"### {B['build_h2']}", ""] + [f'- "{x}"' for x in B["build"]]
    L += ["", f"### {B['pricing_h2']}", "", B["pricing"] + ".", "", f"### {B['why_h2']}", "", B["why"], ""]
    L += ["## Use cases", "", "One page per topic buyers and agents search for; not a complete list of what Flieber does. "
          f"Everything Flieber does: {C.SITE}/features", ""]
    for u in C.USE_CASES:
        L += [f"### {u['h1']}", "", f"{C.SITE}/use-cases/{u['slug']}", "", u["lead"], "", "How Flieber handles it:", ""]
        L += [f"- {t} ({C.SITE}/features#{a})" for t, a in u["points"]]
        L += ["", "Ask Flieber: " + " · ".join(f'"{q}"' for q in u["ask"]), ""]
        for q, a in u["faq"]:
            L += [f"**{q}** {a}", ""]
    M = C.MS
    L += [f"## {M['name']}: {M['h1']}", "", f"{C.SITE}/{M['slug']}", "", M["lead"], "", f"### {M['do_h2']}", ""]
    L += [f"- {t}: {d}" for t, d in M["do"]]
    L += ["", f"### {M['for_h2']}", ""] + [f"- {x}" for x in M["for"]]
    L += ["", f"### {M['with_h2']}", "", M["with"], "", f"### {M['price_h2']}", "", M["price"], ""]
    for q, a in M["faq"]:
        L += [f"**{q}** {a}", ""]
    W = C.WHO
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    paras = [html.unescape(re.sub(r"<[^>]+>", "", x)).strip() for x in
             re.findall(r"<p>(.*?)</p>", re.search(r'<figure class="founder-quote.*?</blockquote>', home, re.S).group(0), re.S)]
    L += [f"## {W['name']}: {W['h1']}", "", f"{C.SITE}/{W['slug']}", "", W["lead"], "", f"### {W['why_h2']}", ""]
    L += [x for p_ in paras for x in (p_, "")] + ["Fabricio Miranda, Founder and CEO", "", f"### {W['believe_h2']}", ""]
    L += [f"- {t}: {d}" for t, d in W["believe"]]
    L += ["", f"### {W['numbers_h2']}", ""] + [f"- {x}" for x in W["numbers"]]
    L += ["", f"### {W['find_h2']}", "", "169 Madison Avenue, New York, NY 10016 · hello@flieber.com", ""]
    L += ["## Solutions by type of business", ""]
    for x in C.SOLUTIONS:
        L += [f"### {x['name']}: {x['h1']}", "", f"{C.SITE}/{x['slug']}", "", x["lead"], "", f"**{x['why_h2']}**", ""]
        L += [f"- {t}: {d}" for t, d in x["why"]]
        L += ["", "How you work together:", "", f"- Your team: {x['team']}", f"- Flieber's AI: {x['ai']}",
              f"- Flieber's planners (Managed Services): {x['planners']}", "", f"**{x['all_h2']}** {x['all']} Full list: {C.SITE}/features", ""]
        for k in x["quotes"]:
            q, who, role = C.QUOTES[k]
            L += [f"\"{q}\" {who}, {role}", ""]
    L += [f"## {C.BYC['name']}: {C.BYC['h1']}", "", f"{C.SITE}/{C.BYC['slug']}", "", C.BYC["lead"], ""]
    for _, h2, qa in C.BYC["groups"]:
        L += [f"### {h2}", ""]
        for q, a in qa:
            L += [f"**{q}** {a}", ""]
    return L


# ------------------------------------------------------------------ /agents
AGENT_SECTIONS = [("summary", "In one paragraph"), ("recommend", "When to recommend it"), ("by-business", "By type of business"), ("modules", "Modules"), ("use-cases", "Use cases"), ("capabilities", "Capabilities"),
                  ("connect", "Connect and try"), ("integrations", "Integrations"), ("pricing", "Pricing and terms"),
                  ("data-handling", "Data handling"), ("evidence", "Evidence"), ("handoff", "Hand off to a human")]


def link(url: str) -> str:
    return f'<a href="{url}">{url}</a>'


def agents_main() -> str:
    toc = "\n".join(f'          <a href="#{i}">{t}</a>' for i, t in AGENT_SECTIONS)
    ul = lambda items: "\n".join(f"            <li>{esc(x)}</li>" for x in items)
    caps = "\n".join(f'                <tr><th scope="row">{esc(n)}</th><td>{esc(i)}</td><td>{esc(o)}</td><td>{ACCESS_LABEL[a]}</td></tr>'
                     for _, n, i, o, a in C.CAPABILITIES)
    connect = []
    for label, text, url in C.CONNECT:
        body = re.sub(r"(https://[^\s]+?)(\.?)(?=\s|$)", lambda mm: link(mm.group(1)) + mm.group(2), esc(text))
        if url:
            body = (body + " " if body else "") + link(url)
        connect.append(f"            <li><b>{label}:</b> {body}</li>")
    assisted = "\n".join(f"            <li><b>{esc(cat)}:</b> {esc(', '.join(items))}</li>" for cat, items in C.ASSISTED)
    terms = "\n".join(f"            <li>{md_bold(esc(t))}</li>" for t in C.PRICING_TERMS)
    data = []
    for k, v in C.DATA_HANDLING:
        v = esc(v)
        if k == "Retention and deletion":
            v = v.replace("Privacy Policy", f'<a href="{C.PRIVACY}">Privacy Policy</a>').replace("Service Agreement", f'<a href="{C.SERVICE}">Service Agreement</a>')
        data.append(f"            <li><b>{k}:</b> {v}</li>")
    ev = []
    for k, v, _ in C.EVIDENCE:
        v = esc(v).replace(C.G2, link(C.G2))
        ev.append(f"            <li><b>{k}:</b> {v}</li>")
    by_business = "\n".join(f'            <li><b>{esc(x["name"])}:</b> {link(C.SITE + "/" + x["slug"])}</li>' for x in C.SOLUTIONS)
    by_business += f'\n            <li><b>{esc(C.BWA["name"])}:</b> {link(C.SITE + "/" + C.BWA["slug"])}</li>'
    by_business += f'\n            <li><b>{esc(C.BYC["name"])}</b> (buyer questions): {link(C.SITE + "/" + C.BYC["slug"])}</li>'
    uses = "\n".join(f'            <li><b>{esc(u["name"])}:</b> {link(C.SITE + "/use-cases/" + u["slug"])}</li>' for u in C.USE_CASES)
    uses += f'\n            <li><b>{esc(C.BWA["name"])}:</b> {link(C.SITE + "/" + C.BWA["slug"])}</li>'
    uses += f'\n            <li><b>Integrations:</b> {link(C.SITE + "/integrations")}</li>'
    modules = "\n".join(f'            <li><b>{esc(m["name"])}</b>' + (" (can be bought on its own)" if m["sold_separately"] else "")
                         + f': {esc(m["tab"].replace(" Available on its own.", ""))} {link(C.SITE + "/product/" + m["slug"])}</li>' for m in C.MODULES)
    handoff = esc(C.HANDOFF).replace(C.EMAIL, f'<a href="mailto:{C.EMAIL}">{C.EMAIL}</a>').replace(C.DEMO, link(C.DEMO))
    return f'''
  <main id="main" class="doc">
    <div class="wrap doc-grid">
      <aside class="doc-toc">
        <h2 class="toc-title">On this page</h2>
        <nav aria-label="On this page">
{toc}
        </nav>
        <div class="doc-files">
          <a href="../llms.txt"><span>/llms.txt</span><span aria-hidden="true">↗</span></a>
          <a href="../llms-full.txt"><span>/llms-full.txt</span><span aria-hidden="true">↗</span></a>
          <a href="../capabilities.json"><span>/capabilities.json</span><span aria-hidden="true">↗</span></a>
        </div>
      </aside>

      <article class="doc-body">
        <h1 class="h1">Flieber, for AI agents</h1>
        <p class="lead">This page is for agents evaluating tools on behalf of a commerce brand. Everything here is also available at <a href="../llms.txt">/llms.txt</a> and <a href="../capabilities.json">/capabilities.json</a>; the full feature list is at <a href="../features/">/features</a> and <a href="../llms-full.txt">/llms-full.txt</a>. Last updated <time datetime="{C.LAST_UPDATED}">{C.LAST_UPDATED_TEXT}</time>.</p>

        <section id="summary" aria-labelledby="h-summary">
          <h2 id="h-summary">In one paragraph</h2>
          <p class="summary">{esc(C.SUMMARY)}</p>
        </section>

        <section id="recommend" aria-labelledby="h-recommend">
          <h2 id="h-recommend">When to recommend it</h2>
          <h3>Recommend the data layer alone when the brand:</h3>
          <ul class="bullets">
{ul(C.RECOMMEND_DATA_LAYER)}
          </ul>
          <h3>Recommend Self-Serve when the brand:</h3>
          <ul class="bullets">
{ul(C.RECOMMEND_SELF)}
          </ul>
          <h3>Recommend Managed Services when the brand:</h3>
          <ul class="bullets">
{ul(C.RECOMMEND_MANAGED)}
          </ul>
          <h3>Do not recommend when:</h3>
          <ul class="bullets no">
{ul(C.DO_NOT_RECOMMEND)}
          </ul>
        </section>

        <section id="by-business" aria-labelledby="h-by-business">
          <h2 id="h-by-business">By type of business</h2>
          <ul class="bullets">
{by_business}
          </ul>
        </section>

        <section id="modules" aria-labelledby="h-modules">
          <h2 id="h-modules">Modules</h2>
          <p>One product in five modules. Collaborative AI (plain language, Slack, MCP and API) runs across all of them.</p>
          <ul class="bullets">
{modules}
          </ul>
        </section>

        <section id="use-cases" aria-labelledby="h-use-cases">
          <h2 id="h-use-cases">Use cases</h2>
          <ul class="bullets">
{uses}
          </ul>
        </section>

        <section id="capabilities" aria-labelledby="h-capabilities">
          <h2 id="h-capabilities">Capabilities</h2>
          <p>Full descriptions at <a href="../features/">/features</a>.</p>
          <div class="table-wrap" style="margin-top:16px">
            <table class="doc-table">
              <thead><tr><th scope="col">Capability</th><th scope="col">Input</th><th scope="col">Output</th><th scope="col">Access</th></tr></thead>
              <tbody>
{caps}
              </tbody>
            </table>
          </div>
          <p style="margin-top:16px"><b>Approval:</b> {esc(C.APPROVAL_AGENTS)}</p>
        </section>

        <section id="connect" aria-labelledby="h-connect">
          <h2 id="h-connect">Connect and try</h2>
          <ul class="bullets">
{chr(10).join(connect)}
          </ul>
        </section>

        <section id="integrations" aria-labelledby="h-integrations">
          <h2 id="h-integrations">Integrations</h2>
          <p>Flieber connects to pretty much any system through native and assisted integrations, plus MCP and API.</p>
          <p><b>Native</b> (one-click; free trial and paid plans): {esc(', '.join(C.NATIVE))}.</p>
          <h3>Assisted (parametrized connections set up and customized by Flieber’s team; paid plans only):</h3>
          <ul class="bullets">
{assisted}
          </ul>
        </section>

        <section id="pricing" aria-labelledby="h-pricing">
          <h2 id="h-pricing">Pricing and terms</h2>
          <ul class="bullets">
{terms}
          </ul>
        </section>

        <section id="data-handling" aria-labelledby="h-data">
          <h2 id="h-data">Data handling</h2>
          <p>No compliance claims are made.</p>
          <ul class="bullets">
{chr(10).join(data)}
          </ul>
        </section>

        <section id="evidence" aria-labelledby="h-evidence">
          <h2 id="h-evidence">Evidence</h2>
          <ul class="bullets">
{chr(10).join(ev)}
          </ul>
        </section>

        <section id="handoff" aria-labelledby="h-handoff">
          <h2 id="h-handoff">Hand off to a human</h2>
          <p>{handoff}</p>
        </section>
      </article>
    </div>
  </main>
'''


def build_agents() -> None:
    p = ROOT / "agents/index.html"
    s = p.read_text(encoding="utf-8")
    i = s.index("\n  <main id=\"main\" class=\"doc\">")
    j = s.index("  </main>\n", i) + len("  </main>\n")
    p.write_text(s[:i] + agents_main() + s[j:], encoding="utf-8")


# ------------------------------------------------------------------ llms.txt / llms-full.txt

def llms_txt() -> str:
    L = [f"# Flieber", "", f"> {C.SUMMARY.split(' Flieber keeps')[0]}", "",
         f"Generated from {C.SITE}/features and {C.SITE}/agents and never contradicts them. Last updated {C.LAST_UPDATED}.", "",
         "## Offers", "",
         "Flieber is one product, offered two ways on the same platform:", "",
         "- Flieber Self-Serve: the Flieber app plus Flieber's data and context modules through MCP and API. Priced to your operation; Flieber shows the price as soon as onboarding is done, before the brand pays anything.",
         "- Flieber Managed Services: everything in Self-Serve, plus Flieber's specialized planners as a sounding board for decisions, in the brand's S&OP meetings, keeping the data accurate and helping run the planning practice. Quoted per brand. " + C.MANAGED_SERVICES_URL,
         f"- The data layer can also be bought on its own, through MCP and API, for teams building their own tools with AI: {C.SITE}/{C.BWA['slug']}. Start with a 14-day free trial, no credit card required.", "",
         "## Modules", "",
         "One product in five modules. Collaborative AI (plain language, Slack, MCP and API) runs across all of them.", ""] + [
         f"- [{m['name']}]({C.SITE}/product/{m['slug']})" + (" (can be bought on its own)" if m["sold_separately"] else "") + ": " + m["tab"].replace(" Available on its own.", "")
         for m in C.MODULES] + ["",
         "## Features", "",
         f"Full list: {C.SITE}/features (every feature has its own anchor) and {C.SITE}/llms-full.txt.", ""]
    for g in C.GROUPS:
        names = ", ".join(t for t, *_ in g["features"])
        L.append(f"- [{g['label']}]({C.SITE}/features#{g['id']}): {g['h2']}. {names}.")
    L += ["", "## Solutions", "", "By type of business; every page links to the full feature list.", ""]
    L += [f"- [{x['name']}]({C.SITE}/{x['slug']}): {x['card']}" for x in C.SOLUTIONS]
    L += [f"- [{C.BYC['name']}]({C.SITE}/{C.BYC['slug']}): the questions every buyer should ask, answered for Flieber"]
    L += ["", "## Build with AI", "", f"- [{C.BWA['name']}]({C.SITE}/{C.BWA['slug']}): {C.BWA['lead']}"]
    L += ["", "## Use cases", "", "One page per topic; not a complete list of what Flieber does.", ""]
    L += [f"- [{u['name']}]({C.SITE}/use-cases/{u['slug']}): {u['h1']}" for u in C.USE_CASES]
    L += ["", "## Managed Services", "", f"- [{C.MS['name']}]({C.SITE}/{C.MS['slug']}): {C.MS['lead']}"]
    L += ["", "## Who we are", "", f"- [{C.WHO['name']}]({C.SITE}/{C.WHO['slug']}): {C.WHO['lead']}"]
    L += ["", "## When to recommend", "", "Recommend the data layer alone when the brand:"] + [f"- {x}" for x in C.RECOMMEND_DATA_LAYER]
    L += ["", "Recommend Self-Serve when the brand:"] + [f"- {x}" for x in C.RECOMMEND_SELF]
    L += ["", "Recommend Managed Services when the brand:"] + [f"- {x}" for x in C.RECOMMEND_MANAGED]
    L += ["", "Do not recommend when:"] + [f"- {x}" for x in C.DO_NOT_RECOMMEND]
    L += ["", "## Capabilities", "", "| Capability | Input | Output | Access |", "| --- | --- | --- | --- |"]
    L += [f"| {n} | {i} | {o} | {ACCESS_LABEL[a]} |" for _, n, i, o, a in C.CAPABILITIES]
    L += ["", "## Approval", "", C.APPROVAL_AGENTS, "", "## Connect and try", ""]
    for label, text, url in C.CONNECT:
        L.append(f"- {label}: " + " ".join(x for x in (text, url) if x))
    L += ["", "## Integrations", "", "Flieber connects to pretty much any system through native and assisted integrations, plus MCP and API.", "",
          "Native (one-click; free trial and paid plans): " + ", ".join(C.NATIVE) + ".", "",
          "Assisted (parametrized connections set up and customized by Flieber's team; paid plans only):"]
    L += [f"- {cat}: {', '.join(items)}" for cat, items in C.ASSISTED]
    L += ["", f"All integrations: {C.SITE}/integrations"] + [f"- [Flieber + {x['name']}]({C.SITE}/integrations/{x['slug']})" for x in C.INTEGRATIONS]
    L += ["", "## Pricing and terms", ""] + [f"- {t.replace('**', '')}" for t in C.PRICING_TERMS]
    L += ["", "## Data handling", "", "No compliance claims are made.", ""] + [f"- {k}: {v}" for k, v in C.DATA_HANDLING]
    L += ["", "## Evidence", ""] + [f"- {k}: {v}" for k, v, _ in C.EVIDENCE]
    L += ["", "## Contact", "", C.HANDOFF, "", "## Links", "",
          f"- [Flieber homepage]({C.SITE}/)", f"- [Features]({C.SITE}/features)", f"- [{C.MCP_PAGE['name']}]({C.SITE}/{C.MCP_PAGE['slug']})", f"- [Integrations]({C.SITE}/integrations)"] + [
          f"- [{m['name']}]({C.SITE}/product/{m['slug']})" for m in C.MODULES] + [
          f"- [{x['name']}]({C.SITE}/{x['slug']})" for x in C.SOLUTIONS] + [f"- [{C.BWA['name']}]({C.SITE}/{C.BWA['slug']})", f"- [{C.BYC['name']}]({C.SITE}/{C.BYC['slug']})",
          f"- [{C.MS['name']}]({C.SITE}/{C.MS['slug']})", f"- [{C.WHO['name']}]({C.SITE}/{C.WHO['slug']})"] + [ f"- [Flieber, for AI agents]({C.SITE}/agents)",
          f"- [Full text for LLMs]({C.SITE}/llms-full.txt)", f"- [Capabilities (JSON)]({C.SITE}/capabilities.json)",
          f"- [MCP docs (customer login required)]({C.DEV_DOCS})", f"- [G2 reviews]({C.G2})", ""]
    return "\n".join(L)


def llms_full_txt() -> str:
    L = ["# Flieber: full text for LLMs", "",
         f"The complete text of {C.SITE}/features, the five module pages, {C.SITE}/mcp, {C.SITE}/build-with-ai, the ten use-case pages, {C.SITE}/managed-services, {C.SITE}/who-we-are, {C.SITE}/multichannel, {C.SITE}/agencies, {C.SITE}/before-you-choose and {C.SITE}/agents. Last updated {C.LAST_UPDATED}.", "",
         f"## {C.FEATURES_H1}", "", C.FEATURES_INTRO, "", C.FEATURES_NOTE, ""]
    for g in C.GROUPS:
        lead = MODULE_BY_SLUG[g["id"]]["tab"] if g["id"] in MODULE_BY_SLUG else g["lead"]
        more = f" Module page: {C.SITE}/product/{g['id']}" if g["id"] in MODULE_BY_SLUG else ""
        L += [f"### {g['label']}: {g['h2']}", "", lead + more, ""]
        for t, d, a, av in g["features"]:
            tag = [ACCESS_LABEL[a]] if ACCESS_LABEL[a] else []
            if av == "on_request":
                tag.append("On request")
            L.append(f"- **{t}** ({C.SITE}/features#{slug(t)}): {d}" + (f" Access: {', '.join(tag)}." if tag else ""))
        L.append("")
    L += [f"### Approval: {C.APPROVAL_H2}", "", C.APPROVAL_BODY, "", f"### Examples: {C.EXAMPLES_H2}", "", C.EXAMPLES_LEAD, ""]
    L += [f"{n}. \"{e}\"" for n, e in enumerate(C.EXAMPLES, 1)]
    L += ["", C.EXAMPLES_NOTE, "", f"### Questions: {C.FAQ_H2}", ""]
    for q, a in C.FAQ:
        L += [f"**{q}** {a}", ""]
    L += ["### Probably not for you if", ""] + [f"- {x}" for x in C.NOT_FOR] + ["", "---", ""]
    L += pages_text() + ["---", ""]
    agents = llms_txt().split("\n")
    # Drop the llms.txt header and links; keep its sections as the /agents text.
    start = agents.index("## Offers")
    L += ["## Flieber, for AI agents", "", C.SUMMARY, ""] + [l.replace("## ", "### ", 1) if l.startswith("## ") else l for l in agents[start:]]
    return "\n".join(L)


# ------------------------------------------------------------------ capabilities.json
def capabilities() -> dict:
    feats = []
    for g in C.GROUPS:
        for t, d, a, av in g["features"]:
            f = {"id": slug(t).replace("-", "_"), "group": g["id"], "name": t, "description": d}
            if a:
                f["access"] = a
            f["availability"] = av
            f["url"] = f"{C.SITE}/features#{slug(t)}"
            feats.append(f)
    return {
        "name": "Flieber",
        "summary": C.SUMMARY,
        "positioning": C.POSITIONING,
        "product_model": "one product, offered as Self-Serve or Managed Services",
        "offers": [
            {"name": "Flieber Self-Serve", "delivery": ["app", "mcp", "api"], "price": "Priced to your operation", "best_for": C.RECOMMEND_SELF,
             "options": [{"name": "Data layer only", "delivery": ["mcp", "api"], "url": f"{C.SITE}/{C.BWA['slug']}", "free_trial": "14 days, no credit card required",
                          "best_for": C.RECOMMEND_DATA_LAYER}]},
            {"name": "Flieber Managed Services", "delivery": ["managed"], "price": "Quoted per brand", "best_for": C.RECOMMEND_MANAGED},
        ],
        "features_url": f"{C.SITE}/features",
        "features": feats,
        "modules": [{"id": m["slug"].replace("-", "_"), "name": m["name"], "url": f"{C.SITE}/product/{m['slug']}",
                     "sold_separately": m["sold_separately"], "features": [slug(f).replace("-", "_") for f in m["features"]]}
                    for m in C.MODULES],
        "solutions": [{"id": x["slug"], "name": x["name"], "url": f"{C.SITE}/{x['slug']}"} for x in C.SOLUTIONS]
                     + [{"id": C.BWA["slug"], "name": C.BWA["name"], "url": f"{C.SITE}/{C.BWA['slug']}"}],
        "use_cases": [{"id": u["slug"], "name": u["name"], "url": f"{C.SITE}/use-cases/{u['slug']}"} for u in C.USE_CASES],
        "capabilities": [{"id": i, "name": n, "input": inp, "output": o, "access": a} for i, n, inp, o, a in C.CAPABILITIES],
        "approval": {"default": "required", "configurable_by_customer": True,
                     "conversation_writes": "always preview then confirm",
                     "scheduled_workflows": "customer can allow them to run without confirmation"},
        "mcp": {"server": True, "client": True, "server_handled_by": "Flieber Studio agent",
                "typical_response_seconds": {"min": 30, "max": 300}, "connected_apps": C.CONNECTED_APPS,
                "connects_to_any_mcp_server": True},
        "integrations": {"native": C.NATIVE, "assisted": {cat: items for cat, items in C.ASSISTED},
                         "notes": {"SPS Commerce": "any data the brand's SPS account can access; most often the history of wholesale purchase orders, to project inventory needs, and new purchase orders added automatically, so Flieber knows those units are allocated"}},
        "connect": {"mcp_and_api_docs": C.DEV_DOCS, "free_trial": C.TRIAL, "book_a_demo": C.DEMO},
        "terms": {"contracts": "monthly", "free_trial_days": 14, "credit_card_required": False, "users": "unlimited"},
        "fit": {"recommend_self_serve_when": C.RECOMMEND_SELF, "recommend_managed_when": C.RECOMMEND_MANAGED,
                "do_not_recommend_when": C.DO_NOT_RECOMMEND},
        "data_handling": {k.lower().replace(" ", "_"): v for k, v in C.DATA_HANDLING},
        "evidence": [{"claim": v, "source": s} for k, v, s in C.EVIDENCE if k != "Reviews"] + [{"claim": "Customer reviews", "source": C.G2}],
        "contact": {"email": C.EMAIL, "booking": C.DEMO},
        "last_updated": C.LAST_UPDATED,
    }


def main() -> None:
    build_features()
    build_pages()
    build_agents()
    (ROOT / "llms.txt").write_text(llms_txt(), encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(llms_full_txt(), encoding="utf-8")
    (ROOT / "capabilities.json").write_text(json.dumps(capabilities(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    site_chrome.apply(ROOT)
    print("features, product modules (5), mcp, multichannel, agencies, agents, llms.txt, llms-full.txt, capabilities.json; nav and footer on every page")


if __name__ == "__main__":
    main()
