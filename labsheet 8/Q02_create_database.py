import sqlite3

from db_utils import ensure_database


def main():
    # SQLite creates its database file when a connection is opened.
    try:
        path = ensure_database()
        print(f"Database is ready: {path}")
    except (OSError, sqlite3.Error) as error:
        print(f"Could not create the database: {error}")


if __name__ == "__main__":
    main()
