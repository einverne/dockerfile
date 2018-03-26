FROM alpine:latest

LABEL maintainer="Ein Verne <einverne@gmail.com>"

RUN apk --no-cache add privoxy \
        && sed -i 's/listen-address\s*127.0.0.1:8118/listen-address 0.0.0.0:8118/g' /etc/privoxy/config
ADD start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh

CMD ["start.sh"]

EXPOSE 8118

