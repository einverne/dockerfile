## v2ray 版本

可查看 Dockerfile 文件中 v2ray 版本

## build image

本地编译可使用

    cd v2ray
    docker build -t "v2ray" .

## 默认配置

**镜像使用官方的样例配置，来源于官方发布包，可执行以下命令获取样例配置**
**具体修改设置可参考 [官方文档配置部分](https://www.v2ray.com/chapter_02/)**


``` sh
docker run -dt --name v2ray -p 10800:10800 v2ray
```

**Container 默认监听 10800 端口**

## v2ray 官方

官方的repo : <https://github.com/v2ray/install>
