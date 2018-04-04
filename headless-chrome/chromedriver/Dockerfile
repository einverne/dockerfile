FROM debian:stable-slim

LABEL maintainer="Ein Verne <einverne@gmail.com>"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -qqy \
  && apt-get -qqy install \
       dumb-init gnupg wget ca-certificates apt-transport-https \
       ttf-wqy-zenhei \
       python-pip unzip \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN wget http://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip -d /usr/local/bin/ \
  && rm chromedriver_linux64.zip

RUN wget -qO- https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -y \
  && apt-get -y install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN useradd headless --shell /bin/bash --create-home \
  && usermod -a -G sudo headless \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'headless:nopassword' | chpasswd

RUN mkdir /data && chown -R headless:headless /data

USER headless

EXPOSE 9222

ENTRYPOINT ["/usr/bin/dumb-init", "--", \
            "/usr/bin/google-chrome", \
            "--disable-gpu", \
            "--headless", \
            "--no-sandbox", \
            "--disable-dev-shm-usage", \
            "--window-size=1920,1080", \
            "--remote-debugging-address=0.0.0.0", \
            "--remote-debugging-port=9222", \
            "--user-data-dir=/data"]

