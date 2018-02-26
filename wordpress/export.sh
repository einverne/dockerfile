#!/bin/bash
now=$(date +"%m_%d_%Y")
file="data_$now.sql"
docker exec wordpress_db sh -c 'exec mysqldump wordpress -uroot -p"$MYSQL_ROOT_PASSWORD"' > $file

