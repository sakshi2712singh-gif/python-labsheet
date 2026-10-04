# Find the square and cube of a number

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)





# Calculate the area of a rectangle

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of the rectangle =", area)







# Calculate the perimeter of a circle

import math

radius = float(input("Enter the radius of the circle: "))

perimeter = 2 * math.pi * radius

print("Perimeter of the circle =", perimeter)








# Swap two variables using a temporary variable

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Before swapping: a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, "b =", b)






# Swap two variables without using a temporary variable

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Before swapping: a =", a, "b =", b)

a, b = b, a

print("After swapping: a =", a, "b =", b)







# Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (9 / 5) * celsius + 32

print("Temperature in Fahrenheit =", fahrenheit)






# Convert Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Temperature in Celsius =", celsius)






# Calculate simple interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)






# 13. Calculate Compound Interest

P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))

CI = P * (1 + R / 100) ** T - P

print("Compound Interest =", CI)






# 14. Calculate average of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average =", average)






# 15. Convert kilometers to miles

kilometers = float(input("Enter distance in kilometers: "))

miles = kilometers * 0.621371

print("Distance in miles =", miles)






# 16. Find the remainder

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 != 0:
    remainder = num1 % num2
    print("Remainder =", remainder)
else:
    print("Division by zero is not allowed.")







    # 17. Calculate power without using pow()

base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = base ** exponent

print("Power =", result)








# 19. Calculate monthly EMI

P = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure in years: "))

r = annual_rate / (12 * 100)
n = years * 12

if P > 0 and years > 0 and annual_rate >= 0:
    if r == 0:
        emi = P / n
    else:
        emi = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)

    print("Monthly EMI =", round(emi, 2))
else:
    print("Enter valid loan details.")







 # 20. Calculate percentage of five subjects

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))
m4 = float(input("Enter marks in subject 4: "))
m5 = float(input("Enter marks in subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print("Total marks =", total)
print("Percentage =", percentage, "%")








# 22. Check even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")







   # 23. Check divisibility by 5

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")







    # 24. Check leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")








    # 25. Find the largest of two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("The largest number is:", a)
elif b > a:
    print("The largest number is:", b)
else:
    print("Both numbers are equal.")








# 26. Find the largest of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)








# 27. Check vowel or consonant

ch = input("Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet character.")
elif ch.lower() in "aeiou":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")







# 28. Check uppercase, lowercase, or digit

ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
elif ch.isupper():
    print("The character is uppercase.")
elif ch.islower():
    print("The character is lowercase.")
elif ch.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")







# 29. Check if a number is in a given range

num = float(input("Enter a number: "))
start = float(input("Enter the starting value: "))
end = float(input("Enter the ending value: "))

if start > end:
    print("Invalid range.")
elif start <= num <= end:
    print("The number is within the given range.")
else:
    print("The number is outside the given range.")







# 30. Check prime number

num = int(input("Enter a number: "))

if num <= 1:
    print("The number is not prime.")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")












     

