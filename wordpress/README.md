## wordpress
确保本地已经安装最新版本 Docker 和 Docker Compose，可参考[博客](http://einverne.github.io/post/2017/07/docker-introduction.html)

正常情况下在该目录下运行 `docker-compose up` 即可启动

- mysql 文件存放在宿主机 `/var/lib/mysql` 下
- wordpress 默认端口在 8000
- wordpress 的 `wp-content` 文件在宿主机 `/var/www/html/wp-content` 目录

将 `wp-content` 文件夹映射到宿主机: `/var/www/html/wp-content/`

    volumes:
      - /var/www/html/wp-content:/var/www/html/wp-content 

## 导出数据库
使用 `export.sh` 脚本导出当前的数据库，默认只备份 wordpress 数据库，如需备份完整数据库，自行修改

参考:

- <https://cntnr.io/setting-up-wordpress-with-docker-262571249d50>
- <https://github.com/nezhar/wordpress-docker-compose>
