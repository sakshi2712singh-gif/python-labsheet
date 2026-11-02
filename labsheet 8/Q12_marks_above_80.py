import sqlite3

from db_utils import database


def main():
    # Use a parameterized threshold to select marks greater than 80.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT id, name, age, marks FROM students WHERE marks > ? ORDER BY marks DESC",
                (80,),
            ).fetchall()
        if not students:
            print("No students scored above 80.")
            return
        for student in students:
            print(
                f"ID: {student['id']}, Name: {student['name']}, "
                f"Age: {student['age']}, Marks: {student['marks']:g}"
            )
    except sqlite3.Error as error:
        print(f"Could not filter student records: {error}")


if __name__ == "__main__":
    main()
