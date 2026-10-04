# Q24: Write a program to find common elements between two tuples.
first = tuple(input("Enter the first tuple's items: ").split())
second = tuple(input("Enter the second tuple's items: ").split())
common = ()

for item in first:
    if item in second and item not in common:
        common += (item,)

print("Common elements:", common)