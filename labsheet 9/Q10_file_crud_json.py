import json
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def data_path():
    # Allow tests or users to select a separate records file.
    configured = os.environ.get("LABSHEET9_RECORDS_PATH")
    return Path(configured).expanduser().resolve() if configured else BASE_DIR / "student_records.json"


def load_records(path):
    # Read JSON records or start with an empty list when no data file exists.
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)
    if not isinstance(records, list) or any(not isinstance(record, dict) for record in records):
        raise ValueError("The records file must contain a JSON list of objects.")
    return records


def save_records(path, records):
    # Write a temporary sibling file and atomically replace only the data file.
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    try:
        with temporary.open("w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)
            file.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def main():
    # Run create, read, update, and delete actions against the JSON data file.
    path = data_path()
    try:
        records = load_records(path)
        while True:
            print("\nFile CRUD: 1 Add  2 View  3 Update  4 Delete  5 Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                try:
                    record_id = int(input("Record ID: "))
                    if any(record["id"] == record_id for record in records):
                        print("That record ID already exists.")
                        continue
                    name = input("Name: ").strip()
                    age = int(input("Age: "))
                    marks = float(input("Marks (0-100): "))
                    if not name or age < 0 or not 0 <= marks <= 100:
                        print("Enter a name and valid age and marks.")
                        continue
                    records.append({"id": record_id, "name": name, "age": age, "marks": marks})
                    save_records(path, records)
                    print("Record added.")
                except ValueError as error:
                    print(f"Invalid record input: {error}")
            elif choice == "2":
                if records:
                    for record in records:
                        print(record)
                else:
                    print("No records found.")
            elif choice == "3":
                try:
                    record_id = int(input("Record ID to update: "))
                    record = next((item for item in records if item["id"] == record_id), None)
                    if record is None:
                        print("No record has that ID.")
                        continue
                    name = input("New name: ").strip()
                    age = int(input("New age: "))
                    marks = float(input("New marks (0-100): "))
                    if not name or age < 0 or not 0 <= marks <= 100:
                        print("Enter a name and valid age and marks.")
                        continue
                    record.update({"name": name, "age": age, "marks": marks})
                    save_records(path, records)
                    print("Record updated.")
                except ValueError as error:
                    print(f"Invalid record input: {error}")
            elif choice == "4":
                try:
                    record_id = int(input("Record ID to delete: "))
                    if not any(record["id"] == record_id for record in records):
                        print("No record has that ID.")
                        continue
                    if input("Type DELETE to confirm removing this record: ") != "DELETE":
                        print("Cancelled; no record was deleted.")
                        continue
                    records = [record for record in records if record["id"] != record_id]
                    save_records(path, records)
                    print("Record deleted.")
                except ValueError as error:
                    print(f"Enter a valid whole-number ID: {error}")
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Choose a number from 1 to 5.")
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Could not load or update the records file: {error}")


if __name__ == "__main__":
    main()
