from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from dotenvy import parser
from dotenvy import exception
from dotenvy import truthy
import pytest


def test_parser_is_blank():
    # positive cases
    assert parser.is_blank('') is True
    assert parser.is_blank('   ') is True
    assert parser.is_blank('\n') is True

    # negative cases
    assert parser.is_blank('hello=world') is False
    assert parser.is_blank('   hello=world   ') is False
    assert parser.is_blank('\n hello=world') is False


def test_parser_is_comment():
    # positive cases
    assert parser.is_comment('# hello world') is True

    # negative cases
    assert parser.is_comment('hello=world') is False
    assert parser.is_comment('hello # world') is False


def test_parser_is_pair():
    # positive cases
    assert parser.is_pair('hello=world') is True
    assert parser.is_pair('hello="world"') is True
    assert parser.is_pair('hello=\'world\'') is True

    # negative cases
    assert parser.is_pair('hello = world') is False
    assert parser.is_pair('hello= world') is False
    assert parser.is_pair('hello = world') is False


def test_parse_line_without_quotes():
    key, val = parser.parse_line('hello=world')
    assert key == 'hello'
    assert val == 'world'


def test_parse_line_invalid():
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('# hello')
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('not a key-val pair')


def test_parse_line_with_blank_value():
    key, val = parser.parse_line('hello=')
    assert key == 'hello'
    assert val == ''

    key, val = parser.parse_line(' hello= ')
    assert key == 'hello'
    assert val == ''


def test_parse_line_with_double_quotes():
    # normal case
    key, val = parser.parse_line('hello="world"')
    assert key == 'hello'
    assert val == 'world'

    # with surrounding whitespaces
    key, val = parser.parse_line(' hello="world" ')
    assert key == 'hello'
    assert val == 'world'

    # with escaped quotes
    key, val = parser.parse_line('message="hello \\\"world\\\""')
    assert key == 'message'
    assert val == 'hello \"world\"'

    # missing closing quote
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('message="')
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('message="hello')
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('message="hello ')


def test_parse_line_with_single_quotes():
    # normal case
    key, val = parser.parse_line('hello=\'world\'')
    assert key == 'hello'
    assert val == 'world'

    # with surrounding whitespaces
    key, val = parser.parse_line(' hello=\'world\' ')
    assert key == 'hello'
    assert val == 'world'

    # with escaped quotes
    key, val = parser.parse_line('message=\'hello \\\'world\\\'\'')
    assert key == 'message'
    assert val == 'hello \'world\''

    # missing closing quote
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('message=\'')
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('message=\'hello')
    with pytest.raises(exception.ParseException):
        key, val = parser.parse_line('message=\'hello ')


def test_parse_string():
    string = '''
    # just a comment
    HELLO=WORLD
    lorem="ipsum"
    dolor='sit amet'
    '''
    envs = parser.parse_string(string)
    assert len(envs) == 3
    assert envs['HELLO'] == 'WORLD'
    assert envs['lorem'] == 'ipsum'
    assert envs['dolor'] == 'sit amet'

    # TODO add negative cases for `parser.parse_string`


def test_parse_string_with_schema():
    string = '''
    INT=1406
    FLOAT=14.06
    BOOLEAN_TRUE=1
    BOOLEAN_FALSE=0
    '''
    schema = {
        'INT': int,
        'FLOAT': float,
        'BOOLEAN_TRUE': truthy,
        'BOOLEAN_FALSE': truthy,
    }
    envs = parser.parse_string(string, schema=schema)
    assert len(envs) == 4
    assert envs['INT'] == 1406
    assert envs['FLOAT'] == 14.06
    assert envs['BOOLEAN_TRUE'] is True
    assert envs['BOOLEAN_FALSE'] is False
