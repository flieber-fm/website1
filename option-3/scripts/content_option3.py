"""Option 3 page content.

Copy follows the Website Strategy & Functional Specification (Oct 12, 2026) for positioning and
structure, and reuses Option 2's approved facts and wording wherever a fact is stated.
Copy rules carried over from Option 2: sentence case, no em dashes, no serial comma,
headings never end with a period. Unconfirmed items render as visible [BRACKET] placeholders
(class "todo"), listed by scripts/check-placeholders.py.

"{P}" is replaced with the path prefix to the site root.
"""
import re

from chrome import DEMO, TRIAL, DEV_DOCS, RUN_APPS

BUILD_DATA_KICKER = "Build · Data foundation"
ARROW = '<span class="arrow" aria-hidden="true">→</span>'
CHECK = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">'
         '<path d="M2.5 7.2l3 3 6-6.4" stroke="#1B1C1C" stroke-width="1.6"/></svg>')
TICK = ('<span class="ico" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 12 12" fill="none">'
        '<path d="M2 6.2l2.6 2.6L10 3.2" stroke="#1B1C1C" stroke-width="1.6"/></svg></span>')
IC_BUILD = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4">'
            '<rect x="2" y="3" width="12" height="10" rx="2"/><path d="M5 7l2 1.5L5 10M8.5 10.5H11"/></svg>')
IC_RUN = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4">'
          '<path d="M2 13V3M2 13h12"/><path d="M4.5 10l3-3 2 2 4-4.5"/></svg>')
IC_TEAM = ('<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true">'
           '<circle cx="5.5" cy="5.5" r="2.2"/><circle cx="11" cy="6" r="1.8"/><path d="M1.6 13.5c.5-2.3 2-3.6 3.9-3.6s3.4 1.3 3.9 3.6M10 9.6c1.9 0 3.3 1.2 3.8 3.4"/></svg>')
IC_AI = ('<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true">'
         '<path d="M8 1.8l1.5 3.7 3.7 1.5-3.7 1.5L8 12.2 6.5 8.5 2.8 7l3.7-1.5z"/><path d="M12.6 11.2l.6 1.5 1.5.6-1.5.6-.6 1.5-.6-1.5-1.5-.6 1.5-.6z"/></svg>')
IC_PERSON = ('<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true">'
             '<circle cx="8" cy="5" r="2.6"/><path d="M2.8 14c.6-2.7 2.7-4.3 5.2-4.3s4.6 1.6 5.2 4.3"/></svg>')
IC_CODE = ('<svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#1B1C1C" stroke-width="1.4" aria-hidden="true">'
           '<path d="M5 4.5L1.8 8 5 11.5M11 4.5L14.2 8 11 11.5M9.2 3L6.8 13"/></svg>')
IC_SHIELD = ('<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#1B1C1C" stroke-width="1.4">'
             '<path d="M9 1.8l6 2.4v4.3c0 3.7-2.5 6.6-6 7.7-3.5-1.1-6-4-6-7.7V4.2z"/><path d="M6.3 9.1l1.9 1.9 3.6-3.8"/></svg>')
IC_CHART = ('<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#1B1C1C" stroke-width="1.4">'
            '<path d="M2.5 15.5h13"/><path d="M4 12l3.5-4 3 2.5L15 5"/></svg>')
IC_HEALTH = ('<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#1B1C1C" stroke-width="1.4">'
             '<path d="M1.8 9.5h3.4l1.8-4 3 8 1.8-4h4.4"/></svg>')
IC_APPROVE = ('<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="#1B1C1C" stroke-width="1.4">'
              '<rect x="2.4" y="3" width="13.2" height="12" rx="2"/><path d="M5.6 9.2l2.2 2.2 4.6-4.8"/></svg>')
PROMPT_IC = ('<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
             '<path d="M3 3v5a3 3 0 003 3h7m0 0l-3-3m3 3l-3 3" stroke="currentColor" stroke-width="1.4"/></svg>')


def pre(html):
    """Prefix root-relative links in snippets taken from Option 2's homepage."""
    return re.sub(r'(href|src)="(?!https?:|#|/|mailto:|data:|\{P\})', r'\1="{P}', html)


def todo(text):
    return f'<span class="todo">[{text}]</span>'


def head(kicker, title, tid, lead="", extra=""):
    lead_html = f'\n          <p class="lead">{lead}</p>' if lead else ""
    return f"""        <div class="section-head reveal">
          <span class="kicker">{kicker}</span>
          <h2 class="h2" id="{tid}" style="margin-top:20px">{title}</h2>{lead_html}{extra}
        </div>
"""


def faq(items):
    return "\n".join(
        f'          <details>\n            <summary>{q}<span class="plus" aria-hidden="true"></span></summary>\n'
        f'            <p>{a}</p>\n          </details>' for q, a in items)


def mq_cards(p="{P}"):
    out = []
    for i, (slug, name, q, a) in enumerate(RUN_APPS, 1):
        out.append(f"""          <a class="mq-card" href="{p}run/{slug}/">
            <span class="mq-mod"><span class="n">0{i}</span>{name}</span>
            <h3 class="mq-q">{q}</h3>
            <p>{a}</p>
            <span class="mq-go">{name} {ARROW}</span>
          </a>""")
    return "\n".join(out)


def layerstack(steps, more):
    lis, plates = [], []
    for i, (name, body) in enumerate(steps):
        active = " is-active" if i == 0 else ""
        lis.append(f"""              <li class="ls-step{active}" data-step="{i}">
                <button class="ls-pill" type="button" aria-controls="ls-body-{i}" aria-expanded="{'true' if i == 0 else 'false'}"><span class="ls-name">{name}</span><span class="ls-plus" aria-hidden="true"></span></button>
                <div class="ls-body" id="ls-body-{i}">
                  <div class="ls-body-inner">
                    <p class="ls-title">{name}</p>
                    <p>{body}</p>
                  </div>
                </div>
              </li>""")
        plates.append(f"""                <div class="iso-plate" style="--i:{i}" data-plate="{i}">
                  <div class="iso-top"><span class="iso-label">{name}</span></div>
                  <div class="iso-side iso-side-a"></div>
                  <div class="iso-side iso-side-b"></div>
                </div>""")
    return f"""      <div class="layerstack" id="layerstack" style="--n:{len(steps)}">
        <div class="ls-pin">
          <div class="wrap ls-grid">
            <ol class="ls-steps" aria-label="The layers, from data to decisions">
{chr(10).join(lis)}
            </ol>
            <div class="ls-scene" aria-hidden="true">
              <div class="iso" id="iso">
                <div class="iso-floor"></div>
{chr(10).join(plates)}
              </div>
            </div>
            <p class="ls-more">{more}</p>
            <div class="ls-progress" aria-hidden="true"><i></i></div>
          </div>
        </div>
      </div>"""


