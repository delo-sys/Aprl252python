for i in range(1,5):
    print(f"Enter marks for student #{i}#")
    for j in range (1,4):
        marks=int(input(f"Enter marks for subject #{j}"))
    average=marks/3
    print(f"Average marks for student {i} is {average:.2f}")