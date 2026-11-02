from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def resolve_path(filename):
    path = Path(filename)
    return path if path.is_absolute() else BASE_DIR / path


def main():
    # Ask for the source and a new destination file.
    source_name = input("Source filename [sample_text.txt]: ").strip() or "sample_text.txt"
    destination_name = input("Destination filename [copied_text.txt]: ").strip() or "copied_text.txt"
    source = resolve_path(source_name)
    destination = resolve_path(destination_name)

    try:
        # Copy text using exclusive creation so an existing destination is preserved.
        if source.resolve() == destination.resolve():
            print("Source and destination must be different files.")
            return
        with source.open("r", encoding="utf-8") as source_file:
            with destination.open("x", encoding="utf-8") as destination_file:
                destination_file.write(source_file.read())
        print(f"Copied {source.name} to {destination.name}.")
    except FileExistsError:
        print("The destination already exists; choose another filename.")
    except OSError as error:
        print(f"Could not copy the file: {error}")


if __name__ == "__main__":
    main()
