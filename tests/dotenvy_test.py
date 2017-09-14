from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

from tempfile import TemporaryDirectory
from os import path, environ
import dotenvy


FILE_CONTENT = """
        # just a comment
        HELLO=WORLD
        lorem="ipsum"
        dolor='sit amet'
        blank=''
        blank_too=
        """


def test_load_string():
    backup = environ.copy()

    dotenvy.load_string(FILE_CONTENT)
    assert environ.get('HELLO') == 'WORLD'
    assert environ.get('lorem') == 'ipsum'
    assert environ.get('dolor') == 'sit amet'
    assert environ.get('blank') == ''
    assert environ.get('blank_too') == ''

    environ.clear()
    environ.update(backup)


def test_read_file():
    with TemporaryDirectory() as d:
        filepath = path.join(d, 'test.env')
        with open(filepath, 'wb') as f:
            f.write(FILE_CONTENT.encode('utf-8'))

        envs = dotenvy.read_file(f.name)
        assert len(envs) == 5
        assert envs['HELLO'] == 'WORLD'
        assert envs['lorem'] == 'ipsum'
        assert envs['dolor'] == 'sit amet'
        assert envs['blank'] == ''
        assert envs['blank_too'] == ''
