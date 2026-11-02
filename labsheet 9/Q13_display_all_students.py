import sqlite3

from db_utils import database


def main():
    # Read every student and display records in roll-number order.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT id, roll_no, name, age, marks FROM students ORDER BY roll_no"
            ).fetchall()
        if not students:
            print("No student records found.")
            return
        for student in students:
            print(
                f"ID: {student['id']}, Roll: {student['roll_no']}, "
                f"Name: {student['name']}, Age: {student['age']}, "
                f"Marks: {student['marks']:g}"
            )
    except sqlite3.Error as error:
        print(f"Could not read student records: {error}")


if __name__ == "__main__":
    main()
