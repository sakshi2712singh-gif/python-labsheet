def main():
    # Prepare sample records and ask which student to find.
    students = [
        {"roll_no": 101, "name": "Asha", "age": 20, "marks": 88.0},
        {"roll_no": 102, "name": "Ravi", "age": 21, "marks": 76.0},
        {"roll_no": 103, "name": "Mina", "age": 19, "marks": 92.0},
    ]
    search_name = input("Student name to search [Asha]: ").strip() or "Asha"
    # Match the complete name without case sensitivity.
    matches = [
        student for student in students
        if student["name"].casefold() == search_name.casefold()
    ]
    if matches:
        for student in matches:
            print(student)
    else:
        print(f"No student named {search_name!r} was found.")


if __name__ == "__main__":
    main()
