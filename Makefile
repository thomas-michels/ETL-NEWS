include ./.env

## Make migrations
migrate:
	docker run --rm -v $(dir $(realpath $(lastword $(MAKEFILE_LIST))))/migrations:/flyway/sql -e FLYWAY_EDITION=community --network etl-news_news_network flyway/flyway:9-alpine -url=jdbc:postgresql://${DATABASE_HOST}:5432/${DATABASE_NAME} -schemas=flyway -user=${DATABASE_USER} -password=${DATABASE_PASSWORD} -connectRetries=10 migrate
