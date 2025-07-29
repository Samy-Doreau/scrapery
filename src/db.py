from pathlib import Path
from typing import Optional

import duckdb

# Path to database file stored on host volume (see docker-compose)
DB_PATH = Path("data") / "scrapery.duckdb"


def get_connection(readonly: bool = False) -> duckdb.DuckDBPyConnection:
    """Return a DuckDB connection. Creates file/dir if necessary."""
    if not DB_PATH.parent.exists():
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    return duckdb.connect(str(DB_PATH), read_only=readonly)


def load_csv(csv_path: str | Path, table_name: str, conn: Optional[duckdb.DuckDBPyConnection] = None):
    """Load a CSV file into *table_name* in DuckDB (overwrites)."""
    close_conn = False
    if conn is None:
        conn = get_connection()
        close_conn = True

    conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{csv_path}');")

    if close_conn:
        conn.close() 