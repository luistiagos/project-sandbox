import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create the Products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        ID INTEGER,
        TITLE TEXT,
        DELIVERLINK TEXT,
        PRICE REAL,
        PURCHASELINK TEXT
    )
''')

# Read the CSV file and execute the INSERT statements
with open('your_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Extract values from the CSV row
        ID = int(row[0])
        TITLE = row[1]
        DELIVERLINK = row[2]
        PRICE = float(row[3])
        PURCHASELINK = row[4]

        # Execute the INSERT statement
        cursor.execute('''
            INSERT INTO Products (ID, TITLE, DELIVERLINK, PRICE, PURCHASELINK)
            VALUES (?, ?, ?, ?, ?)
        ''', (ID, TITLE, DELIVERLINK, PRICE, PURCHASELINK))

# Commit the changes and close the connection
conn.commit()
conn.close()
