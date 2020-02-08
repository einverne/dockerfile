### 项目介绍

项目 Fork 自 WebStack-Laravel 的 [dockerfile](https://github.com/Gourds/WebStackLaravel).

该镜像是 [WebStackLaravel](https://github.com/hui-ho/WebStack-Laravel) 项目的 Docker 部署版本。

### 使用说明

包含直接执行`docker run`的方式

镜像支持的参数：

|参数|说明|
|---|---|
|INSTALL_DIR|容器内的部署家目录|
|DB_HOST|数据库地址，默认`127.0.0.1`|
|DB_PORT|数据库端口，默认`3306`|
|DB_DATABASE|数据库名称，默认`webstack`|
|DB_USERNAME|数据库用户名，默认`webstack`|
|DB_PASSWORD|数据库密码，默认`password`|
|LOGIN_COPTCHA|是否启动控制台验证码，默认 true|


使用`docker run`方式

**注意**由于 webstacklaravel 需要 mysql 支持，所以直接使用`docker run`需要手动指定 Mysql 的地址信息
目前支持的参数



### 常见问题

针对一些原项目的提问在这里做一下汇总，欢迎补充

- 改变监听地址
可以通过 Nginx Proxy 进行代理，或者添加`--host`参数
```
php artisan serve --host=0.0.0.0 --port=8000
```


