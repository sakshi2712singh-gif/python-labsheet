import sqlite3

from db_utils import create_students_table, database, database_path


def main():
    # Create the students table without dropping existing data.
    try:
        with database() as connection:
            create_students_table(connection)
        print(f"Students table is ready in {database_path().name}.")
    except sqlite3.Error as error:
        print(f"Could not create the students table: {error}")


if __name__ == "__main__":
    main()
