FROM jwilder/nginx-proxy:alpine
RUN echo 'client_max_body_size 0;' > /etc/nginx/conf.d/custom.conf \
    && echo 'server_tokens off;' >> /etc/nginx/conf.d/custom.conf
