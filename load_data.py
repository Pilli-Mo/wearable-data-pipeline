import sqlite3 
import pandas as pd  #  reads CSV files and converts them to DataFrames

# STep 1: connect to a database file 
conn = sqlite3.connect("wearable_data.db")  # create a database file if it doesn't exist

# Step 2: read the CSV file into a pandas DataFrame
activity_df = pd.read_csv("data/raw/dailyActivity_merged.csv")
activity_df["ActivityDate"] = pd.to_datetime(activity_df["ActivityDate"]).dt.strftime("%Y-%m-%d")  # convert the ActivityDate column to datetime format

sleep_df = pd.read_csv("data/raw/sleepDay_merged.csv")
sleep_df["SleepDay"] = pd.to_datetime(sleep_df["SleepDay"]).dt.strftime("%Y-%m-%d")  # convert the SleepDay column to datetime format

# Step 3: then write the DataFrame into a database table
activity_df.to_sql("dailyActivity", conn, if_exists="replace", index=False)
sleep_df.to_sql("sleepDay", conn, if_exists="replace", index=False)
# Step 4: close the database connection
conn.close()