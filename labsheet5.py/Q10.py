# Q10: Write a program to repeat a tuple n times
values = tuple(input("Enter tuple items separated by spaces: ").split())
times = int(input("Enter the number of repetitions: "))
print("Repeated tuple:", values * times)