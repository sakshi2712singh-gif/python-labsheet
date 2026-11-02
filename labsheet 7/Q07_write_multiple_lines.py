from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def main():
    # Collect lines until the user submits an empty line.
    filename = input("Output filename [multiple_lines.txt]: ").strip() or "multiple_lines.txt"
    path = Path(filename)
    if not path.is_absolute():
        path = BASE_DIR / path
    print("Enter lines of text; submit an empty line to finish.")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    try:
        # Create a new file without overwriting earlier work.
        with path.open("x", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
        print(f"Wrote {len(lines)} lines to {path.name}.")
    except FileExistsError:
        print("That file already exists; choose a different filename.")
    except OSError as error:
        print(f"Could not write the file: {error}")


if __name__ == "__main__":
    main()
