# Q4: Write a program to access tuple elements using indexing.
values = tuple(input("Enter tuple items separated by spaces: ").split())
index = int(input("Enter an index (starting at 0): "))

if -len(values) <= index < len(values):
    print("Element:", values[index])
else:
    print("Index is out of range.")