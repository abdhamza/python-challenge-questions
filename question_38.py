# 38) Write a Python program that asks the user for their email address and 
# then extracts and prints the domain of the email address. For example, 
# if the input is "user@example.com", the output should be "example.com".

# Ask the user for their email address
email_address = input("Enter your email address: ")

# Extract the domain from the email address
# Assuming the format is always user@domain
domain = email_address.split('@')[-1]

# Print the domain
print(f"The domain of your email address is: {domain}")
