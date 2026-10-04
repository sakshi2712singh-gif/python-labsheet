# Q25: Write a program to find the difference between two tuples.
first = tuple(input("Enter the first tuple's items: ").split())
second = tuple(input("Enter the second tuple's items: ").split())
difference = ()

for item in first:
    if item not in second and item not in difference:
        difference += (item,)

print("Items in the first tuple but not the second:", difference)