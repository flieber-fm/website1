#!/usr/bin/env python3
"""Generate /features, the five /solutions pages, the /agents body, llms.txt, llms-full.txt and
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
        cards = []
        for title, desc, access, avail in g["features"]:
            tags = []
            if ACCESS_LABEL[access]:
                tags.append(ACCESS_LABEL[access])
            if avail == "on_request":
                tags.append("On request")
            tag_html = f'\n              <p class="feat-tag">{" · ".join(tags)}</p>' if tags else ""
            cards.append(f'''            <article class="feat-card" id="{slug(title)}">
              <h3 class="h3">{esc(title)}</h3>
              <p>{esc(desc)}</p>{tag_html}
            </article>''')
        out.append(f'''
    <section class="section{soft} feat-group" id="{g["id"]}" aria-labelledby="{g["id"]}-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">{esc(g["label"])}</span>
          <h2 class="h2" id="{g["id"]}-title" style="margin-top:20px">{esc(g["h2"])}</h2>
          <p class="lead">{esc(g["lead"])}</p>
        </div>
        <div class="feat-grid">
{chr(10).join(cards)}
        </div>
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
    desc = ("Every Flieber feature: your team makes the calls, Flieber's AI keeps the data true, prepares every "
            "decision and carries it out once you approve. Forecasts, purchase orders, inbound shipments, MCP and API.")
    top = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", top)
    top = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', top)
    top = top.replace('https://www.flieber.com/pricing"', 'https://www.flieber.com/features"')
    top = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', top)
    top = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', top)
    top = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: features_jsonld(), top, flags=re.S)
    out = ROOT / "features/index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(top + "\n" + features_main() + "\n" + bottom, encoding="utf-8")


# ------------------------------------------------------------------ /solutions
FEATURES_BY_TITLE = {t: (g, d, a, av) for g in C.GROUPS for t, d, a, av in g["features"]}
FAQ_BY_Q = dict(C.FAQ)
ICON_TEAM = '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true"><circle cx="5.5" cy="5.5" r="2.2"/><circle cx="11" cy="6" r="1.8"/><path d="M1.6 13.5c.5-2.3 2-3.6 3.9-3.6s3.4 1.3 3.9 3.6M10 9.6c1.9 0 3.3 1.2 3.8 3.4"/></svg>'
ICON_AI = '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true"><path d="M8 1.8l1.5 3.7 3.7 1.5-3.7 1.5L8 12.2 6.5 8.5 2.8 7l3.7-1.5z"/><path d="M12.6 11.2l.6 1.5 1.5.6-1.5.6-.6 1.5-.6-1.5-1.5-.6 1.5-.6z"/></svg>'
ICON_PLANNER = '<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true"><circle cx="8" cy="5" r="2.6"/><path d="M2.8 14c.6-2.7 2.7-4.3 5.2-4.3s4.6 1.6 5.2 4.3"/></svg>'


def collab_cards(team: str, ai: str, planners: str, planners_tag: str) -> str:
    """Three-party collaboration cards, shared by the solutions pages (the homepage has its own copy)."""
    cols = [("Your team", ICON_TEAM, team, None, ""), ("Flieber’s AI", ICON_AI, ai, None, " collab-ai"),
            ("Flieber’s planners", ICON_PLANNER, planners, planners_tag, "")]
    out = []
    for name, icon, body, tag, cls in cols:
        tag_html = f'<span class="collab-tag">{esc(tag)}</span>' if tag else ""
        out.append(f'''          <article class="collab-card{cls}">
            <div class="collab-top"><span class="collab-ic">{icon}</span>{tag_html}</div>
            <h3 class="h3">{name}</h3>
            <p>{esc(body)}</p>
          </article>''')
    return '        <div class="collab reveal-stagger">\n' + "\n".join(out) + "\n        </div>"


def solution_feature_cards(x, p: str) -> str:
    cards = []
    for f in x["features"]:
        if f in FEATURES_BY_TITLE:
            g, d, a, av = FEATURES_BY_TITLE[f]
            href, desc = f"{p}features/#{slug(f)}", d
            tags = [ACCESS_LABEL[a]] if ACCESS_LABEL[a] else []
            if av == "on_request":
                tags.append("On request")
        else:
            gid = C.FEATURE_LINK_FALLBACK[f]
            g = next(g for g in C.GROUPS if g["id"] == gid)
            href, desc, tags = f"{p}features/#{gid}", g["lead"], []
        tag_html = f'\n              <p class="feat-tag">{" · ".join(tags)}</p>' if tags else ""
        cards.append(f'''            <a class="feat-card sol-feat" href="{href}">
              <h3 class="h3">{esc(f)} <span class="arrow" aria-hidden="true">→</span></h3>
              <p>{esc(desc)}</p>{tag_html}
            </a>''')
    return "\n".join(cards)


def solution_main(x) -> str:
    p = "../../"
    examples = "\n".join(f'          <li><span class="feat-q">“{esc(e)}”</span></li>' for e in x["examples"])
    quote = ""
    if x["quote"]:
        q, who, role = x["quote"]
        initials = "".join(w[0] for w in who.split()[:2])
        quote = f'''
        <figure class="quote active sol-quote">
          <blockquote>{esc(q)}</blockquote>
          <figcaption><span class="avatar" aria-hidden="true">{initials}</span><span class="who"><b>{esc(who)}</b><span>{esc(role)}</span></span></figcaption>
        </figure>'''
    faq = ""
    if x["faq"]:
        items = "\n".join(f'''          <div class="feat-faq-item">
            <h3 class="h3">{esc(q)}</h3>
            <p>{esc(FAQ_BY_Q[q])}</p>
          </div>''' for q in x["faq"])
        faq = f'''
    <section class="section" id="questions" aria-labelledby="questions-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Questions</span>
          <h2 class="h2" id="questions-title" style="margin-top:20px">{esc(C.FAQ_H2)}</h2>
        </div>
        <div class="feat-faq">
{items}
        </div>
        <p class="link-row"><a class="link-arrow" href="{p}features/#questions">More questions <span class="arrow" aria-hidden="true">→</span></a></p>
      </div>
    </section>
'''
    others = "\n".join(f'            <a href="{p}solutions/{o["slug"]}/">{esc(o["name"])}</a>' for o in C.SOLUTIONS if o is not x)
    return f'''
    <section class="page-head sol-head" aria-labelledby="sol-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Solutions · {esc(x["short"])}</span>
          <h1 class="h1" id="sol-title">{esc(x["h1"])}</h1>
          <p class="lead">{esc(x["lead"])}</p>
        </div>
        <div class="sol-actions">
          <a class="btn btn-primary" href="{C.TRIAL}">Start free trial <span class="arrow" aria-hidden="true">→</span></a>
          <a class="btn btn-ghost" href="{C.DEMO}">Book a demo</a>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="together" aria-labelledby="together-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Collaborative AI</span>
          <h2 class="h2" id="together-title" style="margin-top:20px">How you work together</h2>
        </div>
{collab_cards(x["team"], x["ai"], x["planners"], "With Managed Services")}
      </div>
    </section>

    <section class="section" id="features-involved" aria-labelledby="feat-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Features</span>
          <h2 class="h2" id="feat-title" style="margin-top:20px">Features involved</h2>
        </div>
        <div class="feat-grid">
{solution_feature_cards(x, p)}
        </div>
        <p class="link-row"><a class="link-arrow" href="{p}features/">See every feature <span class="arrow" aria-hidden="true">→</span></a></p>
      </div>
    </section>

    <section class="section section-soft" id="examples" aria-labelledby="examples-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Examples</span>
          <h2 class="h2" id="examples-title" style="margin-top:20px">Example requests</h2>
        </div>
        <ol class="feat-examples">
{examples}
        </ol>
        <p class="feat-note">{esc(C.EXAMPLES_NOTE)}</p>{quote}
      </div>
    </section>
{faq}
    <section class="section try" id="next" aria-labelledby="next-title">
      <div class="wrap" style="position:relative">
        <div class="section-head">
          <span class="kicker">Next step</span>
          <h2 class="h2" id="next-title" style="margin-top:20px">{esc(C.SOLUTIONS_CLOSE_H2)}</h2>
          <p class="lead">{esc(C.SOLUTIONS_CLOSE_BODY)}</p>
        </div>
        <div class="try-actions">
          <a class="btn btn-primary" href="{C.TRIAL}">Start free trial <span class="arrow" aria-hidden="true">→</span></a>
          <a class="btn btn-ghost" href="{C.DEMO}">Book a demo</a>
        </div>
        <nav class="sol-others" aria-label="Other solutions">
          <span class="kicker">Other solutions</span>
          <div>
{others}
          </div>
        </nav>
      </div>
    </section>
'''


def solution_jsonld(x) -> str:
    url = f"{C.SITE}/solutions/{x['slug']}"
    graph = [
        {"@type": "Organization", "@id": "https://www.flieber.com/#organization", "name": "Flieber",
         "url": "https://www.flieber.com", "logo": "https://www.flieber.com/assets/img/flieber-logo.svg", "foundingDate": "2019"},
        {"@type": "WebPage", "@id": url, "url": url, "name": x["h1"], "description": x["lead"],
         "isPartOf": {"@type": "WebSite", "url": "https://www.flieber.com"},
         "about": {"@type": "SoftwareApplication", "name": "Flieber", "applicationCategory": "BusinessApplication",
                   "operatingSystem": "Web", "publisher": {"@id": "https://www.flieber.com/#organization"}}},
    ]
    if x["faq"]:
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": FAQ_BY_Q[q]}} for q in x["faq"]]})
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False) + "\n  </script>")


def build_solutions() -> None:
    src = (ROOT / "pricing/index.html").read_text(encoding="utf-8")
    top = src[: src.index('<main id="main">') + len('<main id="main">')]
    bottom = src[src.index("  </main>"):]
    # One level deeper than /pricing: fix the relative asset paths in the head and the script tag.
    top = top.replace('"../', '"../../')
    bottom = bottom.replace('"../', '"../../')
    for x in C.SOLUTIONS:
        title = f"{x['h1']} | Flieber"
        desc = x["lead"]
        url = f"{C.SITE}/solutions/{x['slug']}"
        t = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", top)
        t = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{html.escape(desc)}">', t)
        t = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', t)
        t = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', t)
        t = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(title)}">', t)
        t = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{html.escape(desc)}">', t)
        t = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: solution_jsonld(x), t, flags=re.S)
        out = ROOT / "solutions" / x["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(t + "\n" + solution_main(x) + "\n" + bottom, encoding="utf-8")


def solutions_text() -> list:
    L = ["## Solutions", ""]
    for x in C.SOLUTIONS:
        L += [f"### {x['name']}: {x['h1']}", "", f"{C.SITE}/solutions/{x['slug']}", "", x["lead"], "",
              "How you work together:", "",
              f"- Your team: {x['team']}", f"- Flieber's AI: {x['ai']}", f"- Flieber's planners (Managed Services): {x['planners']}", "",
              "Features involved: " + ", ".join(x["features"]) + ".", "", "Example requests:", ""]
        L += [f"- \"{e}\"" for e in x["examples"]]
        if x["quote"]:
            q, who, role = x["quote"]
            L += ["", f"\"{q}\" {who}, {role}"]
        for q in x["faq"]:
            L += ["", f"**{q}** {FAQ_BY_Q[q]}"]
        L.append("")
    return L


# ------------------------------------------------------------------ /agents
AGENT_SECTIONS = [("summary", "In one paragraph"), ("recommend", "When to recommend it"), ("use-cases", "Recommend by use case"), ("capabilities", "Capabilities"),
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
        body = esc(text)
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
    use_cases = "\n".join(f'            <li><b>{esc(x["name"])}:</b> {esc(x["card"])} {link(C.SITE + "/solutions/" + x["slug"])}</li>' for x in C.SOLUTIONS)
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

        <section id="use-cases" aria-labelledby="h-use-cases">
          <h2 id="h-use-cases">Recommend by use case</h2>
          <ul class="bullets">
{use_cases}
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
         "- Flieber Self-Serve: the Flieber app plus Flieber's data and context modules through MCP and API. Priced to your operation; the exact price is shared on a demo.",
         "- Flieber Managed Services: everything in Self-Serve, plus Flieber's specialized planners as a sounding board for decisions, in the brand's S&OP meetings, keeping the data accurate and helping run the planning practice. Quoted per brand.", "",
         "## Features", "",
         f"Full list: {C.SITE}/features (every feature has its own anchor) and {C.SITE}/llms-full.txt.", ""]
    for g in C.GROUPS:
        names = ", ".join(t for t, *_ in g["features"])
        L.append(f"- [{g['label']}]({C.SITE}/features#{g['id']}): {g['h2']}. {names}.")
    L += ["", "## Solutions", "", "Flieber by use case; each page lists the features involved and example requests.", ""]
    L += [f"- [{x['name']}]({C.SITE}/solutions/{x['slug']}): {x['card']}" for x in C.SOLUTIONS]
    L += ["", "## When to recommend", "", "Recommend Self-Serve when the brand:"] + [f"- {x}" for x in C.RECOMMEND_SELF]
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
    L += ["", "## Pricing and terms", ""] + [f"- {t.replace('**', '')}" for t in C.PRICING_TERMS]
    L += ["", "## Data handling", "", "No compliance claims are made.", ""] + [f"- {k}: {v}" for k, v in C.DATA_HANDLING]
    L += ["", "## Evidence", ""] + [f"- {k}: {v}" for k, v, _ in C.EVIDENCE]
    L += ["", "## Contact", "", C.HANDOFF, "", "## Links", "",
          f"- [Flieber homepage]({C.SITE}/)", f"- [Features]({C.SITE}/features)"] + [
          f"- [{x['name']}]({C.SITE}/solutions/{x['slug']})" for x in C.SOLUTIONS] + [ f"- [Flieber, for AI agents]({C.SITE}/agents)",
          f"- [Full text for LLMs]({C.SITE}/llms-full.txt)", f"- [Capabilities (JSON)]({C.SITE}/capabilities.json)",
          f"- [MCP docs (customer login required)]({C.DEV_DOCS})", f"- [G2 reviews]({C.G2})", ""]
    return "\n".join(L)


def llms_full_txt() -> str:
    L = ["# Flieber: full text for LLMs", "",
         f"The complete text of {C.SITE}/features, the five solutions pages and {C.SITE}/agents. Last updated {C.LAST_UPDATED}.", "",
         f"## {C.FEATURES_H1}", "", C.FEATURES_INTRO, "", C.FEATURES_NOTE, ""]
    for g in C.GROUPS:
        L += [f"### {g['label']}: {g['h2']}", "", g["lead"], ""]
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
    L += solutions_text() + ["---", ""]
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
            {"name": "Flieber Self-Serve", "delivery": ["app", "mcp", "api"], "price": "Priced to your operation", "best_for": C.RECOMMEND_SELF},
            {"name": "Flieber Managed Services", "delivery": ["managed"], "price": "Quoted per brand", "best_for": C.RECOMMEND_MANAGED},
        ],
        "features_url": f"{C.SITE}/features",
        "features": feats,
        "solutions": [{"id": x["slug"].replace("-", "_"), "name": x["name"], "url": f"{C.SITE}/solutions/{x['slug']}",
                       "features": [slug(f).replace("-", "_") for f in x["features"] if f not in C.FEATURE_LINK_FALLBACK]}
                      for x in C.SOLUTIONS],
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
    build_solutions()
    build_agents()
    (ROOT / "llms.txt").write_text(llms_txt(), encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(llms_full_txt(), encoding="utf-8")
    (ROOT / "capabilities.json").write_text(json.dumps(capabilities(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    site_chrome.apply(ROOT)
    print("features, solutions (5), agents, llms.txt, llms-full.txt, capabilities.json; nav and footer on every page")


if __name__ == "__main__":
    main()