LAYERS = [
    ("Data foundation",
     "Sales, orders, inventory and shipments arrive from every connected system and are reconciled into one record, "
     "with listings mapped to products and bundles converted into components. Optional if your data is already usable."),
    ("Inventory intelligence",
     "The records become a model of how your business works, and a planning engine does the math: forecasts, "
     "projections and recommendations computed against your real constraints. Proprietary algorithms, not language models."),
    ("Applications",
     "Ready-to-use apps for demand forecasting, inventory forecasting, replenishment and workflows, or the app you "
     "build yourself on the same layers through MCP and API."),
    ("Reliability and validation",
     "Data health checks, sales history corrected for anomalies, forecast accuracy and bias, and decisions that wait "
     "for your approval. You can see how well it works before you rely on it."),
]


# =====================================================================================
# HOMEPAGE (spec section 7)
# =====================================================================================
def home_main(s):
    return f"""
    <!-- ================= HERO: vision first, both paths above the fold ================= -->
    <section class="hero hero-paths" aria-labelledby="hero-title">
      <div class="wrap">
        <div class="hero-solo">
          <span class="eyebrow"><span class="pulse" aria-hidden="true"></span><span>Inventory software, your way</span></span>
          <h1 class="h1" id="hero-title">Inventory software that works the way you do</h1>
          <p class="lead">Use powerful inventory applications from day one, or build exactly what your business needs on a proven foundation.</p>
        </div>

        <div class="doors">
          <a class="door door-path" href="{{P}}build/">
            <span class="door-num"><span class="ic" aria-hidden="true">{IC_BUILD}</span>Build with Flieber</span>
            <h2>Create software tailored to your business without starting from zero</h2>
            <p>Flieber’s data, inventory logic, app templates and validation tools, through MCP and API. For developers, technical operations teams and anyone building with AI.</p>
            <div class="door-actions"><span class="btn btn-dark">Explore building blocks {ARROW}</span></div>
          </a>
          <a class="door door-path" href="{{P}}run/">
            <span class="door-num"><span class="ic" aria-hidden="true">{IC_RUN}</span>Run with Flieber</span>
            <h2>Put proven forecasting, inventory and replenishment apps to work today</h2>
            <p>Ready-to-use applications for planners and operators, tailored by Flieber’s team when your process needs more. No build project required.</p>
            <div class="door-actions"><span class="btn btn-primary">Explore ready-to-use apps {ARROW}</span></div>
          </a>
        </div>

        <ul class="under-doors">
          <li>{CHECK}Start ready. Make it yours</li>
          <li>{CHECK}One foundation behind both paths</li>
          <li>{CHECK}14-day free trial</li>
          <li>{CHECK}No credit card</li>
        </ul>
      </div>
    </section>

    <!-- ================= PROOF STRIP ================= -->
{pre(s["logos"])}
    <section class="section-tight proof-facts" aria-label="Flieber at a glance">
      <div class="wrap">
        <ul class="founder-facts">
          <li>More than 1,000 commerce brands since 2019</li>
          <li>Thousands of users</li>
          <li>Native integrations with Amazon, Shopify, Walmart, TikTok Shop and more</li>
        </ul>
      </div>
    </section>

    <!-- ================= TWO PATHS, ONE FOUNDATION ================= -->
    <section class="section section-soft" id="two-paths" aria-labelledby="paths-title">
      <div class="wrap">
{head("Two paths, one foundation", "Use it as it comes, or make it entirely yours", "paths-title",
      "Neither path is the real Flieber. Both run on the same data, logic and validation, so you can start with one and move to the other whenever your needs change.")}
        <div class="which reveal-stagger">
          <article class="which-card" aria-labelledby="which-build">
            <h3 class="which-name" id="which-build"><a href="{{P}}build/">Build with Flieber</a></h3>
            <p class="which-tag">Build your inventory software. Start miles ahead</p>
            <h4 class="which-sub">You’re probably here if:</h4>
            <ul class="which-list">
              <li>{TICK}Your team builds its own tools with Claude, Cursor, ChatGPT or code</li>
              <li>{TICK}You need workflows, fields or screens no off-the-shelf app has</li>
              <li>{TICK}You want one reliable inventory foundation to build on</li>
            </ul>
            <p class="which-body"><b>What you get:</b> The data, business logic, working templates and validation tools you need, through MCP and API. Use one layer or all of them, and customize the experience around your business.</p>
            <div class="which-foot">
              <span class="which-price">Start with the data layer alone</span>
              <a class="btn btn-dark" href="{{P}}build/">Explore building blocks {ARROW}</a>
            </div>
          </article>
          <article class="which-card" aria-labelledby="which-run">
            <h3 class="which-name" id="which-run"><a href="{{P}}run/">Run with Flieber</a></h3>
            <p class="which-tag">Inventory planning that’s ready for your reality</p>
            <h4 class="which-sub">You’re probably here if:</h4>
            <ul class="which-list">
              <li>{TICK}You need reliable forecasts, projections and purchase recommendations now</li>
              <li>{TICK}Spreadsheets can’t keep up with your channels, warehouses or suppliers</li>
              <li>{TICK}You’d rather not build or maintain software</li>
            </ul>
            <p class="which-body"><b>What you get:</b> Ready-to-use apps for demand forecasting, inventory forecasting, replenishment and workflows. Add the capabilities you need, and let our team tailor the experience when your process calls for more.</p>
            <div class="which-foot">
              <span class="which-price">14-day free trial</span>
              <a class="btn btn-dark" href="{{P}}run/">Explore ready-to-use apps {ARROW}</a>
            </div>
          </article>
        </div>
        <div class="which-after reveal">
          <p class="which-under">Run customers can ask Flieber to customize their apps without becoming builders. Builders can adopt any working Flieber app. Not sure which fits? Book a demo and we’ll tell you honestly.</p>
        </div>
      </div>
    </section>

    <!-- ================= START WITH A WORKING APPLICATION ================= -->
    <section class="section on-dark" id="apps" aria-labelledby="apps-title">
      <div class="wrap">
{head("Start with a working application", "Value from day one, not after a build project", "apps-title",
      "Each application answers one of the questions every inventory planner asks. Use one, or combine them.")}
        <div class="mq-grid mq-four reveal-stagger">
{mq_cards()}
        </div>
        <p class="link-row reveal"><a class="link-arrow mq-all" href="{{P}}run/">See the applications {ARROW}</a> <a class="link-arrow mq-all" href="{{P}}build/#templates">Or start from an app template {ARROW}</a></p>
      </div>
    </section>

    <!-- ================= WHAT POWERS EVERY EXPERIENCE ================= -->
    <section class="section layerstack-sec" id="foundation" aria-labelledby="stack-title">
      <div class="wrap">
{head("What powers every experience", "Four layers. Use all of them, or only the ones you need", "stack-title",
      "Every Run application is built on these layers, and builders can select each one on its own. Already have clean data, a forecast or your own interface? Bring it.")}
      </div>
{layerstack(LAYERS, '<a class="link-arrow" href="{P}build/">How the layers work for builders ' + ARROW + '</a>')}
    </section>

    <!-- ================= MADE FOR THE WAY YOU OPERATE ================= -->
    <section class="section section-soft" id="your-way" aria-labelledby="way-title">
      <div class="wrap">
{head("Made for the way you operate", "Fit the software to your process, not the other way around", "way-title",
      "Your suppliers, channels and approval rules are specific to your business. Flieber is set up to follow them. What you can adjust depends on the application, and we’ll show you exactly what in a demo.")}
        <div class="feat-grid reveal-stagger">
          <a class="feat-card" href="{{P}}features/#product-configuration-and-classification">
            <h3 class="h3">Fields and structure {ARROW}</h3>
            <p>Listings mapped to one master product, bundles converted into components and products classified the way your team plans them.</p>
            <p class="feat-tag">Configure</p>
          </a>
          <a class="feat-card" href="{{P}}features/#control-and-approval">
            <h3 class="h3">Workflows {ARROW}</h3>
            <p>Approval rules for every change, plus recurring jobs described in plain language that Flieber runs on schedule.</p>
            <p class="feat-tag">Configure</p>
          </a>
          <a class="feat-card" href="{{P}}features/#reports-and-dashboards">
            <h3 class="h3">Layouts and reports {ARROW}</h3>
            <p>Your own dashboards with live alerts and scheduled delivery, or a frontend designed around your business by Flieber’s engineers.</p>
            <p class="feat-tag">Configure or customize</p>
          </a>
          <a class="feat-card" href="{{P}}features/#planning-parameters">
            <h3 class="h3">Calculations {ARROW}</h3>
            <p>Safety stock, target days of cover, lead times, MOQs, case packs and container rules, by product, category and channel.</p>
            <p class="feat-tag">Configure</p>
          </a>
        </div>
      </div>
    </section>

    <!-- ================= FROM READY-MADE TO UNIQUELY YOURS ================= -->
    <section class="section" id="customize" aria-labelledby="yours-title">
      <div class="wrap">
{head("From ready-made to uniquely yours", "Customize it yourself, or have us do it", "yours-title",
      "You don’t have to become a software team to get software that fits. And if you are one, you don’t have to start from scratch.")}
        <div class="collab reveal-stagger">
          <article class="collab-card">
            <div class="collab-top"><span class="collab-ic">{IC_TEAM}</span><span class="collab-step">Run</span></div>
            <h3 class="h3">Use it as it comes</h3>
            <p>Start with the Flieber app, configure your parameters and plan. Standard setup is included.</p>
          </article>
          <article class="collab-card">
            <div class="collab-top"><span class="collab-ic">{IC_CODE}</span><span class="collab-step">Build</span></div>
            <h3 class="h3">Build it yourself</h3>
            <p>Vibe code reports, dashboards and agents with Claude, Cursor or ChatGPT on data that’s already unified, mapped and corrected.</p>
          </article>
          <article class="collab-card">
            <div class="collab-top"><span class="collab-ic">{IC_PERSON}</span><span class="collab-step">Run or Build</span></div>
            <h3 class="h3">Have Flieber build it</h3>
            <p>Flieber’s engineers build what your business needs, up to a tailored frontend. Flieber’s planners can join your team too.</p>
          </article>
        </div>
        <p class="collab-under reveal"><a href="{{P}}customize/"><span>See how customization works, and what it costs</span> {ARROW}</a></p>
      </div>
    </section>

    <!-- ================= TRUST AND OPERATIONAL ACCURACY ================= -->
    <section class="section section-soft" id="proof" aria-labelledby="proof-title">
      <div class="wrap">
{head("Trust and operational accuracy", "Accuracy you can check, not just a claim", "proof-title",
      "Planning decisions are only as good as the data and logic behind them. Flieber shows both.")}
        <ul class="sec-strip reveal-stagger">
          <li><span class="sec-ic" aria-hidden="true">{IC_HEALTH}</span><h3>Data health checks</h3><p>Issues, gaps and anomalies flagged, and fixed where possible, before anything is planned on them.</p></li>
          <li><span class="sec-ic" aria-hidden="true">{IC_CHART}</span><h3>History you can see through</h3><p>Sales corrected for stockouts, spikes and promotions, shown next to what actually sold.</p></li>
          <li><span class="sec-ic" aria-hidden="true">{IC_SHIELD}</span><h3>Accuracy measured</h3><p>Error and bias tracked, with monthly forecast versions saved to compare with actual sales.</p></li>
          <li><span class="sec-ic" aria-hidden="true">{IC_APPROVE}</span><h3>Decisions under your rules</h3><p>Every change waits for your approval until you set a workflow to run on its own.</p></li>
        </ul>
        <div class="proof-gap"></div>
{s["results"]}{s["quotes"]}      </div>
    </section>

    <!-- ================= FINAL CTA ================= -->
    <section class="section try" id="start" aria-labelledby="start-title">
      <div class="wrap" style="position:relative">
{head("Get started", "Find the right starting point", "start-title",
      "Two ways in, one foundation underneath. Choose the one that fits today.")}
        <div class="try-grid reveal-stagger">
          <a class="try-card dark try-link" href="{{P}}build/">
            <span class="label"><i aria-hidden="true"></i>Build with Flieber</span>
            <p style="margin-top:14px">I want to build or customize my own inventory software on a proven foundation.</p>
            <span class="on-dark-link">Explore building blocks {ARROW}</span>
          </a>
          <a class="try-card try-link" href="{{P}}run/">
            <span class="label"><i aria-hidden="true"></i>Run with Flieber</span>
            <p style="margin-top:14px">I want forecasting, inventory and replenishment software that works now.</p>
            <span class="try-go">Explore ready-to-use apps {ARROW}</span>
          </a>
        </div>
        <div class="try-actions reveal">
          <a class="btn btn-primary" href="{TRIAL}">Start free trial {ARROW}</a>
          <a class="btn btn-ghost" href="{DEMO}">Book a demo</a>
        </div>
      </div>
    </section>
"""


