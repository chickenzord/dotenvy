from setuptools import setup, find_packages


REPO_NAME = 'chickenzord/dotenvy'
VERSION = '0.1.2'
ARCHIVE_URL = 'https://github.com/%s/archive/v%s.tar.gz' % (REPO_NAME, VERSION)

setup(
    name='dotenvy',
    version=VERSION,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={},
    install_requires=[
        'future',
    ],
    zip_safe=False,

    # metadata
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
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
