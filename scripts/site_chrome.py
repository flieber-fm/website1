"""Navigation and footer shared by every page (Option 2 brief, sections 3 and 4).

Navigation: Product (menu: All features with the five modules nested under it, then Integrations, MCP and AI agents and Security & data) · Solutions (menu: the three pages by type of
business and goal, then Before you choose) · Pricing · Who we are · /agents, then Log in · Book a demo · Start free trial.
build-content.py writes these into every page listed in PAGE_FILES.
"""
import html
import re

import site_content as C


def esc(text: str) -> str:
    return html.escape(text, quote=False).replace("'", "’")


PAGE_FILES = {  # file: (path prefix to the site root, current nav item)
    "index.html": ("", None),
    "features/index.html": ("../", "product"),
    "pricing/index.html": ("../", "pricing"),
    "security/index.html": ("../", "product"),
    "contact/index.html": ("../", None),
    "agents/index.html": ("../", "agents"),
}
for _m in C.MODULES:
    PAGE_FILES[f"product/{_m['slug']}/index.html"] = ("../../", "product")
for _s in C.SOLUTIONS:
    PAGE_FILES[f"{_s['slug']}/index.html"] = ("../", "solutions")
PAGE_FILES[f"{C.BYC['slug']}/index.html"] = ("../", "solutions")
PAGE_FILES[f"{C.MCP_PAGE['slug']}/index.html"] = ("../", "product")
PAGE_FILES[f"{C.BWA['slug']}/index.html"] = ("../", "solutions")
PAGE_FILES["integrations/index.html"] = ("../", "product")
for _x in C.INTEGRATIONS:
    PAGE_FILES[f"integrations/{_x['slug']}/index.html"] = ("../../", "product")
for _u in C.USE_CASES:  # not in any menu (brief 7)
    PAGE_FILES[f"use-cases/{_u['slug']}/index.html"] = ("../../", None)
PAGE_FILES[f"{C.MS['slug']}/index.html"] = ("../", None)
PAGE_FILES[f"{C.WHO['slug']}/index.html"] = ("../", "who")

CHEVRON = ('<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true">'
           '<path d="M2 3.5l3 3 3-3" stroke="currentColor" stroke-width="1.5"/></svg>')


def drop_html(key: str, label: str, cur, items: str) -> str:
    current = " is-current" if cur == key else ""
    return f"""<div class="nav-drop{current}">
          <button class="nav-drop-btn" type="button" aria-expanded="false" aria-controls="nav-{key}">{label} {CHEVRON}</button>
          <div class="nav-menu" id="nav-{key}">
{items}
          </div>
        </div>"""


def nav_html(p: str, cur) -> str:
    def a(href, label, key):
        ac = ' aria-current="page"' if key == cur else ""
        return f'<a href="{href}"{ac}>{label}</a>'
    # "All features" first, the five modules nested under it, then a divider and the other product pages.
    product = f'            <a class="nav-menu-all" href="{p}features/">All features <span aria-hidden="true">→</span></a>\n'
    product += '            <div class="nav-sub">\n'
    product += "\n".join(f'              <a href="{p}product/{m["slug"]}/">{esc(m["name"])}</a>' for m in C.MODULES)
    product += '\n            </div>\n            <hr class="nav-menu-sep">'
    product += f'\n            <a href="{p}integrations/">Integrations</a>'
    product += f'\n            <a href="{p}{C.MCP_PAGE["slug"]}/">{esc(C.MCP_PAGE["name"])}</a>'
    product += f'\n            <a href="{p}security/">Security &amp; data</a>'
    sol = "\n".join(f'            <a href="{p}{x["slug"]}/">{esc(x["name"])}</a>' for x in C.SOLUTIONS)
    sol += f'\n            <a href="{p}{C.BWA["slug"]}/">{esc(C.BWA["name"])}</a>'
    sol += f'\n            <a href="{p}{C.BYC["slug"]}/">{esc(C.BYC["name"])}</a>'
    agents_cur = ' aria-current="page"' if cur == "agents" else ""
    return f"""  <header class="nav" id="nav">
    <div class="wrap">
      <a class="nav-logo" href="{p or './'}" aria-label="Flieber home">
        <img src="{p}assets/img/flieber-logo.svg" alt="Flieber" width="116" height="20">
      </a>
      <nav class="nav-links" aria-label="Primary">
        {drop_html("product", "Product", cur, product)}
        {drop_html("solutions", "Solutions", cur, sol)}
        {a(p + "pricing/", "Pricing", "pricing")}
        {a(p + "who-we-are/", "Who we are", "who")}
        <a class="agents-link" href="{p}agents/"{agents_cur} aria-label="For AI agents"><code>/agents</code></a>
        <a class="menu-only" href="https://app.flieber.com">Log in</a>
        <a class="menu-only" href="{C.DEMO}">Book a demo</a>
      </nav>
      <div class="nav-cta">
        <a class="nav-login" href="https://app.flieber.com">Log in</a>
        <a class="btn btn-ghost btn-sm" href="{C.DEMO}">Book a demo</a>
        <a class="btn btn-primary btn-sm" href="{C.TRIAL}">Start free trial</a>
        <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span></button>
      </div>
    </div>
  </header>"""


