total_budget = 0
max_budget=0
best_month=1
for counter in range(1,12):
    month_budget = float(input(f"Enter sales for day {counter}: "))
    total_budget = total_budget + month_budget
    if month_budget > max_budget:
        max_budget = month_budget
        best_month = counter
print(f"Total sales for the week KSH: {total_budget:.2f}")
print(f"the best day was day-{best_month}with sales of : {max_budget:.2f}")