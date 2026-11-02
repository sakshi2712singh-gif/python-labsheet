import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Select a text source and an independent output file.
    source_name = input("Source filename [sample_text.txt]: ").strip() or "sample_text.txt"
    output_name = input("Output filename [unique_words.txt]: ").strip() or "unique_words.txt"
    source = resolve_path(source_name)
    output = resolve_path(output_name)
    if source.resolve() == output.resolve():
        print("Choose a different output file so the source remains unchanged.")
        return

    try:
        # Preserve each word's first spelling while comparing without letter case.
        words = re.findall(r"\b\w+\b", source.read_text(encoding="utf-8"))
        unique_words = []
        seen = set()
        for word in words:
            key = word.casefold()
            if key not in seen:
                seen.add(key)
                unique_words.append(word)
        with output.open("x", encoding="utf-8") as file:
            file.write("\n".join(unique_words) + ("\n" if unique_words else ""))
        print(f"Saved {len(unique_words)} unique word(s) to {output.name}.")
    except FileExistsError:
        print("The output file already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not process the file: {error}")


if __name__ == "__main__":
    main()
