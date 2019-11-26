RELEASE_VERSION=$(shell cat src/resolvref/version.py | grep '^__version__' | cut -d '"' -f2)

tox:
	@if ! which tox; then echo 'you must install tox!'; exit 1; fi

.PHONY: test
test: tox
	tox -p auto

.PHONY: lint
lint: tox
	tox -e lint

.PHONY: docs
docs: tox
	tox -e docs

.PHONY: release
release: tox
	RELEASE_VERSION=$(RELEASE_VERSION) tox -e release

.PHONY: clean
clean:
	rm -rf dist build src/*.egg-info .tox
