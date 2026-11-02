def main():
    # Prepare sample records and request a roll number and new marks.
    students = [
        {"roll_no": 101, "name": "Asha", "age": 20, "marks": 88.0},
        {"roll_no": 102, "name": "Ravi", "age": 21, "marks": 76.0},
        {"roll_no": 103, "name": "Mina", "age": 19, "marks": 92.0},
    ]
    try:
        roll_no = int(input("Roll number to update [102]: ") or "102")
        marks = float(input("New marks (0-100): "))
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")
    except ValueError as error:
        print(f"Invalid input: {error}")
        return
    # Update the matching in-memory record only.
    for student in students:
        if student["roll_no"] == roll_no:
            student["marks"] = marks
            print(f"Updated {student['name']}: {student['marks']:g} marks.")
            return
    print(f"No student has roll number {roll_no}.")


if __name__ == "__main__":
    main()
