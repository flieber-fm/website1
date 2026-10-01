FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
# Only the public site files are served; README, Dockerfile etc. stay out.
COPY index.html robots.txt sitemap.xml llms.txt capabilities.json /srv/
COPY agents /srv/agents
COPY pricing /srv/pricing
COPY assets /srv/assets
