from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Resolve the selected text file relative to this program by default.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # Keep each line's original text while measuring without its line ending.
        with path.open("r", encoding="utf-8") as file:
            lines = file.read().splitlines()
        if not lines:
            print("The file is empty.")
            return
        line_number, longest = max(enumerate(lines, start=1), key=lambda item: len(item[1]))
        print(f"Longest line ({len(longest)} characters, line {line_number}):")
        print(longest)
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
