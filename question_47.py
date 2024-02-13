# 47) Implement a program that asks the user for a string and uses a while loop to 
# reverse the string without using string slicing or reversed methods.

# Ask the user for a string
user_string = input("Enter a string: ")

# Initialize an empty string to hold the reversed string
reversed_string = ''

# Initialize an index to the last character of the user_string
index = len(user_string) - 1

# Use a while loop to reverse the string
while index >= 0:
    reversed_string += user_string[index]
    index -= 1

# Print the reversed string
print("Reversed string:", reversed_string)
