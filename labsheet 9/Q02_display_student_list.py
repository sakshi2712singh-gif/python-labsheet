def main():
    # Prepare a sample list of student records for the read operation.
    students = [
        {"roll_no": 101, "name": "Asha", "age": 20, "marks": 88.0},
        {"roll_no": 102, "name": "Ravi", "age": 21, "marks": 76.0},
        {"roll_no": 103, "name": "Mina", "age": 19, "marks": 92.0},
    ]
    # Print each student so every field can be checked.
    if not students:
        print("No student records found.")
        return
    for student in students:
        print(
            f"Roll: {student['roll_no']}, Name: {student['name']}, "
            f"Age: {student['age']}, Marks: {student['marks']:g}"
        )


if __name__ == "__main__":
    main()
