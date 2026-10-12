"""Option 3: shared head, navigation, journey bar and footer.

Navigation follows the Website Strategy & Functional Specification (Oct 12, 2026), section 6:
Build · Run · Solutions · Pricing · Who we are · /agents, then Log in · Book a demo · Start free trial.
Build and Run are menus whose subpages keep each audience's own terms.
"""
import re

DEMO = "https://www.flieber.com/book-a-demo"
TRIAL = "https://www.flieber.com/free-trial"
DEV_DOCS = "https://app.flieber.com/app/developers"
PRIVACY = "https://www.flieber.com/privacy-policy"
SERVICE = "https://www.flieber.com/service-agreement"
CSS_V = "49"
JS_V = "17"

RUN_APPS = [  # slug, name, one-line answer (Option 2 module copy)
    ("forecasting", "Demand forecasting", "What will sell, and where?",
     "Forecasts for every product on every channel, corrected for stockouts and promotions."),
    ("inventory", "Inventory forecasting", "Where will I run out, or sit on too much?",
     "Stockouts, overstock and lost sales by product and location, while there’s still time to act."),
    ("replenishment", "Replenishment", "What should I buy or move, how much and when?",
     "Purchase and transfer recommendations within MOQs, case packs, lead times and cash, tested before you commit."),
    ("workflows", "Workflows", "How does the decision get done?",
     "Approved decisions carried into suppliers, ERPs, Amazon, 3PLs and your own tools, with as much or as little approval as you choose."),
]

CHEVRON = ('<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true">'
           '<path d="M2 3.5l3 3 3-3" stroke="currentColor" stroke-width="1.5"/></svg>')


