purchases= float(input("Enter the amount of the purchase: "))
if (purchases>=5000):
    discount=purchases*0.05
    print(f"discount is ksh {discount}")
else:    
    discount=purchases*0
    print(f"discount is ksh {discount}")

print("END of program")