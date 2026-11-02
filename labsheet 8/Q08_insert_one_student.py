import sqlite3

from db_utils import database, prompt_int, prompt_marks, prompt_name


def main():
    # Collect and parameterize the values for one student record.
    name = prompt_name("Student name: ")
    age = prompt_int("Student age: ", minimum=0)
    marks = prompt_marks("Student marks (0-100): ")
    try:
        with database() as connection:
            cursor = connection.execute(
                "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                (name, age, marks),
            )
            student_id = cursor.lastrowid
        print(f"Inserted {name} with ID {student_id}.")
    except sqlite3.Error as error:
        print(f"Could not insert the student: {error}")


if __name__ == "__main__":
    main()
