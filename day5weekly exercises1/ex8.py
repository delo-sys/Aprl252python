days = int(input("Enter days of week "))
if days>7 or days<0:
    print("error !!! enter valid days")

if days>1:
    print("monday")
elif days>2: 
    print("Tuesday")
elif days>3:
    print("Wednesday")
elif days>4: 
    print("Thursday")
elif days>5:
    print("Friday")
elif days>6:
    print("saturday")
elif days>7:
    print("sunday")