import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Ask for a CSV file and default to the included student example.
    filename = input("CSV filename [sample_students.csv]: ").strip() or "sample_students.csv"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # DictReader uses the first row as the field names.
        with path.open("r", newline="", encoding="utf-8") as file:
            for record in csv.DictReader(file):
                print(record)
    except OSError as error:
        print(f"Could not read the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
