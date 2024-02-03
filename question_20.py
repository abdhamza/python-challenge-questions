# 20) Write a Python program that categorizes a person's age into 'Child' (< 13), 'Teen' (13-19), 
# 'Adult' (20-59), and 'Senior' (60 and above) using only if-else statements (no elif allowed).

# Input: Age of the person
age = int(input("Enter your age: "))

# Using only if-else statements to categorize age
if age < 0:
    print("invalid age")
else:
    if age < 13:
        print("You are a Child.")
    else:
        if age < 20:
            print("You are a Teen.")
        else:
            if age < 60:
                print("You are an Adult.")
            else:
                print("You are a Senior.")
            

