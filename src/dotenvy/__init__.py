from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

from os import environ
from .parser import parse_string


def load_env(envs):
    for k in envs:
        environ[k] = envs[k]


def load_string(string):
    load_env(parse_string(string))


def read(file):
    return parse_string(file.read())


def read_file(filepath='.env'):
    return read(open(filepath))
