import sqlite3

from db_utils import database, prompt_int


def main():
    # Confirm the target exists before asking permission to remove it.
    roll_no = prompt_int("Roll number to delete: ", minimum=1)
    try:
        with database() as connection:
            student = connection.execute(
                "SELECT name FROM students WHERE roll_no = ?",
                (roll_no,),
            ).fetchone()
        if student is None:
            print("No student has that roll number.")
            return
        if input(f"Type DELETE to remove {student['name']} (roll {roll_no}): ") != "DELETE":
            print("Cancelled; no student was deleted.")
            return
        # Delete only the selected roll number after confirmation.
        with database() as connection:
            cursor = connection.execute(
                "DELETE FROM students WHERE roll_no = ?",
                (roll_no,),
            )
        print("Student deleted." if cursor.rowcount else "No student has that roll number.")
    except sqlite3.Error as error:
        print(f"Could not delete the student: {error}")


if __name__ == "__main__":
    main()
