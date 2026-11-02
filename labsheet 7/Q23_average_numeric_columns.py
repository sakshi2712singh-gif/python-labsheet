import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Load a header-based CSV and inspect each column for numeric values.
    filename = input("CSV filename [sample_students.csv]: ").strip() or "sample_students.csv"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames:
                print("The CSV must have a header row.")
                return
            records = list(reader)

        # Ignore empty cells, and report a column only when its data is numeric.
        found_numeric_column = False
        for column in reader.fieldnames:
            values = []
            is_numeric = True
            for record in records:
                cell = (record.get(column) or "").strip()
                if not cell:
                    continue
                try:
                    values.append(float(cell))
                except ValueError:
                    is_numeric = False
                    break
            if is_numeric and values:
                average = sum(values) / len(values)
                print(f"{column}: average = {average:g}")
                found_numeric_column = True
        if not found_numeric_column:
            print("No numeric columns were found.")
    except OSError as error:
        print(f"Could not read the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
