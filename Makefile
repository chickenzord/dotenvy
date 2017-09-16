tasks:
	@git grep -EI "TODO|FIXME" | grep -v -E '^Makefile:'

test:
	./setup.py test

test-all:
	tox

.PHONY: tasks test test-all
