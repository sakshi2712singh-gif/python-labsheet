import sqlite3

from db_utils import database


def main():
    # Sort student records from the highest mark to the lowest.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT id, name, age, marks FROM students ORDER BY marks DESC, id"
            ).fetchall()
        if not students:
            print("No students found.")
            return
        for student in students:
            print(f"{student['name']}: {student['marks']:g}")
    except sqlite3.Error as error:
        print(f"Could not sort student records: {error}")


if __name__ == "__main__":
    main()
