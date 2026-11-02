import sqlite3

from db_utils import database


def main():
    # Display each column's name, type, and key/nullability information.
    try:
        with database() as connection:
            columns = connection.execute("PRAGMA table_info(students)").fetchall()
        if not columns:
            print("The students table does not exist; run Q03 first.")
            return
        print(f"{'Column':<12} {'Type':<12} {'Not null':<10} Primary key")
        for column in columns:
            print(
                f"{column['name']:<12} {column['type']:<12} "
                f"{bool(column['notnull'])!s:<10} {bool(column['pk'])}"
            )
    except sqlite3.Error as error:
        print(f"Could not describe the students table: {error}")


if __name__ == "__main__":
    main()
