tasks:
	@git grep -EI "TODO|FIXME" | grep -v -E '^Makefile:'

test:
	pytest -v --cov=dotenvy --cov-report=term-missing

style-check:
	pep8 -v .
	@echo 'OK'

style-fix:
	autopep8 -v --in-place $$(find . -name '*.py')

compat-fix:
	pasteurize -wn src tests

fix: style-fix compat-fix

.PHONY: tasks test style-check style-fix compat-fix fix
