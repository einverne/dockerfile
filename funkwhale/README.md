# funkwhale

- Install docker
- Create funkwhale user
- Create .env file
- Create docker-compose.yml file
- Start Funkwhale service

create the user and the directory:

	sudo useradd -r -s /usr/bin/nologin -m -d /srv/funkwhale -U -G docker funkwhale
	cd /srv/funkwhale

Log in as the newly created user:

	sudo -u funkwhale -H bash

create `.env`:

```
touch .env
chmod 600 .env  # reduce permissions on the .env file since it contains sensitive data
cat > .env << EOF
# Replace 'your.funkwhale.example' with your actual domain
FUNKWHALE_HOSTNAME=your.funkwhale.example
# Protocol may also be: http
FUNKWHALE_PROTOCOL=https
# This limits the upload size
NGINX_MAX_BODY_SIZE=100M
# Bind to localhost
FUNKWHALE_API_IP=127.0.0.1
# Container port you want to expose on the host
FUNKWHALE_API_PORT=5000
# Generate and store a secure secret key for your instance
DJANGO_SECRET_KEY=$(openssl rand -hex 45)
# Remove this if you expose the container directly on ports 80/443
NESTED_PROXY=1

YOUR_DOMAIN=your.funkwhale.example
# email to generate Let's Encrypt SSL
YOUR_EMAIL=your@example.com
PATH_TO_MUSIC=/path/to/music/folder
EOF
```

then:

	docker-compose up -d

create admin user:

	docker exec -it funkwhale manage createsuperuser

## reference

- <https://docs.funkwhale.audio/installation/docker.html>
