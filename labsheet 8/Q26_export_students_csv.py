import csv
import sqlite3
from pathlib import Path

from db_utils import BASE_DIR, database


def main():
    # Export all student fields to a new CSV file without overwriting existing files.
    filename = input("Export filename [students_export.csv]: ").strip() or "students_export.csv"
    output = Path(filename)
    if not output.is_absolute():
        output = BASE_DIR / output
    try:
        with database() as connection:
            students = connection.execute(
                "SELECT id, name, age, marks FROM students ORDER BY id"
            ).fetchall()
        with output.open("x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "age", "marks"])
            writer.writerows(
                (student["id"], student["name"], student["age"], student["marks"])
                for student in students
            )
        print(f"Exported {len(students)} student record(s) to {output.name}.")
    except FileExistsError:
        print("That file already exists; choose a different filename.")
    except (OSError, sqlite3.Error, csv.Error) as error:
        print(f"Could not export student data: {error}")


if __name__ == "__main__":
    main()
