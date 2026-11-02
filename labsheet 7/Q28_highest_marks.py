import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Read each student name and mark from the selected CSV file.
    filename = input("CSV filename [sample_students.csv]: ").strip() or "sample_students.csv"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames or not {"Name", "Marks"}.issubset(reader.fieldnames):
                print("The CSV needs Name and Marks columns in its header.")
                return
            students = []
            for record in reader:
                students.append((record["Name"], float(record["Marks"])))
        # Show all students tied for the highest mark.
        if not students:
            print("The CSV contains no student records.")
            return
        highest = max(mark for _, mark in students)
        print(f"Highest marks: {highest:g}")
        for name, mark in students:
            if mark == highest:
                print(name)
    except ValueError as error:
        print(f"A marks value is not numeric: {error}")
    except OSError as error:
        print(f"Could not read the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
