[linuxserverurl]: https://linuxserver.io
[forumurl]: https://forum.linuxserver.io
[ircurl]: https://www.linuxserver.io/irc/
[podcasturl]: https://www.linuxserver.io/podcast/
[appurl]: https://tt-rss.org
[hub]: https://hub.docker.com/r/linuxserver/tt-rss/

[![linuxserver.io](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/linuxserver_medium.png)][linuxserverurl]

The [LinuxServer.io][linuxserverurl] team brings you another container release featuring easy user mapping and community support. Find us for support at:
* [forum.linuxserver.io][forumurl]
* [IRC][ircurl] on freenode at `#linuxserver.io`
* [Podcast][podcasturl] covers everything to do with getting the most from your Linux Server plus a focus on all things Docker and containerisation!

# linuxserver/tt-rss
[![](https://images.microbadger.com/badges/version/linuxserver/tt-rss.svg)](https://microbadger.com/images/linuxserver/tt-rss "Get your own version badge on microbadger.com")[![](https://images.microbadger.com/badges/image/linuxserver/tt-rss.svg)](https://microbadger.com/images/linuxserver/tt-rss "Get your own image badge on microbadger.com")[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/tt-rss.svg)][hub][![Docker Stars](https://img.shields.io/docker/stars/linuxserver/tt-rss.svg)][hub][![Build Status](https://ci.linuxserver.io/buildStatus/icon?job=Docker-Builders/x86-64/x86-64-tt-rss)](https://ci.linuxserver.io/job/Docker-Builders/job/x86-64/job/x86-64-tt-rss/)

[Tiny Tiny RSS][appurl] is an open source web-based news feed (RSS/Atom) reader and aggregator, designed to allow you to read news from any location, while feeling as close to a real desktop application as possible.


[![tt-rss](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/tt-rss-banner.png)][appurl]

## Usage

```
docker create \
--name=tt-rss \
-v /etc/localtime:/etc/localtime:ro \
-v <path to data>:/config \
-e PGID=<gid> -e PUID=<uid> \
-e TZ=<timezone> \
-p 80:80 \
linuxserver/tt-rss
```

## Parameters

`The parameters are split into two halves, separated by a colon, the left hand side representing the host and the right the container side. 
For example with a port -p external:internal - what this shows is the port mapping from internal to external of the container.
So -p 8080:80 would expose port 80 from inside the container to be accessible from the host's IP on port 8080
http://192.168.x.x:8080 would show you what's running INSIDE the container on port 80.`


* `-p 80` - webui port *see note below*
* `-v /etc/localtime` for timesync - *optional* *omit if using TZ variable*
* `-v /config` - where tt-rss should store it's config files
* `-e PGID` for GroupID - see below for explanation
* `-e PUID` for UserID - see below for explanation
* `-e TZ` for setting timezone information, eg Europe/London 

It is based on alpine linux with s6 overlay, for shell access whilst the container is running do `docker exec -it tt-rss /bin/bash`.

### User / Group Identifiers

Sometimes when using data volumes (`-v` flags) permissions issues can arise between the host OS and the container. We avoid this issue by allowing you to specify the user `PUID` and group `PGID`. Ensure the data volume directory on the host is owned by the same user you specify and it will "just work" ™.

In this instance `PUID=1001` and `PGID=1001`. To find yours use `id user` as below:

```
  $ id <dockeruser>
    uid=1001(dockeruser) gid=1001(dockergroup) groups=1001(dockergroup)
```

## Setting up the application 

You must create a user and database for tt-rss to use in a mysql/mariadb or postgresql server. In the setup page for database, use the ip address rather than hostname...

A basic nginx configuration file can be found in /config/nginx/site-confs , edit the file to enable ssl (port 443 by default), set servername etc.. Self-signed keys are generated the first time you run the container and can be found in /config/keys , if needed, you can replace them with your own.

The site files are in /config/www/tt-rss , you can find config files and themes folder there. Email and other settings are in the config.php file.

## Info

* To monitor the logs of the container in realtime `docker logs -f tt-rss`.

* container version number 

`docker inspect -f '{{ index .Config.Labels "build_version" }}' tt-rss`

* image version number

`docker inspect -f '{{ index .Config.Labels "build_version" }}' linuxserver/tt-rss`


## Versions

+ **08.01.18:** Rebase to alpine linux 3.7.
+ **19.07.17:** Use updated [repository](https://git.tt-rss.org/git/tt-rss) for initial install.
+ **25.05.17:** Rebase to alpine linux 3.6.
+ **23.02.17:** Rebase to alpine linux 3.5 and nginx.
+ **14.10.16:** Add version layer information.
+ **10.09.16:** Add layer badges to README. 
+ **31.08.15:** Initial Release.
