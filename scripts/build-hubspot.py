#!/usr/bin/env python3
"""Build self-contained HubSpot templates from the static pages.

Each page becomes one HubL template in hubspot/build/ with CSS and JS inlined.
Fonts and images load from HubSpot File Manager (folder flieber-2026, see
hubspot/CUTOVER.md), and links are made root-relative for www.flieber.com. Tags HubSpot already injects through
standard_header_includes are removed: meta description, canonical, og:url,
og:title, og:description, twitter:card, the preview no-index tag and our
GTM/HubSpot loader (HubSpot adds GTM and its tracking code itself).

    python3 scripts/build-hubspot.py
"""
import base64
import mimetypes
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_content as C  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ASSETS = "https://www.flieber.com/hubfs/flieber-2026/"
OUT = ROOT / "hubspot" / "build"
PAGES = {  # source file: (site path, template label)
    "index.html": ("/", "Flieber 2026 - Home"),
    "features/index.html": ("/features/", "Flieber 2026 - Features"),
    "agents/index.html": ("/agents/", "Flieber 2026 - Agents"),
    "pricing/index.html": ("/pricing/", "Flieber 2026 - Pricing"),
    "security/index.html": ("/security/", "Flieber 2026 - Security"),
    "contact/index.html": ("/contact/", "Flieber 2026 - Contact"),
}
# Option 2 adds five module pages, /multichannel and /agencies (Option 2 brief, section 10). Templates are only
# built locally; nothing is uploaded to HubSpot until an option is elected.
for _slug in ["data-layer", "demand-forecasting", "inventory-forecasting", "replenishment", "workflows"]:
    PAGES[f"product/{_slug}/index.html"] = (f"/product/{_slug}/", f"Flieber 2026 B - Product - {_slug}")
PAGES["multichannel/index.html"] = ("/multichannel/", "Flieber 2026 B - Multichannel")
PAGES["agencies/index.html"] = ("/agencies/", "Flieber 2026 B - Agencies")
PAGES["before-you-choose/index.html"] = ("/before-you-choose/", "Flieber 2026 B - Before you choose")
PAGES["mcp/index.html"] = ("/mcp/", "Flieber 2026 B - MCP and AI agents")
PAGES["build-with-ai/index.html"] = ("/build-with-ai/", "Flieber 2026 B - Build with AI")
PAGES["integrations/index.html"] = ("/integrations/", "Flieber 2026 B - Integrations")
for _x in C.INTEGRATIONS:
    PAGES[f"integrations/{_x['slug']}/index.html"] = (f"/integrations/{_x['slug']}/", f"Flieber 2026 B - Integrations - {_x['slug']}")
for _u in C.USE_CASES:
    PAGES[f"use-cases/{_u['slug']}/index.html"] = (f"/use-cases/{_u['slug']}/", f"Flieber 2026 B - Use case - {_u['slug']}")
PAGES["managed-services/index.html"] = ("/managed-services/", "Flieber 2026 B - Managed Services")
PAGES["who-we-are/index.html"] = ("/who-we-are/", "Flieber 2026 B - Who we are")


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    if path.suffix == ".woff2":
        mime = "font/woff2"
    if path.suffix == ".svg":
        return "data:image/svg+xml;base64," + base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def asset_path(src: str, page_dir: Path) -> Path:
    clean = src.split("?")[0]
    return (page_dir / clean).resolve()


def build(src_rel: str, site_path: str, label: str) -> str:
    src = ROOT / src_rel
    page_dir = src.parent
    html = src.read_text(encoding="utf-8")

    # Drop tags HubSpot's standard_header_includes provides, plus preview-only bits.
    drops = [
        r'\s*<!-- PREVIEW ONLY: remove before public launch -->',
        r'\s*<meta name="robots" content="noindex, nofollow">',
        r'\s*<meta name="description" content="[^"]*">',
        r'\s*<link rel="canonical" href="[^"]*">',
        r'\s*<meta property="og:(url|title|description)" content="[^"]*">',
        r'\s*<meta name="twitter:card" content="[^"]*">',
        r'\s*<link rel="preload" href="[^"]*" as="font"[^>]*>',
        r'\s*<!-- Google Tag Manager.*?</script>',
    ]
    for pat in drops:
        html, n = re.subn(pat, "", html, flags=re.S)

    # Inline the stylesheet, with fonts as data URIs.
    css = (ROOT / "assets/css/site.css").read_text(encoding="utf-8")
    css = re.sub(r'url\("\.\./fonts/([^"]+)"\)', lambda m: f'url("{ASSETS}{m.group(1)}")', css)
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\n\s*\n+", "\n", css)
    html = re.sub(r'<link rel="stylesheet" href="[^"]*site\.css[^"]*">',
                  lambda m: "<style>\n" + css + "\n</style>", html)

    # Inline the script.
    js = (ROOT / "assets/js/site.js").read_text(encoding="utf-8")
    html = re.sub(r'<script src="[^"]*site\.js[^"]*" defer></script>',
                  lambda m: "<script>\n" + js + "\n</script>", html)

    # Images and favicon as data URIs.
    def img(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith(("http", "data:", "#", "mailto:")) or "assets/" not in val:
            return m.group(0)
        return f'{attr}="{ASSETS}{Path(val.split("?")[0]).name}"'
    html = re.sub(r'(src)="([^"]+)"', img, html)
    html = re.sub(r'(href)="([^"]*assets/img/[^"]+)"', img, html)

    # Root-relative links.
    base = "https://www.flieber.com" + site_path
    def link(m):
        val = m.group(1)
        if val.startswith(("http", "mailto:", "tel:", "#", "data:", "/")):
            return m.group(0)
        u = urlparse(urljoin(base, val))
        path = u.path if u.path == "/" else u.path.rstrip("/")
        path += ("#" + u.fragment) if u.fragment else ""
        return f'href="{path}"'
    html = re.sub(r'href="([^"]*)"', link, html)

    # The Organization logo in JSON-LD is uploaded to File Manager at cutover.
    html = html.replace("https://www.flieber.com/assets/img/flieber-logo.svg",
                        ASSETS + "flieber-logo.svg")

    # HubSpot includes (analytics, GTM, canonical, meta) before </head> and </body>.
    html = html.replace("</head>", "  {{ standard_header_includes }}\n</head>", 1)
    html = html.replace("</body>", "  {{ standard_footer_includes }}\n</body>", 1)

    header = f"<!--\n  templateType: page\n  isAvailableForNewContent: true\n  label: {label}\n-->\n"
    return header + html


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_rel, (site_path, label) in PAGES.items():
        out = build(src_rel, site_path, label)
        name = (site_path.strip("/").replace("/", "-") or "home") + ".html"
        (OUT / name).write_text(out, encoding="utf-8")
        print(f"{name}: {len(out.encode()) // 1024} KB")


if __name__ == "__main__":
    main()
