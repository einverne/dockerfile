FROM golang:alpine

RUN set -ex \
        && apk add --no-cache --virtual .build-deps git \
        && go get github.com/andreimarcu/linx-server \
        && apk del .build-deps

ADD config.ini /etc/linx/config.ini

VOLUME ["/data/files", "/data/meta"]

EXPOSE 8080
#USER nobody
ENTRYPOINT ["/go/bin/linx-server", "-config=/etc/linx/config.ini", "-bind=0.0.0.0:8080", "-filespath=/data/files/", "-metapath=/data/meta/"]
CMD ["-sitename=linx", "-allowhotlink"]
