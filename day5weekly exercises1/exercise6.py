sub_total=0
sales_tax=0.07
item1_price= float(input("enter items 1 price"))
item2_price= float(input("enter items 2 price"))
item3_price= float(input("enter items 3 price"))
item4_price= float(input("enter items 4 price"))
item5_price= float(input("enter items 5 price"))
total_sub_total=(item1_price+item2_price+item3_price+item4_price+item5_price)
total_sales_tax=(total_sub_total*sales_tax)
total=(total_sales_tax+total_sub_total)
print()
print(total_sub_total)
print(total_sales_tax)
print(total)
