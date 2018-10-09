## headless-chrome

目录下包含镜像

- chrome 目录下基于 Debian 的 headless-chrome
- chromedriver 下在 chrome 的基础上增加了 chromedriver, chromedriver 位于 /usr/local/bin/ 目录下
- alpine 目录下为基于 Alpine:3.7 镜像的 headless Chromium
- alpine-unstable 是基于 alpine:edge 的 headless Chromium

使用 Docker 跑 Headless Chrome 的一大重要内容就是将 Chrome 作为 server 来跑爬虫，或者进行网页自动化过程。结合 Chrome 官方推出的 [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) 协议，或者使用 chromedriver + [SeleniumHQ](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)。可以实现很多有意思的自动化过程。

## Chrome DevTools Protocol
只要实现该协议就能够编程操作，调试，审查 Chromium，Chrome 或者其他基于 Blink 内核的浏览器。GitHub 上现在有很多基于该协议的[项目](https://developer.chrome.com/devtools/docs/debugging-clients)，设置 Chrome 自己的 [DevTools](https://developers.google.com/web/tools/chrome-devtools/) 也是使用该协议的。

官方有两篇教程

- Getting Started with Headless Chrome <https://developers.google.com/web/updates/2017/04/headless-chrome>
- Headless Chromium readme <https://chromium.googlesource.com/chromium/src/+/lkgr/headless/README.md>

通过这两篇教程能对 Headless Chrome 有一个基本的了解。官方推荐的是基于 nodejs 的这个 [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface/) 库，还有封装更加紧密的 [Puppeteer](https://github.com/GoogleChrome/puppeteer)，如果使用其他语言，比如 Python，可以在 [awesome-chrome-devtools](https://github.com/ChromeDevTools/awesome-chrome-devtools#chrome-devtools-protocol) 这个项目中找到。

启动容器

    docker run -it --rm --name alpine-chrome -p 9222:9222 einverne/alpine-chrome
    docker run -d --name=headless-chrome -p 9222:9222 --restart=always einverne/headless-chrome:latest

容器会监听 9222 端口，访问 <http://localhost:9222> ，会看到 Developer Tools interface 开启了一个内嵌的调试，一旦打开 Developer Tools 自动建立了 Web Socket 连接，并开始交换 JSON 数据。

应用程序可以通过 <http://localhost:9222/json> 链接找到打开的页面，通过 JSON 数据来获知页面内容。

这里使用 [pychrome](https://github.com/fate0/pychrome) 作为例子，具体的代码可以参考 example 目录下[例子](example)。

更多的内容可以参考我的[博客](https://einverne.github.io/post/2018/03/chrome-devtools-protocal-using-python.html)

