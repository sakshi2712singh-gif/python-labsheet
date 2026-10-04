# 1. Check if a number is a multiple of both 3 and 7. 
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("The number is a multiple of both 3 and 7.")
else:
    print("The number is not a multiple of both 3 and 7.")






#2. Check if a number is a palindrome. 
    num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")



 #3. Check if a number is an Armstrong number. 
num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")



#4. Display a grade based on marks: • A: 90–100 • B: 75–89 • C: 50–74 • F: below 50 

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks <= 89:
    print("Grade: B")
elif marks >= 60 and marks <= 74:
    print("Grade: C")
elif marks >= 40 and marks <= 59:
    print("Grade: D")
elif marks >= 0 and marks <= 39:
    print("Grade: F")
else:
    print("Invalid marks.")   






#
num = float(input("Enter a number: "))

absolute_value = abs(num)

print("Absolute value:", absolute_value) 





#6. Check whether a triangle is valid given its angles. 
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")





#7. Determine the type of a triangle (equilateral, isosceles, scalene). 
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 == side2 == side3:
    print("The triangle is Equilateral.")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles.")

else:
    print("The triangle is Scalene.")



#8. Check if a string contains a particular substring. 
text = input("Enter a string: ")
substring = input("Enter the substring to search: ")

if substring in text:
    print("The substring is present.")
else:
    print("The substring is not present.")







#9. Check eligibility for voting. 
age = int(input("Enter your age: "))

if age >= 18:
    print("Result: You are eligible to vote!")
else:
    print(f"Result: Not eligible. Wait {18 - age} more year(s).")








#10. Find the smallest among three numbers. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

smallest = min(num1, num2, num3)
print(f"Result: The smallest number is {smallest}")




#11.  Print numbers from 1 to 10 using a for loop.
limit = int(input("Enter the limit (e.g., 10): "))

print("Result:")
for i in range(1, limit + 1):
    print(i)





        
#12. Print numbers from 10 to 1 using a while loop. 
start = int(input("Enter the starting number (e.g., 10): "))

print("Result:")
while start >= 1:
    print(start)
    start -= 1





#13. Print the sum of first n natural numbers. 
n = int(input("Enter a positive integer (n): "))

# use the arithetic progression formula
total_sum = ( n * (n + 1) )//2
print(f"Result: The sum of the first {n} natural numbers is {total_sum}")





#14. Print the multiplication table of a given number. 
num = int(input("Enter a number for its multiplication table: "))

print("Result:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")





#15. Print all even numbers between 1 and 50. 
input("Press Enter to print even numbers between 1 and 50: ")

print("Result:")
# range(start, stop, step) increments by 2 to get even numbers
for i in range(2, 51, 2):
    print(i, end=" ")
print()  # Move to a new line





#16. Print all odd numbers between 1 and 50. 
input("Press Enter to print odd numbers between 1 and 50: ")

print("Result:")
# Starts at 1 and increments by 2 to get odd numbers
for i in range(1, 51, 2):
    print(i, end=" ")
print()




#17. Find the factorial of a given number. 
import math

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Result: Factorial does not exist for negative numbers.")
else:
    fact = math.factorial(num)
    print(f"Result: The factorial of {num} is {fact}")







#18. Print Fibonacci series up to n terms.
n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

print("Result:")
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    while count < n:
        print(a, end=" ")
        nth = a + b
        # Update values
        a = b
        b = nth
        count += 1
    print()






#19. Reverse a number using a loop. 
num = int(input("Enter an integer to reverse: "))
reversed_num = 0
original_num = num

# Handle negative numbers
sign = -1 if num < 0 else 1
num = abs(num)

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

reversed_num *= sign
print(f"Result: The reversed number is {reversed_num}")





#20. Count the number of digits in a number. 
num = int(input("Enter a number: "))
count = 0

# Absolute value ensures it works for negative numbers
temp = abs(num)

# Special case for 0
if temp == 0:
    count = 1
else:
    while temp > 0:
        count += 1
        temp //= 10

print(f"Result: The number of digits is {count}")







#21. Find the sum of digits of a number. 
num = int(input("Enter a number: "))
digit_sum = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print(f"Result: The sum of digits is {digit_sum}")





#22. Print all prime numbers between 1 and 100. 
input("Press Enter to print prime numbers between 1 and 100: ")

print("Result:")
for num in range(2, 101):
    is_prime = True
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()







#23. Check if a number is perfect. 
num = int(input("Enter a number to check: "))
divisor_sum = 0

for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num and num > 0:
    print(f"Result: {num} is a perfect number.")
else:
    print(f"Result: {num} is not a perfect number.")








#24. Print a Pattern: 
rows = int(input("Enter the number of rows for the pattern: "))

print("Result:")
for i in range(1, rows + 1):
    print("*" * i)






#25. Print a reverse Pattern: * * * * * 
                #             * * * * 
                #             * * * 
                #             * * 
                #             * 
rows = int(input("Enter the number of rows: "))

print("Result:")
# Loop backwards from rows down to 1
for i in range(rows, 0, -1):
    print("* " * i)






#26. Print a pyramid pattern of numbers. 
rows = int(input("Enter the number of rows: "))

print("Result:")
for i in range(1, rows + 1):
    # Print leading spaces for alignment
    print(" " * (rows - i), end="")
    # Print numbers for the current row
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line






#27. Display the multiplication table from 1 to 10. 
input("Press Enter to display the multiplication tables (1 to 10): ")

print("Result:")
for i in range(1, 11):
    for j in range(1, 11):
        # :4 formats the output to take up 4 spaces for clean columns
        print(f"{i * j:4}", end="")
    print()









#28. Find the HCF of two numbers using a loop. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a, b = num1, num2
# Loop until the remainder becomes 0
while b != 0:
    a, b = b, a % b

print(f"Result: The HCF of {num1} and {num2} is {a}")






#29. Find the LCM of two numbers using a loop. 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Start checking from the maximum of the two numbers
lcm = max(num1, num2)

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1

print(f"Result: The LCM of {num1} and {num2} is {lcm}")










#30. Check if a number is strong (sum of factorial of digits equals the number). 
import math

num = int(input("Enter a number to check: "))
temp = num
factorial_sum = 0

# Extract digits and calculate the sum of their factorials
while temp > 0:
    digit = temp % 10
    factorial_sum += math.factorial(digit)
    temp //= 10

if factorial_sum == num:
    print(f"Result: {num} is a Strong number!")
else:
    print(f"Result: {num} is NOT a Strong number.")










