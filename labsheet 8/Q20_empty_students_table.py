import sqlite3

from db_utils import database


def main():
    # Preview the number of records and require typed confirmation before emptying.
    try:
        with database() as connection:
            count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        print(f"Student records to remove: {count}")
        if input("Type EMPTY STUDENTS to remove all rows but keep the table: ") != "EMPTY STUDENTS":
            print("Cancelled; the table was not changed.")
            return
        with database() as connection:
            connection.execute("DELETE FROM students")
        print("Removed all student rows; the table structure remains intact.")
    except sqlite3.Error as error:
        print(f"Could not empty the students table: {error}")


if __name__ == "__main__":
    main()
