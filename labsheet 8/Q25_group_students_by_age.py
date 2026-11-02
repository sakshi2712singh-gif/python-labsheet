import sqlite3

from db_utils import database


def main():
    # Group student rows by age and count records in each group.
    try:
        with database() as connection:
            groups = connection.execute(
                "SELECT age, COUNT(*) AS student_count "
                "FROM students GROUP BY age ORDER BY age"
            ).fetchall()
        if not groups:
            print("No students found.")
            return
        for group in groups:
            print(f"Age {group['age']}: {group['student_count']} student(s)")
    except sqlite3.Error as error:
        print(f"Could not group students by age: {error}")


if __name__ == "__main__":
    main()
