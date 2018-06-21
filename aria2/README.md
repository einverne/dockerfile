## Aria2 webui

一键

    sudo docker run -d \
    --name aria2 \
    -p 6800:6800 \
    -p 6880:80 \
    -p 6888:8080 \
    -v /DOWNLOAD_DIR:/data \
    -v /CONFIG_DIR:/conf \
    -e SECRET=YOUR_SECRET_CODE \
    einverne/aria2

- 6880 for aria2-webui
- 6888 browse data folder

或者本地编译

    sudo docker build -t "aria2" .
