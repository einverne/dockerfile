## Chevereto

[Chevereto](https://chevereto.com/) 是一个强大的图片托管和分享服务，使用 Chevereto 可以快速的搭建自己的图片站点，详细内容可以参考[之前写的博客](http://einverne.github.io/post/2018/01/chevereto-self-hosted-photo-sharing.html) 。Chevereto 提供收费版本和开源版本，本镜像只提供[开源版本](https://github.com/Chevereto/Chevereto-Free)，镜像中使用 Chevereto Free 1.0.9 版本。

## 环境变量
镜像中有如下变量

- `CHEVERETO_DB_HOST` 主机hostname，默认为 `db`
- `CHEVERETO_DB_USERNAME` 用来连接数据库的用户名，默认为 `chevereto`
- `CHEVERETO_DB_PASSWORD` 用来连接数据库的密码，默认为 `chevereto`
- `CHEVERETO_DB_NAME` 数据库名，默认为 `chevereto`
- `CHEVERETO_DB_PREFIX` 表前缀（可以用来同数据库运行多个 Chevereto 实例），默认为 `chv_`

[Chevereto](https://chevereto.com/) 需要 MySQL 数据库来存储信息，可以使用 [MySQL](https://hub.docker.com/_/mysql/) 或者 [MariaDB](https://hub.docker.com/_/mariadb/) 容器。

[Chevereto](https://chevereto.com/) 有一个挂载点 `/var/www/html/images` ，用来存储用户上传的图片。可以在启动时挂载该路径，具体可参考[官网](https://docs.docker.com/storage/volumes/)。

## 使用

```
docker run -it --name chevereto -d \
    --link mysql:mysql \
    -p 80:80 \
    -v "$PWD/images":/var/www/html/images \
    -e "CHEVERETO_DB_HOST=db" \
    -e "CHEVERETO_DB_USERNAME=chevereto" \
    -e "CHEVERETO_DB_PASSWORD=chevereto" \
    -e "CHEVERETO_DB_NAME=chevereto" \
    -e "CHEVERETO_DB_PREFIX=chv_" \
    einverne/chevereto
```

推荐使用 [Docker Compose](https://yeasy.gitbooks.io/docker_practice/content/compose/) ， `docker-compose.yml` 文件在当前目录下

使用

    docker-compose up
    docker-compose up -d

本服务使用 MySQL，如果需要更换可以自行修改 yml 文件

进入容器内部

    sudo docker exec -it chevereto /bin/bash
    apt install net-tools