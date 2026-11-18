# Semaphore UI

[Semaphore UI](https://github.com/semaphoreui/semaphore) 是 Ansible、Terraform/OpenTofu、Bash、PowerShell 的自托管 Web 面板，提供任务模板、定时任务、Key Store、执行历史和 API。这里用 SQLite 单容器部署。

当前部署：v2.20.24，跑在 ser8ubuntu2404，端口 3010（宿主机 3000 已被 vertex 占用）。

## 部署

```bash
cp .env.example .env
# 生成 Key Store 加密密钥，写入 SEMAPHORE_ACCESS_KEY_ENCRYPTION
head -c32 /dev/urandom | base64
# 改掉 SEMAPHORE_ADMIN_PASSWORD
mkdir -p config data tmp   # 容器以 uid 1001 运行，目录要同 UID 所有
docker compose up -d
```

访问 `http://<服务器 IP>:3010`，用 `.env` 里的管理员账号登录。管理员只在首次启动时创建，之后改密码请在界面里改。

## 注意

- Semaphore 存着所有机器的 SSH 私钥，只在局域网 / Tailscale 内访问，不要直接暴露公网
- `SEMAPHORE_ACCESS_KEY_ENCRYPTION` 丢失后 Key Store 里的凭据全部无法解密，和数据库一起备份
- playbook 需要额外 Python 包时，把 `requirements.txt` 放到 `config/requirements.txt`，容器启动时会自动 pip install（需要能访问 PyPI）
- 容器里 `known_hosts` 为空，首次连接新主机会因 host key 校验失败，可以在 inventory 或 `ansible.cfg` 里处理

## 备份

整个状态是 `data/database.sqlite`、`config/config.json`（cookie 密钥）和 `.env` 里的 Key Store 加密密钥。注意 v2.20.24 下 `SEMAPHORE_DB` 环境变量对 SQLite 不生效，数据库固定在容器内 `/var/lib/semaphore/database.sqlite`：

```bash
docker compose stop && tar czf semaphore-$(date +%F).tgz config data .env && docker compose start
```

## 升级

改 `.env` 里的 `SEMAPHORE_VERSION`，然后 `docker compose pull && docker compose up -d`。
