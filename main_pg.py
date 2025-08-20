import polars as pl
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:password@localhost:5432/pocdb")
conn = engine.connect()
query = "SELECT * FROM album"

df = pl.read_database(query=query, connection=conn)
print(df)

df2 = pl.read_database("select * from band", connection=conn)
print(df2)