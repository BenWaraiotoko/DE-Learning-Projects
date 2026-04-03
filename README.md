# Data Engineering Projects

So yeah, I decided to learn Data Engineering. Not because someone told me to, not because of a LinkedIn post about "top 10 in-demand skills" — just because I wanted to understand how data actually moves, transforms, and ends up somewhere useful. Classic self-inflicted nerd spiral.

This repo is the result of that obsession: a collection of hands-on projects where I build things, break them, fix them, and occasionally feel smart for five minutes.

## The Stack

Because apparently you can't touch data without installing half the internet first:

- **Docker** — containerize all the things
- **PostgreSQL** — the database that never lets you down
- **Apache Airflow** — orchestration, or as I call it, "cron jobs with a god complex"
- **dbt** — SQL but make it fashionable
- **PySpark** — for when your laptop fan needs a workout
- **Kubernetes** — containers on steroids, pain included
- **pytest** — because "it works on my machine" is not a deployment strategy

## Projects

### Docker Foundations
- [done] Hello Docker | Docker, Python
- [wip] PostgreSQL in Docker | Docker, PostgreSQL, Python
- [ ] Data Loader | Python, Pandas, PostgreSQL

### Airflow Orchestration
- [ ] First Airflow DAG | Airflow, Python, PostgreSQL
- [ ] Error Handling | Airflow, Python
- [ ] Airflow + PostgreSQL | Airflow, PostgreSQL, Pandas

### dbt Transformations
- [ ] dbt Setup | dbt-core, PostgreSQL
- [ ] Tests & Docs | dbt-core, PostgreSQL, SQL
- [ ] Airflow + dbt | Airflow, dbt-core, PostgreSQL

### Scaling & Cloud
- [ ] PySpark Job | PySpark, Python, PostgreSQL
- [ ] Kubernetes + Airflow | Kubernetes, Airflow, Docker
- [ ] Portfolio Polish | Documentation

### CAPSTONE: Fukuoka Weather ETL

The big one. A complete production-grade pipeline that pulls weather data from the OpenWeatherMap API, shoves it through Airflow, cleans it with dbt, and stores it somewhere that makes sense.

**Stack**: Python, Airflow, dbt, PostgreSQL, Docker, pytest
**Features**: Daily automation, error handling, data quality tests, CI/CD

```
OpenWeatherMap API → Airflow → PostgreSQL (raw) → dbt → PostgreSQL (analytics)
```

Why Fukuoka? Because I can.

### Bootcamp Preparation
Interview prep → Le Wagon application → Prework → Bootcamp

## Contact

[Portfolio](https://bwo-portfolio.pages.dev/) | [benwaraiotoko@proton.me](mailto:benwaraiotoko@proton.me) | [LinkedIn](https://www.linkedin.com/in/benjamin-n-b60b9439a/)

---

**28 projects** | **Goal: Le Wagon Data Engineering Bootcamp**
