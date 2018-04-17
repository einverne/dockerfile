FROM php:7.1-apache

RUN curl -L -o tmp.tgz https://github.com/RSS-Bridge/rss-bridge/tarball/master/ \
        && tar -zxvf tmp.tgz --strip=1 \
        && rm tmp.tgz \
        && echo "Instagram" > whitelist.txt \
        && chown -R www-data:www-data *
