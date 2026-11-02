def main():
    # Build an in-memory list of student dictionaries.
    students = []
    try:
        count = int(input("How many students should be added? "))
        if count < 0:
            print("Enter zero or a positive number.")
            return
        for index in range(count):
            print(f"Student {index + 1}")
            roll_no = int(input("Roll number: "))
            name = input("Name: ").strip()
            age = int(input("Age: "))
            marks = float(input("Marks: "))
            if not name or age < 0 or not 0 <= marks <= 100:
                raise ValueError("Name, age, or marks is invalid.")
            if any(student["roll_no"] == roll_no for student in students):
                raise ValueError("Roll numbers must be unique.")
            students.append(
                {"roll_no": roll_no, "name": name, "age": age, "marks": marks}
            )
        print("Created student records:")
        for student in students:
            print(student)
    except ValueError as error:
        print(f"Invalid student input: {error}")


if __name__ == "__main__":
    main()
