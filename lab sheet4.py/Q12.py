# Q12: Find the maximum and minimum marks from a dictionary.

marks = {}
count = int(input("How many students? "))

for index in range(count):
    name = input("Enter student name: ")
    marks[name] = float(input("Enter marks: "))

if marks:
    highest_name = max(marks, key=marks.get)
    lowest_name = min(marks, key=marks.get)
    print("Maximum marks:", marks[highest_name], "by", highest_name)
    print("Minimum marks:", marks[lowest_name], "by", lowest_name)
else:
    print("The dictionary is empty.")