import sqlite3

from db_utils import database


def main():
    # Sort student records alphabetically by name, ignoring case.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT roll_no, name, age, marks FROM students "
                "ORDER BY name COLLATE NOCASE, roll_no"
            ).fetchall()
        if not students:
            print("No student records found.")
            return
        for student in students:
            print(
                f"{student['name']} (roll {student['roll_no']}): "
                f"{student['marks']:g} marks"
            )
    except sqlite3.Error as error:
        print(f"Could not sort student records: {error}")


if __name__ == "__main__":
    main()
