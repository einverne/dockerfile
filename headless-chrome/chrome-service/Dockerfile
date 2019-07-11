FROM einverne/chromedriver

LABEL maintainer="Ein Verne <einverne@gmail.com>"

USER root
RUN apt-get install -y python-pip \
    && pip install selenium flask gunicorn

COPY server.py /
COPY gunicorn.sh /
RUN chmod +x gunicorn.sh

USER headless
EXPOSE 9223

ENTRYPOINT ["/gunicorn.sh"]