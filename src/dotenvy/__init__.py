from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

from os import environ
from .parser import parse_string
from .parser import truth  # noqa


__version__ = '0.2.0'


def load_env(envs):
    for k in envs:
        environ[k] = envs[k]


def load_string(string):
    load_env(parse_string(string))


def read(file, schema={}, *args, **kwargs):
    return parse_string(file.read(), *args, **kwargs)


def read_file(filepath, schema={}, *args, **kwargs):
    return read(open(filepath), *args, **kwargs)
