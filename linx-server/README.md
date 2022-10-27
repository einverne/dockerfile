## linx-server
`linx-server` 是一个使用 Go 写的文件，代码，媒体共享网站，能够快速一键上传并分享文件。

他的项目地址: <https://github.com/andreimarcu/linx-server>

## 使用

### 自己编译
build 镜像

    docker build -t linx-server .

然后需要创建两个文件夹用来保存上传的文件，比如 `/media/meta` 和 `/media/files` ，运行

    docker run -p 8080:8080 -d -v /media/meta:/data/meta -v /media/files:/data/files linx-server

### 使用镜像

    docker pull einverne/linx-server

## 选项
如果想要修改 linx 的配置，当前目录下有 `config.ini` 文件，文件中可以指定网站的title，还有支持的最大文件大小，其他的配置可参考原项目地址

如果遇到 permission denied 的问题，可以将文件夹权限设置：

```
sudo chown -R 65534:65534 ~/linx
```
