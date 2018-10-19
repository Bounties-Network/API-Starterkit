## Setup
[Download Docker stable version](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)
```
docker volume create --name starter_psql
docker-compose up
```
You may access the api at:

http://locahost:8000

The API will automatically restart if you make code changes. To turn off the services, run `docker-compose down`. Keep in mind, the volumes make it so your DB will be in the same state if you start the services again with `docker-compose up`. If you would like to wipe out your databases and start again, then run:
```
docker-compose down
docker volume rm starter_psql
docker volume create --name starter_psql
docker-compose up
```