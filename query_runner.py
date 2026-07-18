import sqlite3
import pandas as pd

conn = sqlite3.connect("wearable_data.db")
df= pd.read_sql_query("SELECT ActivityDate, TotalSteps FROM dailyActivity;", conn)    # pd.read_sql_query() sends SQL query to the database and returns the result as a DataFrame
df['day_of_week'] = pd.to_datetime(df['ActivityDate']).dt.day_name()  # convert the day_of_week column to a more readable format

result =df.groupby('day_of_week')['TotalSteps'].mean().reset_index().sort_values(by="TotalSteps", ascending=False)  # group by day_of_week and calculate the average TotalSteps for each day, then sort the result in descending order

print(result)

conn.close()