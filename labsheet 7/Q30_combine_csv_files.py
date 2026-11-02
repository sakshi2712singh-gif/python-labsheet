import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Accept a comma-separated list of CSV filenames and an output filename.
    names = input(
        "Input CSV filenames [sample_students.csv,sample_students_2.csv]: "
    ).strip() or "sample_students.csv,sample_students_2.csv"
    sources = [resolve_path(name.strip()) for name in names.split(",") if name.strip()]
    output_name = input("Output CSV filename [combined_students.csv]: ").strip() or "combined_students.csv"
    output = resolve_path(output_name)
    if not sources:
        print("Enter at least one input CSV.")
        return
    if any(source.resolve() == output.resolve() for source in sources):
        print("Choose an output file different from all input files.")
        return

    try:
        # Read all records first and require matching headers across files.
        combined_rows = []
        expected_header = None
        for source in sources:
            with source.open("r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                if header is None:
                    raise ValueError(f"{source.name} is empty.")
                if expected_header is None:
                    expected_header = header
                elif header != expected_header:
                    raise ValueError(f"{source.name} has different columns.")
                combined_rows.extend(reader)
        with output.open("x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(expected_header)
            writer.writerows(combined_rows)
        print(f"Combined {len(combined_rows)} row(s) from {len(sources)} file(s) into {output.name}.")
    except FileExistsError:
        print("The output CSV already exists; choose a different filename.")
    except (OSError, ValueError, csv.Error) as error:
        print(f"Could not combine the CSV files: {error}")


if __name__ == "__main__":
    main()
