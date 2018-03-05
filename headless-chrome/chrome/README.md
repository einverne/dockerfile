## headless chrome
Headless浏览器是一种很好的工具，用于自动化测试和不需要可视化用户界面的服务器。例如，你想在一个网页上运行一些测试，从网页创建一个PDF，或者只是检查浏览器怎样递交URL。

## 使用

    docker pull einverne/headless-chrome
    docker run -it --rm -p 9222:9222 einverne/headless-chrome

相关文章:

- Google : <https://developers.google.com/web/updates/2017/04/headless-chrome>
- Dockerfile文件：<https://github.com/ebidel/lighthouse-ci/blob/master/builder/Dockerfile>

更多关于如何编程操控 Headless Chrome 的内容可以看看这 repo <https://github.com/ChromeDevTools/awesome-chrome-devtools>

[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) 是一个开源的网页自动化测试工具。他提供了比如浏览网页，用户输入，执行JS等等功能。ChromeDriver 在 Chromium 上实现了 [WebDriver wire protocol](https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol)  ，可以作为单独的服务。最新的版本可以在 [这里](https://sites.google.com/a/chromium.org/chromedriver/downloads) 查看。ChromeDriver 是网站测试框架 Selenium Chrome 基础部分，通过 HTTP 通信实现。

Selenium 通过 protocol 和远程 chromedriver 通信，Selenium 实际上是对 Wire protocol 协议的封装，同时提供外部 WebDriver 上层调用类库，


## 遇到的问题

在运行 docker 中运行 Chrome 时遇到

> Failed to move to new namespace: PID namespaces supported, Network namespace supported, but failed: errno = Operation not permitted

在 Dockerfile 中启动 Chrome 时添加参数: `--no-sandbox` 


Dockerfile 文件参考：

- <fate0/headless-chrome>
- <alpeware/chrome-headless-trunk>
- <ebidel/lighthouse-ci>
- <https://github.com/yukinying/chrome-headless-browser-docker>
- <https://github.com/jessfraz/dockerfiles>

