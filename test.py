from dblinea import DBBase
from dblinea import Table

db = DBBase(
    dbhost="172.20.0.2", dbuser="postgres", dbpass="postgres", dbname="postgres"
)
schema = "des_dr2"
table = "coadd_objects"

# sql = "Select * from {}.{}".format(schema, table)
# print(db.fetchall_dict(sql))

tb = Table(db, table, schema, debug=True)
# Table Query filtro
c = tb.columns
rows = tb.query(
    columns=[c.coadd_object_id, c.mag_auto_g],
    # where=[c.mag_auto_g > 20, c.mag_auto_g < 22],
    # where=[c.mag_auto_g.between(20, 22)],
    where=[c.mag_auto_g.between(25, 26), tb.cone_search_stm(359.304227, -0.69393, 0.5)],
    order_by=-c.ra,
    limit=10,
    # offset=100,
)
print(rows)
# print(rows.to_dict())

# #  Queryset to Pandas Dataframe
# rows = tb.head()
# df = rows.to_pandas()
# print(type(df))
# print(df.head())

# # Queryset to AstropyTable
# rows = tb.head()
# tbl = rows.to_astropy_table()
# print(type(tbl))
# tbl.pprint()


# VOTable https://docs.astropy.org/en/stable/io/votable/index.html
# from astropy.table import Table
# Table.write.help("votable")
# Table.write.help("fits")
