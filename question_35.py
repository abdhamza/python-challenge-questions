# 35) You have a string data = "name:John Doe;age:30;profession:Software Engineer". 
# Split this string into individual components based on the semicolon (;) and 
# then create a list where each element is a key-value pair (as a string) derived from the components. 
# Finally, join these key-value pairs using a comma and a space. What is the final string?

data = "name:John Doe;age:30;profession:Software Engineer"

# Split the string into individual components based on the semicolon (;)
components = data.split(';')

# Create a list where each element is a key-value pair (as a string) derived from the components
key_value_pairs = list(map(str.strip, components))

# Join these key-value pairs using a comma and a space
final_string = ", ".join(key_value_pairs)

print(final_string)

