import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Keep the sorted result separate from the original text.
    source_name = input("Source filename [sample_text.txt]: ").strip() or "sample_text.txt"
    output_name = input("Output filename [sorted_words.txt]: ").strip() or "sorted_words.txt"
    source = resolve_path(source_name)
    output = resolve_path(output_name)
    if source.resolve() == output.resolve():
        print("Choose a different output file so the source remains unchanged.")
        return

    try:
        # Sort words alphabetically without case affecting their order.
        words = re.findall(r"\b\w+\b", source.read_text(encoding="utf-8"))
        words.sort(key=str.casefold)
        with output.open("x", encoding="utf-8") as file:
            file.write("\n".join(words) + ("\n" if words else ""))
        print(f"Saved {len(words)} sorted word(s) to {output.name}.")
    except FileExistsError:
        print("The output file already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not process the file: {error}")


if __name__ == "__main__":
    main()
