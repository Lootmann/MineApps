run:
	docker compose up -d

.PHONY: build
build:
	docker compose build

.PHONY: down
down:
	docker compose down

.PHONY: test
test:
	docker compose exec app python3.10 -m pytest -svv

.PHONY: watch
watch:
	cd ./app/tools/ && yarn watch

.PHONY: login
login:
	docker compose exec app /bin/bash

.PHONY: logs
logs:
	docker compose logs -ft

.PHONY: dump
dump:
	docker compose exec app python3.10 manage.py dumpdata --format=yaml > ./dumps/data.yaml
