# qBittorrent

qBittorrent default 6881 port is usually blocked by many trackers. So I replace it with 49153. Remember to modify it in the settings after booting up.

	cp env .env
	mkdir -p ~/qbittorrent/{config,downloads,watch}
	docker-compose up -d


- <https://www.qbittorrent.org/>
