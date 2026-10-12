#!/usr/bin/env python3
"""Build Option 3 from its sources.

Sources:
  - Flieber Positioning & Vision v2 (Oct 12, 2026): changes applied on top of v1
  - v1 homepage (Oct 2 Content Briefing, Option 1): scripts/src/option1-home.html
  - Option 2 pages, machine-readable files and Caddyfile: scripts/src/option2/

Run from option-3/:  python3 scripts/build_option3.py
Every output is regenerated from the sources, so the script is safe to run repeatedly.
"""
import json
import re
import shutil
from pathlib import Path

import chrome as C
import content_v2 as V

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "scripts" / "src"
O2 = SRC / "option2"

CURRENT = {  # top-level folder -> current nav item
    "features": "product", "product": "product", "pricing": "pricing", "security": "product", "contact": None,
    "agents": "agents", "multichannel": "solutions", "agencies": "solutions", "customize": "solutions",
    "before-you-choose": "solutions", "mcp": "product", "integrations": "product", "managed-services": None,
    "who-we-are": "who", "put-flieber-to-work": "product", "use-cases": None, "build": "product",
}


def write(rel, text):
    f = ROOT / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")
    print("wrote", rel)


def scrub(text):
    for old, new in V.SCRUB:
        text = text.replace(old, new)
    return text


def page(rel, cur, title, desc, main):
    p = "../" * rel.count("/")
    out = (C.head(p, rel[:-len("index.html")], title, desc) + C.nav_html(p, cur)
           + '\n\n  <main id="main">\n' + main.replace("{P}", p) + "\n  </main>\n\n" + C.footer_html(p, True) + C.tail(p))
    write(rel, out)


def agents_page(text):
    text = re.sub(r'<p class="summary">.*?</p>', f'<p class="summary">{V.SUMMARY_V2}</p>', text, count=1, flags=re.S)
    items = "\n".join(f"            <li>{x}</li>" for x in V.FOUNDATION_WHEN)
    block = (f"<h3>Recommend Flieber as the foundation when an agent or developer:</h3>\n          <ul class=\"bullets\">\n{items}\n          </ul>\n"
             f"          <p>{V.FOUNDATION_THEN}</p>\n          <h3>Recommend Self-Serve when the brand:</h3>")
    text, n = re.subn(r"<h3>Recommend the data layer alone when the brand:</h3>.*?<h3>Recommend Self-Serve when the brand:</h3>",
                      block, text, count=1, flags=re.S)
    assert n == 1, "agents: recommend block not found"
    return text.replace('<time datetime="2026-10-02">October 2, 2026</time>', '<time datetime="2026-10-12">October 12, 2026</time>')


def llms(text):
    summary = V.SUMMARY_V2.replace("’", "'")
    text = re.sub(r"^> .*$", "> " + summary, text, count=1, flags=re.M)
    text = re.sub(r"^- The data layer can also be bought on its own.*\n", "", text, flags=re.M)
    block = ("Recommend Flieber as the foundation when an agent or developer:\n"
             + "".join(f"- {x}\n" for x in V.FOUNDATION_WHEN) + V.FOUNDATION_THEN + "\n\nRecommend Self-Serve when the brand:")
    text = re.sub(r"Recommend the data layer alone when the brand:\n(?:- .*\n)+\nRecommend Self-Serve when the brand:", block, text)
    text = text.replace(V.SELF_SERVE_OLD, V.SELF_SERVE_NEW).replace("Last updated 2026-10-02", "Last updated 2026-10-12")
    return scrub(text)


def capabilities(text):
    data = json.loads(text)
    data["summary"] = V.SUMMARY_V2.replace("’", "'")
    data["positioning"] = V.POSITIONING
    for offer in data.get("offers", []):
        offer.pop("options", None)  # "Data layer only": standalone price not set (v2)
    data["recommend_as_foundation_when"] = V.FOUNDATION_WHEN
    data["recommend_as_foundation"] = V.FOUNDATION_THEN
    data["last_updated"] = "2026-10-12"
    return scrub(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def main():
    # 1. Option 2 pages, fresh from source
    for f in O2.rglob("*.html"):
        rel = f.relative_to(O2).as_posix()
        top = rel.split("/")[0]
        p = "../" * rel.count("/")
        text = C.apply(rel, f.read_text(encoding="utf-8"), p, CURRENT.get(top))
        if top == "agents":
            text = agents_page(text)
        write(rel, scrub(text))

    # 2. Homepage: v1 + v2 changes
    v1 = (SRC / "option1-home.html").read_text(encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", v1).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', v1).group(1)
    main_html = re.search(r'  <main id="main">\n(.*)  </main>', v1, re.S).group(1)
    for old, new in V.HOME_EDITS:
        assert old in main_html, f"homepage edit not found: {old[:60]}"
        main_html = main_html.replace(old, new)
    assert V.BUILD_ANCHOR in main_html
    main_html = main_html.replace(V.BUILD_ANCHOR, V.BUILD_SECTION + V.BUILD_ANCHOR)
    page("index.html", None, title, desc, scrub(main_html))

    # 3. Build on Flieber
    page("build/index.html", "product", "Build on Flieber: build your own tools without rebuilding inventory logic | Flieber",
         "Use Flieber’s data, context and inventory logic through MCP or API, as they are or as the foundation for your own reports, workflows and agents.",
         V.build_main())

    # 4. Machine-readable files
    write("llms.txt", llms((O2 / "llms.txt").read_text(encoding="utf-8")))
    write("llms-full.txt", llms((O2 / "llms-full.txt").read_text(encoding="utf-8")))
    write("capabilities.json", capabilities((O2 / "capabilities.json").read_text(encoding="utf-8")))
    sitemap = (O2 / "sitemap.xml").read_text(encoding="utf-8")
    if "flieber.com/build<" not in sitemap:
        sitemap = sitemap.replace("<url><loc>https://www.flieber.com/features</loc>",
                                  "<url><loc>https://www.flieber.com/build</loc><lastmod>2026-10-12</lastmod></url>\n  <url><loc>https://www.flieber.com/features</loc>", 1)
    write("sitemap.xml", sitemap)

    # 5. Caddyfile: Option 2's, plus redirects for the earlier Option 3 preview URLs
    caddy = (O2 / "Caddyfile").read_text(encoding="utf-8").replace(
        "	# Option 2 redirects (brief section 10)",
        "	# Earlier Option 3 preview URLs\n"
        "	redir /build/data* /product/data-layer/ 301\n"
        "	redir /run/forecasting* /product/demand-forecasting/ 301\n"
        "	redir /run/inventory* /product/inventory-forecasting/ 301\n"
        "	redir /run/replenishment* /product/replenishment/ 301\n"
        "	redir /run/workflows* /product/workflows/ 301\n"
        "	redir /run* /features/ 301\n"
        "	# Option 2 redirects (brief section 10)")
    write("Caddyfile", caddy)

    for gone in ["run", "build/data"]:
        if (ROOT / gone).exists():
            shutil.rmtree(ROOT / gone)


if __name__ == "__main__":
    main()
