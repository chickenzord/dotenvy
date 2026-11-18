from os import environ, path
from tempfile import TemporaryDirectory

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
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(FILE_CONTENT)

        envs = dotenvy.read_file(filepath)
        assert len(envs) == 5
        assert envs['HELLO'] == 'WORLD'
        assert envs['lorem'] == 'ipsum'
        assert envs['dolor'] == 'sit amet'
        assert envs['blank'] == ''
        assert envs['blank_too'] == ''
