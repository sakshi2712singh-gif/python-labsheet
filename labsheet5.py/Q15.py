# Q15: Write a program to sort a tuple of numbers in ascending order.
values = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_values = tuple(sorted(values))
print("Sorted tuple:", sorted_values)