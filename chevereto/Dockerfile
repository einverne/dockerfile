FROM php:7.1.3-apache

ENV CHEVERETO_APACHE_RUN_USER www-data
ENV CHEVERETO_VERSION 1.0.12

# DB connection environment variables
ENV CHEVERETO_DB_HOST db
ENV CHEVERETO_DB_USERNAME chevereto
ENV CHEVERETO_DB_PASSWORD chevereto
ENV CHEVERETO_DB_NAME chevereto
ENV CHEVERETO_DB_PREFIX chv_

LABEL maintainer="Ein Verne <einverne@gmail.com>" \
      url="https://github.com/einverne/dockerfile" \
      name="Chevereto Free" \
      license="Apache-2.0" \
      version=$CHEVERETO_VERSION

# Install required packages
RUN apt-get update && apt-get install -y \
        libgd-dev

# Install php extensions that we need for Chevereto and its installer
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install \
    gd \
    mysqli \
    pdo \
    pdo_mysql
 
# Enable mod_rewrite for Chevereto
RUN a2enmod rewrite

# Download installer script
WORKDIR /var/www/html
USER ${CHEVERETO_APACHE_RUN_USER}
RUN curl -o chevereto.tar.gz https://codeload.github.com/Chevereto/Chevereto-Free/tar.gz/${CHEVERETO_VERSION} \
    && tar -xzf chevereto.tar.gz --strip 1 \
    && rm -f ${CHEVERETO_VERSION} \
    && chown -R www-data:www-data /var/www/html \
    && chown -R www-data:www-data /var/www/html/images

COPY settings.php app/settings.php

# Expose the image directory
VOLUME /var/www/html/images

# Change back to root user for normal Service start up
USER root