# =====================================================================================
# BUILD OVERVIEW (spec section 8)
# =====================================================================================
def build_main(s):
    return f"""
    <section class="page-head sol-head" aria-labelledby="page-title">
      <div class="wrap">
        <div class="section-head">
          <span class="kicker">Build with Flieber</span>
          <h1 class="h1" id="page-title">Build your inventory software. Start miles ahead</h1>
          <p class="lead">Use proven inventory data structures, business logic, working apps and validation tools, then customize what matters. Connect Claude, Cursor, ChatGPT or your own code through Flieber’s MCP server and public API.</p>
        </div>
        <div class="sol-actions">
          <a class="btn btn-primary" href="#templates">Explore templates {ARROW}</a>
          <a class="btn btn-ghost" href="{DEV_DOCS}">View developer docs</a>
        </div>
        <ul class="under-doors">
          <li>{CHECK}Use any layer on its own</li>
          <li>{CHECK}Start with the data layer alone</li>
          <li>{CHECK}Build it yourself or with our engineers</li>
        </ul>
      </div>
    </section>

    <section class="section section-soft" id="why-build" aria-labelledby="why-title">
      <div class="wrap">
{head("Your business is unique", "Your inventory software can be too, without rebuilding the hard parts", "why-title",
      "Vibe coding the dashboard is the easy part. Keeping the data under it right never ends: every new channel, warehouse or supplier changes the data, and every change breaks something downstream. Flieber keeps that layer right, so your team can spend its time on the tools only you can build.")}
        <div class="why-grid reveal-stagger">
          <article class="why-card"><span class="n">01</span><h3 class="h3">Skip the plumbing</h3><p>Every source connected through native and assisted integrations, so you don’t rebuild connectors, mapping and normalization for each new tool.</p></article>
          <article class="why-card"><span class="n">02</span><h3 class="h3">Start from correct inventory logic</h3><p>Stockout-corrected demand, bundles, routing, lead times and open purchase orders, already worked out by a planning engine shaped by more than 1,000 brands.</p></article>
          <article class="why-card"><span class="n">03</span><h3 class="h3">Check what you build</h3><p>Data health, forecast accuracy and decision tools show where a custom tool drifts from reality.</p></article>
        </div>
      </div>
    </section>

    <section class="section" id="how-a-build-works" aria-labelledby="flow-title">
      <div class="wrap">
{head("A typical build", "From raw data to a working app in four steps", "flow-title")}
        <ol class="mcp-steps reveal">
          <li class="mcp-step"><span class="n">1</span><p><b>Connect or bring your data.</b> Use Flieber’s integrations, or bulk upload catalog, forecasts, shipments and wholesale data.</p></li>
          <li class="mcp-step"><span class="n">2</span><p><b>Apply inventory intelligence.</b> Business context and the planning engine turn records into demand, projections and recommendations.</p></li>
          <li class="mcp-step"><span class="n">3</span><p><b>Start from a working app.</b> Use a Flieber app as is, start from a template or build your own through MCP and API.</p></li>
          <li class="mcp-step"><span class="n">4</span><p><b>Validate and ship.</b> Check data health, forecast accuracy and decisions against what actually happened.</p></li>
        </ol>
        <p class="link-row reveal"><a class="link-arrow" href="{{P}}mcp/">Connect in minutes: the full guide on /mcp {ARROW}</a></p>
      </div>
    </section>

    <section class="section on-dark" id="layers" aria-labelledby="layers-title">
      <div class="wrap">
{head("Four independent capabilities", "Take what you need. Leave what you don’t", "layers-title",
      "Each layer can be selected on its own. Some combinations need specific inputs, and we publish what each one requires rather than claiming everything works with everything.")}
        <div class="mq-grid mq-four reveal-stagger">
          <a class="mq-card" href="{{P}}build/data/"><span class="mq-mod"><span class="n">01</span>Data foundation</span><h3 class="mq-q">Connectors, mapping and ingestion</h3><p>Optional if you already have usable data. Available on its own.</p><span class="mq-go">Data foundation {ARROW}</span></a>
          <a class="mq-card" href="#intelligence"><span class="mq-mod"><span class="n">02</span>Inventory intelligence</span><h3 class="mq-q">The domain model and the math</h3><p>Runs on Flieber data or qualified data you provide.</p><span class="mq-go">Inventory intelligence {ARROW}</span></a>
          <a class="mq-card" href="#templates"><span class="mq-mod"><span class="n">03</span>App templates</span><h3 class="mq-q">Working starting points</h3><p>Use, fork or borrow ideas. Requirements depend on the app.</p><span class="mq-go">App templates {ARROW}</span></a>
          <a class="mq-card" href="#reliability"><span class="mq-mod"><span class="n">04</span>Reliability and validation</span><h3 class="mq-q">Checks for data, forecasts and decisions</h3><p>For Flieber or eligible external workflows.</p><span class="mq-go">Reliability {ARROW}</span></a>
        </div>
      </div>
    </section>

    <section class="section" id="data" aria-labelledby="data-title">
      <div class="wrap">
{head("01 · Data foundation", "Your commerce data, consolidated, contextualized and current", "data-title",
      "Every report, forecast and agent is only as good as the data under it. The data layer connects every channel, warehouse, 3PL and supplier, adds the business context none of them hold and keeps it up to date.")}
        <div class="feat-grid reveal-stagger">
          <a class="feat-card" href="{{P}}features/#data-health"><h3 class="h3">Data health {ARROW}</h3><p>Checks your account for issues, gaps and anomalies, applies the fixes it can and flags the ones that need a person.</p><p class="feat-tag">Read and write</p></a>
          <a class="feat-card" href="{{P}}features/#cross-channel-sku-mapping"><h3 class="h3">Cross-channel SKU mapping {ARROW}</h3><p>Links listings and SKUs across channels to one master product, so sales consolidate for planning.</p><p class="feat-tag">Write</p></a>
          <a class="feat-card" href="{{P}}features/#kits-bundles-and-components"><h3 class="h3">Kits, bundles and components {ARROW}</h3><p>Bundle demand converted into component requirements, so you can buy components and transfer finished goods.</p><p class="feat-tag">Write</p></a>
          <a class="feat-card" href="{{P}}features/#uploads-and-google-sheets"><h3 class="h3">Bring your own data {ARROW}</h3><p>Bulk updates to catalog, forecasts, shipments, bundles and wholesale data through CSV files or Google Sheets, with a preview before anything is saved. Direct connection to your own warehouse: {todo("CONFIRM BRING-YOUR-OWN-WAREHOUSE SUPPORT")}</p><p class="feat-tag">Write</p></a>
        </div>
        <p class="link-row reveal"><a class="link-arrow" href="{{P}}build/data/">Everything in the data foundation {ARROW}</a> <a class="link-arrow" href="{{P}}integrations/">Supported data sources {ARROW}</a></p>
      </div>
    </section>

    <section class="section section-soft" id="intelligence" aria-labelledby="intel-title">
      <div class="wrap">
{head("02 · Inventory intelligence", "Raw transactions in. Decisions you can trust out", "intel-title",
      "Business context turns records into a model of how your business works: which listings are the same product, which components make a bundle, which supplier ships to which warehouse and what a stockout did to last month’s sales. The planning engine then does the math with proprietary algorithms, not language models.")}
        <div class="intel-grid reveal">
          <div>
            <h3 class="h3 cz-sub" style="margin-top:0">A worked example</h3>
            <p class="muted">Will this SKU make it to its next purchase order?</p>
            <div class="table-wrap" style="margin-top:18px">
              <table class="doc-table intel-table">
                <thead><tr><th scope="col">Step</th><th scope="col">Value</th></tr></thead>
                <tbody>
                  <tr><th scope="row">On hand today</th><td>412 units</td></tr>
                  <tr><th scope="row">Daily demand, corrected for stockouts</th><td>18.4 units</td></tr>
                  <tr><th scope="row">Open PO-1187 arrives in</th><td>22 days, 600 units</td></tr>
                  <tr><th scope="row">Demand until the PO lands</th><td>405 units</td></tr>
                  <tr><th scope="row">Projected on hand when it lands</th><td>7 units</td></tr>
                  <tr class="hl"><th scope="row">Stockout risk</th><td>High: under half a day of cover</td></tr>
                </tbody>
              </table>
            </div>
            <p class="intel-note">Sample data. Illustrative only.</p>
          </div>
          <div class="intel-edges">
            <h3 class="h3 cz-sub" style="margin-top:0">Edge cases it already handles</h3>
            <ul class="which-list">
              <li>{TICK}Sales history corrected for stockouts, spikes and promotions, so demand isn’t underestimated</li>
              <li>{TICK}Bundle demand converted into component requirements</li>
              <li>{TICK}Sales orders routed to the regions or warehouses you choose</li>
              <li>{TICK}MOQs, case packs, cartons, pallets and container capacity</li>
              <li>{TICK}Backorders and preorders, and wholesale demand parked on dates that passed</li>
            </ul>
            <p class="link-row"><a class="link-arrow" href="{{P}}features/">Every calculation, by module {ARROW}</a></p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="templates" aria-labelledby="tpl-title">
      <div class="wrap">
{head("03 · App templates", "Start from an app that works. Make it yours", "tpl-title",
      "Functional starting points for specific inventory jobs. Use them as they are, fork them or borrow ideas. Each template lists what it does, what it needs and how ready it is. Production-ready and experimental templates are labeled separately.")}
        <div class="mod-grid tpl-grid reveal-stagger">
          <article class="mod-card tpl-card"><span class="tpl-status">{todo("IN PREPARATION")}</span><h3 class="h3">Inventory projection app</h3><p>Project inventory by SKU and location, including open purchase orders, and flag stockout and overstock risk.</p><p class="tpl-needs"><b>Needs:</b> inventory positions, demand or forecast, open POs</p></article>
          <article class="mod-card tpl-card"><span class="tpl-status">{todo("IN PREPARATION")}</span><h3 class="h3">Replenishment planner</h3><p>Turn projections and lead times into purchase recommendations with a review and approval step.</p><p class="tpl-needs"><b>Needs:</b> projection output, lead times, MOQs</p></article>
          <article class="mod-card tpl-card"><span class="tpl-status">{todo("IN PREPARATION")}</span><h3 class="h3">Forecast accuracy monitor</h3><p>Backtest any forecast, Flieber’s or yours, and track error by SKU, channel and horizon.</p><p class="tpl-needs"><b>Needs:</b> historical forecasts and actual sales</p></article>
          <article class="mod-card tpl-card"><span class="tpl-status">{todo("IN PREPARATION")}</span><h3 class="h3">Wholesale order check</h3><p>Check every new wholesale order against Amazon and Shopify stock before you accept it.</p><p class="tpl-needs"><b>Needs:</b> wholesale orders, channel inventory</p></article>
        </div>
        <p class="tpl-license reveal">Open source, with live preview, repository, version and customization guide on every template: {todo("LICENSE, REPOSITORIES AND RELEASE DATES")}</p>
        <h3 class="h3 cz-sub reveal">What teams build today on Flieber’s data</h3>
        <ul class="uc-asks reveal">
          <li>“A morning dashboard of stockout risk by channel, refreshed every day.”</li>
          <li>“An agent that checks every new wholesale order against Amazon and Shopify stock.”</li>
          <li>“A weekly cash-flow view of open purchase orders and projected inventory value.”</li>
          <li>“A Slack alert when ad spend rises on a product projected to stock out.”</li>
        </ul>
        <p class="link-row reveal"><a class="btn btn-ghost" href="{DEMO}">Get early access to templates {ARROW}</a></p>
      </div>
    </section>

    <section class="section section-soft" id="reliability" aria-labelledby="rel-title">
      <div class="wrap">
{head("04 · Reliability and validation", "Check every output before it reaches a decision", "rel-title",
      "Validation shows how well things are working and where they aren’t. It doesn’t make anything guaranteed correct, and no tool can.")}
        <div class="feat-grid reveal-stagger">
          <a class="feat-card" href="{{P}}features/#data-health"><h3 class="h3">Data health and freshness {ARROW}</h3><p>Issues, gaps and anomalies in every connected source, fixed where possible and flagged where a person is needed.</p><p class="feat-tag">Data quality</p></a>
          <a class="feat-card" href="{{P}}features/#sales-history-adjusted-for-anomalies"><h3 class="h3">Adjusted history, side by side {ARROW}</h3><p>Actual sales next to the adjusted demand used for forecasting, so every correction can be checked.</p><p class="feat-tag">Data quality</p></a>
          <a class="feat-card" href="{{P}}features/#forecast-accuracy-and-bias"><h3 class="h3">Forecast accuracy and bias {ARROW}</h3><p>Error and bias metrics, with monthly forecast versions saved so past predictions can be compared with what actually sold.</p><p class="feat-tag">Forecast accuracy</p></a>
          <a class="feat-card" href="{{P}}features/#decision-simulations"><h3 class="h3">Decision simulations {ARROW}</h3><p>Test changes to order quantities, demand, arrival dates or lead times and see the effect on inventory, revenue, margin and cash before anything is committed.</p><p class="feat-tag">Decisions</p></a>
          <a class="feat-card" href="{{P}}features/#control-and-approval"><h3 class="h3">Approval rules {ARROW}</h3><p>Nothing changes in your systems without passing the approval rules you set.</p><p class="feat-tag">Decisions</p></a>
          <a class="feat-card" href="{{P}}features/#inventory-history-and-balances"><h3 class="h3">Inventory history and balances {ARROW}</h3><p>Snapshots and balances across every connected location, including inbound and in-transit stock, to compare projections with what was on hand.</p><p class="feat-tag">Output auditing</p></a>
        </div>
      </div>
    </section>

    <section class="section" id="services" aria-labelledby="svc-title">
      <div class="wrap">
{head("Build it yourself, or hire Flieber", "Choose how much you want to build", "svc-title",
      "Self-serve on Flieber’s layers, or have Flieber’s engineers build it with you. We agree on what you own, what Flieber hosts and what support is included before work starts.")}
        <div class="sol-two reveal-stagger">
          <a class="sol-card" href="{{P}}customize/#yourself">
            <span class="n">01</span>
            <h3 class="h3">Build it yourself</h3>
            <p>Vibe code your own tools on data that’s already unified, mapped and corrected. Start with a 14-day free trial on your own data.</p>
            <span class="sol-go">Build it yourself {ARROW}</span>
          </a>
          <a class="sol-card" href="{{P}}customize/#engineers">
            <span class="n">02</span>
            <h3 class="h3">Have our engineers build it</h3>
            <p>Custom dashboards, tailored frontends, integrations, agents and workflows. Quoted per project, for qualified accounts.</p>
            <span class="sol-go">Have our engineers build it {ARROW}</span>
          </a>
        </div>
        <p class="tpl-license reveal">Code ownership, hosting and maintenance terms for each model: {todo("CONFIRM OWNERSHIP AND SUPPORT TERMS")}</p>
      </div>
    </section>

    <section class="section section-soft" id="faq" aria-labelledby="faq-title">
      <div class="wrap">
{head("Questions builders ask", "The usual ones, answered plainly", "faq-title")}
        <div class="faq reveal">
{faq([
    ("Our AI can write this. Why use Flieber?", "AI is very good at writing interfaces and glue code. It is much less reliable at inventory logic, such as stockout-corrected demand, bundles, open-PO timing and lead times, and it won’t keep your integrations running. Flieber gives your builders those parts already working, so the code you write sits on something reliable."),
    ("Can I buy only the data layer?", "Yes. Teams building their own tools with AI can use Flieber’s data layer on its own through MCP and API, and add the other modules any time."),
    ("Do I have to use Flieber’s connectors?", "No. If your data is already usable, bring it in through CSV files or Google Sheets, or import your own forecasts. Direct connection to your own data warehouse: " + todo("CONFIRM BRING-YOUR-OWN-WAREHOUSE SUPPORT")),
    ("Can my own AI agent use Flieber?", "Yes. Claude, Cursor and any MCP-compatible agent connect through Flieber’s MCP server; your systems can also use the public API."),
    ("Will Flieber change anything without my approval?", "Not by default. Every change waits for your approval until you set a workflow to run on its own."),
    ("Am I locked in?", "The layers are selected independently and your data is never sold or shared. Data access and portability are covered in technical discovery. " + todo("CONFIRM EXPORT AND PORTABILITY TERMS")),
])}
        </div>
      </div>
    </section>

    <section class="section try" id="next" aria-labelledby="next-title">
      <div class="wrap" style="position:relative">
{head("Next step", "Start building on your own data", "next-title",
      "Start a 14-day free trial, no credit card required, or talk to an expert about what you want to build. Prefer ready-made? <a href=\"{P}run/\">See Run with Flieber</a>.")}
        <div class="try-actions">
          <a class="btn btn-primary" href="{TRIAL}">Start free trial {ARROW}</a>
          <a class="btn btn-ghost" href="{DEMO}">Talk to an expert</a>
          <a class="btn btn-ghost" href="{DEV_DOCS}">View developer docs</a>
        </div>
      </div>
    </section>
"""


