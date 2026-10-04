# Q5: Create a list of squares of numbers from 1 to n.

n = int(input("Enter n: "))
squares = []

for number in range(1, n + 1):
    squares.append(number ** 2)

print("Squares:", squares)