def main():
    loan_payment = float(input("Enter the monthly loan payment: "))
    insurance = float(input("Enter the monthly insurance cost: "))
    gas = float(input("Enter the monthly gas cost: "))
    oil = float(input("Enter the monthly oil cost: "))
    tires = float(input("Enter the monthly tires cost: "))
    maintenance = float(input("Enter the monthly maintenance cost: "))

    total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    total_annual_cost = total_monthly_cost * 12

    print("\nTotal Monthly Cost: ${:.2f}".format(total_monthly_cost))
    print("Total Annual Cost: ${:.2f}".format(total_annual_cost))
if __name__ == "__main__":
    main()