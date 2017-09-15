tasks:
	@git grep -EI "TODO|FIXME" | grep -v -E '^Makefile:'

test:
	tox

style-fix:
	autopep8 --in-place $$(find . -name '*.py')

compat-fix:
	pasteurize -wn src tests

fix: style-fix compat-fix

.PHONY: tasks test  \
	style-fix compat-fix fix
