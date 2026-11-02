import sqlite3

from db_utils import database, prompt_int, prompt_marks


def main():
    # Update marks for a selected ID using bound SQL parameters.
    student_id = prompt_int("Student ID: ", minimum=1)
    marks = prompt_marks("New marks (0-100): ")
    try:
        with database() as connection:
            cursor = connection.execute(
                "UPDATE students SET marks = ? WHERE id = ?",
                (marks, student_id),
            )
        print("Student marks updated." if cursor.rowcount else "No student has that ID.")
    except sqlite3.Error as error:
        print(f"Could not update student marks: {error}")


if __name__ == "__main__":
    main()
