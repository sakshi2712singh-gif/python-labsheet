import sqlite3

from db_utils import database, prompt_int, prompt_marks, prompt_name


def main():
    # Collect multiple rows and save them in a single transaction.
    print("Enter student records. Leave the name blank when finished.")
    records = []
    while True:
        name = input("Student name (blank to finish): ").strip()
        if not name:
            break
        age = prompt_int("Student age: ", minimum=0)
        marks = prompt_marks("Student marks (0-100): ")
        records.append((name, age, marks))

    if not records:
        print("No records were entered.")
        return
    try:
        with database() as connection:
            connection.executemany(
                "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                records,
            )
        print(f"Inserted {len(records)} student record(s).")
    except sqlite3.Error as error:
        print(f"Could not insert the student records: {error}")


if __name__ == "__main__":
    main()
