# Q10: Convert a list into a string without using join().

items = input("Enter list items separated by spaces: ").split()
result = ""

for index in range(len(items)):
    result += items[index]
    if index < len(items) - 1:
        result += ", "

print("String:", result)