# 48) Write a program that asks the user to enter a non-negative integer and 
# uses a while loop to calculate its factorial.

# Ask the user to enter a non-negative integer
n = int(input("Enter a non-negative integer: "))

# Initialize the factorial result to 1 (the factorial of 0 is 1)
factorial = 1

# Use a while loop to calculate the factorial
if n >= 0:
    current_number = n
    while current_number > 1:
        factorial *= current_number
        current_number -= 1

    # Print the factorial
    print(f"The factorial of {n} is {factorial}.")
else:
    print("Please enter a non-negative integer.")
