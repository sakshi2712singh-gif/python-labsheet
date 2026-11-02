import sqlite3

from db_utils import database


def main():
    # Retrieve and display every student in ID order.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT id, name, age, marks FROM students ORDER BY id"
            ).fetchall()
        if not students:
            print("No students found.")
            return
        print(f"{'ID':<5} {'Name':<22} {'Age':<6} Marks")
        for student in students:
            print(
                f"{student['id']:<5} {student['name']:<22} "
                f"{student['age']:<6} {student['marks']:g}"
            )
    except sqlite3.Error as error:
        print(f"Could not read student records: {error}")


if __name__ == "__main__":
    main()
