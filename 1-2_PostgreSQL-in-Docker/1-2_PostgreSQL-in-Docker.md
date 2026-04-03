# 🐘 PROJECT 1.2 – PostgreSQL in Docker

**Estimated time:** 4–5 hours

**Prerequisites:** Project 1.1 (Hello Docker) completed

**Difficulty:** Intermediate (+ DB management)

---

## 🎯 Objective

Create a **Docker container that runs PostgreSQL**, initialize a simple database, and make SQL queries from your local machine.

You will learn:

- How to orchestrate services (DB + Python)
- Docker volumes (data persistence)
- Environment variables and Docker configuration
- Introduction to PostgreSQL (no SQL expertise required)

---

## 📋 Specifications

### 1. **Create a custom PostgreSQL Dockerfile**

You must create a Dockerfile that:

- ✅ Starts with the official `postgres:15` image (or newer)
- ✅ Initializes a database named `dev_db`
- ✅ Creates a custom user with a password
- ✅ Seeds the DB with a simple table (example: `users` with id, name, and email columns)

**Deliverables to put in the repo:**

```
project-1-2/
├── Dockerfile
├── init.sql           (script d'initialisation DB)
├── docker-compose.yml (optionnel mais recommandé)
├── README.md
└── requirements.txt   (si tu vas faire des queries depuis Python)

```

### 2. **Test the connection**

- ✅ Launch the container: `docker run` or `docker-compose up`
- ✅ Check that PostgreSQL is listening on port 5432
- ✅ Connect with `psql` (PostgreSQL CLI)
- ✅ Verify that the table and data exist
- ✅ Run a simple `SELECT * FROM users;` query

### 3. **Bonus (if you want to go further)**

- Write a small Python script that connects to the DB and returns the users
- Use `docker-compose` to orchestrate a PostgreSQL container + a Python container
- Make the data persistent with a Docker volume

---

## 📚 Resources

### Docker + PostgreSQL Fundamentals

- **PostgreSQL Official Image**: [https://hub.docker.com/_/postgres](https://hub.docker.com/_/postgres)
- **Docker Volumes**: [https://docs.docker.com/storage/volumes/](https://docs.docker.com/storage/volumes/)
- **docker-compose quickstart**: [https://docs.docker.com/compose/gettingstarted/](https://docs.docker.com/compose/gettingstarted/)

### PostgreSQL Basics (very accessible)

- **PostgreSQL CREATE TABLE**: [https://www.postgresql.org/docs/current/sql-createtable.html](https://www.postgresql.org/docs/current/sql-createtable.html)
- **PostgreSQL INSERT**: [https://www.postgresql.org/docs/current/sql-insert.html](https://www.postgresql.org/docs/current/sql-insert.html)
- **psql cheatsheet**: [https://tomcam.github.io/postgres/](https://tomcam.github.io/postgres/)

### Testing + Debugging

- **Docker logs**: `docker logs <container_id>`
- **Inside container**: `docker exec -it <container_id> bash`
- **Connect to DB**: `docker exec -it <container_id> psql -U <user> -d <database>`

### Optional: Python + PostgreSQL

- **psycopg2 (Python PostgreSQL driver)**: [https://www.psycopg.org/](https://www.psycopg.org/)
- **SQLAlchemy (ORM)**: [https://www.sqlalchemy.org/](https://www.sqlalchemy.org/) (optional, too early for this phase)

---

## Success criteria

You have succeeded if:

1. ✅ Your Dockerfile creates a valid PostgreSQL image
2. ✅ The container launches without errors and remains active
3. ✅ You can connect with `psql` from your machine
4. ✅ The `dev_db` database exists and contains a `users` table with data
5. ✅ A simple SQL query (`SELECT * FROM users;`) returns the data
6. ✅ Everything is in a GitHub repo with an explanatory README
7. ✅ (Bonus) Python script that queries the DB and displays the results

---

## 🧠 Key Concepts to master

| Concept | Why it's important | To look up |
| --- | --- | --- |
| **PostgreSQL image** | The basis of everything; understanding FROM + config | Docker Hub docs |
| **init.sql / entrypoint** | How the DB is created at startup | PostgreSQL initialization scripts |
| **Ports & networking** | How your machine communicates with the container | `docker run -p`, port mapping |
| **Volumes** | Data does not disappear with `docker rm` | Docker volumes vs bind mounts |
| **Environment variables** | Clean configuration (user, password, DB name) | `-e` flag in `docker run` |
| **psql** | Verify that everything is working | psql basics (connect, list tables, SELECT) |

---

## 📊 Suggested timeline

### Day 1-2: Research + Setup

- Read the PostgreSQL documentation (30 min)
- Create the basic Dockerfile (1 hour)
- Test `docker build` + `docker run` (1 hour)

### Day 3: Init Database

- Create the `init.sql` script (1 hour)
- Connect the users table (30 min)
- Insert test data (30 min)

### Day 4: Testing + Documentation

- Connect with `psql` and verify (30 min)
- Write [README.md](http://readme.md/) (30 min)
- Push to GitHub (15 min)

### Day 5 (Optional): Python Integration

- Create Python script that queries (1 hour)
- Use `docker-compose` to orchestrate everything (1 hour)

---

## 💡 Hints if stuck (peek after 20+ min)

**"Where to start?"**
→ Start with `docker run -d postgres:15` (detached, check that it works)

**"How do I initialize the DB?"**
→ PostgreSQL accepts an `init.sql` file via ENTRYPOINT

**"Why doesn't my table exist?"**
→ Check that the init.sql script is running (logs: `docker logs`)

**"How do I connect?"**
→ `docker exec -it <container> psql -U <user> -d <database>`

---

## 🎁 Bonus (After You Finish)

1. **Add a Python script** that queries the DB and displays the results
2. **Use Docker Compose** to manage the container
3. **Add a second table** with a relationship to `users`
4. **Write tests** for your SQL queries

**Good luck! PostgreSQL is cool once it works.** 💪

---

*Project Brief created: January 15, 2026*