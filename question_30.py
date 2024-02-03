# 30) Create a program where the user enters five movie names to store in a list. After the list is created, ask the user for a movie name to remove from the list. 
# Remove the movie by directly specifying its value (not by index, since you haven't learned loops for finding indexes). Print the updated list.

# Ask the user to enter five movie names, one by one
print("Enter five movie names:")
movie1 = input("Movie 1: ")
movie2 = input("Movie 2: ")
movie3 = input("Movie 3: ")
movie4 = input("Movie 4: ")
movie5 = input("Movie 5: ")

# Create a list of the movie names
movies_list = [movie1, movie2, movie3, movie4, movie5]

# Ask the user for a movie name to remove from the list
movie_to_remove = input("Enter the name of the movie you want to remove from the list: ")

# Remove the movie by specifying its value
# Use a try-except block to handle the case where the movie is not in the list
try:
    movies_list.remove(movie_to_remove)
    print("Updated list:", movies_list)
except ValueError:
    print("The movie is not in the list.")

# Print the updated list
print("Final movie list:", movies_list)
