# yourls

create `.env` file and fill it with config:

```
YOURLS_DB_HOST=
YOURLS_DB_USER=
YOURLS_DB_PASS=
YOURLS_DB_PREFIX=yourls_
YOURLS_SITE=https://yourdomain.com
YOURLS_HOURS_OFFSET=+8
YOURLS_URL_CONVERT=62
YOURLS_USER=
YOURLS_PASS=
YOUR_DOMAIN=www.example.com
YOUR_EMAIL=admin@example.com
```

then:

	docker-compose up -d
