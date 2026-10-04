# Q8: Find pairs of numbers in a list whose sum is equal to a given number.

numbers = [int(value) for value in input("Enter numbers separated by spaces: ").split()]
target = int(input("Enter the target sum: "))

print("Pairs:")
found_pair = False
for first_index in range(len(numbers)):
    for second_index in range(first_index + 1, len(numbers)):
        if numbers[first_index] + numbers[second_index] == target:
            print(numbers[first_index], "and", numbers[second_index])
            found_pair = True

if not found_pair:
    print("No matching pairs found.")