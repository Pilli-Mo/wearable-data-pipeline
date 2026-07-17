import sqlite3
import pandas as pd

conn = sqlite3.connect("wearable_data.db")
df= pd.read_sql_query("Select * from dailyActivity", conn)    # pd.read_sql_query() sends SQL query to the database and returns the result as a DataFrame

print(df)

conn.close()