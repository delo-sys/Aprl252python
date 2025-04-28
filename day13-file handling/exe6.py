with open(r"C:\Users\Student\Documents\Aprl252python\day13-file handling\sales_numbers.txt", 'w') as file:
    total=0
    for i in range(1, 8):
        print(f"Enter sales number {i}:")
        sales_number = input("Enter sales number: ")
        total += int(sales_number)
        file.write(f"Sales number {i}: {sales_number},\n")
        print(f"Sales number {i} saved successfully.\n")
print(f"total:{total}\n")