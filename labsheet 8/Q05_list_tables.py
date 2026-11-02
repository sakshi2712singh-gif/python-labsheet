import sqlite3

from db_utils import database


def main():
    # Read user-created table names from SQLite's schema catalog.
    try:
        with database() as connection:
            tables = connection.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
            ).fetchall()
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table["name"])
        else:
            print("No tables are available yet.")
    except sqlite3.Error as error:
        print(f"Could not list database tables: {error}")


if __name__ == "__main__":
    main()
