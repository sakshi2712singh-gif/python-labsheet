# Q13: Write a program to find the maximum and minimum values in a tuple.
values = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum:", max(values))
print("Minimum:", min(values))