#28) Write a program that asks the user to enter three favorite colors, one by one. 
# Store these colors in a list. Then, print the first and last color entered.

# Ask the user to enter their three favorite colors, one by one
color1 = input("Enter your first favorite color: ")
color2 = input("Enter your second favorite color: ")
color3 = input("Enter your third favorite color: ")

# Store the colors in a list
favorite_colors = [color1, color2, color3]

# Print the first and last color entered
print("Your first favorite color is:", favorite_colors[0])
print("Your last favorite color is:", favorite_colors[-1])
