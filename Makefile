# global variables

.DEFAULT_GOAL := help
SHELL := /bin/bash
NAME := ABOCADOS

# help colors

BOLD   := $(shell tput bold)
RED    := $(shell tput setaf 160)
ORANGE    := $(shell tput setaf 208)
GREEN  := $(shell tput setaf 2)
YELLOW := $(shell tput setaf 3)
BLUE   := $(shell tput setaf 45)
MAGENTA := $(shell tput setaf 98)
RESET  := $(shell tput sgr0)

# help command

HELP := $(HELP),
HELP := $(HELP) $(BOLD)$(NAME) MAKE INTERFACE$(RESET),
HELP := $(HELP)   $(BOLD)$(RED)help$(RESET)                    Prints out this help message.,
HELP := $(HELP)   $(BOLD)$(ORANGE)build$(RESET)                   Builds project.,
HELP := $(HELP)   $(BOLD)$(YELLOW)run$(RESET)                     Runs project.,
HELP := $(HELP)   $(BOLD)$(GREEN)setup_database$(RESET)          Migrate and loads database.,
HELP := $(HELP)   $(BOLD)$(BLUE)test$(RESET)                    Runs all the API tests.,
HELP := $(HELP)   $(BOLD)$(MAGENTA)shell$(RESET)                   Opens bash terminal.,

.PHONY: help
help:
	@printf "$(HELP)" | tr , '\n'

DOCKER_COMPOSE_LOCAL=docker-compose.yml
SERVER_SERVICE=server
FRONT_SERVICE=front-web
SERVER_CONTAINER=abocados-server

.PHONY: run
run:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) up -d --remove-orphans

.PHONY: build
build:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) build

.PHONY: stop
stop:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) stop

.PHONY: shell
shell:
	docker exec -ti $(SERVER_CONTAINER) bash

.PHONY: test
test:
	docker exec $(SERVER_CONTAINER) bash -c "python manage.py test"

.PHONY: makemigrations
makemigrations:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py migrate

.PHONY: migrate
migrate:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py migrate

.PHONY: migrate_full
migrate_full:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py makemigrations
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py migrate

.PHONY: load_data
load_data:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/user.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/category.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/recipe.json

.PHONY: setup_database
setup_database:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py makemigrations
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py migrate
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/user.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/category.json
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py loaddata fixtures/recipe.json

.PHONY: createsuperuser
createsuperuser:
	docker-compose -f $(DOCKER_COMPOSE_LOCAL) run --rm $(SERVER_SERVICE) python manage.py createsuperuser

.PHONY: check_linting
check_linting:
	docker exec $(SERVER_CONTAINER) bash -c "flake8"

.PHONY: fix_formatting
fix_formatting:
	docker exec $(SERVER_CONTAINER) bash -c "black ."
	docker exec $(SERVER_CONTAINER) bash -c "isort ."

.PHONY: generate_translations
generate_translations:
	docker exec $(SERVER_CONTAINER) bash -c "python manage.py makemessages -a"
