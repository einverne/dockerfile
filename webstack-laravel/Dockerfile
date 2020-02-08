FROM alpine:3.11
ARG WEBSTACK_VERSION=v1.2.6
LABEL maintainer="Ein Verne <einverne@gmail.com>" \
      url="https://github.com/einverne/dockerfile" \
      name="webstack_laravel" \
      license="Apache-2.0" \
      version=$WEBSTACK_VERSION
ENV RUN_USER daemon
ENV RUN_GROUP daemon
ENV INSTALL_DIR /opt/navi
ENV DB_HOST 127.0.0.1
ENV DB_PORT 3306
ENV DB_DATABASE webstack
ENV DB_USERNAME webstack
ENV DB_PASSWORD password
ENV LOGIN_COPTCHA true

ARG DOWNLOAD_URL=https://github.com/hui-ho/WebStack-Laravel/archive/${WEBSTACK_VERSION}.tar.gz
EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN apk update -qq \
	&& apk upgrade \
	&& apk add --no-cache tini \
	   curl composer \
       php-pdo php-fileinfo  php-tokenizer php-gd php-dom  php-xmlwriter php-xml php-pdo_mysql php-session \
    && rm -rf /var/cache/apk/* \
    && mkdir -p ${INSTALL_DIR}

RUN curl -L --silent  ${DOWNLOAD_URL} | tar -xz --strip-components=1 -C "${INSTALL_DIR}" \
    && cd ${INSTALL_DIR} \
    && composer install  \
    && cp .env.example .env \
    && chown -R ${RUN_USER}:${RUN_GROUP} ${INSTALL_DIR}\
    && chown -R ${RUN_USER}:${RUN_GROUP} /entrypoint.sh

WORKDIR ${INSTALL_DIR}
VOLUME ${INSTALL_DIR}
CMD ["/entrypoint.sh", "serve"]
ENTRYPOINT ["/sbin/tini", "--"]
