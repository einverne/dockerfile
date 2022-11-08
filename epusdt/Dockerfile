FROM debian:bullseye

RUN apt-get update \
    && apt-get install -y apt-transport-https ca-certificates curl \
    && curl -fsSLo epusdt.tar.gz https://github.com/assimon/epusdt/releases/download/v0.0.1/epusdt_v0.0.1_Linux_x86_64.tar.gz \
    && mkdir -p /app \
    && tar xfz epusdt.tar.gz -C /app \
    && rm -rf epusdt.tar.gz

WORKDIR /app

ENTRYPOINT [ "/app/epusdt" ]
CMD [ "http", "start" ]