# =====================================================================================
# RUN OVERVIEW (spec section 9.1)
# =====================================================================================
def run_main(s):
    return f"""
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap">
        <div class="hero-top">
          <div class="hero-copy">
            <span class="eyebrow"><span class="pulse" aria-hidden="true"></span><span>Run with Flieber</span></span>
            <h1 class="h1" id="hero-title">Inventory planning that’s ready for your reality</h1>
            <p class="lead">Get reliable forecasts, inventory visibility and replenishment recommendations without building from scratch.</p>
            <div class="sol-actions" style="margin-top:32px">
              <a class="btn btn-primary" href="#apps">See the applications {ARROW}</a>
              <a class="btn btn-ghost" href="{DEMO}">Book a demo</a>
            </div>
          </div>
{s["sim"]}        </div>
        <ul class="under-doors">
          <li>{CHECK}No code required</li>
          <li>{CHECK}14-day free trial</li>
          <li>{CHECK}Monthly contracts</li>
          <li>{CHECK}Setup included</li>
        </ul>
      </div>
    </section>

    <section class="section section-soft" id="problems" aria-labelledby="why-title">
      <div class="wrap">
        <div class="why-head reveal">
          <div>
            <span class="kicker">Common operating problems</span>
            <h2 class="h2" id="why-title" style="margin-top:20px">Purchases, promotions, ads, financing: every one is ultimately an inventory decision</h2>
          </div>
          <p class="lead">Stockouts, excess inventory, spreadsheets at their limit, forecasts nobody trusts. For most product brands inventory is the biggest use of cash, and getting it wrong costs more than almost any other mistake.</p>
        </div>
{s["why"]}      </div>
    </section>

    <section class="section on-dark" id="apps" aria-labelledby="apps-title">
      <div class="wrap">
{head("The applications", "Ready-to-use apps for every part of planning", "apps-title",
      "Start with the job that hurts most. Add more when you’re ready.")}
        <div class="mq-grid mq-four reveal-stagger">
{mq_cards()}
        </div>
        <p class="link-row reveal"><a class="link-arrow mq-all" href="{{P}}features/">See every feature {ARROW}</a></p>
      </div>
    </section>

    <section class="section" id="end-to-end" aria-labelledby="e2e-title">
      <div class="wrap">
{head("End to end", "From forecast to purchase order, connected", "e2e-title",
      "Each application works on its own. Used together, each one feeds the next.")}
        <ol class="mcp-steps reveal">
          <li class="mcp-step"><span class="n">1</span><p><b>Forecast.</b> Demand for every product on every channel, corrected for stockouts and promotions.</p></li>
          <li class="mcp-step"><span class="n">2</span><p><b>Project.</b> Stockouts, overstock and lost sales by product and location.</p></li>
          <li class="mcp-step"><span class="n">3</span><p><b>Replenish.</b> Purchase and transfer recommendations within MOQs, case packs, lead times and cash.</p></li>
          <li class="mcp-step"><span class="n">4</span><p><b>Act.</b> Approved decisions carried into suppliers, ERPs, Amazon and 3PLs.</p></li>
        </ol>
      </div>
    </section>

    <section class="section section-soft" id="what-you-need" aria-labelledby="need-title">
      <div class="wrap">
{head("Start with what you need", "One app or several. Your call", "need-title",
      "You don’t have to adopt everything at once. Some apps need inputs that others provide. Replenishment, for example, needs demand assumptions, which can come from Flieber’s forecast or from your own. We confirm the right combination for your business during your demo.")}
        <dl class="kv reveal">
          <dt>“We need to trust our forecast first”</dt><dd><a href="{{P}}run/forecasting/">Demand forecasting</a></dd>
          <dt>“We have a forecast, but keep stocking out”</dt><dd><a href="{{P}}run/inventory/">Inventory forecasting</a> and <a href="{{P}}run/replenishment/">Replenishment</a></dd>
          <dt>“POs take us days to build”</dt><dd><a href="{{P}}run/replenishment/">Replenishment</a></dd>
          <dt>“Approvals and handoffs are chaos”</dt><dd><a href="{{P}}run/workflows/">Workflows</a></dd>
        </dl>
      </div>
    </section>

    <section class="section" id="implementation" aria-labelledby="impl-title">
      <div class="wrap">
{head("Implementation", "Up and running without a build project", "impl-title",
      "You don’t need engineers. Connect your channels, set your key parameters and Flieber starts working. Standard setup is included.")}
        <div class="try-grid reveal-stagger">
          <div class="try-card dark">
            <span class="label"><i aria-hidden="true"></i>During the trial</span>
            <p style="margin-top:14px">Connect your channels through native integrations (Amazon Seller Central, Shopify, Walmart, TikTok Shop, eBay, Etsy, BigCommerce, Google Sheets). Standard setup included.</p>
          </div>
          <div class="try-card">
            <span class="label"><i aria-hidden="true"></i>On a paid plan</span>
            <p style="margin-top:14px">Assisted integrations and simple customizations, set up by Flieber’s team.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-soft" id="proof" aria-labelledby="proof-title">
      <div class="wrap">
{head("Proof", "What brands get when people and AI plan together", "proof-title")}
{s["results"]}{s["quotes"]}      </div>
    </section>

    <section class="section" id="customize" aria-labelledby="cust-title">
      <div class="wrap">
{head("Customization, handled by Flieber", "When your process needs more, we tailor it", "cust-title",
      "Your team doesn’t need to become builders. Tell us what’s different about how you work, and Flieber adapts the application.")}
        <div class="collab reveal-stagger">
          <article class="collab-card">
            <div class="collab-top"><span class="collab-ic">{IC_TEAM}</span><span class="collab-step">On a paid plan</span></div>
            <h3 class="h3">Simple customizations</h3>
            <p>Assisted integrations and simple customizations, set up by Flieber’s team.</p>
          </article>
          <article class="collab-card">
            <div class="collab-top"><span class="collab-ic">{IC_PERSON}</span><span class="collab-step">Managed Services</span></div>
            <h3 class="h3">Flieber’s planners</h3>
            <p>Specialists who master Flieber, keep the data behind your decisions accurate and join your S&amp;OP meetings. Quoted per brand.</p>
          </article>
          <article class="collab-card">
            <div class="collab-top"><span class="collab-ic">{IC_CODE}</span><span class="collab-step">Quoted per project</span></div>
            <h3 class="h3">Flieber’s engineers</h3>
            <p>Views, fields and screens adjusted to how your team plans, custom reports, integrations and agents, up to a tailored frontend.</p>
          </article>
        </div>
        <p class="collab-under reveal"><a href="{{P}}managed-services/"><span>Managed Services</span> {ARROW}</a> <a href="{{P}}customize/#engineers"><span>Custom builds by our engineers</span> {ARROW}</a></p>
      </div>
    </section>

    <section class="section section-soft" id="faq" aria-labelledby="faq-title">
      <div class="wrap">
{head("Questions planners ask", "The usual ones, answered plainly", "faq-title")}
        <div class="faq reveal">
{faq([
    ("How much effort is implementation?", "Standard setup is included: connect your sales channels and warehouses, configure your key parameters and Flieber starts working. You don’t need engineers. Assisted integrations and simple customizations come with a paid plan."),
    ("Will it cover our use case?", "Flieber plans finished-goods inventory across channels, warehouses and suppliers, including kits, bundles, backorders, preorders and wholesale. If your process needs something specific, Flieber’s team can tailor it. We’ll tell you plainly what’s standard and what isn’t."),
    ("How steep is the learning curve?", "The apps follow familiar planning tasks: reviewing forecasts, checking projected stock and approving orders. You can also ask Flieber questions in plain language, in the app or in Slack."),
    ("How is it priced?", "Flieber Self-Serve is priced on the features you enable and your data volume, and shows your price as soon as onboarding is done, before you pay anything. Managed Services is quoted per brand. Contracts are monthly."),
    ("Will it fit our existing process?", "Planning parameters, approval rules and reports are configurable, and Flieber connects to your ERP, 3PLs and suppliers. Flieber plans finished-goods inventory and connects to your WMS, ERP or MRP; it doesn’t replace them."),
])}
        </div>
      </div>
    </section>

    <section class="section try" id="next" aria-labelledby="next-title">
      <div class="wrap" style="position:relative">
{head("Next step", "See it on your own planning problems", "next-title",
      "Book a demo built around the jobs you care about, or start a 14-day free trial, no credit card required. Building your own tools? <a href=\"{P}build/\">See Build with Flieber</a>.")}
        <div class="try-actions">
          <a class="btn btn-primary" href="{DEMO}">Book a demo {ARROW}</a>
          <a class="btn btn-ghost" href="{TRIAL}">Start free trial</a>
        </div>
      </div>
    </section>
"""


