def rect_area(length, width):
    return length * width

def rec_perimeter(length, width):
    return 2 * (length + width)

length = float(input("Enter the length of the rectangle:"))
width = float(input("Enter the width of the rectangle:"))

print(f"The area of the rectangle is: {rect_area(length, width)}")
print(f"The perimeter of the rectangle is: {rec_perimeter(length, width)}")