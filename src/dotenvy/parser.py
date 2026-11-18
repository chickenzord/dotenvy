import re
from string import Template

from .exception import ParseException

QUOTES = ['"', "'"]
TRUTHY_VALUES = ["1", "true", "yes", "on"]
FALSY_VALUES = ["0", "false", "no", "off"]


def truth(string):
    lowered = string.lower()
    if lowered in TRUTHY_VALUES:
        return True
    elif lowered in FALSY_VALUES:
        return False
    else:
        raise ValueError("Invalid truth value")


def is_blank(text):
    return text.strip() == ""


def is_comment(line):
    return len(line) > 0 and line[:1] == "#"


def is_pair(line):
    return bool(re.match(r"^[A-Za-z0-9_]+=(\S|$)", line))


def unescape(text):
    return bytes(text, "utf-8").decode("unicode_escape")


def parse_quoted(text):
    if len(text) == 0:
        return ""

    if len(text) == 1 and text in QUOTES:
        raise ParseException("Invalid quoted value")

    first = text[:1]
    last = text[-1:]

    if (len(text) >= 2) and (first in QUOTES):
        if first == last:
            return unescape(text[1:-1])
        else:
            raise ParseException("Unmatching quotes")
    else:
        return text


def parse_line(line):
    line = line.strip()

    if not is_pair(line):
        raise ParseException("Not a valid key-val line")

    key, val = line.split("=", 1)
    return (key, parse_quoted(val))


def parse_string(string, schema=None, expand=False, env=None, merge_env=False):
    if schema is None:
        schema = {}
    if env is None:
        env = {}

    lookup = env.copy()
    result = env.copy() if merge_env else {}
    for line in [line for line in string.splitlines() if is_pair(line.strip())]:
        key, val = parse_line(line)
        if expand:
            result[key] = Template(val.replace(r"\$", "$$")).substitute(lookup)
        else:
            result[key] = val
        lookup[key] = result[key]

    for key, cast in schema.items():
        cast = truth if cast is bool else cast
        if key in result:
            result[key] = cast(result[key])

    return result
