# PowerContext Server

[PowerContext](https://github.com/oceanbase/powercontext) 是 OceanBase 开源的 AI 记忆与上下文运行时，这里用 Docker 自托管。

当前状态：v1.4.1，Basic 模式（未配置 Generation / Embedding 模型），只做显式保存和全文检索召回。

## 架构

```
Claude Code / CLI ──HTTPS──> Cloudflare ──> cloudflared (Tunnel)
                                              │
                                              └─> 127.0.0.1:18000 ──> 容器 :8000 ──> /data (SQLite)
```

- 容器只绑定宿主机 loopback，外部访问都走 Tunnel
- 鉴权：`POWERCONTEXT_SERVER_ACCESS_MODE=enforced`，静态 Bearer token，所有持有者共享一个管理员身份
- `/health/live` 和 `/health/ready` 无需鉴权，其余 API、MCP、Dashboard 都需要 token

## 目录结构

| 路径 | 说明 |
|---|---|
| `docker-compose.yml` | 从 `src/` 构建镜像并运行 |
| `src/` | git submodule，指向 `oceanbase/powercontext`，固定在发布 tag 的 commit |
| `.env` | Server 配置，含 token，已被 `.gitignore` 忽略，权限 600 |
| `~/powercontext-data` | 数据目录（SQLite 和调度状态），需由 UID 10001 所有 |

## 首次部署

```bash
cd ~/dockerfile
git submodule update --init --depth 1 powercontext/src

cd powercontext
sudo mkdir -p ~/powercontext-data
sudo chown 10001:10001 ~/powercontext-data
```

创建 `.env`（`umask 077` 后再写，避免 token 被其他用户读取）：

```bash
# compose 变量，用 PC_ 前缀避免被当成 Server 配置
PC_VERSION=1.4.1
PC_PORT=18000
PC_DATA_PATH=~/powercontext-data

POWERCONTEXT_SERVER_ACCESS_MODE=enforced
POWERCONTEXT_SERVER_AUTH_TOKEN=<openssl rand -hex 32 生成>
POWERCONTEXT_SERVER_PUBLIC_URL=https://context.example.com
POWERCONTEXT_SERVER_DASHBOARD_ENABLED=true
POWERCONTEXT_SERVER_MCP_ENABLED=true

# 信任 Docker 网关传来的 X-Forwarded-Proto，见下文「Dashboard 登录 403」
FORWARDED_ALLOW_IPS=172.31.0.1
```

启动并检查：

```bash
docker compose up -d --build
curl -s http://127.0.0.1:18000/health/ready
```

`status` 为 `ready` 即正常。Basic 模式下日志里的 `Inference capability notice` 是预期内的提示。

Cloudflare 侧需要两处配置：

- `/etc/cloudflared/config.yml`（`~/.cloudflared/config.yml` 是它的软链接）在 404 兜底规则之前加入 `context.example.com -> http://localhost:18000`，然后 `sudo systemctl restart cloudflared`
- DNS 为该子域名添加 CNAME，指向 tunnel 的 `<tunnel-id>.cfargotunnel.com`，开启代理

## 升级

```bash
cd ~/dockerfile/powercontext
git -C src fetch --depth 1 origin tag powercontext-vX.Y.Z
git -C src checkout powercontext-vX.Y.Z
# 修改 .env 的 PC_VERSION=X.Y.Z
docker compose up -d --build
cd .. && git add powercontext/src && git commit -m "feat(powercontext): upgrade to X.Y.Z"
```

升级 Server 后，客户端的 CLI 和 Claude Code 插件也要升到同一版本，否则召回会静默失效（见下文）。

## 备份

数据都在 `~/powercontext-data`。SQLite 做文件级备份时需要先停写：

```bash
docker compose stop
sudo tar czf powercontext-data-$(date +%F).tar.gz -C ~ powercontext-data
docker compose start
```

也可以用 `powercontext archive` 导出可移植的逻辑备份。

## 接入 Claude Code

插件由 Claude Code 的 `SessionStart` 和 `UserPromptSubmit` 两个 hook 加一个 HTTP MCP server 组成：

- `SessionStart`：会话开始时加载 Scope 的上下文
- `UserPromptSubmit`：每条 prompt 前调用 `/v1/context/prepare` 注入相关记忆，并把 prompt 存为 Source（可关闭）
- MCP：提供 `remember_memory`、`search_memory`、`handoff_current_work`、`continue_handoff` 等工具，供 Claude 主动保存和读取

召回和捕获都是 fail-open 的，Server 不可用时不会阻塞 prompt。

### 前提

在运行 Claude Code 的机器上：

```bash
uv tool install --force "powercontext[cli,server]==1.4.1"   # 版本与 Server 一致
powercontext --version
claude --version
python3 --version    # hook 用 PATH 上的 python3，需 3.9+
```

### 准备客户端凭据

插件从环境变量读取 Server 地址和 token，token 不能写进插件配置、`.mcp.json` 或 URL。建一个只有自己可读的文件：

```bash
mkdir -p ~/.config/powercontext && chmod 700 ~/.config/powercontext
umask 077
cat > ~/.config/powercontext/client.env <<'EOF'
POWERCONTEXT_CLIENT_SERVER_URL=https://context.example.com
POWERCONTEXT_CLIENT_API_TOKEN=<token>
POWERCONTEXT_CLAUDE_SERVER_URL=https://context.example.com
POWERCONTEXT_CLAUDE_AUTHORIZATION="Bearer <token>"
EOF
```

`<token>` 就是 Server `.env` 里的 `POWERCONTEXT_SERVER_AUTH_TOKEN`。

Claude Code 必须在加载了这些变量的 shell 里启动，MCP 的 `Authorization` 头和 hook 都依赖它。在 `~/.zshrc` 加入：

```bash
[ -f ~/.config/powercontext/client.env ] && { set -a; . ~/.config/powercontext/client.env; set +a; }
```

确认连通：

```bash
powercontext ready          # Status: ready
powercontext capabilities
```

### 安装插件

```bash
powercontext setup claude-code \
  --ref powercontext-v1.4.1 \
  --server-url https://context.example.com \
  --no-capture-prompts
powercontext doctor claude-code
```

- `--ref` 一定要写成与 Server 相同的 tag。默认值是 `master`，会装上比 Server 新的插件，可能出现 `version_mismatch`
- `--no-capture-prompts` 表示不把每条 prompt 存为 Source。Basic 模式没有自动提取，捕获下来的 prompt 只是原始记录；需要时可以去掉这个参数重新运行
- setup 会注册 marketplace，并在用户级安装插件，`server_url` 和 `capture_prompts` 写入用户级 `pluginConfigs`；重复运行是安全的

### 只在指定项目启用（可选）

插件装在用户级，默认对所有项目生效。没有绑定 Scope 的项目会落到 Server 的默认 Scope，仍然会召回和注入。如果只想在个别项目里使用：

```bash
claude plugin disable powercontext@powercontext --scope user

cd ~/personal/<project>
claude plugin enable powercontext@powercontext --scope local
```

这个做法没有实测过。启用后在新会话里用 `/plugin` 和 `/mcp` 确认插件只在该项目里出现。

### 为项目绑定 Scope

Scope 是记忆的隔离边界，建议一个项目一个。解析顺序：

1. 环境变量 `POWERCONTEXT_CLAUDE_SCOPE_ID`
2. 会话绑定
3. workspace 绑定，标识是 git 根目录绝对路径的 sha256
4. Server 默认 Scope

创建 Scope，记下输出的 `scp_...` ID：

```bash
powercontext scope create --title "<project>" --summary "<一句话说明>"
```

在项目目录里绑定 workspace：

```bash
cd ~/personal/<project>
SCOPE_ID=scp_xxx
WS=$(python3 -c 'import hashlib,os,pathlib,subprocess
r=subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip() or os.getcwd()
print(hashlib.sha256(os.fsencode(pathlib.Path(r).resolve())).hexdigest())')
powercontext scope binding set "$SCOPE_ID" --integration claude-code --kind workspace --external-id "$WS"
```

这里的计算方式和插件 `scripts/workspace_scope.py` 中的 `workspace_binding_key` 一致。注意 ID 必须是 create 返回的 `scp_...`，不是标题。

也可以在 Claude Code 会话里让 Claude 调用 MCP 工具 `set_scope_binding` 完成绑定。

### 验证

新开一个 `claude` 会话：

1. `/hooks`：能看到 `SessionStart` 和 `UserPromptSubmit`
2. `/mcp`：`powercontext` 显示为 connected
3. 让 Claude 记一条决定，比如「记住：这个项目的部署用 Cloudflare Workers Builds」，它会调用 `remember_memory`
4. 再开一个新会话问「这个项目怎么部署的？」，看能否召回
5. 在 Dashboard（`https://context.example.com/dashboard/home`）里确认记录出现在对应 Scope 下

`powercontext doctor claude-code` 只检查安装状态，不访问 Server，记忆是否生效要按上面的步骤确认。

### 日常用法

Basic 模式下记忆不会自动提炼，靠显式操作：

| 场景 | 做法 |
|---|---|
| 记住一个决定或事实 | 让 Claude「记住 ...」，对应 `remember_memory` |
| 查之前的记忆 | 让 Claude 搜索，对应 `search_memory` |
| 结束一段工作，留交接 | 让 Claude 做 handoff，对应 `handoff_current_work` |
| 新会话接着干 | 让 Claude 读取上次的 handoff，对应 `continue_handoff` |

可选环境变量：

- `POWERCONTEXT_CLAUDE_BOOTSTRAP_CONTEXT=true`：会话开始时注入 Scope 的引导上下文，`POWERCONTEXT_CLAUDE_BOOTSTRAP_MAX_BYTES` 控制大小（512 到 8192，默认 4096）
- `POWERCONTEXT_CLAUDE_CAPTURE_PROMPTS=false`：临时关闭 prompt 捕获
- `POWERCONTEXT_CLAUDE_SCOPE_ID=scp_xxx`：临时指定 Scope，优先级最高

### 排错

| 现象 | 原因 |
|---|---|
| HTTP 401 `authentication_failed` | 启动 Claude Code 的 shell 没加载 `client.env`，或 token 与 Server 不一致 |
| HTTP 404 `version_mismatch` | 插件与 Server 版本不一致，用 `--ref powercontext-vX.Y.Z` 重装 |
| HTTP 503 或无响应 `server_unavailable` | 容器或 cloudflared 没在运行 |
| `/mcp` 里 powercontext 连接失败 | 同上，另外确认 `POWERCONTEXT_CLAUDE_AUTHORIZATION` 带有 `Bearer ` 前缀 |
| 没有召回 | 检查 Scope 绑定是否正确、`/hooks` 是否有两个 hook、版本是否一致 |

### 卸载

```bash
claude plugin uninstall powercontext@powercontext --scope user
claude plugin marketplace remove powercontext
```

从最后一个 scope 卸载时会删除插件数据目录，需要保留就加 `--keep-data`。

## 已知问题

### Dashboard 登录 403

Dashboard 登录会比较浏览器 `Origin` 的 scheme 和 Server 看到的请求 scheme。cloudflared 连接的是宿主机端口，容器看到的来源是 Docker 网关，而 uvicorn 默认只信任 `127.0.0.1` 发来的 `X-Forwarded-Proto`，于是把 scheme 当成 `http`，登录直接返回 403，根本走不到 token 校验。

解决办法：在 `.env` 设置 `FORWARDED_ALLOW_IPS=172.31.0.1`，同时在 `docker-compose.yml` 中固定 default 网络的子网，让网关 IP 不会变化。

### MCP 路径重定向

`/mcp` 会 307 重定向到 `/mcp/`，插件生成的地址是不带斜杠的 `${server_url}/mcp`。手动配置 MCP 客户端时直接写 `https://context.example.com/mcp/`。
