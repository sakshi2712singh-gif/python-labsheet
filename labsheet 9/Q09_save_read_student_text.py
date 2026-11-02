import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Collect student records to store in a readable text-based CSV file.
    try:
        count = int(input("Number of students to save: "))
        if count < 0:
            print("Enter zero or a positive number.")
            return
        records = []
        for index in range(count):
            print(f"Student {index + 1}")
            roll_no = int(input("Roll number: "))
            name = input("Name: ").strip()
            age = int(input("Age: "))
            marks = float(input("Marks (0-100): "))
            if not name or age < 0 or not 0 <= marks <= 100:
                raise ValueError("Student name, age, or marks is invalid.")
            records.append([roll_no, name, age, marks])
        filename = input("Output text filename [students.txt]: ").strip() or "students.txt"
        path = Path(filename)
        if not path.is_absolute():
            path = BASE_DIR / path
        # Create a new text file and write each record as a CSV row.
        with path.open("x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["roll_no", "name", "age", "marks"])
            writer.writerows(records)
        # Open the saved file again and display the stored data.
        print("Saved records:")
        with path.open("r", newline="", encoding="utf-8") as file:
            for record in csv.DictReader(file):
                print(record)
    except ValueError as error:
        print(f"Invalid student input: {error}")
    except FileExistsError:
        print("That output file already exists; choose a different name.")
    except OSError as error:
        print(f"Could not save or read the student file: {error}")


if __name__ == "__main__":
    main()
