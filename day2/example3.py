def calculate_km_per_liter(distance_km, fuel_liters):
    """Calculates kilometers per liter."""
    if fuel_liters == 0:
        return "Error: Fuel consumption cannot be zero."
    return distance_km / fuel_liters

# Get input from the user (optional)
distance = float(input("Enter the distance traveled in kilometers: "))
fuel = float(input("Enter the amount of fuel consumed in liters: "))

# Calculate and print the result
result = calculate_km_per_liter(distance, fuel)
print(f"Kilometers per liter: {result:.2f} km/l")