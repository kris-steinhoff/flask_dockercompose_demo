# flask + docker_compose demo #

## Setup for docker-compose ##

Initial setup

```
docker-compose build
docker-compose up --no-start
docker-compose start
docker-compose run web flask initdb
docker-compose stop
```

Starting the development environment

```
docker-compose up
```

then open your Docker machine's address on port 5000.
