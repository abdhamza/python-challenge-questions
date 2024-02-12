# 2) Write a program that asks the user for the diameter of a sphere and then computes the volume and surface area. 
# Use the value of 𝜋, i.e., 3.142, as a constant.

# Constant for the value of pi
PI = 3.142
# Ask the user for the diameter of the sphere
diameter = float(input("Enter the diameter of the sphere: "))
# Calculate the radius of the sphere
radius = diameter / 2
# Calculate the volume of the sphere
volume = (4/3) * PI * (radius ** 3)
# Calculate the surface area of the sphere
surface_area = 4 * PI * (radius ** 2)
# Print the results
print("Volume of the sphere:", volume)
print("Surface area of the sphere:", surface_area)
