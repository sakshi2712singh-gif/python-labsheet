import sqlite3

from db_utils import database


def main():
    # Keep every student in the result, including students without courses.
    try:
        with database() as connection:
            records = connection.execute(
                """
                SELECT students.name, courses.course_name
                FROM students
                LEFT JOIN courses ON courses.student_id = students.id
                ORDER BY students.id, courses.course_name
                """
            ).fetchall()
        if not records:
            print("No students found.")
            return
        for record in records:
            course = record["course_name"] or "No course assigned"
            print(f"{record['name']} — {course}")
    except sqlite3.Error as error:
        print(f"Could not perform the LEFT JOIN: {error}")


if __name__ == "__main__":
    main()
