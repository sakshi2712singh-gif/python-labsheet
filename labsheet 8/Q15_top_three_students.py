import sqlite3

from db_utils import database


def main():
    # Retrieve at most three students, with ID as a stable tie breaker.
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT id, name, marks FROM students ORDER BY marks DESC, id LIMIT ?",
                (3,),
            ).fetchall()
        if not students:
            print("No students found.")
            return
        print("Top scoring students:")
        for rank, student in enumerate(students, start=1):
            print(f"{rank}. {student['name']} — {student['marks']:g}")
    except sqlite3.Error as error:
        print(f"Could not find top students: {error}")


if __name__ == "__main__":
    main()
