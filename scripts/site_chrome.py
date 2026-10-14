"""Navigation and footer for Option 6 (26-10-14 Website Development Brief).

Option 6 is one focused homepage with anchor navigation (brief: "Navigation and content
management"): How it works · Your options · Examples, then Log in and Talk to us.
/security is the only other page. Run `python3 scripts/site_chrome.py` after editing
the nav or footer; it rewrites both pages in place.
"""
import pathlib
import re

DEMO = "https://www.flieber.com/book-a-demo"
LOGIN = "https://app.flieber.com"
PRIVACY = "https://www.flieber.com/privacy-policy"
SERVICE = "https://www.flieber.com/service-agreement"

PAGE_FILES = {  # file: path prefix to the site root
    "index.html": "",
    "security/index.html": "../",
}

# Anchor links on the homepage (label, anchor)
SECTIONS = [
    ("How it works", "how-it-works"),
    ("Your options", "options"),
    ("Examples", "examples"),
]


def nav_html(p: str) -> str:
    home = p or "./"
    links = "\n".join(f'        <a href="{home}#{a}">{label}</a>' for label, a in SECTIONS)
    return f"""  <header class="nav nav-o6" id="nav">
    <div class="wrap">
      <a class="nav-logo" href="{home}" aria-label="Flieber home">
        <img src="{p}assets/img/flieber-logo.svg" alt="Flieber" width="116" height="20">
      </a>
      <nav class="nav-links" aria-label="Primary">
{links}
        <a class="menu-only" href="{LOGIN}">Log in</a>
      </nav>
      <div class="nav-cta">
        <a class="nav-login" href="{LOGIN}">Log in</a>
        <a class="btn btn-primary btn-sm" href="{home}#talk" data-cta="nav">Talk to us</a>
        <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span></button>
      </div>
    </div>
  </header>"""


def footer_html(p: str) -> str:
    home = p or "./"
    sections = "\n".join(f'            <li><a href="{home}#{a}">{label}</a></li>' for label, a in SECTIONS)
    return f"""  <footer class="footer">
    <div class="wrap">
      <div class="footer-top footer-o6">
        <div class="footer-brand">
          <img src="{p}assets/img/flieber-logo-light.svg" alt="Flieber" width="132" height="23">
          <p class="tagline">Inventory planning <em>built around your business.</em></p>
        </div>
        <div>
          <h2 class="footer-h">On this page</h2>
          <ul>
{sections}
            <li><a href="{home}#talk">Talk to us</a></li>
          </ul>
        </div>
        <div>
          <h2 class="footer-h">Company</h2>
          <ul>
            <li><a href="{p}security/">Security &amp; data</a></li>
            <li><a href="https://www.flieber.com/blog">Blog</a></li>
            <li><a href="mailto:hello@flieber.com">hello@flieber.com</a></li>
            <li><a href="{PRIVACY}">Privacy</a></li>
            <li><a href="{SERVICE}">Service agreement</a></li>
          </ul>
        </div>
        <div>
          <h2 class="footer-h">Customers</h2>
          <ul>
            <li><a href="{LOGIN}">Log in</a></li>
            <li><a href="https://help.flieber.com">Help center</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>169 Madison Avenue, New York, NY 10016</span>
        <span>© <span id="year">2026</span> Flieber</span>
      </div>
    </div>
  </footer>"""


# Review banner on every page, so Fabricio always knows which version he is looking at (Oct 14).
REVIEW_BAR = ('  <div class="review-bar" role="note">Review build · <b>Option 6</b> · '
              'Oct 14 development brief on Option 2’s design</div>')


def apply(root: pathlib.Path) -> None:
    for rel, p in PAGE_FILES.items():
        f = root / rel
        s = f.read_text(encoding="utf-8")
        s = re.sub(r'  <header class="nav[^"]*" id="nav">.*?</header>', lambda m: nav_html(p), s, count=1, flags=re.S)
        s = re.sub(r'  <div class="review-bar"[^>]*>.*?</div>\n', "", s, flags=re.S)
        s = s.replace('  <header class="nav', REVIEW_BAR + '\n  <header class="nav', 1)
        s = re.sub(r'  <footer class="footer">.*?</footer>', lambda m: footer_html(p), s, count=1, flags=re.S)
        f.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    apply(pathlib.Path(__file__).resolve().parent.parent)
