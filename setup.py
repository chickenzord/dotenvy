#!/usr/bin/env python

from setuptools import setup, find_packages


REPO_NAME = 'chickenzord/dotenvy'
VERSION = '0.2.0'
ARCHIVE_URL = 'https://github.com/%s/archive/v%s.tar.gz' % (REPO_NAME, VERSION)

setup(
    # packaging
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={},
    install_requires=[
        'future',
    ],
    setup_requires=[
        'pytest-runner',
        'flake8',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'mock',
        'backports.tempfile',
    ],
    entry_points={
        "console_scripts": ['dotenvy = dotenvy.cli:main']
    },
    zip_safe=False,

    # metadata
    name='dotenvy',
    version=VERSION,
    author='Akhyar Amarullah',
    author_email='akhyrul@gmail.com',
    description='Dotenv handler for Python',
    long_description=open('README.rst').read(),
    download_url=ARCHIVE_URL,
    license='MIT',
    keywords=['dotenv', 'configuration', 'environment'],
    url='https://github.com/%s' % (REPO_NAME),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
