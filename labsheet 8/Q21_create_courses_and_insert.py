import sqlite3

from db_utils import database


def main():
    # Create a student-linked courses table with a key that prevents duplicates.
    try:
        with database() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER NOT NULL,
                    course_name TEXT NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
                    UNIQUE (student_id, course_name)
                )
                """
            )
            sample_courses = (
                ("Python Programming",),
                ("Database Management",),
                ("File Handling",),
            )
            for offset, (course_name,) in enumerate(sample_courses):
                student = connection.execute(
                    "SELECT id FROM students ORDER BY id LIMIT 1 OFFSET ?",
                    (offset,),
                ).fetchone()
                if student is not None:
                    connection.execute(
                        "INSERT OR IGNORE INTO courses (student_id, course_name) VALUES (?, ?)",
                        (student["id"], course_name),
                    )
            count = connection.execute("SELECT COUNT(*) FROM courses").fetchone()[0]
        print(f"Courses table is ready with {count} course record(s).")
        if count == 0:
            print("Add students with Q08 or Q09, then rerun Q21 to add sample courses.")
    except sqlite3.Error as error:
        print(f"Could not create or populate the courses table: {error}")


if __name__ == "__main__":
    main()
