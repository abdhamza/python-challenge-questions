# 29) Ask the user to create a list of four numbers by entering them one at a time. 
# After the list is created, ask the user for a number to add to the list, 
# but they must also specify the position (index) in the list where this 
# new number should be placed, replacing the existing number at that position. 
# Print the updated list.

# Ask the user to enter four numbers, one by one
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# Create a list of the numbers
numbers_list = [num1, num2, num3, num4]

# Ask the user for a new number and the position to insert it
new_number = int(input("Enter a new number to add to the list: "))
position = int(input("Specify the position (0-3) where the new number should be placed: "))

# Replace the number at the specified position with the new number
# Check if the position is within the valid range
if 0 <= position < len(numbers_list):
    numbers_list[position] = new_number
    print("Updated list:", numbers_list)
else:
    print("Invalid position. The list has not been updated.")
