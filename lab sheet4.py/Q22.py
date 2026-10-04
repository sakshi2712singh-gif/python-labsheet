# Q22: Create a dictionary with numbers as keys and their squares as values.

n = int(input("Enter n: "))
squares = {}

for number in range(1, n + 1):
    squares[number] = number ** 2

print("Number and square dictionary:", squares)