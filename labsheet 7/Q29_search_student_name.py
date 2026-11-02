import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Ask which CSV and student name to search.
    filename = input("CSV filename [sample_students.csv]: ").strip() or "sample_students.csv"
    name = input("Student name to search [Asha]: ").strip() or "Asha"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # Compare names without regard to letter case and display matching rows.
        found = False
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames or "Name" not in reader.fieldnames:
                print("The CSV needs a Name column in its header.")
                return
            for record in reader:
                if (record.get("Name") or "").strip().casefold() == name.casefold():
                    print(record)
                    found = True
        if not found:
            print(f"No student named {name!r} was found.")
    except OSError as error:
        print(f"Could not read the CSV: {error}")
    except csv.Error as error:
        print(f"Invalid CSV data: {error}")


if __name__ == "__main__":
    main()
