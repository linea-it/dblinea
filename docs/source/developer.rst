Developer documentation
=======================

   .. todo:: Adicionar textos e exemplos para os desenvolvedores

Installation
~~~~~~~~~~~~

Python 3.8 `https://tecadmin.net/install-python-3-8-ubuntu/ <https://tecadmin.net/install-python-3-8-ubuntu/>`__

.. code:: bash

   sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev liblzma-dev

virtual environment

.. code:: bash

   python3.8 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip

.. code:: bash

   pip install wheel setuptools twine pytest pytest-runner pytest-cov black

Executar os testes:

.. code:: bash

   python setup.py pytest --cov --cov-report term-missing --cov-report html

Fazer o Build:
`https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f <https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f>`__

.. code:: bash

   python setup.py sdist bdist_wheel

Testando o pacote apos o build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   python3.8 -m venv venv
   source venv/bin/activate

.. code:: bash

   pip install sqlalchemy psycopg2 numpy pandas

Para instalar usando o pacote local

.. code:: bash

   pip install --force-reinstall <path>/dist/wheelfile.whl

Abrir um terminal e importar a classe DBBase. ou utilizar o comando.

.. code:: bash

   python -c 'from dblinea import DBBase'

Outro Teste

.. code:: bash

   (env) glauber: ~ $ python 
   Python 3.8.12 (default, Jan 28 2022, 15:50:21) 
   [GCC 7.5.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> from dblinea import DBBase
   >>> a = DBBase()
   >>> a.get_engine()
   Engine(postgresql+psycopg2://untrustedprod:***@desdb4.linea.gov.br:5432/prod_gavo)
   >>> 

Publish in PyPi Test
~~~~~~~~~~~~~~~~~~~~

Check if build is ok for publish

.. code:: bash

   python -m twine check dist/*

.. code:: bash

   python -m twine upload --verbose --repository testpypi dist/*

Check in
`https://test.pypi.org/manage/project/dblinea/releases/ <https://test.pypi.org/manage/project/dblinea/releases/>`__

Publish in PyPi Oficial
~~~~~~~~~~~~~~~~~~~~~~~

`https://realpython.com/pypi-publish-python-package/ <https://realpython.com/pypi-publish-python-package/>`__

.. code:: bash

   twine upload dist/*

Executar o Lint em busca de errors de sintaxe ou formatação.

.. code:: bash

   black . --check

Executar o Lint para corrigir automaticamente os errors encontrados.

.. code:: bash

   black .

.. raw:: html

   <!-- ```bash
   flake8 . --count  --max-complexity=10 --max-line-length=127 --statistics
   ``` -->

Documentation with sphinx
~~~~~~~~~~~~~~~~~~~~~~~~~

Generate Api Docs

.. code:: bash

   cd docs
   sphinx-apidoc -f -o ./source ../dblinea

Build html docs

.. code:: bash

   make html



============================================================================================

.. |Python package| image:: https://github.com/linea-it/dblinea/actions/workflows/python-package.yml/badge.svg?branch=main
   :target: https://github.com/linea-it/dblinea/actions/workflows/python-package.yml
