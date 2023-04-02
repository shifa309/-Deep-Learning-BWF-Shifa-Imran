import pandas as pd
import mysql.connector

# Connect to the SQL database
# create a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="example.sql"
)

# Read data from the "people" table
query = 'SELECT * FROM people'
df = pd.read_sql(query, conn)

# Display the resulting DataFrame
print(df)

conn.close()
