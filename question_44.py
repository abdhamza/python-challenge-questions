# 44) Write a program that takes an integer input from the user and uses a while loop to count how many digits the number has. 
# For instance, if the user inputs 75869, the program should print that the number has 5 digits.

# Ask the user to input an integer
user_input = input("Enter an integer: ")

# Convert the input to an integer
number = int(user_input)

# Initialize the digit count to 0
digit_count = 0

# Use a while loop to count the digits
while number > 0:
    # Remove the last digit from the number
    number = number // 10
    # Increment the digit count
    digit_count += 1

# Print the number of digits
print(f"The number has {digit_count} digits.")
