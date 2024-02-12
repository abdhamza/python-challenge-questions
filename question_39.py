# 39) Ask the user to input a string and write a Python program to count how many vowels 
# (a, e, i, o, u) are in the string. Use string methods and consider both uppercase and 
# lowercase vowels. For example, if the input is "Hello World", the output should be 3.

# Ask the user to input a string
user_input = input("Enter a string: ")

# Convert the string to lowercase to make the search case-insensitive
lowercase_input = user_input.lower()

# Count each vowel separately using the count method and then sum them up
vowel_count = (lowercase_input.count('a') +
               lowercase_input.count('e') +
               lowercase_input.count('i') +
               lowercase_input.count('o') +
               lowercase_input.count('u'))

# Print the count of vowels
print(f"The number of vowels in the input string is: {vowel_count}")