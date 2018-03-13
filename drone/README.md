## drone

drone 是Go语言实现的持续集成CI软件，比 Jenkins 轻量，他允许使用类似 docker-compose 的语法来定义自动化过程。

在启动 `sudo docker-compose up` 之前，新建 `.env` 文件，填入以下内容

    ONE_SECRET=drone
    DRONE_HOST=http://localhost:4000
    DRONE_ADMIN=<your github name>
    DRONE_GITHUB_CLIENT=<github client id>
    DRONE_GITHUB_SECRET=<github client secret>

在 GitHub [Developer settings](https://github.com/settings/developers) 下申请 OAuth Apps，得到 Client ID 和 Client Secret。

## reference

- 源代码 <https://github.com/drone/drone>
- 官方文档 <http://docs.drone.io/installation/>
