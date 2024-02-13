# 43) Write a Python program that simulates a login system where the user has up to 3 attempts to enter the correct password. 
# The program should ask for input each time and print "Access granted" if the correct password is entered, or "Access denied. Attempts exceeded" if the user fails all attempts. 
# Assume the correct password is a fixed string in your program.

# Set the correct password
correct_password = "password123"

# Initialize the number of attempts
attempts = 0

# Maximum number of attempts allowed
max_attempts = 3

# Use a while loop to allow up to 3 attempts
while attempts < max_attempts:
    # Ask the user to enter the password
    entered_password = input("Enter password: ")
    
    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Access granted")
        break  # Exit the loop if the password is correct
    else:
        print("Access denied. Try again.")
        attempts += 1  # Increment the attempt count

# Check if all attempts were used without success
if attempts == max_attempts:
    print("Access denied. Attempts exceeded")
