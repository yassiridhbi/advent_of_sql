# Target to run the Python script (requires 'day' to be specified)
run:
ifndef day
	$(error day is not set. Usage: make run day=01)
endif
	uv run advent_of_sql/advent_sql.py $(day)

# Target to open the DuckDB CLI with the database for the given day (requires 'day')
db:
ifndef day
	$(error day is not set. Usage: make db day=01)
endif
	duckdb advent_day_$(day).duckdb

.PHONY: run db
