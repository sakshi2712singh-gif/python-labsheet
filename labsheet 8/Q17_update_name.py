import sqlite3

from db_utils import database, prompt_int, prompt_name


def main():
    # Update the chosen student's name with a parameterized query.
    student_id = prompt_int("Student ID: ", minimum=1)
    name = prompt_name("New name: ")
    try:
        with database() as connection:
            cursor = connection.execute(
                "UPDATE students SET name = ? WHERE id = ?",
                (name, student_id),
            )
        print("Student name updated." if cursor.rowcount else "No student has that ID.")
    except sqlite3.Error as error:
        print(f"Could not update student name: {error}")


if __name__ == "__main__":
    main()
