import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Open the selected CSV and confirm the requested columns are present.
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
            # Display only the requested fields from each student record.
            print(f"{'Name':<20} Marks")
            for record in reader:
                print(f"{(record.get('Name') or ''):<20} {record.get('Marks', '')}")
    except OSError as error:
        print(f"Could not read the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
