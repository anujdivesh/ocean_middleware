#!/bin/sh


docker rm middleware_web middleware_db
docker rmi pop_middleware-web
docker volume rm pop_middleware_postgres_data