import sqlite3

from db_utils import database


def main():
    # Select and display only the name and marks columns.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT name, marks FROM students ORDER BY id"
            ).fetchall()
        if not students:
            print("No students found.")
            return
        print(f"{'Name':<22} Marks")
        for student in students:
            print(f"{student['name']:<22} {student['marks']:g}")
    except sqlite3.Error as error:
        print(f"Could not read student records: {error}")


if __name__ == "__main__":
    main()
