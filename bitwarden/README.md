# bitwarden

The [Vaultwarden](https://github.com/dani-garcia/vaultwarden) project (formerly known as bitwarden_rs) provides a lightweight, single-process, API-compatible service alternative to [Bitwarden](https://bitwarden.com/). [Vaultwarden](https://bitwarden.com/) is an open source password management application that can be self-hosted and run on your infrastructure.



Caddyfile:

```
# Caddyfile
{$DOMAIN} {
    tls {$EMAIL}

    header / {
        # Enable HTTP Strict Transport Security (HSTS)
        Strict-Transport-Security "max-age=31536000;"
        # Enable cross-site filter (XSS) and tell browser to block detected attacks
        X-XSS-Protection "1; mode=block"
        # Disallow the site to be rendered within a frame (clickjacking protection)
        X-Frame-Options "DENY"
        # Prevent search engines from indexing (optional)
        #X-Robots-Tag "none"
    }

    # The negotiation endpoint is also proxied to Rocket
    reverse_proxy /notifications/hub/negotiate bitwarden:80

    # Notifications redirected to the websockets server
    reverse_proxy /notifications/hub bitwarden:3012

    # Proxy the Root directory to Rocket
    reverse_proxy bitwarden:80
}
```

