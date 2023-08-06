#!/bin/bash
if docker ps -a | grep bruhforum-mysql
then
    docker start bruhforum-mysql
else
    docker run --name bruhforum-mysql -p 3306:3306 -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d mysql:8.1.0
fi