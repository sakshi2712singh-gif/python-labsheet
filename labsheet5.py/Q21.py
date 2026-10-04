# Q21: Write a program to create a nested tuple and access its elements.
first_row = tuple(input("Enter the first row's items: ").split())
second_row = tuple(input("Enter the second row's items: ").split())
nested = (first_row, second_row)
print("Nested tuple:", nested)

row = int(input("Enter row index (0 or 1): "))
column = int(input("Enter item index: "))

if 0 <= row < len(nested) and 0 <= column < len(nested[row]):
    print("Element:", nested[row][column])
else:
    print("Index is out of range.")