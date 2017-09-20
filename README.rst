dotenvy
=======

.. image:: https://img.shields.io/travis/chickenzord/dotenvy.svg?style=flat-square
    :target: https://travis-ci.org/chickenzord/dotenvy
    :alt: Build status

.. image:: https://img.shields.io/coveralls/chickenzord/dotenvy.svg?style=flat-square
    :target: https://coveralls.io/github/chickenzord/dotenvy
    :alt: Coverage status

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://raw.githubusercontent.com/chickenzord/dotenvy/master/LICENSE.txt
    :alt: MIT license

.. image:: https://img.shields.io/pypi/v/dotenvy.svg?style=flat-square
    :target: https://pypi.python.org/pypi/dotenvy
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/dotenvy.svg?style=flat-square
    :target: https://pypi.python.org/pypi/dotenvy
    :alt: PyPI python version


Dotenv handler for Python


usages
------

Installing ::

  pip install dotenvy

Common usage as library ::

  from dotenvy import load_env, read_file
  from os import environ

  load_env(read_file('.env'))
  my_var = environ.get('MY_VAR')

Loading dotenv file to a dict with type casting ::

  from dotenvy import read_file, truthy

  config = read_file('.env', schema={
    'HOSTNAME': str,
    'PORT': int,
    'IS_DEBUG': bool,  # either [1/true/on/yes] or [0/false/off/no]
  })

Using it as a CLI tool ::

  # default dotenv file is '.env'
  dotenvy ./mywebapp run

  # using alternate dotenv file
  dotenvy --file=prod.env ./mywebapp run


development
-----------

Checking codestyle ::

  ./setup.py stylecheck

Running tests ::

  ./setup.py test

Running tests on all supported python versions ::

  pip install tox
  tox
