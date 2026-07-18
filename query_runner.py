import sqlite3
import pandas as pd

conn = sqlite3.connect("wearable_data.db")
df= pd.read_sql_query("SELECT strftime('%w', ActivityDate) as day_of_week, ActivityDate, TotalSteps FROM dailyActivity;", conn)    # pd.read_sql_query() sends SQL query to the database and returns the result as a DataFrame
df['day_of_week'] = pd.to_datetime(df['ActivityDate']).dt.day_name()  # convert the day_of_week column to a more readable format

print(df)

conn.close()