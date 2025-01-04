import argparse

import duckdb


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
    # Read the SQL file contents
    with open(data_file_path) as f:
        sql_file_contents = f.read()

    # Execute the SQL statements
    conn.execute(sql_file_contents)

    conn.close()
    print("Database setup complete!")


def run_answer(answer_file_path: str, db_path: str):
    """Runs the answer SQL against the database for the given day."""
    conn = duckdb.connect(db_path)
    with open(answer_file_path) as f:
        answer_sql = f.read()
    print("Answer:")
    df = conn.sql(answer_sql)
    for row in df.fetchall():
        print(",".join(str(x) for x in row))  # Join values with commas

    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", help="Day of the challenge (e.g., 1, 2)")

    args = parser.parse_args()

    db_path = get_db_path(args.day)
    setup_database(get_data_file_path(args.day), db_path)
    run_answer(get_answer_file_path(args.day), db_path)
