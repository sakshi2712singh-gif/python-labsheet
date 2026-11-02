def main():
    # Store employee records by unique employee ID.
    employees = {
        1: {"name": "Asha", "department": "Accounts", "salary": 42000.0},
        2: {"name": "Ravi", "department": "IT", "salary": 50000.0},
    }
    while True:
        # Show the available dictionary CRUD actions.
        print("\nEmployee CRUD: 1 Add  2 View  3 Update  4 Delete  5 Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                employee_id = int(input("Employee ID: "))
                if employee_id in employees:
                    print("That employee ID already exists.")
                    continue
                name = input("Employee name: ").strip()
                department = input("Department: ").strip()
                salary = float(input("Salary: "))
                if not name or not department or salary < 0:
                    print("Enter a name, department, and non-negative salary.")
                    continue
                employees[employee_id] = {
                    "name": name, "department": department, "salary": salary
                }
                print("Employee added.")
            elif choice == "2":
                for employee_id, employee in sorted(employees.items()):
                    print(f"{employee_id}: {employee}")
                if not employees:
                    print("No employees found.")
            elif choice == "3":
                employee_id = int(input("Employee ID to update: "))
                if employee_id not in employees:
                    print("No employee has that ID.")
                    continue
                name = input("New name: ").strip()
                department = input("New department: ").strip()
                salary = float(input("New salary: "))
                if not name or not department or salary < 0:
                    print("Enter a name, department, and non-negative salary.")
                    continue
                employees[employee_id] = {
                    "name": name, "department": department, "salary": salary
                }
                print("Employee updated.")
            elif choice == "4":
                employee_id = int(input("Employee ID to delete: "))
                if employees.pop(employee_id, None) is None:
                    print("No employee has that ID.")
                else:
                    print("Employee deleted.")
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Choose a number from 1 to 5.")
        except ValueError as error:
            print(f"Invalid numeric input: {error}")


if __name__ == "__main__":
    main()
