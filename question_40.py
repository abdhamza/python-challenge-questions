# 40) Write a Python program that takes a sentence from the user and reverses the order of the words in the sentence. 
# Use string methods to accomplish this. For example, if the input is "Python is easy to learn", the output should be 
# "learn to easy is Python".

# Take a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words, reverse the list of words, and join them back into a sentence
reversed_sentence = ' '.join(sentence.split()[::-1])

# Print the reversed sentence
print(reversed_sentence)
