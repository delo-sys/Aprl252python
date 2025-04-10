marks = int(input("Enter marks percentage marks scored "))
if marks > 100 or marks < 0:
    print("error !!! enter valid mark 0-100%")

if marks >= 70 and marks <= 100:
    print("Grade is A")
elif marks >= 60 and marks < 70:
    print("Grade is B")
elif marks >= 50 and marks < 60:
    print("Grade is C")
elif marks >= 40 and marks < 50:
    print("Grade is D")
elif marks >= 30 and marks < 40:
    print("Grade is E")