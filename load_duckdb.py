import duckdb

import numpy

import pandas



# Connect to an in-memory DuckDB (or use 'database.db' for a persistent DB)

con = duckdb.connect()



file_path = "base_carbone_files/base_carbone.csv"



# Create a table and load CSV

con.execute(f"CREATE TABLE my_table AS SELECT * FROM read_csv_auto('base_carbone_files/base_carbone.csv', IGNORE_ERRORS=TRUE) ")



# Fetch data as Pandas DataFrame

df = con.execute("SELECT * FROM my_table limit 10").fetchdf()



print(df.head()) # Display first few rows

