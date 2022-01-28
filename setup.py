from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="linea-db",
    packages=find_packages(include=['linea-db']),
    version="0.1.0",
    description="Python library to access LIneA's database from Python code. Useful to retrieve data inside LIneA's JupyterHub platform.",
    author="Glauber Costa Vila Verde",
    license="MIT",
    python_requires='>=3.8',
    setup_requires=[
        "pytest-runner",
        "numpy"
    ],
    install_requires=[
        "sqlalchemy",
        "psycopg2-binary",
        "numpy",
        "pandas",
    ],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",

    # Long description of your library
    long_description=long_description,
    long_description_content_type='text/markdown',

    # Either the link to your github or to your website
    url='https://github.com/linea-it/linea-db',
    # # Link from which the project can be downloaded
    # download_url='',

)
