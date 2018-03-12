## frp

frp 是一个可用于内网穿透的高性能的反向代理应用，支持 tcp, udp, http, https 协议。

更加详细的配置及代码查看 [GitHub](https://github.com/fatedier/frp/blob/master/README_zh.md)

## 使用


本镜像只提供服务端，Dockerfile 文件在 frps 目录下，服务端配置在 `frps.ini` 中。

    docker-compose up

内网中客户端配置

    [common]
    server_addr = 服务端IP
    server_port = 7000
    protocol = kcp

    [ssh-client]
    type = tcp
    local_ip = 127.0.0.1
    local_port = 22
    remote_port = 6000
    use_encryption = true
    use_compression = true

客户端启动 `./frpc -c frpc.ini` 启动，这样就可以使用 `ssh user@server-ip -p 6000` 来连接在局域网中的主机。

