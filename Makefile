.PHONY: build up down install-scraper run-scraper dbt-run dbt-test

COMPOSE=docker-compose -f docker/docker-compose.yml

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

install-scraper:
	pip install -r requirements.txt

run-scraper:
	python src/scraper.py

dbt-run:
	dbt run --profiles-dir dbt/

dbt-test:
	dbt test --profiles-dir dbt/ 