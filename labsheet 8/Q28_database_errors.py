import sqlite3

from db_utils import database


def main():
    # Attempt a deliberately invalid query to demonstrate SQLite error handling.
    try:
        with database() as connection:
            connection.execute("SELECT * FROM table_that_does_not_exist").fetchall()
        print("The query completed without a database error.")
    except sqlite3.Error as error:
        print(f"Database error caught ({type(error).__name__}): {error}")
        print("The error was handled; the connection was closed.")


if __name__ == "__main__":
    main()
