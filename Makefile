.PHONY: test lint type-check

SRC = yacht.py

test:
	pytest

lint:
	flake8 $(SRC) tests

type-check:
	mypy --ignore-missing-imports --disallow-untyped-defs $(SRC)
