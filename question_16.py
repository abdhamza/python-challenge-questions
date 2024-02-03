# 16) Write a Python program that asks the user to enter a number. 
# The program should then use an if-else statement to print whether the number is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
