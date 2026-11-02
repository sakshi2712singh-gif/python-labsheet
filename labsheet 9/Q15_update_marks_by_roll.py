import sqlite3

from db_utils import database, prompt_int, prompt_marks


def main():
    # Collect a roll number and validated replacement marks.
    roll_no = prompt_int("Roll number to update: ", minimum=1)
    marks = prompt_marks("New marks (0-100): ")
    try:
        # Update the matching student using parameterized SQL.
        with database() as connection:
            cursor = connection.execute(
                "UPDATE students SET marks = ? WHERE roll_no = ?",
                (marks, roll_no),
            )
        print("Student marks updated." if cursor.rowcount else "No student has that roll number.")
    except sqlite3.Error as error:
        print(f"Could not update student marks: {error}")


if __name__ == "__main__":
    main()
