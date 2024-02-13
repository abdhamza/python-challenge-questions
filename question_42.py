# 42) Implement a "Guess the Number" game in Python where the target number is set to a fixed value within the program (for example, 42). 
# The user has to guess this fixed number. The program should provide hints like "Too high" or "Too low" based on the user's guesses. 
# Use a while loop to keep the game going until the correct guess is made. The game ends when the user correctly guesses the number, 
# and the program should congratulate the user.

# Setting fixed target number
target_number = 42

# Initialize a variable to store the user's guess
user_guess = None

# Use a while loop to let the user guess until they get it right
while user_guess != target_number:
    # Ask the user to enter their guess
    user_guess = int(input("Guess a number between 1 and 100: "))
    
    # Provide hints
    if user_guess < target_number:
        print("Too low")
    elif user_guess > target_number:
        print("Too high")

# Congratulate the user once they guess correctly
print("Congratulations! You guessed the number correctly.")
