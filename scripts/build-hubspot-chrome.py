#!/usr/bin/env python3
"""Build the new site's header and footer as self-contained HubSpot includes, for pages that stay on old themes.

The free-trial and book-a-demo pages (old "flieber" theme, with their HubSpot forms) and the blog (old "sr" theme)
keep their own content and CSS; only their header and footer are swapped for the new site's (Oct 26). Every class
gets an "fz-" prefix and every rule is scoped under .fz, with a reset inside .fz, so the old theme's CSS cannot
distort the snippet and the snippet's CSS cannot touch the old content (forms included).

    python3 scripts/build-hubspot-chrome.py   (after build-hubspot.py; reads hubspot/build/home.html)

Output: hubspot/build/chrome/site-header.html and site-footer.html, uploaded to Design Manager
flieber-2026-b/partials/ and included with {% include "/flieber-2026-b/partials/site-header.html" %}.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT / "hubspot" / "build" / "home.html"
CSS = ROOT / "assets" / "css" / "site.css"
JS = ROOT / "assets" / "js" / "site.js"
OUT = ROOT / "hubspot" / "build" / "chrome"
ASSETS = "https://www.flieber.com/hubfs/flieber-2026/"


def blocks(css: str):
    """Split CSS into top-level (prelude, body) pairs; nested braces kept in body."""
    out, i, n = [], 0, len(css)
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    n = len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        depth, k = 1, j + 1
        while k < n and depth:
            depth += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        out.append((css[i:j].strip(), css[j + 1:k - 1]))
        i = k
    return out


def main() -> None:
    home = HOME.read_text(encoding="utf-8")
    header = re.search(r'<header class="nav" id="nav">.*?</header>', home, re.S).group(0)
    footer = re.search(r'<footer\b.*?</footer>', home, re.S).group(0)
    names = sorted({c for x in re.findall(r'class="([^"]+)"', header + footer) for c in x.split()}, key=len, reverse=True)
    cls_re = re.compile(r"\.(" + "|".join(map(re.escape, names)) + r")(?![\w-])")

    def rename_html(h: str) -> str:
        h = re.sub(r'class="([^"]+)"', lambda m: 'class="' + " ".join("fz-" + c for c in m.group(1).split()) + '"', h)
        h = h.replace('id="nav"', 'id="fz-nav"').replace('aria-controls="nav-', 'aria-controls="fz-nav-').replace('id="nav-', 'id="fz-nav-')
        return h

    def keep(sel: str) -> bool:
        parts = [p.strip() for p in sel.split(",")]
        return all(cls_re.search(p) or p.startswith("#nav") for p in parts) and not any(re.match(r"(html|body)\b", p) for p in parts)

    def scope(sel: str) -> str:
        out = []
        for p in sel.split(","):
            p = cls_re.sub(lambda m: ".fz-" + m.group(1), p.strip()).replace("#nav", "#fz-nav")
            out.append(".fz " + p)
        return ", ".join(out)

    css_out = []
    for pre, body in blocks(CSS.read_text(encoding="utf-8")):
        if pre.startswith("@font-face"):
            css_out.append(pre + "{" + re.sub(r'url\("\.\./fonts/([^"]+)"\)', lambda m: f'url("{ASSETS}{m.group(1)}")', body) + "}")
        elif pre == ":root":
            css_out.append(".fz{" + body + "}")
        elif pre.startswith("@media"):
            inner = [scope(p) + "{" + b + "}" for p, b in blocks(body) if keep(p)]
            if inner:
                css_out.append(pre + "{" + "".join(inner) + "}")
        elif not pre.startswith("@") and keep(pre):
            css_out.append(scope(pre) + "{" + body + "}")
    reset = (".fz{font-family:var(--font,'Open Sauce One',system-ui,sans-serif);font-size:16px;line-height:1.5;color:#1B1C1C;"
             "-webkit-font-smoothing:antialiased;text-align:left}"
             ".fz :where(*:not(svg):not(svg *)){all:revert;box-sizing:border-box;font-family:inherit;letter-spacing:inherit}"
             ".fz a{color:inherit;text-decoration:none}.fz ul{list-style:none;margin:0;padding:0}.fz p{margin:0}"
             ".fz img{max-width:100%;height:auto;display:block}.fz button{font:inherit;cursor:pointer}")
    # Old themes pad the page for their own fixed header (106 px on the flieber theme); the new header is sticky,
    # so drop that padding, and keep the header opaque over the old themes' dark heroes. Last, so they win.
    overrides = ".body-wrapper:has(#fz-nav){padding-top:0!important}.fz header.fz-nav{background:#fff}"
    style = "<style>" + reset + "".join(css_out) + overrides + "</style>"

    js = JS.read_text(encoding="utf-8")
    # The nav section of site.js (scrolled state, phone menu, dropdowns), with ids and classes renamed.
    nav_js = js[js.index("  /* ---------- Nav: scrolled state"):]
    end = re.search(r"\n  /\* ---------- (?!Nav)", nav_js)
    nav_js = nav_js[:end.start()] if end else nav_js
    nav_js = nav_js.replace("getElementById('nav')", "getElementById('fz-nav')")
    nav_js = re.sub(r"'\.(" + "|".join(map(re.escape, names)) + r")(?![\w-])", lambda m: "'.fz-" + m.group(1), nav_js)
    nav_js = re.sub(r"(querySelectorAll|querySelector)\('\.(?!fz-)([\w-]+)", lambda m: f"{m.group(1)}('.fz-{m.group(2)}" if m.group(2) in names else m.group(0), nav_js)
    script = "<script>(function(){\n" + nav_js + "\n})();</script>"

    OUT.mkdir(parents=True, exist_ok=True)
    head = "<!--\n  templateType: none\n-->\n"
    (OUT / "site-header.html").write_text(head + style + '\n<div class="fz">' + rename_html(header) + "</div>\n" + script + "\n", encoding="utf-8")
    (OUT / "site-footer.html").write_text(head + '<div class="fz">' + rename_html(footer) + "</div>\n", encoding="utf-8")
    print("header", len((OUT / "site-header.html").read_text()), "bytes; footer", len((OUT / "site-footer.html").read_text()), "bytes;",
          len(css_out), "CSS blocks")


if __name__ == "__main__":
    main()
