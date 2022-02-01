import unittest
from dblinea import DBBase
from sqlalchemy.engine.cursor import LegacyCursorResult
from sqlalchemy.sql.elements import TextClause
from sqlalchemy.types import INTEGER, VARCHAR
from pandas.testing import assert_frame_equal
import pandas as pd
import os


class TestAbilityToTest(unittest.TestCase):
    def test_ability_to_test(self):
        # Apenas verifica se é possivel executar os testes.
        self.assertEqual(1, 1)


class TestDaoPostgres(unittest.TestCase):
    def setUp(self):

        self.dbhost = os.environ.get("POSTGRES_HOST", "localhost")
        self.dbport = os.environ.get("POSTGRES_PORT", "5432")
        self.dbuser = os.environ.get("POSTGRES_USER", "postgres")
        self.dbpass = os.environ.get("POSTGRES_PASSWORD", "postgres")
        self.dbname = "db_test"

        self.schema = "sch_test"
        self.table = "tb_sample"

        self.dao = DBBase(
            dbhost=self.dbhost,
            dbport=self.dbport,
            dbuser=self.dbuser,
            dbpass=self.dbpass,
            dbname=self.dbname,
        )

        self.select_sql = "Select * from {}.{}".format(self.schema, self.table)

    def test_get_db_uri(self):
        uri = (
            "postgresql+psycopg2://%(username)s:%(password)s@%(host)s:%(port)s/%(database)s"
        ) % {
            "username": self.dbuser,
            "password": self.dbpass,
            "host": self.dbhost,
            "port": self.dbport,
            "database": self.dbname,
        }

        self.assertEqual(self.dao.database.get_db_uri(), uri)

    def test_execute(self):

        sql = "insert into {schema}.{table} values (1, 'jose', 30)".format(
            schema=self.schema, table=self.table
        )

        result = self.dao.execute(sql)

        # Verifica se o resultado é uma instancia de CursorResult
        self.assertTrue(isinstance(result, LegacyCursorResult))

        # Quantidade de linhas inseridas
        self.assertEqual(result.rowcount, 1)

    def test_fetchall(self):

        row = [(1, "jose", 30)]

        self.assertEqual(self.dao.fetchall(self.select_sql), row)

    def test_fetchall_dict(self):

        row = [{"id": 1, "name": "jose", "age": 30}]
        sql = "Select * from {}.{}".format(self.schema, self.table)

        self.assertEqual(self.dao.fetchall_dict(sql), row)

    def test_fetchall_df(self):

        row = [{"id": 1, "name": "jose", "age": 30}]

        self.assertEqual(self.dao.fetchall_dict(self.select_sql), row)

    def test_fetchall_df(self):

        df = pd.DataFrame([{"id": 1, "name": "jose", "age": 30}])

        assert_frame_equal(self.dao.fetchall_df(self.select_sql), df)

    def test_fetchone(self):

        row = (1, "jose", 30)

        self.assertEqual(self.dao.fetchone(self.select_sql), row)

    def test_fetchone_dict(self):

        row = {"id": 1, "name": "jose", "age": 30}

        self.assertEqual(self.dao.fetchone_dict(self.select_sql), row)

    def test_fetc_scalar(self):

        self.assertEqual(self.dao.fetch_scalar(self.select_sql), 1)

    def test_to_dict(self):

        row = {"id": 1, "name": "jose", "age": 30}

        line = self.dao.fetchone(self.select_sql)

        self.assertEqual(self.dao.to_dict(line), row)

    def test_raw_sql_to_stm(self):

        row = {"id": 1, "name": "jose", "age": 30}

        stm = self.dao.raw_sql_to_stm(self.select_sql)

        self.assertTrue(isinstance(stm, TextClause))

        # Double Check
        self.assertEqual(self.select_sql, str(stm))

    def test_get_table_columns(self):

        columns = ["id", "name", "age"]

        self.assertEqual(self.dao.get_table_columns(self.table, self.schema), columns)

    def test_describe_table(self):

        columns = [
            {"name": "id", "type": INTEGER()},
            {"name": "name", "type": VARCHAR(length=100)},
            {"name": "age", "type": INTEGER()},
        ]

        # OBS: A comparação só ficou igual quando convertido para String.
        self.assertEqual(
            str(self.dao.describe_table(self.table, self.schema)), str(columns)
        )


if __name__ == "__main__":
    unittest.main()
