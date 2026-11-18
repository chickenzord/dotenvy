tasks:
	@git grep -EI "TODO|FIXME" | grep -v -E '^Makefile:'

sync:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check
	uv run ruff format --check

format:
	uv run ruff format
	uv run ruff check --fix

build:
	uv build

.PHONY: tasks sync test lint format build
