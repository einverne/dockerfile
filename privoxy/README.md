## privoxy

Privoxy 是一款不进行网页缓存且自带过滤功能的代理服务器[^1]。

镜像提供一个在 Alpine Linux 上运行的 Privoxy 服务，config 配置中将本地 1080 端口 socks 流量转发到 8118 端口 HTTP 。

## 本地编译运行

    sudo docker build -t "privoxy" .
    sudo docker run --name=privoxy -p 8118:8118 privoxy:latest

## 使用docker hub
    
    sudo docker run --name=privoxy -p 8118:8118 einverne/privoxy:latest

[^1]: 详情可以参考之前的[博客](http://einverne.github.io/post/2018/03/privoxy-forward-socks-to-http.html)
