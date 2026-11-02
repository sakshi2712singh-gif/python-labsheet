import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Create a CSV containing a header and example student records.
    filename = input("Output CSV filename [created_students.csv]: ").strip() or "created_students.csv"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path
    records = [
        ["Name", "Marks", "Age"],
        ["Asha", 88, 20],
        ["Ravi", 92, 21],
        ["Mina", 92, 19],
    ]

    try:
        # newline="" lets the csv module write correct line endings on every OS.
        with path.open("x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(records)
        print(f"Created {path.name} with {len(records) - 1} student record(s).")
    except FileExistsError:
        print("That CSV already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not create the CSV: {error}")


if __name__ == "__main__":
    main()
