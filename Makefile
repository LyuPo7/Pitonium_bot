install:
	poetry install

test:
	poetry run pytest -vv --ff --cov=page_loader --cov-report xml tests/*

lint:
	poetry run flake8 page_loader --show-source --verbose

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

publish:
	poetry publish --repository PyPiTest

run:
	poetry run python3 -m page_loader.scripts.page_loader --output=/var/tmp https://pythonjobs.github.io

.PHONY: install test lint selfcheck check build
