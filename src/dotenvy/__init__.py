from os import environ

from .parser import parse_string

__version__ = "1.0.0"


def load_env(envs):
    for k, v in envs.items():
        environ[k] = v


def load_string(string):
    load_env(parse_string(string))


def read(file, *args, schema=None, **kwargs):
    if schema is None:
        schema = {}
    return parse_string(file.read(), *args, schema=schema, **kwargs)


def read_file(filepath, *args, schema=None, **kwargs):
    if schema is None:
        schema = {}
    with open(filepath, encoding="utf-8") as f:
        return read(f, *args, schema=schema, **kwargs)
