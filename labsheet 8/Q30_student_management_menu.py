import sqlite3

from db_utils import (
    database,
    create_students_table,
    prompt_int,
    prompt_marks,
    prompt_name,
)


def add_student():
    """Collect and save one student record."""
    name = prompt_name("Student name: ")
    age = prompt_int("Student age: ", minimum=0)
    marks = prompt_marks("Student marks (0-100): ")
    with database() as connection:
        cursor = connection.execute(
            "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
            (name, age, marks),
        )
    print(f"Added student with ID {cursor.lastrowid}.")


def view_students():
    """Display every student currently in the database."""
    with database() as connection:
        students = connection.execute(
            "SELECT id, name, age, marks FROM students ORDER BY id"
        ).fetchall()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(
            f"{student['id']}: {student['name']}, age {student['age']}, "
            f"marks {student['marks']:g}"
        )


def update_student():
    """Update a student's marks after asking for its ID."""
    student_id = prompt_int("Student ID to update: ", minimum=1)
    marks = prompt_marks("New marks (0-100): ")
    with database() as connection:
        cursor = connection.execute(
            "UPDATE students SET marks = ? WHERE id = ?",
            (marks, student_id),
        )
    print("Student updated." if cursor.rowcount else "No student has that ID.")


def delete_student():
    """Delete one student only after explicit confirmation."""
    student_id = prompt_int("Student ID to delete: ", minimum=1)
    if input("Type DELETE to confirm: ") != "DELETE":
        print("Cancelled; no student was deleted.")
        return
    with database() as connection:
        cursor = connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
    print("Student deleted." if cursor.rowcount else "No student has that ID.")


def main():
    # Ensure this standalone menu can be used after running Q02 only.
    try:
        with database() as connection:
            create_students_table(connection)
        actions = {
            "1": add_student,
            "2": view_students,
            "3": update_student,
            "4": delete_student,
        }
        while True:
            print("\nStudent Management")
            print("1. Add  2. View  3. Update  4. Delete  5. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "5":
                print("Goodbye.")
                break
            action = actions.get(choice)
            if action is None:
                print("Choose a number from 1 to 5.")
                continue
            try:
                action()
            except sqlite3.Error as error:
                print(f"Database error: {error}")
    except sqlite3.Error as error:
        print(f"Could not start the student manager: {error}")


if __name__ == "__main__":
    main()
