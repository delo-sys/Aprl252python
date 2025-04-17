prices=[100, 200, 250, 55, 500]

# new_prices = []  # should have 10 percent increment of prices
# for price in prices:
#    np=price * 1.1
#    new_prices.append(np)

newprices = [f"{(price * 1.1):.2f}" for price in prices] # list comprehension

print("oldpirces"+str(prices))
print("newprices"+str(newprices))

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqlnumbers = [num**2 for num in numbers] # list comprehension with condition
print("sqlnumbers"+str(sqlnumbers))

evennumbers = [num for num in numbers if num % 2 == 0]
print("evennumbers"+str(evennumbers))