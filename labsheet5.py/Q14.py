# Q14: Write a program to calculate the sum of numeric elements in a tuple.
values = tuple(map(float, input("Enter numbers separated by spaces: ").split()))
print("Sum:", sum(values))