# =====================================================================================
# RUN APPLICATION PAGES (spec section 9.2): additions to Option 2's module pages
# =====================================================================================
APPS = {
    "forecasting": dict(
        user="Demand planners, inventory planners and supply chain leaders",
        jobs=[("Forecast at the level you plan", "Every product on every channel, across marketplaces, DTC and wholesale, built from adjusted history and seasonality."),
              ("Know how much to trust it", "Error and bias tracked over time, with monthly forecast versions saved to compare with what actually sold."),
              ("Add what only your team knows", "Adjust for a retailer’s promotion, a launch date or a target, at SKU, store, channel or group level.")],
        inputs=[("Required", "Sales history by product and channel, from connected channels or uploads"),
                ("Improves it", "Stockout history, planned promotions and events, product relationships"),
                ("Optional", "Your own forecast, imported to use or compare")],
        outputs=[("Forecasts", "Demand by product, channel and period"),
                 ("Accuracy", "Error and bias by product, with saved monthly versions"),
                 ("Feeds", "Inventory forecasting and replenishment")],
        accuracy="36% more accurate than our previous portfolio of 16 forecasting models, tested on a random sample of 46,000 products. Built with Nixtla, the team behind the TimeGPT forecasting model. Accuracy for your own products is measured continuously once you’re live.",
        faq=[("Can I use my own forecast?", "Yes. Import your own forecasts, or adjust Flieber’s at SKU, store, channel or group level."),
             ("Does Flieber correct sales history for stockouts?", "Yes. History distorted by stockouts, spikes and promotions is corrected, and actual sales are shown next to the adjusted demand."),
             ("How accurate will it be for us?", "It depends on your products and data, and no forecast is perfect. Flieber measures error and bias continuously and shows them to you.")]),
    "inventory": dict(
        user="Inventory planners, supply chain leaders and commerce operators",
        jobs=[("See projected inventory", "By product and location, including inbound and in-transit stock."),
              ("Catch stockouts early", "Know which products will run out, where and when, while there’s still time to act."),
              ("Find excess before it ages", "Spot overstock and the cash tied up in it, and slow orders or move stock.")],
        inputs=[("Required", "Inventory positions by location from connected warehouses, 3PLs and channels"),
                ("Required", "Demand assumptions: Flieber’s forecast or your own"),
                ("Improves it", "Open purchase orders, inbound shipments, transfers, backorders and preorders")],
        outputs=[("Projections", "On-hand inventory by product, location and period"),
                 ("Exposure", "Stockouts, overstock and lost sales, with timing"),
                 ("Feeds", "Replenishment and alerts")],
        accuracy="Every projection can be traced to its inputs: on hand, demand and inbound supply. Inventory history and balances are kept for every connected location, so projections can be compared with what was actually on hand.",
        faq=[("Can I use my own forecast?", "Yes. Inventory forecasting can run on an imported demand forecast instead of Flieber’s."),
             ("Does it handle several warehouses and channels?", "Yes. Projections are calculated by product and location across every connected warehouse, 3PL and channel."),
             ("Does it handle backorders and preorders?", "Yes, they are part of the projection.")]),
    "replenishment": dict(
        user="Inventory planners, buyers and supply chain leaders",
        jobs=[("Get recommended quantities", "Purchase and transfer recommendations within MOQs, case packs, lead times and cash."),
              ("Order at the right time", "Recommendations follow your lead times, order frequency and target days of cover."),
              ("Test before you commit", "Simulate changes to quantities, demand, arrival dates or lead times and see the effect on inventory, revenue, margin and cash.")],
        inputs=[("Required", "Inventory state and open purchase orders"),
                ("Required", "Demand assumptions: Flieber’s forecast or your own"),
                ("Required", "Supply parameters: lead times, MOQs, case packs, safety stock")],
        outputs=[("Recommendations", "What to buy or move, how much and when"),
                 ("Simulations", "Impact on inventory, revenue, margin and cash"),
                 ("Plans", "Saved plans and draft purchase orders for approval")],
        accuracy="Decision simulations show the effect of a recommendation before anything is committed, and every change waits for your approval until you set a workflow to run on its own.",
        faq=[("Will it place orders automatically?", "Not by default. Recommendations wait for your approval, and approved orders can be sent to suppliers or to NetSuite and light ERPs such as Cin7 and Brightpearl."),
             ("Does it account for MOQs, case packs and containers?", "Yes. Minimum order quantities, rounding to case packs, cartons or pallets and container planning are part of the recommendation."),
             ("Does it plan Amazon FBA replenishment?", "Yes. It recommends transfers from warehouses or 3PLs to FBA, creates the inbound shipments in Amazon and tracks them to delivery.")]),
    "workflows": dict(
        user="Planning teams, operations leads and finance approvers",
        jobs=[("Carry out approved decisions", "Purchase orders to suppliers and ERPs, inbound shipments in Amazon and 3PLs, tracked to delivery."),
              ("Watch and alert", "Alerts and scheduled reports that flag only what needs a person."),
              ("Automate recurring jobs", "Describe a recurring job in plain language and Flieber runs it on schedule, across its own data and your connected apps.")],
        inputs=[("Required", "Decisions from Flieber’s other modules, or your own"),
                ("Required", "Your approval rules"),
                ("Depends on the workflow", "Connected systems: suppliers, ERPs, Amazon, 3PLs, Slack and any system with an MCP server")],
        outputs=[("Actions", "POs sent, shipments created, updates in other systems"),
                 ("Alerts", "Scheduled checks and reports"),
                 ("Record", "Who approved what, and when")],
        accuracy="Nothing changes in your systems without passing the approval rules you set. You decide how much runs on its own; by default, every change waits for your approval.",
        faq=[("Will Flieber change anything without my approval?", "Not by default. Every change waits for your approval until you set a workflow to run on its own."),
             ("Can it send purchase orders to my ERP?", "Yes, to NetSuite and to light ERPs such as Cin7 and Brightpearl."),
             ("Can Flieber build a workflow specific to us?", "Yes. Describe it in plain language, or have Flieber’s engineers build custom agents and workflows for your process.")]),
}


