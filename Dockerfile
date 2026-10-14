FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
# Option 6: one focused homepage plus /security. README, Dockerfile etc. stay out.
COPY index.html robots.txt sitemap.xml /srv/
COPY security /srv/security
COPY assets /srv/assets