def head(p, path, title, desc, extra=""):
    url = "https://www.flieber.com/" + path
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- PREVIEW ONLY: remove before public launch -->
  <meta name="robots" content="noindex, nofollow">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="{p}assets/img/favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#F5ED61">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Flieber">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta name="twitter:card" content="summary">

  <!-- Machine-readable versions for AI agents -->
  <link rel="alternate" type="text/plain" href="{p}llms.txt" title="Flieber for LLMs">
  <link rel="alternate" type="application/json" href="{p}capabilities.json" title="Flieber capabilities">

  <link rel="preload" href="{p}assets/fonts/open-sauce-one-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{p}assets/fonts/open-sauce-one-latin-600-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{p}assets/css/site.css?v={CSS_V}">

  <script>document.documentElement.classList.remove('no-js');</script>
  <!-- Google Tag Manager (GTM-5FS8NPG) and HubSpot tracking (portal 5767502).
       Loaded only on flieber.com so preview traffic stays out of analytics. -->
  <script>
    (function (h) {{
      if (!/(^|\\.)flieber\\.com$/.test(h)) return;
      (function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-5FS8NPG');
      var hs = document.createElement('script'); hs.id = 'hs-script-loader'; hs.async = true; hs.defer = true;
      hs.src = 'https://js.hs-scripts.com/5767502.js'; document.head.appendChild(hs);
    }})(location.hostname);
  </script>{extra}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

"""


def drop(key, label, cur, items, dot=""):
    current = " is-current" if cur == key else ""
    return f"""<div class="nav-drop{current}">
          <button class="nav-drop-btn" type="button" aria-expanded="false" aria-controls="nav-{key}">{dot}{label} {CHEVRON}</button>
          <div class="nav-menu" id="nav-{key}">
{items}
          </div>
        </div>"""


def nav_html(p, cur):
    def a(href, label, key):
        ac = ' aria-current="page"' if key == cur else ""
        return f'<a href="{href}"{ac}>{label}</a>'
    build = (f'            <a class="nav-menu-all" href="{p}build/">Build overview <span aria-hidden="true">→</span></a>\n'
             '            <div class="nav-sub">\n'
             f'              <a href="{p}build/data/">Data foundation</a>\n'
             f'              <a href="{p}build/#intelligence">Inventory intelligence</a>\n'
             f'              <a href="{p}build/#templates">App templates</a>\n'
             f'              <a href="{p}build/#reliability">Reliability and validation</a>\n'
             '            </div>\n            <hr class="nav-menu-sep">\n'
             f'            <a href="{p}mcp/">MCP and API</a>\n'
             f'            <a href="{p}customize/">Build services</a>\n'
             f'            <a href="{p}integrations/">Integrations</a>\n'
             f'            <a href="{p}security/">Security &amp; data</a>')
    run = (f'            <a class="nav-menu-all" href="{p}run/">Run overview <span aria-hidden="true">→</span></a>\n'
           '            <div class="nav-sub">\n'
           + "\n".join(f'              <a href="{p}run/{s}/">{n}</a>' for s, n, _, _ in RUN_APPS) +
           '\n            </div>\n            <hr class="nav-menu-sep">\n'
           f'            <a href="{p}managed-services/">Managed Services</a>\n'
           f'            <a href="{p}put-flieber-to-work/">Put Flieber to work</a>\n'
           f'            <a href="{p}features/">All features</a>')
    sol = (f'            <a href="{p}multichannel/">Multichannel brands</a>\n'
           f'            <a href="{p}agencies/">Agencies and aggregators</a>\n'
           '            <hr class="nav-menu-sep">\n'
           f'            <a href="{p}before-you-choose/">Before you choose</a>')
    agents_cur = ' aria-current="page"' if cur == "agents" else ""
    return f"""  <header class="nav" id="nav">
    <div class="wrap">
      <a class="nav-logo" href="{p or './'}" aria-label="Flieber home">
        <img src="{p}assets/img/flieber-logo.svg" alt="Flieber" width="116" height="20">
      </a>
      <nav class="nav-links" aria-label="Primary">
        {drop("build", "Build", cur, build, '<i class="jdot jdot-build" aria-hidden="true"></i>')}
        {drop("run", "Run", cur, run, '<i class="jdot jdot-run" aria-hidden="true"></i>')}
        {drop("solutions", "Solutions", cur, sol)}
        {a(p + "pricing/", "Pricing", "pricing")}
        {a(p + "who-we-are/", "Who we are", "who")}
        <a class="agents-link" href="{p}agents/"{agents_cur} aria-label="For AI agents"><code>/agents</code></a>
        <a class="menu-only" href="https://app.flieber.com">Log in</a>
        <a class="menu-only" href="{DEMO}">Book a demo</a>
      </nav>
      <div class="nav-cta">
        <a class="nav-login" href="https://app.flieber.com">Log in</a>
        <a class="btn btn-ghost btn-sm" href="{DEMO}">Book a demo</a>
        <a class="btn btn-primary btn-sm" href="{TRIAL}">Start free trial</a>
        <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span></button>
      </div>
    </div>
  </header>"""


def pathbar(p, journey, crumbs):
    """Persistent journey indicator with a one-click switch (spec section 12)."""
    items = "".join(
        f'<li><a href="{h}">{t}</a></li>' if h else f'<li><span aria-current="page">{t}</span></li>'
        for t, h in crumbs)
    b = ' aria-current="true"' if journey == "build" else ""
    r = ' aria-current="true"' if journey == "run" else ""
    return f"""  <div class="pathbar">
    <div class="wrap">
      <nav aria-label="Breadcrumb"><ol class="crumbs">{items}</ol></nav>
      <nav class="path-switch" aria-label="Choose your path">
        <a href="{p}build/"{b}><i class="jdot jdot-build" aria-hidden="true"></i>Build with Flieber</a>
        <a href="{p}run/"{r}><i class="jdot jdot-run" aria-hidden="true"></i>Run with Flieber</a>
      </nav>
    </div>
  </div>"""


def footer_html(p, mark):
    run = "\n".join(f'            <li><a href="{p}run/{s}/">{n}</a></li>' for s, n, _, _ in RUN_APPS)
    mark_html = (f'\n      <div class="footer-mark" aria-hidden="true"><img src="{p}assets/img/flieber-logo-light.svg" alt=""></div>'
                 if mark else "")
    return f"""  <footer class="footer">
    <div class="wrap">
      <div class="footer-top">
        <div class="footer-brand">
          <img src="{p}assets/img/flieber-logo-light.svg" alt="Flieber" width="132" height="23">
          <p class="tagline">Inventory software that works <em>the way you do.</em></p>
        </div>
        <div>
          <h2 class="footer-h">Build</h2>
          <ul>
            <li><a href="{p}build/">Build overview</a></li>
            <li><a href="{p}build/data/">Data foundation</a></li>
            <li><a href="{p}build/#templates">App templates</a></li>
            <li><a href="{p}mcp/">MCP and API</a></li>
            <li><a href="{p}customize/">Build services</a></li>
            <li><a href="{p}integrations/">Integrations</a></li>
          </ul>
        </div>
        <div>
          <h2 class="footer-h">Run</h2>
          <ul>
            <li><a href="{p}run/">Run overview</a></li>
{run}
            <li><a href="{p}managed-services/">Managed Services</a></li>
            <li><a href="{p}pricing/">Pricing</a></li>
          </ul>
        </div>
        <div>
          <h2 class="footer-h">For agents</h2>
          <ul>
            <li><a href="{p}agents/"><code>/agents</code></a></li>
            <li><a href="{p}llms.txt"><code>/llms.txt</code></a></li>
            <li><a href="{p}capabilities.json"><code>/capabilities.json</code></a></li>
            <li><a href="{DEV_DOCS}">MCP docs</a></li>
          </ul>
        </div>
        <div>
          <h2 class="footer-h">Company</h2>
          <ul>
            <li><a href="{p}who-we-are/">Who we are</a></li>
            <li><a href="{p}multichannel/">Multichannel brands</a></li>
            <li><a href="{p}agencies/">Agencies and aggregators</a></li>
            <li><a href="{p}security/">Security &amp; data</a></li>
            <li><a href="https://help.flieber.com">Help center</a></li>
            <li><a href="https://www.flieber.com/blog">Blog</a></li>
            <li><a href="{p}contact/">Contact</a></li>
            <li><a href="{PRIVACY}">Privacy</a></li>
            <li><a href="{SERVICE}">Service agreement</a></li>
          </ul>
        </div>
      </div>{mark_html}
      <div class="footer-bottom">
        <span>169 Madison Avenue, New York, NY 10016</span>
        <span>© <span id="year">2026</span> Flieber</span>
      </div>
    </div>
  </footer>"""


def tail(p):
    return f"""
  <script src="{p}assets/js/site.js?v={JS_V}" defer></script>
</body>
</html>
"""


def apply(path, text, p, cur):
    """Swap nav and footer on a page carried over from Option 2."""
    text = re.sub(r'  <header class="nav" id="nav">.*?</header>', lambda m: nav_html(p, cur), text, count=1, flags=re.S)
    mark = 'class="footer-mark"' in text
    text = re.sub(r'  <footer class="footer">.*?</footer>', lambda m: footer_html(p, mark), text, count=1, flags=re.S)
    text = re.sub(r'site\.css\?v=\d+', f'site.css?v={CSS_V}', text)
    return text
