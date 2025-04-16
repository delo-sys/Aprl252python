friends=["Anna","Bob","Charlie","David","Eva","Frank","Grace","Hannah"]
fruits= list(("apple","banana","cherry","date","elderberry","fig","grape","honeydew"))
prices=[34.99, 24.99, 29.99, 10, 20, 30, 40, 50]

# print(friends[3])
# print(friends[8])

for friend in friends:
    print(friend)

total=0
for price in prices:
    total=total+price
print(f"Total price: KSH {total:.2f}")
average=total/3
print(f"Average price: KSH {average:.2f}")

print(f"total price: KSH{sum(prices):.2f}")

