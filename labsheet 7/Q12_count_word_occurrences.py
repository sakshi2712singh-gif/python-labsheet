import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Ask which complete word and file to count.
    filename = input("Text filename [sample_text.txt]: ").strip() or "sample_text.txt"
    word = input("Word to count [fox]: ").strip() or "fox"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path
    if not word:
        print("Enter a word to count.")
        return

    try:
        # Count whole-word matches so a word inside a longer word is not counted.
        content = path.read_text(encoding="utf-8")
        count = len(re.findall(rf"\b{re.escape(word)}\b", content, re.IGNORECASE))
        print(f"{word!r} occurs {count} time(s).")
    except OSError as error:
        print(f"Could not read the file: {error}")


if __name__ == "__main__":
    main()
