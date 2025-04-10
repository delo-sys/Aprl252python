
age = int(input("Enter the person's age: "))
if age < 0:
    print("Error! Age cannot be negative.")

if age < 2:
    print("The person is an infant.")

elif 2 <= age < 13:
    print("The person is a child.")

elif 13 <= age < 20:
    print("The person is a teenager.")

else:
    print("The person is an adult.")