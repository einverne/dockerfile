# qBittorrent

The default username and password is admin/adminadmin, try to change it after booting up in the WEB UI.

qBittorrent default 6881 port is usually blocked by many trackers. So I replace it with 49153. Remember to modify it in the settings after booting up. If the torrent is showing stalled status, remember to change the Listening port to 49153 which is defined in the `docker-compose.yml`.

	cp env .env
	mkdir -p ~/qbittorrent/{config,downloads,watch}
	docker-compose up -d

- <https://www.qbittorrent.org/>
