FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
# Only the public site files are served; README, Dockerfile etc. stay out.
COPY index.html robots.txt sitemap.xml llms.txt llms-full.txt capabilities.json /srv/
COPY agents /srv/agents
COPY features /srv/features
COPY pricing /srv/pricing
COPY security /srv/security
COPY contact /srv/contact
COPY solutions /srv/solutions
COPY assets /srv/assets
