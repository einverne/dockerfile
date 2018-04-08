# nextcloud

官方其实有一个非常详细的[Repo](https://github.com/nextcloud/docker) 其中不仅包括如何制作镜像，也包括如何使用 `docker compose` 来一键启用服务。

当然因为之前使用过 [nginx-proxy](../nginx-proxy) 所以也很熟悉在 Docker 中使用 nginx 的 vhost，再搭配 lets encrypt 就可以做到一键启动服务，配置域名A记录，等待证书生成就一切OK。 然后在初始配置的时候需要注意的是其中 mysql 的地址，使用 `docker inspect nextcloud_db` 来查看本机 db 的 IP 地址，然后使用 `172.19.0.4:3306` 这样的地址填写即可。

总之使用起来比之前 snap 安装方便许多，当然备份起来也比较容易，使用 docker 的 volumn 备份即可。

