# Q1: Find the sum and average of elements in a list.

numbers = [float(value) for value in input("Enter numbers separated by spaces: ").split()]

if len(numbers) == 0:
    print("The list is empty.")
else:
    total = sum(numbers)
    average = total / len(numbers)
    print("Sum:", total)
    print("Average:", average)