# dockerfile
一些平常用到的 dockerfile

## docker-h5ai
使用 docker 显示文件列表

## docker-nginx-google
使用 docker 一键反向代理 Google

## netdata
netdata 监控 VPS

    cd netdata
    docker build -t "netdata" .

netdata 默认的端口在 19999

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

### rrshare

这个人人影视的镜像跑起来后对 CPU 的占用异常，个人已经弃用。

- <https://hub.docker.com/r/oldiy/rrshare64>

### calibre-web

linuxserver 的 image 有些简陋，所以换用这个

- <https://hub.docker.com/r/technosoft2000/calibre-web>

### bookstack

- <https://hub.docker.com/r/linuxserver/bookstack>
