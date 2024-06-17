# global variables
CONTAINER=abocados-server-prod

.PHONY: run
run:
	docker run --env-file .env -p 3003:3003 --name=$(CONTAINER) $(CONTAINER)

.PHONY: build
build:
	docker build -t $(CONTAINER) .
	docker exec $(CONTAINER) bash -c "python manage.py makemigrations"
	docker exec $(CONTAINER) bash -c "python manage.py migrate"

.PHONY: stop
stop:
	docker stop $(CONTAINER)

.PHONY: test
test:
	docker exec $(CONTAINER) bash -c "python manage.py test"

.PHONY: setup_database
setup_database:
	docker exec $(CONTAINER) bash -c "python manage.py makemigrations"
	docker exec $(CONTAINER) bash -c "python manage.py migrate"
	docker exec $(CONTAINER) bash -c "python manage.py loaddata fixtures/user.json"
	docker exec $(CONTAINER) bash -c "python manage.py loaddata fixtures/category.json"
	docker exec $(CONTAINER) bash -c "python manage.py loaddata fixtures/recipe.json"
