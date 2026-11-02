from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Select a source and a new destination to preserve the original file.
    source_name = input("Source filename [sample_text.txt]: ").strip() or "sample_text.txt"
    output_name = input("Output filename [nonblank_lines.txt]: ").strip() or "nonblank_lines.txt"
    source = resolve_path(source_name)
    output = resolve_path(output_name)
    if source.resolve() == output.resolve():
        print("Choose a different output file so the source remains unchanged.")
        return

    try:
        # Keep lines containing non-whitespace characters, including their endings.
        with source.open("r", encoding="utf-8") as source_file:
            lines = [line for line in source_file if line.strip()]
        with output.open("x", encoding="utf-8") as output_file:
            output_file.writelines(lines)
        print(f"Saved {len(lines)} nonblank line(s) to {output.name}.")
    except FileExistsError:
        print("The output file already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not process the file: {error}")


if __name__ == "__main__":
    main()
