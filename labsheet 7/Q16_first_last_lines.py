from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Read all lines so both boundary lines can be selected.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        with path.open("r", encoding="utf-8") as file:
            lines = file.read().splitlines()
        if not lines:
            print("The file is empty.")
            return
        # The same line is both first and last for a one-line file.
        print(f"First line: {lines[0]}")
        print(f"Last line: {lines[-1]}")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
