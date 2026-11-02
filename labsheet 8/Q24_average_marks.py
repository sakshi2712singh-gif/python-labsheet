import sqlite3

from db_utils import database


def main():
    # Calculate an aggregate average and handle an empty table explicitly.
    try:
        with database() as connection:
            result = connection.execute(
                "SELECT AVG(marks), COUNT(*) FROM students"
            ).fetchone()
        if result[1] == 0:
            print("No student marks are available to average.")
        else:
            print(f"Average marks: {result[0]:.2f}")
    except sqlite3.Error as error:
        print(f"Could not calculate the average: {error}")


if __name__ == "__main__":
    main()
