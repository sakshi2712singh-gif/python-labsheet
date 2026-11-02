import sqlite3

from db_utils import database, prompt_int, prompt_marks, prompt_name


def main():
    # Gather a student's roll number and details from the user.
    roll_no = prompt_int("Roll number: ", minimum=1)
    name = prompt_name("Student name: ")
    age = prompt_int("Student age: ", minimum=0)
    marks = prompt_marks("Student marks (0-100): ")
    try:
        # Use bound parameters rather than building SQL from user input.
        with database() as connection:
            connection.execute(
                "INSERT INTO students (roll_no, name, age, marks) VALUES (?, ?, ?, ?)",
                (roll_no, name, age, marks),
            )
        print(f"Added {name} with roll number {roll_no}.")
    except sqlite3.IntegrityError as error:
        print(f"Could not add that student; check for a duplicate roll number: {error}")
    except sqlite3.Error as error:
        print(f"Database error while adding the student: {error}")


if __name__ == "__main__":
    main()
