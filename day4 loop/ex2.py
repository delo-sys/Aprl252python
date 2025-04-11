### 
total_sales = 0
max_sales=0
best_day=1
for counter in range(1,8):
    day_sales = float(input(f"Enter sales for day {counter}: "))
    total_sales = total_sales + day_sales
    if day_sales > max_sales:
        max_sales = day_sales
        best_day = counter
print(f"Total sales for the week KSH: {total_sales:.2f}")
print(f"the best day was day-{best_day}with sales of : {max_sales:.2f}")