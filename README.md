# dockerfile
dockerfile collection

install docker-compose

    bash install_docker_compose.sh

## Basic tools

### docker-h5ai
h5ai is a modern HTTP web server index, require HTTP server and PHP

## docker-nginx-google
使用 docker 一键反向代理 Google

## netdata
netdata now has the official docker support. Recommend using the official image:

```bash
docker run -d --name=netdata \
  -p 19999:19999 \
  -v netdataconfig:/etc/netdata \
  -v netdatalib:/var/lib/netdata \
  -v netdatacache:/var/cache/netdata \
  -v /etc/passwd:/host/etc/passwd:ro \
  -v /etc/group:/host/etc/group:ro \
  -v /proc:/host/proc:ro \
  -v /sys:/host/sys:ro \
  -v /etc/os-release:/host/etc/os-release:ro \
  --restart unless-stopped \
  --cap-add SYS_PTRACE \
  --security-opt apparmor=unconfined \
  netdata/netdata
```

## weibo-rss

将微博内容输出到 RSS

## headless-chrome

顾名思义



## 一些常用镜像

### Transmission

- <https://hub.docker.com/r/linuxserver/transmission>

### ruTorrent
rTorrent 和 ruTorrent 这是个人用过的感觉非常不错的 BitTorrent 客户端。用的也是 LinuxServer 的镜像，不过我自己再上面加了一些扩展，比如主题和插件。

- <https://github.com/einverne/docker-rutorrent>

### Aria2-with-webui

- <https://hub.docker.com/r/xujinkai/aria2-with-webui> 已停止更新
- <https://hub.docker.com/r/fanningert/aria2-with-webui>

### Jellyfin

- <https://hub.docker.com/r/linuxserver/jellyfin>
- <https://hub.docker.com/r/jellyfin/jellyfin>

### Plex

- <https://hub.docker.com/r/linuxserver/plex>

### NextCloud

- <https://hub.docker.com/_/nextcloud>

### krusader

- <https://hub.docker.com/r/djaydev/krusader>

### calibre-web

linuxserver 的 image 有些简陋，所以换用这个

- <https://hub.docker.com/r/technosoft2000/calibre-web>

### bookstack

- <https://hub.docker.com/r/linuxserver/bookstack>
