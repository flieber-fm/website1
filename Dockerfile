FROM caddy:2-alpine
COPY Caddyfile /etc/caddy/Caddyfile
# Only the public site files are served; README, Dockerfile etc. stay out.
COPY index.html robots.txt sitemap.xml llms.txt llms-full.txt capabilities.json /srv/
COPY agents /srv/agents
COPY features /srv/features
COPY pricing /srv/pricing
COPY security /srv/security
COPY contact /srv/contact
COPY product /srv/product
COPY multichannel /srv/multichannel
COPY agencies /srv/agencies
COPY before-you-choose /srv/before-you-choose
COPY mcp /srv/mcp
COPY build-with-ai /srv/build-with-ai
COPY use-cases /srv/use-cases
COPY integrations /srv/integrations
COPY managed-services /srv/managed-services
COPY who-we-are /srv/who-we-are
COPY assets /srv/assets
