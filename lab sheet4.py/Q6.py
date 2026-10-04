# Q6: Split a list into two halves.

items = input("Enter list items separated by spaces: ").split()
middle = len(items) // 2
first_half = items[:middle]
second_half = items[middle:]

print("First half:", first_half)
print("Second half:", second_half)