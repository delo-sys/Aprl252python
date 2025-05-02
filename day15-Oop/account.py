class Account :
    def __init__(self, accNo,accname,accbalance):
        self.acc_no = accNo
        self.acc_name = accname
        self.accbalance = accbalance
    def deposit(self, amount):
        if amount < 0:
            print("error amount should be > 0")
        else:
            self.accbalance = self.accbalance + amount
            print(f"Deposit of {amount} successful")

    def withdraw(self,amount):
        if amount > self.accbalance:
            print("Insufficient balance")
        else:
            self.accbalance = self.accbalance - amount
            print(f"Withdraw of {amount:2f} successful")
    def get_balance(self):
        return self.accbalance

def get_menuchoice():
    print()
    print("bank account menu")
    print("*****************")
    print("1. show the balance")
    print("2. add a account")
    print("3. deposit a contact")
    print("4. withdraw a contacts")
    print("5. quit the program")

    choice = int(input("Enter your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input("Please enter valid choice(1-5): "))
            
    return choice

def balance(acc):
    print(f"Your balance is {acc.get_balance()}")

def add(acc):
    print("Add a new account")
    while True:
        try:
            accNo = int(input("Enter the account number: "))
            break
        except ValueError:
            print("Please enter a valid integer for the account number.")
    accname = input("Enter the account name: ")
    while True:
        try:
            accbalance = float(input("Enter the account balance: "))
            break
        except ValueError:
            print("Please enter a valid number for the account balance.")
    new_account = Account(accNo, accname, accbalance)
    print(f"Account {new_account.acc_name} added successfully.")
    return new_account

def deposit(acc):
    amount = float(input("Enter the amount to deposit: "))
    acc.deposit(amount)
    print(f"Deposit of {amount} successful")

def withdraw(acc):
    amount = float(input("Enter the amount to withdraw: "))
    acc.withdraw(amount)
    print(f"Withdraw of {amount} successful")

def main():
    Account = None  # Start with no account
    choice = 0
    while choice != 5:
        choice = get_menuchoice()
        if choice == 1:
            if Account:
                balance(Account)
            else:
                print("No account found. Please add an account first.")
        elif choice == 2:
            Account = add(Account)
        elif choice == 3:
            if Account:
                deposit(Account)
            else:
                print("No account found. Please add an account first.")
        elif choice == 4:
            if Account:
                withdraw(Account)
            else:
                print("No account found. Please add an account first.")
main()