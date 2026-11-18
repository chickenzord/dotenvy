dotenvy
=======

.. image:: https://img.shields.io/github/actions/workflow/status/chickenzord/dotenvy/ci.yml?branch=master&style=flat-square
    :target: https://github.com/chickenzord/dotenvy/actions/workflows/ci.yml
    :alt: Build status

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://raw.githubusercontent.com/chickenzord/dotenvy/master/LICENSE.txt
    :alt: MIT license

.. image:: https://img.shields.io/pypi/v/dotenvy.svg?style=flat-square
    :target: https://pypi.org/project/dotenvy/
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/dotenvy.svg?style=flat-square
    :target: https://pypi.org/project/dotenvy/
    :alt: PyPI python version


Dotenv handler for Python


Usages
------

Installing ::

  uv add dotenvy
  # or: pip install dotenvy

Common usage as library ::

  from os import environ
  from dotenvy import load_env, read_file

  load_env(read_file('.env'))
  my_var = environ.get('MY_VAR')

Loading dotenv file to a dict with type casting ::

  from dotenvy import read_file

  config = read_file('.env', schema={
      'HOSTNAME': str,
      'PORT': int,
      'IS_DEBUG': bool,  # either [1/true/on/yes] or [0/false/off/no]
  })

Using it as a CLI tool ::

  # run directly via uvx
  uvx dotenvy ./mywebapp run

  # using alternate dotenv file
  uvx dotenvy --file=prod.env ./mywebapp run


Development
-----------

Install dependencies ::

  uv sync

Running tests ::

  uv run pytest

Checking code style and linting ::

  uv run ruff check
  uv run ruff format --check
