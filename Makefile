.DEFAULT_GOAL := help

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
	@docker build -t "podcast-transcription" $(PWD)

.PHONY: run-image
run-image:  ## Run docker image (needs build first)
	@docker run --rm \
	-v "$(PWD)/audio_mp3_folder":/app/audio_mp3_folder \
	-v "$(PWD)/audio_text_folder":/app/audio_text_folder \
	podcast-transcription \
	make run-local
