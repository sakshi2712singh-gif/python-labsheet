from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Use the text sample by default so the program is ready to run.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # Count newline characters too; they are part of the file's contents.
        content = path.read_text(encoding="utf-8")
        print(f"Lines: {len(content.splitlines())}")
        print(f"Characters (including line breaks): {len(content)}")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
