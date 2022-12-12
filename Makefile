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
	@pipenv install --ignore-pipfile
	@cd /app && mkdir data && cd data
	@mkdir mp3_folder text_folder mp4_folder

.PHONY: lint
lint:   ## Lint the project files
	@echo "Formatting with autopep8"
	@PIPENV_VERBOSITY=-1 pipenv run autopep8 -i -r ./
	@echo "Check for errors with flake8"
	@PIPENV_VERBOSITY=-1 pipenv run flake8 ./

.PHONY: tests
tests:  ## Locally run tests
	@PYTHONPATH=src PIPENV_VERBOSITY=-1 pipenv run pytest -v tests/

AUDIO_PARSER_MODULE ?= audio_parser
VIDEO_PARSER_MODULE ?= video_parser
DATA_DIRECTORY ?= $(PWD)/data

.PHONY: run-audio-parser
run-audio-parser: ## Runs locally selected module
	@PYTHONPATH=src PIPENV_VERBOSITY=-1 pipenv run python -m $(AUDIO_PARSER_MODULE)

.PHONY: run-video-parser
run-video-parser: ## Runs locally selected module
	@PYTHONPATH=src PIPENV_VERBOSITY=-1 pipenv run python -m $(VIDEO_PARSER_MODULE)

.PHONY: build-audio-parser-image
build-audio-parser-image:  ## Create a docker image
	@cp $(PWD)/docker/$(AUDIO_PARSER_MODULE)/Dockerfile .
	@docker build -t "$(AUDIO_PARSER_MODULE)" $(PWD)
	@rm Dockerfile

.PHONY: build-video-parser-image
build-video-parser-image:  ## Create a docker image
	@cp $(PWD)/docker/$(VIDEO_PARSER_MODULE)/Dockerfile .
	@docker build -t "$(VIDEO_PARSER_MODULE)" $(PWD)
	@rm Dockerfile

.PHONY: run-video-parser-image
run-video-parser-image:  ## Run docker image (needs build first)
	@docker run --rm \
	-v "$(DATA_DIRECTORY)/mp3_folder":/app/data/mp3_folder \
	-v "$(DATA_DIRECTORY)/text_folder":/app/data/text_folder \
	-v "$(DATA_DIRECTORY)/mp4_folder":/app/data/mp4_folder \
	$(VIDEO_PARSER_MODULE) \
	make run-video-parser

.PHONY: run-audio-parser-image
run-audio-parser-image:  ## Run docker image (needs build first)
	@docker run --rm \
	-v "$(DATA_DIRECTORY)/mp3_folder":/app/data/mp3_folder \
	-v "$(DATA_DIRECTORY)/text_folder":/app/data/text_folder \
	-v "$(DATA_DIRECTORY)/mp4_folder":/app/data/mp4_folder \
	$(AUDIO_PARSER_MODULE) \
	make run-audio-parser
