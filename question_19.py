# 19) Ask the user to input a year. Use an if-else statement to determine if the year is a leap year or not. 
# A year is a leap year if it is divisible by 4, 
# except for years which are divisible by 100 unless they are also divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
