# 32) Ask the user to enter their top three hobbies and then their top three foods. 
# Store these in two separate lists. Then, create a nested list that contains both lists and print it. 
# Finally, ask the user to select a number: 1 for hobbies or 2 for foods. 
# Based on their choice, print the corresponding list from the nested list.

# Ask the user to enter their top three hobbies
hobby1 = input("Enter your first hobby: ")
hobby2 = input("Enter your second hobby: ")
hobby3 = input("Enter your third hobby: ")

# Store the hobbies in a list
hobbies_list = [hobby1, hobby2, hobby3]

# Ask the user to enter their top three foods
food1 = input("Enter your first favorite food: ")
food2 = input("Enter your second favorite food: ")
food3 = input("Enter your third favorite food: ")

# Store the foods in a list
foods_list = [food1, food2, food3]

# Create a nested list that contains both lists
nested_list = [hobbies_list, foods_list]

# Print the nested list
print("Nested list:", nested_list)

# Ask the user to select a number: 1 for hobbies or 2 for foods
choice = input("Enter 1 for hobbies or 2 for foods: ")

# Print the corresponding list from the nested list
if choice == "1":
    print("Your hobbies are:", nested_list[0])
elif choice == "2":
    print("Your favorite foods are:", nested_list[1])
else:
    print("Invalid choice.")
