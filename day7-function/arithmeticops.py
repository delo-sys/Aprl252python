def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    if y !=0:
        return x / y
    else:
        print("Error division by zero is not possible")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = addition(num1, num2)
print(f"The sum is {result}")
result = subtraction(num1, num2)
print(f"The difference is {result}")
result = multiplication(num1, num2)
print(f"The product is {result}")
result = division(num1, num2)
print(f"The quotient is {result}")