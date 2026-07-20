import sqlite3
import pandas as pd

conn = sqlite3.connect("wearable_data.db")

query = """
        SELECT dailyActivity.Id, TotalSteps, TotalMinutesAsleep
        FROM dailyActivity
        JOIN sleepDay ON dailyActivity.Id = sleepDay.Id
                AND dailyActivity.ActivityDate = sleepDay.SleepDay;
"""
df = pd.read_sql_query(query, conn)

correlation = df["TotalSteps"].corr(df["TotalMinutesAsleep"])

print("Correlation between Total Steps and Total Minutes Asleep: ", correlation)
conn.close()