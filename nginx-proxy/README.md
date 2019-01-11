在运行

    sudo docker-compose up
    
之前，如果遇到

    ERROR: Network nginx-proxy declared as external, but could not be found. Please create the network manually using `docker network create nginx-proxy` and try again.

需要首先创建

    sudo docker network create nginx-proxy
    
然后

    sudo docker-compose up -d
    
    