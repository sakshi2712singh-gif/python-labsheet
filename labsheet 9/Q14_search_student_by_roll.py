import sqlite3

from db_utils import database, prompt_int


def main():
    # Ask for the roll number to look up.
    roll_no = prompt_int("Roll number to search: ", minimum=1)
    try:
        with database() as connection:
            student = connection.execute(
                "SELECT id, roll_no, name, age, marks FROM students WHERE roll_no = ?",
                (roll_no,),
            ).fetchone()
        if student is None:
            print(f"No student has roll number {roll_no}.")
        else:
            print(
                f"ID: {student['id']}, Roll: {student['roll_no']}, "
                f"Name: {student['name']}, Age: {student['age']}, "
                f"Marks: {student['marks']:g}"
            )
    except sqlite3.Error as error:
        print(f"Could not search student records: {error}")


if __name__ == "__main__":
    main()
