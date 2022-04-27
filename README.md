# blog_comments_api
## Requirements
* Debian 10+ /Ubuntu 20.04+
* Docker 20.10+
* Docker Compose 1.29+
* Python 3.9+
* Poetry

## Prepare
Download repository
```bash
$ git clone https://github.com/Twylixy/blog_comments_api.git
```
Save **.env.dev.example** (or **.env.prod.example**) without **.example** tail and edit variables.

(Optional) Install Poetry
Requiered for future dependencies updates
```bash
python3 -m pip install poetry
```

## Deploy (development)
```bash
$ cd /path/to/project/root/
$ docker-compose -f docker-compose.dev.yml up -d --build
```

## Deploy (production)
```bash
$ cd /path/to/project/root/
$ docker-compose -f docker-compose.prod.yml up -d --build
```

## Shutdown
```bash
$ cd /path/to/project/root/
$ docker-compose -f docker-compose.dev.yml down # development
or
$ docker-compose -f docker-compose.prod.yml down # production
```

## On dependency update
Needed for update requirements.txt for docker container installation
```bash
cd /path/to/project/root/
$ poetry export -f requirements.txt -o requirements.txt
```

## Project's API
You can see API structure here [here](https://github.com/Twylixy/blog_comments_api/blob/master/API.md).