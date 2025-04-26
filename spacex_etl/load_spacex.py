import psycopg2
import pandas as pd
import os


# Load the cleaned data
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "data", "spacex_launches_cleaned.csv")
df = pd.read_csv(data_path)

# Database connection parameters
conn = psycopg2.connect(
    dbname="data_portfolio",
    user="etl_user",          # or "postgres" if you didn't make a new user
    password="ETL_password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Create the table if it doesn't exist

cur.execute("""
    CREATE TABLE IF NOT EXISTS spacex_launches (
        id SERIAL PRIMARY KEY,
        name TEXT,
        date_utc TIMESTAMP,
        success BOOLEAN,
        details TEXT,
        rocket TEXT
    );
""")

# Insert rows into the table
for _, row in df.iterrows():

    success = row["success"]
    if pd.isna(success):
        success = None
    else:
        success = bool(success)  # cast 1.0/0.0 to True/False

    cur.execute("""
        INSERT INTO spacex_launches (name, date_utc, success, details, rocket)
        VALUES (%s, %s, %s, %s, %s);
    """, (
        row['name'], 
        row['date_utc'], 
        success, 
        row['details'], 
        row['rocket']
    ))

# Commit and close the connection

conn.commit()
cur.close()
conn.close()

print("Data loaded into PostgreSQL database successfully.")