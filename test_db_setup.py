import os

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

dbhost = os.environ.get("POSTGRES_HOST", "localhost")
dbport = os.environ.get("POSTGRES_PORT", "5432")
dbuser = os.environ.get("POSTGRES_USER", "postgres")
dbpass = os.environ.get("POSTGRES_PASSWORD", "postgres")

con = psycopg2.connect(
    host="localhost", user="postgres", password="postgres", port=5432
)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

db_name = "db_test"
schema = "sch_test"
table = "tb_sample"

with con.cursor() as cursor:
    # Create a database
    cursor.execute("DROP DATABASE IF EXISTS {}".format(db_name))
    cursor.execute("create database {};".format(db_name))
    cursor.close()


con = psycopg2.connect(
    host="localhost", user="postgres", password="postgres", port=5432, database=db_name
)

with con.cursor() as cursor:
    # Create Schema
    cursor.execute("DROP SCHEMA IF EXISTS {} CASCADE".format(schema))
    cursor.execute("CREATE SCHEMA {};".format(schema))

    # Create sample Table
    cursor.execute(
        "DROP TABLE IF EXISTS {schema}.{table}".format(schema=schema, table=table)
    )
    cursor.execute(
        "create table {schema}.{table} (id serial primary key, name varchar(100), age int)".format(
            schema=schema, table=table
        )
    )
    cursor.close()
    con.commit()

# from dblinea import DBBase
# a = DBBase(dbhost="localhost", dbuser="postgres", dbpass="postgres", dbname="db_test")
# db_name = "db_test"
# schema = "sch_test"
# table = "tb_sample"
# sql = "Select * from {}.{}".format(schema, table)
# print(type(a.raw_sql_to_stm(sql)))
