# Q16: Write a program to sort a tuple of strings alphabetically.
words = tuple(input("Enter words separated by spaces: ").split())
sorted_words = tuple(sorted(words))
print("Sorted tuple:", sorted_words)