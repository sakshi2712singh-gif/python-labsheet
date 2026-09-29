# Q1_palindrome.py

s = input("Enter a string: ")

reverse = ""
for ch in s:
    reverse = ch + reverse

if s == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")








 # Q2_vowels_consonants.py

s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
           ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)








# Q3_replace_spaces.py

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == " ":
        result += "_"
    else:
        result += ch

print("Result:", result)







# Q4_uppercase.py

s = input("Enter a string: ")

result = ""

for ch in s:
    if 'A' <= ch <= 'Z':
        result += ch

print("Uppercase characters:", result)








# Q5_remove_duplicates.py

s = input("Enter a string: ")

result = ""

for ch in s:
    found = False

    for r in result:
        if ch == r:
            found = True
            break

    if not found:
        result += ch

print("String after removing duplicates:", result)











# Q6_character_frequency.py

s = input("Enter a string: ")

visited = ""

for ch in s:
    if ch not in visited:
        count = 0

        for x in s:
            if x == ch:
                count += 1

        print(ch, ":", count)
        visited += ch









   # Q7_reverse_string.py

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print("Reversed string:", reverse)









# Q8_title_case.py

s = input("Enter a string: ")

result = ""
new_word = True

for ch in s:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            if 'a' <= ch <= 'z':
                ch = chr(ord(ch) - 32)
            new_word = False
        else:
            if 'A' <= ch <= 'Z':
                ch = chr(ord(ch) + 32)

        result += ch

print("Title case:", result)










# Q9_word_count.py

s = input("Enter a string: ")

count = 0
inside_word = False

for ch in s:
    if ch != " ":
        if not inside_word:
            count += 1
            inside_word = True
    else:
        inside_word = False

print("Number of words:", count)












# Q10_longest_word.py

s = input("Enter a string: ")

word = ""
longest = ""

for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

print("Longest word:", longest)








# Q11_anagram.py

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Strings are not anagrams.")
else:
    visited = ""
    anagram = True

    for ch in s1:
        if ch not in visited:
            count1 = 0
            count2 = 0

            for x in s1:
                if x == ch:
                    count1 += 1

            for x in s2:
                if x == ch:
                    count2 += 1

            if count1 != count2:
                anagram = False
                break

            visited += ch

    if anagram:
        print("Strings are anagrams.")
    else:
        print("Strings are not anagrams.")








 # Q12_substring.py

s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring exists in the string.")
else:
    print("Substring does not exist.")








# Q13_vowels_upper_consonants_lower.py

s = input("Enter a string: ")

result = ""

for ch in s:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':

        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or \
           ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':

            if 'a' <= ch <= 'z':
                ch = chr(ord(ch) - 32)

        else:
            if 'A' <= ch <= 'Z':
                ch = chr(ord(ch) + 32)

    result += ch

print("Result:", result)









# Q14_remove_punctuation.py

s = input("Enter a string: ")

punctuation = ".,!?;:'\"-()[]{}"

result = ""

for ch in s:
    if ch not in punctuation:
        result += ch

print("After removing punctuation:", result)










# Q15_first_non_repeated.py

s = input("Enter a string: ")

found = False

for ch in s:
    count = 0

    for x in s:
        if x == ch:
            count += 1

    if count == 1:
        print("First non-repeated character:", ch)
        found = True
        break

if not found:
    print("No non-repeated character found.")








    # Q16_count_characters.py

s = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0

for ch in s:
    if '0' <= ch <= '9':
        digits += 1
    elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        alphabets += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special characters:", special)








# Q17_all_substrings.py

s = input("Enter a string: ")

print("All substrings:")

for i in range(len(s)):
    substring = ""

    for j in range(i, len(s)):
        substring += s[j]
        print(substring)
        \






 # Q18_sort_characters.py

s = input("Enter a string: ")

characters = []

for ch in s:
    characters.append(ch)

# Bubble sort
for i in range(len(characters)):
    for j in range(0, len(characters) - i - 1):
        if characters[j] > characters[j + 1]:
            temp = characters[j]
            characters[j] = characters[j + 1]
            characters[j + 1] = temp

result = ""

for ch in characters:
    result += ch

print("Sorted string:", result)












# Q19_most_repeated_word.py

s = input("Enter a sentence: ")

words = s.split()

most_word = ""
max_count = 0

for word in words:
    count = 0

    for w in words:
        if word == w:
            count += 1

    if count > max_count:
        max_count = count
        most_word = word

print("Most repeated word:", most_word)
print("Frequency:", max_count)









# Q20_string_rotation.py

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Strings are not rotations.")
else:
    combined = s1 + s1

    if s2 in combined:
        print("Strings are rotations of each other.")
    else:
        print("Strings are not rotations.")







    # Q21_largest_smallest.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest element:", largest)
print("Smallest element:", smallest)  







# Q22_sort_list.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Ascending order
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Ascending order:", numbers)

# Descending order
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Descending order:", numbers)









# Q23_remove_duplicates.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = []

for num in numbers:
    found = False

    for x in result:
        if num == x:
            found = True
            break

    if not found:
        result.append(num)

print("List after removing duplicates:", result)









# Q24_reverse_list.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

left = 0
right = len(numbers) - 1

while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

    left += 1
    right -= 1

print("Reversed list:", numbers)









# Q25_list_frequency.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

visited = []

for num in numbers:
    if num not in visited:
        count = 0

        for x in numbers:
            if x == num:
                count += 1

        print(num, ":", count)
        visited.append(num)









        # Q26_merge_lists.py

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged = []

for item in list1:
    merged.append(item)

for item in list2:
    merged.append(item)

print("Merged list:", merged)










# Q27_second_largest.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = None
second = None

for num in numbers:
    if largest is None or num > largest:
        second = largest
        largest = num
    elif num != largest and (second is None or num > second):
        second = num

if second is None:
    print("Second largest element does not exist.")
else:
    print("Second largest element:", second)










    # Q28_common_elements.py

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = []

for x in list1:
    if x in list2 and x not in common:
        common.append(x)

print("Common elements:", common)








# Q29_difference_lists.py

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

difference = []

for x in list1:
    if x not in list2:
        difference.append(x)

print("Elements present in first list but not in second:", difference)










# Q30_even_odd.py

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)







