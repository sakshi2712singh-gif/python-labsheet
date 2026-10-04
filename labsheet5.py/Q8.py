# Q8: Write a program to find the index of an element in a tuple.
values = tuple(input("Enter tuple items separated by spaces: ").split())
item = input("Enter the item to find: ")

if item in values:
    print("Index:", values.index(item))
else:
    print("The item is not in the tuple.")