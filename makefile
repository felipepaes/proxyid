.PHONY: build build-clean cache-clean help install mock-project-set mock-project-run mock-project-clean test test-complete


help: ## Show this help
	@echo
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

cache-clean: ## Remove .pyc and .pyo files
	find . -name '*.pyc' -exec rm --force {} \;
	find . -name '*.pyo' -exec rm --force {} \;

install: ## Install dependencies from Pipfile
	pipenv install --dev


# commands

build: ## Build python package
	pipenv run python -m build

build-clean: ## Remove package building generated files
	rm --recursive --force build/
	rm --recursive --force dist/
	rm --recursive --force *.egg-info

mock-project-set: ## Set django_mock_project database and load fixtures
	python tests/django_mock_project/manage.py migrate
	python tests/django_mock_project/manage.py loaddata person.json

mock-project-run: mock-project-set ## Run django_mock_project 
	python tests/django_mock_project/manage.py runserver

mock-project-clean: ## Remove django_mock_project generated files
	rm tests/django_mock_project/*.sqlite*

test: ## Run tests via Pytest
	pipenv run pytest tests/

test-complete: ## Run tests against multiple python and django version via Tox
	pipenv run tox

