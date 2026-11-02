from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Ask for a relative output filename and the text to save.
    filename = input("Output filename [created_text.txt]: ").strip() or "created_text.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path
    content = input("Enter text to write: ")

    try:
        # Exclusive mode prevents replacing an existing file by accident.
        with path.open("x", encoding="utf-8") as file:
            file.write(content + "\n")
        print(f"Text written to {path.name}.")
    except FileExistsError:
        print("That file already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not write the file: {error}")


if __name__ == "__main__":
    main()
