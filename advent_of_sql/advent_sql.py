from pkgutil import get_data
import duckdb
import argparse
import os

def get_data_file_path(day: str) -> str:
    """Returns the path to the data file for the given day."""
    return f"advent_of_sql/day_{day}/advent_of_sql_day_{day}.sql"

def get_answer_file_path(day: str) -> str:
    """Returns the path to the answer file for the given day."""
    return f"advent_of_sql/day_{day}/answer.sql"

def get_db_path(day: str) -> str:
    """Returns the path to the DuckDB database for the given day."""
    return f"advent_day_{day}.duckdb"

def setup_database(data_file_path: str, db_path: str):
    """Creates and sets up the DuckDB database for the given day."""
    conn = duckdb.connect(db_path)
    conn.execute("INSTALL sqlite; LOAD sqlite;")
    conn.execute(f".read {data_file_path}")
    conn.close()
    print(f"Database setup complete!")

def run_answer(answer_file_path: str, db_path: str):
    """Runs the answer SQL against the database for the given day."""
    conn = duckdb.connect(db_path)
    with open(answer_file_path, "r") as f:
        answer_sql = f.read()
    conn.execute(answer_sql)
    result = conn.fetchall()
    conn.close()
    print("Answer:")
    print(result) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="Day of the challenge (e.g., 1, 2)")

    args = parser.parse_args()

    db_path = get_db_path(args.day)
    setup_database(get_data_file_path(args.day), db_path)
    run_answer(get_answer_file_path(args.day), db_path) 
