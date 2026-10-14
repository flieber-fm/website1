FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
# Option 7: homepage, /security, /agents, the agent files and the /review guide (preview only).
# README, Dockerfile etc. stay out.
COPY index.html robots.txt sitemap.xml llms.txt capabilities.json /srv/
COPY security /srv/security
COPY agents /srv/agents
COPY review /srv/review
COPY assets /srv/assets
