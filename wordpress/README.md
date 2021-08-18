## wordpress

确保本地已经安装最新版本 Docker 和 Docker Compose，可参考[博客](http://einverne.github.io/post/2017/07/docker-introduction.html)

这个 docker-compose 配置使用 nginx-proxy 会自动配置 Nginx 反向代理，并自动使用 Let's Encrypt SSL 证书。

所以需要在配置 `.env` 中替换自己的配置。

正常情况下在该目录下运行 `docker-compose up` 即可启动

- MySQL 文件在 volumn 中
- wordpress 默认端口在 80
- wordpress 的 `wp-content` 文件在宿主机 `/var/www/html/wp-content` 目录，可以通过 `.env` 配置

将 `wp-content` 文件夹映射到宿主机：`/var/www/html/wp-content/`

    volumes:
      - /var/www/html/wp-content:/var/www/html/wp-content

## 运行无数据库版本

当使用一台其他的服务器作为 MySQL 数据库时，可以使用 `docker-compose-without-db.yml` 来使用，在配置中修改 db_host 的地址，一般为 IP，然后修改数据库名，数据库用户名和密码。

需要注意的是，这个配置中 WordPress 映射到本地 `/var/www/html/wordpress` 目录。

## 导出数据库
使用 `export.sh` 脚本导出当前的数据库，默认只备份 wordpress 数据库，如需备份完整数据库，自行修改

参考：

- <https://cntnr.io/setting-up-wordpress-with-docker-262571249d50>
- <https://github.com/nezhar/wordpress-docker-compose>
