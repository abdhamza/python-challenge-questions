# 37) Ask the user to input a word, and write a Python program to check if the word is a palindrome. 
# A palindrome is a word that reads the same backward as forward, e.g., "racecar". 
# Ignore case sensitivity and spaces.

# Ask the user to input a word
word = input("Enter a word: ")

# Remove spaces and convert to lowercase for comparison
clean_word = word.replace(" ", "").lower()

# Check if the word is a palindrome
if clean_word == clean_word[::-1]:
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')
