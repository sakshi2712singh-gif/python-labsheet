# Q11: Create a dictionary of student names and marks and display it.

students = {}
count = int(input("How many students? "))

for index in range(count):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("Student marks:", students)