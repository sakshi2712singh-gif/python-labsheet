import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Open a CSV file and read its header and data records.
    filename = input("CSV filename [sample_students.csv]: ").strip() or "sample_students.csv"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, [])
            row_count = sum(1 for _ in reader)
        # Count records without treating the header as a data row.
        print(f"Rows (excluding header): {row_count}")
        print(f"Columns: {len(header)}")
    except OSError as error:
        print(f"Could not read the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
