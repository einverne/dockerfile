## gogs

Gogs 是一个可以自己托管的Git服务，类似于GitHub，GitLab等等平台。他是一个[开源](https://github.com/gogits/gogs)项目，主要使用 Go 语言。

## usage

### 直接使用 gogs 镜像

具体可参考官网教程：<https://github.com/gogits/gogs/blob/master/docker/README.md>

### 使用 docker compose

    docker-compose up -d

该 compose 设置会创建两个 volume ，`gogs_app_data` 和 `gogs_db_data` 分别用来保存 gogs 应用数据和数据库数据，在备份或者迁移时使用。

在第一次访问 <http://<ip>:3000> 启动 gogs 之后，会有一个安装界面，其中需要填写 mysql 的连接信息，开始我以为映射到本地 127.0.0.1:13306 就可以了，但是一直报错

> Unable to open tcp connection with host ‘xxx:13306’: dial tcp xxx:13306: getsockopt: no route to host

其实这里需要使用 `gogsdb` 的网关地址

    sudo docker inspect gogsdb

在输出结果中找 `"Gateway": "172.19.0.1"` 字段

然后验证 

    mysql -h ip -P 13306 -ugogs -p
    # 输入密码 gogs

如果验证成功那么在安装 gogs 时填写该地址就可以。

## reference

- <https://github.com/gogits/gogs/tree/master/docker>
