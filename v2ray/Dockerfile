FROM alpine:3.6
LABEL maintainer="Ein Verne <einverne@gmail.com>"

ENV TZ 'Asia/Shanghai'

ENV V2RAY_VERSION v4.31.0

RUN apk upgrade --update \
    && apk add \
        bash \
        tzdata \
        curl \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && mkdir -p \
        /var/log/v2ray \
        /usr/bin/v2ray \
        /tmp/v2ray \
        /etc/v2ray/ \
    && curl -L -H "Cache-Control: no-cache" -o /tmp/v2ray/v2ray.zip \
        https://github.com/v2ray/v2ray-core/releases/download/${V2RAY_VERSION}/v2ray-linux-64.zip \
    && unzip /tmp/v2ray/v2ray.zip -d /tmp/v2ray/ \
    && mv /tmp/v2ray/v2ray-${V2RAY_VERSION}-linux-64/* /usr/bin/v2ray/ \
    && chmod +x /usr/bin/v2ray/v2ray && chmod +x /usr/bin/v2ray/v2ctl \
    && apk del curl \
    && rm -rf /tmp/v2ray /var/cache/apk/*

EXPOSE 10800

COPY config.json /etc/v2ray/config.json
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
