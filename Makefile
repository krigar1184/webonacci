build:
	docker-compose build

run: build
	docker-compose up -d

down:
	docker-compose stop

bash:
	docker-compose exec app bash

test: run
	docker-compose exec app pytest
