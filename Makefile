export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1

.PHONY: up

up:
	./pb/scripts/compile
	docker-compose build