import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Choose the source, the word pair, and a separate output file.
    source_name = input("Source filename [sample_text.txt]: ").strip() or "sample_text.txt"
    old_word = input("Word to replace [fox]: ").strip() or "fox"
    new_word = input("Replacement word [wolf]: ").strip() or "wolf"
    output_name = input("Output filename [replaced_text.txt]: ").strip() or "replaced_text.txt"
    source = resolve_path(source_name)
    output = resolve_path(output_name)
    if not old_word:
        print("Enter a word to replace.")
        return
    if source.resolve() == output.resolve():
        print("Choose a different output file so the source remains unchanged.")
        return

    try:
        # Replace whole-word matches and save the result separately.
        content = source.read_text(encoding="utf-8")
        updated = re.sub(rf"\b{re.escape(old_word)}\b", new_word, content)
        with output.open("x", encoding="utf-8") as file:
            file.write(updated)
        print(f"Saved the replaced text to {output.name}; the source was not changed.")
    except FileExistsError:
        print("The output file already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not process the file: {error}")


if __name__ == "__main__":
    main()
