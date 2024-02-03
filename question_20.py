# 20) Write a program that simulates a traffic light. The user enters a color ('red', 'yellow', 'green'), and the program 
# prints 'Stop' for red, 'Caution' for yellow, and 'Go' for green using only if-else statements.

# Input: Color of the traffic light
color = input("Enter the color of the traffic light (red, yellow, green): ").lower()

# Using only if-else statements to determine the action
if color == 'red':
    print("Stop")
else:
    if color == 'yellow':
        print("Caution")
    else:
        if color == 'green':
            print("Go")
        else:
            print("Invalid color")
