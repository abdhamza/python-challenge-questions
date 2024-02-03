# 21) Write a program that converts a temperature from Fahrenheit to Celsius. 
# Classify the temperature as 'Freezing' (< 0°C), 'Cold' (0-15°C), 'Moderate' (15-25°C), 'Warm' (25-35°C), and 'Hot' (>35°C) 
# using only if-else statements.


# Input: Temperature in Fahrenheit
temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9

# Classification using only if-else statements
if temperature_celsius < 0:
    classification = "Freezing"
else:
    if temperature_celsius < 15:
        classification = "Cold"
    else:
        if temperature_celsius < 25:
            classification = "Moderate"
        else:
            if temperature_celsius < 35:
                classification = "Warm"
            else:
                classification = "Hot"

# Output the result
print(f"The temperature is {temperature_celsius:.2f}°C, which is classified as {classification}.")
