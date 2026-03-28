.PHONY: build up down logs test shell

build:
docker compose build

up:
docker compose up

down:
docker compose down

logs:
docker compose logs -f

test:
docker compose run --rm web python manage.py test

shell:
docker compose run --rm web sh
