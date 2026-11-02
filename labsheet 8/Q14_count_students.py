import sqlite3

from db_utils import database


def main():
    # Count the rows in the students table.
    try:
        with database() as connection:
            count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        print(f"Total student records: {count}")
    except sqlite3.Error as error:
        print(f"Could not count student records: {error}")


if __name__ == "__main__":
    main()
