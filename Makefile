.DEFAULT_GOAL:=help

.PHONY: test
test: ## run tests in tests directory in parallel
	tox

.PHONY: build-docker
build-docker: ## build pyper docker image
	@if [ -n "$(docker images -q pyper:latest)" ]; then \
		docker build -t pyper . ; \
	fi

.PHONY: run-interactive-docker
run-interactive-docker: build-docker ## run in interactive mode in docker
	@docker run --name pyper-interactive --rm -it pyper


.PHONY: help
help: ## Show this help message.
	@echo 'usage: make [target]'
	@echo
	@echo 'targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'