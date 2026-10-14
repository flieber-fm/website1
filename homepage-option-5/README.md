# Homepage Option 5 (service-led, after the Comp benchmark)

Review build of a Comp-style flieber.com homepage that gives more weight to service: planners who co-lead the planning, AI specialists who shape the tools and the platform underneath. Built on the Option 2 design system, copied from `homepage-v1/` (`site.css`, `v1.css`, `site.js`, `v1.js`, fonts, images and logos unchanged). `assets/css/o5.css` adds only the new components: the hero team card, the three partner panels (org chart, static five-layer stack), the four ways and the three steps.

Copy sources: `docs/26-10-13-website-positioning-review.md`, `docs/26-10-13-approved-claims-addendum.md`, the Option 2 Technical Briefing and /managed-services page (branch `claude/eager-bohr-ui8a03`) and `homepage-v1/index.html` (Option 4) for the scenario tool, proof, founder statement and trial findings.

- Sections: hero, logos, the old way (three failure modes), your partner (planners, AI specialists, the platform, four ways in), how it works (three steps), proof, from the founder, talk to a planner, footer.
- "To confirm" tags mark claims that are not approved yet: "end to end", the planner-reviewed health check and "Our planners work on Flieber, not on spreadsheets".
- Links to pages that exist only on Option 2 point to the Option 2 preview. "Talk to a planner" goes to book-a-demo, as on Option 2's /managed-services.
- `noindex, nofollow`. Serve the folder with any static server, for example `python3 -m http.server`. No Railway service until Fabricio approves.
