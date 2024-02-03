# 17) Write a program where a user enters a number. 
# Use an if-else structure to check whether the number is positive, negative, or zero and print the result.


number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print(f"The number is Zero")