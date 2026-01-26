# Dufs - Docker File Server Usage Guide

A lightweight file server for serving files over HTTP with authentication support, powered by Docker.

## Overview

[Dufs](https://github.com/sigoden/dufs) is a simple, fast, and secure file server that allows you to share files over HTTP. This Docker Compose setup provides an easy way to deploy dufs with authentication.

## Features

- 🚀 Simple HTTP file server
- 🔐 Authentication support (username/password)
- 📤 Upload and download files
- 🐳 Easy Docker deployment
- 🔄 Auto-restart on failure
- 📁 Configurable serving directory

## Quick Start

### 1. Clone or Setup

```bash
git clone <your-repo> dufs
cd dufs
```

### 2. Configure Environment

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```bash
DUFS_PORT=5000              # Port to expose dufs on
DUFS_PATH=~/dufs            # Directory to serve files from
USER=admin                  # Username for authentication
PASSWORD_HASH=<hash>        # Password hash (see below)
```

### 3. Generate Password Hash

To generate a secure password hash for authentication:

```bash
# Using OpenSSL (recommended)
openssl passwd -6 your_password

# Using mkpasswd (if available)
mkpasswd -m sha-512 your_password

# Using Docker
docker run --rm -it alpine mkpasswd -m sha-512 your_password
```

Copy the generated hash to the `PASSWORD_HASH` variable in `.env`.

**Important:** When adding the hash to `.env`, escape any `$` characters by doubling them:
```bash
# If hash is: $6$salt$hash
# In .env use: $$6$$salt$$hash
PASSWORD_HASH=$$6$$qv1HhkSDIAODW3tJ$$R..m7Tg7SnuBHsD2kGB5BnV4b5UyVVM8w7TrubSqlsEXnkfUFf2Sp66tez3DjXhA3zS.MenbUv6FuRdwxU2IC/
```

### 4. Create Serving Directory

```bash
mkdir -p ~/dufs
# Or use your configured DUFS_PATH
```

### 5. Start Dufs

```bash
docker-compose up -d
```

### 6. Access Dufs

Open your browser and navigate to:
```
http://localhost:5000
```

Login with your configured username and password.

## Configuration Options

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `DUFS_PORT` | Port to expose on host | `5000` | `5001` |
| `DUFS_PATH` | Directory to serve | `~/dufs` | `/data/files` |
| `USER` | Authentication username | `admin` | `myuser` |
| `PASSWORD_HASH` | SHA-512 password hash | - | See generation above |

### Docker Compose Configuration

The `docker-compose.yml` uses the following dufs command:

```bash
/data --allow-all -a '${USER}:${PASSWORD_HASH}/@/:rw'
```

**Command breakdown:**
- `/data` - Serve files from /data directory (mounted volume)
- `--allow-all` - Allow all operations (upload, download, delete)
- `-a` - Authentication configuration
- `${USER}:${PASSWORD_HASH}/@/:rw` - User authentication with read/write access

## Usage Examples

### Basic Operations

**Upload files:**
- Drag and drop files into the web interface
- Or use curl:
  ```bash
  curl -u admin:password -T file.txt http://localhost:5000/file.txt
  ```

**Download files:**
- Click files in the web interface
- Or use wget:
  ```bash
  wget --user=admin --password=password http://localhost:5000/file.txt
  ```

**Create directories:**
- Use the web interface "New Folder" button
- Or use curl:
  ```bash
  curl -u admin:password -X MKCOL http://localhost:5000/newfolder/
  ```

**Delete files:**
- Use the web interface delete button
- Or use curl:
  ```bash
  curl -u admin:password -X DELETE http://localhost:5000/file.txt
  ```

### Advanced Configuration

**Change permissions (read-only):**

Edit the command in `docker-compose.yml`:
```yaml
command: >
  /data --allow-all
  -a '${USER}:${PASSWORD_HASH}/@/:ro'  # ro = read-only
```

**Serve specific subdirectory only:**

Update `DUFS_PATH` in `.env`:
```bash
DUFS_PATH=~/dufs/public
```

**Multiple users:**

Edit command in `docker-compose.yml`:
```yaml
command: >
  /data --allow-all
  -a 'admin:${ADMIN_HASH}/@/:rw'
  -a 'guest:${GUEST_HASH}/@/:ro'
```

## Management

### View Logs

```bash
docker-compose logs -f dufs
```

### Stop Service

```bash
docker-compose down
```

### Restart Service

```bash
docker-compose restart
```

### Update to Latest Version

```bash
docker-compose pull
docker-compose up -d
```

## Security Considerations

1. **Strong Passwords**: Always use strong, unique passwords
2. **HTTPS**: For production, use a reverse proxy (nginx/tracer) with SSL
3. **Firewall**: Limit access to trusted networks if possible
4. **Backups**: Regularly backup your `DUFS_PATH` directory
5. **Updates**: Keep dufs updated to the latest version

### Recommended Reverse Proxy Setup (nginx)

```nginx
server {
    listen 443 ssl http2;
    server_name files.yourdomain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # For large file uploads
        client_max_body_size 1000M;
    }
}
```

## Troubleshooting

### Cannot access dufs

**Check if container is running:**
```bash
docker ps | grep dufs
```

**Check logs for errors:**
```bash
docker-compose logs dufs
```

### Authentication fails

**Verify password hash:**
- Ensure `$` characters are doubled in `.env`
- Regenerate hash if needed
- Check username matches exactly

### Permission denied errors

**Check directory permissions:**
```bash
ls -la $(echo $DUFS_PATH)
```

**Fix permissions:**
```bash
chmod 755 ~/dufs
```

### Port already in use

**Change port in `.env`:**
```bash
DUFS_PORT=5001  # Use different port
```

## Additional Resources

- [Dufs GitHub Repository](https://github.com/sigoden/dufs)
- [Docker Hub - sigoden/dufs](https://hub.docker.com/r/sigoden/dufs)
- [Dufs Documentation](https://github.com/sigoden/dufs#readme)

## License

This Docker Compose configuration is provided as-is for convenience. Dufs itself is licensed under its original license terms.

## Support

For issues with:
- **Dufs software**: Report to [sigoden/dufs](https://github.com/sigoden/dufs/issues)
- **This setup**: Create an issue in this repository
