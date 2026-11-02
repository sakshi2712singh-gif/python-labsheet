import sqlite3

from db_utils import database, prompt_name


def main():
    # Require explicit confirmation before dropping the selected table.
    table_name = prompt_name("Table to drop [students]: ").strip()
    if table_name != "students":
        print("This exercise only allows dropping the students table.")
        return
    confirmation = input("This permanently removes the students table and its data. Type DROP STUDENTS to confirm: ")
    if confirmation != "DROP STUDENTS":
        print("Cancelled; the table was not changed.")
        return

    try:
        with database() as connection:
            exists = connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?",
                (table_name,),
            ).fetchone()
            if exists is None:
                print("The students table does not exist.")
                return
            connection.execute("DROP TABLE students")
        print("Dropped the students table.")
    except sqlite3.Error as error:
        print(f"Could not drop the students table: {error}")


if __name__ == "__main__":
    main()
