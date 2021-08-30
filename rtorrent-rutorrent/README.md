## rtorrent and rutorrent

```
mkdir data downloads passwd
chown ${PUID}:${PGID} data downloads passwd
```
add password:

```
docker run --rm -it httpd:2.4-alpine htpasswd -Bbn <username> <password> >> $(pwd)/passwd/webdav.htpasswd
```

- rpc.htpasswd: XMLRPC through nginx
- rutorrent.htpasswd: ruTorrent basic auth
- webdav.htpasswd: WebDAV on completed downloads

```
docker-compose up -d
docker-compose logs -f
```


- <https://github.com/crazy-max/docker-rtorrent-rutorrent>
