import sqlite3

from db_utils import (
    create_students_table,
    database,
    prompt_int,
    prompt_marks,
    prompt_name,
)


def add_student():
    """Add a student record with a unique roll number."""
    roll_no = prompt_int("Roll number: ", minimum=1)
    name = prompt_name("Student name: ")
    age = prompt_int("Student age: ", minimum=0)
    marks = prompt_marks("Student marks (0-100): ")
    with database() as connection:
        connection.execute(
            "INSERT INTO students (roll_no, name, age, marks) VALUES (?, ?, ?, ?)",
            (roll_no, name, age, marks),
        )
    print("Student added.")


def view_students():
    """Display every student in roll-number order."""
    with database() as connection:
        students = connection.execute(
            "SELECT roll_no, name, age, marks FROM students ORDER BY roll_no"
        ).fetchall()
    if not students:
        print("No student records found.")
        return
    for student in students:
        print(
            f"Roll: {student['roll_no']}, Name: {student['name']}, "
            f"Age: {student['age']}, Marks: {student['marks']:g}"
        )


def update_student():
    """Update a student's marks using the roll number."""
    roll_no = prompt_int("Roll number to update: ", minimum=1)
    marks = prompt_marks("New marks (0-100): ")
    with database() as connection:
        cursor = connection.execute(
            "UPDATE students SET marks = ? WHERE roll_no = ?",
            (marks, roll_no),
        )
    print("Student updated." if cursor.rowcount else "No student has that roll number.")


def delete_student():
    """Delete one student only after confirming the record."""
    roll_no = prompt_int("Roll number to delete: ", minimum=1)
    if input("Type DELETE to confirm removing this student: ") != "DELETE":
        print("Cancelled; no student was deleted.")
        return
    with database() as connection:
        cursor = connection.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll_no,),
        )
    print("Student deleted." if cursor.rowcount else "No student has that roll number.")


def main():
    # Ensure the schema is available before entering the CRUD menu.
    try:
        with database() as connection:
            create_students_table(connection)
        actions = {"1": add_student, "2": view_students, "3": update_student, "4": delete_student}
        while True:
            print("\nStudent database CRUD: 1 Add  2 View  3 Update  4 Delete  5 Exit")
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
            except sqlite3.IntegrityError as error:
                print(f"Could not save this record; check the roll number: {error}")
            except sqlite3.Error as error:
                print(f"Database error: {error}")
    except sqlite3.Error as error:
        print(f"Could not start the student manager: {error}")


if __name__ == "__main__":
    main()
