# Q30: Create a dictionary from a string with characters as keys and frequency as values.

text = input("Enter a string: ")
character_frequency = {}

for character in text:
    if character in character_frequency:
        character_frequency[character] += 1
    else:
        character_frequency[character] = 1

print("Character frequency dictionary:", character_frequency)