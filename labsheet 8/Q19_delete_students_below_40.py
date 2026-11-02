import sqlite3

from db_utils import database


def main():
    # Show how many rows match before asking permission to delete them.
    try:
        with database() as connection:
            matching = connection.execute(
                "SELECT COUNT(*) FROM students WHERE marks < ?",
                (40,),
            ).fetchone()[0]
        print(f"Students with marks below 40: {matching}")
        if matching == 0:
            return
        if input("Type DELETE to remove these records: ") != "DELETE":
            print("Cancelled; no students were deleted.")
            return
        with database() as connection:
            cursor = connection.execute("DELETE FROM students WHERE marks < ?", (40,))
        print(f"Deleted {cursor.rowcount} student record(s).")
    except sqlite3.Error as error:
        print(f"Could not remove low-scoring students: {error}")


if __name__ == "__main__":
    main()
