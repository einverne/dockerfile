# Beszel

[Beszel](https://github.com/henrygd/beszel) 是一个轻量的服务器监控工具，可以看 CPU、内存、磁盘、网络、温度和 Docker 容器的资源占用，支持告警。比 Prometheus + Grafana 省资源得多。

当前部署：v0.21.1，跑在 ser8ubuntu2404，公网地址 https://beszel.einverne.info

## 架构

```
VPS beszel-agent ──WebSocket(HTTPS)──> Cloudflare ──> cloudflared (Tunnel)
                                                         │
ser8ubuntu2404 beszel-agent (容器, host 网络) ──> 127.0.0.1:8090 ──> beszel 容器 ──> /beszel_data
```

- 所有 Agent 都用 WebSocket 主动连 Hub，靠 `HUB_URL` + 通用 token 自动注册，不用在面板里一台台点 Add System
- Hub 和 Agent 都设了 `DISABLE_SSH=true`：Hub 不会去 SSH 连 Agent，Agent 也不监听 45876，VPS 不需要开放任何入站端口
- Hub 只绑定宿主机 loopback，外部访问都走 Tunnel（`/etc/cloudflared/config.yml` 里的 `beszel.einverne.info` 规则）
- 本机的 Agent 也在这个 compose 里，用 host 网络直接连 `127.0.0.1:8090`

## 目录结构

| 路径 | 说明 |
|---|---|
| `docker-compose.yml` | Hub + 本机 Agent |
| `.env` | 版本、数据目录、Agent 的 KEY/TOKEN，已被 `.gitignore` 忽略，权限 600 |
| `~/beszel-data` | Hub 数据（PocketBase SQLite、Hub 的 SSH 密钥），整个备份它就行 |
| `~/beszel-agent-data` | 本机 Agent 的 fingerprint |

## 首次部署

```bash
cd ~/dockerfile/beszel
mkdir -p ~/beszel-data ~/beszel-agent-data
umask 077 && cat > .env <<'EOF'
BESZEL_VERSION=0.21.1
BESZEL_PORT=8090
BESZEL_DATA_PATH=/home/einverne/beszel-data
BESZEL_AGENT_DATA_PATH=/home/einverne/beszel-agent-data
APP_URL=https://beszel.example.com
# 仅全新安装时用来创建首个管理员，创建后删掉这两行
USER_EMAIL=you@example.com
USER_PASSWORD=<openssl rand -base64 18>
# 下面两项在 Hub 起来之后再填
AGENT_KEY=
AGENT_TOKEN=
AGENT_SYSTEM_NAME=ser8ubuntu2404
EOF
docker compose up -d beszel
```

然后拿 Hub 公钥和通用 token：

- 网页：`/settings/tokens` 里打开 Universal token，并勾选永久（不勾的话 1 小时后失效）；公钥在 Add System 弹窗里
- 或者 API：用 `users` 集合登录拿 JWT，`GET /api/beszel/info` 返回 `key`，`POST /api/beszel/universal-token` 带 `{"enable":1,"permanent":1}` 返回 `token`

把它们填进 `.env` 的 `AGENT_KEY`（加引号）和 `AGENT_TOKEN`，再 `docker compose up -d beszel-agent`。

最后在 `/etc/cloudflared/config.yml` 的 404 兜底规则前面加上：

```yaml
  - hostname: beszel.example.com
    service: http://localhost:8090
```

```bash
sudo cloudflared --config /etc/cloudflared/config.yml tunnel ingress validate
cloudflared tunnel route dns einverne-tunnel beszel.example.com
sudo systemctl restart cloudflared
```

## 其他机器装 Agent

用 Ansible 仓库里的 playbook 批量装（二进制 + systemd），KEY、TOKEN、版本都在那边配置：

```bash
cd ~/Sync/ansible
ansible-playbook playbook/beszel-agent.yml --limit gc4 --check --diff
ansible-playbook playbook/beszel-agent.yml
```

详见 `playbook/beszel-agent.yml` 开头的注释。

## 升级

1. 改 `.env` 的 `BESZEL_VERSION`，`docker compose pull && docker compose up -d`
2. 改 Ansible 仓库 `playbook/vars/beszel.yml` 的 `beszel_version`，重跑 playbook

Hub 和 Agent 的版本尽量保持一致。

## 踩过的坑

- 同一个镜像装出来的 VPS，`/etc/machine-id`（和 DMI product_uuid）是一样的。Agent 默认用它们算 fingerprint，Hub 就会把几台机器当成同一个系统，它们连上之后会互相踢下线（日志里反复出现 `Connection closed code=1000`）。gc1-4、rn1-3、rn5 共用一个，gc5-9 共用另一个。Agent 会优先读 `/var/lib/beszel-agent/fingerprint`，所以 playbook 给每台机器写入固定的 `sha256(machine-id:主机名)`
- `SYSTEM_NAME` 只在第一次注册时生效，之后改名要在面板里改
- 通用 token 默认只有 1 小时有效，要在面板里勾选永久
