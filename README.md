# Advent of SQL with DuckDB

This project provides a streamlined setup for solving Advent of SQL challenges using DuckDB and Python.

## Prerequisites

- **`uv`:**  Install the `uv` package manager (`pip install uv`)


## Setup

- For each day's challenge, create a folder within advent_of_sql (e.g., advent_of_sql/day_01, advent_of_sql/day_02).
- Inside each day's folder, place:
    advent_of_sql_day_{day_number}.sql: The SQL file provided for that day's challenge.
    answer.sql: Your SQL solution for the challenge.
Usage
- **Run your solution:**

   ```bash
   make run day=1  # Replace 1 with the desired day number
   ```

- **Open the DuckDB CLI:**

   ```bash
   make db day=1  # Replace 1 with the desired day number
   ```

### Makefile Targets
- `run`: Runs the Python script to set up the database and execute your answer SQL.
    - Requires the `day` parameter (e.g., `make run day=02`).
- `db`: Opens the DuckDB CLI with the database for the specified day. 
    - Requires the `day` parameter (e.g., `make db day=02`).

### Project Structure

```bash
├── README.md
├── advent_of_sql
│   ├── __init__.py
│   └── advent_sql.py
├── pyproject.toml
├── Makefile
└── ...
```
