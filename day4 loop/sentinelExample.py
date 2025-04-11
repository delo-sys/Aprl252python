proceed=True
totalExpenses=0
budgetAmount=float (input("Enter the amount that you have budgeted for this month"))
while proceed:
    expense=float(input("Enter the current expense "))
    totalExpenses=totalExpenses+expense
    respond= input("Do you wish to continue? enter Y(yes) or key(no)")
    if respond.lower()=='n':
        proceed=False
print(f" monthy budget minus total expenses is KSH {budgetAmount-totalExpenses:.2f}")
if over_the_budget:
    print("You have exceeded your budget")
else:under_the_budget
print("You are within your budget")