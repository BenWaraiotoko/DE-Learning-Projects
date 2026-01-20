# Simple script to queries the PostgreSQL database
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def query_database():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Execute a simple query
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

        # Close the connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error connecting to database: {e}")

# Run the query when the script is executed
if __name__ == "__main__":
    query_database()
    