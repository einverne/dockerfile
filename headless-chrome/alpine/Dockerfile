FROM alpine:3.7
# current development of Alpine Linux
# FROM alpine:edge

LABEL maintainer="Ein Verne <einverne@gmail.com>"

ARG TZ="Asia/Shanghai"

# Update apk repositories
#RUN echo "http://dl-2.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories
#RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
#RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

ENV TZ ${TZ}

# https://pkgs.alpinelinux.org/package/edge/community/x86_64/chromium
RUN apk update && apk add --no-cache bash \
    alsa-lib \
    at-spi2-atk \
    atk \
    cairo \
    cups-libs \
    dbus-libs \
    eudev-libs \
    expat \
    flac \
    gdk-pixbuf \
    glib \
    libgcc \
    libjpeg-turbo \
    libpng \
    libwebp \
    libx11 \
    libxcomposite \
    libxdamage \
    libxext \
    libxfixes \
    tzdata \
    libexif \
    udev \
    xvfb \
    zlib-dev \
    chromium \
    chromium-chromedriver \
    && apk add wqy-zenhei --update-cache --repository http://nl.alpinelinux.org/alpine/edge/testing --allow-untrusted \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && rm -rf /var/cache/apk/* \
    /usr/share/man \
    /tmp/*

RUN mkdir -p /data && adduser -D chrome \
    && chown -R chrome:chrome /data
USER chrome

EXPOSE 9222

# chrome launch flag https://peter.sh/experiments/chromium-command-line-switches/
ENTRYPOINT [ "chromium-browser", \
  "--headless", "--no-sandbox", "--disable-gpu", \
  "--remote-debugging-address=0.0.0.0", \
  "--remote-debugging-port=9222", \
  "--disable-dev-shm-usage", \
  "--window-size=1920,1080", \
  # Disable various background network services, including extension updating,
  #   safe browsing service, upgrade detector, translate, UMA
  "--disable-background-networking", \
  # Disable installation of default apps on first run
  "--disable-default-apps", \
  # Disable all chrome extensions entirely
  "--disable-extensions", \
  # Disable syncing to a Google account
  "--disable-sync", \
  # Disable chrome pop-up notifications which cover the page
  "--disable-notifications", \
  # Disable built-in Google Translate service
  "--disable-translate", \
  # Hide scrollbars on generated images/PDFs
  "--hide-scrollbars", \
  # Disable reporting to UMA, but allows for collection
  "--metrics-recording-only", \
  # Mute audio
  "--mute-audio", \
  # Skip first run wizards
  "--no-first-run", \
  # Disable fetching safebrowsing lists, likely redundant due to disable-background-networking
  "--safebrowsing-disable-auto-update", \
  # set user data path
  "--user-data-dir=/data" \
]

