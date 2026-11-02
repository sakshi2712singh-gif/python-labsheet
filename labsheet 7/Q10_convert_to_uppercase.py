from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Read a file chosen by the user or use the included text sample.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # Convert the complete contents before displaying the result.
        print(path.read_text(encoding="utf-8").upper(), end="\n")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
