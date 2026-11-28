#!/usr/bin/env python3
"""Homepage V16: the positioning brief as written at Claude Doc revision 92 (Nov 28, 2026).

V15 (scripts/build-positioning-variant.py) is kept frozen with Claude's suggested changes; this page follows the brief verbatim.
Writes scripts/home-snapshots/2026-11-28-positioning-v16.html, which build-home-variants.py shows as V16.
Header, footer, styles and scripts come from the current index.html so the page keeps the site's design;
only the review bar, nav, main content, footer tagline and footer links change.
Placeholders (hero video, customer logos, Self-Serve page) are marked on the page, as the brief asks.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "scripts" / "home-snapshots" / "2026-11-28-positioning-v16.html"
BOOK = "https://www.flieber.com/book-a-demo"
SELF_SERVE = "pricing/#plan-ss"  # placeholder until the Self-Serve page exists (brief, open items)

ARROW = '<span class="arrow" aria-hidden="true">→</span>'
TAGLINE = "Flieber: combining AI and specialists to power your inventory decisions."
SHORT = "Flieber: where AI meets inventory experts."
# Monthly scorecard copy is an open item in the brief (section 10): shown with this marker so it is easy to drop.
PEND = '<span class="pv-pend" title="Open item in the brief: confirm before this goes live">Pending confirmation</span>'
MIT_URL = "https://www.aol.com/finance/mit-report-95-generative-ai-105412029.html"

CSS = """<style>
/* Positioning variant (Nov 27 brief): page-scoped components */
.pv-hero-grid{display:grid;grid-template-columns:1fr;gap:clamp(28px,4vw,56px);align-items:center}
@media(min-width:980px){.pv-hero-grid{grid-template-columns:1.2fr 1fr}}
.pv-hero-grid .h1{font-size:clamp(34px,3.6vw,50px);line-height:1.06}
.pv-br{display:none}
@media(min-width:980px){.pv-br{display:block}}
.pv-hero-grid .lead{max-width:560px;margin-top:22px}
.pv-actions{display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px;margin-top:28px}
.pv-alt{font-size:15px;color:var(--charcoal);text-decoration:underline;text-underline-offset:3px}
.pv-alt:hover{color:var(--black)}
.pv-video{margin:0;position:relative;aspect-ratio:16/9;border-radius:20px;background:var(--black);color:#fff;display:flex;flex-direction:column;justify-content:flex-end;padding:22px 24px;overflow:hidden}
.pv-video::before{content:"";position:absolute;inset:0;background:radial-gradient(120% 90% at 85% 10%,rgba(245,237,97,.28),transparent 60%)}
.pv-play{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:72px;height:72px;border-radius:50%;background:var(--yellow);display:grid;place-items:center}
.pv-play svg{margin-left:4px}
@media(max-width:600px){.pv-video{aspect-ratio:auto;min-height:300px;padding:18px}.pv-play{top:30%;width:56px;height:56px}}
.pv-video p{position:relative;margin:0;font-size:14px;line-height:1.45;color:rgba(255,255,255,.82)}
.pv-video b{color:#fff;font-weight:600}
.pv-ph{display:inline-block;margin-bottom:8px;padding:3px 8px;border:1px dashed rgba(255,255,255,.55);border-radius:6px;font:600 11px/1.2 ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--yellow)}
.pv-ph.dark{border-color:var(--gray-dark);color:var(--charcoal)}
.pv-3{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:820px){.pv-3{grid-template-columns:repeat(3,1fr)}}
.pv-2{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:820px){.pv-2{grid-template-columns:repeat(2,1fr)}}
.pv-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px 26px 28px}
.section-soft .pv-card{background:#fff}
.pv-card h3{margin:0 0 10px;font-size:20px;line-height:1.25;letter-spacing:-.02em;font-weight:600}
.pv-card p{margin:0;color:var(--charcoal);font-size:16px;line-height:1.55}
.pv-num{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--yellow);font:600 15px/1 ui-monospace,monospace;margin-bottom:18px}
.pv-proof-pt{margin-top:16px!important;padding-top:14px;border-top:1px solid var(--line);font-size:14px!important;color:var(--black)!important}
.pv-proof-pt b{font-weight:600}
.pv-moments{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:700px){.pv-moments{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1040px){.pv-moments{grid-template-columns:repeat(3,1fr)}}
.pv-moment{display:flex;flex-direction:column;gap:14px}
.pv-moment .pv-tag{font:600 12px/1.2 ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--gray-dark)}
.pv-moment blockquote{margin:0;font-size:19px;line-height:1.35;letter-spacing:-.01em}
.pv-moment p{margin-top:auto!important;padding-top:14px;border-top:1px solid var(--line)}
.pv-beyond{max-width:860px;margin:0 auto;text-align:center;font-size:clamp(24px,3vw,34px);line-height:1.25;letter-spacing:-.025em}
.pv-stats{display:grid;grid-template-columns:1fr;gap:16px;margin-top:40px}
@media(min-width:820px){.pv-stats{grid-template-columns:repeat(3,1fr)}}
.pv-stat{border-top:2px solid var(--black);padding-top:18px}
.pv-stat strong{display:block;font-size:clamp(34px,4vw,48px);line-height:1;letter-spacing:-.04em;font-weight:500}
.pv-stat span{display:block;margin-top:12px;color:var(--charcoal);font-size:15px;line-height:1.5}
.pv-integ{margin-top:36px;display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.pv-integ-l{font-size:14px;color:var(--gray-dark);margin-right:6px}
.pv-chip{padding:8px 14px;border:1px solid var(--line);border-radius:999px;background:#fff;font-size:15px}
.pv-logos{margin-top:28px;padding:18px 20px;border:1px dashed var(--gray-medium);border-radius:14px;color:var(--charcoal);font-size:14px}
.pv-ss{display:grid;grid-template-columns:1fr;gap:20px;align-items:center;background:var(--gray-light);border-radius:22px;padding:clamp(26px,4vw,44px)}
@media(min-width:820px){.pv-ss{grid-template-columns:1fr auto}}
.pv-ss h2{margin:0 0 8px}
.pv-ss p{margin:0;color:var(--charcoal);max-width:620px}
.pv-pend{display:inline-block;margin-left:6px;padding:1px 7px;border:1px dashed var(--gray-dark);border-radius:6px;font:600 10px/1.5 ui-monospace,monospace;letter-spacing:.05em;text-transform:uppercase;color:var(--charcoal);vertical-align:2px;white-space:nowrap}
.pv-build{display:grid;grid-template-columns:1fr;gap:clamp(24px,4vw,56px);align-items:start}
@media(min-width:900px){.pv-build{grid-template-columns:1fr 1fr}}
.pv-big{font-size:clamp(56px,7vw,88px);line-height:1;letter-spacing:-.05em;font-weight:500}
.pv-big-l{margin-top:12px;color:var(--charcoal);font-size:16px;line-height:1.5;max-width:420px}
.pv-build .lead{margin-top:0}
.pv-cite{margin-top:18px;font-size:13px;line-height:1.5;color:var(--gray-dark)}
.pv-cite a{color:inherit;text-decoration:underline;text-underline-offset:2px}
.pv-note{display:inline-grid;place-items:center;width:20px;height:20px;margin:0 2px;border-radius:50%;background:var(--blue);color:#fff;font:600 11px/1 ui-monospace,monospace;vertical-align:3px;cursor:help}
.pv-ex{padding:1px 6px;border:1px dashed var(--gray-dark);border-radius:6px;background:var(--yellow-light);font-size:.92em;white-space:normal}
.pv-reassure{margin:16px 0 0;max-width:520px;font-size:16px;line-height:1.5;font-weight:600;color:var(--black)}
.pv-close{max-width:820px;margin:36px 0 0;font-size:clamp(19px,2vw,23px);line-height:1.4;letter-spacing:-.015em}
.pv-row{align-items:start}
@supports (grid-template-rows:subgrid){
  .pv-row>.pv-card{display:grid;grid-template-rows:subgrid;align-content:start;row-gap:0}
  .pv-span2>.pv-card{grid-row:span 2}
  .pv-span3>.pv-card{grid-row:span 3}
  .pv-row>.pv-card>*{margin-top:0;margin-bottom:0}
  .pv-row>.pv-card>h3{margin-bottom:10px;align-self:start}
  .pv-span3.pv-3>.pv-card>.pv-num{margin-bottom:18px}
  .pv-moments.pv-row>.pv-card{row-gap:14px}
  .pv-moments.pv-row>.pv-card>p{margin-top:0!important}
}
.pv-sub{margin:56px 0 18px;font-size:22px;line-height:1.25;letter-spacing:-.02em;font-weight:600}
.pv-team-lead{margin:-6px 0 18px;color:var(--charcoal);font-size:16px}
.pv-team{display:grid;grid-template-columns:1fr;gap:16px}
@media(min-width:820px){.pv-team{grid-template-columns:repeat(3,1fr)}}
.pv-team-i{border-top:2px solid var(--black);padding-top:16px}
.pv-team-i b{display:block;font-size:19px;font-weight:600;letter-spacing:-.01em}
.pv-team-i span{display:block;margin-top:8px;color:var(--charcoal);font-size:15px;line-height:1.5}
.pv-voices{background:var(--yellow)}
.pv-voices .quotes{margin-top:0}
.pv-voices .quote-dots button{background:rgba(27,28,28,.22)}
.pv-voices .quote-dots button[aria-current="true"]{background:var(--black)}
.pv-voices .icon-btn{border-color:rgba(27,28,28,.35)}
.pv-voices .avatar{background:#fff}
.pv-proof{display:grid;grid-template-columns:1fr;gap:32px;align-items:stretch;margin-top:40px}
.pv-proof-l{display:flex;flex-direction:column}
@media(min-width:960px){.pv-proof-note{margin-left:calc((100% - 40px) / 3 + 40px)}}
@media(min-width:960px){.pv-proof{grid-template-columns:4fr 8fr;gap:40px}}
.pv-exp{flex:1;display:flex;flex-direction:column;justify-content:flex-end;background:var(--yellow);border-radius:16px;padding:22px 24px}
.pv-exp .pv-res-n{font-size:clamp(48px,6vw,72px)}
.pv-exp .pv-res-l{color:var(--black)}
.pv-proof .pv-big{margin:36px 0 0}
.pv-proof .pv-sub{margin:0 0 18px}
.pv-res{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.pv-res-i{background:var(--gray-light);border-radius:16px;padding:20px 22px}
.pv-res-n{display:block;font-size:clamp(34px,4vw,46px);line-height:1;letter-spacing:-.04em;font-weight:500}
.pv-res-l{display:block;margin-top:10px;color:var(--charcoal);font-size:15px;line-height:1.4}
.pv-teamband{margin-top:56px;display:grid;grid-template-columns:1fr;gap:28px;background:var(--black);color:var(--gray-light);border-radius:22px;padding:clamp(26px,4vw,44px)}
@media(min-width:960px){.pv-teamband{grid-template-columns:4fr 8fr;gap:48px}}
.pv-teamband .pv-sub{color:#fff}
.pv-teamband .pv-team-lead{margin:8px 0 0;color:rgba(240,245,246,.75)}
.pv-teamband .pv-team-i{border-top-color:var(--yellow)}
.pv-teamband .pv-team-i b{color:#fff}
.pv-teamband .pv-team-i span{color:rgba(240,245,246,.75)}
/* hero stage */
.pv-hero-grid{align-items:stretch}
.pv-stage{position:relative;display:flex;align-items:center;justify-content:center;min-height:100%;padding:clamp(28px,4vw,56px) clamp(18px,3vw,40px);border-radius:28px;background:radial-gradient(90% 70% at 85% 0%,var(--yellow-light),transparent 60%),radial-gradient(80% 70% at 0% 100%,#DDE7F7,transparent 60%),var(--gray-light);overflow:hidden}
.pv-stage .pv-video{width:100%;max-width:400px;box-shadow:0 24px 60px rgba(27,28,28,.22)}
.pv-float{position:absolute;z-index:2;display:flex;align-items:center;gap:10px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:10px 14px;font-size:13.5px;line-height:1.35;box-shadow:0 12px 30px rgba(27,28,28,.12);animation:pvFloat 6s ease-in-out infinite}
.pv-float b{font-weight:600}
.pv-float-a{top:44px;left:22px}
.pv-float-b{right:22px;bottom:22px;animation-delay:-3s}
.pv-dot{width:9px;height:9px;border-radius:50%;background:#2BB673;box-shadow:0 0 0 4px rgba(43,182,115,.18)}
.pv-approve{padding:6px 10px;border-radius:8px;background:var(--yellow);font-weight:600;font-size:12.5px}
.pv-illus{position:absolute;right:24px;top:14px;max-width:46%;text-align:right;font:500 10.5px/1 ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--gray-dark)}
@keyframes pvFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@media(max-width:979px){.pv-stage{padding:64px 16px 72px}.pv-stage .pv-video{max-width:none}}
@media(min-width:980px){.pv-stage{padding:92px 32px 96px}}
@media(max-width:600px){.pv-float{font-size:12px;padding:8px 10px}.pv-float-a{top:14px;left:14px}.pv-float-b{right:14px;bottom:14px}.pv-illus{display:none}}
/* why now icons */
.pv-ico{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:12px;background:var(--yellow);color:var(--black);margin-bottom:18px;justify-self:start}
/* dark era section */
.pv-dark .pv-card{background:#262829;border-color:rgba(240,245,246,.1)}
.pv-dark .pv-card h3{color:#fff}
.pv-dark .pv-card p{color:rgba(240,245,246,.75)}
.pv-viz{margin:-6px -6px 22px;height:142px}
.pv-viz svg{width:100%;height:100%;display:block}
.pv-viz path{stroke:var(--gray-dark);stroke-width:1.6}
.pv-viz .pv-viz-y{stroke:var(--yellow);stroke-width:2.2}
.pv-viz .pv-viz-base{stroke:rgba(240,245,246,.15)}
.pv-viz-t{font:500 10.5px ui-monospace,monospace;fill:var(--gray-medium)}
.pv-viz-dot{fill:var(--yellow)}
.pv-viz-dot2{fill:#fff}
.pv-viz-loop{stroke:var(--yellow);stroke-width:2;stroke-dasharray:6 7}
.pv-spin{transform-origin:130px 55px;animation:pvSpin 14s linear infinite}
@keyframes pvSpin{to{transform:rotate(360deg)}}
/* steps connector */
.pv-steps-wrap{position:relative}

/* MIT bars */
.pv-bars{margin-top:22px;display:grid;gap:12px}
.pv-bar{display:grid;grid-template-columns:1fr;gap:6px}
@media(min-width:600px){.pv-bar{grid-template-columns:190px 1fr 170px;align-items:center;gap:14px}}
.pv-bar-l{font-size:14px;color:var(--charcoal)}
.pv-bar-t{height:14px;border-radius:7px;background:var(--gray-light);overflow:hidden}
.pv-bar-t i{display:block;height:100%;width:var(--w);border-radius:7px;background:var(--yellow);transform-origin:left;transform:scaleX(0);transition:transform 1.2s var(--ease) .2s}
.pv-bar:last-child .pv-bar-t i{background:var(--gray-medium)}
.in-view .pv-bar-t i,.no-js .pv-bar-t i{transform:none}
.pv-bar-v{font:500 12.5px ui-monospace,monospace;color:var(--charcoal);white-space:nowrap}
@media(prefers-reduced-motion:reduce){.pv-float,.pv-spin{animation:none}.pv-bar-t i{transform:none;transition:none}}
.pv-card-h{display:flex;align-items:flex-start;gap:14px;margin-bottom:14px}
.pv-card-h h3{margin:0!important}
.pv-card-h .pv-ico+h3{padding-top:9px}
.pv-card-h .pv-num+h3{padding-top:4px}
.pv-card-h .pv-ico,.pv-card-h .pv-num{flex:none;margin:0}
.pv-row>.pv-card>.pv-card-h{margin-bottom:14px;align-self:start}
.pv-row>.pv-card>.pv-viz{margin-bottom:36px}
/* product views from the video kit */
.pv-demo{margin:18px 0 0;font:500 11px/1.4 ui-monospace,monospace;letter-spacing:.04em;color:var(--gray-dark)}
.pv-demo-dark{color:var(--gray-medium)}
.pv-iv-band{fill:rgba(86,209,138,.12);stroke:rgba(86,209,138,.35)}
.pv-iv-lost{fill:rgba(255,90,90,.18)}
.pv-viz path.pv-iv-ln{stroke:#fff;stroke-width:2}
.pv-viz path.pv-iv-on{stroke:var(--yellow);stroke-width:2.2;stroke-dasharray:6 5}
.pv-red{fill:#FF8A8A}
.pv-toasts{display:grid;gap:6px;height:100%;align-content:start;overflow:hidden}
.pv-toast{display:flex;align-items:center;justify-content:space-between;gap:8px;background:#1F2122;border:1px solid rgba(240,245,246,.1);border-radius:10px;padding:5px 9px;animation:pvToast 9s ease-in-out infinite}
.pv-toast:nth-child(2){animation-delay:1.2s}.pv-toast:nth-child(3){animation-delay:2.4s}
.pv-toast b{display:block;font-size:12px;color:#fff;font-weight:600;line-height:1.3}
.pv-toast small{display:block;font-size:11px;color:var(--gray-medium);line-height:1.3}
.pv-toast em{font:normal 600 10px ui-monospace,monospace;color:var(--black);background:var(--yellow);border-radius:6px;padding:3px 6px;white-space:nowrap}
@keyframes pvToast{0%,6%{opacity:.25;transform:translateX(-6px)}12%,80%{opacity:1;transform:none}92%,100%{opacity:.25}}
.pv-viz-step{height:auto;margin:0 0 22px;align-self:stretch}
.pv-viz-step .pv-sv{height:100%;box-sizing:border-box}
.pv-sv{border-radius:12px;background:var(--gray-light);padding:12px;font-size:11.5px;line-height:1.35;min-height:96px}
.pv-sv-learn{display:grid;gap:5px}
.pv-sv-rules{display:grid;gap:5px}
.pv-sv-rules div:not(.pv-sv-h){background:#fff;border-radius:7px;padding:5px 8px;display:grid;grid-template-columns:auto 1fr;gap:8px;align-items:baseline}
.pv-sv-rules b{font-size:11px;font-weight:600;white-space:nowrap}
.pv-sv-rules span{font:500 10.5px/1.35 ui-monospace,monospace;color:var(--charcoal)}
.pv-card p.pv-sv-tags{display:flex;flex-wrap:wrap;gap:4px;margin:3px 0 0;font-size:10.5px;line-height:1.2}
.pv-sv-tags i{font-style:normal;padding:3px 7px;border-radius:999px;background:var(--black);color:#fff}
.pv-sv-rules .pv-sv-h,.pv-sv-learn .pv-sv-h{display:block;background:none;padding:0;margin:0 0 2px;font:500 10px ui-monospace,monospace;letter-spacing:.04em;color:var(--gray-dark)}
.pv-sv-learn .pv-sv-h{display:block;background:none;padding:0;margin:0 0 2px;font:500 10px ui-monospace,monospace;letter-spacing:.04em;color:var(--gray-dark)}
.pv-sv-learn div{background:#fff;border-radius:7px;padding:5px 8px;display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.pv-sv-learn b{font-size:11px;font-weight:600}
.pv-sv-learn span{color:var(--charcoal);font-size:10.5px}
.pv-sv-top{display:flex;align-items:center;gap:8px;background:var(--black);color:#fff;border-radius:8px;padding:7px 8px;flex-wrap:wrap}
.pv-sv-logo{border:1px dashed rgba(255,255,255,.5);border-radius:5px;padding:2px 6px;font-size:10px;color:var(--yellow)}
.pv-sv-top b{font-size:11px;font-weight:600}
.pv-sv-url{margin-left:auto;font:500 10px ui-monospace,monospace;color:var(--gray-medium)}
.pv-sv-sw{display:flex;align-items:center;gap:6px;margin-top:10px}
.pv-sv-sw i{width:18px;height:18px;border-radius:5px;background:#3D5AFE}
.pv-sv-sw i:nth-child(2){background:#2BB673}.pv-sv-sw i:nth-child(3){background:var(--yellow)}
.pv-sv-sw span{margin-left:4px;color:var(--charcoal)}
.pv-stg{display:grid;grid-template-columns:repeat(5,1fr);gap:4px}
.pv-stg span{position:relative;text-align:center;padding:7px 2px;border-radius:7px;background:#fff;font-size:10.5px;color:var(--charcoal);animation:pvStage 7.5s linear infinite}
.pv-stg span:nth-child(2){animation-delay:1s}.pv-stg span:nth-child(3){animation-delay:2s}.pv-stg span:nth-child(4){animation-delay:3s}.pv-stg span:nth-child(5){animation-delay:4s}
@keyframes pvStage{0%{background:#fff;color:var(--charcoal)}6%,70%{background:var(--yellow);color:var(--black)}80%,100%{background:#fff;color:var(--charcoal)}}
.pv-sv-chip{display:inline-block;margin-top:10px;padding:4px 9px;border-radius:999px;background:rgba(43,182,115,.14);color:#167A4B;font-weight:600;font-size:11px}
.pv-float-a{max-width:300px}
@media(prefers-reduced-motion:reduce){.pv-toast,.pv-stg span{animation:none}}
/* hero to logo strip: tighter so the logos show in the first screen */
#main>.hero{padding-top:clamp(32px,4.5vw,64px);padding-bottom:clamp(24px,3vw,40px)}
#main>.logos-band .logos-block{padding-top:clamp(12px,1.5vw,20px)}
.pv-final{text-align:center}
.pv-final .h2{max-width:760px;margin:20px auto 0}
.pv-final .pv-actions{justify-content:center}
</style>"""


def card(title: str, body: str, extra: str = "", lead: str = "", side: str = "") -> str:
    if side:
        return f'''          <article class="pv-card">
            <div class="pv-card-h">{side}<h3>{title}</h3></div>
            <p>{body}</p>{extra}
          </article>'''
    return f'''          <article class="pv-card">{lead}
            <h3>{title}</h3>
            <p>{body}</p>{extra}
          </article>'''


GAP = [
    ("AI is changing how you plan",
     "Forecasts can now take in everything a business knows, not only its sales history. Routine work runs on its own, and every cycle feeds what was learned back in, so each plan is sharper than the last."),
    ("Few know how to get there",
     "AI is in every board meeting, conference and newsletter. Your team sees the potential, but between daily firefighting and the next purchase order, nobody has the time or the knowledge to bring it into how your business plans."),
    ("First movers will win",
     "While most brands are still working out where to start, the ones that take planning and operations to the next level first will move faster, react sooner and build an advantage that grows every cycle."),
]

ERA = [
    ("Data and context without limits",
     "Not just sales, inventory and purchase orders. Add marketing plans, cash flow, competitive information and the reasons behind past decisions. Flieber’s AI takes all of it into account in every forecast and plan, so your decisions reflect how your business really works, not just what your systems record."),
    ("Automations that get smarter",
     "Flieber specialists gather context from everyone involved in your business, from finance to marketing to operations, and bring what they’ve learned from more than 1,000 brands. They turn it into automations that take the routine off your team and improve with every cycle, so your people spend their time growing the brand, not running the process."),
    ("Intelligence that compounds",
     "Every exception resolved, every plan approved and every outcome observed feeds back in. Insights build on each other and alerts get sharper, so each cycle you plan with more confidence than the last, and what your team learns stays even when people change."),
]

STEPS = [
    ("We learn how you operate",
     "Our team connects your data and creates a routine of interactions with yours to continuously capture the context behind your numbers, from finance to marketing to operations. Within the first month, you already start seeing measurable value."),
    ("We tailor your platform",
     "You get your own version of Flieber, with your logo and colors, tailored to your use cases and how your team operates. Forecasting models are fine-tuned to your catalog, and new products and wholesale channels are handled by specialized tools. Views, alerts and workflows follow your preferences. When a new need comes up, it becomes part of your platform instead of a spreadsheet workaround or a long wait on the roadmap of a generic system."),
    ("We stay, and it keeps getting smarter",
     "Your Flieber specialists stay with your account, learning from the different people in your team. Each cycle, new opportunities are detected and more of the routine moves onto automations. Every plan is reviewed with your team before money goes out, and every month you get a scorecard on the measures that show your progress."),
]

MOMENTS = [
    ("A planner leaves or changes roles", "“The person who knew how all this works is gone.”",
     "What they knew is captured in your system, so the intelligence stays when people change."),
    ("A new channel, retailer or wholesale account", "“We just added Amazon, TikTok Shop, a big retailer.”",
     "We plan every channel from one picture, including wholesale and launches with no sales history."),
    ("A system dies or changes", "“Our planning tool shut down.” “We’re moving ERP or warehouse.”",
     "We set up around your new systems and keep planning running through the switch."),
    ("Fast growth", "“We’re aiming to double, and the way we plan won’t hold.”",
     "Planning scales with you: the routine runs on its own, and your team stays focused on the calls."),
    ("An inventory scare", "“We ran out of our bestseller.” “We’re sitting on months of stock.”",
     "Risks are flagged before they hit your shelves or your cash, and every plan is checked before money goes out."),
    ("A push to use AI", "“The board asked what we’re doing with AI.”",
     "A clear path into AI for your operation, with people who’ve done it for more than 1,000 brands."),
]

FAQ = [
    ("I already have a great team.",
     "Good, because Flieber works through them, not around them. Your team keeps every decision and every relationship with suppliers and partners. What changes is the work around those decisions: data checks, plan preparation and follow-ups move onto automations, new context reaches them every day, and they get specialists who have seen how more than 1,000 brands solve the same problems. Most teams are not short on talent; they are short on time."),
    ("Why not build this ourselves with AI?",
     "You can, and some brands try. The first version is usually exciting. The hard part comes after: every new use case, team change and data source adds upkeep, until maintaining the tool becomes someone’s full-time job. MIT found that partnering with specialists succeeds about three times as often as building in-house. With Flieber you start from what works across more than 1,000 brands, and the upkeep is ours."),
    ("What exactly do your specialists do?",
     "They create a routine of interactions with your team, which can go as far as joining your planning and S&amp;OP meetings if you want them there. Through it, they gather context from finance, marketing and operations and make sure your platform has it. They keep your data and setup right as your business changes, review plans with your team before money goes out, and find the opportunities for better data and automation in how you work. Behind your main contacts is a wider team with experience at the intersection of planning, operations and technology."),
    ("Do I lose control?",
     "No. Your team approves every plan and every order, and nothing moves without that approval. You also decide how much the specialists take on: some brands start with a second set of eyes on their plans, others hand over the whole planning preparation, and you can change that as trust builds."),
    ("Do your specialists leave after setup?",
     "No. Once your platform is set up, the specialists stay with your account. Their ongoing work is what makes the automations learn and the intelligence compound."),
    ("How do I know it’s working?",
     "Every month you get a scorecard on the measures you agree on with us at the start. You also see the work directly: plans reviewed, exceptions resolved and routine moved onto automations."),
    ("Why does it cost more than software?",
     "Because you’re not buying a tool your team then has to make work. You get three things software alone doesn’t give you. A platform tailored to your brand, with your products, channels, suppliers and rules built in. Specialists who keep it right as your business changes, review plans with your team and turn recurring work into automations. And what we’ve learned from more than 1,000 brands, so you start from what works instead of from scratch. Compare it with what the alternatives really cost: the time your team spends working around a generic tool, a new hire to run the process, or an in-house app someone has to maintain. Inventory shapes your advertising, promotions and cash flow, and one avoided stockout or overstock on a bestseller can pay for a year."),
    ("I just want software. I don’t want to pay for a team.",
     "We understand, and for years we sold Flieber that way. Here’s what we learned from more than 1,000 brands: software that has to fit everyone leaves gaps. Each brand used a small slice of it and filled the rest with spreadsheets and workarounds, so planning still depended on a few people’s heads. The specialists aren’t a team added on top of the software. They work with your team to make every planning cycle more streamlined and complete: they bring best practices from what works across other brands, act as a second set of eyes before money goes out, and find where better data or automation will help, building it into your platform as your business changes. They don’t replace your team or take your decisions. You decide how involved they get, from reviewing your plans to preparing the whole planning cycle for your team’s approval."),
    ("What happens in the first month?",
     "We get everything ready for you to plan on a solid foundation. Our team learns how you operate and gathers the context behind your numbers from the people involved, from finance to marketing to operations. We connect your data, map your products, channels and suppliers, and make the platform your own: views, alerts, workflows and forecasting set up around your use cases and preferences. Together we define the main gaps to close and the indicators we’ll follow. Within the first month, you already start seeing measurable value, and every cycle after that builds on it."),
]

INTEGRATIONS = ["Amazon", "Shopify", "Walmart", "NetSuite", "Flexport", "Google Sheets"]


def head(kicker: str, h2: str, hid: str, lead: str = "") -> str:
    lead_html = f'\n          <p class="lead">{lead}</p>' if lead else ""
    return f'''        <div class="section-head reveal">
          <span class="kicker">{kicker}</span>
          <h2 class="h2" id="{hid}" style="margin-top:20px">{h2}</h2>{lead_html}
        </div>'''


def live_part(start: str, end: str) -> str:
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    s = src.index(start)
    return src[s:src.index(end, s) + len(end)]


RESULTS = [("↑", "38%", "more sales"), ("↓", "62%", "fewer stockouts"),
           ("↓", "17%", "less excess inventory"), ("↓", "88%", "less time on replenishment decisions")]

TEAM = [
    ("Former operators", "People who have planned and run operations at commerce brands themselves."),
    ("A senior AI team", "The engineers and data scientists behind your models and automations."),
    ("Process consultants", "Experience improving how planning teams work, not only what tools they use."),
]


GAP_ICONS = [
    '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/>',
    '<circle cx="12" cy="12" r="9"/><path d="M15.6 8.4l-2.1 5.1-5.1 2.1 2.1-5.1z"/>',
    '<path d="M6 21V4"/><path d="M6 4h12l-2.5 4.5L18 13H6"/>',
]


def icon(i: int) -> str:
    return (f'\n            <span class="pv-ico" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round">{GAP_ICONS[i]}</svg></span>')


ERA_VIZ = [
    # data and context: many streams converging into one plan
    """<svg viewBox="0 0 260 110" fill="none">
              <text x="6" y="17" class="pv-viz-t">sales</text><text x="6" y="43" class="pv-viz-t">marketing</text>
              <text x="6" y="69" class="pv-viz-t">cash</text><text x="6" y="95" class="pv-viz-t">past decisions</text>
              <path class="viz-draw" d="M104 14 C150 14 150 56 196 56"/><path class="viz-draw" d="M104 40 C150 40 150 56 196 56"/>
              <path class="viz-draw" d="M104 66 C150 66 150 56 196 56"/><path class="viz-draw" d="M104 92 C150 92 150 56 196 56"/>
              <path class="viz-draw pv-viz-y" d="M206 56 H252"/><circle cx="200" cy="56" r="9" class="pv-viz-dot"/>
            </svg>""",
    # automations: a loop that keeps turning
    """<svg viewBox="0 0 260 110" fill="none">
              <g class="pv-spin"><circle cx="130" cy="55" r="38" class="pv-viz-loop"/>
              <circle cx="130" cy="17" r="5" class="pv-viz-dot"/><circle cx="163" cy="74" r="5" class="pv-viz-dot2"/><circle cx="97" cy="74" r="5" class="pv-viz-dot2"/></g>
              <text x="130" y="59" text-anchor="middle" class="pv-viz-t">every cycle</text>
            </svg>""",
    # intelligence: a curve that compounds
    """<svg viewBox="0 0 260 110" fill="none">
              <path d="M10 100 H252" class="pv-viz-base"/>
              <path class="viz-draw pv-viz-y" d="M12 96 C70 94 110 86 150 66 S220 22 250 10"/>
              <circle cx="70" cy="92" r="3.5" class="pv-viz-dot2"/><circle cx="150" cy="66" r="3.5" class="pv-viz-dot2"/><circle cx="250" cy="10" r="5" class="pv-viz-dot"/>
            </svg>""",
]


DEMO_NOTE = "Illustration · Flieber Demo Account · fictional products and people"


def inv_chart() -> str:
    """Mini Inventory Forecast, same simulation as the videos: stock runs out, the approved plan adds a dashed on-order line."""
    n, dem, avg = 120, 30, 30
    def sim(inb):
        s, st = 1500, []
        for k in range(n):
            for d, q in inb:
                if k == d: s += q
            s = max(0, s - dem); st.append(s)
        return st
    if0, if1 = sim([]), sim([(58, 3000)])
    x = lambda k: 8 + k * 244 / (n - 1)
    y = lambda v: 100 - min(1, v / 3200) * 80
    path = lambda st, a, b: "M" + " L".join(f"{x(k):.1f} {y(v):.1f}" for k, v in enumerate(st) if a <= k <= b)
    band = f'<rect x="8" width="244" y="{y(50*avg):.1f}" height="{y(21*avg)-y(50*avg):.1f}" class="pv-iv-band"/>'
    lost = f'<rect x="{x(50):.1f}" width="{x(58)-x(50):.1f}" y="18" height="82" class="pv-iv-lost"/>'
    return f"""<svg viewBox="0 0 260 110" fill="none">{band}{lost}
              <path d="M8 100 H252" class="pv-viz-base"/>
              <path class="viz-draw pv-iv-ln" d="{path(if0, 0, 57)}"/>
              <path class="pv-iv-on" d="{path(if1, 57, n - 1)}"/>
              <path d="M{x(58)-6:.1f} 4 L{x(58)+6:.1f} 4 L{x(58):.1f} 13Z" class="pv-viz-dot"/>
              <text x="{x(61):.1f}" y="12" class="pv-viz-t">on order</text>
              <text x="250" y="{y(21*avg)-4:.1f}" text-anchor="end" class="pv-viz-t">safety</text>
              <text x="{x(49):.1f}" y="30" text-anchor="end" class="pv-viz-t pv-red">stockout</text>
            </svg>"""


TOASTS = [("Draft ready", "Supplier 1 · 14 products · $47,750", "Flieber"),
          ("Draft ready", "3PL US → FBA US · 5 pallets + 1 by air", "Slack"),
          ("2 items need you", "Supplier 1 · Dec 2026", "Claude")]


def toasts() -> str:
    rows = "".join(f'<div class="pv-toast"><span><b>{h}</b><small>{d}</small></span><em>{s}</em></div>' for h, d, s in TOASTS)
    return f'<div class="pv-toasts">{rows}</div>'


def viz(i: int) -> str:
    inner = ERA_VIZ[0] if i == 0 else toasts() if i == 1 else inv_chart()
    return f'\n            <div class="pv-viz" aria-hidden="true">{inner}</div>'


STEP_VIEWS = [
    """<div class="pv-sv pv-sv-learn"><div class="pv-sv-h">At setup · we learn how your company works</div>
              <div><b>Your team</b><span>How you plan · who approves what</span></div>
              <div><b>Your integrations</b><span>Amazon · Shopify · your ERP · your 3PL</span></div>
              <div><b>Your AI agents</b><span>Your rules · your notes · your history</span></div></div>""",
    """<div class="pv-sv pv-sv-rules"><div class="pv-sv-h">Your platform · fine-tuned to how you operate</div>
              <div><b>Supplier 1</b><span>every 4 weeks · cover 120 days · full cartons · round up to MOQ if within 10%</span></div>
              <div><b>Supplier 2</b><span>every 6 weeks · cover 90 days · full containers</span></div>
              <div><b>3PL US → FBA US</b><span>weekly · by the pallet</span></div>
              <p class="pv-sv-tags"><i>Rules in your own words</i><i>Combined MOQs</i><i>Launches</i><i>Wholesale</i><i>Your approval stages</i></p></div>""",
    """<div class="pv-sv pv-sv-stages"><div class="pv-stg"><span>Draft</span><span>In review</span><span>Ops</span><span>Finance</span><span>Approved</span></div>
              <div class="pv-sv-chip">Engine improved · your platform gets it too</div></div>""",
]


def row(cards: str, span: int) -> str:
    return f'''        <div class="pv-3 pv-row pv-span{span} reveal-stagger">
{cards}
        </div>'''


def main_html() -> str:
    gap = "\n".join(card(t, b, side=icon(i).strip()) for i, (t, b) in enumerate(GAP))
    era = "\n".join(card(t, b, lead=viz(i)) for i, (t, b) in enumerate(ERA))
    steps = "\n".join(card(t, b, side=f'<span class="pv-num" aria-hidden="true">{i}</span>').replace('<article class="pv-card">', f'<article class="pv-card">\n            <div class="pv-viz pv-viz-step" aria-hidden="true">{STEP_VIEWS[i-1]}</div>', 1) for i, (t, b) in enumerate(STEPS, 1))
    moments = "\n".join(f'''          <article class="pv-card pv-moment">
            <span class="pv-tag">{m}</span>
            <blockquote>{q}</blockquote>
            <p>{a}</p>
          </article>''' for m, q, a in MOMENTS)
    faq = "\n".join(f'''          <details>
            <summary>{q}<span class="plus" aria-hidden="true"></span></summary>
            <p>{a}</p>
          </details>''' for q, a in FAQ)
    logos = live_part('    <section class="logos-band"', "    </section>").replace(
        '<p class="logos-label" id="logos-label">Trusted by hundreds of brands</p>',
        '<p class="logos-label" id="logos-label">Brands that plan with Flieber</p>')
    results = "".join(f'<div class="pv-res-i"><span class="pv-res-n">{arrow}{n}</span><span class="pv-res-l">{l}</span></div>'
                      for arrow, n, l in RESULTS)
    quotes = live_part('        <div class="quotes reveal" id="quotes"', "            </div>\n          </div>\n        </div>")
    team = "".join(f'<div class="pv-team-i"><b>{n}</b><span>{d}</span></div>' for n, d in TEAM)
    buttons = f'''<a class="btn btn-primary" href="{BOOK}">Talk to a specialist {ARROW}</a>
              <a class="btn btn-ghost" href="{BOOK}">Book a demo</a>'''
    return f'''  <main id="main">

    <!-- Hero -->
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap">
        <div class="pv-hero-grid">
          <div>
            <h1 class="h1" id="hero-title">AI that powers decisions.<span class="pv-br"></span> Humans who shape it around your business</h1>
            <p class="lead">Planning is entering a new era: automations that learn, data and context without limits, intelligence that compounds. Flieber takes your inventory decisions there, with a platform tailored to your brand and specialists who’ve seen how more than 1,000 brands operate.</p>
            <div class="pv-actions">
              {buttons}
            </div>
          </div>
          <div class="pv-stage">
            <div class="pv-float pv-float-a" aria-hidden="true"><span class="pv-dot"></span><span><b>Draft ready</b><br>Supplier 1 · Dec 2026 · 14 products · $47,750</span></div>
          <figure class="pv-video" aria-label="Hero video placeholder">
            <span class="pv-play" aria-hidden="true"><svg width="22" height="24" viewBox="0 0 22 24"><path d="M2 2l18 10L2 22z" fill="#1B1C1C"/></svg></span>
            <p><span class="pv-ph">Placeholder</span><br><b>Hero video, about 60 to 75 seconds.</b> The shift, the gap, the bridge, smarter every cycle, then “{SHORT}” Plays with captions so it works with the sound off.</p>
          </figure>
            <div class="pv-float pv-float-b" aria-hidden="true"><span><b>ALMN-CRON-LUGG below MOQ 500</b><br>Round up: +$1,440, +32 days of cover</span><span class="pv-approve">Round up</span></div>
            <span class="pv-illus" aria-hidden="true">Illustration · Flieber Demo Account</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Customer logos, as on the live homepage -->
{logos}

    <!-- Why now? The gap -->
    <section class="section section-soft" id="why-now" aria-labelledby="gap-title">
      <div class="wrap">
{head("The gap", "Why now?", "gap-title")}
{row(gap, 2)}
      </div>
    </section>

    <!-- What changes? The new era of planning -->
    <section class="section on-dark pv-dark" id="what-changes" aria-labelledby="era-title">
      <div class="wrap">
{head("The new era of planning", "What changes?", "era-title")}
{row(era, 3)}
        <p class="pv-demo pv-demo-dark reveal">{DEMO_NOTE}</p>
      </div>
    </section>

    <!-- How do we get there? -->
    <section class="section section-soft" id="how-flieber-gets-you-there" aria-labelledby="how-title">
      <div class="wrap">
{head("How Flieber gets you there", "How do we get there?", "how-title")}
<div class="pv-steps-wrap">
{row(steps, 3)}
        </div>
        <p class="pv-demo reveal">{DEMO_NOTE}</p>
      </div>
    </section>

    <!-- Why not just buy or build software? -->
    <section class="section" id="why-not-software-alone" aria-labelledby="build-title">
      <div class="wrap">
        <div class="pv-build reveal">
          <div class="reveal">
            <span class="kicker">Why software alone isn’t enough anymore</span>
            <h2 class="h2" id="build-title" style="margin-top:20px">Why not just buy or build software?</h2>
          </div>
          <div class="reveal">
            <p class="lead">For years, software had to fit every customer the same way. Each brand used a small slice of it and filled the gaps with spreadsheets. AI changed that: a platform can now be tailored to each brand, and the value comes from shaping it around how you work. That takes people who know the work, which is why Flieber now comes with the specialists who shape it, and why we no longer sell the software on its own.</p>
            <p class="lead" style="margin-top:18px">Building it yourself is the other route, and it rarely holds: MIT’s study <i>The GenAI Divide: State of AI in Business 2025</i> found that partnering with specialists succeeds about three times as often as building in-house.</p>
            <div class="pv-bars" aria-hidden="true">
              <div class="pv-bar"><span class="pv-bar-l">Partnering with specialists</span><span class="pv-bar-t"><i style="--w:100%"></i></span><span class="pv-bar-v">about 67%</span></div>
              <div class="pv-bar"><span class="pv-bar-l">Building in-house</span><span class="pv-bar-t"><i style="--w:33%"></i></span><span class="pv-bar-v">about a third as often</span></div>
            </div>
            <p class="pv-cite">Source: MIT NANDA, <i>The GenAI Divide: State of AI in Business 2025</i>. Vendor and partnership routes succeeded about 67% of the time, and internal builds about a third as often (<a href="{MIT_URL}" rel="noopener" target="_blank">as reported by Fortune</a>). This is an outside study, not a Flieber result.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Is this for me? -->
    <section class="section section-soft" id="when-brands-bring-us-in" aria-labelledby="moments-title">
      <div class="wrap">
{head("When brands bring us in", "Is this for me?", "moments-title")}
        <div class="pv-moments pv-row pv-span3 reveal-stagger">
{moments}
        </div>
      </div>
    </section>

    <!-- Can I trust you? -->
    <section class="section" id="proof" aria-labelledby="proof-title">
      <div class="wrap">
{head("Proof", "Can I trust you?", "proof-title")}
        <div class="pv-proof reveal">
          <div class="pv-proof-l">
            <h3 class="pv-sub">Experience</h3>
            <div class="pv-exp"><span class="pv-res-n">1,000+</span><span class="pv-res-l">brands have used Flieber since 2019</span></div>
          </div>
          <div class="pv-proof-r">
            <h3 class="pv-sub">What brands see after 12 months or more</h3>
            <div class="pv-res">{results}</div>
          </div>
        </div>
        <p class="pv-cite pv-proof-note">Results are averages across customers using Flieber for 12 months or more. Not a guarantee for every brand.</p>
        <div class="pv-teamband reveal">
          <div>
            <h3 class="pv-sub" style="margin-top:0">The team behind your account</h3>
            <p class="pv-team-lead">Experience at the intersection of planning, operations and technology.</p>
          </div>
          <div class="pv-team">{team}</div>
        </div>
      </div>
    </section>

    <!-- Customer voices -->
    <section class="section pv-voices" id="customer-quotes" aria-label="What customers say">
      <div class="wrap">
{quotes}
      </div>
    </section>

    <!-- What else should I know? -->
    <section class="section section-soft" id="questions" aria-labelledby="questions-title">
      <div class="wrap">
{head("Questions", "What else should I know?", "questions-title")}
        <div class="faq">
{faq}
        </div>
      </div>
    </section>

    <!-- Final call to action -->
    <section class="section pv-final" id="talk-to-a-specialist" aria-labelledby="final-title">
      <div class="wrap">
        <h2 class="h2" id="final-title">See what your planning looks like in the new era</h2>
        <div class="pv-actions">
          {buttons}
        </div>
      </div>
    </section>
  </main>
'''


def rep(t: str, a: str, b: str) -> str:
    assert t.count(a) == 1, f"expected once: {a[:70]}"
    return t.replace(a, b)


def main() -> None:
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    top = src[:src.index("  <main id=\"main\">")]
    bottom = src[src.index("  </main>") + len("  </main>\n"):]

    top = re.sub(r"<title>[^<]*</title>", f"<title>{TAGLINE[:-1]}</title>", top, count=1)
    top = re.sub(r'(<meta name="description" content=")[^"]*', r"\1" + TAGLINE + " Your team keeps every call.", top, count=1)
    top = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\1" + TAGLINE[:-1], top, count=1)
    top = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\1A planning platform tailored to your brand, with specialists who work with your team. Your team keeps every call.", top, count=1)
    top = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", top, count=1, flags=re.S)
    top = re.sub(r'<div class="review-bar"[^>]*>.*?</div>', '<div class="review-bar" role="note">Review build · <b>Positioning</b> · brief as written (doc rev 98) · V16</div>', top, count=1, flags=re.S)
    top = top.replace("</head>", CSS + "\n</head>", 1)
    # Nav: one product, the team inside the copy, Self-Serve as the secondary path.
    nav = re.search(r'<nav class="nav-links" aria-label="Primary">.*?</nav>', top, flags=re.S).group(0)
    top = top.replace(nav, f'''<nav class="nav-links" aria-label="Primary">
        <a href="#how-flieber-gets-you-there">How it works</a>
        <a href="#when-brands-bring-us-in">When brands bring us in</a>
        <a href="#questions">Questions</a>
        <a href="who-we-are/">Who we are</a>
        <a class="menu-only" href="https://app.flieber.com">Log in</a>
        <a class="menu-only" href="{BOOK}">Talk to a specialist</a>
      </nav>''')
    cta = re.search(r'<div class="nav-cta">.*?<button class="nav-toggle"', top, flags=re.S).group(0)
    top = top.replace(cta, f'''<div class="nav-cta">
        <a class="nav-login" href="https://app.flieber.com">Log in</a>
        <a class="btn btn-primary btn-sm" href="{BOOK}">Talk to a specialist</a>
        <button class="nav-toggle"''')

    bottom = re.sub(r'\s*<div class="footer-mark"[^>]*>.*?</div>', '', bottom, count=1, flags=re.S)
    bottom = rep(bottom, '<p class="tagline">The inventory intelligence layer <em>your agents run on.</em></p>',
                 '<p class="tagline">Flieber: where AI meets <em>inventory experts.</em></p>')
    bottom = rep(bottom, '            <li><a href="managed-services/">Managed Services</a></li>\n', '')

    page = top + main_html() + bottom
    for bad in ("Managed Services", "managed-services", "Lite", "Core,", "Full plan", "—", "Flieber Studio", "Flieber Inventory", "alongside", "run by Flieber", "Managed", "dashboard", "single source of truth", "visibility", "planning system", "Self-Serve", "Beyond inventory"):
        assert bad not in page, f"brief rule broken: {bad}"
    OUT.write_text(page, encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