def footer_html(p: str, mark: bool) -> str:
    sol = "\n".join(f'            <li><a href="{p}{x["slug"]}/">{esc(x["name"])}</a></li>' for x in C.SOLUTIONS)
    sol += f'\n            <li><a href="{p}{C.BWA["slug"]}/">{esc(C.BWA["name"])}</a></li>'
    sol += f'\n            <li><a href="{p}{C.BYC["slug"]}/">{esc(C.BYC["name"])}</a></li>'
    mark_html = (f'\n      <div class="footer-mark" aria-hidden="true"><img src="{p}assets/img/flieber-logo-light.svg" alt=""></div>'
                 if mark else "")
    return f"""  <footer class="footer">
    <div class="wrap">
      <div class="footer-top">
        <div class="footer-brand">
          <img src="{p}assets/img/flieber-logo-light.svg" alt="Flieber" width="132" height="23">
          <p class="tagline">Collaborative AI for <em>multichannel brands.</em></p>
        </div>
        <div>
          <h2 class="footer-h">Product</h2>
          <ul>
            <li><a href="{p}features/">Features</a></li>
            <li><a href="{p}integrations/">Integrations</a></li>
            <li><a href="{p}{C.MCP_PAGE["slug"]}/">{esc(C.MCP_PAGE["name"])}</a></li>
            <li><a href="{p}pricing/">Pricing</a></li>
            <li><a href="{p}security/">Security &amp; data</a></li>
            <li><a href="{p}{C.MS["slug"]}/">Managed Services</a></li>
          </ul>
        </div>
        <div>
          <h2 class="footer-h">Solutions</h2>
          <ul>
{sol}
          </ul>
        </div>
        <div>
          <h2 class="footer-h">For agents</h2>
          <ul>
            <li><a href="{p}agents/"><code>/agents</code></a></li>
            <li><a href="{p}llms.txt"><code>/llms.txt</code></a></li>
            <li><a href="{p}capabilities.json"><code>/capabilities.json</code></a></li>
            <li><a href="{C.DEV_DOCS}">MCP docs</a></li>
          </ul>
        </div>
        <div>
          <h2 class="footer-h">Company</h2>
          <ul>
            <li><a href="{p}who-we-are/">Who we are</a></li>
            <li><a href="https://help.flieber.com">Help center</a></li>
            <li><a href="https://www.flieber.com/blog">Blog</a></li>
            <li><a href="{p}contact/">Contact</a></li>
            <li><a href="{C.PRIVACY}">Privacy</a></li>
            <li><a href="{C.SERVICE}">Service agreement</a></li>
          </ul>
        </div>
      </div>{mark_html}
      <div class="footer-bottom">
        <span>169 Madison Avenue, New York, NY 10016</span>
        <span>© <span id="year">2026</span> Flieber</span>
      </div>
    </div>
  </footer>"""


def apply(root) -> None:
    for rel, (p, cur) in PAGE_FILES.items():
        f = root / rel
        s = f.read_text(encoding="utf-8")
        s = re.sub(r'  <header class="nav" id="nav">.*?</header>', lambda m: nav_html(p, cur), s, count=1, flags=re.S)
        mark = 'class="footer-mark"' in s
        s = re.sub(r'  <footer class="footer">.*?</footer>', lambda m: footer_html(p, mark), s, count=1, flags=re.S)
        f.write_text(s, encoding="utf-8")
