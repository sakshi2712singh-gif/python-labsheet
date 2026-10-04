# Q30: Write a program to find the element-wise sum of two tuples.
first = tuple(map(int, input("Enter the first tuple's numbers: ").split()))
second = tuple(map(int, input("Enter the second tuple's numbers: ").split()))

if len(first) == len(second):
    total = ()
    for index in range(len(first)):
        total += (first[index] + second[index],)
    print("Element-wise sum:", total)
else:
    print("The tuples must have the same length.")