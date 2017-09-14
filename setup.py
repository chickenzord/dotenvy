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
    zip_safe=False,

    # metadata
    author='Akhyar Amarullah',
    author_email='akhyrul@gmail.com',
    description='Dotenv handler for Python',
    long_description=open('README.rst').read(),
    download_url=ARCHIVE_URL,
    license='MIT',
    keywords=['dotenv', 'configuration', 'environment'],
    url='https://github.com/%s' % (GITHUB_REPO),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ],
)
