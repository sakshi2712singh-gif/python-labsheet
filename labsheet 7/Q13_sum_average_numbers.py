from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Read a file containing numbers separated by spaces, commas, or newlines.
    filename = input("Numbers filename [sample_numbers.txt]: ").strip() or "sample_numbers.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        content = path.read_text(encoding="utf-8")
        numbers = [float(item) for item in content.replace(",", " ").split()]
        if not numbers:
            print("The file contains no numbers.")
            return
        # Calculate the total and average from the parsed numeric values.
        total = sum(numbers)
        print(f"Sum: {total:g}")
        print(f"Average: {total / len(numbers):g}")
    except ValueError as error:
        print(f"The file contains a value that is not a number: {error}")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
