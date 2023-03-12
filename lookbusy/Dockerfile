FROM --platform=$TARGETPLATFORM debian:11
LABEL org.opencontainers.image.authors="EV"
ARG VERSION="1.4"

COPY ./app /app

WORKDIR /app

RUN apt update \
    && apt install -y curl wget cron git cmake build-essential tar \
    && wget -O "lookbusy.tar.gz" "http://www.devin.com/lookbusy/download/lookbusy-${VERSION}.tar.gz" \
    && mkdir lookbusy \
    && tar xzvf lookbusy.tar.gz -C lookbusy --strip-components=1 \
    && curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash \
    && apt install -y speedtest \
    && cd lookbusy && chmod +x ./configure && ./configure && make && make install \
    && rm -rf /app/lookbusy && chmod +x /app/*.sh \
    && apt autoremove -y && apt autoclean && apt remove -y && apt clean

CMD [ "/app/docker-entrypoint.sh" ]

USER root
