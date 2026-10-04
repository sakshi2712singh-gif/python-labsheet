# Q7: Write a program to count the occurrences of an element in a tuple.
values = tuple(input("Enter tuple items separated by spaces: ").split())
item = input("Enter the item to count: ")
print("Occurrences:", values.count(item))