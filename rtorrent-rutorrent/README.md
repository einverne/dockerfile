## rtorrent and rutorrent

copy the env to `.env`:

	cp env .env

edit `.env`:

```
RT_DHT_PORT=6881
XMLRPC_PORT=8000
RUTORRENT_PORT=8080
WEBDAV_PORT=9000
RT_INC_PORT=50000
RT_BASE_PATH=/path/to/rtorrent/
```

create folders under `$RT_BASE_PATH`:

```
cd $RT_BASE_PATH
mkdir data downloads passwd
chown ${PUID}:${PGID} data downloads passwd
```

add password:

```
docker run --rm -it httpd:2.4-alpine htpasswd -Bbn <username> <password> >> $(pwd)/passwd/rpc.htpasswd
docker run --rm -it httpd:2.4-alpine htpasswd -Bbn <username> <password> >> $(pwd)/passwd/rutorrent.htpasswd
docker run --rm -it httpd:2.4-alpine htpasswd -Bbn <username> <password> >> $(pwd)/passwd/webdav.htpasswd
```

- rpc.htpasswd: XMLRPC through nginx
- rutorrent.htpasswd: ruTorrent basic auth
- webdav.htpasswd: WebDAV on completed downloads

Finally:

```
docker-compose up -d
docker-compose logs -f
```

## reference

- <https://github.com/crazy-max/docker-rtorrent-rutorrent>
