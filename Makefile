build:
	docker-compose build

run: build
	docker-compose up -d

stop:
	docker-compose down

bash:
	docker-compose exec app bash

test: run
	docker-compose exec app pytest
