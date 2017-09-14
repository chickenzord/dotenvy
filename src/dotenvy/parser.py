from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import bytes
from future import standard_library
standard_library.install_aliases()

from sys import version_info
from .exception import ParseException
import re


QUOTES = ['"', '\'']


def truthy(string):
    return string.lower() in ['1', 'true', 'yes', 'on']


def is_blank(text):
    return text.strip() == ''


def is_comment(line):
    return len(line) > 0 and line[:1] == '#'


def is_pair(line):
    return bool(re.match(r'^[A-Za-z0-9_]+=(\S|$)', line))


def unescape(text):
    if version_info.major <= 2:
        return text.decode('string_escape')
    else:
        return bytes(text, 'utf-8').decode('unicode_escape')


def parse_quoted(text):
    if len(text) == 0:
        return ''

    if len(text) == 1 and text in QUOTES:
        raise ParseException('Invalid quoted value')

    first = text[:1]
    last = text[-1:]

    if (len(text) >= 2) and (first in QUOTES):
        if first == last:
            return unescape(text[1:-1])
        else:
            raise ParseException('Unmatching quotes')
    else:
        return text


def parse_line(line):
    line = line.strip()

    if not is_pair(line):
        raise ParseException('Not a valid key-val line')

    key, val = line.split('=', 1)
    return (key, parse_quoted(val))


def parse_string(string, schema={}, *args, **kwargs):
    pairs = [parse_line(line)
             for line in string.splitlines() if is_pair(line.strip())]
    envs = {key: val for key, val in pairs}

    for key in schema:
        cast = schema[key]
        if key in envs:
            envs[key] = cast(envs[key])

    return envs
