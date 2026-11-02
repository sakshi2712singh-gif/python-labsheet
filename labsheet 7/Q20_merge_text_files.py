from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Ask for two input files and a separate destination.
    first_name = input("First filename [sample_text.txt]: ").strip() or "sample_text.txt"
    second_name = input("Second filename [second_text.txt]: ").strip() or "second_text.txt"
    output_name = input("Output filename [merged_text.txt]: ").strip() or "merged_text.txt"
    first = resolve_path(first_name)
    second = resolve_path(second_name)
    output = resolve_path(output_name)
    if output.resolve() in {first.resolve(), second.resolve()}:
        print("Choose an output file different from both inputs.")
        return

    try:
        # Read both sources before exclusively creating the merged output.
        first_text = first.read_text(encoding="utf-8")
        second_text = second.read_text(encoding="utf-8")
        separator = "" if not first_text or first_text.endswith("\n") else "\n"
        with output.open("x", encoding="utf-8") as file:
            file.write(first_text + separator + second_text)
        print(f"Merged the two files into {output.name}.")
    except FileExistsError:
        print("The output file already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not merge the files: {error}")


if __name__ == "__main__":
    main()
