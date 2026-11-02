import sqlite3

from db_utils import database


def main():
    # Match each course to its student using an INNER JOIN.
    try:
        with database() as connection:
            records = connection.execute(
                """
                SELECT students.name, courses.course_name
                FROM students
                INNER JOIN courses ON courses.student_id = students.id
                ORDER BY students.id, courses.course_name
                """
            ).fetchall()
        if not records:
            print("No matching student and course records; run Q21 after adding students.")
            return
        for record in records:
            print(f"{record['name']} — {record['course_name']}")
    except sqlite3.Error as error:
        print(f"Could not join students and courses: {error}")


if __name__ == "__main__":
    main()
