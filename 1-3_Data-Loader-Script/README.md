# Project 1-3: Data Loader Script

## Project Objective
The objective of this project is to create a Python script that can be used to load data from a CSV file into a database table. The script should be able to handle different types of data, including integers, floats, and strings, and should be able to handle missing values in the data.

---
## Project Structure

```
project-1-3/
├── loader.py                 # Main script
├── Dockerfile                # To run loader.py
├── docker-compose.yml        # Reusable from 1.2, adapted
├── requirements.txt          # Python dependencies
├── sample_data.csv           # CSV file with sample data
├── README.md                 # This file
|── .env                    # Environment variables (not in repo)
└── init.sql                  # Database schema if needed
```

---

## Prerequisites


- Python 3.11
- Docker
- Docker Compose

---

## How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run `docker-compose up -d` to start the database
4. Run `docker-compose exec app python loader.py` to run the script

---

## Environment Variables

The following environment variables are used:

| Variable | Description | Example |
|----------|-------------|---------|
| `POSTGRES_DB` | Database name | `dev_db` |
| `POSTGRES_USER` | Database user | `dev_user` |
| `POSTGRES_PASSWORD` | User password | `mysecretpassword` |

These are loaded from the `.env` file at runtime.

---

## Key Concepts Learned


- Data loading from CSV to database
- Handling different data types
- Handling missing values
- Using Docker for development
- Using environment variables for configuration

---

## Resources


- [Python CSV Module](https://docs.python.org/3/library/csv.html)
- [Python psycopg2 Module](https://www.psycopg.org/docs/)
- [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL Docker Image](https://hub.docker.com/_/postgres)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)
- [Pandas](https://pandas.pydata.org/)
- [psycopg2](https://www.psycopg.org/)