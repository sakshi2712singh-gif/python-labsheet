import sqlite3

from db_utils import database


def main():
    # Count and display the number of student records.
    try:
        with database() as connection:
            count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        print(f"Total student records: {count}")
    except sqlite3.Error as error:
        print(f"Could not count student records: {error}")


if __name__ == "__main__":
    main()
