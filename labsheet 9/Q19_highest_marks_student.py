import sqlite3

from db_utils import database


def main():
    # Return every student tied for the highest mark.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT roll_no, name, marks FROM students "
                "WHERE marks = (SELECT MAX(marks) FROM students) "
                "ORDER BY roll_no"
            ).fetchall()
        if not students:
            print("No student records found.")
            return
        highest = students[0]["marks"]
        print(f"Highest marks: {highest:g}")
        for student in students:
            print(f"{student['name']} (roll {student['roll_no']})")
    except sqlite3.Error as error:
        print(f"Could not find the highest mark: {error}")


if __name__ == "__main__":
    main()
