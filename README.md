# worldcupprono

Fun website for pronostic world cup 2018

[![Build Status](https://travis-ci.org/raisou/worldcupprono.svg?branch=master)](https://travis-ci.org/raisou/worldcupprono)

## Rules

Prono correct = 1 pt
Score correct = 3 pt

## Main points

- / : Vuejs app
- /api : Rest Api
- /admin : Path to django admin to be able to update match scores (need to be superuser)
- /docs : Swagger doc api (main points need to have an authenticated user)

## How to start

### LOCAL ENV WITH DOCKER (Recommended)

#### Docker compose env

To be able to easily run on every linux dev env keeping production-like dependencies we use **docker**. With **docker-compose** we deal with dependencies.

1. Install Docker and Docker-compose.

    On Ubuntu pay attention on user rights, it is not recommended to run it as root https://docs.docker.com/engine/installation/linux/linux-postinstall/

    *The first time you'll use docker-compose it will build and download docker images, it can take a long time*

2. clone this repository and get you in the project root directory

3. create a file local.py in worldcupprono/settings/ following the example local.py.example (copy/paste should be enough, then you can custom it)

4. create a virtualenv in docker env :
```
docker-compose run --rm app virtualenv /env -p /usr/bin/python3.6
```

5. Install project dependencies
```
docker-compose run --rm app /env/bin/pip install -r requirements.txt
```

6. Install dependencies for dev env
```
docker-compose run --rm app /env/bin/pip install -r requirements-dev.txt
```

7. To generate initial database and data fixtures (for dev purpose)
```
docker-compose run --rm app /env/bin/python manage.py reset_db
```

8. To get frontend dependencies
```
docker-compose run --rm app bash -c 'cd frontend/ && npm i'
```

9. Create superuser
```
docker-compose run --rm app /env/bin/python manage.py createsuperuser
```

10. To run tests
```
docker-compose run --rm app /env/bin/pip install -r requirements-tests.txt
docker-compose run --rm app /env/bin/python manage.py test
```

To run dev env i recommend the use of tmuxinator. I join the file wcp.yml.example.

If you do not use tmuxinator you can see the commands i run in the panes section.

### LOCAL ENV FOR Ubuntu 16.04

#### Prerequisites
- Python3.6 (see https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa)
    => +python3.6-dev package
- Postgresql 9.6 (see https://www.postgresql.org/download/linux/ubuntu/)
- Nodejs v8.x (see https://github.com/nodesource/distributions)

To start:

1. clone this repository

2. install postgresql + create user + database

3. create a file local.py in worldcupprono/settings/ following the example local.py.example

4. Create a python virtualenv the way you like, example:
```
virtualenv wcp -p /usr/bin/python3.6
```

5. Install dependencies
```
pip install -r requirements.txt
```

6. Install dev dependencies
```
pip install -r requirements-dev.txt
```

6. To generate initial database and data (for dev purpose)
```
python manage.py reset_db
```

7. To create superuser
```
python manage.py createsuperuser
```

8. To install frontend dependencies
```
cd frontend/ && npm install
```

9. To run backend
```
python manage.py runserver
```
Then hit 127.0.0.1:8000

10. To run frontend
```
cd frontend/ && npm run dev
```
Then hit 127.0.0.1:8080

11. To run tests
```
pip install -r requirements-tests.txt
python manage.py test
```
