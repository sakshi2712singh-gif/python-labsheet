from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Resolve relative filenames from this script's folder.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # Iterating over the open file reads one line at a time.
        with path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line}", end="" if line.endswith("\n") else "\n")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
