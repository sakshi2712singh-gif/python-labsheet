# Q2: Rotate a list by n positions.

numbers = input("Enter list items separated by spaces: ").split()
positions = int(input("Enter the number of positions to rotate: "))
direction = input("Rotate left or right? ").lower()

if numbers:
    positions = positions % len(numbers)
    if direction == "left":
        rotated = numbers[positions:] + numbers[:positions]
    else:
        rotated = numbers[-positions:] + numbers[:-positions] if positions else numbers
    print("Rotated list:", rotated)
else:
    print("The list is empty.")