# 9) Given three variables (num1, num2, and num3) entered by the user, write a program that checks if:
# num1 < num2 and num2 >= num3
# num1 > num2 or num1 >num3
# num2 >= num1 and num1 != num3

# Take input of three variables from the user
num1 = float(input("Enter the value of num1: "))
num2 = float(input("Enter the value of num2: "))
num3 = float(input("Enter the value of num3: "))

# Check if num1 < num2 and num2 >= num3
condition1 = num1 < num2 and num2 >= num3
print(f"num1 < num2 and num2 >= num3: {condition1}")

# Check if num1 > num2 or num1 > num3
condition2 = num1 > num2 or num1 > num3
print(f"num1 > num2 or num1 > num3: {condition2}")

# Check if num2 >= num1 and num1 != num3
condition3 = num2 >= num1 and num1 != num3
print(f"num2 >= num1 and num1 != num3: {condition3}")
