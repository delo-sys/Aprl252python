with open(r'C:\Users\Student\Documents\Aprl252python\day13-file handling\employee.txt', 'w') as file:
    for i in range(1,6):
        print(f"Enter details for employee {i}:")
        name = input("Enter employee name: ")
        salary = input("Enter employee salary: ")
        date_of_birth = input("Enter employee date of birth: ")
        email = input("Enter employee email: ")
        file.write(f"Employee {i}: {name}, Salary: {salary} , date_of_brith:{date_of_birth} , Email{email}\n")
        print(f"Details for employee {i} saved successfully.\n")
file.close()