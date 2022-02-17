# netmaker

Netmaker is a tool for creating and managing virtual networks, Netmaker makes networks with WireGuard. Netmaker automates fast, secure, and distributed virtual networks.

Netmaker 是一个 WireGuard 组网的管理工具，可以非常轻松地创建和管理虚拟网络。Netmaker 可以在不同的数据中心，不同的机房快速组建一个基于 WireGuard 的虚拟网络。



Netmaker docker-compose 启动后会暴露 3 个端口。包括后台 Dashboard 默认为 8082，后台访问 API 端口 8081，以及 gRPC 端口 50051。

使用 Caddyfile 反向代理，可以根据自己的需要进行修改。


Caddyfile:

```
{
    # LetsEncrypt account
    email fake@email.com
}

# Dashboard
https://dashboard.nm.10-10-10-10.nip.io {
    reverse_proxy http://127.0.0.1:8082
}

# API
https://api.nm.10-10-10-10.nip.io {
    reverse_proxy http://127.0.0.1:8081
}

# gRPC
https://grpc.nm.10-10-10-10.nip.io {
    reverse_proxy h2c://127.0.0.1:50051
}
```
