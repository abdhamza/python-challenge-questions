# 16) Ask the user to input two numbers. Use an if-else statement to determine which number is larger, or if they are equal, 
# and print an appropriate message for each case.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"The larger number is {num1}")
elif num2 > num1:
    print(f"The larger number is {num2}")
else:
    print("Both numbers are equal")
