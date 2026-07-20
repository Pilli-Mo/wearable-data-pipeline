import sqlite3
import pandas as pd

conn = sqlite3.connect("wearable_data.db")

query = """
        Select Id, count(*) as days_tracked
        From dailyActivity
        Group by Id
        Having count(*) < 25;
"""
df = pd.read_sql_query(query, conn)

# correlation = df["TotalSteps"].corr(df["TotalMinutesAsleep"])

# print("Correlation between Total Steps and Total Minutes Asleep: ", correlation)
print(df)
conn.close()