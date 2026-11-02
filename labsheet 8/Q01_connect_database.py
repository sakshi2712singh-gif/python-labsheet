import sqlite3

from db_utils import database, database_path


def main():
    # Open and close a SQLite connection to verify database connectivity.
    try:
        with database() as connection:
            connection.execute("SELECT 1").fetchone()
        print(f"Connected to SQLite database successfully: {database_path()}")
    except sqlite3.Error as error:
        print(f"Database connection failed: {error}")


if __name__ == "__main__":
    main()
