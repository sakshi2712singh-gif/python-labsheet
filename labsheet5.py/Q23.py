# Q23: Write a program to swap two tuples.
first = tuple(input("Enter the first tuple's items: ").split())
second = tuple(input("Enter the second tuple's items: ").split())
first, second = second, first
print("First tuple after swapping:", first)
print("Second tuple after swapping:", second)