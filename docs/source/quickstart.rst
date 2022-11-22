Quickstart
==========

Installation
------------

  
   For security reasons, the library usage is restricted to `LIneA's JupyterJub <https://jupyter.linea.org.br>`_ environment and does not require any installation by the users. 



Import dblinea
------------

The Python library `dblinea` can be simply imported as a regular Python library.

   .. code:: python
      
      import dblinea

The connection with the database is done by the class `DBBase`.
An example of usage is to create an instance of `DBBase` to make queries to the database.
   
   .. code:: python
      
      from dblinea import DBBase
      db = DBBase()
      db.describe_table("coadd_objects", schema = "des_dr2")



Tutorial
------------

The best way to learn more about `dblinea` is by the tutorial notebook *2-acesso-a-dados.ipynb* available on the GitHub repository `jupyterhub-tutorial <https://github.com/linea-it/jupyterhub-tutorial>`_. To access the notebook, once you are logged in on LIneA JupyterHub, please clone the tutorials repository. 

On Jupyter Lab's Terminal, run:

   .. code:: shell

      $ git clone https://github.com/linea-it/jupyterhub-tutorial.git 




