# Fast Note Sync

A Docker-based note synchronization service that provides real-time note syncing capabilities through REST API and WebSocket connections.

## Features

- **REST API**: HTTP API service on port 9000
- **WebSocket**: Real-time sync on port 9001
- **Persistent Storage**: Data stored in local volumes
- **Auto-restart**: Container restarts automatically on failure

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone or navigate to this directory:
```bash
cd fast-note-sync
```

2. Create environment file:
```bash
cp .env.example .env
```

Edit `.env` to configure your data directory (default is current directory):
```bash
FAST_NOTE_SYNC=/path/to/your/data
```

3. (Optional) Customize configuration:
```bash
# Edit config/config.yaml to customize service settings
nano config/config.yaml
```

4. Start the service:
```bash
docker-compose up -d
```

5. Verify the service is running:
```bash
docker-compose ps
```

### Access

- **API Endpoint**: http://localhost:9000
- **WebSocket**: ws://localhost:9001

## Directory Structure

```
fast-note-sync/
├── docker-compose.yml      # Docker Compose configuration
├── .env.example            # Environment variables template
├── .env                    # Your environment configuration (create from .env.example)
├── config/                 # Configuration directory
│   └── config.yaml         # Main configuration file
└── storage/                # Data storage (auto-created)
    ├── database/           # SQLite database
    ├── uploads/            # Uploaded files
    ├── temp/               # Temporary files
    └── logs/               # Application logs
```

## Management Commands

**Start service:**
```bash
docker-compose up -d
```

**Stop service:**
```bash
docker-compose down
```

**View logs:**
```bash
docker-compose logs -f
```

**Restart service:**
```bash
docker-compose restart
```

**Update to latest version:**
```bash
docker-compose pull
docker-compose up -d
```

## Configuration

### Environment Variables

Create a `.env` file from the template:
```bash
cp .env.example .env
```

**Available variables:**
- `FAST_NOTE_SYNC`: Base directory for data storage (default: `.` - current directory)

### Application Configuration

The main configuration file is located at `config/config.yaml`. Key settings include:

**Server Configuration:**
- `run-mode`: Server mode (release/debug)
- `http-port`: API server port (default: 9000)
- `private-http-listen`: WebSocket port (default: 9001)

**Application Settings:**
- `default-page-size`: Pagination size (default: 10)
- `soft-delete-retention-time`: Deleted notes retention (default: 7d)
- `history-keep-versions`: History versions to keep (default: 100)

**Security:**
- `auth-token-key`: Token encryption key
- `token-expiry`: Token expiration time (default: 7d)

**Database:**
- `type`: Database type (default: sqlite)
- `path`: Database file path (default: storage/database/db.sqlite3)

**User Management:**
- `register-is-enable`: Allow user registration (default: true)
- `admin-uid`: Admin user ID (0 = no admin access)

Refer to `config/config.yaml` for all available options and detailed descriptions.

## Data Persistence

All note data is stored in the `./storage` directory, which is mounted to `/fast-note-sync/storage` inside the container. This ensures your data persists across container restarts.

## Ports

| Port | Protocol | Purpose |
|------|----------|---------|
| 9000 | HTTP | REST API |
| 9001 | WebSocket | Real-time sync |

## Troubleshooting

**Port conflicts:**
If ports 9000 or 9001 are already in use, modify the port mappings in `docker-compose.yml`:
```yaml
ports:
  - "YOUR_PORT:9000"  # Change YOUR_PORT
  - "YOUR_PORT:9001"  # Change YOUR_PORT
```

**Permission issues:**
Ensure the `storage` and `config` directories have proper permissions:
```bash
chmod -R 755 storage config
```

## License

Refer to the service documentation for licensing information.
