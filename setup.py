from setuptools import setup, find_packages

GITHUB_REPO = 'chickenzord/dotenvy'
VERSION = '0.1.0'
ARCHIVE_URL = 'https://github.com/%s/archive/%s.tar.gz' % (GITHUB_REPO, VERSION)

setup(
    name='dotenvy',
    version=VERSION,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'future',
    ],
    package_data={},

    # metadata
    author='Akhyar Amarullah',
    author_email='akhyrul@gmail.com',
    description='dotenv handler for python',
    long_description=open('README.rst').read(),
    download_url=ARCHIVE_URL,
    license='MIT',
    keywords=['dotenv', 'configuration', 'environment'],
    url='https://github.com/%s' % (GITHUB_REPO),
)
