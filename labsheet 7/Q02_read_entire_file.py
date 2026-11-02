from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Use the supplied sample when no relative filename is entered.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path

    try:
        # Read the complete file with an explicit text encoding.
        content = path.read_text(encoding="utf-8")
        print(content, end="" if content.endswith("\n") else "\n")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
