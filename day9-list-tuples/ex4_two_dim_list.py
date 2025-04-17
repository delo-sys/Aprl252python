# 2 dim lists conist of rows and columns
marks=[[70,80,80], 
[60,70,95],
[50,60,87],
[62,78,90]] 
# print(marks[1][2])
# print(marks[3][2])

total=0
for row in marks:
    for mark in row:
        total+=mark
print(f"the total marks is {total:.2f}")
print(f"the overall average is {total/12:.2f}")

for i in range(len(marks)):
    row_total = sum(marks[i])
    row_average = row_total / len(marks[i])
    print(f"Row {i+1} Average: {row_average:.2f}")

num_cols = len(marks[0])
for j in range(num_cols):
    col_total = 0
    for i in range(len(marks)):
        col_total += marks[i][j]
    col_average = col_total / len(marks)
    print(f"Column {j+1} Average: {col_average:.2f}")