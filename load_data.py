import sqlite3 
import pandas as pd  #  reads CSV files and converts them to DataFrames

# STep 1: connect to a database file 
conn = sqlite3.connect("wearable_data.db")  # create a database file if it doesn't exist

# Step 2: read the CSV file into a pandas DataFrame
activity_df = pd.read_csv("data/raw/dailyActivity_merged.csv")
sleep_df = pd.read_csv("data/raw/sleepDay_merged.csv")

# Step 3: then write the DataFrame into a database table
activity_df.to_sql("dailyActivity", conn, if_exists="replace", index=False)
sleep_df.to_sql("sleepDay", conn, if_exists="replace", index=False)
# Step 4: close the database connection
conn.close()