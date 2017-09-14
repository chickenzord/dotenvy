from setuptools import setup, find_packages

setup(
    name="dotenvy",
    version="0.1.0",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    package_data={},

    # metadata for upload to PyPI
    author="Akhyar Amarullah",
    author_email="akhyrul@gmail.com",
    description="dotenv handler for python",
    license="MIT",
    keywords="dotenv",
    url="https://projects.chickenzord.com/dotenvy",
)
