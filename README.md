# Scrapery – Local Data Engineering Proof-of-Concept

This repository is a **minimal, local-first pipeline** that you can run entirely on your laptop and later migrate to the cloud.

## Stack

- Python 3.11
- DuckDB (embedded, runs in-process)
- `dbt-core` + `dbt-duckdb`
- Docker + Docker Compose (optional for isolation)

## Project Layout

```
├── docker/                 # Docker / Compose configs
│   ├── Dockerfile          # Python runtime for the app service
│   └── docker-compose.yml  # Services for duckdb + app
├── dbt/                    # dbt project (duckdb profile)
│   ├── dbt_project.yml
│   ├── profiles.yml
│   └── models/
│       ├── staging/
│       │   ├── example_staging.sql
│       │   └── schema.yml
│       ├── intermediate/
│       └── marts/
├── src/                    # Python modules
│   ├── scraper.py          # Example web-scraper
│   ├── db.py               # DuckDB helpers
│   └── config.py           # .env loader
├── data/                   # DuckDB file + raw scraped data (volume-mounted)
├── requirements.txt        # Python dependencies
└── Makefile                # Convenience commands
```

## Quickstart

### 1. Prerequisites

- Docker & Docker Compose
- Python 3.11 + `pip`

### 2. Clone & Install

```bash
# Install Python deps locally (outside Docker) – optional
make install-scraper
```

### 3. Configure Targets

Copy the sample environment file and update it with real selectors / URLs:

```bash
cp .env.example .env
# Edit the values
```

### 4. Build & Run Services (optional)

Run everything in containers:

```bash
make build   # builds the app image
make up      # starts duckdb & app containers in background
```

### 5. Scrape Data

```bash
make run-scraper
```

Scraped output is written to `data/scraped.txt`.

### 6. Load Into DuckDB (example)

Inside a Python shell or a Jupyter notebook:

```python
from src.db import load_csv
load_csv("data/scraped.txt", table_name="raw_scraped")
```

### 7. Transform With dbt

```bash
make dbt-run   # build models
make dbt-test  # run tests
```

## Next Steps / TODOs

- Replace the placeholder scraper logic with real parsing rules
- Add proper staging & transformation SQL in `dbt/`
- Configure CI and remote storage when moving to the cloud

---

MIT © 2024
