import sqlite3
import csv

# File paths
csv_file_path = 'data.csv'
sqlite_db_path = 'data/sqlite_db/transactions.db'

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect(sqlite_db_path)
cursor = conn.cursor()

# Create a table in the database (you may need to adjust the schema to match your CSV)
cursor.execute('''
CREATE TABLE IF NOT EXISTS purchases (
    user_id TEXT,
    referrer TEXT,
    revenue REAL,
    date TEXT,
    platform TEXT,
    store_id TEXT
)
''')


with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO purchases (user_id, referrer, revenue, date, platform, store_id)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', row)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("CSV data has been imported into the SQLite database successfully.")
