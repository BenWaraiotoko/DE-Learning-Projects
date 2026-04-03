# Project 1-2: PostgreSQL in Docker

## Project Objective
Create a **Docker container that runs PostgreSQL**, initialize a simple database, and make SQL queries from your local machine.

This project covers:

- How to orchestrate services (DB + Python)
- Docker volumes (data persistence)
- Environment variables and Docker configuration
- Introduction to PostgreSQL (no SQL expertise required)

---
## Project Structure

```
project-1-2/
├── Dockerfile              # PostgreSQL container configuration
├── init.sql                # Database initialization script
├── docker-compose.yml      # Service orchestration
├── queries.py              # Python script to query the database
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
└── README.md               # This file
```

---

## Prerequisites

- Docker installed and running
- Docker Compose installed
- Python 3.8+ (for the optional Python script)
- PostgreSQL client (psql) for testing

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone 
cd project-1-2
```

### 2. Create the environment file

Create a `.env` file in the project root with the following variables:

```bash
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_USER=dev_user
POSTGRES_DB=dev_db
```

**Important:** Add `.env` to your `.gitignore` to keep credentials secure.

### 3. Build and run with Docker Compose

```bash
# Build and start the container
docker-compose up -d

# Check that the container is running
docker ps
```

### 4. Verify PostgreSQL is running

```bash
# Check container logs
docker logs 1-2_postgresql-in-docker-db-1

# You should see: "database system is ready to accept connections"
```

---

## Database Initialization

The `init.sql` script automatically:

1. Creates a `users` table with the following schema:
   - `id` (SERIAL PRIMARY KEY)
   - `name` (VARCHAR 100, NOT NULL)
   - `email` (VARCHAR 255, UNIQUE, NOT NULL)
   - `created_at` (TIMESTAMP, DEFAULT NOW)
2. Inserts 5 sample users

**Note:** The `dev_db` database is automatically created by Docker via the `POSTGRES_DB` environment variable in `.env`.

---

## Testing the Database

### Method 1: Using psql from the container

```bash
# Connect to the database inside the container
docker exec -it 1-2_postgresql-in-docker-db-1 psql -U dev_user -d dev_db

# Once connected, run SQL queries:
SELECT * FROM users;

# List all tables
\dt

# Exit psql
\q
```

### Method 2: Using psql from your local machine

If you have PostgreSQL client installed locally:

```bash
psql -h localhost -p 5432 -U dev_user -d dev_db
# Enter password: mysecretpassword
```

### Method 3: Using the Python script

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run the query script
python3 queries.py
```

Expected output:
```
(1, 'Benjamin Dubois', 'benjamin@example.com', datetime.datetime(...))
(2, 'Marie Martin', 'marie.martin@example.com', datetime.datetime(...))
(3, 'Jean Dupont', 'jean.dupont@example.com', datetime.datetime(...))
(4, 'Sophie Laurent', 'sophie.laurent@example.com', datetime.datetime(...))
(5, 'Lucas Bernard', 'lucas.bernard@example.com', datetime.datetime(...))
```

---

## Docker Commands Reference

### Basic Operations

```bash
# Start the container
docker-compose up -d

# Stop the container
docker-compose down

# Stop and remove volumes (deletes all data)
docker-compose down -v

# View logs
docker-compose logs -f

# Rebuild the image
docker-compose build --no-cache
```

### Database Management

```bash
# Execute a SQL file
docker exec -i 1-2_postgresql-in-docker-db-1 psql -U dev_user -d dev_db < your_script.sql

# Create a database backup
docker exec -t 1-2_postgresql-in-docker-db-1 pg_dump -U dev_user dev_db > backup.sql

# Restore a database backup
docker exec -i 1-2_postgresql-in-docker-db-1 psql -U dev_user -d dev_db < backup.sql
```

---

## Data Persistence

This project uses Docker volumes to persist data:

- Volume name: `postgres_data`
- Mount point: `/var/lib/postgresql/data`

This means your data will survive container restarts. To completely remove the data:

```bash
docker-compose down -v
```

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

## Troubleshooting

### Container won't start

```bash
# Check logs for errors
docker-compose logs

# Common issues:
# - Port 5432 already in use (stop other PostgreSQL instances)
# - Missing .env file (create it with required variables)
```

### Can't connect to the database

```bash
# Verify the container is running
docker ps

# Check network connectivity
docker exec -it 1-2_postgresql-in-docker-db-1 pg_isready -U dev_user

# Verify environment variables
docker exec -it 1-2_postgresql-in-docker-db-1 env | grep POSTGRES
```

### Table doesn't exist

```bash
# Check if init.sql ran successfully
docker logs 1-2_postgresql-in-docker-db-1 | grep "CREATE TABLE"

# If not, the container might have been started before
# Remove the volume and restart:
docker-compose down -v
docker-compose up -d
```

### Python script fails to connect

```bash
# Verify .env file exists and contains correct values
cat .env

# Check that psycopg2 is installed
pip list | grep psycopg2

# Ensure the database is accessible
telnet localhost 5432
```

---

## Key Concepts Learned

### PostgreSQL Docker Image
- Using the official `postgres:17` image as a base
- Understanding `FROM` instruction and configuration

### Database Initialization
- How PostgreSQL automatically runs scripts in `/docker-entrypoint-initdb.d/`
- Using `init.sql` to create tables and seed data

### Port Mapping
- Exposing container port 5432 to host port 5432
- Understanding how your machine communicates with the container

### Docker Volumes
- Ensuring data persists even when containers are removed
- Difference between volumes and bind mounts

### Environment Variables
- Clean configuration using `.env` files
- Security best practices (not committing passwords to Git)

### Database Client (psql)
- Connecting to PostgreSQL from the command line
- Basic SQL queries (SELECT, INSERT, CREATE TABLE)

---

## Success Criteria

This project is successful if:

1. The Dockerfile creates a valid PostgreSQL image
2. The container launches without errors and remains active
3. You can connect with `psql` from your machine
4. The `dev_db` database exists and contains a `users` table with data
5. A simple SQL query (`SELECT * FROM users;`) returns the data
6. Everything is in a GitHub repo with an explanatory README
7. (Bonus) Python script queries the DB and displays the results

---

## Resources

### Docker + PostgreSQL
- [PostgreSQL Official Image](https://hub.docker.com/_/postgres)
- [Docker Volumes Documentation](https://docs.docker.com/storage/volumes/)
- [Docker Compose Getting Started](https://docs.docker.com/compose/gettingstarted/)

### PostgreSQL Basics
- [PostgreSQL CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html)
- [PostgreSQL INSERT](https://www.postgresql.org/docs/current/sql-insert.html)
- [psql Cheatsheet](https://tomcam.github.io/postgres/)

### Python + PostgreSQL
- [psycopg2 Documentation](https://www.psycopg.org/)
- [SQLAlchemy ORM](https://www.sqlalchemy.org/)

---

## Part of Learning Roadmap

This is **Project 1-2** in the 10-month Data Engineering Learning Roadmap (Jan-Oct 2026).

**Month** January (Week 3)
**Focus:** Databases, SQL, Docker, Python
**Time Investment:** 4-5 hours
**Repository** https://github.com/benwaraiotoko/DE-Learning-Projects/1-2_PostgreSQL-in-Docker