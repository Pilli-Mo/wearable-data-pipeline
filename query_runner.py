import sqlite3
import pandas as pd

conn = sqlite3.connect("wearable_data.db")

query = """
        SELECT dailyActivity.Id, TotalSteps, avg_heartrate
        From dailyActivity
        JOIN (
            Select id, strftime('%Y-%m-%d', Time) as day, AVG(value) as avg_heartrate
            from heartrate
            Group by Id,day
        ) AS dailyHR
        ON dailyActivity.Id = dailyHR.Id
            AND dailyActivity.ActivityDate = dailyHR.day;
"""
df = pd.read_sql_query(query, conn)

# correlation = df["TotalSteps"].corr(df["TotalMinutesAsleep"])

# print("Correlation between Total Steps and Total Minutes Asleep: ", correlation)
print(df)
conn.close()