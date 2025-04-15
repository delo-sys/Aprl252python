def main():
    try:
        replacement_cost = float(input("Enter the replacement cost of the building: $"))
        
        minimum_insurance = replacement_cost * 0.126
        print(f"The minimum amount of insurance you should buy for the property is: ${minimum_insurance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    main()