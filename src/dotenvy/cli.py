#!/usr/bin/env python
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import str
from future import standard_library
standard_library.install_aliases()

import argparse
import subprocess
import sys

import dotenvy


def main(stdout=sys.stdout):
    description = '''
        Run any shell command with environment variables loaded from DotEnv file
        '''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--file', type=str, default='.env',
                        help='dotenv file path (default: .env)')
    parser.add_argument('commands', type=str, nargs='+',
                        help='command to run')
    args = parser.parse_args()

    try:
        env = dotenvy.read_file(args.file)
    except IOError as e:
        sys.exit('Cannot load dotenv: %s\n%s' % (args.file, str(e)))

    subprocess.call(' '.join(args.commands),
                    env=env, shell=True, stdout=stdout)


if __name__ == '__main__':  # pragma: no cover
    main()
