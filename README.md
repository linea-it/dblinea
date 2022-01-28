# linea-db

Python library to access LIneA's database from Python code. 
Useful to retrieve data inside LIneA's JupyterHub platform. 

## Authors

* [@glaubervila](https://github.com/glaubervila)
* [@gschwend](https://www.github.com/gschwend)

## Installation

Install **linea-db** with pip

```bash
  pip install linea-db
```

## Requirements

* pandas
* sqlalchemy 

## Future plans 

Sub-package to allow users to send user-generated data products to LIneA Science Server (e.g., a list of targets for visual inspection). 

### Requirements

Python 3.8: <https://tecadmin.net/install-python-3-8-ubuntu/>

* Dependencias:

```bash
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev     libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
```

```bash
python3.8 -m venv env
pip install --upgrade pip
```

```bash
pip install wheel setuptools twine pytest pytest-runner
```

Executar os testes:

```bash
python setup.py pytest
```

Fazer o Build: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

```bash
python setup.py bdist_wheel
```
