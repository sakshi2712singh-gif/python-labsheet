# Q6: Write a program to check if an element exists in a tuple.
values = tuple(input("Enter tuple items separated by spaces: ").split())
item = input("Enter the item to find: ")

if item in values:
    print("The item exists in the tuple.")
else:
    print("The item does not exist in the tuple.")