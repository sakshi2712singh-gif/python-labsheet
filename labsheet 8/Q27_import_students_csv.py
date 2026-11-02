import csv
import sqlite3
from pathlib import Path

from db_utils import BASE_DIR, database


REQUIRED_COLUMNS = {"id", "name", "age", "marks"}


def main():
    # Import validated CSV records with bound parameters in one transaction.
    filename = input("CSV filename [sample_students_import.csv]: ").strip() or "sample_students_import.csv"
    source = Path(filename)
    if not source.is_absolute():
        source = BASE_DIR / source
    try:
        with source.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames or not REQUIRED_COLUMNS.issubset(reader.fieldnames):
                print("The CSV header must include id, name, age, and marks.")
                return
            records = []
            for line_number, row in enumerate(reader, start=2):
                try:
                    student_id = int(row["id"])
                    name = row["name"].strip()
                    age = int(row["age"])
                    marks = float(row["marks"])
                except (TypeError, ValueError):
                    raise ValueError(f"Invalid values on CSV line {line_number}.")
                if student_id < 1 or age < 0 or not name or not 0 <= marks <= 100:
                    raise ValueError(f"Values out of range on CSV line {line_number}.")
                records.append((student_id, name, age, marks))

        with database() as connection:
            connection.executemany(
                "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
                records,
            )
        print(f"Imported {len(records)} student record(s).")
    except FileNotFoundError:
        print(f"CSV file not found: {source}")
    except (OSError, ValueError, sqlite3.Error, csv.Error) as error:
        print(f"Could not import student data: {error}")


if __name__ == "__main__":
    main()
