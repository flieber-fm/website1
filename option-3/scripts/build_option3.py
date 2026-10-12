#!/usr/bin/env python3
"""Build Option 3 (Build with Flieber / Run with Flieber) on Option 2's design system.

Source of the positioning, structure and page requirements:
  Flieber Website Strategy & Functional Specification, working draft 1.0, Oct 12, 2026.
Source of approved facts, copy, customer logos, quotes and results:
  Option 2 (branch claude/eager-bohr-ui8a03). Original module pages and homepage are kept in scripts/src/.

Run from option-3/:  python3 scripts/build_option3.py
It is safe to run repeatedly: pages it writes are regenerated from scripts/src and the code below,
and pages carried over from Option 2 only get their nav, footer and links rewritten.
"""
import re
import shutil
from pathlib import Path

import chrome as C
from content_option3 import home_main, build_main, run_main, app_extra, BUILD_DATA_KICKER

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "src"

# Option 2 URL -> Option 3 URL (same depth, so relative prefixes stay valid)
MOVES = {
    "product/data-layer": "build/data",
    "product/demand-forecasting": "run/forecasting",
    "product/inventory-forecasting": "run/inventory",
    "product/replenishment": "run/replenishment",
    "product/workflows": "run/workflows",
}
MODULE_SRC = {"forecasting": "demand-forecasting", "inventory": "inventory-forecasting",
              "replenishment": "replenishment", "workflows": "workflows"}

CARRIED = {  # Option 2 page -> current nav item
    "features": "run", "pricing": "pricing", "security": "build", "contact": None, "agents": "agents",
    "multichannel": "solutions", "agencies": "solutions", "before-you-choose": "solutions",
    "mcp": "build", "customize": "build", "integrations": "build", "managed-services": "run",
    "who-we-are": "who", "put-flieber-to-work": "run", "use-cases": "solutions",
}


def move_links(text):
    for old, new in MOVES.items():
        text = text.replace(old + "/", new + "/").replace(old + '"', new + '"').replace(old + "#", new + "#")
        text = re.sub(re.escape(old) + r"(?=[\s<\"',)])", new, text)
    # Option 2's homepage section "Which Flieber is right for you?" is "Two paths, one foundation" here
    return text.replace('#which-flieber">See which Flieber is right for you', '#two-paths">See which path is right for you')


def section(html, sid):
    m = re.search(r'    <section [^>]*id="%s".*?</section>\n' % re.escape(sid), html, re.S)
    if not m:
        raise SystemExit(f"section #{sid} not found")
    return m.group(0)


def write(rel, text):
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")
    print("wrote", rel)


def page(rel, cur, title, desc, main, journey=None, crumbs=None):
    depth = rel.count("/")
    p = "../" * depth
    path = rel[:-len("index.html")]
    out = C.head(p, path, title, desc) + C.nav_html(p, cur) + "\n"
    if journey:
        out += C.pathbar(p, journey, crumbs) + "\n"
    out += '\n  <main id="main">\n' + main.replace("{P}", p) + "\n  </main>\n\n" + C.footer_html(p, True) + C.tail(p)
    write(rel, move_links(out))


def main():
    home2 = (SRC / "option2-home.html").read_text(encoding="utf-8")
    snippets = {
        "logos": re.search(r'    <section class="logos-band".*?</section>\n', home2, re.S).group(0),
        "sim": re.search(r'          <figure class="sim sim-compact".*?</figure>\n', home2, re.S).group(0),
        "results": re.search(r'        <div class="results-block.*?(?=        <div class="quotes)', home2, re.S).group(0),
        "quotes": re.search(r'        <div class="quotes.*?\n        </div>\n(?=      </div>\n    </section>)', home2, re.S).group(0),
        "why": re.search(r'        <div class="cards-4 reveal-stagger">.*?\n        </div>\n', home2, re.S).group(0),
    }

    # ---- New pages ----
    page("index.html", None,
         "Flieber: inventory software that works the way you do",
         "Start with proven inventory applications, or build your own with Flieber’s data, intelligence and ready-to-use foundations.",
         home_main(snippets))
    page("build/index.html", "build",
         "Build with Flieber: build your inventory software, start miles ahead | Flieber",
         "Use proven inventory data structures, business logic, working apps and validation tools, then customize what matters. Connect through MCP or API.",
         build_main(snippets), "build", [("Home", "../"), ("Build with Flieber", None)])
    page("run/index.html", "run",
         "Run with Flieber: inventory planning that’s ready for your reality | Flieber",
         "Reliable forecasts, inventory visibility and replenishment recommendations without building from scratch.",
         run_main(snippets), "run", [("Home", "../"), ("Run with Flieber", None)])

    # ---- Run applications: Option 2 module pages + the spec's application template (9.2) ----
    for slug, name, _, _ in C.RUN_APPS:
        src = (SRC / "product" / MODULE_SRC[slug] / "index.html").read_text(encoding="utf-8")
        title = re.search(r"<title>(.*?)</title>", src).group(1)
        desc = re.search(r'<meta name="description" content="(.*?)">', src).group(1)
        head_sec = re.search(r'    <section class="page-head.*?</section>\n', src, re.S).group(0)
        head_sec = head_sec.replace(f"Product · {name}", f"Run · {name}")
        extra = app_extra(slug)
        body = (head_sec.replace("    </section>\n", extra["built_for"] + "\n    </section>\n", 1)
                + extra["jobs"]
                + section(src, "what-you-can-do")
                + extra["io"]
                + extra["accuracy"]
                + section(src, "together")
                + extra["customize"]
                + section(src, "common-uses")
                + section(src, "works-with")
                + extra["faq"]
                + section(src, "next"))
        page(f"run/{slug}/index.html", "run", title, desc, body, "run",
             [("Home", "../../"), ("Run with Flieber", "../"), (name, None)])

    # ---- Build · Data foundation: Option 2's data layer page, now under Build ----
    src = (SRC / "product" / "data-layer" / "index.html").read_text(encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", src).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', src).group(1)
    body = re.search(r'  <main id="main">\n(.*)  </main>', src, re.S).group(1).replace("Product · Data layer", BUILD_DATA_KICKER)
    page("build/data/index.html", "build", title, desc, body, "build",
         [("Home", "../../"), ("Build with Flieber", "../"), ("Data foundation", None)])

    # ---- Pages carried over from Option 2: new nav, footer and links ----
    for rel in sorted(ROOT.rglob("index.html")):
        r = rel.relative_to(ROOT).as_posix()
        top = r.split("/")[0]
        if top not in CARRIED:
            continue
        p = "../" * r.count("/")
        text = C.apply(r, rel.read_text(encoding="utf-8"), p, CARRIED[top])
        rel.write_text(move_links(text), encoding="utf-8")
        print("updated", r)

    for name in ["llms.txt", "llms-full.txt", "capabilities.json", "sitemap.xml"]:
        f = ROOT / name
        f.write_text(move_links(f.read_text(encoding="utf-8")), encoding="utf-8")
        print("links", name)

    old = ROOT / "product"
    if old.exists():
        shutil.rmtree(old)


if __name__ == "__main__":
    main()
