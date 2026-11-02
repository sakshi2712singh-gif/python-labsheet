import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Select an existing CSV, then collect one student record.
    filename = input("Existing CSV filename [appendable_students.csv]: ").strip() or "appendable_students.csv"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path
    name = input("Student name: ").strip()
    marks_text = input("Marks (0-100): ").strip()
    try:
        marks = float(marks_text)
        if not name or not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Enter a non-empty name and marks between 0 and 100.")
        return

    try:
        # Check the existing header before appending a row in its column order.
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
        if not fieldnames or not {"Name", "Marks"}.issubset(fieldnames):
            print("The CSV needs Name and Marks columns in its header.")
            return
        with path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({"Name": name, "Marks": f"{marks:g}"})
        print(f"Added {name} to {path.name}.")
    except OSError as error:
        print(f"Could not append to the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
