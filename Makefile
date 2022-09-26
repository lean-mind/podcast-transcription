.DEFAULT_GOAL := help

MP3_FOLDER ?= audio_mp3_folder
TEXT_FOLDER ?= audio_text_folder
PROJECT_NAME ?= podcast-transcription

.PHONY: help
help:  ## Show this help
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup local environment
	@pipenv install --dev

.PHONY: setup-docker
setup-docker: ## Setup local environment only for dockerfile
	@pipenv install

.PHONY: lint
lint:   ## Lint the project files
	@echo "Formatting with autopep8"
	@PIPENV_VERBOSITY=-1 pipenv run autopep8 -i -r ./
	@echo "Check for errors with flake8"
	@PIPENV_VERBOSITY=-1 pipenv run flake8 ./

.PHONY: tests
tests:  ## Locally run tests
	@PYTHONPATH=src PIPENV_VERBOSITY=-1 pipenv run pytest -v tests/

.PHONY: run-local
run-local:
	@PYTHONPATH=src PIPENV_VERBOSITY=-1 pipenv run python -m src

.PHONY: build-image
build-image:  ## Create a docker image
	@docker build -t "${PROJECT_NAME}" $(PWD)

.PHONY: run-image
run-image:  ## Run docker image (needs build first)
	@docker run --rm --volume "$(PWD)/${MP3_FOLDER}":/${MP3_FOLDER} "$(PWD)/${TEXT_FOLDER}":/${TEXT_FOLDER} ${PROJECT_NAME} make run-local
