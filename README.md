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

* sqlalchemy>=1.4.31
* psycopg2>=2.9.1
* numpy>=1.19.4
* pandas>=1.2

```bash
pip install sqlalchemy psycopg2 numpy pandas
```

## Future plans

Sub-package to allow users to send user-generated data products to LIneA Science Server (e.g., a list of targets for visual inspection).

### Development

Python 3.8: <https://tecadmin.net/install-python-3-8-ubuntu/>

* Dependencias:

```bash
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev liblzma-dev
```

```bash
python3.8 -m venv env
source env/bin/activate
pip install --upgrade pip
```

```bash
pip install wheel setuptools twine pytest pytest-runner
```

Executar os testes:

```bash
python setup.py pytest
```

Fazer o Build: <https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f>

```bash
python setup.py bdist_wheel
```

### Testando o pacote apos o build

```bash
python3.8 -m venv env
source env/bin/activate
```

Para instalar usando o pacote local

```bash
pip install --force-reinstall <path>/dist/wheelfile.whl
```

Abrir um terminal e importar a classe DBBase. ou utilizar o comando.

```bash
python -c 'from dblinea import DBBase'
```

Outro Teste

```bash
(env) glauber: ~ $ python 
Python 3.8.12 (default, Jan 28 2022, 15:50:21) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from dblinea import DBBase
>>> a = DBBase()
>>> a.get_engine()
Engine(postgresql+psycopg2://untrustedprod:***@desdb4.linea.gov.br:5432/prod_gavo)
>>> 

```
