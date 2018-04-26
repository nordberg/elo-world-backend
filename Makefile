.PHONY: build start migrate

build:
	docker-compose build

start:
	docker-compose up -d

migrate:
	docker-compose exec api python /app/migrate.py

clean:
	- docker-compose kill
	- docker-compose rm -f
