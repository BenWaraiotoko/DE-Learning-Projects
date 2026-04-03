# Project 1.3: "Data Loader Script"

**Goal**: Build a Python script that loads CSV data into PostgreSQL, with error handling and Docker support.

## 🎯 Objective

Write a Python script (`loader.py`) that:

1. **Reads a CSV** file (sample data provided)
2. **Transforms the data** with Pandas (renaming columns, types, validation)
3. **Loads into PostgreSQL** (the DB from Project 1.2)
4. **Handles errors** gracefully (DB down, malformed CSV, etc.)
5. **Runs in a Docker container** with dependencies (Pandas, psycopg2)

---

## 📊 Stack

- **Python 3.x**
- **Pandas** (CSV reading/transformation)
- **psycopg2** (PostgreSQL driver for Python)
- **PostgreSQL** (DB for project 1.2)
- **Docker** (run script in container)

---

## 📁 Expected deliverables

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

## 🔧 Specifications

### 1. Script `loader.py`

**Input**: a CSV file with columns `name`, `email`, `age`,**city Output**: insertion into the PostgreSQL `users` table (or new table)

```
Comportement attendu :
- Lire sample_data.csv
- Nettoyer : colonnes uppercase → lowercase, espaces trim, NULL handling
- Valider : email doit être unique, age > 0
- Insérer dans DB avec try/except
- Log : "✓ Loaded 10 rows" ou "✗ Error: Connection failed"

```

### 2. Dockerfile

Must build an image capable of:

- Have Python 3.x + dependencies (Pandas, psycopg2)
- Execute `python loader.py`
- Connect to the PostgreSQL container from docker-compose

### 3. docker-compose.yml

- Service `db`: PostgreSQL (as in 1.2)
- `Loader` service: Python script
- `loader` must wait for `db` to be ready before running

### 4. sample_data.csv

Provide a CSV with 5–10 rows for testing:

```
name,email,age,city
Alice Johnson,alice@example.com,28,Paris
Bob Smith,bob@example.com,35,Lyon
Carol White,  carol@example.com  ,31,Marseille

```

---

## 📌 Recommended resources

| Resource | Duration | Objective |
| --- | --- | --- |
| [Pandas Official Docs - read_csv()](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) | 10 min | Reading CSV + essential options |
| [psycopg2 Tutorial](https://www.psycopg.org/documentation/) | 15 min | Connection, cursor, INSERT |
| [Docker + Python](https://docs.docker.com/language/python/) | 10 min | Dockerfile for Python app |
| [Error Handling Python](https://docs.python.org/3/tutorial/errors.html) | 10 min | try/except patterns |
| YouTube: "Pandas + PostgreSQL" | ~20 min | Example project walk-through |

---

## ⏱️ Estimated duration

| Task | Time |
| --- | --- |
| Reading CSV + Pandas | 45 min |
| DB connection + INSERT | 45 min |
| Error handling + logging | 30 min |
| Docker + docker-compose | 30 min |
| Testing + README | 30 min |
| **TOTAL** | **~3 to 4 hours** |

---

## 📋 Delivery checklist

- [ ]  `loader.py` reads CSV, inserts into DB, handles errors
- [ ]  `Dockerfile` + `requirements.txt` builds without errors
- [ ]  `docker-compose up` launches DB + loader, loads data
- [ ]  `sample_data.csv` included (5–10 lines min)
- [ ]  `README.md`: step-by-step setup + run
- [ ]  Commits: 2–3 logical commits (setup / loader / docker)
- [ ]  Repo: `benjamin-data-loader` or similar
- [ ]  Logs: displays number of lines loaded or clear error

---

## 🤔 Questions to check your understanding

1. *What is the role of Pandas in relation to psycopg2?*
2. *Why have a CSV if you have a DB?*
3. *What could go wrong during execution, and how would you handle it?*

