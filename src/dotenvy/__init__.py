from os import environ
from .parser import parse_string


__version__ = '0.2.0'


def load_env(envs):
    for k, v in envs.items():
        environ[k] = v


def load_string(string):
    load_env(parse_string(string))


def read(file, schema=None, *args, **kwargs):
    if schema is None:
        schema = {}
    return parse_string(file.read(), schema=schema, *args, **kwargs)


def read_file(filepath, schema=None, *args, **kwargs):
    if schema is None:
        schema = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return read(f, schema=schema, *args, **kwargs)
