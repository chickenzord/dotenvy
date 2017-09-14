tasks:
	@git grep -EI "TODO|FIXME" | grep -v -E '^Makefile:'

test-deps:
	pip install pytest pytest-cov pep8 backports.tempfile

test:
	pytest

style-check:
	pep8 .
	@echo 'OK'

style-fix:
	autopep8 --in-place $$(find . -name '*.py')

compat-fix:
	pasteurize -wn src tests

fix: style-fix compat-fix

.PHONY: tasks \
	test test-deps \
	style-check style-fix \
	compat-fix \
	fix
