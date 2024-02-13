# 14) If your bike uses 3 liters of fuel per 100 km and fuel costs 262 rupees per liter, how much will the fuel cost for a 400 km trip? write a python code for that.

# Bike's fuel consumption and fuel cost
fuel_consumption_per_100km = 3  # liters per 100 km
cost_per_liter = 262  # rupees per liter

# Distance of the trip
distance_km = 400

# Calculate the total liters of fuel needed for the trip
total_liters_needed = (distance_km / 100) * fuel_consumption_per_100km

# Calculate the total fuel cost
total_fuel_cost = total_liters_needed * cost_per_liter

# Print the total fuel cost
print(f"The total fuel cost for a {distance_km} km trip is: {total_fuel_cost} rupees")
