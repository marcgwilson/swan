SHELL := /bin/bash # Use bash syntax
NS = swan
REPO = python3
IMAGE = $(NS)/$(REPO)

define latest_version
	$(shell docker images $(1) --format '{{.Tag}}' | sort -r | head -n 1 | sed -e 's/[^0-9]//g' || 0)
endef

define next_version
	$(shell echo $$(($(1)+1)))
endef

LATEST=$(strip $(call latest_version,$(IMAGE)))
NEXT=$(strip $(call next_version,$(LATEST)))

.PHONY: build rebuild

build: Dockerfile
	@docker build -f Dockerfile -t $(IMAGE):v$(NEXT) .
	@docker image tag $(IMAGE):v$(NEXT) $(IMAGE):latest

rebuild: Dockerfile
	@docker build --no-cache -f Dockerfile -t $(IMAGE):v$(NEXT) .
	@docker image tag $(IMAGE):v$(NEXT) $(IMAGE):latest

default: build
