Quickstart
==========

The Python library `dblinea` is available on the default environment of [LIneA JupyterJub](https://jupyter.linea.org.br) and can be simply imported as a regular Python library:

   .. code:: python
      
      import dblinea

The connection with the database is done by the class _DBBase_.
An example of usage is to create an instance of _DBBase_ to make queries to the database.
   
   .. code:: python
      
      from dblinea import DBBase
      db = DBBase()
      db.describe_table("coadd_objects", schema = "des_dr2")


Installation
------------

   For security reasons, the library is restricted to be used inside LIneA's JupyterHub environment and does not require any installation for regular users. 





