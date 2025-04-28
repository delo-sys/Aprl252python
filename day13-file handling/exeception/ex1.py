try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a  second number: "))
    print(f"the quotient is {num1/num2}")
except ZeroDivisionError:
    print("division by zero is not possible")
except ValueError:
    print("enter integer values")
except Exception:
    print("an error occurred")
print("End of program")