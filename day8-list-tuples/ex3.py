marks=[30,40,50,60,70,80,90]
for i in range(5):
    mark = int(input(f"Enter marks{i+1}: "))
    marks.append (mark)
print("the marks entered are:", marks)
average = sum(marks) /5
maximum = max(marks)
minimum = min(marks)
print(f"the average is {average:.0f}")
print(f"the maximum is {maximum}")
print(f"the minimum is {minimum}")