def app_extra(slug):
    a = APPS[slug]
    jobs = "\n".join(f'          <article class="why-card"><span class="n">0{i}</span><h3 class="h3">{t}</h3><p>{d}</p></article>'
                     for i, (t, d) in enumerate(a["jobs"], 1))

    def kv(rows):
        return "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    return dict(
        built_for=f'      <div class="wrap"><p class="built-for"><b>Built for:</b> {a["user"]}</p></div>',
        jobs=f"""    <section class="section" id="jobs" aria-labelledby="jobs-title">
      <div class="wrap">
{head("What it does for you", "Three jobs, done well", "jobs-title")}
        <div class="why-grid reveal-stagger">
{jobs}
        </div>
      </div>
    </section>
""",
        io=f"""    <section class="section" id="inputs-outputs" aria-labelledby="io-title">
      <div class="wrap">
{head("Inputs and outputs", "What goes in, and what you get out", "io-title")}
        <div class="io-grid reveal-stagger">
          <div><h3 class="h3 cz-sub" style="margin-top:0">Inputs and integrations</h3><dl class="kv">{kv(a["inputs"])}</dl></div>
          <div><h3 class="h3 cz-sub" style="margin-top:0">Outputs and decisions</h3><dl class="kv">{kv(a["outputs"])}</dl></div>
        </div>
        <p class="link-row reveal"><a class="link-arrow" href="{{P}}integrations/">Supported integrations {ARROW}</a></p>
      </div>
    </section>
""",
        accuracy=f"""    <section class="section" id="accuracy" aria-labelledby="acc-title">
      <div class="wrap">
{head("Performance and accuracy", "How you know it’s working", "acc-title", a["accuracy"])}
      </div>
    </section>
""",
        customize=f"""    <section class="section" id="customize" aria-labelledby="cust-title">
      <div class="wrap">
{head("Customization options", "Configured for you, or tailored by our team", "cust-title",
      "Planning parameters, approval rules and reports are configurable. When your process needs more, Flieber’s team can tailor the app, with no code from your side.")}
        <p class="link-row reveal"><a class="link-arrow" href="{{P}}customize/#engineers">Customizations by Flieber’s engineers {ARROW}</a> <a class="link-arrow" href="{{P}}managed-services/">Managed Services {ARROW}</a> <a class="link-arrow" href="{{P}}build/">Build your own on the same data {ARROW}</a></p>
      </div>
    </section>
""",
        faq=f"""    <section class="section section-soft" id="faq" aria-labelledby="faq-title">
      <div class="wrap">
{head("Questions", "Frequently asked", "faq-title")}
        <div class="faq reveal">
{faq(a["faq"])}
        </div>
      </div>
    </section>
""",
    )
