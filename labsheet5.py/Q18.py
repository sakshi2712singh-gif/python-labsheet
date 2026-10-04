# Q18: Write a program to check if two tuples are equal.
first = tuple(input("Enter the first tuple's items: ").split())
second = tuple(input("Enter the second tuple's items: ").split())

if first == second:
    print("The tuples are equal.")
else:
    print("The tuples are not equal.")