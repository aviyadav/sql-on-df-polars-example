import polars as pl
from sqlalchemy import create_engine

# engine = create_engine("postgresql://postgres:password@localhost:5432/pocdb")
engine = create_engine("postgresql://devuser:password@localhost:5432/devdb")
conn = engine.connect()
query = "SELECT * FROM books"

df = pl.read_database(query=query, connection=conn)
print(df)

query_1 = """
    SELECT
        id,
        isbn,
        publisher,
        author
    FROM
        books,
        JSON_TABLE (data, '$' COLUMNS (
            publisher text PATH '$.publisher',
            isbn text PATH '$.isbn',
            author text PATH '$.author'
        )) AS jt;
"""

df_1 = pl.read_database(query=query_1, connection=conn)
print(df_1)


query_2 = """
    SELECT jt.*
    FROM products,
     JSON_TABLE(
         data,
         '$' 
         COLUMNS (
             brand text PATH '$.brand',
             model text PATH '$.model',
             release_year integer PATH '$.release_year',
             specifications jsonb PATH '$.specifications',
             features jsonb PATH '$.features',
             warranty text PATH '$.warranty',
             price numeric PATH '$.price'
         )
     ) AS jt;
"""

df2 = pl.read_database(query=query_2, connection=conn)
print(df2)