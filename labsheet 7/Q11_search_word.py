import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Read a search term and the relative text file to inspect.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    word = input("Word to search for [fox]: ").strip() or "fox"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path
    if not word:
        print("Enter a word to search for.")
        return

    try:
        # Match complete words without regard to letter case.
        found = False
        pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
        with path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if pattern.search(line):
                    print(f"Found on line {line_number}: {line}", end="" if line.endswith("\n") else "\n")
                    found = True
        if not found:
            print(f"The word {word!r} was not found.")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
