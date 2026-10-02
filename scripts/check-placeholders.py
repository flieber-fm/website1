#!/usr/bin/env python3
"""List every placeholder left on the site before launch.

Finds [BRACKETED] placeholders in the published files and link destinations
still marked with data-placeholder. Run from the repo root:

    python3 scripts/check-placeholders.py           # list placeholders
    python3 scripts/check-placeholders.py --strict  # also exit 1 if any remain

The preview-only no-index tags are reported too, since they must also be
removed at launch.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["index.html", "features/index.html", "agents/index.html", "pricing/index.html", "security/index.html", "contact/index.html"] + sorted(str(x.relative_to(ROOT)) for x in ROOT.glob("product/*/index.html")) + ["multichannel/index.html", "agencies/index.html"] + ["llms.txt", "llms-full.txt", "capabilities.json", "robots.txt", "sitemap.xml"]
BRACKET = re.compile(r"\[[A-Z][A-Z0-9 ,:/'’.&-]{2,}\]|\[others\]")
LINK = re.compile(r'data-placeholder="([^"]+)"')
NOINDEX = re.compile(r'name="robots" content="noindex|^Disallow: /\s*$', re.M)


def main() -> int:
    found = 0
    for rel in FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        hits = []
        for i, line in enumerate(text.splitlines(), 1):
            for m in LINK.finditer(line):
                hits.append((i, f"link destination {m.group(1)}"))
            stripped = LINK.sub("", line)
            for m in BRACKET.finditer(stripped):
                hits.append((i, m.group(0)))
            if NOINDEX.search(line):
                hits.append((i, "preview no-index (remove at launch)"))
        if hits:
            print(f"\n{rel}")
            for i, what in hits:
                print(f"  line {i:>4}: {what}")
            found += len(hits)
    caddy = (ROOT / "Caddyfile").read_text(encoding="utf-8")
    if "X-Robots-Tag" in caddy:
        print("\nCaddyfile\n  X-Robots-Tag no-index header (remove at launch)")
        found += 1
    print(f"\n{found} placeholder(s) remaining.")
    return 1 if found and "--strict" in sys.argv else 0


if __name__ == "__main__":
    sys.exit(main())
