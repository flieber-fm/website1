# Homepage v1 (Oct 13 positioning)

Review build of the new flieber.com homepage, built on the Option 2 prototype's design system (`site.css`, `site.js`, fonts and logos copied unchanged from `claude/eager-bohr-ui8a03`). `assets/css/v1.css` adds only the new components: the hero tool toggle, the Run and Build cards, the role cards, the decision hub and the "What AI changes" grid.

Copy source: the Claude Doc "Flieber homepage: structure and copy" and `docs/26-10-13-website-positioning-review.md`.

- Sections: hero, logos, why it's different (scroll-driven three-layer stack), two ways to get started (Run and Build), every decision is an inventory decision, the old way, what AI changes, your rules, proof, from the founder, start free, footer.
- "To confirm" tags mark claims not yet approved: per-brand environment, coding-agent connection, open code, Build pricing, trial findings, the logo label and the founder statement.
- Links to pages that exist only on Option 2 point to the Option 2 preview. Pages not built yet (/run, /build, docs, AI specialists) are placeholders.
- `noindex, nofollow`. Serve the folder with any static server, for example `python3 -m http.server`.
