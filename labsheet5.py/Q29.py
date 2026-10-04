# Q29: Write a program to check if all elements in a tuple are the same.
values = tuple(input("Enter tuple items separated by spaces: ").split())

if len(values) > 0 and all(item == values[0] for item in values):
    print("All elements are the same.")
else:
    print("The elements are not all the same.")