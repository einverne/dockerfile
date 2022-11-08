# ZooKeeper

single node:

```
docker run -d --name zookeeper -p 2181:2181 zookeeper:3.5.8
```

enter container:

```
docker exec -it ContainerID /bin/bash
cd /apache-zookeeper-3.5.8-bin/bin
./zkCli.sh -server 127.0.0.1:2181
```

