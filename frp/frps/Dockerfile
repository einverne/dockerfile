FROM alpine:3.7

LABEL maintainer="Ein Verne <einverne@gmail.com>"

ARG TZ='Asia/Shanghai'

ENV TZ ${TZ}
ENV FRP_PATH frp_linux
ENV FRP_FILENAME frp.tar.gz

RUN apk upgrade --update \
    && apk add bash tzdata wget \
    && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo "${TZ}" > /etc/timezone \
    && FRP_DOWNLOAD_URL=`wget -qO- "https://api.github.com/repos/fatedier/frp/releases/latest" | grep "browser_download_url" | grep "linux_amd64" | sed -E 's/.*"([^"]+)".*/\1/'` \
    && wget ${FRP_DOWNLOAD_URL} -O ${FRP_FILENAME} \
    && mkdir -p ${FRP_PATH} \
    && tar -zxf ${FRP_FILENAME} --strip 1 -C ${FRP_PATH} \
    && rm -f ${FRP_FILENAME} \
    && rm -f ${FRP_PATH}/LICENSE \
    && mkdir -p /etc/frp/ \
    && mv ${FRP_PATH}/* /usr/local/bin \
    && apk del wget \
    && rm -rf /var/cache/apk/* ${FRP_PATH}

ADD frps.ini /etc/frp/frps.ini

EXPOSE 7000

CMD ["frps","-c","/etc/frp/frps.ini"]

