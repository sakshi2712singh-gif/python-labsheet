def main():
    # Prepare a sample list and request the roll number to remove.
    students = [
        {"roll_no": 101, "name": "Asha", "age": 20, "marks": 88.0},
        {"roll_no": 102, "name": "Ravi", "age": 21, "marks": 76.0},
        {"roll_no": 103, "name": "Mina", "age": 19, "marks": 92.0},
    ]
    try:
        roll_no = int(input("Roll number to delete [102]: ") or "102")
    except ValueError:
        print("Enter a valid whole-number roll number.")
        return
    # Remove the matching in-memory record without changing any source file.
    remaining = [student for student in students if student["roll_no"] != roll_no]
    if len(remaining) == len(students):
        print(f"No student has roll number {roll_no}.")
    else:
        students = remaining
        print(f"Removed roll number {roll_no}. Remaining students:")
        for student in students:
            print(student)


if __name__ == "__main__":
    main()
