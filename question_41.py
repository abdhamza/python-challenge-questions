# 41) Write a Python program that asks the user to enter a number and then reverses that number using a while loop. 
# For example, if the user enters 12345, the program should print 54321.

# Ask the user to enter a number
number = input("Enter a number: ")

# Convert the input to an integer
number = int(number)

# Initialize the reversed number to 0
reversed_number = 0

# Use a while loop to reverse the number
while number > 0:
    # Extract the last digit of the number
    digit = number % 10
    # Add the digit to the reversed number, adjusting its position
    reversed_number = reversed_number * 10 + digit
    # Remove the last digit from the number
    number = number // 10

# Print the reversed number
print(f"The reversed number is: {reversed_number}")
