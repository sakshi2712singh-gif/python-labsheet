import sqlite3

from db_utils import database, prompt_int, prompt_marks, prompt_name


def insert_student(connection, name, age, marks):
    """Insert a student using a reusable, parameterized function."""
    cursor = connection.execute(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
        (name, age, marks),
    )
    return cursor.lastrowid


def fetch_students(connection):
    """Return all students using a reusable query function."""
    return connection.execute(
        "SELECT id, name, age, marks FROM students ORDER BY id"
    ).fetchall()


def main():
    # Keep the insert and fetch logic in functions that can be reused elsewhere.
    name = prompt_name("Student name: ")
    age = prompt_int("Student age: ", minimum=0)
    marks = prompt_marks("Student marks (0-100): ")
    try:
        with database() as connection:
            student_id = insert_student(connection, name, age, marks)
            students = fetch_students(connection)
        print(f"Inserted student with ID {student_id}.")
        for student in students:
            print(f"{student['id']}: {student['name']}, age {student['age']}, marks {student['marks']:g}")
    except sqlite3.Error as error:
        print(f"Could not insert or fetch students: {error}")


if __name__ == "__main__":
    main()
