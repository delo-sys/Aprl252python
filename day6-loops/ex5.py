total = 0
for counter in range(1,11):
    price = float(input(f"Enter item price{counter}\n"))
    while price<0:#using a while loop for input validation
        print("Please enter a positive number.>=0")
        price=float(input(f"Enter item price{counter}\n"))
    total = total+price
print(f"Total price for ten items is {total:.2f}")