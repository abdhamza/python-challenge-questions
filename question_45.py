# 45) Modify the classic "Guess the Number" (question 42) game by setting a limit on how 
# close the guess must be to the actual number. The program picks a fixed number (say, 50), 
# and the user has unlimited guesses, but they must guess the number exactly or 
# within a range of +/- 5. The program should give feedback ("Too high", "Too low", or "Close enough") 
# until the user guesses correctly or within the allowed range.

# Set the fixed target number
target_number = 50

# Start an infinite loop for unlimited guesses
while True:
    # Ask the user to make a guess
    user_guess = int(input("Guess a number: "))
    
    # Calculate the difference between the guess and the target number
    difference = abs(target_number - user_guess)
    
    # Check if the guess is exactly right or within the allowed range
    if difference == 0:
        print("Congratulations! You guessed the number correctly.")
        break
    elif difference <= 5:
        print("Close enough! You're within the allowed range.")
        break
    # Provide feedback if the guess is too high or too low
    elif user_guess < target_number:
        print("Too low")
    else:
        print("Too high")
