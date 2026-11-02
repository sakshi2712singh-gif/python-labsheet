from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Read a text file whose name may be relative to this script.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # split() treats consecutive spaces and line breaks as one separator.
        word_count = len(path.read_text(encoding="utf-8").split())
        print(f"Word count: {word_count}")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
