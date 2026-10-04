# Q28: Create a nested dictionary for student details (Name, Roll, Marks).

students = {}
count = int(input("How many students? "))

for index in range(count):
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[roll] = {"Name": name, "Roll": roll, "Marks": marks}

print("Student details:", students)