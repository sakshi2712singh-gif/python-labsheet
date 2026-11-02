import sqlite3

from db_utils import database, prompt_name


def main():
    # Bind the requested name as a value instead of embedding it in SQL.
    table_name = prompt_name("Table name to check [students]: ")
    try:
        with database() as connection:
            result = connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type = 'table' AND name = ?",
                (table_name,),
            ).fetchone()
        print(f"Table {table_name!r} {'exists' if result else 'does not exist'}.")
    except sqlite3.Error as error:
        print(f"Could not check the table: {error}")


if __name__ == "__main__":
    main()
