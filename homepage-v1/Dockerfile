FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
# Only the public site files are served; README and Dockerfile stay out.
COPY index.html /srv/
COPY assets /srv/assets
