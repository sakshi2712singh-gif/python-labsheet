from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Ask for a file to append to, and a single line of new content.
    filename = input("Existing filename [append_target.txt]: ").strip() or "append_target.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path
    addition = input("Content to append: ")

    try:
        # Check that the input really exists before opening in append mode.
        if not path.is_file():
            print("The file does not exist; create it before appending.")
            return
        with path.open("a", encoding="utf-8") as file:
            file.write(addition + "\n")
        print(f"Appended content to {path.name}.")
    except OSError as error:
        print(f"Could not append to the file: {error}")


if __name__ == "__main__":
    main()
