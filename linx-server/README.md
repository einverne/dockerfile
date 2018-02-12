## linx-server
`linx-server` 是一个使用 Go 写的文件，代码，媒体共享网站，能够快速一键上传并分享文件。

他的项目地址: <https://github.com/andreimarcu/linx-server>

## 使用
build 镜像

    docker build -t linx-server .

然后需要创建两个文件夹用来保存上传的文件，比如 `/media/meta` 和 `/media/files` ，运行

    docker run -p 8080:8080 -d -v /media/meta:/data/meta -v /media/files:/data/files linx-server


