from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

import sys
import os
import pytest
from mock import patch
from backports.tempfile import TemporaryDirectory
import dotenvy.cli


def test_cli_main():
    with TemporaryDirectory() as d:
        dotenv = os.path.join(d, 'test.env')
        open(dotenv, 'wb').write('hello=world'.encode('utf-8'))

        args = ['prog', '--file=' + dotenv, 'echo $hello']
        with patch.object(sys, 'argv', args):
            result = os.path.join(d, 'result.env')
            dotenvy.cli.main(stdout=open(result, 'w'))

        with open(result, 'r', encoding='utf-8') as f:
            assert f.read().rstrip() == 'world'


def test_cli_main_nonexists():
    args = ['prog', '--file=notexists.env', 'echo $hello']
    with patch.object(sys, 'argv', args):
        with pytest.raises(SystemExit):
            dotenvy.cli.main()
