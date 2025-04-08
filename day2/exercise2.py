# Program to calculate state and county sales tax

# Constants for tax rates
STATE_TAX_RATE = 0.05  # 5%
COUNTY_TAX_RATE = 0.025  # 2.5%

# Get the amount of purchase from the user
amount_of_purchase = float(input("Enter the amount of the purchase: "))

# Calculate state sales tax
state_sales_tax = amount_of_purchase * STATE_TAX_RATE

# Calculate county sales tax
county_sales_tax = amount_of_purchase * COUNTY_TAX_RATE

# Calculate total sales tax
total_sales_tax = state_sales_tax + county_sales_tax

# Calculate total sale amount
total_sale = amount_of_purchase + total_sales_tax

# Display the results
print("\n--- Sales Tax Breakdown ---")
print(f"Amount of purchase: ${amount_of_purchase:.2f}")
print(f"State sales tax: ${state_sales_tax:.2f}")
print(f"County sales tax: ${county_sales_tax:.2f}")
print(f"Total sales tax: ${total_sales_tax:.2f}")
print(f"Total of the sale: ${total_sale:.2f}")