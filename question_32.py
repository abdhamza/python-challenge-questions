# 32) Write a program that starts with a list of two items: ["Hello", "World"]. 
# Ask the user to add three more words to the list, entering them one at a time. 
# After adding each word, print the current state of the list.

# Start with a list of two items
words_list = ["Hello", "World"]

# Ask the user to add three more words to the list, entering them one by one
new_word1 = input("Enter word 1: ")
words_list.append(new_word1)
print("Current state of the list:", words_list)

new_word2 = input("Enter word 2: ")
words_list.append(new_word2)
print("Current state of the list:", words_list)

new_word3 = input("Enter word 3: ")
words_list.append(new_word3)
print("Current state of the list:", words_list)
