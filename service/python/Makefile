
VERSION=$(shell cat VERSION)

.PHONY: version

version: ## Report current version of the code
	@echo "Code version: ${VERSION}"


buildforlocal: ## Build image using local docker daemon
	docker build . -t pythonhello:$(VERSION)


help: ## Show this help.
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
