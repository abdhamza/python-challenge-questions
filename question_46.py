# 46) Write a program that asks the user to enter a number and uses a 
# while loop to determine if it's a prime number.

# Ask the user to enter a number
number = int(input("Enter a number: "))

# A flag variable to indicate if the number is prime
is_prime = True

# Prime numbers are greater than 1
if number > 1:
    # Check for factors
    divisor = 2
    while divisor <= number // 2:
        if (number % divisor) == 0:
            is_prime = False
            break  # A factor is found, so the number is not prime
        divisor += 1
else:
    # If the number is less than or equal to 1, it is not prime
    is_prime = False

# Print if the number is prime or not
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
