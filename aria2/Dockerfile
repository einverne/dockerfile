FROM alpine:edge
LABEL maintainer="Ein Verne <einverne@gmail.com>"

RUN apk update && \
	apk add --no-cache --update bash && \
	mkdir -p /conf && \
	mkdir -p /conf && \
	mkdir -p /data && \
	apk add --no-cache --update aria2 && \
	apk add git && \
	git clone https://github.com/ziahamza/webui-aria2 /aria2-webui && \
    rm -rf /aria2-webui/.git* && \
    apk del git && \
	apk add --update darkhttpd

ADD conf/start.sh /conf-custom/start.sh
ADD conf/aria2.conf /conf-custom/aria2.conf
ADD conf/on-complete.sh /conf-custom/on-complete.sh

RUN chmod +x /conf-custom/start.sh

WORKDIR /
VOLUME ["/data"]
VOLUME ["/conf"]
EXPOSE 6800
EXPOSE 80
EXPOSE 8080

CMD ["/conf-custom/start.sh"]
