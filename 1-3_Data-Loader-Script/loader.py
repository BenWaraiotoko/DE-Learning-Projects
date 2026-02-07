import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# Read data from CSV file
def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
        # Clean csv data (if necessary)
def clean_data(df):
    # Example: Remove rows with missing values
    df = df.dropna()
    # Convert column names to lowercase and strip whitespace from 'name' column
    df.columns = df.columns.str.lower()
    # Strip whitespace from 'name' and 'email' columns
    df['name'] = df['name'].str.strip()
    df['email'] = df['email'].str.strip()
    # Replace missing values in 'age' with 0
    df['age'] = df['age'].fillna(0)
    return df

# Insert data into PostgreSQL database
def insert_data(df):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db",
            port="5432"
        )
        cursor = conn.cursor()
        # Insert data into the database
        for index, row in df.iterrows():
            cursor.execute(
                "INSERT INTO users (name, email, age, city) VALUES (%s, %s, %s, %s)",
                (row['name'], row['email'], row['age'], row['city'])
            )
        #Execute a simple query to verify data insertion
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)
        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Main function
def main():
    # Read data from CSV file
    df = read_csv('sample_data.csv')
    if df is not None:
        # Clean data
        df = clean_data(df)
        # Insert data into PostgreSQL database
        insert_data(df)

if __name__ == "__main__":
    main()