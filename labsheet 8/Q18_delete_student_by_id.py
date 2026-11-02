import sqlite3

from db_utils import database, prompt_int


def main():
    # Require explicit confirmation before deleting a student's row.
    student_id = prompt_int("Student ID to delete: ", minimum=1)
    if input("Type DELETE to confirm removing this student record: ") != "DELETE":
        print("Cancelled; no student was deleted.")
        return

    try:
        with database() as connection:
            cursor = connection.execute("DELETE FROM students WHERE id = ?", (student_id,))
        print("Student deleted." if cursor.rowcount else "No student has that ID.")
    except sqlite3.Error as error:
        print(f"Could not delete the student: {error}")


if __name__ == "__main__":
    main()
