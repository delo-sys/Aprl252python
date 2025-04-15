def distance_to_miles(kilometers):
    miles = kilometers * 0.6214
    return (kilometers, miles)
def main():
    km = float(input("Enter the distance in kilometers: "))
    km, miles = distance_to_miles(km)
    print(f"{km} kilometers is equal to {miles:.0f} miles.")
main()