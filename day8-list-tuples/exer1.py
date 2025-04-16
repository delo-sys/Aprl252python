sales = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days:
    sale = float(input(f"Enter the sales for {day}: "))
    sales.append(sale)
total_sales = sum(sales)
print(f"The total sales for the week are: KSH {total_sales:.2f}")