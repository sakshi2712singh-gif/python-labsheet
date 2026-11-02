import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Ask for an input CSV and a new destination file.
    source_name = input("Source CSV [sample_students.csv]: ").strip() or "sample_students.csv"
    destination_name = input("Destination CSV [copied_students.csv]: ").strip() or "copied_students.csv"
    source = resolve_path(source_name)
    destination = resolve_path(destination_name)

    try:
        # Parse and rewrite CSV rows so the copy remains valid CSV data.
        if source.resolve() == destination.resolve():
            print("Source and destination must be different files.")
            return
        with source.open("r", newline="", encoding="utf-8") as source_file:
            rows = list(csv.reader(source_file))
        with destination.open("x", newline="", encoding="utf-8") as destination_file:
            csv.writer(destination_file).writerows(rows)
        print(f"Copied {len(rows) - 1 if rows else 0} data row(s) to {destination.name}.")
    except FileExistsError:
        print("The destination already exists; choose another filename.")
    except OSError as error:
        print(f"Could not copy the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
