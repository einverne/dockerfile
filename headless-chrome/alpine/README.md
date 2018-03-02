## alpine-chrome

基于 alpine:3.7 构建

使用 alpine [源](https://pkgs.alpinelinux.org/packages?name=chrom*&branch=v3.7) 中的 chromium 61。

如果需要使用最新的 Chromium 可以将 base image 改为 `alpine:edge` 从开发版中拉取最新的 Chromium，当前最新版本为 Chromium 64 。

为什么要使用 Alpine 作为基础镜像呢？是为了减少镜像的体积，之前使用 debian 作为基础镜像，最后的 einverne/headless-chrome 有584M大小，而使用 Alpine 之后大小减小到322，近一半大小，这其中 Chrome 自身100+M的大小是无法避免的。


## build

    docker build -t "einverne/alpine-chrome" .

## run

    docker run -it --rm -p 9222:9222 einverne/alpine-chrome

镜像中包含了一系列的启动参数，可以查看[这篇文章](https://peter.sh/experiments/chromium-command-line-switches/) 来使用。

## 安全
镜像中简单地使用了 `--no-sandbox` 选项，如果需要更加安全的启动方式，一种是网上推荐的使用 `--cap-add=SYS_ADMIN` 参数，另外一种就是用 sccomp （Linux 内核提供的安全沙盒机制），具体可以参考这篇[文章](https://github.com/Zenika/alpine-chrome)。

    docker container run -it --rm --security-opt seccomp=$(pwd)/chrome.json einverne/alpine-chrome

## 遇到问题

> error: Gtk-WARNING **: cannot open display

解决办法

在 alpine 中运行 headless chrome 需要添加 `--headless` 选项。

> Failed to move to new namespace: PID namespaces supported, Network namespace supported, but failed: errno = Operation not permitted

Chrome 启动时添加 `--no-sandbox` 参数

## reference

- <https://github.com/Zenika/alpine-chrome/blob/master/Dockerfile>
- <https://github.com/westy92/headless-chrome-alpine/blob/master/Dockerfile>
- <https://github.com/Leafney/alpine-selenium-chrome/blob/master/Dockerfile>
- <https://github.com/sylvaindumont/docker-node-karma-protractor-chrome>
- <https://github.com/rastasheep/alpine-node-chromium>
